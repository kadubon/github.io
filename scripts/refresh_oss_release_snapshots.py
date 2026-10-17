#!/usr/bin/env python3
"""Explicit network refresh of public GitHub release/source observations.

Uses authenticated gh if available. Never executes repository code. A failed
request retains the previous observation and marks its refresh stale.
"""
import argparse
import concurrent.futures
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'data/oss-release-snapshots.json'


def request(endpoint):
    for attempt in range(3):
        result = subprocess.run(['gh', 'api', endpoint], capture_output=True,
                                text=True, encoding='utf-8', timeout=40)
        if result.returncode == 0:
            return json.loads(result.stdout)
        if '404' in result.stderr:
            return None
        if attempt < 2:
            time.sleep(2 ** attempt)
    raise RuntimeError('GitHub request failed after bounded retries')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--selected-only', action='store_true',
                        help='Refresh only software already selected by the collective index')
    args = parser.parse_args()
    old = json.loads(PATH.read_text(encoding='utf-8')) if PATH.exists() else {'repositories': {}}
    repos = json.loads((ROOT / 'oss-catalog.json').read_text(encoding='utf-8'))['repositories']
    if args.selected_only:
        curated = json.loads((ROOT / 'data/collective-intelligence-curation.json').read_text(encoding='utf-8'))
        selected = {r['source_catalog_id'] for r in curated['resources'] if r['kind'] == 'software'}
        repos = [r for r in repos if r['full_name'] in selected]
    observed = datetime.now(timezone.utc).isoformat(timespec='seconds')

    def inspect(repo):
        name = repo['name']
        try:
            release = request(f'repos/{repo["full_name"]}/releases/latest')
            commit = request(f'repos/{repo["full_name"]}/commits/{repo["default_branch"]}')
            if commit is None:
                raise RuntimeError('Default branch unavailable')
            value = {
                'observed_at': observed, 'refresh_status': 'current',
                'default_branch_revision': commit['sha'],
                'source_url': repo['repository_url'],
                'latest_release': None if release is None else {
                    'tag': release['tag_name'], 'url': release['html_url'],
                    'published_at': release['published_at'],
                    'assets': [a['browser_download_url'] for a in release.get('assets', [])],
                },
                'release_status': 'no_published_github_release' if release is None else 'observed',
                # A GitHub refresh cannot renew or erase a separately dated package observation.
                'package_registry_status': old['repositories'].get(name, {}).get(
                    'package_registry_status', 'not_checked_by_this_github_refresh'),
            }
        except (RuntimeError, subprocess.TimeoutExpired) as error:
            value = dict(old['repositories'].get(name, {}))
            value.update(refresh_status='stale', refresh_attempted_at=observed,
                         refresh_error=str(error))
        return name, value

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        refreshed = dict(pool.map(inspect, repos))
    values = dict(old['repositories']) if args.selected_only else {}
    values.update(refreshed)
    PATH.parent.mkdir(exist_ok=True)
    PATH.write_text(json.dumps({'schema_version': '1.0', 'repositories': values},
                              ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    stale = [name for name, value in refreshed.items() if value['refresh_status'] != 'current']
    print(f'Observed {len(refreshed)} repositories; stale: {stale}')
    return bool(stale)


if __name__ == '__main__':
    raise SystemExit(main())

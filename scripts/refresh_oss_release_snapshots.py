#!/usr/bin/env python3
"""Explicit network refresh of public GitHub release/source observations.

Uses authenticated gh if available. Never executes repository code. A failed
request retains the previous observation and marks its refresh stale.
"""
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
    old = json.loads(PATH.read_text(encoding='utf-8')) if PATH.exists() else {'repositories': {}}
    repos = json.loads((ROOT / 'oss-catalog.json').read_text(encoding='utf-8'))['repositories']
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
                'package_registry_status': 'not_checked_by_this_github_refresh',
            }
        except (RuntimeError, subprocess.TimeoutExpired) as error:
            value = dict(old['repositories'].get(name, {}))
            value.update(refresh_status='stale', refresh_attempted_at=observed,
                         refresh_error=str(error))
        return name, value

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        values = dict(pool.map(inspect, repos))
    PATH.parent.mkdir(exist_ok=True)
    PATH.write_text(json.dumps({'schema_version': '1.0', 'repositories': values},
                              ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    stale = [name for name, value in values.items() if value['refresh_status'] != 'current']
    print(f'Observed {len(values)} repositories; stale: {stale}')
    return bool(stale)


if __name__ == '__main__':
    raise SystemExit(main())

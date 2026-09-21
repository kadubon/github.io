#!/usr/bin/env python3
"""Explicit HTTP checks, separate from offline generation and validation.

Compares served bytes with the checked-out files. Origin robots is observed,
never edited. External failures distinguish missing from unavailable/uncertain.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import subprocess
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

import generate_collective_intelligence_index as gen
from validate_collective_intelligence_index import Document


def fetch(url, head=False):
    try:
        request = Request(url, method='HEAD' if head else 'GET', headers={'User-Agent': 'CollectiveIndexPublicationCheck/1.0'})
        with urlopen(request, timeout=25) as response:
            data = b'' if head else response.read(5_000_000)
            return {'url': url, 'status': response.status, 'final_url': response.url,
                    'content_type': response.headers.get('Content-Type'),
                    'classification': 'accessible', 'sha256': hashlib.sha256(data).hexdigest()}, data
    except HTTPError as error:
        classification = 'missing' if error.code in (404, 410) else 'unavailable_or_uncertain'
        return {'url': url, 'status': error.code, 'classification': classification}, b''
    except (URLError, TimeoutError, OSError) as error:
        return {'url': url, 'status': None, 'classification': 'unavailable_or_uncertain',
                'error_type': type(error).__name__}, b''


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url', default=gen.BASE)
    p.add_argument('--external', action='store_true')
    p.add_argument('--report', required=True)
    args = p.parse_args()
    base = args.base_url.rstrip('/') + '/'
    files = list(gen.FORMATS) + ['index.html', 'agent-index.json', 'sitemap.xml', 'oss.html',
                                'docs/collective-intelligence-index-maintenance.md']
    # Include every linked site-local destination under a correctly mounted prefix.
    for lang in ('en', 'ja'):
        raw = (gen.ROOT / (gen.STEM + ('.ja' if lang == 'ja' else '') + '.html')).read_text(encoding='utf-8')
        for url in Document(raw).links:
            if url.startswith(gen.BASE):
                name = urlsplit(url).path[len('/github.io/'):]
                files.append(name + 'index.html' if not name or name.endswith('/') else name)
    def check(name):
        result, data = fetch(base + name)
        result['file'] = name
        expected = (subprocess.check_output(['git', 'show', 'HEAD:' + name], cwd=gen.ROOT)
                    if base == gen.BASE else (gen.ROOT / name).read_bytes())
        result['bytes_match_checkout'] = data == expected
        result['comparison_source'] = 'committed Git blob (canonical LF)' if base == gen.BASE else 'working-tree file'
        result['utf8_decodable'] = True
        try:
            data.decode('utf-8')
        except UnicodeDecodeError:
            result['utf8_decodable'] = False
        return result
    with ThreadPoolExecutor(max_workers=4) as pool:
        local = list(pool.map(check, sorted(set(files))))
    report = {'checked_at': datetime.now(timezone.utc).isoformat(), 'base_url': base, 'site_files': local}
    if base == gen.BASE:
        origin, body = fetch('https://kadubon.github.io/robots.txt')
        origin['body'] = body.decode('utf-8', errors='replace')[:8000]
        project, body = fetch(gen.BASE + 'robots.txt')
        project['body'] = body.decode('utf-8', errors='replace')[:8000]
        report['robots'] = {'origin': origin, 'project': project,
                            'scope': 'Only origin-root robots sets origin-wide policy; account-root repository was not modified.'}
    if args.external:
        urls = set()
        for lang in ('en', 'ja'):
            raw = (gen.ROOT / (gen.STEM + ('.ja' if lang == 'ja' else '') + '.html')).read_text(encoding='utf-8')
            urls.update(u for u in Document(raw).links if u.startswith('https://') and not u.startswith(gen.BASE))
        with ThreadPoolExecutor(max_workers=3) as pool:
            report['external'] = list(pool.map(lambda u: fetch(u, head=True)[0], sorted(urls)))
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    failed = [r['file'] for r in local if r['status'] != 200 or not r['bytes_match_checkout'] or not r['utf8_decodable']]
    print(f'Checked {len(local)} served local destinations; failures: {failed}')
    if args.external:
        from collections import Counter
        print('External:', dict(Counter(r['classification'] for r in report['external'])))
    return bool(failed)


if __name__ == '__main__':
    sys.exit(main())

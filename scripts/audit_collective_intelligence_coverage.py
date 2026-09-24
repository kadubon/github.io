#!/usr/bin/env python3
"""Offline lexical acceptance diagnostic; not ranking, relevance or adoption evidence."""
import argparse
from collections import Counter
import json

import generate_collective_intelligence_index as gen

REPORT = 'docs/collective-intelligence-coverage.md'
SEEDS = 'data/collective-intelligence-coverage-seeds.json'


def audit(model, fixture=None):
    fixture = fixture or gen.read(SEEDS)
    gen.query_index(model)  # Ambiguous aliases are errors, never first-match wins.
    rows = []; ids = set(); queries = {lang: set() for lang in ('en', 'ja')}
    problems = {p['id'] for p in model['problems']}
    for seed in fixture['seeds']:
        if seed['id'] in ids:
            raise ValueError('Duplicate seed ID')
        ids.add(seed['id'])
        expected = seed['expected_problem_id']
        if expected is not None and expected not in problems:
            raise ValueError('Dangling seed expectation')
        if expected is None and not seed['unresolved_reason']:
            raise ValueError('Unresolved seed needs a reason')
        actual = {}
        for lang in ('en', 'ja'):
            q = gen.normalize_query(seed['query'][lang])
            if not q or q in queries[lang]:
                raise ValueError('Empty or duplicate seed query')
            queries[lang].add(q)
            match = gen.route(model, seed['query'][lang])
            actual[lang] = match['id'] if match else None
        rows.append({**seed, 'actual': actual,
                     'matches_expectation': all(v == expected for v in actual.values())})
    return rows


def report(model, fixture=None):
    fixture = fixture or gen.read(SEEDS)
    rows = audit(model, fixture)
    lines = ['# Collective Intelligence routing coverage / 経路カバレッジ', '',
             'Offline, deterministic lexical acceptance diagnostic for the supplied A–O seed families.',
             '語句の到達性を測る保守診断。検索順位・検索意図全般の精度・クローラー採用・科学的妥当性の証拠ではない。', '',
             'An exact declared alias can lead to a bounded diagnostic route, not necessarily an implementation of the searched feature. Read each route’s unsupported and stop conditions.',
             '一致は限定的な診断経路への入口であり、検索された機能の実装を保証しない。未対応条件・停止条件を参照。', '',
             f"Baseline registry: `{fixture['baseline_commit']}`; baseline matching was casefold/trim over legacy queries and IDs only.",
             'Baseline values are frozen measured observations, not a second operational routing table.', '',
             '| Family | Seeds per language | Baseline EN / JA | Current EN / JA | Unresolved EN / JA |',
             '|---|---:|---:|---:|---:|']
    for family in sorted({r['family'] for r in rows}):
        rs = [r for r in rows if r['family'] == family]
        baseline = [sum(r['baseline_problem_ids'][lang] is not None for r in rs) for lang in ('en', 'ja')]
        current = [sum(r['actual'][lang] is not None for r in rs) for lang in ('en', 'ja')]
        lines.append(f'| {family} | {len(rs)} | {baseline[0]} / {baseline[1]} | {current[0]} / {current[1]} | {len(rs)-current[0]} / {len(rs)-current[1]} |')
    lines += ['', '## All seed queries / 全シード', '', '| ID | EN | JA | EN route | JA route | Expected result |', '|---|---|---|---|---|---|']
    def cell(s):
        return gen.md_text(s).replace('|', '\\|').replace('\n', ' ')
    for r in rows:
        route_ids = [r['actual'][lang] or 'UNRESOLVED' for lang in ('en', 'ja')]
        lines.append('| ' + ' | '.join([r['id'], cell(r['query']['en']), cell(r['query']['ja']), *route_ids, 'PASS' if r['matches_expectation'] else 'FAIL']) + ' |')
    lines += ['', '## Explicit gaps / 未解決', '']
    for r in rows:
        if r['expected_problem_id'] is None:
            lines += ['- ' + r['id'] + ': ' + cell(r['query']['en']) + ' / ' + cell(r['query']['ja']),
                      '  ' + cell(r['unresolved_reason']['en']) + ' ' + cell(r['unresolved_reason']['ja'])]
    lines += ['', '## Interpretation / 解釈', '',
              'The original 12 routes covered research concepts such as verification, reuse and accounting, but these practical seed phrases were not exact aliases. The expanded 27 routes retain those IDs and add practical questions in eight groups. This is an explicit curated vocabulary, not open-ended natural-language understanding.',
              '旧12経路は検証・再利用・計上などを扱っていたが、この実務シード群の表現は一致語として登録されていなかった。既存IDを保持し、8群・27経路へ拡張した。自由文全般の理解ではなく、明示的に選定した語彙である。', '',
              'Tool search, incident containment and security routes expose evidence/host obligations, not a new MCP search service, universal kill switch, OAuth implementation, attack immunity or production guarantee.',
              'ツール探索・事故封じ込め・安全性の経路は根拠とホストの義務を示す。MCP検索サービス、万能停止装置、OAuth実装、攻撃耐性保証、本番保証を新設したものではない。', '']
    lines += ['## Additional source review / 追加ソースレビュー', '',
              'Source inspection only; no indexed software was installed or executed. These six supporting resources add bounded evidence, not tested interoperability. No papers or bibliography identities were added.',
              'ソース確認のみ。対象OSSの導入・実行は行っていない。6件は補助資料として追加し、検証済み相互運用を主張しない。論文・書誌IDの追加はない。', '']
    for r in model['resources']:
        if r['id'] not in ('sw-cmgl', 'sw-memoryflow', 'sw-pfg', 'sw-fost', 'sw-atrb', 'sw-oversight'):
            continue
        sw = r['software']
        lines += ['### ' + r['name'], '',
                  f"- Revision: [{sw['source_revision']}]({r['canonical_url']}/tree/{sw['source_revision']})",
                  f"- Declared source version: {sw['source_version'] or 'unknown / 未宣言'}; license: {sw['license_spdx']}; inspected: {r['last_reviewed_at']}",
                  '- Selected because: ' + cell(r['summary']['en']) + ' ' + cell(r['summary']['ja']),
                  '- Limits: ' + cell(r['limitations']['en']) + ' ' + cell(r['limitations']['ja']), '']
    return '\n'.join(lines), rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--write', action='store_true')
    modes.add_argument('--check', action='store_true')
    args = parser.parse_args()
    text, rows = report(gen.build_model())
    path = gen.ROOT / REPORT
    if args.write:
        path.write_bytes(text.encode('utf-8'))
    if args.check and (not path.exists() or path.read_bytes() != text.encode('utf-8')):
        print('Coverage report drift: ' + REPORT)
        return 1
    counts = {lang: Counter('routed' if r['actual'][lang] else 'unresolved' for r in rows) for lang in ('en', 'ja')}
    failures = [r['id'] for r in rows if not r['matches_expectation']]
    print(json.dumps({'seeds_per_language': len(rows), 'languages': counts, 'mismatches': failures}, ensure_ascii=False, sort_keys=True))
    if not args.write and not args.check:
        print(text)
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())

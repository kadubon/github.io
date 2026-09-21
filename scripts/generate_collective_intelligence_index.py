#!/usr/bin/env python3
"""Offline deterministic Collective Intelligence Index representations.

Authority: works.html -> research-catalog.json; oss-catalog.json -> repository
identity; curated editorial/evidence records supply bounded interpretations.
No network, package execution, current-clock timestamps or external templates.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://kadubon.github.io/github.io/'
STEM = 'collective-intelligence-index'
SCHEMA = BASE + 'schemas/' + STEM + '.schema.json'
FORMATS = [STEM + '.html', STEM + '.ja.html', STEM + '.json', STEM + '.md',
           STEM + '.ja.md', 'schemas/' + STEM + '.schema.json', 'collective-intelligence.bib']
REQUIRED_CORE = {'sw-ccr', 'sw-pic', 'sw-vek', 'sw-alt', 'sw-cait', 'sw-cpcf'}


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':'), allow_nan=False).encode('utf-8')).hexdigest()


def safe_url(value):
    p = urlsplit(value)
    if p.scheme != 'https' or not p.netloc or p.username or p.password or any(ord(c) < 32 for c in value):
        raise ValueError('Only absolute credential-free HTTPS URLs are allowed')
    return value


def link(url, label):
    return f'<a href="{escape(safe_url(url), quote=True)}">{escape(str(label))}</a>'


def ld_text(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e')


def build_model():
    c = read('data/collective-intelligence-curation.json')
    e = read('data/collective-intelligence-evidence.json')
    papers = {r['id']: r for r in read('research-catalog.json')['records']}
    repos = {r['full_name']: r for r in read('oss-catalog.json')['repositories']}
    releases = read('data/oss-release-snapshots.json')['repositories']
    resources = []
    for entry in c['resources']:
        r = copy.deepcopy(entry)
        r.update(ownership='takahashi', alternate_names=[], language=['en'],
                 source_state='reviewed_snapshot', last_reviewed_at=e['reviewed_at'],
                 unsupported_claims=c['sections'][10]['text'])
        r['related_resource_ids'] = sorted({x['target'] if x['source'] == r['id'] else x['source']
                                            for x in c['relations'] if r['id'] in (x['source'], x['target'])})
        if r['kind'] == 'paper':
            p = papers[r['source_catalog_id']]
            if p['record_type'] != 'scholarly_article':
                raise ValueError('Software archive cannot become a paper')
            r.update(name=p['title'], canonical_url=p['doi_url'])
            r['paper'] = {k: p[k] for k in ('title', 'authors', 'doi', 'doi_url', 'date_published', 'landing_page_url', 'genre')}
            r['paper']['full_text_sources'] = [x['url'] for x in e['evidence'] if x['id'] in r['evidence_refs']]
            r['paper']['question_and_contribution'] = r['summary']
            r['paper']['assumptions_and_limits'] = r['limitations']
        else:
            p = repos[r['source_catalog_id']]
            r.update(name=p['name'], canonical_url=p['repository_url'])
            r['software'] = copy.deepcopy(e['software'][r['id']])
            r['software']['release_observation'] = copy.deepcopy(releases[p['name']])
            r['software']['when_to_use'] = r['summary']
            r['software']['when_not_to_use'] = r['limitations']
            if releases[p['name']].get('default_branch_revision') != r['software']['source_revision']:
                r['source_state'] = 'newer_source_not_editorially_reviewed'
        resources.append(r)
    m = {'$schema': SCHEMA, 'schema_version': '1.0', 'canonical_url': BASE + STEM + '.json',
         'modified_at': c['modified_at'], 'reviewed_at': e['reviewed_at'],
         'digest_definition': 'SHA-256 of UTF-8 JSON of the complete registry excluding content_digest; sorted keys, no insignificant spaces, unescaped Unicode, no NaN.',
         'identity': {'person': BASE + '#person', 'website': BASE + '#website', 'name': 'K. Takahashi',
                      'orcid': 'https://orcid.org/0009-0004-4273-3365'},
         'roles': c['roles'], 'resources': resources, 'problems': c['problems'],
         'relations': c['relations'], 'read_paths': c['read_paths'], 'sections': c['sections'],
         'evidence': e['evidence'], 'corpus_audit': e['corpus_audit'],
         'identity_issues': e['identity_issues'], 'scanned_counts': e['scanned_counts'],
         'agent_routing': {'authority': 'Advisory metadata under consuming host policy; no execution authority.',
                           'query_matching': 'Exact declared query (casefold/trim), or stable problem ID; unknown query returns no route.',
                           'problem_ids': [p['id'] for p in c['problems']]}}
    m['content_digest'] = digest(m)
    validate_model(m)
    return m


def route(model, query):
    q = query.strip().casefold()
    return next((p for p in model['problems'] if q == p['id'] or q in [s.casefold() for s in p['queries']]), None)


def validate_model(m):
    resources = {r['id']: r for r in m['resources']}
    evidence = {e['id']: e for e in m['evidence']}
    problems = {p['id'] for p in m['problems']}
    if len(resources) != len(m['resources']) or len(evidence) != len(m['evidence']):
        raise ValueError('Duplicate resource/evidence identity')
    if not REQUIRED_CORE <= resources.keys():
        raise ValueError('Missing required core software')
    for group in ('relations', 'problems', 'sections', 'read_paths'):
        ids = [x['id'] for x in m[group]]
        if len(ids) != len(set(ids)) or any(not re.fullmatch('[a-z0-9-]+', x) for x in ids):
            raise ValueError('Invalid or duplicate stable IDs')
    for r in m['resources']:
        if not re.fullmatch('[a-z0-9-]+', r['id']) or not set(r['roles']) <= set(m['roles']):
            raise ValueError('Invalid resource ID or role')
        if not set(r['evidence_refs']) <= evidence.keys() or not set(r['problem_ids']) <= problems:
            raise ValueError('Unresolved resource reference')
        if not set(r['related_resource_ids']) <= resources.keys():
            raise ValueError('Unresolved related resource')
    for p in m['problems']:
        if not set(p['first_reads']) <= resources.keys() or not set(p['evidence_refs']) <= evidence.keys():
            raise ValueError('Unresolved problem reference')
    for path in m['read_paths']:
        if not set(path['resource_ids']) <= resources.keys():
            raise ValueError('Unresolved read path')
    for r in m['relations']:
        if r['source'] not in resources or r['target'] not in resources or not set(r['evidence_refs']) <= evidence.keys():
            raise ValueError('Unresolved relation reference')
        if not r['versions']['source'] or not r['versions']['target']:
            raise ValueError('Unbound relation version')
        if r['kind'] == 'proposed_integration_with' and r['status'] != 'proposed':
            raise ValueError('Proposed integration cannot become tested')
        if r['status'] == 'tested_upstream' and (r['evidence_origin'] != 'upstream_reported' or not r['checked_fields']):
            raise ValueError('Upstream test needs attributed check scope')
        if r['locally_executed']:
            raise ValueError('This index does not claim native package execution')
    def urls(v):
        if isinstance(v, dict):
            for k, value in v.items():
                if k in {'url', 'canonical_url', 'docs_url', 'license_url', 'doi_url', 'landing_page_url', 'source_url'} and isinstance(value, str):
                    safe_url(value)
                urls(value)
        elif isinstance(v, list):
            for value in v:
                urls(value)
    urls(m)
    candidate = dict(m)
    expected = candidate.pop('content_digest')
    if digest(candidate) != expected:
        raise ValueError('Content digest mismatch')


LABELS = {
    'limits': ('Limits / unsupported uses', '限界・未対応用途'), 'role': ('Primary editorial role', '編集上の主役割'),
    'evidence': ('Evidence', '根拠'), 'source': ('Source revision / declared version', 'ソース版・宣言バージョン'),
    'release': ('Observed GitHub release', '確認したGitHubリリース'), 'inputs': ('Inputs', '入力'),
    'outputs': ('Outputs', '出力'), 'prerequisites': ('Prerequisites', '前提'), 'effects': ('Effects and trust boundary', '作用と信頼境界'),
    'first_inspection_steps': ('First inspection', '最初の確認'), 'installation_guidance': ('Installation guidance', '導入案内'),
    'commands': ('Source-inspected interface (not executed)', 'ソース確認した操作（未実行）'),
    'stop_or_handoff_conditions': ('Stop / handoff', '停止・引継ぎ'), 'required_inputs': ('Required inputs', '必要入力'),
    'expected_outputs': ('Expected outputs', '期待出力'), 'prerequisite_or_unsupported_conditions': ('Conditions', '条件'),
}


def label(key, lang):
    return LABELS[key][lang == 'ja']


def page_url(lang):
    return BASE + STEM + ('.ja' if lang == 'ja' else '') + '.html'


def resource_fields(r, lang):
    fields = [(label('role', lang), r['primary_role']), (label('limits', lang), r['limitations'][lang])]
    if r['kind'] == 'paper':
        p = r['paper']
        fields += [('DOI', p['doi']), ('Publication / 著者・発表', ', '.join(p['authors']) + ' · ' + p['date_published'][:10] + ' · ' + p['genre']),
                   ('Source scope / 根拠範囲', 'Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.')]
    else:
        s = r['software']
        rel = s['release_observation']
        release = rel.get('latest_release')
        fields += [(label('source', lang), s['source_revision'] + ' / ' + str(s['source_version'] or 'unknown')),
                   ('Review state / レビュー状態', r['source_state']),
                   (label('release', lang), (release['tag'] + ' · ' + release['published_at']) if release else 'null — no published GitHub release observed'),
                   ('Release observation / リリース確認', rel.get('observed_at', 'unknown') + ' · ' + rel['refresh_status']),
                   ('License', s['license_spdx'])]
        for contract in s['interface_contracts']:
            fields.append(('Interface schema identity / スキーマ識別子', str(contract['schema_identity'] or 'null — upstream schema has no $id') + ' · ' + contract['scope']))
        fields += [(label(k, lang), s[k][lang]) for k in ('inputs', 'outputs', 'prerequisites', 'effects', 'first_inspection_steps', 'installation_guidance')]
        for cmd in s['commands']:
            fields.append((label('commands', lang), ' '.join([cmd['executable']] + cmd['arguments']) + ' — ' + cmd['purpose'][lang] + ' Ref: ' + cmd['source_ref'] + '; effects: ' + ', '.join(cmd['effects']) + '; cwd: ' + cmd['working_directory']))
    return fields


def resource_links(r, model):
    links = [(r['canonical_url'], 'DOI' if r['kind'] == 'paper' else 'Repository')]
    if r['kind'] == 'paper':
        links += [(r['paper']['landing_page_url'], 'Scholarly landing page')]
    else:
        s = r['software']; release = s['release_observation'].get('latest_release')
        links += [(s['docs_url'], 'Pinned contract'), (s['license_url'], 'Apache-2.0 license')]
        links += [(v['source_url'], 'Pinned interface schema') for v in s['interface_contracts']]
        if release:
            links += [(release['url'], 'Observed release')]
            links += [(u, u.rsplit('/', 1)[-1]) for u in release['assets']]
        links += [(u, 'Agent entry: ' + u.rsplit('/', 1)[-1]) for u in s['agent_entrypoints']]
    links += [(e['url'], e['id']) for e in model['evidence'] if e['id'] in r['evidence_refs']]
    return list(dict((url, name) for url, name in reversed(links)).items())[::-1]


def graph(model, lang):
    items = []
    for r in model['resources']:
        item = {'@type': 'ScholarlyArticle' if r['kind'] == 'paper' else 'SoftwareSourceCode',
                '@id': r['source_catalog_id'] if r['kind'] == 'paper' else r['canonical_url'], 'name': r['name'], 'url': r['canonical_url'],
                'description': r['summary'][lang], 'author': {'@id': BASE + '#person'}}
        if r['kind'] == 'paper':
            item.update(headline=r['name'], identifier=r['paper']['doi'], datePublished=r['paper']['date_published'],
                        mainEntityOfPage=r['paper']['landing_page_url'])
        else:
            item['codeRepository'] = r['canonical_url']
            item['license'] = r['software']['license_url']
            item['citation'] = [{'@id': next(x['source_catalog_id'] for x in model['resources'] if x['id'] == rel['target'])}
                                for rel in model['relations'] if rel['source'] == r['id'] and rel['kind'] == 'based_on']
        items.append(item)
    return {'@context': 'https://schema.org', '@graph': [
        {'@type': 'CollectionPage', '@id': page_url(lang), 'url': page_url(lang),
         'name': model['sections'][0]['heading'][lang], 'inLanguage': lang, 'dateModified': model['modified_at'],
         'about': {'@id': BASE + '#person'}, 'isPartOf': {'@id': BASE + '#website'},
         'mainEntity': {'@type': 'ItemList', 'numberOfItems': len(items), 'itemListElement': [
             {'@type': 'ListItem', 'position': i, 'item': {'@id': r['@id']}} for i, r in enumerate(items, 1)]}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': BASE},
            {'@type': 'ListItem', 'position': 2, 'name': model['sections'][0]['heading'][lang], 'item': page_url(lang)}]},
        *items]}


def html(model, lang):
    title = model['sections'][0]['heading'][lang]
    content = []
    for section in model['sections']:
        sid = section['id']
        body = '<p>' + escape(section['text'][lang]) + '</p>' if section['text'][lang] else ''
        if sid == 'start-here':
            body += '<ul>' + ''.join('<li>' + escape(p['id']) + ': ' + ' · '.join(link(page_url(lang) + '#' + rid, next(r['name'] for r in model['resources'] if r['id'] == rid)) for rid in p['resource_ids']) + '</li>' for p in model['read_paths']) + '</ul>'
        if sid == 'problems':
            for p in model['problems']:
                body += f'<article id="problem-{p["id"]}" data-problem-id="{p["id"]}"><h3>{escape(p["question"][lang])}</h3><p>'
                body += ' → '.join(link(page_url(lang) + '#' + rid, next(r['name'] for r in model['resources'] if r['id'] == rid)) for rid in p['first_reads']) + '</p><dl>'
                body += ''.join('<dt>' + escape(label(k, lang)) + '</dt><dd>' + escape(p[k][lang]) + '</dd>' for k in ('required_inputs', 'expected_outputs', 'prerequisite_or_unsupported_conditions', 'stop_or_handoff_conditions')) + '</dl></article>'
        if sid in ('core-software', 'core-papers', 'supporting-research'):
            selected = [r for r in model['resources'] if (r['tier'] == 'supporting' if sid == 'supporting-research' else r['tier'] == 'core' and r['kind'] == ('software' if sid == 'core-software' else 'paper'))]
            for r in selected:
                body += f'<article id="{r["id"]}" data-resource-id="{r["id"]}"><h3>{link(r["canonical_url"], r["name"])}</h3><p>{escape(r["summary"][lang])}</p><dl>'
                body += ''.join('<dt>' + escape(k) + '</dt><dd>' + escape(v) + '</dd>' for k, v in resource_fields(r, lang)) + '</dl><ul class="source-links">'
                body += ''.join('<li>' + link(u, name) + '</li>' for u, name in resource_links(r, model)) + '</ul></article>'
        if sid == 'interoperability':
            for rel in model['relations']:
                body += f'<article id="relation-{rel["id"]}" data-relation-id="{rel["id"]}"><h3>{escape(rel["source"])} → {escape(rel["target"])}</h3>'
                body += '<p><strong>' + escape(rel['kind'] + ' · ' + rel['status'] + ' · ' + rel['evidence_origin']) + '</strong></p><p>' + escape(rel['scope'][lang]) + '</p>'
                body += '<p>' + escape(rel['versions']['source'] + ' → ' + rel['versions']['target']) + '</p><p>' + escape(', '.join(rel['checked_fields']) or 'No executable mapping checked / 実行写像の検査なし') + '</p><p>' + escape(rel['unsupported_obligations'][lang]) + '</p><p>'
                body += ' · '.join(link(e['url'], e['id']) for e in model['evidence'] if e['id'] in rel['evidence_refs']) + '</p></article>'
        if sid == 'downloads':
            body += '<ul>' + ''.join('<li>' + link(BASE + p, p) + '</li>' for p in FORMATS) + '</ul>'
        if sid == 'sources-and-maintenance':
            body += '<p>' + escape(f"Scanned: {model['scanned_counts']['research_records']} research records; {model['scanned_counts']['repositories']} repositories. Selected: {len(model['resources'])} resources. Full-text scope review applies only to selected papers; remaining candidate matches are explicitly unresolved in the registry.") + '</p>'
            body += '<ul>' + ''.join('<li>' + escape(i['source'] + ': ' + i['status'] + ' — ' + i['reason']) + '</li>' for i in model['identity_issues']) + '</ul><p>'
            body += link(BASE + 'docs/collective-intelligence-index-maintenance.md', 'Maintenance / 保守') + ' · ' + link('https://github.com/kadubon/github.io/issues', 'Corrections / 訂正') + '</p>'
        content.append(f'<section class="container" id="{sid}"><h2>{escape(section["heading"][lang])}</h2>{body}</section>')
    toc = ''.join(f'<li><a href="#{s["id"]}">{escape(s["heading"][lang])}</a></li>' for s in model['sections'])
    return f'''<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | K. Takahashi</title><meta name="description" content="{escape(model['sections'][0]['text'][lang], quote=True)}">
<meta name="robots" content="index,follow"><meta property="og:type" content="website"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:url" content="{page_url(lang)}">
<link rel="canonical" href="{page_url(lang)}"><link rel="alternate" hreflang="en" href="{page_url('en')}"><link rel="alternate" hreflang="ja" href="{page_url('ja')}">
<link rel="alternate" type="application/json" href="{BASE + STEM}.json"><link rel="alternate" type="text/markdown" href="{BASE + STEM}{'.ja' if lang == 'ja' else ''}.md">
<link rel="stylesheet" href="{BASE}style.css"><style>article{{border-top:1px solid #ccd8e5;padding:1rem 0;min-width:0}}.container{{box-sizing:border-box}}main,dd,a,code{{overflow-wrap:anywhere}}dd{{margin:0 0 .6rem}}dt{{font-weight:600}}.source-links{{font-size:.9rem}}a:focus-visible{{outline:3px solid #174c87;outline-offset:3px}}.index-toc{{columns:2;text-align:left}}.index-toc li{{display:block;break-inside:avoid;margin:0 0 .45rem}}@media(max-width:600px){{.container{{margin:16px 8px;padding:16px}}.index-toc{{columns:1}}h1{{font-size:1.7rem}}}}</style>
<script type="application/ld+json">{ld_text(graph(model, lang))}</script></head><body>
<a class="skip-link" href="#main-content">{'本文へ' if lang == 'ja' else 'Skip to content'}</a>
<header class="container"><h1>{escape(title)}</h1><nav aria-label="Primary">{link(BASE, 'Home')} · {link(BASE + 'research-map.html', 'Research Map')} · {link(BASE + 'works.html', 'Works')} · {link(BASE + 'oss.html', 'OSS')} · {link(page_url('ja' if lang == 'en' else 'en'), '日本語' if lang == 'en' else 'English')}</nav>
<p>K. Takahashi · <time datetime="{model['reviewed_at']}">{model['reviewed_at']}</time></p><nav aria-label="Contents"><ul class="index-toc">{toc}</ul></nav></header>
<main id="main-content">{''.join(content)}</main><footer class="container">CC BY 4.0 · K. Takahashi</footer></body></html>
'''


def md_text(s):
    return escape(str(s), quote=False).replace('\\', '\\\\').replace('[', '\\[').replace(']', '\\]').replace('*', '\\*').replace('`', '\\`')


def markdown(m, lang):
    # Render the same normalized cards/fields as HTML; Markdown is a plain download.
    lines = ['# ' + m['sections'][0]['heading'][lang], '', 'K. Takahashi · ' + m['reviewed_at'], '', page_url(lang), '']
    for s in m['sections']:
        lines += ['## ' + s['heading'][lang], '', md_text(s['text'][lang]), '']
        if s['id'] == 'start-here':
            for p in m['read_paths']:
                lines += [p['id'] + ': ' + ' → '.join(f'[{rid}]({page_url(lang)}#{rid})' for rid in p['resource_ids']), '']
        if s['id'] == 'problems':
            for p in m['problems']:
                lines += ['### ' + p['question'][lang] + ' (' + p['id'] + ')', '', ' → '.join(f'[{rid}]({page_url(lang)}#{rid})' for rid in p['first_reads']), '']
                lines += [label(k, lang) + ': ' + md_text(p[k][lang]) + '\n' for k in ('required_inputs', 'expected_outputs', 'prerequisite_or_unsupported_conditions', 'stop_or_handoff_conditions')]
        if s['id'] in ('core-software', 'core-papers', 'supporting-research'):
            for r in m['resources']:
                target = 'supporting-research' if r['tier'] == 'supporting' else ('core-papers' if r['kind'] == 'paper' else 'core-software')
                if target != s['id']:
                    continue
                lines += [f'### {md_text(r["name"])} ({r["id"]})', '', md_text(r['summary'][lang]), '']
                lines += [md_text(k) + ': ' + md_text(v) + '\n' for k, v in resource_fields(r, lang)]
                lines += ['- [' + md_text(n) + '](' + safe_url(u) + ')' for u, n in resource_links(r, m)] + ['']
        if s['id'] == 'interoperability':
            for r in m['relations']:
                lines += ['### ' + r['id'], '', f"{r['source']} → {r['target']}: {r['kind']} / {r['status']} / {r['evidence_origin']}", '',
                          md_text(r['scope'][lang]), '', md_text(r['versions']['source'] + ' → ' + r['versions']['target']), '',
                          'Checked fields: ' + md_text(', '.join(r['checked_fields']) or 'none'), '', md_text(r['unsupported_obligations'][lang]), '']
                lines += ['- [' + e['id'] + '](' + e['url'] + ')' for e in m['evidence'] if e['id'] in r['evidence_refs']] + ['']
        if s['id'] == 'downloads':
            lines += [f'- [{p}]({BASE}{p})' for p in FORMATS] + ['']
        if s['id'] == 'sources-and-maintenance':
            lines += [f"Scanned {m['scanned_counts']['research_records']} research records and {m['scanned_counts']['repositories']} repositories; selected {len(m['resources'])} resources.", '']
            lines += [md_text(i['source'] + ': ' + i['status'] + ' — ' + i['reason']) + '\n' for i in m['identity_issues']]
            lines += [f'[Maintenance]({BASE}docs/collective-intelligence-index-maintenance.md)', '']
    return '\n'.join(lines).rstrip() + '\n'


def bibtex(m):
    def bib(s):
        return str(s).replace('\\', r'\textbackslash{}').replace('{', r'\{').replace('}', r'\}').replace('&', r'\&').replace('%', r'\%').replace('_', r'\_')
    records = []
    for r in m['resources']:
        if r['kind'] != 'paper':
            continue
        p = r['paper']
        fields = {'author': ' and '.join(p['authors']), 'title': p['title'], 'year': p['date_published'][:4],
                  'doi': p['doi'], 'url': p['doi_url'], 'note': p['genre']}
        records.append('@misc{takahashi-' + r['id'] + ',\n' + ',\n'.join('  ' + k + ' = {' + bib(v) + '}' for k, v in fields.items()) + '\n}')
    return '\n\n'.join(records) + '\n'


def sitemap_bytes(model):
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    tree = ET.fromstring((ROOT / 'sitemap.xml').read_bytes())
    entries = {n.findtext(ns + 'loc'): n for n in tree}
    for lang in ('en', 'ja'):
        url = page_url(lang)
        node = entries.get(url)
        if node is None:
            node = ET.Element(ns + 'url'); ET.SubElement(node, ns + 'loc').text = url
            entries[url] = node
        date = node.find(ns + 'lastmod')
        if date is None:
            date = ET.SubElement(node, ns + 'lastmod')
        date.text = model['modified_at']
    root = ET.Element(ns + 'urlset')
    root.extend(entries[k] for k in sorted(entries))
    ET.register_namespace('', ns[1:-1])
    return ET.tostring(root, encoding='utf-8', xml_declaration=True)


def outputs(model):
    result = {STEM + '.json': json_text(model).encode('utf-8'),
              'collective-intelligence.bib': bibtex(model).encode('utf-8'), 'sitemap.xml': sitemap_bytes(model)}
    for lang in ('en', 'ja'):
        stem = STEM + ('.ja' if lang == 'ja' else '')
        result[stem + '.html'] = html(model, lang).encode('utf-8')
        result[stem + '.md'] = markdown(model, lang).encode('utf-8')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    changed = []
    for name, content in outputs(build_model()).items():
        path = ROOT / name
        if not path.exists() or path.read_bytes() != content:
            changed.append(name)
            if not args.check:
                path.write_bytes(content)
    print(('Drift: ' if args.check else 'Generated: ') + (', '.join(changed) or 'none'))
    return int(args.check and bool(changed))


if __name__ == '__main__':
    raise SystemExit(main())

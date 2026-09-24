"""Regression and failure-mode tests; no indexed software is imported/executed."""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import generate_collective_intelligence_index as gen
import generate_agent_catalogs as catalogs
import generate_paper_pages as papers
import validate_collective_intelligence_index as validation
import audit_collective_intelligence_coverage as coverage
from jsonschema import Draft202012Validator


class IndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = gen.build_model()

    def mutate(self, fn):
        m = copy.deepcopy(self.model); fn(m)
        m.pop('content_digest'); m['content_digest'] = gen.digest(m)
        return m

    def test_complete_validation(self):
        validation.validate()

    def test_required_core(self):
        self.assertTrue(gen.REQUIRED_CORE <= {r['id'] for r in self.model['resources']})

    def test_exact_seed_identity(self):
        p = next(r for r in self.model['resources'] if r['id'] == 'paper-growth')['paper']
        self.assertEqual(p['title'], 'Observing and Accelerating Collective Capability Growth')
        self.assertEqual(p['doi'], '10.5281/zenodo.22604358')
        self.assertEqual(p['landing_page_url'], gen.BASE + 'papers/2026-09-07-observing-and-accelerating-collective-capability-growth-22604358/')

    def test_bibliography_source_authority(self):
        source = {r['id']: r for r in gen.read('research-catalog.json')['records']}
        bib = gen.bibtex(self.model)
        for r in self.model['resources']:
            if r['kind'] == 'paper':
                p = source[r['source_catalog_id']]
                self.assertEqual(p['record_type'], 'scholarly_article')
                for key in ('authors', 'title', 'doi', 'date_published'):
                    self.assertEqual(r['paper'][key], p[key])
                e = next(x for x in self.model['evidence'] if x['id'] in r['evidence_refs'])
                if e['doi_record']['issued'] != p['date_published'][:10]:
                    self.assertTrue(any(i['source'] == p['doi'] and i['status'] == 'concept_record_date_discrepancy'
                                        for i in self.model['identity_issues']))
                    self.assertIn('unresolved', r['limitations']['en'])
                self.assertIn(p['doi'], bib)
            else:
                self.assertNotIn('paper', r)
        self.assertNotIn('10.5281/zenodo.20107661', bib)

    def test_problem_routes(self):
        cases = {'verification backlog':'sw-vek', 'reuse versus solving from scratch':'sw-alt',
                 'did copied artifacts increase capability':'sw-cait','coordinate leased multi-agent work':'sw-ccr',
                 'preserve unknown output obligations':'sw-pic','choose information gathering before capability investment':'sw-cpcf',
                 'remember a verified procedure':'sw-oawm','change local workflow policy':'sw-oasg',
                 'adaptive hypothesis testing':'sw-audit','forecast when ASI will arrive':'sw-simulator',
                 'integrate ALT with CCR automatically':'sw-alt','identify who pays for verification':'paper-conversion'}
        for query, resource in cases.items():
            with self.subTest(query=query):
                route = gen.route(self.model, query)
                self.assertIn(resource, route['first_reads'])
                self.assertTrue(route['stop_or_handoff_conditions']['en'])
        self.assertIsNone(gen.route(self.model, 'unknown arbitrary request'))

    def test_routing_boundaries(self):
        self.assertIn('synthetic local profile', gen.route(self.model, 'verification-backlog')['stop_or_handoff_conditions']['en'])
        self.assertIn('No custom host admission', gen.route(self.model, 'interchange')['stop_or_handoff_conditions']['en'])
        self.assertIn('no empirical ASI', gen.route(self.model, 'forecast')['stop_or_handoff_conditions']['en'])

    def test_duplicate_and_dangling_ids_rejected(self):
        for fn in (lambda m: m['resources'].append(m['resources'][0]),
                   lambda m: m['relations'][0].update(target='missing')):
            with self.assertRaises(ValueError): gen.validate_model(self.mutate(fn))

    def test_proposal_cannot_be_tested(self):
        m = self.mutate(lambda m: next(r for r in m['relations'] if r['status'] == 'proposed').update(status='tested_upstream'))
        with self.assertRaises(ValueError): gen.validate_model(m)
        self.assertFalse(Draft202012Validator(gen.read('schemas/collective-intelligence-index.schema.json')).is_valid(m))

    def test_upstream_not_local_execution(self):
        with self.assertRaises(ValueError):
            gen.validate_model(self.mutate(lambda m: m['relations'][0].update(locally_executed=True)))

    def test_version_pair_not_renewed(self):
        m = copy.deepcopy(self.model)
        r = next(r for r in m['resources'] if r['id'] == 'sw-ccr')
        r['software']['release_observation']['latest_release']['tag'] = 'v999.0.0'
        self.assertEqual(m['relations'], self.model['relations'])
        old = next(x for x in m['relations'] if x['id'] == 'ccr-from-alt-legacy')
        self.assertTrue(old['versions']['target'].startswith('0.4.0'))

    def test_no_transitive_claim(self):
        r = next(x for x in self.model['relations'] if x['id'] == 'alt-to-oawm')
        self.assertEqual(r['status'], 'proposed')
        self.assertEqual(r['checked_fields'], [])

    def test_xss_quotes_unicode_and_long_urls(self):
        m = copy.deepcopy(self.model)
        payload = '</script><img src=x onerror="alert(1)"> 日本語 & "quoted"'
        m['resources'][0]['name'] = payload
        page = gen.html(m, 'ja')
        doc = validation.Document(page)
        self.assertEqual(len(doc.resources), len(m['resources']))
        self.assertNotIn('<img src=x', page)
        self.assertEqual(doc.scripts[0]['@graph'][2]['name'], payload)
        self.assertIn('&lt;/script&gt;', page)
        self.assertEqual(gen.safe_url('https://example.org/' + 'a' * 4000), 'https://example.org/' + 'a' * 4000)

    def test_malicious_urls_rejected(self):
        for url in ('javascript:alert(1)', 'data:text/html,x', '//evil.example', 'https://user:password@example.org', 'https://example.org/\nx', 'file:///tmp/x'):
            with self.subTest(url=url), self.assertRaises(ValueError): gen.link(url, 'x')

    def test_schema_rejects_unknown_claim_flags(self):
        m = copy.deepcopy(self.model); m['resources'][0]['verified'] = True
        self.assertFalse(Draft202012Validator(gen.read('schemas/collective-intelligence-index.schema.json')).is_valid(m))

    def test_unknowns_remain_explicit(self):
        oawm = next(r for r in self.model['resources'] if r['id'] == 'sw-oawm')['software']
        self.assertIsNone(oawm['release_observation']['latest_release'])
        self.assertEqual(oawm['release_observation']['release_status'], 'no_published_github_release')
        vek = next(r for r in self.model['resources'] if r['id'] == 'sw-vek')
        self.assertIn('remain null', vek['limitations']['en'])

    def test_pdf_network_failure_is_not_no_pdf(self):
        doi = '10.5281/zenodo.22604358'
        cached = {'record_id': '22604358', 'status': 'PDF_UNRESOLVED', 'candidates': [],
                  'pdf_url': None, 'reason': 'Zenodo API lookup failed after retries: HTTPError'}
        self.assertEqual(papers.resolve_pdf(doi, 'Title', {doi: cached}, False), cached)
        with patch.object(papers, 'urlopen', side_effect=TimeoutError), patch.object(papers.time, 'sleep'):
            result = papers.resolve_pdf(doi, 'Title', {doi: cached}, True)
        self.assertEqual(result['reason'], cached['reason'])
        self.assertEqual(result['refresh_status'], 'stale')

    def test_offline_and_deterministic(self):
        with patch('socket.socket', side_effect=AssertionError('network forbidden')):
            self.assertEqual(gen.outputs(gen.build_model()), gen.outputs(gen.build_model()))

    def test_check_detects_drift_without_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ['data/collective-intelligence-curation.json','data/collective-intelligence-evidence.json',
                         'data/oss-release-snapshots.json','research-catalog.json','oss-catalog.json','sitemap.xml',
                         'scripts/generate_collective_intelligence_index.py', *gen.outputs(self.model).keys()]:
                (root / name).parent.mkdir(exist_ok=True, parents=True); shutil.copyfile(ROOT / name, root / name)
            target = root / (gen.STEM + '.html'); target.write_bytes(target.read_bytes() + b'<!-- drift -->')
            before = {str(p): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            run = subprocess.run([sys.executable, '-B', str(root / 'scripts/generate_collective_intelligence_index.py'), '--check'], capture_output=True)
            self.assertEqual(run.returncode, 1)
            self.assertEqual(before, {str(p): p.read_bytes() for p in root.rglob('*') if p.is_file()})

    def test_generators_preserve_discovery_and_sitemap(self):
        records, state = catalogs.load_research_catalog()
        repos = gen.read('oss-catalog.json')['repositories']
        self.assertIn(gen.STEM + '.html', catalogs.render_oss_html(repos))
        index = catalogs.agent_index(records, state, repos)
        for name in gen.FORMATS:
            self.assertIn(gen.BASE + name, index['entry_points'].values())
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); shutil.copyfile(ROOT / 'sitemap.xml', root / 'sitemap.xml')
            with patch.object(papers, 'ROOT', root): papers.sync_sitemap([gen.BASE + 'papers/'])
            text = (root / 'sitemap.xml').read_text()
            for lang in ('en', 'ja'): self.assertIn(gen.page_url(lang), text)
            self.assertIn('<lastmod>' + self.model['modified_at'] + '</lastmod>', text)
            with patch.object(gen, 'ROOT', root):
                self.assertEqual((root / 'sitemap.xml').read_bytes(), gen.sitemap_bytes(self.model))

    def test_index_has_no_empirical_acceleration_claim(self):
        for lang in ('en', 'ja'):
            page = gen.html(self.model, lang)
            phrase = 'No observed global self-acceleration' if lang == 'en' else '大域的自己加速の観測'
            self.assertIn(phrase, page)
        self.assertFalse(any(r['locally_executed'] for r in self.model['relations']))

    def test_no_private_paths_or_staging(self):
        for name, data in gen.outputs(self.model).items():
            text = data.decode('utf-8').lower()
            for forbidden in ('c:\\users\\', 'c:/users/', 'localhost', '127.0.0.1', 'sandbox:', 'ghp_', 'github_pat_'):
                self.assertNotIn(forbidden, text, (name, forbidden))

    def test_audit_coverage_and_resource_counts(self):
        audit = self.model['corpus_audit']
        self.assertEqual(len(audit), sum(self.model['scanned_counts'].values()))
        self.assertEqual(len({a['source_catalog_id'] for a in audit}), len(audit))
        self.assertEqual(sum(r['kind'] == 'paper' for r in self.model['resources']), 19)
        self.assertEqual(sum(r['kind'] == 'software' for r in self.model['resources']), 18)

    def test_bilingual_seed_coverage(self):
        rows = coverage.audit(self.model)
        self.assertEqual({r['family'] for r in rows}, set('ABCDEFGHIJKLMNO'))
        self.assertEqual(len(rows), 168)
        self.assertTrue(all(r['matches_expectation'] for r in rows))
        self.assertEqual(sum(r['actual']['en'] is None for r in rows), 5)
        self.assertTrue(all(r['actual']['en'] == r['actual']['ja'] for r in rows))

    def test_query_normalization_and_precision(self):
        for query in ['  AGENT KEEPS\nRETRYING THE SAME MCP TOOL?! ', 'ａｇｅｎｔ keeps retrying the same MCP tool', '同じMCPツールの再試行が止まらない？']:
            self.assertEqual(gen.route(self.model, query)['id'], 'retry-recovery')
        for query in ['do not use the retry-recovery route', 'not memory deletion', 'OAuth for agents', 'MCP token passthrough', 'slopsquatting', 'agent retry banana']:
            self.assertIsNone(gen.route(self.model, query))

    def test_duplicate_aliases_fail_instead_of_first_match(self):
        for fn in [lambda m: m['problems'][0]['query_aliases']['en'].extend(['same alias', ' SAME ALIAS?!']),
                   lambda m: m['problems'][0]['query_aliases']['en'].append(m['problems'][1]['question']['en']),
                   lambda m: m['problems'][0]['query_aliases']['en'].append('OAuth for agents')]:
            with self.assertRaises(ValueError): gen.validate_model(self.mutate(fn))

    def test_related_problem_graph_is_bounded_and_nonrecursive(self):
        for p in self.model['problems']:
            self.assertTrue(2 <= len(p['related_problem_ids']) <= 4)
        m = copy.deepcopy(self.model)
        a, b = m['problems'][:2]
        a['related_problem_ids'] = [b['id'], 'memory']
        b['related_problem_ids'] = [a['id'], 'memory']
        m.pop('content_digest'); m['content_digest'] = gen.digest(m)
        gen.validate_model(m)
        self.assertIn('#problem-' + b['id'], gen.html(m, 'en'))
        with self.assertRaises(ValueError):
            gen.validate_model(self.mutate(lambda m: m['problems'][0]['related_problem_ids'].append('missing')))

    def test_selected_resources_are_reachable(self):
        reached = {rid for p in self.model['problems'] for rid in p['relevant_resource_ids']}
        self.assertEqual(reached, {r['id'] for r in self.model['resources']})
        for p in self.model['problems']:
            self.assertTrue(1 <= len(p['first_reads']) <= 3)
        with self.assertRaises(ValueError):
            gen.validate_model(self.mutate(lambda m: m['problems'][0]['relevant_resource_ids'].append('missing')))

    def test_boundaries_cannot_disappear(self):
        for key in ['question', 'symptoms', 'prerequisite_or_unsupported_conditions', 'stop_or_handoff_conditions']:
            for lang in ('en', 'ja'):
                with self.subTest(key=key, lang=lang), self.assertRaises(ValueError):
                    gen.validate_model(self.mutate(lambda m: m['problems'][0][key].update({lang: ''})))
        schema = Draft202012Validator(gen.read('schemas/collective-intelligence-index.schema.json'))
        self.assertFalse(schema.is_valid(self.mutate(lambda m: m['agent_routing'].update(authority='Permission to execute tools'))))

    def test_review_dates_are_scoped(self):
        for r in self.model['resources']:
            if r['id'] in {'sw-cmgl', 'sw-memoryflow', 'sw-pfg', 'sw-fost', 'sw-atrb', 'sw-oversight'}:
                self.assertEqual(r['last_reviewed_at'], '2026-09-24')
            else:
                self.assertEqual(r['last_reviewed_at'], '2026-09-21')
        self.assertTrue(all(r['checked_at'] == '2026-09-21' for r in self.model['relations']))

    def test_coverage_report_offline_determinism_and_drift(self):
        with patch('socket.socket', side_effect=AssertionError('network forbidden')):
            text, rows = coverage.report(self.model)
            self.assertEqual(text, coverage.report(self.model)[0])
            self.assertEqual((ROOT / coverage.REPORT).read_bytes(), text.encode('utf-8'))
        fixture = gen.read(coverage.SEEDS)
        fixture['seeds'][0]['query']['en'] = 'a query with no declared alias'
        self.assertFalse(coverage.audit(self.model, fixture)[0]['matches_expectation'])

    def test_symptoms_static_anchors_and_no_keyword_markup(self):
        for lang in ('en', 'ja'):
            page = gen.html(self.model, lang); doc = validation.Document(page)
            self.assertEqual(doc.problems, [p['id'] for p in self.model['problems']])
            self.assertEqual(len(doc.ids), len(set(doc.ids)))
            self.assertIn('find-by-symptom', doc.ids)
            self.assertNotIn('name="keywords"', page)
            self.assertNotIn('FAQPage', page)
            for p in self.model['problems']:
                self.assertIn(gen.page_url(lang) + '#problem-' + p['id'], doc.links)


if __name__ == '__main__':
    unittest.main()

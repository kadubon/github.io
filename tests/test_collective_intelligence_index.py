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
import check_collective_intelligence_publication as publication
import refresh_oss_release_snapshots as refresh
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

    def test_source_difference_is_not_chronology_or_review(self):
        original_read = gen.read
        baseline = gen.build_model()
        for revision, status, issue in [('f' * 40, 'current', 'observed_revision_differs'),
                                        (None, 'current', 'source_comparison_unavailable'),
                                        ('', 'unresolved', 'source_comparison_unavailable'),
                                        ('f' * 40, 'stale', 'source_comparison_unavailable')]:
            def read(path):
                value = original_read(path)
                if path == 'data/oss-release-snapshots.json':
                    value['repositories']['collective-capability-runtime'].update(
                        default_branch_revision=revision, refresh_status=status)
                return value
            with self.subTest(revision=revision, status=status), patch.object(gen, 'read', side_effect=read):
                model = gen.build_model()
            resource = next(r for r in model['resources'] if r['id'] == 'sw-ccr')
            self.assertEqual(resource['source_state'], 'reviewed_snapshot')
            self.assertTrue(any(i['source'] == 'sw-ccr' and i['status'] == issue for i in model['identity_issues']))
            self.assertEqual(model['relations'], baseline['relations'])
            self.assertEqual(resource['last_reviewed_at'], next(r for r in baseline['resources'] if r['id'] == 'sw-ccr')['last_reviewed_at'])

    def test_publication_mime_accepts_text_but_rejects_html_data(self):
        for name, mime in [('index.html', 'text/html; charset=utf-8'),
                           ('index.json', 'application/json'), ('schema.json', 'application/schema+json'),
                           ('index.md', 'text/plain; charset=utf-8'), ('index.md', 'text/markdown'),
                           ('index.bib', 'text/plain'), ('index.bib', 'application/x-bibtex'),
                           ('index.bib', 'application/octet-stream'),
                           ('sitemap.xml', 'application/xml')]:
            self.assertTrue(publication.appropriate_content_type(name, mime))
        for name in ('index.json', 'schema.json', 'index.md', 'index.bib'):
            for mime in ('text/html', 'application/xhtml+xml', None):
                self.assertFalse(publication.appropriate_content_type(name, mime))
        for name in ('index.json', 'index.md'):
            self.assertFalse(publication.appropriate_content_type(name, 'application/octet-stream'))

    def test_publication_head_unsupported_uses_one_get(self):
        from urllib.error import HTTPError
        from unittest.mock import MagicMock
        response = MagicMock()
        response.__enter__.return_value = response
        response.status = 200
        response.url = 'https://example.org/paper'
        response.headers = {'Content-Type': 'text/plain'}
        response.read.return_value = b'paper'
        error = HTTPError(response.url, 405, 'HEAD unsupported', {}, None)
        with patch.object(publication, 'urlopen', side_effect=[error, response]) as opened:
            result, body = publication.fetch(response.url, head=True)
        self.assertEqual(result['status'], 200)
        self.assertEqual(body, b'paper')
        self.assertEqual([call.args[0].get_method() for call in opened.call_args_list], ['HEAD', 'GET'])

    def test_selected_refresh_preserves_other_records_and_package_dates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'data').mkdir()
            old = {'schema_version': '1.0', 'repositories': {'selected': {'package_registry_status': '2026-10-17 metadata only'}, 'other': {'observed_at': 'old'}}}
            path = root / 'data/oss-release-snapshots.json'
            path.write_text(json.dumps(old), encoding='utf-8')
            (root / 'oss-catalog.json').write_text(json.dumps({'repositories': [
                {'name': 'selected', 'full_name': 'owner/selected', 'default_branch': 'main', 'repository_url': 'https://github.com/owner/selected'},
                {'name': 'other', 'full_name': 'owner/other'}]}), encoding='utf-8')
            (root / 'data/collective-intelligence-curation.json').write_text(json.dumps({'resources': [{'kind': 'software', 'source_catalog_id': 'owner/selected'}]}), encoding='utf-8')
            with patch.object(refresh, 'ROOT', root), patch.object(refresh, 'PATH', path), patch.object(sys, 'argv', ['refresh', '--selected-only']), patch.object(refresh, 'request', side_effect=[None, {'sha': 'a' * 40}]):
                self.assertEqual(refresh.main(), 0)
            result = json.loads(path.read_text(encoding='utf-8'))['repositories']
            self.assertEqual(result['other'], old['repositories']['other'])
            self.assertEqual(result['selected']['package_registry_status'], '2026-10-17 metadata only')

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
        self.assertEqual(sum(r['kind'] == 'paper' for r in self.model['resources']), 20)
        self.assertEqual(sum(r['kind'] == 'software' for r in self.model['resources']), 21)

    def test_checkedflow_is_supporting_without_route_or_integration_promotion(self):
        selected = [r for r in self.model['resources'] if r['id'] == 'sw-checkedflow']
        self.assertEqual(len(selected), 1)
        r = selected[0]
        self.assertEqual((r['kind'], r['tier'], r['source_catalog_id']),
                         ('software', 'supporting', 'kadubon/checkedflow'))
        self.assertEqual(r['primary_role'], 'collective-coordination')
        self.assertNotIn('forecast', r['problem_ids'])
        for p in self.model['problems']:
            self.assertNotIn(r['id'], p['first_reads'])
            self.assertEqual(r['id'] in p['relevant_resource_ids'], p['id'] in r['problem_ids'])
        self.assertFalse(any(r['id'] in (edge['source'], edge['target']) for edge in self.model['relations']))
        evidence = [e for e in self.model['evidence'] if e['id'] in r['evidence_refs']]
        self.assertEqual(len(evidence), len(r['evidence_refs']))
        for entry in evidence:
            self.assertEqual(entry['revision'], r['software']['source_revision'])
            self.assertIn('/blob/' + entry['revision'] + '/', entry['url'])
            self.assertEqual(entry['observed_at'], '2026-09-26')
        upstream = next(e for e in evidence if e['id'] == 'e-checkedflow-validation')
        self.assertEqual(upstream['origin'], 'upstream_reported')
        self.assertEqual(len(self.model['resources']), 41)

    def test_cio_version_refresh_preserves_historical_evidence(self):
        r = next(r for r in self.model['resources'] if r['id'] == 'sw-cio')
        self.assertEqual((r['tier'], r['source_catalog_id']),
                         ('supporting', 'kadubon/collective-intelligence-overlay'))
        self.assertEqual(r['software']['source_version'], '0.5.1')
        self.assertIn('0.5.1', r['summary']['en'])
        self.assertIn('assess_stock', r['software']['effects']['en'])
        self.assertEqual(r['software']['license_spdx'], 'Apache-2.0')
        for p in self.model['problems']:
            self.assertNotIn(r['id'], p['first_reads'])
            self.assertEqual(r['id'] in p['relevant_resource_ids'], p['id'] in r['problem_ids'])
        self.assertFalse(any(r['id'] in (edge['source'], edge['target']) for edge in self.model['relations']))
        evidence = [e for e in self.model['evidence'] if e['id'] in r['evidence_refs']]
        self.assertEqual(len(evidence), len(r['evidence_refs']))
        for entry in evidence:
            self.assertEqual(entry['revision'], r['software']['source_revision'] if entry['id'].startswith('e-cio-051-') else 'e830a6a54a22ba8190a64e0b184d461103287ee3')
            self.assertIn('/blob/' + entry['revision'] + '/', entry['url'])
            self.assertEqual(entry['observed_at'], '2026-10-06' if entry['id'].startswith('e-cio-051-') else '2026-10-04')
        self.assertEqual(next(e for e in evidence if e['id'] == 'e-cio-validation')['origin'],
                         'upstream_reported')

    def test_egr_has_bounded_completion_and_no_integration_promotion(self):
        r = next(r for r in self.model['resources'] if r['id'] == 'sw-egr')
        self.assertEqual((r['tier'], r['source_catalog_id']),
                         ('supporting', 'kadubon/evidence-gap-router'))
        self.assertEqual(r['software']['source_version'], '0.3.0')
        self.assertEqual(r['software']['license_spdx'], 'Apache-2.0')
        self.assertIn('external completeness unknown', r['limitations']['en'])
        self.assertIn('empirical utility is unmeasured', r['limitations']['en'])
        for p in self.model['problems']:
            self.assertNotIn(r['id'], p['first_reads'])
            self.assertEqual(r['id'] in p['relevant_resource_ids'], p['id'] in r['problem_ids'])
        self.assertFalse(any(r['id'] in (edge['source'], edge['target']) for edge in self.model['relations']))
        evidence = [e for e in self.model['evidence'] if e['id'] in r['evidence_refs']]
        self.assertEqual(len(evidence), len(r['evidence_refs']))
        for entry in evidence:
            self.assertEqual(entry['revision'], r['software']['source_revision'])
            self.assertIn('/blob/' + entry['revision'] + '/', entry['url'])
            self.assertEqual(entry['observed_at'], '2026-10-06')
        self.assertEqual(next(e for e in evidence if e['id'] == 'e-egr-validation')['origin'],
                         'upstream_reported')

    def test_phase_engineering_version_identity_and_static_publication(self):
        r = next(r for r in self.model['resources'] if r['id'] == 'paper-phase-engineering')
        self.assertEqual(r['paper']['doi'], '10.5281/zenodo.23240329')
        self.assertEqual(r['paper']['genre'], 'Preprint')
        self.assertEqual(r['name'], 'Collective Intelligence Phase Engineering: Audited Retention and Achieved Growth')
        evidence = next(e for e in self.model['evidence'] if e['id'] in r['evidence_refs'])
        self.assertEqual(evidence['doi_record']['related_identifiers'][0]['relatedIdentifier'],
                         '10.5281/zenodo.23240328')
        self.assertIn('not an empirical', r['limitations']['en'])
        for p in self.model['problems']:
            self.assertEqual(r['id'] in p['first_reads'], p['id'] == 'rsi-evidence')
            self.assertEqual(r['id'] in p['relevant_resource_ids'], p['id'] in r['problem_ids'])
        self.assertFalse(any(r['id'] in (e['source'], e['target']) for e in self.model['relations']))
        works = (ROOT / 'works.html').read_text(encoding='utf-8')
        self.assertIn('id="2026-10-08-collective-intelligence-phase-engineering-23240329"', works)
        self.assertIn(r['name'], works)
        self.assertIn(r['paper']['doi'], (ROOT / 'collective-intelligence.bib').read_text(encoding='utf-8'))

    def test_phase_engineering_core_reader_and_preserved_source(self):
        matches = [r for r in self.model['resources'] if r['id'] == 'paper-phase-engineering']
        self.assertEqual(len(matches), 1)
        r = matches[0]
        self.assertEqual(r['tier'], 'core')
        self.assertEqual(r['last_reviewed_at'], '2026-10-09')
        raw = next(r for r in gen.read('data/collective-intelligence-curation.json')['resources']
                   if r['id'] == 'paper-phase-engineering')
        self.assertEqual(gen.digest({k: v for k, v in raw.items() if k not in ('tier', 'problem_ids')}),
                         'd54689836c6084c61576c9df9bf1a8f79b64c3cf2f6c23866a5d026efd901556')
        expected = ['paper-growth', 'paper-phase-engineering', 'paper-vet', 'paper-alt', 'paper-cait']
        self.assertEqual(next(p for p in self.model['read_paths'] if p['id'] == 'reader')['resource_ids'], expected)
        for lang in ('en', 'ja'):
            page = gen.html(self.model, lang)
            core = page.split('id="core-papers"', 1)[1].split('</section>', 1)[0]
            supporting = page.split('id="supporting-research"', 1)[1].split('</section>', 1)[0]
            self.assertEqual(validation.Document(core).resources.count(r['id']), 1)
            self.assertNotIn(r['id'], validation.Document(supporting).resources)
            start = page.split('id="start-here"', 1)[1].split('</section>', 1)[0]
            self.assertIn(gen.page_url(lang) + '#' + r['id'], validation.Document(start).links)

    def test_rsi_explicit_bilingual_queries_and_negative_routing(self):
        p = next(p for p in self.model['problems'] if p['id'] == 'rsi-evidence')
        self.assertEqual(p['first_reads'], ['paper-phase-engineering', 'paper-growth', 'paper-cait'])
        self.assertEqual(p['symptom_group'], 'evaluation')
        for lang in ('en', 'ja'):
            for query in [p['question'][lang], *p['query_aliases'][lang]]:
                self.assertEqual(gen.route(self.model, query)['id'], p['id'])
        self.assertEqual(gen.route(self.model, '  RSI EVIDENCE ASSESSMENT?! ')['id'], p['id'])
        for query in ['RSI', 'rsi', 'relative strength index', 'banana',
                      'not RSI evidence assessment', 'RSI evidence assessment tomorrow',
                      '反復性緊張障害', 'RSIの株価指標', 'OAuth for agents',
                      'MCP token passthrough', 'slopsquatting', 'package hallucination']:
            self.assertIsNone(gen.route(self.model, query), query)
        forecast = next(p for p in self.model['problems'] if p['id'] == 'forecast')
        for query in [*forecast['question'].values(), *forecast['queries']]:
            self.assertEqual(gen.route(self.model, query)['id'], 'forecast')
        with self.assertRaises(ValueError):
            gen.validate_model(self.mutate(lambda m: m['problems'][-1]['query_aliases']['en'].append(
                'forecast when ASI will arrive')))

    def test_rsi_scientific_boundaries_are_bilingual_and_static(self):
        p = next(p for p in self.model['problems'] if p['id'] == 'rsi-evidence')
        phrases = {
            'en': ['Level 1', 'Level 2', 'Level 3', 'Iteration counts do not prove self-acceleration',
                   'score improvement is not improvement of the ability to improve',
                   'PASS is not proof of truth', 'unknown', 'independent external evaluation'],
            'ja': ['水準1', '水準2', '水準3', '反復回数は自己加速の証明ではなく',
                   'スコア改善は改善能力そのものの向上と同一ではない',
                   'PASSは真実の証明ではない', 'unknown（未確定）', '独立した外部評価']}
        for lang, required in phrases.items():
            body = ' '.join(p[k][lang] for k in ('required_inputs', 'expected_outputs',
                'prerequisite_or_unsupported_conditions', 'stop_or_handoff_conditions'))
            page, md = gen.html(self.model, lang), gen.markdown(self.model, lang)
            for phrase in required:
                self.assertIn(phrase, body)
                self.assertIn(gen.escape(phrase), page)
                self.assertIn(gen.md_text(phrase), md)

    def test_rsi_scope_preserves_existing_27_routes(self):
        self.assertEqual((len(self.model['resources']), len(self.model['roles']),
                          len(self.model['relations']), len(self.model['problems'])), (41, 13, 20, 28))
        raw = gen.read('data/collective-intelligence-curation.json')
        # Preserve the historical contract except the documented unavailable != absent translation fix.
        corrected = next(p for p in raw['problems'] if p['id'] == 'evidence-support')
        self.assertEqual(corrected['expected_outputs']['ja'], '取得・確認できない根拠と有限の最終性を明示した、主張と支持根拠の義務。')
        corrected['expected_outputs']['ja'] = '不在の根拠と有限の最終性を明示した、主張と支持根拠の義務。'
        self.assertEqual(gen.digest([p for p in raw['problems'] if p['id'] != 'rsi-evidence']),
                         '8171b3db25360d404f58b4677e34c3b102b8fb361846db06fa78cf069b222664')

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
            if r['id'] == 'paper-phase-engineering':
                self.assertEqual(r['last_reviewed_at'], '2026-10-09')
            elif r['id'] in {'sw-cio', 'sw-egr'}:
                self.assertEqual(r['last_reviewed_at'], '2026-10-06')
            elif r['id'] == 'sw-checkedflow':
                self.assertEqual(r['last_reviewed_at'], '2026-09-26')
            elif r['id'] in {'sw-cmgl', 'sw-memoryflow', 'sw-pfg', 'sw-fost', 'sw-atrb', 'sw-oversight'}:
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

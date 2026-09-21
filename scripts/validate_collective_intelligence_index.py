#!/usr/bin/env python3
"""Validate the offline registry, raw HTML, local URLs and generated parity."""
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator, FormatChecker
import generate_collective_intelligence_index as gen


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = []; self.resources = []; self.relations = []; self.links = []
        self.metadata = []; self.scripts = []; self.script = None; self.lang = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang = a.get('lang')
        if 'id' in a:
            self.ids.append(a['id'])
        if 'data-resource-id' in a:
            self.resources.append(a['data-resource-id'])
        if 'data-relation-id' in a:
            self.relations.append(a['data-relation-id'])
        if any(k.lower().startswith('on') for k in a):
            raise ValueError('Active event attribute')
        for k in ('href', 'src'):
            if k in a:
                self.links.append(a[k])
        if tag in ('link', 'meta'):
            self.metadata.append(a)
        if tag == 'script':
            if a.get('type') != 'application/ld+json' or 'src' in a:
                raise ValueError('Executable script is not required by this index')
            self.script = ''

    def handle_data(self, data):
        if self.script is not None:
            self.script += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.script is not None:
            self.scripts.append(json.loads(self.script)); self.script = None


def local_target(url, current, root):
    if url.startswith('#'):
        return current, unquote(url[1:])
    gen.safe_url(url)
    p = urlsplit(url)
    if p.netloc != 'kadubon.github.io':
        return None, None
    if not p.path.startswith('/github.io/'):
        raise ValueError('Published project URL escaped /github.io/')
    relative = unquote(p.path[len('/github.io/'):])
    target = root / relative
    if target.is_dir():
        target /= 'index.html'
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError('Local URL escaped workspace')
    return target, unquote(p.fragment)


def validate(root=None):
    root = root or gen.ROOT
    model = json.loads((root / (gen.STEM + '.json')).read_text(encoding='utf-8'))
    schema = json.loads((root / 'schemas/collective-intelligence-index.schema.json').read_text(encoding='utf-8'))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(model)
    gen.validate_model(model)
    for name, expected in gen.outputs(gen.build_model()).items():
        if (root / name).read_bytes() != expected:
            raise ValueError('Generated drift: ' + name)
    resources = {r['id'] for r in model['resources']}
    relations = {r['id'] for r in model['relations']}
    checked_links = 0
    for lang in ('en', 'ja'):
        path = root / (gen.STEM + ('.ja' if lang == 'ja' else '') + '.html')
        raw = path.read_text(encoding='utf-8'); doc = Document(raw)
        if doc.lang != lang or len(doc.ids) != len(set(doc.ids)):
            raise ValueError('Language or duplicate anchor error')
        if set(doc.resources) != resources or set(doc.relations) != relations:
            raise ValueError('Raw HTML resource/relation mismatch')
        if [a.get('href') for a in doc.metadata if a.get('rel') == 'canonical'] != [gen.page_url(lang)]:
            raise ValueError('Canonical mismatch')
        if {a.get('hreflang'): a.get('href') for a in doc.metadata if 'hreflang' in a} != {x: gen.page_url(x) for x in ('en', 'ja')}:
            raise ValueError('Hreflang mismatch')
        if any('noindex' in a.get('content', '') for a in doc.metadata):
            raise ValueError('Unexpected noindex')
        if doc.scripts != [gen.graph(model, lang)]:
            raise ValueError('JSON-LD mismatch')
        md = path.with_suffix('.md').read_text(encoding='utf-8')
        for r in model['resources']:
            if r['canonical_url'] not in doc.links or r['id'] not in md:
                raise ValueError('Missing initial HTML / Markdown resource')
            if gen.escape(r['limitations'][lang]) not in raw or gen.md_text(r['limitations'][lang]) not in md:
                raise ValueError('Limitations differ between representations')
        for r in model['relations']:
            if r['id'] not in md or gen.md_text(r['unsupported_obligations'][lang]) not in md:
                raise ValueError('Markdown relation boundary missing')
        for url in doc.links:
            target, anchor = local_target(url, path, root)
            if target is None:
                continue
            if not target.is_file():
                raise ValueError('Missing public local target: ' + url)
            if anchor and target.suffix == '.html' and anchor not in Document(target.read_text(encoding='utf-8')).ids:
                raise ValueError('Missing local anchor: ' + url)
            checked_links += 1
    for name in ('index.html', 'research-map.html', 'works.html', 'oss.html', 'agent-index.json', 'llms.txt', 'llms-full.txt'):
        if gen.BASE + gen.STEM + '.html' not in (root / name).read_text(encoding='utf-8'):
            raise ValueError('Missing discovery entry: ' + name)
    print(f'PASS: schema, digest, references, raw HTML/Markdown/JSON-LD parity; {checked_links} local links; {len(resources)} resources, {len(relations)} relationships.')
    return model


if __name__ == '__main__':
    validate()

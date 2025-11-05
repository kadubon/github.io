# -*- coding: utf-8 -*-
import re
import json
import time
import unicodedata
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

html_path = Path('works.html')
raw_bytes = html_path.read_bytes()
try:
    html_text = raw_bytes.decode('utf-8')
except UnicodeDecodeError:
    html_text = raw_bytes.decode('cp932')

pattern = re.compile(r'https://doi.org/[^"\s<>]+', re.I)
seen = {}
ordered_dois = []
for match in pattern.findall(html_text):
    clean = match.rstrip(').,;')
    if clean not in seen:
        seen[clean] = True
        ordered_dois.append(clean)

print(f'Found {len(ordered_dois)} cleaned DOIs')

def normalize_ascii(text):
    if text is None:
        return ''
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'\s+', ' ', text.strip())
    return text

def sanitize_ascii(text):
    text = normalize_ascii(text)
    result = []
    for ch in text:
        code = ord(ch)
        if code < 128:
            result.append(ch)
        else:
            if ch in ('–', '—', '―', '‑', '‒'):
                result.append('-')
            elif ch in ('“', '”'):
                result.append('"')
            elif ch in ('‘', '’'):
                result.append("'")
            elif ch == '…':
                result.append('...')
            elif ch in ('•', '·', '・'):
                result.append('-')
            elif ch == '©':
                result.append('(c)')
            elif ch == '™':
                result.append('TM')
            elif 0xFF61 <= code <= 0xFF9F:
                continue
            else:
                decomp = unicodedata.normalize('NFKD', ch)
                ascii_part = ''.join(c for c in decomp if ord(c) < 128)
                if ascii_part:
                    result.append(ascii_part)
    return ''.join(result)

def sanitize_for_html(text):
    text = sanitize_ascii(text)
    text = (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;'))
    return text

def sanitize_json(text):
    return sanitize_ascii(text)

metadata_records = []
for doi_url in ordered_dois:
    time.sleep(0.12)
    req = Request(doi_url, headers={'Accept': 'application/vnd.citationstyles.csl+json'})
    try:
        with urlopen(req) as resp:
            meta = json.load(resp)
    except HTTPError as e:
        print(f'Failed to fetch {doi_url}: {e}')
        continue
    issued = meta.get('issued', {}).get('date-parts', [])
    date_str = ''
    if issued and issued[0]:
        parts = issued[0]
        if len(parts) >= 3:
            date_str = f"{parts[0]:04d}-{parts[1]:02d}-{parts[2]:02d}"
        elif len(parts) == 2:
            date_str = f"{parts[0]:04d}-{parts[1]:02d}"
        else:
            date_str = f"{parts[0]:04d}"
    title = meta.get('title') or meta.get('name') or ''
    title_clean = sanitize_ascii(title)
    abstract = sanitize_json(meta.get('abstract') or '')
    if len(abstract) > 1200:
        abstract = abstract[:1197].rstrip() + '...'
    authors = []
    for auth in meta.get('author', []):
        given = sanitize_ascii(auth.get('given', ''))
        family = sanitize_ascii(auth.get('family', ''))
        name = ' '.join(part for part in [given, family] if part)
        if not name:
            literal = sanitize_ascii(auth.get('literal', ''))
            if literal:
                name = literal
        if name:
            authors.append(name)
    if not authors:
        authors = ['K. Takahashi']
    pub_type = (meta.get('type') or '').lower()
    type_map = {
        'article': 'Preprint',
        'journal-article': 'Article',
        'article-journal': 'Article',
        'report': 'Report',
        'book': 'Book',
        'chapter': 'Book Chapter',
        'dataset': 'Dataset',
        'software': 'Software'
    }
    publisher = sanitize_ascii(meta.get('publisher') or 'Zenodo')
    if pub_type in type_map:
        genre = type_map[pub_type]
    elif 'zenodo' in publisher.lower():
        genre = 'Preprint'
    else:
        genre = pub_type.title() if pub_type else 'Preprint'
    metadata_records.append({
        'doi_url': doi_url,
        'doi': doi_url.split('https://doi.org/')[-1],
        'title': title_clean,
        'date': date_str,
        'genre': genre,
        'authors': authors,
        'publisher': publisher,
        'abstract': abstract,
        'url': doi_url
    })

metadata_records.sort(key=lambda rec: (rec['date'], ordered_dois.index(rec['doi_url'])), reverse=True)

json_publications = []
for rec in metadata_records:
    authors_json = [{'@type': 'Person', 'name': name} for name in rec['authors']]
    citation = f"{rec['authors'][0]} ({rec['date']}). {rec['title']}. {rec['publisher']}. {rec['url']}"
    entry = {
        '@type': 'ScholarlyArticle',
        'name': rec['title'],
        'genre': rec['genre'],
        'url': rec['url'],
        'datePublished': rec['date'],
        'author': authors_json,
        'isPartOf': {
            '@type': 'Periodical',
            'name': rec['publisher'] or 'Zenodo'
        },
        'citation': citation
    }
    if rec['abstract']:
        entry['abstract'] = rec['abstract']
    json_publications.append(entry)

json_ld_obj = {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    'mainEntity': {
        '@type': 'Person',
        '@id': '#person',
        'name': 'K. Takahashi',
        'jobTitle': 'Researcher',
        'description': 'A researcher specializing in artificial intelligence, self-organizing systems, and computational philosophy.',
        'url': 'https://kadubon.github.io/github.io/',
        'knowsAbout': [
            'Artificial Intelligence',
            'Large Language Models',
            'AI Alignment',
            'AI Safety',
            'Superintelligence',
            'Computational Philosophy',
            'Self-Organizing Systems',
            'Category Theory',
            'Free Energy Principle',
            'Poiesis'
        ],
        'sameAs': [
            'https://orcid.org/0009-0004-4273-3365',
            'https://scholar.google.com/citations?view_op=list_works&hl=ja&hl=ja&user=0iEnSjkAAAAJ',
            'https://medium.com/@omanyuk',
            'https://x.com/YukiMiyake1919',
            'https://note.com/omanyuk',
            'https://independent.academia.edu/KTakahashi8',
            'https://huggingface.co/kadubon'
        ],
        'publication': json_publications
    }
}
json_ld_text = json.dumps(json_ld_obj, ensure_ascii=True, indent=2)

html_items = []
for rec in metadata_records:
    title_html = sanitize_for_html(rec['title'])
    date_html = sanitize_for_html(rec['date']) if rec['date'] else ''
    genre_html = sanitize_for_html(rec['genre'])
    doi_html = sanitize_for_html(rec['doi'])
    url_html = rec['url']
    meta_parts = [genre_html]
    if date_html:
        meta_parts.append(f"Published: {date_html}")
    meta_text = ' | '.join(meta_parts)
    item = f"     <li>\n      <div class=\"publication-item\">\n       <h3>\n        {title_html}\n       </h3>\n       <p>\n        <span class=\"publication-meta\">\n         {meta_text}\n        </span>\n        <a href=\"{url_html}\" target=\"_blank\">\n         DOI: {doi_html}\n        </a>\n       </p>\n      </div>\n     </li>"
    html_items.append(item)

new_publication_list = "    <ol class=\"publication-list\">\n" + "\n".join(html_items) + "\n    </ol>"

json_pattern = re.compile(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', re.S)
html_text = json_pattern.sub(lambda m: m.group(1) + json_ld_text + m.group(3), html_text)
list_pattern = re.compile(r'    <ol class="publication-list">.*?</ol>', re.S)
html_text = list_pattern.sub(new_publication_list, html_text)

html_path.write_text(html_text, encoding='utf-8')
print('Updated works.html with regenerated content.')

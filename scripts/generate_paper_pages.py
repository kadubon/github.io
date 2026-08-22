#!/usr/bin/env python3
"""Generate deterministic scholarly landing pages from research-catalog.json."""
from __future__ import annotations

import argparse
import concurrent.futures
import difflib
import html
import json
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
SITE_URL = "https://kadubon.github.io/github.io/"
ORCID = "https://orcid.org/0009-0004-4273-3365"
MARKER = "<!-- AUTO-GENERATED FROM research-catalog.json. DO NOT EDIT DIRECTLY. -->"


def dump(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def json_for_script(value: object) -> str:
    """Serialize JSON-LD without allowing metadata to terminate its script element."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")


def esc(value: object, quote: bool = True) -> str:
    return html.escape(str(value), quote=quote)


def zenodo_id(doi: str) -> str | None:
    match = re.fullmatch(r"10\.5281/zenodo\.(\d+)", doi.strip(), re.I)
    return match.group(1) if match else None


def valid_file_url(value: object) -> bool:
    parsed = urlparse(str(value))
    return parsed.scheme == "https" and parsed.hostname in {"zenodo.org", "www.zenodo.org"} and "/files/" in parsed.path


def canonical_file_url(value: str) -> str:
    """Use Zenodo's public record-file route when the API returns its content route."""
    match = re.fullmatch(r"/api/records/(\d+)/files/(.+)/content", urlparse(value).path)
    if not match:
        return value
    return f"https://zenodo.org/records/{match.group(1)}/files/{quote(unquote(match.group(2)), safe='')}"


def score(filename: str, title: str, size: int) -> int:
    name = filename.lower()
    words = re.sub(r"[^a-z0-9]+", " ", title.lower()).split()
    filename_words = re.sub(r"[^a-z0-9]+", " ", Path(filename).stem.lower()).split()
    result = 100 if name in {"paper.pdf", "manuscript.pdf", "main.pdf", "article.pdf", "preprint.pdf"} else 0
    result += min(30, 3 * sum(word in filename_words for word in words if len(word) > 3))
    # A filename that is the opening phrase of the exact title is stronger
    # evidence than scattered shared words in a different paper title.
    if filename_words and words[:len(filename_words)] == filename_words:
        result += 100
    result += int(25 * difflib.SequenceMatcher(a=" ".join(words), b=" ".join(filename_words)).ratio())
    result += min(10, size // 1_000_000)
    if any(part in name for part in ("supplement", "appendix", "slide", "poster", "figure", "license")):
        result -= 100
    return result


def select_pdf(record_id: str | None, candidates: list[dict[str, object]], title: str) -> dict[str, object]:
    ranked = []
    for candidate in candidates:
        value = dict(candidate)
        value["url"] = canonical_file_url(str(value["url"]))
        value["score"] = score(str(value["filename"]), title, int(value.get("size") or 0))
        ranked.append(value)
    ranked.sort(key=lambda item: (-int(item["score"]), str(item["filename"]).lower()))
    if len(ranked) == 1 or (len(ranked) > 1 and ranked[0]["score"] > ranked[1]["score"]):
        return {"record_id": record_id, "status": "PDF_RESOLVED", "pdf_url": ranked[0]["url"], "filename": ranked[0]["filename"], "candidates": ranked}
    status = "PDF_AMBIGUOUS" if ranked else "PDF_UNRESOLVED"
    return {"record_id": record_id, "status": status, "pdf_url": None, "candidates": ranked, "reason": "Multiple plausible Zenodo PDF files" if ranked else "No Zenodo PDF file"}


def resolve_pdf(doi: str, title: str, cache: dict[str, object], refresh: bool) -> dict[str, object]:
    record_id = zenodo_id(doi)
    cached = cache.get(doi)
    if isinstance(cached, dict) and cached.get("record_id") == record_id and not refresh:
        return select_pdf(record_id, list(cached.get("candidates", [])), title)
    if not record_id:
        return {"record_id": None, "status": "PDF_UNRESOLVED", "pdf_url": None, "candidates": [], "reason": "Not a Zenodo record DOI"}
    payload = None
    error = None
    request = Request(f"https://zenodo.org/api/records/{record_id}", headers={"Accept": "application/json", "User-Agent": "kadubon-paper-page-generator/1.0 (+https://kadubon.github.io/github.io/)"})
    for timeout in (8, 20, 40):
        try:
            with urlopen(request, timeout=timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
            break
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as caught:
            error = caught
            time.sleep(0.25)
    if payload is None:
        return {"record_id": record_id, "status": "PDF_UNRESOLVED", "pdf_url": None, "candidates": [], "reason": f"Zenodo API lookup failed after retries: {type(error).__name__}"}
    actual_dois = {str(payload.get("doi") or "").lower(), str(payload.get("metadata", {}).get("doi") or "").lower(), str(payload.get("conceptdoi") or "").lower(), str(payload.get("metadata", {}).get("conceptdoi") or "").lower()}
    # A concept DOI can legitimately resolve to the latest versioned Zenodo record.
    if doi.lower() not in actual_dois:
        return {"record_id": record_id, "status": "PDF_UNRESOLVED", "pdf_url": None, "candidates": [], "reason": "Zenodo DOI mismatch"}
    candidates = []
    for file in payload.get("files", []):
        filename = str(file.get("key") or file.get("filename") or "")
        mime = str(file.get("mimetype") or file.get("type") or "").lower()
        # Zenodo's current API exposes an authoritative per-file `self` content URL.
        # Older responses use `content` or `download`; all are direct file targets.
        url = file.get("links", {}).get("content") or file.get("links", {}).get("download") or file.get("links", {}).get("self")
        if (filename.lower().endswith(".pdf") or mime == "application/pdf") and valid_file_url(url):
            candidates.append({"filename": filename, "url": url, "size": int(file.get("size") or 0), "score": score(filename, title, int(file.get("size") or 0))})
    return select_pdf(record_id, candidates, title)


def meta_description(abstract: str) -> str:
    text = " ".join(abstract.split())
    return text if len(text) <= 300 else text[:297].rsplit(" ", 1)[0] + "..."


def jsonld(record: dict[str, object], resolution: dict[str, object]) -> dict[str, object]:
    url = str(record["landing_page_url"])
    authors = [{"@type": "Person", "name": name, "identifier": ORCID, "sameAs": [ORCID, SITE_URL, "https://github.com/kadubon"]} for name in record["authors"]]
    value: dict[str, object] = {"@context": "https://schema.org", "@type": "ScholarlyArticle", "@id": url + "#article", "url": url, "mainEntityOfPage": url, "headline": record["title"], "author": authors, "datePublished": record["date_published"], "description": record["abstract"], "keywords": record["keywords"], "inLanguage": record.get("in_language", "en"), "genre": record.get("genre", "Preprint"), "identifier": {"@type": "PropertyValue", "propertyID": "DOI", "value": record["doi"]}, "sameAs": [record["doi_url"]], "isPartOf": {"@type": "CollectionPage", "url": SITE_URL + "works.html"}}
    if resolution.get("status") == "PDF_RESOLVED":
        value["encoding"] = {"@type": "MediaObject", "contentUrl": resolution["pdf_url"], "encodingFormat": "application/pdf"}
    return value


def render_page(record: dict[str, object], resolution: dict[str, object]) -> str:
    iso = str(record["date_published"])[:10]
    citation_date = iso.replace("-", "/")
    abstract = str(record["abstract"])
    pdf_url = resolution.get("pdf_url") if resolution.get("status") == "PDF_RESOLVED" else None
    citation_authors = "\n".join(f'  <meta name="citation_author" content="{esc(author)}">' for author in record["authors"])
    citation_pdf = f'\n  <meta name="citation_pdf_url" content="{esc(pdf_url)}">' if pdf_url else ""
    keywords = "".join(f"<li>{esc(keyword)}</li>" for keyword in record["keywords"])
    full_text = f'<p><a href="{esc(pdf_url)}">Full text PDF (Zenodo)</a></p>' if pdf_url else ""
    body = f'''{MARKER}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(record["title"])} | K. Takahashi</title>
  <meta name="description" content="{esc(meta_description(abstract))}">
  <meta name="author" content="{esc(record["authors"][0] if record["authors"] else "K. Takahashi")}">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta name="googlebot" content="index,follow,max-snippet:-1">
  <meta name="citation_title" content="{esc(record["title"])}">
{citation_authors}
  <meta name="citation_publication_date" content="{citation_date}">
  <meta name="citation_doi" content="{esc(record["doi"])}">{citation_pdf}
  <link rel="canonical" href="{esc(record["landing_page_url"])}">
  <link rel="stylesheet" href="{SITE_URL}style.css">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{esc(record["title"])}">
  <meta property="og:description" content="{esc(meta_description(abstract))}">
  <meta property="og:url" content="{esc(record["landing_page_url"])}">
  <meta property="article:published_time" content="{esc(record["date_published"])}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{esc(record["title"])}">
  <meta name="twitter:description" content="{esc(meta_description(abstract))}">
  <style>body{{margin:0;color:#111;background:#fff;font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}header,main,footer{{max-width:54rem;margin:auto;padding:1rem}}nav ul,.keywords{{display:flex;gap:.4rem 1rem;flex-wrap:wrap;padding:0;list-style:none}}a{{color:#0645ad}}article{{border-top:1px solid #ccc;padding-top:1rem}}h1,h2{{line-height:1.2}}.eyebrow{{font-size:.85rem;text-transform:uppercase;letter-spacing:.04em;color:#444}}dl{{display:grid;grid-template-columns:max-content 1fr;gap:.3rem 1rem}}dt{{font-weight:700}}dd{{margin:0}}.abstract{{white-space:pre-wrap}}@media(max-width:36rem){{body{{font-size:15px}}header,main,footer{{padding:.85rem}}dl{{grid-template-columns:1fr}}}}</style>
  <script type="application/ld+json">{json_for_script(jsonld(record, resolution))}</script>
</head>
<body>
  <header><nav aria-label="Site navigation"><ul><li><a href="{SITE_URL}">Home</a></li><li><a href="{SITE_URL}works.html">Works</a></li><li><a href="{SITE_URL}papers/">Papers</a></li><li><a href="{ORCID}">ORCID</a></li></ul></nav></header>
  <main><article>
    <p class="eyebrow">{esc(record.get("genre", "Preprint"))} / scholarly article</p>
    <h1>{esc(record["title"])}</h1>
    <p class="authors">{esc(", ".join(record["authors"]))}</p>
    <dl><dt>Published</dt><dd><time datetime="{esc(record["date_published"])}">{iso}</time></dd><dt>DOI</dt><dd><a href="{esc(record["doi_url"])}">{esc(record["doi"])}</a></dd></dl>
    {full_text}
    <section><h2>Abstract</h2><p class="abstract">{esc(abstract)}</p></section>
    <section><h2>Keywords</h2><ul class="keywords">{keywords}</ul></section>
    <section><h2>Identifiers and source records</h2><ul><li><a href="{esc(record["doi_url"])}">DOI</a></li><li><a href="{esc(record["local_record_url"])}">Works entry</a></li><li><a href="{ORCID}">ORCID</a></li></ul></section>
  </article></main>
  <footer><p><a href="{SITE_URL}">K. Takahashi Research Hub</a></p></footer>
</body></html>
'''
    return body


def render_index(records: list[dict[str, object]]) -> str:
    entries = []
    for record in records:
        keywords = ", ".join(esc(keyword) for keyword in record["keywords"][:4])
        extra = " <span>" + keywords + "</span>" if keywords else ""
        entries.append(f'<li><time datetime="{esc(record["date_published"])}">{esc(str(record["date_published"])[:10])}</time> — <a href="{esc(record["landing_page_url"])}">{esc(record["title"])}</a> — <a href="{esc(record["doi_url"])}">DOI</a>{extra}</li>')
    itemlist = {"@context": "https://schema.org", "@type": "ItemList", "name": "K. Takahashi scholarly paper landing pages", "numberOfItems": len(records), "itemListOrder": "https://schema.org/ItemListOrderDescending", "itemListElement": [{"@type": "ListItem", "position": index, "url": record["landing_page_url"], "name": record["title"]} for index, record in enumerate(records, 1)]}
    head = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Papers | K. Takahashi</title><meta name="description" content="Static landing-page index for K. Takahashi scholarly papers."><meta name="robots" content="index,follow,max-snippet:-1"><link rel="canonical" href="' + SITE_URL + 'papers/"><link rel="stylesheet" href="' + SITE_URL + 'style.css"><style>body{margin:0;font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#111}header,main,footer{max-width:70rem;margin:auto;padding:1rem}a{color:#0645ad}li{margin:.7rem 0}span{color:#444;font-size:.9em}</style><script type="application/ld+json">' + json_for_script(itemlist) + '</script></head>'
    body = '<body><header><nav aria-label="Site navigation"><a href="' + SITE_URL + '">Home</a> · <a href="' + SITE_URL + 'works.html">Works</a> · <a href="' + ORCID + '">ORCID</a></nav></header><main><h1>Scholarly papers</h1><p>' + str(len(records)) + ' scholarly articles. This index is reverse chronological and JavaScript-independent.</p><p><a href="' + SITE_URL + 'research-catalog.json">Research catalog</a> · <a href="' + SITE_URL + 'papers/index.json">Machine-readable papers index</a></p><ol>' + ''.join(entries) + '</ol></main><footer><p>K. Takahashi Research Hub</p></footer></body></html>\n'
    return MARKER + "\n" + head + body


def sync_sitemap(paper_urls: list[str]) -> None:
    path = ROOT / "sitemap.xml"
    original = ET.parse(path).getroot()
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    existing = [node.findtext(namespace + "loc") or "" for node in original.findall(namespace + "url")]
    remaining = [url for url in existing if not url.startswith(SITE_URL + "papers/")]
    root = ET.Element(namespace + "urlset")
    for url in sorted(set(remaining + paper_urls)):
        node = ET.SubElement(root, namespace + "url")
        ET.SubElement(node, namespace + "loc").text = url
    ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)


def clean_stale(slugs: set[str]) -> None:
    if not PAPERS.exists():
        return
    for directory in PAPERS.iterdir():
        if not directory.is_dir() or directory.name in slugs:
            continue
        page = directory / "index.html"
        if page.is_file() and page.read_text(encoding="utf-8", errors="ignore").startswith(MARKER):
            page.unlink()
            directory.rmdir()


def main() -> int:
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--refresh-zenodo", action="store_true", help="Refresh cached Zenodo record metadata.")
    args.add_argument("--retry-unresolved", action="store_true", help="Re-query only cached unresolved or ambiguous PDF records.")
    options = args.parse_args()
    catalog = json.loads((ROOT / "research-catalog.json").read_text(encoding="utf-8"))
    records = [record for record in catalog["records"] if record.get("record_type") == "scholarly_article"]
    slugs = [str(record["slug"]) for record in records]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Slug collision: generation stopped before writing files")
    cache_path = ROOT / "data" / "zenodo-pdf-map.json"
    cache_path.parent.mkdir(exist_ok=True)
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    resolutions: dict[str, dict[str, object]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        pending = {executor.submit(resolve_pdf, str(record["doi"]), str(record["title"]), cache, options.refresh_zenodo or (options.retry_unresolved and isinstance(cache.get(str(record["doi"])), dict) and cache[str(record["doi"])].get("status") in {"PDF_UNRESOLVED", "PDF_AMBIGUOUS"})): record for record in records}
        for future in concurrent.futures.as_completed(pending):
            record = pending[future]
            result = future.result()
            cache[str(record["doi"])] = result
            resolutions[str(record["doi"])] = result
    cache_path.write_text(dump(dict(sorted(cache.items()))), encoding="utf-8")
    PAPERS.mkdir(exist_ok=True)
    clean_stale(set(slugs))
    index_records = []
    for record in records:
        resolution = resolutions[str(record["doi"])]
        target = PAPERS / str(record["slug"])
        target.mkdir(exist_ok=True)
        (target / "index.html").write_text(render_page(record, resolution), encoding="utf-8")
        index_records.append({"title": record["title"], "authors": record["authors"], "date_published": record["date_published"], "doi": record["doi"], "doi_url": record["doi_url"], "landing_page_url": record["landing_page_url"], "zenodo_pdf_url": resolution.get("pdf_url"), "pdf_status": resolution.get("status"), "works_entry_url": record["local_record_url"], "keywords": record["keywords"]})
    (PAPERS / "index.html").write_text(render_index(records), encoding="utf-8")
    (PAPERS / "index.json").write_text(dump({"schema_version": "1.0", "index_type": "scholarly_paper_landing_pages", "canonical_url": SITE_URL + "papers/index.json", "source_catalog": SITE_URL + "research-catalog.json", "creator": {"name": "K. Takahashi", "orcid": ORCID, "website": SITE_URL}, "paper_count": len(index_records), "papers": index_records}), encoding="utf-8")
    sync_sitemap([SITE_URL + "papers/"] + [str(record["landing_page_url"]) for record in records])
    statuses = {state: sum(1 for item in resolutions.values() if item.get("status") == state) for state in ("PDF_RESOLVED", "PDF_UNRESOLVED", "PDF_AMBIGUOUS")}
    print(f"Generated {len(records)} paper pages; " + ", ".join(f"{state}={count}" for state, count in statuses.items()))
    for record in records:
        result = resolutions[str(record["doi"])]
        if result.get("status") == "PDF_AMBIGUOUS":
            print(f"PDF_AMBIGUOUS {record['doi']} | {record['title']} | " + ", ".join(str(item['filename']) for item in result.get('candidates', [])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

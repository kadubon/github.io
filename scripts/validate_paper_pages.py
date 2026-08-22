#!/usr/bin/env python3
"""Validate generated scholarly-paper landing-page invariants."""
from __future__ import annotations

import json
import html
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://kadubon.github.io/github.io/"
MARKER = "<!-- AUTO-GENERATED FROM research-catalog.json. DO NOT EDIT DIRECTLY. -->"


class Scripts(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.jsonld = False
        self.parts: list[str] = []
    def handle_starttag(self, tag, attrs):
        self.jsonld = tag == "script" and dict(attrs).get("type") == "application/ld+json"
    def handle_endtag(self, tag):
        if tag == "script": self.jsonld = False
    def handle_data(self, data):
        if self.jsonld: self.parts.append(data)


def check(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    catalog = json.loads((ROOT / "research-catalog.json").read_text(encoding="utf-8"))
    all_records = catalog["records"]
    records = [record for record in all_records if record["record_type"] == "scholarly_article"]
    software = [record for record in all_records if record["record_type"] != "scholarly_article"]
    papers = json.loads((ROOT / "papers" / "index.json").read_text(encoding="utf-8"))
    check(len(records) == papers["paper_count"], "catalog/index paper counts differ", failures)
    check(len(all_records) == catalog["record_count"], "research catalog record count differs", failures)
    check(len({record["doi"] for record in records}) == len(records), "duplicate DOI", failures)
    check(len({record["slug"] for record in records}) == len(records), "duplicate slug", failures)
    sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
    sitemap_urls = [node.text for node in sitemap.iter() if node.tag.endswith("loc") and node.text]
    check(len(sitemap_urls) == len(set(sitemap_urls)), "duplicate sitemap URLs", failures)
    index_urls = {item["landing_page_url"] for item in papers["papers"]}
    html_index = (ROOT / "papers" / "index.html").read_text(encoding="utf-8")
    for record in records:
        page = ROOT / "papers" / record["slug"] / "index.html"
        check(page.is_file(), f"missing page: {record['slug']}", failures)
        if not page.is_file(): continue
        text = page.read_text(encoding="utf-8")
        plain = html.unescape(text)
        check(text.startswith(MARKER), f"missing marker: {record['slug']}", failures)
        for expected, label in ((record["title"], "title"), (record["abstract"], "abstract"), (record["doi"], "DOI"), (record["landing_page_url"], "canonical URL"), (record["local_record_url"], "Works link")):
            check(expected in plain, f"{label} not exact: {record['slug']}", failures)
        for author in record["authors"]:
            check(author in text, f"author absent: {record['slug']}", failures)
        check('<h1>' in text and '<h2>Abstract</h2>' in text and 'noindex' not in text.lower(), f"semantic/noindex issue: {record['slug']}", failures)
        parser = Scripts(); parser.feed(text)
        try:
            data = next(json.loads(part) for part in parser.parts if json.loads(part).get("@type") == "ScholarlyArticle")
            check(data["headline"] == record["title"] and data["description"] == record["abstract"], f"JSON-LD mismatch: {record['slug']}", failures)
            encoding = data.get("encoding")
            item = next(x for x in papers["papers"] if x["doi"] == record["doi"])
            if item["zenodo_pdf_url"]:
                url = item["zenodo_pdf_url"]
                parsed = urlparse(url)
                check(parsed.scheme == "https" and parsed.hostname in {"zenodo.org", "www.zenodo.org"} and "/files/" in parsed.path, f"invalid PDF URL: {record['slug']}", failures)
                check(url in text and encoding and encoding.get("contentUrl") == url and encoding.get("encodingFormat") == "application/pdf", f"PDF metadata mismatch: {record['slug']}", failures)
            else:
                check(not encoding, f"unresolved PDF has encoding: {record['slug']}", failures)
        except (StopIteration, json.JSONDecodeError, KeyError, TypeError) as error:
            failures.append(f"invalid JSON-LD: {record['slug']} ({error})")
        check(record["landing_page_url"] in sitemap_urls, f"not in sitemap: {record['slug']}", failures)
        check(record["landing_page_url"] in index_urls and record["landing_page_url"] in html_index, f"not in paper indexes: {record['slug']}", failures)
    agent = json.loads((ROOT / "agent-index.json").read_text(encoding="utf-8"))
    check(agent["entry_points"].get("paper_landing_index") == SITE_URL + "papers/", "agent index lacks papers entry point", failures)
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8") + (ROOT / "llms-full.txt").read_text(encoding="utf-8")
    check(SITE_URL + "papers/" in llms and SITE_URL + "papers/index.json" in llms, "LLMS routing lacks papers pointers", failures)
    statuses = {}
    for item in papers["papers"]: statuses[item["pdf_status"]] = statuses.get(item["pdf_status"], 0) + 1
    print(f"Validated {len(records)} scholarly pages and {len(software)} software records. " + ", ".join(f"{key}={value}" for key, value in sorted(statuses.items())))
    if failures:
        print("VALIDATION FAILED", file=sys.stderr)
        print("\n".join(failures[:100]), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

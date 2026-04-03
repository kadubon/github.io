#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, time, timezone, timedelta
import email.utils as eut
import html
import re

SITE_URL = "https://kadubon.github.io/github.io/"
WORKS_URL = "https://kadubon.github.io/github.io/works.html"
FEED_URL = "https://kadubon.github.io/github.io/feed.xml"
FEED_TITLE = "K. Takahashi — Research Updates"
FEED_DESC = "Research preprints and theoretical works by K. Takahashi"
FEED_LANG = "en"
JST = timezone(timedelta(hours=9))

root = Path(__file__).resolve().parents[1]
works_path = root / "works.html"
feed_path = root / "feed.xml"

ARTICLE_RE = re.compile(r'<article class="publication" id="([^"]+)">(.*?)</article>', re.S)
TITLE_RE = re.compile(r'<h3><a href="#[^"]+">(.*?)</a></h3>', re.S)
AUTHORS_RE = re.compile(r'<div><dt>Authors</dt><dd>(.*?)</dd></div>', re.S)
TYPE_RE = re.compile(r'<div><dt>Type</dt><dd>(.*?)</dd></div>', re.S)
DATE_RE = re.compile(r'<time datetime="([0-9]{4}-[0-9]{2}-[0-9]{2})">')
DOI_RE = re.compile(r'<div><dt>DOI</dt><dd><a href="https://doi.org/([^"]+)">', re.S)
SUMMARY_RE = re.compile(r'<p class="publication-summary">(.*?)</p>', re.S)
KEYWORD_BLOCK_RE = re.compile(r'<ul class="keyword-list" aria-label="Keywords">(.*?)</ul>', re.S)
KEYWORD_RE = re.compile(r"<li>(.*?)</li>", re.S)


def unescape_recursive(text: str) -> str:
    prev = None
    cur = text
    while cur != prev:
        prev = cur
        cur = html.unescape(cur)
    return cur


def clean_text(text: str) -> str:
    return " ".join(unescape_recursive(text).replace("\xa0", " ").split())


def xml_esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def first_match(pattern: re.Pattern[str], text: str, default: str = "") -> str:
    match = pattern.search(text)
    return match.group(1) if match else default


html_text = works_path.read_text(encoding="utf-8", errors="ignore")
articles = ARTICLE_RE.findall(html_text)
if not articles:
    raise SystemExit(f"No publication articles found in {works_path}")

items = []
for position, (slug, article_html) in enumerate(articles, 1):
    title = clean_text(first_match(TITLE_RE, article_html, "Untitled"))
    authors = clean_text(first_match(AUTHORS_RE, article_html, "K. Takahashi"))
    pub_type = clean_text(first_match(TYPE_RE, article_html, "Work"))
    date_str = first_match(DATE_RE, article_html, "")
    doi = first_match(DOI_RE, article_html, "").lower()
    summary = clean_text(first_match(SUMMARY_RE, article_html, ""))

    keywords = []
    keyword_block = first_match(KEYWORD_BLOCK_RE, article_html, "")
    if keyword_block:
        keywords = [clean_text(x) for x in KEYWORD_RE.findall(keyword_block)]

    link = f"{WORKS_URL}#{slug}"
    pub_date = None
    if date_str:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        dt = datetime.combine(dt.date(), time(0, 0, 0), tzinfo=JST)
        pub_date = eut.format_datetime(dt)

    items.append(
        {
            "position": position,
            "slug": slug,
            "title": title,
            "authors": authors,
            "type": pub_type,
            "date": date_str,
            "pubDate": pub_date,
            "doi": doi,
            "doi_url": f"https://doi.org/{doi}" if doi else "",
            "link": link,
            "guid": link,
            "summary": summary,
            "keywords": keywords,
        }
    )

now = eut.format_datetime(datetime.now(tz=JST))
rss = []
rss.append('<?xml version="1.0" encoding="UTF-8"?>')
rss.append('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">')
rss.append("<channel>")
rss.append(f"  <title>{xml_esc(FEED_TITLE)}</title>")
rss.append(f"  <link>{xml_esc(SITE_URL)}</link>")
rss.append(f"  <description>{xml_esc(FEED_DESC)}</description>")
rss.append(f"  <language>{FEED_LANG}</language>")
rss.append(f"  <lastBuildDate>{now}</lastBuildDate>")
rss.append(f'  <atom:link rel="self" type="application/rss+xml" href="{xml_esc(FEED_URL)}" />')

for item in items:
    description_parts = []
    if item["summary"]:
        description_parts.append(item["summary"])
    meta = []
    if item["type"]:
        meta.append(item["type"])
    if item["doi"]:
        meta.append(f"DOI: {item['doi']}")
    if meta:
        description_parts.append(" | ".join(meta))
    description = "\n".join(description_parts).strip()

    rss.append("  <item>")
    rss.append(f"    <title>{xml_esc(item['title'])}</title>")
    rss.append(f"    <link>{xml_esc(item['link'])}</link>")
    rss.append(f'    <guid isPermaLink="true">{xml_esc(item["guid"])}</guid>')
    if item["pubDate"]:
        rss.append(f"    <pubDate>{item['pubDate']}</pubDate>")
    rss.append(f"    <dc:creator>{xml_esc(item['authors'])}</dc:creator>")
    if item["type"]:
        rss.append(f"    <category>{xml_esc(item['type'])}</category>")
    for keyword in item["keywords"]:
        rss.append(f"    <category>{xml_esc(keyword)}</category>")
    if item["doi_url"]:
        rss.append(f"    <source url=\"{xml_esc(item['doi_url'])}\">{xml_esc(item['doi'])}</source>")
    rss.append("    <description><![CDATA[")
    rss.append(f"      {description}")
    rss.append("    ]]></description>")
    rss.append("  </item>")

rss.append("</channel>")
rss.append("</rss>")

feed_path.write_text("\n".join(rss) + "\n", encoding="utf-8")
print(f"Wrote {feed_path} with {len(items)} items.")

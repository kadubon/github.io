#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from bs4 import BeautifulSoup
import re
from datetime import datetime, time, timezone, timedelta
import email.utils as eut

# ====== サイト/フィード設定 ======
SITE_URL   = "https://kadubon.github.io/github.io/"
FEED_URL   = "https://kadubon.github.io/github.io/feed.xml"
FEED_TITLE = "K. Takahashi — Research Updates"
FEED_DESC  = "Research preprints and theoretical works by K. Takahashi"
FEED_LANG  = "en"
JST        = timezone(timedelta(hours=9))

# ====== 著者/ORCID（ご指定の値） ======
AUTHOR_NAME  = "K. Takahashi"
AUTHOR_ORCID = "https://orcid.org/0009-0004-4273-3365"

# ====== 入出力 ======
root = Path(__file__).resolve().parents[1]
works_path = root / "works.html"
feed_path  = root / "feed.xml"

html = works_path.read_text(encoding="utf-8", errors="ignore")
soup = BeautifulSoup(html, "html.parser")

# ====== 抽出ロジック ======
DOI_CORE   = re.compile(r"(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", re.IGNORECASE)
PUBLISHED  = re.compile(r"Published:\s*(\d{4}-\d{2}-\d{2})")
TYPE_WORDS = ("Preprint", "Working paper", "Other", "Book review", "Report")

def extract_doi(a):
    href = a.get("href", "") or ""
    m = DOI_CORE.search(href) or DOI_CORE.search(a.get_text(" ", strip=True))
    return m.group(1) if m else None

# doi.org アンカーを列挙
doi_anchors = []
for a in soup.find_all("a", href=True):
    if "doi.org" in a["href"]:
        doi = extract_doi(a)
        if doi:
            doi_anchors.append((a, doi))

# sourcepos 代替（文書順を安定化）
pos = 0
for el in soup.descendants:
    if getattr(el, "name", None):
        pos += 1
        setattr(el, "sourcepos", pos)

def nearest_heading(node):
    for el in node.previous_elements:
        if getattr(el, "name", None) in ("h1","h2","h3","h4"):
            return el
    return None

def block_text_between(head):
    texts = []
    for sib in head.next_siblings:
        if getattr(sib, "name", None) in ("h1","h2","h3","h4"):
            break
        texts.append(getattr(sib, "get_text", lambda **k: str(sib))(" ", strip=True))
    return " ".join(t for t in texts if t)

def find_kind_and_date(head):
    blob = block_text_between(head)
    kind = next((kw for kw in TYPE_WORDS if kw.lower() in blob.lower()), None)
    m = PUBLISHED.search(blob)
    pub = m.group(1) if m else None
    return kind, pub

def xml_esc(s: str) -> str:
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# ====== アイテム化 ======
items, seen = [], set()
for a, doi in doi_anchors:
    key = doi.lower()
    if key in seen:
        continue
    h = nearest_heading(a)
    title = (h.get_text(" ", strip=True) if h else a.get_text(" ", strip=True)) or "Untitled"
    kind, pub = (find_kind_and_date(h) if h else (None, None))
    pubDate = None
    if pub:
        try:
            d = datetime.strptime(pub, "%Y-%m-%d")
            d = datetime.combine(d.date(), time(0,0,0), tzinfo=JST)
            pubDate = eut.format_datetime(d)
        except Exception:
            pass
    link = f"https://doi.org/{doi}"
    items.append({
        "title": title,
        "link": link,
        "guid": link,
        "doi": doi,
        "kind": kind or "Work",
        "pubDate": pubDate,
        "pos": getattr(a, "sourcepos", 0)
    })
    seen.add(key)

items.sort(key=lambda x: x["pos"])

# ====== RSS 2.0 + Atom/Dublin Core 拡張で出力 ======
now = eut.format_datetime(datetime.now(tz=JST))
rss = []
rss.append('<?xml version="1.0" encoding="UTF-8"?>')
rss.append('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">')
rss.append('<channel>')
rss.append(f'  <title>{xml_esc(FEED_TITLE)}</title>')
rss.append(f'  <link>{xml_esc(SITE_URL)}</link>')
rss.append(f'  <description>{xml_esc(FEED_DESC)}</description>')
rss.append(f'  <language>{FEED_LANG}</language>')
rss.append(f'  <lastBuildDate>{now}</lastBuildDate>')
# 自己参照（推奨）
rss.append(f'  <atom:link rel="self" type="application/rss+xml" href="{xml_esc(FEED_URL)}" />')
# チャンネル著者（ORCID付き）
rss.append('  <atom:author>')
rss.append(f'    <atom:name>{xml_esc(AUTHOR_NAME)}</atom:name>')
rss.append(f'    <atom:uri>{xml_esc(AUTHOR_ORCID)}</atom:uri>')
rss.append('  </atom:author>')

for it in items:
    rss.append('  <item>')
    rss.append(f'    <title>{xml_esc(it["title"])}</title>')
    rss.append(f'    <link>{xml_esc(it["link"])}</link>')
    rss.append(f'    <guid isPermaLink="true">{xml_esc(it["guid"])}</guid>')
    if it["pubDate"]:
        rss.append(f'    <pubDate>{it["pubDate"]}</pubDate>')
    # アイテム著者（機械可読）
    rss.append(f'    <dc:creator>{xml_esc(AUTHOR_NAME)}</dc:creator>')
    rss.append('    <atom:author>')
    rss.append(f'      <atom:name>{xml_esc(AUTHOR_NAME)}</atom:name>')
    rss.append(f'      <atom:uri>{xml_esc(AUTHOR_ORCID)}</atom:uri>')
    rss.append('    </atom:author>')
    # 簡潔説明
    desc = f'{it["kind"]} — DOI: {it["doi"]}'
    rss.append('    <description><![CDATA[')
    rss.append(f'      {desc}')
    rss.append('    ]]></description>')
    rss.append('  </item>')

rss.append('</channel>')
rss.append('</rss>')

feed_path.write_text("\n".join(rss) + "\n", encoding="utf-8")
print(f"Wrote {feed_path} with {len(items)} items (ORCID={AUTHOR_ORCID}).")



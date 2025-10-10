#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from bs4 import BeautifulSoup
import re
from datetime import datetime, time, timezone, timedelta
import email.utils as eut

# ====== サイト設定 ======
SITE_URL   = "https://kadubon.github.io/github.io/"
FEED_TITLE = "K. Takahashi — Research Updates"
FEED_DESC  = "Research preprints and theoretical works by K. Takahashi"
FEED_LANG  = "en"
JST        = timezone(timedelta(hours=9))

root = Path(__file__).resolve().parents[1]
works_path = root / "works.html"
feed_path  = root / "feed.xml"

html = works_path.read_text(encoding="utf-8", errors="ignore")
soup = BeautifulSoup(html, "html.parser")

# DOI抽出（hrefかテキスト）。大文字混在も許容
DOI_CORE = re.compile(r"(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", re.IGNORECASE)
PUBLISHED = re.compile(r"Published:\s*(\d{4}-\d{2}-\d{2})")
TYPE_WORDS = ("Preprint", "Working paper", "Other", "Book review", "Report")

def extract_doi(a):
    # href優先
    href = a.get("href", "") or ""
    m = DOI_CORE.search(href)
    if m:
        return m.group(1)
    # テキストにも DOI がある場合
    m = DOI_CORE.search(a.get_text(" ", strip=True))
    if m:
        return m.group(1)
    return None

# すべての doi.org アンカーを列挙（順序保持）
doi_anchors = []
for a in soup.find_all("a", href=True):
    if "doi.org" in a["href"]:
        doi = extract_doi(a)
        if doi:
            doi_anchors.append((a, doi))

def nearest_heading(node):
    """node から遡って直近の見出し(h1–h4)を返す。なければ None"""
    for prev in node.parents:
        # 同一ブロック内の見出しを優先
        for h in prev.find_all(["h1","h2","h3","h4"], recursive=False):
            if h.sourcepos and node.sourcepos and h.sourcepos < node.sourcepos:
                return h
    # さらに全体から previous_elements で遡る
    for el in node.previous_elements:
        if getattr(el, "name", None) in ("h1","h2","h3","h4"):
            return el
    return None

def block_text_between(head):
    """見出し head から次の見出しまでのテキスト（抽出用）"""
    texts = []
    # 兄弟を順に歩き、次の見出しが来るまで収集
    for sib in head.next_siblings:
        if getattr(sib, "name", None) in ("h1","h2","h3","h4"):
            break
        texts.append(getattr(sib, "get_text", lambda **k: str(sib))(" ", strip=True))
    return " ".join(t for t in texts if t)

def find_kind_and_date(head):
    """見出しブロック内から種別と公開日を拾う"""
    blob = block_text_between(head)
    kind = None
    for kw in TYPE_WORDS:
        if kw.lower() in blob.lower():
            kind = kw
            break
    pub = None
    m = PUBLISHED.search(blob)
    if m:
        pub = m.group(1)
    return kind, pub

def xml_esc(s: str) -> str:
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

items = []
seen = set()

# BeautifulSoup の Tag に sourcepos が無い実装もあるので埋める（順序用）
# fallback: enumerate順で surrogate position を割当て
pos = 0
for el in soup.descendants:
    if getattr(el, "name", None):
        pos += 1
        setattr(el, "sourcepos", pos)

for a, doi in doi_anchors:
    key = doi.lower()
    if key in seen:
        continue
    # 直近見出しを取る → タイトル
    h = nearest_heading(a)
    if h is None:
        # 見出しが無い場合は、アンカー親の周辺テキストからタイトル候補
        title = a.get_text(" ", strip=True)
    else:
        title = h.get_text(" ", strip=True)
    kind, pub = (None, None)
    if h is not None:
        kind, pub = find_kind_and_date(h)
    # pubDate
    pubDate = None
    if pub:
        try:
            d = datetime.strptime(pub, "%Y-%m-%d")
            d = datetime.combine(d.date(), time(0, 0, 0), tzinfo=JST)
            pubDate = eut.format_datetime(d)
        except Exception:
            pubDate = None

    link = f"https://doi.org/{doi}"
    items.append({
        "title": title or "Untitled",
        "link": link,
        "guid": link,
        "doi": doi,
        "kind": kind or "Work",
        "pubDate": pubDate,
        "pos": getattr(a, "sourcepos", 0)
    })
    seen.add(key)

# 文書順でソート（見出し/アンカーの出現順）
items.sort(key=lambda x: x["pos"])

# RSS 2.0 を出力
now = eut.format_datetime(datetime.now(tz=JST))
rss = []
rss.append('<?xml version="1.0" encoding="UTF-8"?>')
rss.append('<rss version="2.0">')
rss.append('<channel>')
rss.append(f'  <title>{xml_esc(FEED_TITLE)}</title>')
rss.append(f'  <link>{xml_esc(SITE_URL)}</link>')
rss.append(f'  <description>{xml_esc(FEED_DESC)}</description>')
rss.append(f'  <language>{FEED_LANG}</language>')
rss.append(f'  <lastBuildDate>{now}</lastBuildDate>')

for it in items:
    rss.append('  <item>')
    rss.append(f'    <title>{xml_esc(it["title"])}</title>')
    rss.append(f'    <link>{xml_esc(it["link"])}</link>')
    rss.append(f'    <guid>{xml_esc(it["guid"])}</guid>')
    if it["pubDate"]:
        rss.append(f'    <pubDate>{it["pubDate"]}</pubDate>')
    desc = f'{it["kind"]} — DOI: {it["doi"]}'
    rss.append('    <description><![CDATA[')
    rss.append(f'      {desc}')
    rss.append('    ]]></description>')
    rss.append('  </item>')

rss.append('</channel>')
rss.append('</rss>')
feed_path.write_text("\n".join(rss) + "\n", encoding="utf-8")

print(f"Wrote {feed_path} with {len(items)} items.")


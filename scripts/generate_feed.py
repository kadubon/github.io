#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
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

text = works_path.read_text(encoding="utf-8", errors="ignore")

# ====== 行単位 ======
lines = [ln.strip() for ln in text.splitlines()]

# 見出し行: "12. ### Title ..."（先頭に番号. ###）
title_re     = re.compile(r"^\d+\.\s*###\s+(?P<title>.+)$")
# 種別キーワード
type_words   = ("Preprint", "Working paper", "Other", "Book review", "Report")
# Published: YYYY-MM-DD
published_re = re.compile(r"Published:\s*(\d{4}-\d{2}-\d{2})")
# DOI本体（大文字混在も許容）
doi_core_re  = re.compile(r"(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", re.IGNORECASE)
# aタグのhrefだけに DOI があるケースの保険
href_doi_re  = re.compile(r'href=["\']https?://(?:dx\.)?doi\.org/(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)["\']', re.IGNORECASE)

def find_nearby_info(start_idx: int, max_lookahead: int = 10):
    kind = None
    pub  = None
    doi  = None
    for j in range(start_idx + 1, min(len(lines), start_idx + 1 + max_lookahead)):
        line = lines[j]
        # 種別
        for kw in type_words:
            if kw.lower() in line.lower():
                kind = kw
                break
        # 日付
        mdate = published_re.search(line)
        if mdate and not pub:
            pub = mdate.group(1)
        # DOI（テキスト中 or aタグのhref）
        if not doi:
            mdoi = doi_core_re.search(line)
            if mdoi:
                doi = mdoi.group(1)
            else:
                mhref = href_doi_re.search(line)
                if mhref:
                    doi = mhref.group(1)
    return kind, pub, doi

def xml_esc(s: str) -> str:
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

items = []
for i, ln in enumerate(lines):
    m = title_re.match(ln)
    if not m:
        continue
    title = m.group("title").strip()
    kind, pub, doi = find_nearby_info(i)
    if not doi:
        # さらに少し広く（次の見出しまで）保険探索
        k = i + 1
        while k < len(lines) and not title_re.match(lines[k]):
            line = lines[k]
            mh = href_doi_re.search(line) or doi_core_re.search(line)
            if mh:
                doi = mh.group(1)
                break
            k += 1
    if not doi:
        continue

    link = f"https://doi.org/{doi}"
    pubDate = None
    if pub:
        try:
            d = datetime.strptime(pub, "%Y-%m-%d")
            d = datetime.combine(d.date(), time(0, 0, 0), tzinfo=JST)
            pubDate = eut.format_datetime(d)
        except Exception:
            pubDate = None

    items.append({
        "title": title,
        "link": link,
        "guid": link,
        "doi": doi,
        "kind": kind or "Work",
        "pubDate": pubDate
    })

# 重複 DOI 除去（先勝ち）
seen = set(); dedup = []
for it in items:
    key = it["doi"].lower()
    if key in seen: continue
    seen.add(key); dedup.append(it)
items = dedup

# RSS 2.0
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


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

# ====== 行単位に分割 ======
lines = [ln.strip() for ln in text.splitlines()]

# ====== 抽出用の厳密パターン ======
title_re     = re.compile(r"^\d+\.\s*###\s+(?P<title>.+)$")
type_words   = ("Preprint", "Working paper", "Other", "Book review", "Report")
published_re = re.compile(r"Published:\s*(\d{4}-\d{2}-\d{2})")
doi_re       = re.compile(r"(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", re.IGNORECASE)

def find_nearby_info(start_idx: int, max_lookahead: int = 6):
    """タイトル行の直後数行から 種別, 公開日, DOI を抽出"""
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
        # Published
        mdate = published_re.search(line)
        if mdate:
            pub = mdate.group(1)
        # DOI
        mdoi = doi_re.search(line)
        if mdoi and doi is None:
            doi = mdoi.group(1)
        if doi and (kind or "Published" in line):
            # 必須のDOIが取れ、かつ種別 or Published 情報に到達したら打ち切り
            pass
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
        continue  # DOI がない行はスキップ（必須）
    # フィード項目
    link = f"https://doi.org/{doi}"
    # pubDate（任意）
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
        "kind": kind,
        "pubDate": pubDate
    })

# ====== 重複 DOI を除去（先勝ち） ======
seen = set()
dedup = []
for it in items:
    if it["doi"].lower() in seen:
        continue
    seen.add(it["doi"].lower())
    dedup.append(it)
items = dedup

# ====== RSS 2.0 を構築 ======
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
    # description は種別と DOI を短く
    desc = f'{it["kind"] or "Work"} — DOI: {it["doi"]}'
    rss.append('    <description><![CDATA[')
    rss.append(f'      ' + desc)
    rss.append('    ]]></description>')
    rss.append('  </item>')

rss.append('</channel>')
rss.append('</rss>')

feed_path.write_text("\n".join(rss) + "\n", encoding="utf-8")
print(f"Wrote {feed_path} with {len(items)} items.")

#!/usr/bin/env python3
"""Generate stable, machine-readable research and OSS discovery catalogs.

The research catalog is derived from the JSON-LD already embedded in
``works.html``. The OSS catalog is derived from the public GitHub REST API.
No source publication or software repository content is modified.
"""

from __future__ import annotations

from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import re
from typing import Any, Iterable
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen


SITE_URL = "https://kadubon.github.io/github.io/"
GITHUB_OWNER = "kadubon"
GITHUB_PROFILE = f"https://github.com/{GITHUB_OWNER}"
ORCID = "https://orcid.org/0009-0004-4273-3365"
ROOT = Path(__file__).resolve().parents[1]
WORKS_PATH = ROOT / "works.html"

JSONLD_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)


def write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def iso_date(value: str | None) -> str:
    if not value:
        return ""
    return value[:10]


def max_timestamp(values: Iterable[str]) -> str:
    candidates = sorted(value for value in values if value)
    return candidates[-1] if candidates else ""


def repository_source_state(records: Iterable[dict[str, Any]]) -> str:
    timestamps: list[str] = []
    for record in records:
        timestamps.extend([record.get("updated_at", ""), record.get("pushed_at", "")])
    return max_timestamp(timestamps)


def normalize_keywords(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    return []


def resolve_author(author: Any, people: dict[str, str]) -> str:
    if isinstance(author, str):
        return author
    if not isinstance(author, dict):
        return ""
    if author.get("name"):
        return str(author["name"])
    if author.get("@id"):
        return people.get(str(author["@id"]), str(author["@id"]))
    return ""


def extract_doi(identifier: Any) -> str:
    identifiers = identifier if isinstance(identifier, list) else [identifier]
    for item in identifiers:
        if not isinstance(item, dict):
            continue
        if str(item.get("propertyID", "")).upper() == "DOI" and item.get("value"):
            return str(item["value"]).lower()
    return ""


def stable_slug(local_record_url: str, date_published: str, title: str, doi: str) -> str:
    """Use the established Works anchor as the stable paper-page slug."""
    fragment = urlparse(local_record_url).fragment
    if re.fullmatch(r"[a-z0-9-]+", fragment):
        return fragment
    normalized = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f"{iso_date(date_published)}-{normalized}-{doi.rsplit('.', 1)[-1]}".strip("-")


def load_research_catalog() -> tuple[list[dict[str, Any]], str]:
    source = WORKS_PATH.read_text(encoding="utf-8")
    graphs: list[dict[str, Any]] = []
    for raw in JSONLD_RE.findall(source):
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            graphs.append(parsed)

    nodes: list[dict[str, Any]] = []
    for graph in graphs:
        if isinstance(graph.get("@graph"), list):
            nodes.extend(node for node in graph["@graph"] if isinstance(node, dict))
        else:
            nodes.append(graph)

    people = {
        str(node["@id"]): str(node.get("name", node["@id"]))
        for node in nodes
        if node.get("@type") == "Person" and node.get("@id")
    }
    works_page = next(
        (
            node
            for node in nodes
            if node.get("@type") == "CollectionPage"
            and str(node.get("@id", "")).startswith(f"{SITE_URL}works.html")
        ),
        {},
    )

    records: list[dict[str, Any]] = []
    for node in nodes:
        schema_type = node.get("@type")
        if schema_type not in {"ScholarlyArticle", "SoftwareSourceCode"}:
            continue

        authors_value = node.get("author", [])
        authors_raw = authors_value if isinstance(authors_value, list) else [authors_value]
        authors = [
            name
            for name in (resolve_author(author, people) for author in authors_raw)
            if name
        ]
        doi = extract_doi(node.get("identifier"))
        date_published = str(node.get("datePublished", ""))
        local_record_url = str(node.get("mainEntityOfPage", ""))
        title = str(node.get("headline") or node.get("name") or "")
        record = {
                "record_type": (
                    "research_software"
                    if schema_type == "SoftwareSourceCode"
                    else "scholarly_article"
                ),
                "schema_org_type": schema_type,
                "id": node.get("@id", ""),
                "title": title,
                "authors": authors,
                "date_published": date_published,
                "doi": doi,
                "doi_url": f"https://doi.org/{doi}" if doi else "",
                "canonical_url": node.get("url") or node.get("mainEntityOfPage") or "",
                "local_record_url": local_record_url,
                "abstract": node.get("description", ""),
                "keywords": normalize_keywords(node.get("keywords")),
                "language": node.get("inLanguage", ""),
                "genre": node.get("genre", ""),
                "same_as": node.get("sameAs", []),
        }
        if record["record_type"] == "scholarly_article":
            record["slug"] = stable_slug(local_record_url, date_published, title, doi)
            record["landing_page_url"] = f"{SITE_URL}papers/{record['slug']}/"
        records.append(record)

    records.sort(
        key=lambda item: (item["date_published"], item["title"]),
        reverse=True,
    )
    if not records:
        raise RuntimeError(f"No research records found in {WORKS_PATH}")

    source_state = str(works_page.get("dateModified", "")) or iso_date(
        records[0]["date_published"]
    )
    return records, source_state


def github_request(url: str) -> tuple[Any, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "kadubon-research-hub-catalog-generator",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response), response.headers.get("Link", "")


def next_link(link_header: str) -> str:
    for part in link_header.split(","):
        match = re.match(r'\s*<([^>]+)>;\s*rel="([^"]+)"', part)
        if match and match.group(2) == "next":
            return match.group(1)
    return ""


def load_oss_catalog() -> list[dict[str, Any]]:
    query = urlencode(
        {
            "type": "owner",
            "sort": "updated",
            "direction": "desc",
            "per_page": 100,
        }
    )
    url = f"https://api.github.com/users/{GITHUB_OWNER}/repos?{query}"
    repositories: list[dict[str, Any]] = []
    while url:
        payload, link_header = github_request(url)
        if not isinstance(payload, list):
            raise RuntimeError("GitHub repository response was not a list")
        repositories.extend(item for item in payload if isinstance(item, dict))
        url = next_link(link_header)

    records: list[dict[str, Any]] = []
    for repo in repositories:
        owner = repo.get("owner") if isinstance(repo.get("owner"), dict) else {}
        if (
            owner.get("login", "").lower() != GITHUB_OWNER.lower()
            or repo.get("private")
            or repo.get("fork")
        ):
            continue
        license_data = (
            repo.get("license") if isinstance(repo.get("license"), dict) else {}
        )
        topics = sorted(str(topic) for topic in (repo.get("topics") or []))
        records.append(
            {
                "schema_org_type": "SoftwareSourceCode",
                "name": repo.get("name", ""),
                "full_name": repo.get("full_name", ""),
                "description": repo.get("description") or "",
                "repository_url": repo.get("html_url", ""),
                "clone_url": repo.get("clone_url", ""),
                "homepage": repo.get("homepage") or "",
                "programming_language": repo.get("language") or "",
                "topics": topics,
                "license_spdx": license_data.get("spdx_id") or "",
                "default_branch": repo.get("default_branch", ""),
                "created_at": repo.get("created_at", ""),
                "updated_at": repo.get("updated_at", ""),
                "pushed_at": repo.get("pushed_at", ""),
                "archived": bool(repo.get("archived")),
                "stars": int(repo.get("stargazers_count") or 0),
                "forks": int(repo.get("forks_count") or 0),
                "open_issues": int(repo.get("open_issues_count") or 0),
            }
        )

    records.sort(
        key=lambda item: (
            item["archived"],
            item["pushed_at"],
            item["updated_at"],
            item["name"].lower(),
        ),
        reverse=True,
    )
    # Active repositories first, with the newest source activity first.
    records.sort(key=lambda item: item["archived"])
    if not records:
        raise RuntimeError(f"No public source repositories found for {GITHUB_OWNER}")
    return records


def research_catalog(records: list[dict[str, Any]], source_state: str) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "catalog_type": "research_works",
        "canonical_url": f"{SITE_URL}research-catalog.json",
        "source_url": f"{SITE_URL}works.html",
        "source_state_date": source_state,
        "creator": {
            "name": "K. Takahashi",
            "orcid": ORCID,
            "website": SITE_URL,
            "github": GITHUB_PROFILE,
        },
        "selection_policy": (
            "All ScholarlyArticle and SoftwareSourceCode records in the canonical "
            "works.html JSON-LD graph."
        ),
        "record_count": len(records),
        "records": records,
    }


def oss_catalog(records: list[dict[str, Any]]) -> dict[str, Any]:
    source_state = repository_source_state(records)
    return {
        "schema_version": "1.0",
        "catalog_type": "open_source_repositories",
        "canonical_url": f"{SITE_URL}oss-catalog.json",
        "human_url": f"{SITE_URL}oss.html",
        "source_url": GITHUB_PROFILE,
        "source_state_at": source_state,
        "owner": {
            "name": "K. Takahashi",
            "github_login": GITHUB_OWNER,
            "github_url": GITHUB_PROFILE,
            "orcid": ORCID,
        },
        "selection_policy": {
            "included": (
                "Public, non-fork repositories owned by the GitHub account kadubon."
            ),
            "archived_records": "Included and explicitly marked.",
            "interpretation": (
                "Catalog inclusion is a discovery aid, not a claim of production "
                "readiness, maintenance status, security, or scientific validation."
            ),
        },
        "record_count": len(records),
        "archived_count": sum(1 for record in records if record["archived"]),
        "repositories": records,
    }


def agent_index(
    research_records: list[dict[str, Any]],
    research_state: str,
    oss_records: list[dict[str, Any]],
) -> dict[str, Any]:
    oss_state = repository_source_state(oss_records)
    source_state = max_timestamp(
        [
            f"{research_state}T00:00:00Z" if len(research_state) == 10 else research_state,
            oss_state,
        ]
    )
    return {
        "schema_version": "1.0",
        "index_type": "research_and_software_discovery",
        "canonical_url": f"{SITE_URL}agent-index.json",
        "source_state_at": source_state,
        "identity": {
            "name": "K. Takahashi",
            "orcid": ORCID,
            "website": SITE_URL,
            "github": GITHUB_PROFILE,
        },
        "scope": [
            "auditable autonomous intelligence",
            "observable-only and no-meta AI governance",
            "deterministic replay and fail-closed verification",
            "long-running agents and memory governance",
            "Constraint Generative Theory",
            "research automation and AI scientist protocols",
            "provenance, claim certification, and scientific availability",
        ],
        "entry_points": {
            "human_overview": SITE_URL,
            "research_map": f"{SITE_URL}research-map.html",
            "publication_index": f"{SITE_URL}works.html",
            "research_catalog_json": f"{SITE_URL}research-catalog.json",
            "paper_landing_index": f"{SITE_URL}papers/",
            "paper_landing_catalog_json": f"{SITE_URL}papers/index.json",
            "software_catalog_human": f"{SITE_URL}oss.html",
            "software_catalog_json": f"{SITE_URL}oss-catalog.json",
            "llm_short_context": f"{SITE_URL}llms.txt",
            "llm_extended_context": f"{SITE_URL}llms-full.txt",
            "update_feed": f"{SITE_URL}feed.xml",
            "citation_metadata": f"{SITE_URL}CITATION.cff",
            "sitemap": f"{SITE_URL}sitemap.xml",
            "paper_source_archive": f"{GITHUB_PROFILE}/paper-tex-backup",
        },
        "counts": {
            "research_records": len(research_records),
            "scholarly_paper_count": sum(1 for record in research_records if record["record_type"] == "scholarly_article"),
            "public_source_repositories": len(oss_records),
            "archived_source_repositories": sum(
                1 for record in oss_records if record["archived"]
            ),
        },
        "authority_order": {
            "identity": ["ORCID", "canonical website", "GitHub profile"],
            "research": [
                "DOI landing record",
                "canonical works index",
                "paper source archive",
                "secondary summaries",
            ],
            "software": [
                "repository README and release metadata",
                "repository source and tests",
                "OSS catalog snapshot",
                "secondary summaries",
            ],
        },
        "agent_selection_guidance": [
            (
                "Match a task against titles, abstracts, repository descriptions, and "
                "topics before retrieving full artifacts."
            ),
            (
                "For research claims, follow the DOI and distinguish the paper's claims "
                "from this catalog's discovery metadata."
            ),
            (
                "For software use, inspect the repository README, license, tests, "
                "dependencies, releases, and pushed_at value before execution or reuse."
            ),
            (
                "Do not infer production readiness, security, scientific validity, or "
                "endorsement from catalog inclusion, stars, or recency."
            ),
            (
                "Treat archived=true, absent license_spdx, and absent descriptions as "
                "signals requiring additional review, not automatic rejection."
            ),
        ],
        "refresh": {
            "method": (
                "Generated from works.html JSON-LD and the public GitHub repositories API."
            ),
            "policy": "Regenerate after publication changes and on a weekly schedule.",
        },
    }


def render_oss_html(records: list[dict[str, Any]]) -> str:
    source_state = repository_source_state(records)
    active_count = sum(1 for record in records if not record["archived"])
    item_list = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "@id": f"{SITE_URL}oss.html#page",
        "url": f"{SITE_URL}oss.html",
        "name": "Open Source Software Catalog | K. Takahashi",
        "description": (
            "Human-readable catalog of public source repositories owned by kadubon, "
            "with corresponding machine-readable metadata."
        ),
        "about": {"@id": f"{SITE_URL}#person"},
        "mainEntity": {
            "@type": "ItemList",
            "numberOfItems": len(records),
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": position,
                    "url": record["repository_url"],
                }
                for position, record in enumerate(records, 1)
            ],
        },
    }

    cards: list[str] = []
    for record in records:
        topics = "".join(
            f"<li>{escape(topic)}</li>" for topic in record["topics"]
        )
        topics_block = (
            f'<ul class="topic-list" aria-label="Topics">{topics}</ul>'
            if topics
            else '<p class="quiet">No GitHub topics declared.</p>'
        )
        description = record["description"] or (
            "No GitHub repository description is currently declared."
        )
        status = "Archived" if record["archived"] else "Active repository"
        homepage = (
            f'<a href="{escape(record["homepage"], quote=True)}">Project or related record</a>'
            if record["homepage"]
            else "Not declared"
        )
        cards.append(
            f"""      <article class="repo-card">
        <h2><a href="{escape(record["repository_url"], quote=True)}">{escape(record["name"])}</a></h2>
        <p>{escape(description)}</p>
        <dl class="repo-meta">
          <div><dt>Status</dt><dd>{status}</dd></div>
          <div><dt>Language</dt><dd>{escape(record["programming_language"] or "Not detected")}</dd></div>
          <div><dt>License</dt><dd>{escape(record["license_spdx"] or "Not declared in GitHub metadata")}</dd></div>
          <div><dt>Last source push</dt><dd><time datetime="{escape(record["pushed_at"], quote=True)}">{escape(iso_date(record["pushed_at"]) or "Unknown")}</time></dd></div>
          <div><dt>Default branch</dt><dd>{escape(record["default_branch"] or "Unknown")}</dd></div>
          <div><dt>Related URL</dt><dd>{homepage}</dd></div>
        </dl>
        {topics_block}
      </article>"""
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Open Source Software Catalog | K. Takahashi</title>
  <meta name="description" content="Discover public OSS and research reference implementations by K. Takahashi using descriptions, topics, licenses, and source-activity metadata.">
  <meta name="author" content="K. Takahashi">
  <meta name="robots" content="index,follow,max-snippet:-1">
  <link rel="canonical" href="{SITE_URL}oss.html">
  <link rel="alternate" type="application/json" title="Machine-readable OSS catalog" href="{SITE_URL}oss-catalog.json">
  <link rel="alternate" type="application/json" title="Research and OSS agent index" href="{SITE_URL}agent-index.json">
  <link rel="stylesheet" href="style.css">
  <style>
    .catalog-summary {{ display: flex; flex-wrap: wrap; gap: 0.5rem 1.25rem; padding-left: 0; list-style: none; }}
    .repo-grid {{ display: grid; gap: 1rem; }}
    .repo-card {{ border: 1px solid #ddd; border-radius: 6px; background: #fafafa; padding: 1rem; }}
    .repo-card h2 {{ margin-top: 0; overflow-wrap: anywhere; }}
    .repo-meta {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr)); gap: 0.35rem 1rem; }}
    .repo-meta div {{ min-width: 0; }}
    .repo-meta dt {{ font-weight: 700; }}
    .repo-meta dd {{ margin: 0; overflow-wrap: anywhere; }}
    .topic-list {{ display: flex; flex-wrap: wrap; gap: 0.35rem; padding-left: 0; list-style: none; }}
    .topic-list li {{ border: 1px solid #ccd8e5; border-radius: 999px; background: #eef5fb; padding: 0.15rem 0.55rem; font-size: 0.86rem; }}
    .quiet {{ color: #555; }}
  </style>
  <script type="application/ld+json">{json.dumps(item_list, ensure_ascii=False, separators=(",", ":"))}</script>
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to content</a>
  <header class="container">
    <h1>Open Source Software Catalog</h1>
    <p>Public source repositories owned by K. Takahashi (<a href="{GITHUB_PROFILE}">@{GITHUB_OWNER}</a>), exposed as a human-readable page and a stable machine-readable catalog.</p>
    <nav aria-label="Primary">
      <ul>
        <li><a href="{SITE_URL}">Home</a></li>
        <li><a href="{SITE_URL}research-map.html">Research Map</a></li>
        <li><a href="{SITE_URL}works.html">Works</a></li>
        <li><a href="{SITE_URL}agent-index.json">Agent Index</a></li>
      </ul>
    </nav>
  </header>
  <main id="main-content">
    <section class="container">
      <h2>Catalog scope</h2>
      <ul class="catalog-summary">
        <li><strong>{len(records)}</strong> public non-fork repositories</li>
        <li><strong>{active_count}</strong> not archived</li>
        <li>GitHub source state: <time datetime="{escape(source_state, quote=True)}">{escape(iso_date(source_state))}</time></li>
      </ul>
      <p>Use <a href="{SITE_URL}oss-catalog.json">oss-catalog.json</a> for structured retrieval and <a href="{SITE_URL}agent-index.json">agent-index.json</a> for authority and selection guidance. Inclusion supports discovery only; inspect each repository's README, license, tests, dependencies, releases, and source activity before reuse.</p>
    </section>
    <section class="container" aria-labelledby="repositories-heading">
      <h2 id="repositories-heading">Repositories</h2>
      <div class="repo-grid">
{chr(10).join(cards)}
      </div>
    </section>
  </main>
  <footer class="container">
    <p>&copy; 2026 K. Takahashi</p>
  </footer>
</body>
</html>
"""


def main() -> None:
    research_records, research_state = load_research_catalog()
    oss_records = load_oss_catalog()

    write_json(
        ROOT / "research-catalog.json",
        research_catalog(research_records, research_state),
    )
    write_json(ROOT / "oss-catalog.json", oss_catalog(oss_records))
    write_json(
        ROOT / "agent-index.json",
        agent_index(research_records, research_state, oss_records),
    )
    (ROOT / "oss.html").write_text(
        render_oss_html(oss_records),
        encoding="utf-8",
    )

    print(
        "Wrote agent-index.json, research-catalog.json, oss-catalog.json, "
        f"and oss.html ({len(research_records)} research records; "
        f"{len(oss_records)} public source repositories)."
    )


if __name__ == "__main__":
    main()

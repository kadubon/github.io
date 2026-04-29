#!/usr/bin/env python3
"""Submit sitemap-scoped URLs to IndexNow."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE_URL = "https://kadubon.github.io/github.io/"
DEFAULT_ENDPOINT = "https://api.indexnow.org/indexnow"
DEFAULT_KEY = "301c5859d4134ce8a80373c7991ed72f"
DEFAULT_KEY_FILE = ROOT / f"{DEFAULT_KEY}.txt"


def normalize_repo_path(path: str) -> str:
    path = path.strip().replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def read_key(key_file: Path) -> str:
    key = key_file.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", key):
        raise ValueError(f"Invalid IndexNow key in {key_file}")
    return key


def parse_sitemap(sitemap: Path) -> list[str]:
    root = ET.parse(sitemap).getroot()
    urls: list[str] = []
    for node in root.iter():
        if node.tag.endswith("loc") and node.text:
            url = node.text.strip()
            if url:
                urls.append(url)
    if not urls:
        raise ValueError(f"No URLs found in {sitemap}")
    return urls


def url_to_repo_path(url: str, base_url: str) -> str | None:
    if url == base_url:
        return "index.html"
    if not url.startswith(base_url):
        return None
    relative = url[len(base_url) :]
    if not relative:
        return "index.html"
    if relative.endswith("/"):
        return f"{relative}index.html"
    return normalize_repo_path(relative)


def validate_sitemap_urls(urls: list[str], base_url: str) -> dict[str, str]:
    base = urlparse(base_url)
    if not base.scheme or not base.netloc:
        raise ValueError(f"Invalid base URL: {base_url}")

    mapping: dict[str, str] = {}
    for url in urls:
        parsed = urlparse(url)
        if parsed.netloc != base.netloc:
            raise ValueError(f"Sitemap URL host does not match base host: {url}")
        repo_path = url_to_repo_path(url, base_url)
        if repo_path is None:
            raise ValueError(f"Sitemap URL is outside base URL path: {url}")
        mapping[url] = repo_path
    return mapping


def load_changed_files(path: Path) -> set[str]:
    changed: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        item = normalize_repo_path(line)
        if item:
            changed.add(item)
    return changed


def select_urls(
    url_to_path: dict[str, str],
    changed_files: set[str] | None,
    key_file_name: str,
) -> list[str]:
    if changed_files is None:
        return list(url_to_path.keys())
    if "sitemap.xml" in changed_files or key_file_name in changed_files:
        return list(url_to_path.keys())
    return [url for url, repo_path in url_to_path.items() if repo_path in changed_files]


def wait_for_key_file(
    key_location: str,
    expected_key: str,
    attempts: int,
    wait_seconds: float,
) -> None:
    for attempt in range(1, attempts + 1):
        try:
            request = Request(key_location, headers={"User-Agent": "IndexNow submitter"})
            with urlopen(request, timeout=20) as response:
                body = response.read().decode("utf-8", errors="replace").strip()
                if response.status == 200 and body == expected_key:
                    print(f"Verified key file at {key_location}")
                    return
                print(
                    f"Key file check {attempt}/{attempts} returned "
                    f"HTTP {response.status} with unexpected body."
                )
        except (HTTPError, URLError, TimeoutError) as exc:
            print(f"Key file check {attempt}/{attempts} failed: {exc}")
        if attempt < attempts:
            time.sleep(wait_seconds)
    raise RuntimeError(f"Could not verify IndexNow key file at {key_location}")


def submit_indexnow(endpoint: str, payload: dict[str, object]) -> tuple[int, str]:
    body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    request = Request(
        endpoint,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "IndexNow submitter",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return response.status, response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        return exc.code, detail


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sitemap", default=str(ROOT / "sitemap.xml"))
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--key-file", default=str(DEFAULT_KEY_FILE))
    parser.add_argument("--key-location")
    parser.add_argument("--changed-file-list")
    parser.add_argument("--all", action="store_true", help="Submit every URL in sitemap.xml.")
    parser.add_argument("--dry-run", action="store_true", help="Print payload without submitting.")
    parser.add_argument("--wait-key", action="store_true", help="Verify the hosted key file first.")
    parser.add_argument("--wait-attempts", type=int, default=18)
    parser.add_argument("--wait-seconds", type=float, default=10)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    sitemap = Path(args.sitemap)
    key_file = Path(args.key_file)
    key = read_key(key_file)
    base_url = args.base_url if args.base_url.endswith("/") else f"{args.base_url}/"
    key_location = args.key_location or urljoin(base_url, key_file.name)

    urls = parse_sitemap(sitemap)
    url_to_path = validate_sitemap_urls(urls, base_url)

    changed_files = None
    if args.changed_file_list and not args.all:
        changed_files = load_changed_files(Path(args.changed_file_list))

    selected_urls = select_urls(url_to_path, changed_files, key_file.name)
    if not selected_urls:
        print("No sitemap-listed URL changed; nothing to submit.")
        return 0

    payload = {
        "host": urlparse(base_url).netloc,
        "key": key,
        "keyLocation": key_location,
        "urlList": selected_urls,
    }

    print(json.dumps(payload, indent=2))
    if args.dry_run:
        print("Dry run complete; no request sent.")
        return 0

    if args.wait_key:
        wait_for_key_file(key_location, key, args.wait_attempts, args.wait_seconds)

    status, response_body = submit_indexnow(args.endpoint, payload)
    if response_body:
        print(response_body)
    print(f"IndexNow response: HTTP {status}")
    return 0 if status in (200, 202) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

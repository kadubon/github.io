# Collective Intelligence Index maintenance

The index is a static, bilingual editorial map of this site's research and OSS.
It operates offline and does not execute or install any indexed software.
The initial review is dated 2026-09-21; regeneration never advances review dates.

## Source authority and reviewed scope

`works.html` JSON-LD remains the publication authority, including SoftwareSourceCode
records. `scripts/generate_agent_catalogs.py` derives `research-catalog.json`,
`oss-catalog.json`, `oss.html` and `agent-index.json`. Do not maintain a second
title/author/DOI list. The bibliography is generated from selected scholarly
records only. OASG, CCR, PIC and CPCF software DOI records remain software.

The initial screening covers 233 research records and 54 public repository
metadata records. Selection contains 19 papers (8 core, 11 supporting) and 12
repositories (6 core, 6 supporting). The JSON registry's `corpus_audit` records
every screened identity, depth, decision and reason. Keyword matches outside
the selected full-text review remain unresolved rather than rejected on age.
This is not a comprehensive survey of world research, or a full-text review of
all 233 records. Adjacent public repositories were considered through their
catalogue descriptions/topics and release observations; only the selected 12
received the stated README/contract/interface/license review.

Included paper titles and DOI kinds were checked against DataCite registration
metadata, and scope was inspected in the public `paper-tex-backup` archive.
The registry stores immutable archive paths, hashes, locators and observation
dates, not copies of manuscripts. Hashes bind source bytes, not mathematical
truth. CGT's concept/series DOI has multiple versions and different catalogue
and current registration dates; its exact TeX/version binding remains explicit
as unresolved. Distinct CGT supplements must not be invented as separate DOI
records or collapsed into a single claimed implementation. No exact Boundary
Exchange title/DOI was resolved in the scanned catalogue.

The original website license remains CC BY 4.0. The 12 inspected OSS licenses
are Apache-2.0. The Audit-Closed repository separately licenses its bundled
protocol paper CC BY 4.0. Repository metadata for other projects is not
overwritten with a blanket license assertion.

## Rebuild and validate

```text
python -m pip install -r requirements-index.txt
python scripts/generate_agent_catalogs.py --offline
python scripts/generate_paper_pages.py
python scripts/generate_collective_intelligence_index.py
python scripts/generate_collective_intelligence_index.py --check
python scripts/validate_collective_intelligence_index.py
python scripts/validate_paper_pages.py
python -m unittest discover -s tests -v
```

The new generator and `--check` never use the network. Paper generation reuses
the checked-in PDF metadata cache. New paper records without cached metadata
may need the existing explicit PDF refresh workflow. `--check` compares bytes
without writing. JSON Schema Draft 2020-12 and semantic reference validation
are complementary. The registry digest covers the entire JSON value except
`content_digest`, serialized with sorted keys, compact separators, unescaped
Unicode and no NaN. The schema is separately served and versioned at
https://kadubon.github.io/github.io/schemas/collective-intelligence-index.schema.json.

All representations use one normalized model. Both HTML pages contain complete
cards, relationships, limits and links without JavaScript. Stable ASCII IDs
are independent of titles and versions. Do not reuse a retired ID.

## Editorial changes

1. Add or correct a paper in the existing `works.html` source, regenerate its
   catalogue and landing page, then add its existing source ID to
   `data/collective-intelligence-curation.json`. Verify exact DOI identity,
   type, title, author and dates; distinguish concept and version DOIs.
2. Read the actual scope/limitations in the paper. Record a bounded evidence
   entry with URL, immutable revision, locator, hash and observation date in
   `data/collective-intelligence-evidence.json`. Add bilingual question,
   contribution, relevance and limitations. Mark any unavailable source or
   ambiguous version explicitly; do not infer peer review from a DOI.
3. Classify software by its actual repository catalogue ID. Read README,
   license, public interface, schemas, examples, tests and release documents.
   Record source revision/version separately from release observation. An
   unknown package location is not an invitation to invent a pip command.
4. Add a problem ID with symptoms, first reads, inputs, outputs, unsupported
   conditions and stop/handoff conditions. Roles are local editorial
   classifications, not an upstream standard or privileged agent instruction.
5. Record relationships with direction, exact version pair, checked fields,
   evidence origin and unsupported obligations. `imports_artifact_from` goes
   consumer → producer; `exports_proposal_to` goes producer → host.
   `based_on` is a citation, not complete implementation.
6. `tested_upstream` requires a cited native check report and scope. It is not
   a test performed by this website task. `proposed_integration_with` must
   remain `proposed`. Source inspection cannot become native test execution.
   Compatibility never propagates transitively or to a new version pair.
7. Advance review dates only after an actual review. Regenerate, run tests,
   inspect both rendered pages, review the diff and use a normal pull request.

## Factual refresh versus scientific review

```text
python scripts/generate_agent_catalogs.py
python scripts/refresh_oss_release_snapshots.py
python scripts/generate_agent_catalogs.py --offline
python scripts/generate_collective_intelligence_index.py
```

The explicit refresh uses bounded `gh api` requests (four workers, three
attempts, timeout and backoff). It stores latest published GitHub release
metadata and current default-branch commits for all catalogue repositories.
A 404 on the latest-release endpoint means no published GitHub release was
observed, not no installable source. Temporary failures preserve the previous
record and mark it stale. GitHub release status does not verify PyPI, npm,
installed bytes, CI, or production readiness. Reviewed source versions remain
fixed in the evidence layer; new source revisions get a not-editorially-reviewed
status and do not renew relationships. Periodic factual refresh does not
auto-select new papers or perform scientific editorial review.

`works.html` software entries display latest observed release versions while
retaining original publication dates and historical archive DOI links. Updating
those entries is an editorial change: do not relabel an old immutable archive
DOI as the new release. The catalogue generator preserves software version,
license and source-repository metadata from that source.

## Publication, concurrency and crawler scope

The existing main-branch GitHub Pages publication is retained. `.nojekyll`
makes this already static site serve Markdown as files, avoiding automatic
Markdown conversion. There are no Jekyll layouts, includes or configuration
in the inspected baseline. The explicit existing HTML pages remain the reader
destinations. No new hosting service, release, version bump or endpoint exists.

Both trusted derived-content writers share `derived-content-writers` and
check out the current `main` when starting, rather than a queued event's old
commit, so a preceding writer's generated updates are retained. They
rebuild after rebasing before pushing; read-only pull-request CI has only
contents-read permission and does not use `pull_request_target`. Existing
paper generation preserves non-paper sitemap metadata. The feed still
represents publications, not an index page presented as a new paper. The
existing IndexNow workflow sees changed HTML/sitemap URLs; submission is not
evidence of indexing.

After normal-policy merge, check the exact Pages build/deployment commit and
unauthenticated public status, MIME type, UTF-8 bytes and content digest for
HTML, JSON, schema, Markdown and bibliography. Check homepage, OSS page,
agent-index and sitemap discovery. The public verification report is retained
as an execution artifact, not fabricated in advance by this document.

Origin-wide robots policy belongs at https://kadubon.github.io/robots.txt.
The file at https://kadubon.github.io/github.io/robots.txt is project content;
it cannot set origin-wide crawler rules. The account-root repository is out
of scope. Search indexing, retrieval, training and actual adoption are separate
outcomes. Optional llms files do not grant access policy or guarantee use.

Engineering references: [Schema.org SoftwareSourceCode](https://schema.org/SoftwareSourceCode),
[Google AI feature guidance](https://developers.google.com/search/docs/appearance/ai-features),
[robots location](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt),
and the optional [llms.txt proposal](https://llmstxt.org/).

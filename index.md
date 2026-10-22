# Index — Knowledge Base Catalog

Last updated: 2026-10-22 (Karpathy layout migration)

## Top-Level

| Path | Role |
|------|------|
| `AGENTS.md` | Operational rules for agents (pending — protected write) |
| `SCHEMA.md` | Formatting conventions, schemas, taxonomy |
| `log.md` | Append-only ledger of agent operations |
| `golden_tier_list.md` | Track A curation output |
| `emerging_edge_list.md` | Track B curation output |
| `mirage_short_list.md` | Track C curation output |
| `watchlist_changelog.md` | Dated Deep-Dive curation blocks |
| `research_interest.md` | Human-curated interest overrides |

## raw/ — Immutable source ingestion (READ-ONLY)

- `raw/articles/` — ingested article text (2 files)
- `raw/transcripts/` — transcripts (empty)
- `raw/metrics/` — metric snapshots (empty)

## wiki/ — Mutable agent knowledge base

- `wiki/companies/` — atomic company/ticker dossiers (869 entries)
- `wiki/sectors/` — sector & value-chain breakdowns (empty — to be backfilled)
- `wiki/concepts/` — paradigms, moats, tech gaps (7 entries: CASCADE, counter_uas, sic_gan_power, smr_datacenter, INDEX, SCHEMA, endpoint-mapping)
- `wiki/comparisons/` — head-to-head competitive analyses (empty — to be backfilled)
- `wiki/research/` — research workpapers
- `wiki/signal_briefs/` — signal brief artifacts
- `wiki/comparisons_corpus/` — 17 corpus files (SMR, TALO research)
- `wiki/archived/` — demoted/exit dossiers
- `wiki/archived_archive/` — pre-migration archive

## Ingest Pipeline

1. Source material → `raw/` (URL, title, date, source)
2. Company dossier updated → `wiki/companies/<T>/`
3. Sector/concept pages from sources → `wiki/sectors/` or `wiki/concepts/`
4. Competitive head-to-head → `wiki/comparisons/`
5. Queries filed from answered questions → `wiki/research/`

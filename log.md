# Log — Action History

## 2026-06-22
- [INIT] Clean rebuild of knowledge base wiki at ~/wiki
- Stripped all operational/trading system content
- Defined 4-pillar domain taxonomy (SCHEMA.md)
- Created entity pages for 4 research pillars
- Created concept pages: framework, methodology, mapping, inflection detection
- Empty directories ready: entities/, concepts/, comparisons/, queries/, raw/articles/, _archive/
- Cross-linking via [[wikilinks]] active

---

## 2026-10-22 — Karpathy layout migration
- Backup: /tmp/wiki_pre_migration_20261022.tar.gz (941KB, pre-migration state)
- Merged 131 dual-form + legacy dossiers (tickers/, entities/tickers/legacy_20261013/ -> entities/tickers/)
- Removed 16 UPPERCAST_TICKER.md junk files (content preserved in backups + canonical merges)
- Structural move: entities/tickers -> wiki/companies (869 dossiers); entities/tech_gaps -> wiki/concepts; concepts -> wiki/concepts; comparisons -> wiki/comparisons; corpus -> wiki/comparisons_corpus; research/signal_briefs/archived/_archive -> wiki/*
- Created raw/transcripts/, raw/metrics/, wiki/sectors/
- Rewrote index.md to new tree
- Patched consumers: pipeline_engine.py (wiki/companies paths + drift sentinel), pipeline_health_gate.py (drift sentinel), Deep-Dive cron prompt (archived/ path)
- Pending: AGENTS.md (protected-file write gate)

---

## 2026-10-22 — Sector + comparison backfill (post-migration)
- 4 sector dossiers in wiki/sectors/ (semiconductors, advanced-energy-grid, ai-infrastructure-thermal, physical-ai-edge-automation) — 802 verified ticker links
- 6 comparisons in wiki/comparisons/ (ceg-vs-vst, oklo-vs-ge-v, rgti-vs-ionq, on-vs-mchp, drs-vs-avav, qcom-edge-ai) — sub-agent web research, financials cited with source+date, 'verify next run' markers where FMP data pending
- Repaired 20 broken relative links in sectors (truncated path artifacts)

## 2026-10-22 — AGENTS.md written
- Approved by user (Discord), protected-write gate satisfied
- Karpathy topology + hard rules + consumer list + sub-agent timeout protocol recorded

## 2026-10-22 — Audit pass (recursive research sweep)
- Dedup: 72 dossiers, -377 exact-duplicate dated note lines (ARE was 257->164 lines)
- Root cause fixed: pipeline_engine.append_wiki_note() brief_id guard was case-sensitive (stored lowercase, compared uppercase) -> same brief re-appended every run for legacy files without [bid] markers; now case-insensitive
- Archived 22 one-char junk dossiers (A.md..Z.md, no real tickers) -> wiki/archived_archive/onechar_junk_20261022/
- Removed orphan twins: root signal_briefs.json (15.5d stale copy; live one is ~/.hermes/cron/signal_briefs.json), companies/index.json.bak_pre_p5
- Rebuilt companies/index.json from disk (744 entries; was 796 with stale refs)
- Removed 57 empty dirs (archived/pruned_20261016/GEV/ etc., legacy_20261013/); kept raw/transcripts+metrics (intentional)
- Patched 11 skill files + get_wiki_path.py: dead ~/wiki/entities/tickers + ~/wiki/tickers paths -> wiki/wiki/companies
- Re-verify: 0 dup-content files, 0 note dups, 0 dual-form, index==disk, 0 broken cross-links, gate ALL_GOOD

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
- Re-verify: 0 dup-content files, 0 dual-form, 0 note dups, index==disk, 0 broken cross-links, gate ALL_GOOD

---

## 2026-10-25 — Phase 1: drift-event schema (technology-substitution graph)
- Backup: /tmp/wiki_pre_phase1_drifts_20261025.tar.gz (2.6MB, pre-drifts state)
- Created wiki/drifts/ (first-class drift-event objects; upgrades concepts/ gap files to a bipartite graph: Company node + Drift-Event node, typed edges)
- SCHEMA.md: event object, M×T×C composite scoring axis (Gap 3), substitution/short losers track + sub_downside (Gap 2), winner/loser/sequencing/competitive edges, idempotency + immutability (deterministic evidence_id8, case-insensitive dedup = brief-id lesson), normalized layer vocabulary mapped to all 4 sector dossiers
- Seeded 3 grounded events (the user's 3 examples, 1:1): DRIFT-001 FinFET→GAA 2nm (HIGH 432, scaling), DRIFT-002 GaN LED→power (CRITICAL 600, deployed, reference anchor w/ clean winner WOLF + loser SMART/CreeLED), DRIFT-003 300mm→450mm wafer (NOISE 20, stress test: big magnitude/low certainty must score low yet stay filed)
- INDEX.md: drift catalog + scores + Track D seed rows
- Pending Phase 2-4: Track D generator into tier_lists.py, autonomous drift-detector cron (value-chain scaffold → substitution scan → LLM win/lose judgment), cascade-on-event wiring into CASCADE.md
- Gate verify + stress-test agents follow

## 2026-10-25 — Phase 1 stress-test: 5-panel pillar validation + v1.1 fixes
- Dispatched 5 sub-agents (semi / ai-infra / advanced-energy / physical-AI / adversarial schema-critic). ALL 5 hit the 600s timeout (backend ~50s/web call; each had 2-5 API calls = reads + 1 salvageable search). Salvage protocol per AGENTS.md: extracted each transcript's research (real dated sources), wrote the 5 validation dossiers inline to wiki/research/drift-validation/.
- Panel verdicts: ALL 4 pillars PASS; schema-critic = YES-with-fixes.
- Landed v1.1 fixes in SCHEMA.md (8 edits): class enum +procurement-substitution; Sector → primary+Secondary (FM-1 BLOCKING); Drift Exposure backlink w/ mandatory net_drift_position (FM-2 BLOCKING); cap-band columns on Winner/Loser tables; Magnitude displacement sub-classes (cutoff/additive/content-per-unit/architecture-reset); timing-gate rule (regulated pillars); nuclear certainty min(TRL, licensing-progress).
- Backfilled 3 seeds: Secondary sectors + Horizon tag + Displacement sub-class (+ timing-gate on DRIFT-003).
- INDEX.md: v1.1 note + 4 sample drifts queued for Phase 2 filing (DRIFT-004 High-NA EUV 144, DRIFT-005 liquid-cooling default 336, DRIFT-006 SMR DC power 105 gate-watched, DRIFT-007 autonomous C-UAS 180).
- Deferred to Phase 2/3: gradual displacement curve, private-winner supplier-discovery cascade rule, horizon column in tier table.
- Lesson codified: research+write children WILL 600s-timeout on this backend — salvage transcripts, write inline in parent. Confirmed 5-for-5.

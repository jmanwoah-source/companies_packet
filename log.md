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

## 2026-10-25 — Phase 2: file DRIFT-004..007 + Track D generator + backlinks

- **4 new drifts filed** (from the 5-panel validation sample candidates, all salvage-cited): DRIFT-004 High-NA EUV (144 EMERGING, semis), DRIFT-005 liquid-cooling default (336 HIGH, ai-infra), DRIFT-006 SMR data-center power (105 EMERGING, advanced-energy, timing-gate: NRC SDA), DRIFT-007 autonomous C-UAS detect-and-kill (180 EMERGING upper, physical-ai, FM-4 private-winner rule noted for Anduril).
- **`~/.hermes/scripts/drift_track_d.py`** (deterministic, no LLM): parses all 7 drifts → writes `~/wiki/substitution_short_list.md` (Track D, root-level, generator-owned like tier_lists.py) + `## Drift Exposure` backlinks into 16 company dossiers (fenced block, idempotent: exactly 1 block per dossier after re-run — verified) + regenerates the INDEX.md catalog table.
- Track D logic: named loser rows only (class rows stay in drift files); sub_downside midpoint parsed from `est. lo-hi` / `<x` / bare; confidence = certainty weight (high ≥0.9 / medium ≥0.5 / low <0.5); low-confidence named losers stay on the short list, do NOT get dossier backlinks; winner/loser edges → net_drift_position line (FM-2).
- Current Track D: 1 named row — SMART (CreeLED) sub_downside 100.0, weight 1.0, high confidence, from DRIFT-002. SMART has no wiki dossier (not in tracked universe) → correctly skipped for backlink, stays on short list.
- Parser bugs found+fixed this phase (all at the tool layer, zero manual table edits after): composite regex (bold table form), status regex (`## Status` heading), cells[2] not cells[3] for company (off-by-one vs cap-band column), `(class)`/`(conditional)` rows filtered from edges.
- Seed score tables DRIFT-001/002/003 confirmed 3-col `Component|Score|Rationale` with `**Composite** | **N** | **TIER**` rows — the canonical format the parser reads.
- **Pending user approval (protected-write gate):** AGENTS.md topology + consumer list should gain `wiki/drifts/` and root `substitution_short_list.md` (generator-owned). Staged in log; do not route around the gate.
- Next: Phase 3 autonomous drift-detector cron (sector dossiers as query scaffold → substitution-language scan → LLM win/lose judgment → files candidate events for scoring).

## 2026-10-25 — Phase 3: autonomous drift detector (scan + judgment + cron)

- **`~/.hermes/scripts/drift_scan.py`** (deterministic, no LLM): 13 substitution-language queries across the 4 pillars (value-chain layers as scaffold), SearXNG local JSON API, time_range=month (structural cadence, not news-day), 2.5s sleeps, dedup vs ALL existing drift evidence URLs + 14d feed_raw.json, caps 3 candidates/query, appends per-query health ledger to drift_query_health.jsonl. Verified live: 13 queries → 39 fresh candidates in ~35s (real hits: NVIDIA 800VDC architecture, CPO production planning, 8-inch free-standing GaN substrate paper, TSMC 2nm node).
- **Cron job `e9711f5abb15` — "Drift Detector"** (every 360m, enabled, delivers to this Discord thread): the prompt runs the health gate, re-runs drift_scan.py, then the LLM does ONLY the win/lose + M/T/C judgment per SCHEMA.md (max 2 drift files/run, max 2 web fetches, quality bar = named process swap + named winner, "additive, no clean loser" allowed, thinkpieces rejected), files DRIFT-NNN via the exact schema, runs drift_track_d.py, appends log.md, commits. Deterministic work stays in scripts; LLM tokens spent only on the genuinely hard inference (the old→new + winner/loser judgment).
- Query doctrine from self-hosted-search-mcp skill applied: one query = one signal 3-6 words, no year tokens (recency via time_range), site: precision sources where useful.
- jobs.json backed up (jobs.json.bak_drift_1792903570) before the 4th job was added; verified 4 jobs, unique ids, next_run_at set explicitly.
- **Remaining (Phase 4):** cascade-on-event wiring into concepts/CASCADE.md — drift events become CASCADE triggers (today CASCADE triggers on a company's score; the upgrade is to trigger on the drift event, propagating to ALL linked dossiers + next value-chain layer).
- **Pending user approval (protected-write gate):** AGENTS.md gains wiki/drifts/ + root substitution_short_list.md to topology/consumers. Staged in log; do not route around the gate.

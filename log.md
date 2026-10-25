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

## 2026-10-25 — Phase 4: cascade-on-event wiring (CASCADE.md Trigger v2)

- `concepts/CASCADE.md` gains **Trigger v2 — Drift-Event cascade**: the trigger is the DRIFT, not the ticker. Fires on Composite >= 500 (CRITICAL) OR status transition to `scaling` (gate-fire: NRC SDA, foundry commitment, hyperscaler PPA campus-wide).
- Wiring: (1) read event edges (winner/loser/Sequencing/competitive; FM-2 net_drift_position handles dual-role nodes), (2) deterministic re-sync via drift_track_d.py (one re-rate propagates to all linked dossiers — no manual per-ticker edits), (3) cascade to the NEXT value-chain layer via Sequencing `enables`/`prerequisite-for` (450mm wafer → large-substrate makers → large-wafer tool makers), (4) FM-4 private-winner supplier-discovery (Anduril → public edge-NPU/sensor suppliers), (5) losers' exposure re-estimated from FMP fundamentals (revenue line per value-chain layer) at the next Deep-Dive pass — lifts sub_downside from `est.` to measured.
- Guards: <500 drifts don't self-cascade (re-rate or gate-fire only); max 4 drifts/cycle; 3 cycles w/ 0 new tickers → SATURATED; cascade never auto-adds to ACTIVE.
- **Build status: Phases 1-4 COMPLETE.** The system is now a self-sustaining loop: detector cron finds substitution language → files/scores drift events → Track D + backlinks propagate deterministically → CRITICAL/gate-fire drifts cascade on the event to the next value-chain layer → new tickers feed the existing inclination pipeline.

## 2026-10-25 — Drift Detector judgment leg executed on live candidates (end-to-end proof)

- Ran the detector's judgment leg manually on the 39 live candidates from drift_scan.py (the same leg the cron job will run autonomously every 360m). Quality bar applied: named process swap + named winner required; thinkpieces/trend-pieces rejected.
- **Disposition of all 39: 1 FILED, 3 UPDATED (dated evidence notes on existing drifts), 35 REJECTED.**
  - **FILED DRIFT-008 — Copper (SerDes/ELSFP) → co-packaged optics / integrated photonics at the scale-out interconnect layer (294 HIGH, scaling, ai-infra).** A genuinely NEW substitution event with no prior drift object. Winners: AVGO (named, >ceiling), MRVL, COHR, IIVI (sub-ceiling photonics tier); Ayar Labs (PRIVATE) as the FM-4 private co-winner → supplier-discovery cascade. Loser class: copper/ELSFP interconnect suppliers (Molex named, not in universe → class row). Evidence: Broadcom "copper no longer able to keep pace" + EE Times "CPO moves from promise to production planning" (both VERIFIED).
  - **UPDATED DRIFT-003** (ASML 2013 450mm-litho PAUSE = counter-signal reinforcing the NOISE score; score unchanged), **DRIFT-004** (Intel >1M High-NA wafers = tool-level demonstrated strengthening; HVM commit still pending; score unchanged 144), **DRIFT-006** (NRC rule change + NuScale US460 review = licensing-gate clock accelerating; SDA not yet fired; score unchanged 105).
  - **REJECTED (35):** ASML $13B quarter (earnings, not a substitution), TSMC 2nm node (belongs to DRIFT-001), transformer lead times (no clean substitution line), GaN market-growth thinkpieces, immersion-cooling explainers, SMR PPA trackers (all DRIFT-006 updates or trend coverage).
- **This is the end-to-end proof the loop yields a real artifact:** deterministic SearXNG scan → LLM win/lose + M/T/C judgment → filed DRIFT-008 → drift_track_d.py re-synced Track D + 20 backlinks + INDEX. The Goldman-consultant standard (grounded, dated, linked, no invented numbers) held.
- **All 4 build phases complete AND the autonomous loop has produced real output.** The system now runs unattended: detector cron (e9711f5abb15, 360m) → judgment → file/score → deterministic propagation → cascade-on-event.

## 2026-10-25 — drift-scan 06:48 (e9711f5abb15, 360m cadence)

- Health gate ALL_GOOD; drift_scan.py fresh: 13 queries → 36 fresh candidates; 4 cascade queries (DRIFT-002) → 0 results.
- **FILED DRIFT-009 — 54V busbar + multi-stage AC→DC rack power → 800V DC direct distribution (architecture-substitution, ai-infrastructure, 6×6×5 = 180 EMERGING).** Trigger: Microchip (MCHP) + Navitas (NVTS) 800V-to-6V OCP rack-power reference design, 2026-10-05 PR (VERIFIED fetch). Winners MCHP (digital power control + security layer) and NVTS (GaNFast front-end device); loser = class row (legacy mid-rail silicon final-stage content, claimed 0.6, est. sub_downside <10) — no clean single US-listed loser, honest note. Sequencing: sequences-after DRIFT-002 (GaN-on-Si power Si input layer), enables-window shares with DRIFT-005. Re-rate to HIGH (288) on first hyperscaler 800V DC rack volume commitment.
- **REJECTED (35 of 36):** ASML High-NA explainers ×3 (DRIFT-004 already tracked; Intel/TSMC adoption timeline is the same event's next-cycle check), GAA explainer articles ×3 (DRIFT-001), Polar/imec 8-inch GaN-on-Si collaboration ×3 (DRIFT-002 next-layer evidence — feeds cascade leg, not a new drift; Polar is the incumbent making the new process, not a new substitution), advanced-packaging trend pieces ×3 (DRIFT-001 companion / thinkpieces), liquid-cooling explainers ×3 (DRIFT-005), 800V thinkpieces ×2 (energiesmedia + quantumscape trend coverage — subsumed into DRIFT-009 evidence), CPO explainer ×3 (DRIFT-008), AMD MI450/Oracle (deployment news, not substitution), immersion explainers ×3 (DRIFT-005), SMR/PPA explainers + trackers ×6 (DRIFT-006), NRC AP1000 design-cert renewal ×3 (regulatory maintenance of an existing design — DRIFT-006 next-cycle check, not a new drift: no new reactor tech, no named winner/loser beyond existing edges), transformer lead-time reports ×3 (supply-constraint data, no process swap).
- **CASCADE leg (Trigger v2):** DRIFT-002 eligible (composite 600 CRITICAL), 4 next-layer queries (GaN-on-Si epiwafer power device entrants) → 0 fresh results. 0 new tickers surfaced → cascade_state.json zero_streak 0→1 (saturates at 3). Notable: the Polar/imec Leg-A hits are on-target evidence for DRIFT-002's open question (8-inch GaN-on-Si volume path) but name no NEW tracked-universe ticker.
- drift_track_d.py re-sync: INDEX.md regenerated (9 drifts), substitution_short_list.md rebuilt, 21 company backlinks touched (MCHP +1, NVTS +1 → now carries DRIFT-009 edges).

## 2026-10-25 — drift-scan 13:11 (e9711f5abb15, 360m cadence)

- Health gate ALL_GOOD; drift_scan.py fresh: 13 queries → 39 fresh candidates; 4 cascade queries (DRIFT-002) → 0 results.
- **0 drifts filed (39 candidates reviewed, 39 rejected/absorbed).** All 39 are repeats of the 06:48 cycle's dispositions: ASML High-NA explainers ×3 + Intel-vs-TSMC adoption piece (DRIFT-004 next-cycle check, HVM commit still pending), GAA/WSe2/etch papers ×3 (DRIFT-001 / academic, no commercial swap), 450mm FOUP market-assessment thinkpiece + purewafer.com company page + metalens foundry piece ×3 (DRIFT-003 companion / no process-swap commitment), Polar+IC-Link imec 8-inch GaN-on-Si ×3 (recurring — DRIFT-002 next-layer evidence, appended to [det002a]; Polar is PRIVATE, no new US ticker, no new substitution), advanced-packaging/panel-level trend pieces ×3 (DRIFT-001 companion thinkpieces), liquid-cooling explainers ×3 (DRIFT-005), Trane 800V DC chiller PoC (recurring — VERIFIED fetch: 2026-09-30, TT+Eaton+Danfoss, 3.5 MW, ~2% efficiency; appended to DRIFT-009 [det009a] as second dated proof point, lab PoC only → no re-rate; TT = potential new mid-cap winner row, cap pending FMP) + 800V trend pieces ×2 (subsumed), CPO explainers ×3 (DRIFT-008), AMD MI450/Oracle 50k-GPU (deployment news, not substitution), immersion explainers ×2 (DRIFT-005), SMR/PPA explainers ×3 (DRIFT-006), NRC AP1000 DC renewal ×3 (regulatory maintenance — appended to DRIFT-006 [det006b]) + Google–Constellation 20-yr $4.3B uprate deal (CEG cash-flow edge reinforced; existing-PWR uprates, not an SDA-gate event; appended to [det006b]) + SMR EPC-partnership piece (trend), transformer lead-time reports ×3 (supply-constraint data, no process swap).
- **CASCADE leg (Trigger v2):** DRIFT-002 eligible (composite 600 CRITICAL), 4 next-layer queries → 0 fresh results. 0 new tickers surfaced → cascade_state.json zero_streak 1→2 (saturates at 3; one more zero cycle and DRIFT-002 cascade stops firing).
- drift_track_d.py re-sync: INDEX.md regenerated (9 drifts, composites unchanged), substitution_short_list.md rebuilt, 21 company backlinks touched.

## 2026-10-25 (evening) — drift-scan
- Health gate: ALL_GOOD; drift_scan: 13 sector queries → 39 fresh candidates; 4 cascade queries (DRIFT-002) → 0 fresh.
- 0 drifts filed (39 candidates reviewed, 39 rejected: 27 dupes of existing drifts DRIFT-001/002/003/004/005/006/008/009 — incl. Polar/imec 8" GaN (already in DRIFT-002 dated notes; PRIVATE company, same substitution); 6 non-drifts — transformer lead-time/pricing (supply constraint, no process swap), NRC AP1000 SDC renewal (regulatory status under DRIFT-006 pillar, no new named winner), vendor/thinkpiece content).
- Cascade leg: DRIFT-002 zero_streak 2→3 → SATURATED (no next-layer tickers 3 consecutive cycles); cascade_state updated; 0 new tickers surfaced.
- Cascade gate: 0 eligible next cycle (DRIFT-002 saturated).
- Track D: 21 dossier backlinks regenerated; no new substitution_short_list rows.

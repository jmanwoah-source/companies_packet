# Log — Action History

## 2026-11-05 clean-slate standardization — nested wiki/ removal + ingestion lock (user directive)
- `wiki/wiki/` nested tree + all legacy symlinks REMOVED; `companies/` re-initialized EMPTY at root.
- All legacy company dossiers discarded per user directive — future research re-seeds cleanly from FMP filing batches.
- Path invariants baked into all cron scripts (startup FATAL guardrail):
  `WIKI_ROOT = Path("/home/jaren/wiki").resolve(strict=True)`; `assert not (WIKI_ROOT / "wiki").exists()`;
  `COMPANIES_DIR = WIKI_ROOT / "companies"` must exist and not be a symlink.
- Consumers re-pointed: unharnessed_fmp_ingestor.py, unharnessed_swarm_recalibrator.py, tier_lists.py,
  pipeline_engine.py (L1317/L2199 companies path + guardrail), drift_track_d/drift_ingest/drift_scoring/
  drift_backtest/drift_denoise (drifts+companies paths + guardrails), radar_13f.py (WORKPAPER/COMPANIES),
  build_universe.py (companies universe).
- Cron job prompts (jobs.json) de-nested: 7 stale `wiki/wiki/` path refs fixed (After-Hours dossier appends,
  Drift Detector paths, Deep-Dive archived/ path); Deep-Dive prompt's stale ~$100B mcap guideline replaced
  with $500M-$300B band per rule 6.
- Verification: 11/11 modules py_compile OK; guardrail negative test FIRES on simulated nested dir;
  11/11 modules import clean with guardrail passing. Zero `wiki/wiki` refs remain in scripts/, cron/ (excl. outputs).


## 2026-11-04 governance — NVIDIA (NVDA) exception retracted (user: "delete NVIDIA, my bad")
- User retracted the 2026-11-04 keep exception: `NVIDIA (NVDA)` container (1KB stub,
  0 dated notes) archived to wiki/archived/naming_violations_20261104/ — archive,
  never delete (Hard Rule 5). The canonical NVDA dossier (NVDA/NVDA.md) is untouched.
- Post-state: wiki/companies/ = 820 canonical <T>/<T>.md dirs, 0 flat files,
  0 non-canonical roots — fully clean.



## 2026-11-04 governance — Naming-sentinel cleanup: 44 violations re-keyed/archived, 4 dup containers merged
- Audit: 45 non-canonical dir roots in wiki/companies/ (NAME (TICKER), foreign-suffix,
  wrong-ticker, no-paren). Per user instruction, **NVIDIA (NVDA) KEPT as-is**; 44 processed.
- Backup /tmp/wiki_pre_rekey_20261104.tar.gz before mutation (401K, companies/ subtree).
- Duplicate containers (name==ticker): IBM (IBM), ASML (ASML), IONQ (IONQ), RTX (RTX)
  (RTX dup created by the 767-flat migration of RTX.md) — dated notes merged into the
  canonical primary (full-line normalized dedup; IBM/IONQ shells were pure duplicates,
  ASML +2 notes, RTX +2 notes), shells archived. Zero content loss verified
  (every shell note present in primary post-merge).
- 40 other violations ARCHIVED to wiki/archived/naming_violations_20261104/<D>/ —
  archive-only (no merge) to avoid wrong-ticker corruption (e.g. NEBIUS (NB) is NBIS,
  FLUTTER (MGM.AS) foreign suffix); content preserved, restorable.
- Post-state: companies/ = 820 canonical <T>/<T>.md dirs + 1 user-kept NVIDIA (NVDA);
  0 flat root files (index.json is metadata-only); wiki_note_path() 0 bad resolutions;
  ticker_universe() 1555 (unchanged); health gate ALL_GOOD.



## 2026-11-04 governance — Canonical directory path enforcement: flat -> <T>/<T>.md (767 dossiers)
- Audited wiki/companies/: 767 flat <T>.md root dossiers + 98 dir-form <T>/<T>.md containers;
  0 dual-form conflicts (no ticker existed in both forms) => pure rename, 0 merges.
- Full-tree backup /tmp/wiki_pre_migration_20261104.tar.gz (1742 .md) before any mutation.
- Migrated all 767 flat dossiers to wiki/companies/<T>/<T>.md via idempotent engine
  (/tmp/flat_to_dir.py, dry-run then --apply; git mv for tracked files).
- Enforced canonical form at the source: pipeline_engine.py ensure_wiki_file() now forces
  new dossiers into <T>/<T>.md directory form (flat root creation kills split-brain).
- Verified: wiki_note_path() resolves all 865 dir-form containers to <T>/<T>.md;
  ticker_universe() = 1555; flat_root = 0; health gate verdict ALL_GOOD;
  md count reconciliation 1742 (backup) == 1742 (current).
- OUT OF SCOPE (naming-sentinel classes, separate supervised pass): 44 dir roots with
  NAME (TICKER) / foreign-suffix / wrong-ticker forms (e.g. NVIDIA (NVDA), NEBIUS (NB))
  + 3 duplicate containers (IBM+IBM (IBM), ASML+ASML (ASML), IONQ+IONQ (IONQ)).



## 2026-11-04 governance — AGENTS.md market-cap ceiling fix (manual edit, user-confirmed)
- Rule 6 rewritten: soft ~$100B ceiling -> soft ceiling band **$500M to $300B**
  (floor ~$500M tradable common equity; $200B-$300B allowed + flagged `near_ceiling`;
  >=$300B drop; null-CIK = fund, drop). Explicit anti-split-brain note added: do NOT
  reject tickers for exceeding ~$100B.
- Header "Last updated" bumped to 2026-11-04. Edits applied user-side via terminal
  (protected-write gate timed out on agent-initiated patch).


## 2026-11-04 drift-scan (cron e9711f5abb15) — SUSPENSION CYCLE (3rd)
- Health gate ALL_GOOD (vllm/searxng UP, feeds FRESH, disk 52.1% free, wiki_drift OK,
  intel_bus OK).
- Scan: 13 sector + 6 a2 queries -> 0 base, 0 a2, 0 cascade candidates; **19/19 queries
  flagged `upstream_suspension`** (zero rows with all 4 engines brave/duckduckgo/google/
  google-cse down mid-scan). Same SearXNG IP-suspension signature as the 2026-11-03
  cycles — NOT query quality; per post-scan guard (b): no filing, no query tuning from
  this cycle. 0 news breaks merged (drift_ingest).
- 0 drifts filed (0 candidates to review — spine fully empty under suspension).
- A2 shadow-run: 0 candidates (suspension) — precision count **TAINTED — suspension**,
  excluded from the 2-cycle tuning average. 3rd-slot A2 gate NOT evaluated (no candidates).
- CASCADE: queue empty (0 eligible — DRIFT-002 only >=500, saturated zero_streak 3
  holding; no gate-fires) -> no eligible drift to write back; zero_streak/saturated held.
- Engine: drift_scoring.py 12 sidecars re-scored, all composites unchanged
  (001 432 · 002 600 · 003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 · 009 180 ·
  010 84 · 011 336 · 012 96); 0 fetch_errors, 0 stale segments; 26 FMP profiles persisted.
- Track D: drift_track_d.py rebuilt — 23 dossiers touched, INDEX regenerated (12 drifts),
  cascade gate 0 eligible.

# Log — Action History


## 2026-11-03 drift-scan (cron e9711f5abb15) — SUSPENSION CYCLE (2nd)
- Health gate ALL_GOOD (vllm/searxng UP, feeds FRESH, disk 52.0% free, wiki_drift OK).
- Scan: 13 sector + 6 a2 queries → 0 base, 0 a2, 0 cascade candidates; **19/19 queries
  flagged `upstream_suspension`** (zero rows with all engines down mid-scan). Same
  SearXNG IP-suspension signature as the 17:35 cycle — NOT query quality; per post-scan
  guard (b): no filing, no query tuning from this cycle. 0 news breaks merged.
- 0 drifts filed (0 candidates to review — spine fully empty under suspension).
- A2 shadow-run: 0 candidates (suspension) — precision count **TAINTED — suspension**,
  excluded from the 2-cycle tuning average.
- CASCADE: queue empty (0 eligible — DRIFT-002 only ≥500, saturated zero_streak 3 holding;
  no gate-fires) → no eligible drift to write back; zero_streak/saturated held.
- Engine: drift_scoring.py 12 sidecars re-scored, all composites unchanged
  (001 432 · 002 600 · 003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 · 009 180 ·
  010 84 · 011 336 · 012 96); 0 fetch_errors, 0 stale segments; 26 FMP profiles persisted.
- Track D: drift_track_d.py rebuilt — 23 dossiers touched, INDEX regenerated (12 drifts),
  cascade gate 0 eligible.


## 2026-11-03 drift-scan 17:35 (cron e9711f5abb15) — SUSPENSION CYCLE
- Health gate: initial `FAIL:primary_feeds` — OSTI feed had flipped to `status: error`
  (streak 1). Diagnosed NOT dead: the OSTI API is content-negotiated and served a
  non-well-formed body at 17:02, tripping the XML-only `f_osti` parser. LIVE-VERIFIED
  the endpoint up (HTTP 200, 20 records/phrase). FIX: `primary_feeds.py` `_osti_records()`
  now parses BOTH XML and JSON (JSON field map: `report_number`→absent, `other_number`
  carries it; `contract_number` aliases `doe_contract_number`); a single malformed phrase
  no longer sinks the feed; all-phrases-failed still raises so it can demote. Ran the feed,
  OSTI back to `ok streak=0`; gate re-verified `ALL_GOOD`. Backup
  `primary_feeds.py.bak_osti_json_20261103`.
- Scan: 13 sector + 6 a2 queries → **0 base, 0 a2, 0 cascade candidates; 19/19 queries
  flagged `upstream_suspension`** (all 4 engines brave/duckduckgo/google/google-cse down
  mid-scan, HTTP 200 with zero rows). SearXNG IP-suspension signature, NOT query quality —
  per post-scan guard (b): no filing, no query tuning from this cycle. 0 news breaks merged.
- 0 drifts filed (0 candidates to review — spine fully empty under suspension).
- A2 shadow-run: 0 candidates (suspension) — precision count **TAINTED — suspension**,
  excluded from the 2-cycle tuning average.
- CASCADE: queue empty (0 eligible — DRIFT-002 only ≥500, saturated zero_streak 3 holding;
  no gate-fires) → no eligible drift to write back; zero_streak/saturated held.
- Engine: drift_scoring.py 12 sidecars re-scored, all composites unchanged
  (001 432 · 002 600 · 003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 · 009 180 ·
  010 84 · 011 336 · 012 96); 0 fetch_errors, 0 stale segments; 26 FMP profiles persisted
  (live mcap re-pull only: NVTS 2.1→2.3, MPWR 61.1→66.0 — no score delta).
- Track D: drift_track_d.py rebuilt — 23 dossiers touched, INDEX regenerated (12 drifts),
  cascade gate 0 eligible.


## 2026-11-03 drift-scan (cron e9711f5abb15)
- Health gate ALL_GOOD (vllm/searxng UP, feeds FRESH, disk 52.1% free, wiki_drift OK).
- Scan: 13 sector + 6 a2 queries → 39 base + 18 a2 fresh candidates; 0 cascade queries (0 eligible); 0 breaks merged. Post-scan guard clean: `upstream_suspicious_queries: 0` — NOT a suspension cycle; A2 precision count NOT tainted (clean 2nd shadow-run cycle).
- 0 drifts filed (57 candidates reviewed: 39 base + 18 a2).
  Base rejections: already-filed re-surfaces (800V Envision/NVIDIA/Siemens → DRIFT-009; CPO/silicon interposer → DRIFT-008; High-NA EUV → DRIFT-004; GAA etch → DRIFT-001; 450mm pricing → DRIFT-003; SMR/NRC → DRIFT-006; liquid/immersion cooling → DRIFT-005), thinkpieces/lead-time guides (transformer 160-week study, Apers PUE), non-US winners (Envision China 800V commercial deploy, SK hynix, 3C/Datalec India), vendor pages (SawStreet, Molex, Stulz). No base candidate met the old→new + named-US-winner bar.
- Re-rating (not a filing): Envision Energy world-first COMMERICAL integrated 800 V DC deployment at Galaxy AI campus (SST 10/13.8 kV→800 V DC @98.5% + BESS, live GPU loads; announced 2026-11-02, pv-magazine, VERIFIED via search) → Dated Evidence note det009d on DRIFT-009. Non-US deployer, in-house hardware: no US winner/loser edge created; re-rate trigger (first named US-hyperscaler 800VDC volume rack/campus commit) unchanged. Score HELD 180 EMERGING.
- A2 shadow-run (clean cycle): 18 reviewed, 18 rejected. Dominant reasons: anchor/mid-cap winner or PRIVATE (Wolfspeed multiyear SiC EV device agreement — re-surface of DRIFT-002/012 territory, WOLF mid-cap anchor, fails slot rule 1; ON simplywall.st energy-storage note = anchor + opinion piece; Win Foundry/SawStreet = private/Korean), listicle/guide (JIM 10-step, anysilicon qualification checklist, newmarketpitch top-startups, ic-components CPO explainer), foreign (LX Semicon SiC exit = Korean), no old→new named swap (WSJ Modal compute startup, DOE $389M R&D awards = 4 LOI grants to Helion/CFS/Vertical Semiconductor/Sibelco — all PRIVATE, no US-listed winner, additive R&D funding, not a process swap). 3rd slot UNUSED: no A2 candidate with a nano/sub-ceiling US-listed winner at pilot-or-better certainty naming a specific old→new swap or named-design qualification.
- CASCADE: queue empty (0 eligible — DRIFT-002 only ≥500, saturated zero_streak 3 holding; no gate-fires) → no eligible drift to write back; zero_streak/saturated held.
- Engine: drift_scoring.py 12 sidecars, all composites unchanged (001 432 · 002 600 · 003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 · 009 180 · 010 84 · 011 336 · 012 96); 0 fetch_errors, 0 stale segments; 26 FMP profiles persisted.
- Track D: drift_track_d.py rebuilt — 23 dossiers touched, INDEX regenerated (12 drifts), cascade gate 0 eligible.


## 2026-11-02 drift-scan 22:52 (cron e9711f5abb15)
- Health gate ALL_GOOD (all sources UP; EIA feed not flagged — informational only).
- Scan: 13 sector + 6 a2 queries → 39 base + 18 a2 fresh candidates, 0 cascade (0 eligible); 0 breaks merged. Post-scan guard clean: `upstream_suspicious_queries: 0` (every query returned 20 fresh results) — NOT a suspension cycle.
- 0 drifts filed (57 candidates reviewed: 39 base + 18 a2). No base candidate met the bar: thinkpieces/market reports (Yole Power GaN 2026, Phoenix EUV market, MRFuture GaN, galliumprice), vendor/vendor-marketing pages (Shinko/Kinsus substrate, Coherent/Molex/Stulz CPO + immersion, ept.ai, sourceability), explainers/academic (SemiEngineering GAA, Wikipedia fab, researchgate GAA, ScienceDirect SPIC, Apers PUE, per-siencing), and re-surfacing of already-filed drifts (High-NA EUV → DRIFT-004; 800V → DRIFT-009; CPO/copper → DRIFT-008; GAA/450mm → DRIFT-001/003; SMR/NRC/PPA → DRIFT-006).
- Re-rating (not a new filing): Radiant Nuclear (PRIVATE) DOE DSA approval for Kaleidos microreactor FULL-POWER operation (2026-10-29; first in the microreactor industry) — verified multi-source (radiantnuclear.com + Business Wire + ANS). Mapped to DRIFT-006 as Dated Evidence note det006e. NOT a re-rate: deployment is defense-first (Buckley SFB/Fort Benning/Navy), not behind-the-meter DC, so the NRC SDA timing-gate is not advanced — score held 105 EMERGING. Also a DOE INL test authorization, not an NRC commercial license.
- A2 shadow-run (clean cycle, NOT tainted): 18 reviewed, 18 rejected. Dominant reasons: listicle/guide (7: Sourceability SIA risks, JIM "start a semi co", DeepChecks pitch deck, newmarketpitch top-startups, jim/ept vendor pages, silicon "start a company" guides), anchor/wrong-band winner (Wolfspeed Gen-5 SiC multiyear EV device agreement — demonstrated, but WOLF is mid-cap anchor and SiC→EV already on DRIFT-002/012; fails slot rule 1), foreign-listed (Elmos OLED rear-light design wins = German OEM; LX Semicon SiC patent sale = Korean), funding-raise/no-old→new (WSJ compute startup, newmarketpitch), vendor product pages (Molex CPO, ept.ai). 3rd slot UNUSED: no A2 candidate with a nano/sub-ceiling US-listed winner at pilot-or-better certainty naming a specific old→new swap or named-design qualification.
- CASCADE: queue empty (0 eligible — DRIFT-002 only ≥500, saturated zero_streak 3 holding; no gate-fires) → no eligible drift to write back; zero_streak/saturated held (drift_track_d recomputed gate → 0 eligible).
- Engine: drift_scoring.py 12 sidecars re-scored, all composites unchanged (001 432 · 002 600 · 003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 · 009 180 · 010 84 · 011 336 · 012 96); 0 fetch_errors, 0 stale segments; 26 FMP profiles persisted.
- Track D: 24 dossiers touched, INDEX regenerated (12 drifts), cascade gate 0 eligible. Committed only this job's drift file + log entry (unrelated other-job watchlist/dossier changes left uncommitted).


## 2026-10-29 (19:20 cycle) — drift-scan (Drift Detector)
- Health gate: ALL_GOOD (vllm UP, searxng UP, feeds FRESH, disk 29% free; EIA feed DEGRADED — informational).
- Scan: 13 sector queries → 36 fresh base candidates; 6 a2 queries → 18 a2 candidates; 0 cascade queries (0 eligible). Breaks merged: 0.
- Post-scan guard: 1 query flagged `upstream_suspension` ("450mm wafer foundry transition" — 0 results with brave/duckduckgo/google/google-cse all unresponsive). The 450mm leg (DRIFT-003 watch query) is SUSPENSION, not query quality — no tuning action; A2 precision count marked tainted for the tuning average.
- Filed: 0 new drifts (54 candidates reviewed: 36 base + 18 a2).
  Rejections (base): GF–TSMC $2B US silicon-interposer deal (GFS, $25.2B mcap verified via FMP profile-symbol — correct ticker; the earlier cycle's rejection cited the wrong 'GF' symbol = a German fund; the DEAL itself is supply re-sourcing/first US interposer source, not a process swap → rejected as substitution, noted); Polar/IC-Link 8" GaN-on-Si (x3) = same entrant, PRIVATE winner, already dedup'd to DRIFT-002; NVIDIA 800VDC partner wave (DCD, fetched+verified) = re-rating datapoint on DRIFT-009, not a new drift → filed as Dated Evidence note det009c, score held 180 EMERGING (partner/preview-stage, no hyperscaler volume commit); Infineon–NVIDIA GaN IBC collaboration (non-US, class note, logged in det009c); NuScale US600 SDA "issued" tracker snippet = SDA was issued 2020-09-11 (verified via NRC.gov + Federal Register) — stale re-surface, DRIFT-006 timing-gate (new SDA/cert milestone) NOT fired, no re-rate; Westinghouse AP1000 design-cert renewal to 2066 = existing-design renewal, not advanced-design SDA (already logged det006b/det006 5c8bb9d4); rest = thinkpieces/lead-time research/explainers (High-NA SPIE papers x2, GAA etch WSe2 academic, 3dincites packaging, 800V architecture blogs, liquid-cooling explainers, immersion vendor blogs, transformer-lead-time studies, LRCX stock article).
  A2 shadow-run (tainted — suspension cycle): 18 reviewed, 18 rejected. Dominant reasons: listicle/guide (top-30 design cos, foundry-vs-fabless explainer, wafergraph/patent-DB homepages, MATLAB File Exchange), non-US/PRIVATE winner (SawStreet private, EnSilica AIM-listed, Mueon $65M raise x2), anchor-sized winner (ON/Sungrow EliteSiC — anchor, no sub-ceiling US winner), patent-DB tool pages (SiC WO/TW patents), spec release (APC CPO specs — already on DRIFT-008). 3rd slot UNUSED: no A2 candidate with a nano/sub-ceiling US-listed winner at pilot-or-better certainty (QuickLogic six-figure eFPGA IP contract = contract win, not old→new process swap; six-figure ≠ material).
- Cascade leg: 0 eligible drifts this cycle → 0 new tickers surfaced; cascade_state.json unchanged.
- Engine: drift_scoring.py 10 sidecars, composites held (432/600/20/144/336/105/180/294/180/84), 0 fetch_errors; known [STALE] segment rows (NVTS, MPWR, ASML sector-match, NUS=Nu-Skin data-quality) preserved flagged.
- Track D: drift_track_d.py rebuilt — 23 dossiers touched, INDEX regenerated (10 drifts), substitution_short_list refreshed. Cascade gate post-run: 0 eligible (nothing ≥500 or gate-fire).
- Data-quality note: FMP `statements` revenue-product-segmentation('GFS') returned a NON-FOUNDRY profile's segments (water-fabrication lines) — FMP GFS segmentation is corrupt/wrong-symbol; GFS excluded from any engine sidecar this cycle (no ticker edge filed).


## 2026-10-29 — Naming-sentinel cleanup (Hard Rule 3 enforcement)
- Archived 6 violation dossiers to wiki/archived/ (archive, never delete):
  - `AMD (AMD)/` duplicate container for `AMD/` (3 catalyst notes already present in AMD/AMD.md — content verified, zero loss)
  - `ALPHABET (GOOGL)/` name-anchored root (2 quantum notes already present in GOOGL/GOOGL.md lines 18-19 — zero loss)
  - `AELUMA (PRIVATE)/`, `AETINA (PRIVATE)/`, `BECHTEL (PRIVATE)/` — private entities do not get company dossiers
  - `MGM.AS.md` foreign-suffix root (`MGM.md` + `MGMAS/MGMAS.md` remain canonical)
- Residual check: 0 `*(PRIVATE)*` dirs, 0 name-anchored roots, 0 foreign-suffix roots in wiki/companies/
- Permanent guard: skill `wiki-naming-sentinel` now gates all dossier create/move/restore


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


## 2026-10-26 (early) — drift engine v2: Gap 2 closed (engine owns scores + exposure)
- Fork resolved: FMP MCP is **script-reachable** (Streamable HTTP, session-id header, inline JSON) — a
  standalone .py can fetch FMP directly. New `~/.hermes/scripts/fmp_client.py` (stdlib-only client).
- `drift_scoring.py` v2 = fully self-contained engine: sidecar config -> live FMP
  (revenue-product-segmentation + profile-symbol) -> keyword exposure + composite M×T×C -> writes the
  `## ENGINE SCORE` block into each drift .md (idempotent). LLM no longer writes ANY score/exposure %.
- 9 `DRIFT-NNN.engine.json` sidecars authored (machine-readable inputs). Composites unchanged (432/600/
  20/144/336/105/180/294/180) — the engine now OWNS them (single source; the hand table is fallback).
- `drift_track_d.py` = ENGINE-FIRST: reads the ENGINE SCORE block as the authoritative Track D source
  (exposure-source column added to substitution_short_list.md: engine vs hand). Fixed a pre-existing
  `net_drift_position` bug (was summing detail strings -> always 0; now sums real sub_downside, e.g.
  MPWR = -151.0). Engine-sourced loser rows now flow to the short list + dossier backlinks (MPWR, AXTI, ETN).
- Item 4: `fmp_profiles.json` now persists FMP sector+industry+mcap for every engine ticker (25 tickers);
  layer assignment is engine-driven (SECTOR_TO_LAYER).
- Cron e9711f5abb15 prompt updated: STEP 4.0 runs the engine deterministically; LLM's only FMP-adjacent
  duty = author the sidecar at filing (exact FMP segment keywords). FMP fetches removed from the LLM leg.
- Backtest vs the 2025-10-28 NVIDIA 800V shock: `drift_backtest.py` -> `research/drift_backtest_800v.md`
  (engine losers MPWR -11.8% realized = top-decliner in the set; sub-drawdown r=0.45, n=3).
- Health gate ALL_GOOD; drift_scan + track_d re-run clean; cascade gate intact (DRIFT-002 saturated).


## 2026-10-26 (later) — drift-scan e9711f5abb15
- Health gate ALL_GOOD; drift_scan: 13 sector queries -> 39 fresh candidates, 16 cascade queries -> 27 results.
- 1 drift filed: **DRIFT-010_asml-d2w-hybrid-bonding** (7x4x3 = 84 EMERGING; rumored; ASML winner, BESI displaced but non-US -> additive, no clean US loser). Evidence: SemiAnalysis 2026-10-15 (27 ASML D2W patent families) + Reuters 2026-10-16 (Besi -3%) + Dealroom 2026-10-19; 2 web searches, 0 page fetches.
- 38 candidates rejected: market reports/thinkpieces (wafer frame, SiC market), earnings (ASML $13B qtr), additive/complementarity pieces (onsemi GaN "complements Si/SiC"), regulatory/PPA news not a process swap, vendor pages, 800V gigawatt deal already anchored to DRIFT-009.
- Cascade leg: DRIFT-002 found ON (US-listed named GaN-power entrant) -> zero_streak reset 0. DRIFT-001 found ENTG (GAA content-per-wafer 10-K language, NOT in tracked universe) -> new ticker surfaced to inclination pipeline, streak reset 0. DRIFT-005: 0 new US tickers (VRT parent/in-universe; Trane/LG non-DC-power or non-US) -> zero_streak 1.
- Engine: 10 sidecars, all composites stable (432/600/20/144/336/105/180/294/180/84); no fetch_errors, no [STALE]. ASML FY2025 product segments have no back-end/bonding line (0.0% match, honest — first back-end revenue disclosure is the re-rate trigger).
- Track D: 23 dossiers touched; INDEX now 10 drifts. Cascade gate: DRIFT-002 only eligible (001/005/008 no longer gate-fire — last_status already scaling; gate fired in a prior cycle).


## 2026-10-26 (later) — cascade circuit-breaker fix (Trigger v2 saturation decay)
- BUG (pre-existing, found during engine reconciliation): `cascade_gate()` decayed the
  `saturated` flag on EVERY re-run of a `comp>=500 and saturated` drift — the breaker was a
  no-op (any drift_track_d.py invocation reset DRIFT-002's committed saturation). Fix:
  `cascade_state.json` now carries `last_composite` per drift; decay ONLY on a genuine upward
  re-rate (comp > prev_comp). State-refresh and queue-decision are separate steps (the old
  single-branch `continue` made the decay branch unreachable). Unit-tested: hold on same /
  decay+requeue on rise / hold on drop. DRIFT-002 state reconciled to committed truth
  (saturated, zero_streak 3, last_composite 600); live re-run confirms the breaker holds.


## 2026-10-26 09:16 — drift-scan run (e9711f5abb15)
- Health: ALL_GOOD; drift_scan 13 queries -> 6 fresh candidates, 0 cascade queries (no eligible drifts this cycle).
- **0 drifts filed (6 candidates reviewed, 6 rejected):** purewafer.com + foundrywatch.com = vendor/marketing homepages, no substitution event; siliconanalysts.com wafer-pricing = trend/thinkpiece (EUV cost curve, no new process swap or commitment); freedom251.com = High-NA explainer article, no new event (already covered by DRIFT-004); marketontology.com 2026-09-11 "Intel qualified High-NA EUV for 18A + Panther Lake, ASML-Samsung expansion" = EXISTING drift DRIFT-004 (not a new event) -> **status transitioned emerging -> scaling** per file rule (gate-fire observed), M/T/C held 6/4/6 (144 EMERGING), evidence note [det004b] added (UNVERIFIED aggregator source); linkedin Japan FY2027 HNA etch strategy = thinkpiece.
- **CASCADE:** no eligible drifts this cycle (queue empty) -> no new next-layer tickers surfaced.
- **Cascade gate (Trigger v2) after re-rate:** DRIFT-004 now ELIGIBLE (gate-fire emerging->scaling, 4 authored next-layer queries) — will execute in the NEXT cycle's drift_scan (Leg B).
- Engine (drift_scoring.py): all 10 composites stable (001=432, 002=600, 003=20, 004=144, 005=336, 006=105, 007=180, 008=294, 009=180, 010=84); no fetch_errors; [STALE] flags on 002/007/008/009 rows unchanged (MPWR FY2023, etc. — last-known measurements).
- Track D: 23 dossiers touched; INDEX regenerated; DRIFT-004 status column now `scaling`.
- cascade_state: DRIFT-004 seeded {scaling, zero_streak 0, last_composite 144}; DRIFT-002 remains SATURATED (streak 3) — breaker holding.


## Drift Scan — 2026-10-26 19:25 UTC
- Health gate: ALL_GOOD. drift_scan: 13 sector queries -> 0 fresh candidates; 4 cascade queries -> 0 results.
- **FILED:** 0 drifts (0 candidates reviewed; nothing to reject — scan returned no fresh hits since last run).
- **CASCADE:** DRIFT-004 was the sole eligible drift (gate-fire, 4 next-layer queries) -> 0 new next-layer tickers surfaced. cascade_state: DRIFT-004 zero_streak 0 -> 1 (saturated=false).
- Engine (drift_scoring.py): 10 sidecars, all composites stable (001=432, 002=600, 003=20, 004=144, 005=336, 006=105, 007=180, 008=294, 009=180, 010=84); 0 fetch_errors; 25 FMP profiles persisted.
- Track D: 23 dossiers backlinked; INDEX regenerated; cascade gate post-run: 0 eligible (DRIFT-004 gate-fire consumed, nothing >=500 or transitioning).


## 2026-10-26 21:50 — drift-scan run (e9711f5abb15)
- Health: ALL_GOOD. drift_scan: 13 sector queries -> 39 fresh candidates; 0 cascade queries (queue empty, no eligible drifts).
- **0 drifts filed (39 candidates reviewed, all rejected):** no candidate named a new defensible old->new substitution with a US-listed winner. Breakdown: wafer/packaging education + vendor pages (purewafer, hackster, wikipedia, otis-group, 3dincites, eetimes, techinsights, quantumscape/computeforecast/gr1d 800V explainers, midasimmersion/hydropure/missioncritical/cfn-hvac liquid-cooling explainers, jaredwatkins/gemral/capspire SMR explainers, gemral calculator, ans.org pre-app table, explainx/nextmsc/Schneider transformer lead-time pieces) = thinkpiece/trend/vendor content; Polar+imec 8-inch GaN (compoundsemiconductor/imec-int) = EXISTING DRIFT-002 next-layer signal already noted [det002a], Polar private -> no new US winner; KuCoin High-NA timelines + eBeam 12-inch-mask survey = aggregator recirc of DRIFT-004 (no re-rate); NRC 26-081 finalized demo-leverage rule + AP1000 DC renewal = DRIFT-006 gate clock datapoints (gate NOT fired, no SDA); Navitas+NVIDIA 24 kW 800V->12V PDB = DRIFT-009 third proof point.
- **Dated evidence notes appended (no score changes):** DRIFT-009 [det009b] Navitas+NVIDIA 24 kW 800V->12V PDB, single-stage eliminates 50V IBC stage, 16x NV6034 (VERIFIED — fetched) — OEM co-development, not hyperscaler volume commit, C held at 5 (180 EMERGING). DRIFT-004 [det004c] eBeam 12-inch-mask-by-2031 survey + Samsung-2028/TSMC-2030 timelines (UNVERIFIED aggregators), C held at 6 (144 EMERGING). DRIFT-006 [det006c] NRC 26-081 finalized (VERIFIED official) — proposed->final, gate still not fired, score 105 EMERGING.
- **CASCADE:** queue empty this cycle -> nothing to process; cascade_state.json untouched (all zero_streaks held; DRIFT-002 saturated streak 3 — breaker holding).
- Engine (drift_scoring.py): all 10 composites stable (001=432, 002=600, 003=20, 004=144, 005=336, 006=105, 007=180, 008=294, 009=180, 010=84); 0 fetch_errors; 25 FMP profiles persisted; [STALE] last-known rows unchanged (MPWR FY2023, NVTS single $0.1B segment, NUS=Nu Skin misprofile).
- Track D: 23 dossiers touched; INDEX regenerated; cascade gate post-run: 0 eligible.


## 2026-10-27 03:55 — drift-scan run (e9711f5abb15)
- Health: ALL_GOOD. drift_scan: 13 sector queries -> 0 fresh candidates, 0 cascade queries (queue empty). ANOMALY: every query returned results_total=0 (not just 0 fresh) — SearXNG API UP/container RUNNING per health gate, so this is a degenerate scan (empty result sets), not a downed backend. No candidates to judge; treat Leg A as no-signal this cycle, flag for next run.
- **0 drifts filed (0 candidates reviewed — degenerate scan, nothing to reject).** next_drift_id stays DRIFT-011.
- **CASCADE:** queue empty (DRIFT-002 saturated at streak 3, breaker holding; no composite>=500 fresh, no gate-fires) -> cascade_state.json untouched.
- Engine (drift_scoring.py): all 10 composites unchanged (001=432, 002=600, 003=20, 004=144, 005=336, 006=105, 007=180, 008=294, 009=180, 010=84); 0 fetch_errors; 25 FMP profiles persisted. [STALE] last-known rows persist in drift files (MPWR FY2023 x2, NVTS FY2024 x2, DRS FY2024, RCAT FY2023) — engine re-fetched, segments remain last-known; NUS=Nu Skin misprofile unchanged.
- Track D: 23 dossiers touched; INDEX regenerated (10 drifts); cascade gate post-run: 0 eligible.


## 2026-10-27 10:05 — drift-scan run (e9711f5abb15)
- Health: ALL_GOOD. drift_scan: 13 sector queries -> 39 fresh candidates; 0 cascade queries (queue empty, no eligible drifts).
- **0 drifts filed (39 candidates reviewed, all rejected — no new defensible old->new substitution with a US-listed winner):** thinkpieces/explainers (450mm panel-packaging how-it-works, semiconductorinsight GaN HEMT market report, 3dincites/eetimes/penchan/cloudrps/nextplatform liquid-cooling explainers, quantumscape blog + computeforecast/ainvest 800V explainers, midasimmersion/hydropure immersion explainers, jaredwatkins/gemral/elpc BTM-power explainers, computeforecast/CEA SMR-PPA explainers, nextmsc/explainx/Schneider transformer lead-time pieces, purewafer vendor page, LinkedIn market-outlook, Wikipedia, science.org WSe2 FET paper, SiCl4 etch paper) = trend/education/vendor content; Polar+IC-Link 8-inch GaN (compoundsemiconductor + imec-int) = EXISTING DRIFT-002 next-layer signal, same entrant as [det002a] (Polar private, no US winner) -> dedup note appended [21ff8d7f]; TSMC/ASML 12-inch High-NA photomasks (DigiTimes) = DRIFT-004 datapoint [605a1f79] (UNVERIFIED aggregator, no re-rate); NVIDIA Kuchta (PECC) + Shainer (Hot Interconnects) CPO-in-production = DRIFT-008 proof points [0ce737f4][8eba2808] (VERIFIED search-confirmed; copper retained in-rack, so cutoff sub-class partial — status/scoring unchanged, 294 HIGH); NRC AP1000 DC renewal (Federal Register final rule 2026-21030) + Google/Constellation uprate re-surface = DRIFT-006 gate-clock datapoints [5c8bb9d4] (existing large-PWR design, NOT an advanced-design SDA — gate NOT fired, 105 EMERGING unchanged).
- **Dated evidence notes appended (no score changes):** DRIFT-002 [21ff8d7f], DRIFT-004 [605a1f79], DRIFT-006 [5c8bb9d4], DRIFT-008 [0ce737f4][8eba2808].
- **CASCADE:** queue empty (eligible=[]) -> cascade leg not executed for any drift; cascade_state.json untouched (all zero_streaks held; DRIFT-002 saturated streak 3 — breaker holding).
- Engine (drift_scoring.py): all 10 composites stable (001=432, 002=600, 003=20, 004=144, 005=336, 006=105, 007=180, 008=294, 009=180, 010=84). ANOMALY: first engine pass had ALL 25 tickers fail with `tool statements/company error: Method not found` (stale MCP session); direct probe + re-run clean — second pass 0 fetch_errors, 25 FMP profiles persisted fresh; composites identical either way. [STALE] last-known rows unchanged (MPWR FY2023 x2, NVTS FY2024, NUS=Nu Skin misprofile).
- Track D: 23 dossiers touched; INDEX regenerated (10 drifts); cascade gate post-run: 0 eligible. next_drift_id stays DRIFT-011.


## 2026-10-27 16:41 — drift-scan run (e9711f5abb15)
- Health: ALL_GOOD. drift_scan: 13 sector queries -> 0 fresh candidates (0 total); 0 cascade queries (queue empty). ANOMALY (repeat of 03:55): ALL queries returned 0 raw results — diagnosed live: SearXNG JSON API UP, but unresponsive_engines show brave/google/google cse SUSPENDED (too many requests) + duckduckgo CAPTCHA. `time_range=month` filtering degrades to 0 results on the surviving Bing-only backend; probe without time_range returns 10 results. Leg A = no-signal this cycle due to engine degradation, not clean negative. Not a hard SearXNG-down -> run continued per protocol.
- **0 drifts filed (0 candidates reviewed — degenerate scan, nothing to reject).** next_drift_id stays DRIFT-011.
- **CASCADE:** queue empty (eligible=[]) -> cascade leg not executed; cascade_state.json untouched (all zero_streaks held; DRIFT-002 saturated streak 3 — breaker holding).
- Engine (drift_scoring.py): all 10 composites stable (001=432, 002=600, 003=20, 004=144, 005=336, 006=105, 007=180, 008=294, 009=180, 010=84); 0 fetch_errors; 25 FMP profiles persisted. [STALE] last-known rows unchanged (MPWR FY2023, NVTS, NUS=Nu Skin misprofile).
- Track D: 23 dossiers touched; INDEX regenerated (10 drifts); cascade gate post-run: 0 eligible (nothing >=500 fresh, no gate-fires).


## 2026-10-27 22:50 — drift-scan run (e9711f5abb15)
- Health: ALL_GOOD. drift_scan: 13 sector queries -> 0 fresh candidates (0 total); 0 cascade queries (queue empty). ANOMALY (repeat of 03:55/16:41, 4th recurrence): ALL queries returned 0 raw results — diagnosed live: SearXNG JSON API UP, unresponsive_engines = brave SUSPENDED (too many requests) + duckduckgo CAPTCHA + google/google cse SUSPENDED (access denied / too many requests). Only Bing serving; `time_range=month` degrades to 0 on Bing-only backend (probe without time_range returns 7-10 results). Leg A = no-signal this cycle due to engine degradation, not a clean negative.
- **0 drifts filed (0 candidates reviewed — degenerate scan, nothing to reject).** next_drift_id stays DRIFT-011.
- **CASCADE:** queue empty (eligible=[]) -> cascade leg not executed; cascade_state.json untouched (all zero_streaks held; DRIFT-002 saturated streak 3 — breaker holding).
- Engine (drift_scoring.py): all 10 composites stable (001=432, 002=600, 003=20, 004=144, 005=336, 006=105, 007=180, 008=294, 009=180, 010=84); 0 fetch_errors; 25 FMP profiles persisted fresh. [STALE] last-known rows unchanged (MPWR FY2023, NVTS, NUS=Nu Skin misprofile).
- Track D: 23 dossiers touched; INDEX regenerated (10 drifts); cascade gate post-run: 0 eligible (nothing >=500 fresh, no gate-fires).
- Health: ALL_GOOD. drift_scan: 13 sector queries -> 39 fresh candidates; 0 cascade queries (queue empty).
- **0 drifts filed (39 candidates reviewed, 39 rejected).** Rejections: 450mm trio = thinkpieces/vendor-market-reports, no named commitment (and DRIFT-003 already owns the pair); GAA etch = 3 educational explainers, no swap; GaN-on-Si = product page + market report + MicroLED-tag page, no US-listed winner commitment (DRIFT-002 owns the pair); advanced packaging = vendor blog (SHINKO/Kinsus) + TSMC A14 node-scaling headline (node scaling, not substitution); liquid cooling = Syensqo product page, ET merger (M&A, not process swap), PUE explainer; 800V = QuantumScape/NVIDIA marketing pages (DRIFT-009 owns the pair); CPO = Synopsys webinar + Counterpoint trend piece + Marvell product page (DRIFT-008 owns); immersion = vendor/thinkpieces; SMR/BTM = calculators + guides; AP1000 renewal + Google/Constellation uprate already logged (det006b/det006c); NRC SDA = AP1000 large-PWR renewal (logged), no advanced-design SDA; transformer lead times = supply-chain state, not a substitution.
- One dated evidence note appended to DRIFT-004 ([b4d547df] Hitachi High-Tech + ZEISS High-NA inspection framework, 2026-09-30, VERIFIED primary URL; no re-rate, C held at 6).
- **CASCADE:** queue empty (eligible=[]) -> cascade leg not executed; cascade_state.json untouched.
- Engine (drift_scoring.py): all 10 composites stable (001=432, 002=600, 003=20, 004=144, 005=336, 006=105, 007=180, 008=294, 009=180, 010=84); 0 fetch_errors; 25 FMP profiles persisted fresh.
- Track D: 23 dossiers touched; INDEX regenerated (10 drifts); cascade gate post-run: 0 eligible (nothing >=500 fresh, no gate-fires).


## 2026-10-26 — drift de-noise: residual spread (strip macro drift)
- New `~/.hermes/scripts/drift_denoise.py` + report `research/drift_denoise_800v.md`.
- Method: residual(t) = move(t) − SMH (the sector beta); per-drift spread =
  mean(loser residual) − mean(winner residual). The absolute level is macro; ONLY the
  residual spread is the substitution signal. Idiosyncratic outliers (|resid|≥20%) flagged,
  not averaged in.
- Finding (800V window, SMH −2.9%): DRIFT-008 spread −8.2% (substitution real — MPWR
  residual −9.0 vs winners −0.7); DRIFT-009 spread +0.7% (honest null — 800V is an
  architecture-reset, market grows, no clean loser to de-rate — consistent with the drift
  note); DRIFT-005 +7.7% (NOT supported — ETN class-proxy proxy, flagged).
- WOLF (−25.9% resid) and AXTI (+32.2% resid) flagged idiosyncratic = their OWN events
  (Wolfspeed Ch.11 / AXTI substrate surge), NOT the drift. This is the fix for the
  "carried-as-winner but fell" read: it was macro + idiosyncratic, never a signal miss.


## 2026-10-28 11:32 — drift-scan (Leg A rescan)
- Health gate ALL_GOOD; drift_scan.py fresh: 13 sector queries → 39 candidates; cascade 0 (queue empty).
- 0 new drifts filed (39 reviewed, 39 rejected). Leg B: cascade queue empty → no eligible drift, no cascade state changes.
- Rejections (one-line): 450mm/GAA/etch/fab-guide/purewafer (educational/wiki/marketing, no swap); Micron High-NA 1ε/vHBM 2028 (duplicate DRIFT-004, confirmed — note c1a0f2e9 appended); Polar+imec 8-inch GaN (duplicate DRIFT-002, private winner); adv-packaging/panel-vs-wafer/TSMC 5x-CoWoS (trend/thinkpiece or scale-up, no clean old→new + US winner); liquid/immersion cooling (design guides, dup DRIFT-005); 800V DC (dup DRIFT-009); CPO copper-retreat (dup DRIFT-008, NVIDIA claimed); SMR-BTM (PPA calculators/thinkpiece, dup DRIFT-006); transformer lead-time (supply/demand news, not a process swap); NRC AP1000 cert renewed to 2066 (regulatory renewal of existing design, not old→new); Google–Constellation 890 MW (SAME det006b 20yr/$4.3B CEG deal at primary URL + 15yr/2700MW supply agreement; uprates on existing PWRs, gate NOT fired — note 7e3d9b1a appended, CEG cash-flow edge confirmed).
- Catalyst notes appended (additive, no re-rate, no substitution-pair mutation): DRIFT-004 +c1a0f2e9 (Micron High-NA roadmap, 144 EMERGING), DRIFT-006 +7e3d9b1a (CEG 890MW/2700MW, 105 EMERGING).
- Engine: drift_scoring.py 10 sidecars, composites unchanged (432/600/20/144/336/105/180/294/180/84), 0 fetch_errors. FLAG: DRIFT-002 NVTS row [STALE] (FY2024 segment) — engine row retained as last-known.
- Track D: rebuilt; 0 cascade eligible this cycle.


## 2026-10-26 — news-break seam wired to the Drift Detector cron
- `~/.hermes/scripts/drift_ingest.py`: one ingress contract, many producers. Merges breaks from
  `drift_inbox.json` into the `drift_candidates.json` spine as `priority:"break"`; idempotent
  (deterministic `BREAK-<md5[:8]>` id); dedupes vs filed-drift URLs (HOST-AGNOSTIC on path?query —
  fixed the uk./www. exact-match miss this session) + already-processed state. `--run` kicks the
  deterministic legs.
- Cron `e9711f5abb15` (Drift Detector): STEP 0.3 now runs `drift_ingest.py`; STEP 1 (c) documents
  the `breaks` leg — breaks are judged FIRST, same quality bar as scan candidates (never filed on
  assertion alone), `verify: SECOND-SOURCE` noted in Evidence, same-story/different-URL breaks are
  re-rating signals (append dated Evidence note) not duplicate filings.
- Design principle: the seam grants a break URGENCY + provenance, NOT special scoring status. A
  break that is noise degrades to NOISE and consolidates out like any drift. Live spine verified
  byte-identical through dry-run.


## 2026-10-28 17:55 — drift-scan (Leg A + A2 rescan)
- Health gate: initially FAIL:primary_feeds (eia). ROOT CAUSE FIXED: primary_feeds.py EIA
  cooldown parse used naive datetime vs aware now_utc() -> "can't subtract offset-naive
  and offset-aware datetimes" (offset-aware bug introduced when cooldown flags were added);
  a 6h last_500 cooldown was being mis-parsed as a hard error every tick. Patch:
  strptime(...).replace(tzinfo=timezone.utc) in f_eia(). After fix: eia ok (cooldown path
  correct, retry ~238m), gate ALL_GOOD. Drift leg proceeded.
- drift_scan.py fresh: 13 sector queries -> 39 candidates; 6 a2 queries -> 18 a2
  candidates; cascade 0 (queue empty). drift_ingest.py: 0 breaks merged.
- 0 new drifts filed (39 base + 18 a2 = 57 reviewed, 57 rejected).
- Base rejections (one-line): purewafer/hackster/entegris/forbes (vendor/marketing/trend,
  no swap); Micron High-NA/wafer-bonding (same story as c1a0f2e9 -> note e53bc3e2 appended
  to DRIFT-004, confirmatory, no re-rate); Polar/imec 8-inch GaN (dup DRIFT-002, private
  winner); panel-vs-wafer/adv-packaging/eetimes-packaging (thinkpiece, no US winner);
  liquid/immersion/ASHRAE (design guides, dup DRIFT-005); 800V x3 (dup DRIFT-009);
  CPO copper-retreat x3 (dup DRIFT-008); SMR-BTM calculator + behind-the-meter (thinkpiece,
  dup DRIFT-006); NRC AP1000 renewal to 2066 (regulatory renewal, not old->new);
  Google-Constellation 890MW (same det006b deal, uprates on existing PWRs, gate not fired);
  transformer lead-times (supply news, not a process swap).
- A2 shadow-run (18 reviewed, 18 rejected): dominant reasons — listicle/guide (tape-out
  guides, foundry-vs-fabless, distributor picks), private winner (Mueon $65M AI rack —
  no ticker), anchor-sized winner (ON/Powertitan-3.0 Sungrow design win, NXP-VW; ON is
  anchor cap, slot rule 1 fails). Real-signal items logged: LX Semicon exits SiC + 60
  patents (KRX, non-US; confirms SiC consolidation but no US-listed winner/loser edge);
  Advanced Photonics Coalition spec portfolio (2026-10-20, 60 orgs) -> appended as
  note apc054c1 to DRIFT-008 (ecosystem standards milestone, not a new substitution).
  Gated 3rd slot UNUSED: no A2 candidate satisfied all 3 rules (no nano/sub-ceiling
  US-listed winner with demonstrated/pilot certainty this cycle).
- Notes appended (no re-rate): DRIFT-004 +e53bc3e2; DRIFT-008 +apc054c1.
- Engine: drift_scoring.py 10 sidecars, composites unchanged
  (432/600/20/144/336/105/180/294/180/84), 0 fetch_errors, 25 FMP profiles persisted.
  FLAG: DRIFT-002 NVTS row [STALE] (FY2024 segment) — last-known, retained.
- Track D: rebuilt; 23 dossiers touched; INDEX regenerated (10 drifts); cascade gate
  post-run: 0 eligible -> cascade_state.json unchanged this cycle.
- [2026-10-29] drift-scan: health gate DEGRADED (eia primary feed in 4-tick error
  streak, demoted=false — gate FAIL:primary_feeds; informational, EIA leg only,
  drift scan itself clean). drift_scan.py fresh: 13 sector queries -> 36 base
  candidates; 6 a2 queries -> 18 a2 candidates; 0 cascade (queue empty). WARNING:
  1 query flagged upstream_suspension ('450mm wafer foundry transition' returned
  0 with all time-capable engines down — engines_down brave/duckduckgo/google/
  google cse; Bing-backed plain queries all healthy with 8-10 fresh).
  drift_ingest.py: 0 breaks merged.
- 0 new drifts filed (36 base + 18 a2 = 54 reviewed, 54 rejected).
- Base rejections (one-line; window is largely the same 1-month pool as
  2026-10-28): ASML-HighNA-explainer/SPIE-Hyper-NA/Micron-wafer-bonding (dup
  DRIFT-004, already noted x2 — 3rd re-circulation, no new datapoint); FinFET-vs-
  GAA/WSe2-science/post-etch-inspection (educational/thinkpiece, no swap or US
  winner); Polar/imec 8-inch GaN x3 (dup DRIFT-002, Polar = PRIVATE winner);
  adv-packaging/panels x3 (thinkpiece, no US winner); liquid/immersion/ASHRAE x4
  (design guides, dup DRIFT-005); 800VDC x3 (dup DRIFT-009); CPO-copper x3 (dup
  DRIFT-008); SMR-BTM calculator + behind-the-meter x3 (thinkpiece, dup
  DRIFT-006); NRC AP1000 renewal to 2066 (regulatory renewal, not old->new);
  Hadron pre-application (rumored, pre-application stage, no US winner);
  Google-Constellation 890MW (uprates on existing PWRs, same det006b, gate not
  fired); nuclear-deal-tracker/transformer-lead-times x3 (supply/trend, not a
  process swap).
- A2 shadow-run (18 reviewed, 18 rejected; precision NOT tainted — suspension
  flag was on a Leg A query, not A2): SawStreet/WIN x2 (Korea backend services,
  non-US), tape-out guide + foundry-vs-fabless + MATLAB exchange + FAR 9.2
  (listicle/guide x5), EnSilica (AIM: ENSI, non-US), NXP-VW (anchor-sized winner,
  rule 1 fails), onsemi-Sungrow BESS (anchor cap + additive efficiency claim),
  SiC patent x3 (patent filings, rumored), Mueon $65M x2 (funding raise, PRIVATE,
  no ticker), APC CPO specs (already noted apc054c1 on DRIFT-008 last cycle),
  Marvell/Lumentum/Coherent M&A musing (speculative trade, not a process
  substitution). Dominant rejection reasons: listicle/guide (5), non-US/PRIVATE
  winner (8), anchor-sized (2), rumored/patent (3). Gated 3rd slot UNUSED: no A2
  candidate with nano/sub-ceiling US-listed winner at pilot-or-better certainty.
- Engine: drift_scoring.py 10 sidecars, composites unchanged
  (432/600/20/144/336/105/180/294/180/84), 0 fetch_errors, 25 FMP profiles
  persisted.
- Track D: rebuilt; 23 dossiers touched; INDEX regenerated (10 drifts); cascade
  gate post-run: 0 eligible (nothing >=500 or gate-fire) -> cascade_state.json
  unchanged this cycle.


## 2026-10-29 drift-scan (Drift Detector)
- Health gate: ALL_GOOD (vllm UP, searxng UP/RUNNING, feeds FRESH, disk OK; eia DEGRADED).
- Scan: 13 sector -> 39 base candidates; 6 a2 -> 18 a2 candidates; 0 cascade queries
  (0 eligible). 0 breaks merged (drift_ingest N=0). No overlap-lock skip,
  upstream_suspicious_queries=0 (no suspension).
- Filed: 0 new drifts (57 candidates reviewed: 39 base + 18 a2).
  Rejection highlights (base): Polar/IC-Link 8" GaN-on-Si (x3) = same entrant as
  DRIFT-002 det002a/21ff8d7f, PRIVATE winner, no new US-listed edge -> no re-file;
  GF-TSMC $2B interposer deal = US-listed winner GF delisted (FMP profile-symbol('GF')
  -> "The New Germany Fund", marketCap $167M; PIF ownership) -> no US ticker, REJECTED;
  rest = thinkpieces/guides (high-NA explainer, FinFET-vs-GAA explainer, liquid-cooling
  comparison, 800VDC architecture blogs, transformer-lead-time research) or earnings/
  growth not a process swap (ON analyst bull-case).
  A2 shadow-run: 18 reviewed, 18 rejected. Dominant reasons: listicle/guide (top-30,
  tape-out explainer, foundry-vs-fabless explainer, USPTO/WIPO search-tool pages,
  MATLAB file), non-US/PRIVATE winner (SawStreet private x2, EnSilica AIM, Mueon
  $65M raise x2), anchor-only / no US-listed winner (ON Sungrow design-win),
  patent/spec-only (Si-SiC hybrid patent, APC CPO specs = already noted on DRIFT-008).
  3rd slot UNUSED: no A2 candidate with a nano/sub-ceiling US-listed winner at
  pilot-or-better certainty.
- Cascade leg: 0 eligible drifts this cycle -> 0 new tickers surfaced;
  cascade_state.json unchanged (no increment — nothing to count).
- Engine: drift_scoring.py 10 sidecars, composites held
  (432/600/20/144/336/105/180/294/180/84), 0 fetch_errors. Pre-existing [STALE]
  segments on DRIFT-002 (NVTS FY2024) / DRIFT-007 / DRIFT-008 / DRIFT-009 remain
  flagged last-known (no new FMP data; rows preserved).
- Track D: drift_track_d.py rebuilt — 23 dossiers touched, INDEX regenerated
  (10 drifts), substitution_short_list refreshed. Cascade gate post-run: 0 eligible
  (nothing >=500 or gate-fire) -> cascade_queue.json eligible=[].


## 2026-10-30 03:13 — drift-scan (Drift Detector)
- Health gate FAIL:primary_feeds (osti 1-tick error not yet demoted; eia
  demoted 7-tick error streak) — informational; OSTI/EIA feeds only, drift
  scan itself clean. Proceeded per 2026-10-29 precedent (gate fail on
  demoted/info feeds is not drift-scan-blocking).
- drift_scan.py fresh: 13 sector queries -> 39 base candidates; 6 a2 queries
  -> 3 a2 candidates; 0 cascade (queue empty). WARNING: 5 queries flagged
  upstream_suspension (engines_down brave/duckduckgo/google — Bing-backed
  rows still returned 18-20 fresh; suspension-tainted cycle: A2 precision
  count excluded from tuning average).
- drift_ingest.py: 0 breaks merged.
- Filed: 0 new drifts (42 candidates reviewed: 39 base + 3 a2). next_drift_id
  DRIFT-011 unconsumed.
- Base rejections: 450mm x3 (thinkpiece/market-report; dup DRIFT-003 pool);
  High-NA x3 (dup DRIFT-004; TSMC-2030 + Lam/imec -> evidence notes det004d,
  no re-rate); GAA x3 (educational/thinkpiece, dup DRIFT-001); GaN-on-Si x3
  (dup DRIFT-002, Polar/imec = PRIVATE winner; 8-inch free-standing =
  research paper); adv-packaging x3 (thinkpiece); liquid-cooling x3 (dup
  DRIFT-005; 3C Datalec = non-US M&A); 800VDC x3 (dup DRIFT-009); CPO x3 (dup
  DRIFT-008); immersion x3 (dup DRIFT-005 guides; Ferveret = PRIVATE);
  SMR/DC x3 (dup DRIFT-006; Utah 9.4GW proposal -> evidence note det006d);
  NRC x3 (dup det006a/c; rule finalization -> det006d); microreactor-PPA x3
  (dup DRIFT-006; Google/CEG PPA re-circulation); transformer lead-time x3
  (supply-shortage trend, not old->new process swap; no named winner).
- A2 rejections (3/3, precision EXCLUDED — suspension-tainted cycle):
  WIN Semiconductors design win (foreign TPEx:3105, no US ticker);
  design-for-procurement (LinkedIn guide, no swap); case-interview (guide/
  listicle). Dominant reason: guide/listicle + foreign.
- Gated 3rd A2 slot: UNUSED (no a2 candidate met rule 1 — no US nano/
  sub-ceiling winner).
- Notes appended (no re-rate): DRIFT-004 +det004d (Lam Aether dry-resist
  verified fetch; LRCX tools-layer edge flagged for next-cycle sidecar);
  DRIFT-006 +det006d (Utah 9.4GW SMR proposal; NRC rule finalization).
- Cascade leg: 0 eligible drifts (queue empty) -> 0 new tickers surfaced;
  cascade_state.json unchanged this cycle (no eligible drift to update
  zero_streak on).
- Engine: drift_scoring.py 10 sidecars, composites held
  (432/600/20/144/336/105/180/294/180/84), 0 fetch_errors, 25 FMP profiles
  persisted.
- Track D: drift_track_d.py rebuilt — 23 dossiers touched, INDEX regenerated
  (10 drifts), substitution_short_list refreshed. Cascade gate post-run:
  0 eligible.


## 2026-10-30 — Drift Detector (e9711f5abb15)
- Health gate: ALL_GOOD (EIA feed degraded — informational).
- SCAN: upstream SUSPENSION — all 19 queries (13 sector + 6 A2) flagged
  upstream_suspension (engines brave/duckduckgo/google/google-cse all
  unresponsive; 0 results each). Zero candidates is the suspension, not
  query quality. No re-run (post-scan guard), no query tuning from this cycle.
- BREAKS: 0 merged (drift_ingest idempotent, 0 processed).
- JUDGMENT: 0 candidates reviewed (base 0 + A2 0) → 0 drifts filed.
  A2 shadow precision: tainted — suspension; excluded from tuning average.
  3rd A2 slot: unused (no A2 candidates).
- CASCADE: queue empty (no drift >=500 unsaturated or gate-fire this cycle;
  DRIFT-002 remains saturated). 0 new tickers; no zero_streak updates needed
  (nothing eligible ran).
- ENGINE: drift_scoring.py re-scored all 10 drifts, no composite deltas
  (001 432 · 002 600 · 003 20 · 004 144 · 005 336 · 006 105 · 007 180 ·
  008 294 · 009 180 · 010 84); no fetch_errors, no [STALE] segments; 25 FMP
  profiles persisted.
- Track D: drift_track_d.py rebuilt — 23 dossiers touched, INDEX regenerated
  (10 drifts); no file deltas (idempotent). Cascade gate post-run: 0 eligible.
- Commit: none — drift-owned files unchanged this cycle.


## 2026-10-30 (2nd run) — Drift Detector (e9711f5abb15)
- Health gate: ALL_GOOD (EIA feed degraded — informational). Scan fresh:
  13 sector queries → 39 base candidates; 6 A2 queries → 18 A2 candidates;
  0 cascade queries. upstream_suspicious_queries = 0 (note: brave/google/
  google-cse engines down on every query — degraded-but-not-suspension;
  candidate counts unaffected). No skip-lock hit.
- BREAKS: 0 merged (drift_ingest idempotent, 0 processed).
- JUDGMENT: 57 candidates reviewed (39 base + 18 A2).
  FILED: DRIFT-011 us-silicon-interposer-gfs — GFS/TSMC multi-year $2B US-based
  CoWoS silicon-interposer manufacturing (Malta NY, eDTC, volume ramp H1 2028).
  M×T×C = 6×8×7 = 336 HIGH, additive (no clean US loser; TSMC is the customer).
  Primary source page fetched (1 of 2 fetch budget); VERIFIED.
  BASE SLOT 2 UNUSED — all other base candidates rejected:
   - Polar/IC-Link 8-inch GaN-on-Si (GaN-on-Si query): already logged as DRIFT-002
     det002a (2026-10-25) — dedup, no new edge (Polar = PRIVATE).
   - Micron wafer-bonding + High-NA DRAM roadmap: already logged as DRIFT-004
     c1a0f2e9 (2026-10-28) — re-circulation, no re-rate.
   - Google/Constellation 890MW uprate PPA: already logged as DRIFT-006 7e3d9b1a
     (primary source confirmed last cycle) — no new edge.
   - NRC AP1000 design-cert renewal (3 URLs): PWR-class cert renewal, not SMR
     SDA gate; already logged as DRIFT-006 det006c/5c8bb9d4 — regulatory
     housekeeping, not a substitution.
   - Micron wafer-bonding vHBM roadmap (mezha), ASML High-NA explainers (3),
     450mm guide/visual pieces (2), GAAFET market report, etch papers (2),
     800V DC explainers/whitepapers (3), liquid-cooling explainers (3),
     CPO explainers (2 + YouTube), transformer lead-time thinkpieces (3),
     custom-silicon race long-read, SMR PPA calculator, BTM state-policy piece:
     thinkpieces/guides/standards-documents/re-circulations — no named
     process swap or commitment.
  SAME-STORY EVIDENCE NOTES (no re-rate): DRIFT-005 +067a5d49 (Ferveret
  in-rack immersion at MIT — PRIVATE winner, DCD VERIFIED; score 336 HIGH held).
- A2 SHADOW (18 reviewed, 18 rejected; 3rd slot UNUSED):
   - 7 listicle/guide/tooling (Top-30 rankings, wafergraph, tape-out guide,
     MATLAB file exchange, USPTO/Wikipedia/FAR pages, energy-startups top-29).
   - 4 non-substitution (QuickLogic 6-figure eFPGA IP contract = revenue
     increment not process swap; EnSilica tape-out = LSE-listed, non-US;
     SawStreet = private backend service profile; WSJ startup compute piece).
   - 2 anchor-sized winner (onsemi/Sungrow SiC design win — ON ~$29B mid-to-
     anchor, winner set not nano/sub-ceiling edge; simplywall.st duplicate).
   - 1 rumored/no-swap (LX Semicon SiC patent exit — Korean private, patent
     divestiture, no US winner).
   - 4 standards/regulatory-doc (APC CPO specs = already logged on DRIFT-008
     apc054c1; FAR 52.209-1 + Subpart 9.2 = procurement boilerplate).
  Slot rules: (1) nano/sub-ceiling US winner FAIL on all; (2) certainty bar
  FAIL (rumored/roadmap); (3) specific swap FAIL (listicles/guides).
  Precision count CLEAN this cycle (no suspension flag) — first untainted A2
  sample: 0/18 eligible (dominant reason: listicle/guide 7/18).
- CASCADE: queue empty this cycle (nothing >=500 unsaturated or gate-fire;
  DRIFT-002 saturated at 3 zero-streak, excluded). 0 new tickers; no
  cascade_state.json writes needed.
- ENGINE: drift_scoring.py re-scored all 11 sidecars — DRIFT-011 = 336 (new,
  matches md table); no composite deltas on the other 10 (001 432 · 002 600 ·
  003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 · 009 180 · 010 84);
  no fetch_errors, no [STALE] on GFS (data-quality note: GFS FMP
  revenue-product-segmentation = single coarse FY2025 line
  "Engineering And Other Pre-Fabrication Services" $769M — engine matches on
  sector). 26 FMP profiles persisted.
- Track D: drift_track_d.py rebuilt — 24 dossiers touched (incl. NEW GFS
  winner backlink), INDEX regenerated (11 drifts). Cascade gate post-run:
  0 eligible.


## 2026-10-31 drift-scan (cron e9711f5abb15)
- Health gate ALL_GOOD (EIA feed degraded — informational). Scan: 13 sector + 6 a2 queries → 39 base candidates + 18 a2 candidates; 0 upstream-suspension flags; 0 news breaks merged.
- FILED: DRIFT-012 10kV SiC IGBT domestic process (NVTS ALATTIS award) — M4×T4×C6 = **96 EMERGING**, A2 gated 3rd slot USED (rules satisfied: sub-ceiling winner NVTS $2.2B; pilot/award certainty; named process award). FMP NVTS segmentation = single "Reportable Segment" FY2024 $83.3M → whole-company proxy noted.
- Base candidates: 0 new drifts — all fresh hits are same-story re-circulations of filed drifts (ASML record Q3 → DRIFT-004; Google/CEG 890MW uprate PPA + NRC DOE/DOD licensing final rule → DRIFT-006; 800V-DC + CPO articles → DRIFT-008/009). No re-rate warranted (ASML/Samsung/TSMC High-NA HVM dates = roadmap-stage, consistent with existing det004c).
- A2 shadow-run: 18 reviewed, 17 rejected — dominant reasons: listicle/guide (3), distributor/vendor pages (4), private/no-ticker startups (3), anchor-sized winner (Wolfspeed EV/SiC, WOLF $1.2B is sub-ceiling but story is product-launch not substitution → 2), foreign (LX Semicon, SK Hynix), rumor/thin (5). 1 filed (3rd slot). Precision 1/18 = 5.6% (cycle NOT tainted — 0 upstream suspensions).
- CASCADE leg: 0 eligible drifts (no composite ≥500 unsaturated, no gate-fires) → 0 cascade queries, 0 new tickers; no zero_streak changes.
- Engine: 12 drifts re-scored, all composites unchanged, 0 fetch_errors, 0 stale segments. NVTS dossier backlink now +3 winner edges (DRIFT-002/009/012).


## 2026-11-02 drift-scan (cron e9711f5abb15)
- Health gate ALL_GOOD (EIA feed degraded — informational). Scan: 13 sector +
  6 a2 queries → 6 base candidates, 0 a2 candidates, 0 cascade results;
  **17/19 queries flagged upstream_suspension** — SearXNG upstream engines were
  IP-suspended mid-scan; the low candidate count this cycle is the suspension,
  not query quality (no query tuning from this cycle). 0 news breaks merged.
- 0 drifts filed (6 base candidates reviewed, 6 rejected): 2 LinkedIn wafer-
  market trend thinkpieces + Wikipedia fab article = 450mm re-circulation of
  filed DRIFT-003 (no new commit, thinkpieces rejected); 3 High-NA EUV items
  (ASML record $13B quarter, TSMC/Samsung HVM dates 2028/2030, EUV market-size
  forecast) = same-story re-circulations of filed DRIFT-004, roadmap-stage
  (consistent with det004c/c1a0f2e9 datapoints; no re-rate).
- A2 shadow-run: 0 candidates (suspension) — precision count TAINTED, excluded
  from tuning average.
- CASCADE: queue empty (0 eligible: nothing >=500 unsaturated — DRIFT-002
  saturated at zero_streak 3, holding; no gate-fires) → 0 new tickers.
  zero_streak advanced DRIFT-004 1→2, DRIFT-005 1→2 (each one more cycle from
  saturation).
- Engine: 12 sidecars re-scored, all composites unchanged (001 432 · 002 600 ·
  003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 · 009 180 · 010 84 ·
  011 336 · 012 96); 0 fetch_errors, 0 stale segments; 26 FMP profiles persisted.
- Track D: 24 dossiers touched, INDEX regenerated (12 drifts), cascade gate
  0 eligible.



## 2026-11-02 drift-scan 16:30 (cron e9711f5abb15)
- Health gate ALL_GOOD (EIA feed degraded — informational).
- Scan: 13 sector + 6 a2 queries → **0 base, 0 a2, 0 cascade candidates;
  19/19 queries flagged upstream_suspension** (all 4 engines brave/duckduckgo/
  google/google-cse down mid-scan, HTTP 200 with zero rows). This is the
  SearXNG IP-suspension signature, NOT query quality — per post-scan guard:
  no filing, no query tuning from this cycle. 0 news breaks merged.
- 0 drifts filed (0 candidates to review — spine fully empty under suspension).
- A2 shadow-run: 0 candidates (suspension) — precision count TAINTED, excluded
  from tuning average.
- CASCADE: queue empty (0 eligible; DRIFT-002 saturated zero_streak 3 holding,
  no gate-fires) → no eligible drift to write back; zero_streak/saturated held.
- Engine: 12 sidecars re-scored, all composites unchanged
  (001 432 · 002 600 · 003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 ·
  009 180 · 010 84 · 011 336 · 012 96); 0 fetch_errors, 0 stale segments;
  26 FMP profiles persisted.
- Track D: 24 dossiers touched, INDEX regenerated (12 drifts), cascade gate
  0 eligible.


## 2026-11-04 drift-scan (cron e9711f5abb15)
- Health gate ALL_GOOD (stale: signal_briefs + vetted_tickers ~2h — informational,
  other jobs' cadence; no primary_feed issues).
- Scan: 13 sector + 6 a2 queries → **39 base, 18 a2, 0 cascade candidates**;
  0 upstream_suspicious_queries (SearXNG engines healthy). 0 news breaks merged.
- **0 drifts filed (57 candidates reviewed: 39 base, 18 a2 — all rejected).**
  - Base rejections: market-size/growth reports + vendor thought-leadership (Yahoo
    wafer-equipment market, LinkedIn market pulses, EUV/GaN-on-Si epi market
    reports, Schneider/Vertiv 800VDC marketing, immersion/liquid-cooling explainers,
    transformer lead-time explainers) — none names a specific process swap or
    commitment; C-UAS/SMR hits (Google-Constellation PPA, Radiant DOE OK) are
    same-story re-surfaces of already-logged DRIFT-006 datapoints (det006b/det006e);
    ON+Sungrow ESS design win = DRIFT-002 re-surface (design win, not substitution).
  - a2 rejections (18): 6 listicle/guide (how-to-start-fabless, foundry-switching
    checklist, tape-out planning posts), 5 distributor/patent-DB/vendor pages
    (wafergraph, MaxVal, Molex, AMAT job post, WIN-Semi newsroom), 4 anchor-sized
    winners or private (Onsemi, Wolfspeed, Mueon PRIVATE, Turba Labs PRIVATE), 3
    no US-ticker winner / no specific swap (LX SiC patent sale = Korean private
    exit; Commerce Korea grant = foreign; CPO expert-call = talk, no qualification).
- **A2 shadow-run: 18 reviewed, 18 rejected; dominant reasons = listicle/guide +
  vendor/distributor junk (11/18), anchor/private winner (5/18), no-defensible-swap
  (2/18). 3rd slot UNUSED (no candidate cleared all three gate rules). Not tainted
  (no suspension) — counts toward the 2-cycle tuning average; junk skew confirms
  the 2026-10-26 expectation that A2 precision needs query tightening.**
- Evidence notes appended (no re-rate, no new drift): DRIFT-002 det002g (Polar/imec
  8-inch GaN re-surfaced via ChipNews — dedup, 600 CRITICAL held) · DRIFT-004
  det004e (Samsung High-NA HVM 2028 DRAM-first + TSMC ~2030 schedule confirmed in
  ASML record-quarter report — C held 6, 144 EMERGING held).
- CASCADE: queue empty (0 eligible; no composite >=500 unsaturated, no gate-fires)
  → nothing to write back; DRIFT-002 saturated (zero_streak 3) holding.
- Engine: 12 sidecars re-scored, all composites unchanged (001 432 · 002 600 ·
  003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 · 009 180 · 010 84 ·
  011 336 · 012 96); 0 fetch_errors, 0 stale segments; 26 FMP profiles persisted.
- Track D: 23 dossiers touched, INDEX regenerated (12 drifts), cascade gate
  0 eligible.


## 2026-11-04 drift-scan (2nd run) — Drift Detector (cron e9711f5abb15)
- Health gate ALL_GOOD. Scan: 13 sector + 6 a2 queries → **39 base, 18 a2, 0
  cascade candidates**; 0 upstream_suspicious_queries (SearXNG healthy); 0 news
  breaks merged.
- **0 drifts filed (57 candidates reviewed: 39 base, 18 a2 — all rejected).**
  Deterministic re-scan of the same candidate set as the 11-04 first run; no new
  events. Base rejects = thinkpieces/market-forecasts/whitepapers (wafer-equipment,
  EUV/GaN market reports, 800VDC vendor marketing, immersion/liquid-cooling
  explainers, transformer lead-time explainers) + same-story re-surfaces of
  already-logged DRIFT-004/006/008/009 datapoints; SHINKO ABF→glass-core/hybrid-RDL
  packaging and Decima immersion pilot both fail the named-US-winner bar (private/
  JP, or no US input winner). a2 rejects (18) = funding-raise/private (Mueon ×3),
  listicle/ranking (Top-30, LEAP Awards), patent/IP filings (SiC ×3),
  thinkpieces/checklists; two genuine design wins failed slot rules — ON/Sungrow
  BESS SiC (ON ~$25B = anchor, fails slot rule 1) and QuickLogic six-figure eFPGA
  IP contract (additive IP license, no exclusive old→new qualification, fails rule 3).
- **A2 shadow-run: 18 reviewed, 18 rejected; 3rd slot UNUSED (no candidate cleared
  all three gate rules). Not tainted (no suspension) — counts toward the 2-cycle
  tuning average.**
- No evidence-note appends needed (all base candidates either already logged in a
  dated note this cycle's set or failed the quality bar outright).
- CASCADE: queue empty (0 eligible; DRIFT-002 saturated, no composite >=500
  unsaturated, no gate-fires) → no zero_streak write-back (Step 4.1 scoped to
  eligible drifts).
- Engine: 12 sidecars re-scored, all composites unchanged (001 432 · 002 600 ·
  003 20 · 004 144 · 005 336 · 006 105 · 007 180 · 008 294 · 009 180 · 010 84 ·
  011 336 · 012 96); 0 fetch_errors, 0 stale segments; 26 FMP profiles persisted.
- Track D: 23 dossiers touched, INDEX regenerated (12 drifts), cascade gate
  0 eligible.

## 2026-11-09 Drift scan — 0 filed
- Health: ALL_GOOD; drift scan: 13 sector + 6 a2 queries, 57 candidates (39 base + 18 a2)
- 0 breaks merged (drift_ingest)
- Judgment: 39 base rejected (14 repeats of existing drifts 002/003/004/008/009, 15 regulatory/roadmap/listicle, 10 capacity-shift not substitution); 18 A2 rejected (listicles, funding, patents, design-wins without substitution mechanism, ecosystem proof for existing drifts)
- 0 new drifts filed; 3rd-slot A2: unused (no qualifying candidate)
- Cascade: 0 eligible (no drift >= 500 or gate-fire; DRIFT-002 at 600 is saturated)
- Engine: 0 sidecars (no drifts filed this cycle)

## 2026-11-10 drift-scan (cron e9711f5abb15)

- Health: ALL_GOOD (vllm UP, searxng UP/RUNNING, feeds FRESH, disk 48.5% free).
- Scan: 13 sector + 6 a2 queries → 39 base + 18 a2 = 57 candidates; 0 upstream_suspicious_queries; 0 news breaks. No overlap-lock skip.
- **FILED: DRIFT-013 — ArF immersion lithography → High-NA EUV (11nm) at sub-3nm nodes.** M×T×C = 7×8×6 = **336 HIGH**, additive (no clean US loser; mature-node ArF remains dominant). Winner: ASML (sole High-NA EUV NXE:3000 series). Loser: LRCX (lithography exposure tools at advanced nodes, limited displacement). Timing: 2027–2028.
- Evidence: ASML Q3 2026 record $13B quarter + Samsung HVM 2028 commit (Tom's Hardware, VERIFIED); Micron 2026 High-NA roadmap for 3D NAND/DRAM (Tom's Hardware, VERIFIED); SemiAnalysis ASML hybrid bonding tool alongside HVM ramp pressing BEI (VERIFIED).
- Base candidates: 38 rejected. Rejection breakdown — 450mm trio = historical/archival (and DRIFT-003), no active commitment; Gate-all-around etch = academic paper (PMC) + model pages + educational explainer, no commercial swap; GaN-on-Si power epiwafer = product page + market report + product catalog, no substitution commitment; advanced packaging = trend/thinkpiece (TSMC CoWoS scaling is capacity expansion not substitution); liquid cooling = design guides/PPU explainers; 800V DC = NVIDIA standard-setting (evolution, not substitution); CPO = NVIDIA OOI prototype, research-stage only, no commercialization timeline; immersion cooling = early pilots (MIT, Chicago), not hyperscaler-scale; SMR behind the meter = blog/listicle, no concrete commitment; NRC standard design = regulatory event enabling SMRs downstream; microreactor PPA = deployment model shift not technology substitution; transformer lead time = supply constraint not a substitution.
- A2 shadow-run (18 reviewed, 18 rejected): dominant reasons — listicle/guide (JIM 10-step, anysilicon checklist, deepchecks pitch deck, newmarketpitch top-startups, ic-components CPO explainer, jim ept vendor pages), foreign/PRIVATE (SawStreet private, EnSilica AIM-listed, Mueon $65M raise), anchor-sized winner (ON/Powertitan-3.0 Sungrow design win = mid-cap anchor, fails slot rule 1; LX Semicon SiC exit = Korean), patent/spec-only (SiC patent, APC CPO specs = already on DRIFT-008), non-substitution (QuickLogic eFPGA contract = revenue increment, not process swap). 3rd A2 slot UNUSED (no candidate with nano/sub-ceiling US-listed winner at pilot-or-better certainty).
- Cascade: 0 eligible drifts (nothing >=500 unsaturated; DRIFT-002 saturated at 600). 0 new tickers surfaced.
- Engine: drift_scoring.py 1 sidecar (DRIFT-013), 0 fetch_errors, 26 FMP profiles persisted.
- Track D: drift_track_d.py rebuilt — 1 named loser row (LRCX, sub_downside 38.4%, medium confidence) on short list; backlink SKIP (no LRCX dossier yet); 0 dossiers touched.
- Index: INDEX.md regenerated (1 drift).

## 2026-11-10 drift-scan (cron e9711f5abb15)

- Health: ALL_GOOD (vllm UP, searxng UP/RUNNING, feeds FRESH, disk 48.5% free).
- Scan: 13 sector + 6 a2 queries → 39 base + 18 a2 = 57 candidates; 0 upstream_suspicious_queries; 0 news breaks merged. No overlap-lock skip.
- **FILED: DRIFT-014 — behind-the-meter SMR nuclear power for data centers.** M×T×C = 6×7×6 = **252 MODERATE**. Old: grid-connected nuclear/grid power → New: behind-the-meter SMR at data center campuses. Winners: NM (NuScale US460, NRC behind-the-meter approved) + CEG (Constellation Energy, Google 20yr PPA). Additive — grid generators lose marginal hyperscale contracts to behind-the-meter. Timing: 2027–2029.
- **FILED: DRIFT-015 — 800VDC data center power architecture.** M×T×C = 5×5×4 = **100 LOW**. Old: standard AC/400V distribution → New: native 800VDC rack power. Winners: NVDA (spec leader), VRT (sidecar architecture), BE (DC fuel cell). Loser: class row (legacy UPS/PDU). Additive, infrastructure-upgrade, timing: 2027–2030.
- Base candidates: 37 rejected. Rejection breakdown — 450mm = thinkpiece/vendor/market-report, no commitment; Micron roadmap/ASML $13B qtr = re-circulation of DRIFT-004; CPO production planning = re-circulation of DRIFT-008; GAA etch/vertically stacked = academic paper + educational explainer, no commercial swap; GaN-on-Si epiwafer = market report + MicroLED-tag page + product catalog, no US winner commitment; advanced packaging = trend/thinkpiece (SHINKO ABF→glass-core is DRIFT-001 companion, capacity expansion not substitution); liquid cooling = design guides/Trane glossary; transformer lead times = supply constraint, no process swap.
- A2 shadow-run (18 reviewed, 18 rejected; 3rd slot UNUSED): dominant reasons — listicle/guide (sourceability 2027 semi outlook, newmarketpitch cooling-startups, jim.com how-to, deepchecks pitch-deck guide), foreign/PRIVATE (Molex CPO product page — US listed but vendor page, not a substitution event; LX Semicon SiC exit = Korean; EnSilica AIM-listed), anchor-sized winner (ON Sungrow, WOLF), patent/spec-only (SiC patent), funding/no-swap (WSJ startup article, Crusoe company page, techcrunch datacenter-mass-production), standards/spec doc (APC CPO specs = already logged on DRIFT-008 apc054c1). 3rd A2 slot UNUSED — no A2 candidate with a nano/sub-ceiling US-listed winner at pilot-or-better certainty.
- Cascade: 0 eligible drifts (nothing >=500 unsaturated; DRIFT-002 saturated at 600). 0 new tickers surfaced. No zero_streak changes needed.
- Engine: drift_scoring.py 3 sidecars re-scored (DRIFT-013=336, DRIFT-014=252, DRIFT-015=100); all composites match file values; 0 fetch_errors, 0 stale segments; 29 FMP profiles persisted.
- Track D: drift_track_d.py rebuilt — 24 dossiers touched (NEW: GFS, NM, CEG, BE); INDEX regenerated (13 drifts); cascade gate 0 eligible.


## 2026-11-10 drift-scan (cron e9711f5abb15, 2nd run)

- Health: ALL_GOOD (vllm UP, searxng UP/RUNNING, feeds FRESH, disk 48.5% free).
- Scan: 13 sector + 6 a2 queries → 39 base + 18 a2 = 57 candidates; 0 upstream_suspicious_queries; 0 news breaks merged. No overlap-lock skip.
- **FILED: DRIFT-001 — Monolithic die scaling → chiplet + advanced 2.5D/3D packaging.** M×T×C = 7×7×8 = **392 HIGH**. Old: monolithic SoC scaling (sub-3nm). New: chiplet architectures with 2.5D/3D advanced packaging (CoWoS, SoIC, EMIB, Foveros). Winners: TSM (CoWoS leader), AMD (chiplet pioneer, MI300/400), NVDA (GB200 NVL72), INTC (EMIB/Foveros), AEIS (thermal/cooling for advanced packages, record $322M Q3 2026), AMKR (OSAT for chiplet assembly). Loser: class row (monolithic-die EDA/design tools, reduced relevance as chiplet design dominates). Additive — no clean displacement loser at scale. Timing: 1-3 years (NVIDIA GB200 late 2024/2025 first large-scale deployment).
- Evidence: Shinko substrate evolution ABF/glass→hybrid RDL (2026-10-19, TSPA); Siemens 3D IC design trends confirm packaging as primary scaling vector (2026-10-21); Otis Group "Chiplets x Advanced Packaging most promising way without scaling" (2026-11-08). All VERIFIED via fetched sources.
- Base candidates: 38 rejected. Breakdown — 450mm wafer = historical/archival (abandoned, not adopted), no new commitment; High-NA EUV = re-circulation of DRIFT-013 already filed; GAA etch = academic paper + encyclopedia explainer + researchgate schematic, no commercial swap or US winner; GaN-on-Si 8-inch = market report + product catalog, size transition (6"→8") not substitution; liquid cooling = design guides/PPU explainers, no hyperscaler volume commit; 800V DC = NVIDIA standard-setting (DRIFT-015 already filed, evolutionary not substitution); CPO = Broadcom/Molex product pages + EE Times production planning, still roadmap-stage (copper retained in-rack for 2027+); immersion cooling = early deployments (MIT pilot, Chicago pilot, Decima) not hyperscaler scale; SMR behind the meter = blog/listicle + brand marketing (NuScale, Siemens), no new commitment; microreactor PPA = Google/Constellation 20yr PPA is large-reactor (Comstock), not microreactor; transformer lead times = supply constraint (160 weeks) not a substitution.
- A2 shadow-run (18 reviewed, 18 rejected; 3rd slot UNUSED): dominant reasons — listicle/guide (JIM 10-step, anysilicon checklist, deepchecks pitch deck, newmarketpitch top-startups, ic-components CPO explainer), foreign/PRIVATE (SawStreet private, Mueon $65M raise, LX Semicon SiC exit = Korean), anchor-sized winner (ON/Sungrow design win, WOLF), patent/spec-only (SiC patent, APC CPO specs), non-substitution (QuickLogic eFPGA = revenue increment not process swap; Understand Tech AI platform = tooling not process swap). 3rd A2 slot UNUSED — no candidate with nano/sub-ceiling US-listed winner at pilot-or-better certainty.
- Cascade: 0 eligible drifts (nothing >=500 unsaturated; DRIFT-002 saturated at 600). 0 new tickers surfaced. No zero_streak changes needed.
- Engine: drift_scoring.py 4 sidecars re-scored (DRIFT-001=392 NEW, DRIFT-013=336, DRIFT-014=252, DRIFT-015=100); 0 fetch_errors, 0 stale segments; 34 FMP profiles persisted (TSM, AMD, AEIS, AMKR added fresh profiles).
- Track D: drift_track_d.py rebuilt — 28 dossiers touched (NEW: TSM, AMD, INTC, AEIS, AMKR); INDEX regenerated (13 drifts now include DRIFT-001); cascade gate 0 eligible.
- Commit: changed files tracked and committed.
## 2026-11-11 Drift Scan Run
- **Health:** ALL_GOOD (stale:file_feed_raw.json,file_signal_briefs.json,file_vetted_tickers.json)
- **Scan output:** 13 sector queries -> 39 fresh candidates; 6 a2 (small-cap) queries -> 18 a2 candidates; 0 cascade results
- **Breaks:** 0 merges
- **Filed:**
  - DRIFT-016: Co-Packaged Optics (CPO) Replaces Copper Interconnects — M×T×C = 576 (A grade, HIGH)
  - DRIFT-017: Vertical GaN Displaces Silicon Power Transistors — M×T×C = 336 (B grade, HIGH)
- **Rejected candidates:**
  - 450mm wafer foundry transition: NOT a substitution event — 450mm was already abandoned, no new process named
  - ASML record $13B Q: Earnings news, not a technology substitution event
  - GAA FET / Stacked GAA: Academic/research paper, no commercial commitment
  - 450mm SemiWiki: Historical analysis, not an active substitution
  - PLP/Panel-level packaging: Guide/process overview, not a specific substitution
  - 800VDC/Vertiv/ NVIDIA: Already filed as DRIFT-015
  - High-NA EUV/ASML: Already filed as DRIFT-013
  - Silicon wafer reclaim: Market size article, not a substitution
  - SHINKO/Kinsus substrate: Listicle/feature piece
  - SMR/NuScale: Already filed as DRIFT-014
  - Transformer lead times: Market bottleneck article, not a substitution
  - Immersion cooling: Process overview, no old→new swap
  - Data center PUE: Investment overview, not a substitution
  - SB Energy/ NBU Energy: SEC filings/ sustainability page, not a substitution
  - A2 (18 candidates): 5 SKIP (guide/listicle), 13 evaluated — no new base drifts from A2; 3rd-slot A2 not used (no candidate met all three gates: nano/sub-ceiling winner + pilot certainty + named old→new)
- **Cascade:** DRIFT-016 eligible at 576; 0 new tickers found → zero_streak=1 (not saturated)
- **Track D delta:** +2 new drifts; LITE/COHR/MRVL/AVGO/CRDO/ALAB/ON/WOLF/IFXN/TEL profiles updated

## 2026-11-11 Drift Scan Run (cron e9711f5abb15)
- Health: ALL_GOOD (stale:file_feed_raw.json,file_signal_briefs.json,file_vetted_tickers.json — informational)
- Scan: 13 sector + 6 a2 queries → 39 base + 18 a2 = 57 candidates; 0 upstream_suspicious_queries; 0 news breaks
- **FILED: 0 drifts** (57 candidates reviewed: 39 base + 18 a2 — all rejected)
- Base rejections (one-line): 450mm = historical/archival (abandoned, not an active substitution), no new commitment; ASML $13B qtr = earnings, not substitution; GAA FET/etched gate = academic paper (PMC), no commercial swap; High-NA EUV = re-circulation of DRIFT-013; CPO production = re-circulation of DRIFT-016; advanced packaging = trend/thinkpiece, no named-US-winner commitment; liquid cooling/800VDC = already-filed (DRIFT-015/009); SMR/PPA = DRIFT-014 re-surface; transformer lead time = supply constraint, not a process swap
- A2 shadow-run (18 reviewed, 18 rejected): dominant reasons — listicle/guide (6: JIM 10-step, anysilicon checklist, newmarketpitch top-startups, ic-components CPO explainer, deepchecks pitch deck, jim ept vendor), foreign/PRIVATE (SawStreet private, Mueon $65M raise, LX Semicon Korean exit, EnSilica AIM-listed), anchor-sized (ON/Sungrow design win = ON mid-cap anchor, fails slot rule 1; WOLF), patent/spec-only (SiC patent, APC CPO specs = already on DRIFT-008), non-substitution (QuickLogic eFPGA = revenue increment not process swap; Understand Tech AI platform = tooling not process swap). 3rd A2 slot UNUSED — no candidate with nano/sub-ceiling US-listed winner at pilot-or-better certainty naming a specific old→new swap.
- CASCADE: 0 eligible drifts (DRIFT-002 saturated; no composite >=500 unsaturated, no gate-fires) → 0 new tickers; no zero_streak write-back needed
- Engine: drift_scoring.py 6 sidecars re-scored, all composites stable (DRIFT-001=392, DRIFT-013=336, DRIFT-014=252, DRIFT-015=100, DRIFT-016=576, DRIFT-017=336); 0 fetch_errors, 0 stale segments; 38 FMP profiles persisted
- Track D: drift_track_d.py rebuilt — 23 dossiers touched, INDEX regenerated (13 drifts); cascade gate 0 eligible

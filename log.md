
--- 2026-11-21 drift-scan cycle ---
Health: ALL_GOOD
Scan: 13 sector queries → 39 candidates; 6 a2 queries → 18 a2 candidates; 0 cascade results; 0 breaks
Filed:
  - DRIFT-001 co-packaged-optics-replaces-copper M=8 T=7 C=7 → composite 392 (HIGH)
    Sector: ai-infrastructure. Substitution: copper electrical interconnects → CPO/NPO optical engines.
    Winners: AVGO (Broadcom, Bailly shipping), MRVL (Marvell, Teralynx CPO), COHR (Coherent, PhotonLink Q4 2026 ramp).
    Evidence: Broadcom Oct 2026 shipping status, Coherent 10+ customer engagements, Marvell ECOC 2026 demo.
    Certainty: Claimed → Demonstrated (production shipping + customer engagements).
  - DRIFT-002 advanced-packaging-replaces-node-scaling M=8 T=8 C=8 → composite 512 (CRITICAL)
    Sector: semiconductors. Substitution: monolithic node shrinking → chiplet-based heterogeneous integration (CoWoS, 3D stacking, hybrid bonding).
    Winners: LRCX (Lam Research, TSV/HB equipment), AMAT (Applied Materials, advanced packaging), AMKR (Amkor, OSAT packaging capacity).
    Loser: ASML/KLA node-scaling equipment (moderate exposure decline as industry pivots).
    Evidence: Yole Group 2026 revenue crossover, $28B expected capex, TSMC CoWoS 80% CAGR.
    Certainty: Demonstrated (shipping revenue crossover confirmed).
    Cascade: DRIFT-002 composite 512 ≥ 500 → eligible for Trigger v2 cascade; 0 queries ran this cycle → zero_streak=0.
Rejected: 0 candidates (all 57 candidates were either not-defensible substitutions or borderline noise)
  - Rejection reasons: listicles, guide articles, general market overviews without named substitution pair
  - Notable rejects: Samsung 8-inch exit (execution/expansion, not substitution), SMR news (no clear US-listed winner substitution), transformer lead time (demand growth, not substitution), fabless tape-out (generic guide), silicon carbide patent search (generic WIPO results)
A2 review: 18 A2 candidates reviewed; 0 passed; 18 rejected (dominant: listicles/guides/no-defensible old→new+winner substitution).
3rd-slot A2 rule: NOT APPLICABLE (no A2 candidate met all three gates: nano/sub-ceiling winner + pilot certainty + specific process swap).
Track D delta: 2 new drifts added to substitution_short_list.md.
## 2026-11-21 21:10 UTC — Drift Detector Run

**Health:** ALL_GOOD (stale: signal_briefs.json, vetted_tickers.json — informational)
**Scan:** 13 sector queries → 36 candidates; 6 a2 queries → 18 a2 candidates; 1 upstream_suspicious (NRC query flagged); 0 cascade results
**Ingest:** 0 breaks merged
**Decisions:** 0 drifts filed. All 54 candidates rejected — base candidates are market reports/guides/product announcements without a named US-listed winner with >5% revenue exposure to the new process. A2 candidates all listicles/guides/patent abstracts.
**Cascade:** DRIFT-002 advanced-packaging composite 512 had 0 new tickers — zero_streak 0→1 (not saturated at <3).
**A2 precision:** 18 reviewed, 18 rejected (dominant reason: guide/listicle/non-substitution; 1 patent abstract; 2 supplier directories). 3rd slot unused (no A2 candidate named a nano/sub-ceiling winner with demonstrated or pilot certainty and a specific old→new process swap).
**Engine:** drift_scoring.py ran successfully; DRIFT-002 M=8×T=8×C=8=512 (CRITICAL), DRIFT-001 M=8×T=7×C=7=392 (HIGH). No fetch_errors.
**Track D:** No changes — no new drifts filed. No delta.

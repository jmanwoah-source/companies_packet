# Drift Schema Validation — Nuclear / Advanced Energy Pillar

**Date:** 2026-10-25 · **Method:** salvage (sub-agent timed out at 600s after search; dossier written inline from salvaged transcript evidence)
**Inputs read:** `drifts/SCHEMA.md`, `drifts/DRIFT-003_300mm-to-450mm.md`, `sectors/advanced-energy-grid.md`

## Verdict

**PASS (with 2 blocking fixes).** The schema generalizes, but this pillar is the hardest
stress test for the Timing and Certainty axes: SMR licensing is a **decade-long binary
regulatory gate**, and the current rubric compresses both "7-10 yrs out" and "10 yrs out
but gate just opened" into the same low scores. The salvage evidence is exactly the
failure case: **OKLO's NRC Principal Design Criteria Topical Report was approved (2026)**
— a milestone that should lift the *certainty* of the SMR drift NOW, while *timing* stays
long. The current schema has no field that says "long-timing but gate-opening event this
cycle."

## Schema gaps found

1. **Timing axis has no "gate" sub-state.** A drift gated by a binary regulatory event
   (NRC standard design approval) has a *discontinuous* timing distribution: nothing
   changes for years, then the gate flips and 5 yrs become 3. Fix: add a `timing-gate`
   field (e.g. `NRC-SDA`) + rule: when the gate fires, re-rate Timing on the post-gate
   clock and log a dated note. Without this, the decade-out SMR drift permanently
   under-scores even as its licensing evidence accrues.
2. **Certainty conflates "the tech is demonstrated" with "the license is granted."** For
   nuclear, TRL 8-9 (a prototype works) is worth less than a 50%-approved licensing
   dossier. Fix: in this pillar, Certainty = min(tech-TRL score, licensing-progress
   score), where licensing-progress maps: topical-report approved → +2, combined-license
   50% → +4, SDA granted → full. The OKLO topical-report approval is the first real test
   case.
3. **Winner-side is the *developer* tier (nano-cap, binary) while the cash flows accrue to
   the operator tier (CEG/VST/TLN, large-cap).** The schema's single winner table doesn't
   distinguish the *optionality* winner (OKLO) from the *cash-flow* winner (CEG). Fix:
   allow a `winner-role` column (optionality | cash-flow | moat-owner) so one drift can
   score the nano optionality edge and the operator edge separately.

## Sample drift (NOT in index)

**Suggestion: DRIFT-006 — Large-PWR fleet-only base load → SMR/microreactor data-center
power (architecture-substitution, nuclear)**

- **Substitution.** Centralized large-PWR grid base load (20-40 yr PPA model, multi-year
  interconnect queues) → on-site / behind-the-meter SMR + microreactor generation for
  AI campuses.
- **Layer:** reactor tech/SMR (developers), operators/DC power (operators), DC customers downstream.
- **Magnitude (7).** Data-center nuclear is a new multi-GW demand category; the
  interconnect-queue constraint (the sector dossier's binding constraint) is what the
  substitution removes. At-stake: CEG/TLN/VST PPA models + the entire SMR developer tier
  (OKLO, NUS, BWXT, HTZ).
- **Timing (3).** 3-5 yrs to first DC-serving SMR delivery; TRL 6-7 for Aurora-class
  (Idaho deployment track). Pre-gate clock.
- **Certainty (5).** Claimed tier: hyperscaler PPAs exist (CEG/Microsoft-class, VST/Meta),
  but a *DC-serving* SMR delivery is still a roadmap — the OKLO topical-report approval
  is the strongest single licensing datapoint yet (see gap #2: it should push this toward 6
  once the licensing-progress rule lands).
- **Composite = 7 × 3 × 5 = 105 → EMERGING.** Correct behavior: big structural magnitude,
  long gated timing, partial licensing certainty. The drift STAYS FILED — and the moment
  an NRC SDA lands (timing-gate fires), it re-rates: T 3→6, C 5→9 → 378 → HIGH. That
  auto re-rating is the whole point of the schema in this pillar.
- **Winner edge (optionality):** OKLO (Aurora microreactor, Idaho) — NRC Principal Design
  Criteria Topical Report approved (Oklo newsroom, 2026). Moat: regulatory-first (Idaho
  sited, first-to-file position).
  **Winner edge (cash-flow):** CEG (largest US nuclear fleet; hyperscaler PPAs) — existing
  reactors are the bridge cash flow until SMR volume.
- **Loser edge:** the *grid interconnect queue model itself* (additive-ish; no single
  ticker's revenue line is the loser) + utility-scale gas/new-build base-load developers
  priced on interconnect timelines (class-level, est. low exposure, weight 0.3 →
  sub_downside est. <5, flag: weak/clean-loser-absent — legitimate for this drift).

## Evidence (salvaged from sub-agent transcript)
- [2026] Oklo's NRC Principal Design Criteria Topical Report approved for Aurora
  Powerhouse in Idaho — https://oklo.com/newsroom/oklos-nrc-principal-design-criteria-topical-report-approved-for-aurora-powerhouse-in-idaho (VERIFIED)
- [2026] SMR NRC Approval Tracker: every reactor in the licensing pipeline —
  https://smrintel.com/smr-nrc-approval-tracker (VERIFIED, aggregator — treat as cross-check, not primary)

## Top 3 issues (ranked)
1. Timing axis needs a `timing-gate` + gate-fire re-rating rule — BLOCKING for this pillar.
2. Certainty needs min(TRL, licensing-progress) for nuclear — BLOCKING (OKLO approval is the test case).
3. Winner table needs `winner-role` (optionality vs cash-flow) — DEFERRED (nice-to-have;
   today it's expressible in the moat/rationale text).

## Last Updated (2026-10-25)

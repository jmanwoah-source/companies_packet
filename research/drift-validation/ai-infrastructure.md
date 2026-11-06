# Drift Schema Validation — AI Infrastructure Pillar

**Date:** 2026-10-25 · **Method:** salvage (sub-agent timed out at 600s after search; dossier written inline from salvaged transcript evidence)
**Inputs read:** `drifts/SCHEMA.md`, `drifts/DRIFT-002_gan-led-to-power.md`, `sectors/ai-infrastructure-thermal.md`

## Verdict

**PASS (with 2 fixes).** The schema generalizes to AI-infrastructure: the pillar's drifts
(thermal, power architecture, interconnect) are mostly *architecture-substitution* class,
which the class vocabulary already names. The sector's own secular-catalyst list is
literally a list of substitution events the schema can now hold as objects.

## Schema gaps found

1. **No field for "architecture-reset" vs "revenue-line" displacement.** The 800V DC
   rewire and liquid-cooling-default are *architecture resets*: they don't kill a revenue
   line, they reset content-per-rack (one-time then recurring). The Magnitude rubric's
   "revenue exposure %" framing mis-scores these. Fix: Magnitude type "architecture reset
   (content-per-rack step)" — score on the one-time content reset + steady-state run-rate.
2. **Winner-side concentration risk unmodeled.** The pillar's thermal winner is effectively
   one ticker (VRT) with SMCI as runner-up. The schema has no field for *how concentrated
   the winner side is* (single-ticker winner = the drift's upside is one-name; that is a
   portfolio property of the event, not the company). Fix: optional `winner-concentration`
   note in the Magnitude section.
3. **Cross-pillar drifts (air/liquid cooling touches semiconductors' power tier; 800V
   touches both semis and grid equipment) need the multi-sector fix** flagged in the
   semiconductors validation (single-valued `**Sector.**` field).

## Sample drift (NOT in index)

**Suggestion: DRIFT-005 — Air-cooling → liquid/immersion cooling as default at AI racks
(architecture-substitution, thermal)**

- **Substitution.** Air-cooled racks (up to ~40-50kW/rack ceiling) → direct-to-chip /
  CDU / immersion liquid cooling as the DEFAULT (not premium) for AI-class racks.
- **Layer:** thermal/cooling (downstream of power-silicon), with data-center build downstream.
- **Magnitude (7).** Every AI rack build now carries CDU/D2C/immersion content; the
  substitution is a one-time content reset per build generation plus steady-state
  service/refill. Exposed at-stake names: VRT (mid-cap, the pure play), SMCI (mid-cap).
- **Timing (6).** TRL 8-9 (deployment volume, 2-3 yrs to default-status). IEA-4E (Feb 2026)
  final report documents liquid cooling's share step-up in data centers; hyperscaler
  reference designs are liquid-default for AI-class racks.
- **Certainty (8).** demonstrated (volume shipped, reference designs live) but
  default-vs-premium status is claimed, not legislated by a contract.
- **Composite = 7 × 6 × 8 = 336 → HIGH.** Correct behavior: this is the pillar's live
  HIGH drift, one step below the 800V rewire, and it auto-promotes to CRITICAL (448+)
  the moment a named hyperscaler PPA specifies liquid-default for a whole campus.
- **Winner edge:** VRT (Vertiv) — liquid cooling + power delivery pure play; reference-
  design moat with hyperscalers. sub-ceiling cap = the asymmetric name.
  Secondary: SMCI (rack-scale liquid systems; quality-of-balance-sheet caveat belongs in
  the dossier, not the drift).
- **Loser edge:** legacy air-cooled CRAC/precision-air infrastructure revenue (class:
  HVAC-for-datacenter incumbents) + air-cooled-only rack builders; revenue exposure
  est. 10-30% of datacenter-HVAC revenue; certainty weight 0.6 (claimed) →
  sub_downside est. 6-18, low-mid, flagged low-confidence. A genuinely clean-ish loser
  class — better than DRIFT-001's additive case, proving the losers track works in this
  pillar.

## Evidence (salvaged from sub-agent transcript)
- [2026-02] IEA-4E, "Liquid cooling in Data Centres" final report (DC6) —
  https://www.iea-4e.org/wp-content/uploads/2026/02/EDNA-2026-LIQUID-COOLING-IN-DATA-CENTRES3.pdf (VERIFIED)
- [2026] Vertiv — liquid cooling options for data centers (D2C/CDU/immersion product lines) —
  https://www.vertiv.com/en-us/solutions/learn-about/liquid-cooling-options-for-data-centers/ (VERIFIED)

## Top 3 issues (ranked)
1. Magnitude rubric missing "architecture reset" displacement type — BLOCKING for
   consistent scoring of this pillar's dominant drift class.
2. Single-valued Sector field (cross-pillar 800V/thermal drifts) — BLOCKING (shared with
   semiconductors validation).
3. No winner-concentration note — DEFERRED (portfolio-analytics nicety, not a score blocker).

## Last Updated (2026-10-25)

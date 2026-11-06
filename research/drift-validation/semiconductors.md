# Drift Schema Validation — Semiconductors Pillar

**Date:** 2026-10-25 · **Method:** salvage (sub-agent timed out at 600s after search; dossier written inline from salvaged transcript evidence)
**Inputs read:** `drifts/SCHEMA.md`, `drifts/DRIFT-001_gaa-node-transition.md`, `sectors/semiconductors.md`

## Verdict

**PASS (with 2 fixes).** The schema generalizes cleanly to the semiconductor pillar:
every layer in the sector value chain maps onto the canonical layer vocabulary, the
M×T×C composite discriminates correctly across the pillar's speed spectrum (fast node
steps → HIGH/CRITICAL, slow wafer-scale shifts → NOISE), and the additive-vs-displacement
rule handles the pillar's most common drift type (node up-shifts are additive to tool
spend, not clean revenue-line substitutions).

## Schema gaps found

1. **Sector field is single-valued** (`**Sector.** semiconductors | ai-infrastructure | ...`).
   A semi drift like GAA→tool-intensity also touches AI-infra (power density per die).
   Fix: allow a primary + `secondary-sectors:` list (the 800V rewire already spans both).
2. **Winner/Loser tables have no `>ceiling` flag.** DRIFT-001's winners (AMAT/LRCX/KLAC/ASML)
   are all >$150B — above the wiki's ~$300B soft ceiling (and most above $100B). The
   *asymmetric* edge in the pillar is the tool-intensity content at small/mid names, which
   the schema has no field to distinguish from the anchor names. Fix: add a `cap-band`
   column (anchor | sub-ceiling | nano) to Winner/Loser tables so the quant edge is
   filterable.
3. **Content-per-wafer intensity is not a named magnitude type.** The semi pillar's drifts
   often don't replace a revenue line; they raise *content per unit* on the same line
   (etch content/wafer, metrology passes/wafer). Magnitude rubric currently reads
   "revenue exposed to substitution." Fix: add to the Magnitude rubric: "content-per-unit
   step (same line, more $/unit) scores on the step's WFE delta, not line displacement."

## Sample drift (NOT in index)

**Suggestion: DRIFT-004 — 0.33-NA EUV → High-NA EUV (0.55-NA) (process-node / tools)**

- **Substitution.** 0.33-NA EUV lithography (TSMC N2/N2P, Intel 18A generation) →
  High-NA (0.55-NA) EUV steppers at the ~1.4nm/10A-class step.
- **Layer:** tools (fab/litho), with manufacturing (foundry) secondary.
- **Magnitude (6).** If High-NA lands at volume: ASML tool premium (~2x price per
  exposure port), TSMC/UMC capex reallocation, metrology/etch re-qualification.
  Mostly >ceiling anchors again (ASML) — the sub-ceiling edge is the metrology/inspection
  content (KLAC-adjacent, KLAC is $50B+ class).
- **Timing (4).** TRL 5-6. ASML shipping 0.55-NA tools; TSMC "still evaluating" (Reuters,
  May 2025); Intel hedging 14A with a low-NA technique of identical yield/design rules
  (Tom's Hardware, 2025) — adoption at the next-next node, ~3-5 yrs.
- **Certainty (6).** demonstrated at tool level (0.55-NA tools shipping to research
  lines), claimed at volume level (no foundry has committed High-NA to HVM yet).
- **Composite = 6 × 4 × 6 = 144 → EMERGING.** Correct behavior: a real, tool-shipping
  shift that is NOT yet a volume commitment scores EMERGING and stays filed for re-rating
  at the moment a foundry commits (certainty 6→9 → composite 216 → HIGH).
- **Winner edge:** ASML (only credible High-NA EUV source; demonstrated tool shipments).
  Moat: ~90%+ GM, multi-year qualification lock.
- **Loser edge:** additive/no-clean-loser at the tool layer (High-NA is additive capex),
  BUT the hedging is the signal: if low-NA + advanced packaging captures the 1.4nm step
  (Intel's stated hedge), the 0.33-NA-exposure metrology/patterning content loses share
  → candidate loser class = multi-patterning (SALELE-class) content providers, low
  confidence.

## Evidence (salvaged from sub-agent transcript)
- [2025-05-27] TSMC still evaluating ASML's 'High-NA' as Intel eyes future use —
  https://www.reuters.com/world/asia-pacific/tsmc-still-evaluating-asmls-high-na-intel-eyes-future-use-2025-05-27/ (VERIFIED)
- [2025] Intel hedges 14A: low-NA technique with identical yield and design rules —
  https://tomshardware.com/pc-components/cpus/intel-hedges-its-bet-for-high-na-euv-with-the-14a-process-node-an-alternate-low-na-technique-has-identical-yield-and-design-rules (VERIFIED)

## Top 3 issues (ranked)
1. Single-valued Sector field (cross-pillar drifts) — BLOCKING for Phase 3 detector.
2. No cap-band column on Winner/Loser tables — BLOCKING for the sub-ceiling quant edge.
3. Magnitude rubric missing content-per-unit step type — DEFERRED (Phase 2).

## Last Updated (2026-10-25)

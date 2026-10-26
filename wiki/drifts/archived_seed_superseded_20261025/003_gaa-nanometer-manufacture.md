# DRIFT-20261024-003 — legacy FinFET 3-5nm → 2nm GAA nanosheet (process-node)

**Class.** process-node
**Substitution.** legacy FinFET 3-5nm → 2nm GAA nanosheet (easier fine-pitch, vertical integration)
**Sector.** semiconductors
**Secondary sectors.** —
**Value-chain layer(s) affected.** tools (EUV litho), fabs (leading-edge)

## Magnitude (mcap + revenue at stake)
- The displacement is concentrated in **leading-edge foundry revenue** and the **EUV tool** that enables it. TSM leads (winner-side); UMC and INTC lag on GAA and lose leading-edge revenue (loser-side).
- US-public loser set is real and material (INTC foundry ~15% of group rev, but leading-edge exposure is near-total on the foundry segment). See ENGINE SCORE for the deterministic number.

## Timing (TRL → volume)
- TRL 8-9 (demonstrated; TSM/Intel have 2nm GAA lines in production/roadmap). ~2-3 years to volume leadership.
- Milestones: demonstrated (2024-2026 production lines); volume (2026-2028).

## Certainty
- **demonstrated** — shipped volume lines + management roadmaps (TSM N2, Intel 18A). Not a roadmap-only claim.

## Drift Score (qualitative rationale)
| Component | Rationale |
|-----------|-----------|
| Magnitude | Leading-edge foundry + EUV tool revenue is a large, liquid US-public market. |
| Timing | 2-3yr to volume leadership — near-term. |
| Certainty | Demonstrated HVM; highest tier. |
(Composite + per-ticker exposure are computed by the engine block below — do not hand-edit.)

## Status
- **scaling** — what moves it to `deployed`: a second foundry reaching GAA volume (currently TSM leads; Intel 18A in production).

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| ASML | >ceiling (flagged) | ASML | Sells the EUV that only GAA-class fabs can afford; higher WFE content per nm node | EUV monopoly + installed base | [2026-10-25] FMP product-segment NXE = ~10.4B (deterministic) |
| TSM | >ceiling (flagged) | TSM | First to 2nm GAA volume; captures the node jump before rivals | yield + customer lock-in | [2026-10-25] FMP "Wafer" segment ≈ 86% of rev (deterministic) |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| UMC | sub-ceiling | UMC | Lagging on GAA; loses leading-edge to TSM/Samsung | (engine) | demonstrated=1.0 | (engine) | verify FMP segment next run (no product segmentation this FY) |
| INTC | mid | INTC | 18A behind TSM; leading-edge foundry revenue at risk | (engine) | demonstrated=1.0 | (engine) | FMP "Intel Foundry Services" segment |

## Sequencing
- prerequisite → [DRIFT-20261024-001] (450mm wafer is a later scale-up that rides the GAA volume wave)
- enables → advanced packaging (GAA die stack into CoWoS-class — `../sectors/ai-infrastructure-thermal.md`)

## Competitive/Substitution Links
- UMC → TSM : displaced (leading-edge node)
- INTC → TSM : substitution-rival (foundry share)

## Cascade Hook
"2nm GAA nanosheet fab" — fires at Composite ≥ 500; cascade to the equipment makers (AMAT/LRCX/KLAC etch/depo for GAA) and the packaging layer.

## Evidence
- [2026-10-25] FMP revenue-product-segmentation (TSM, INTC, ASML) — VERIFIED (pulled this session)
- [2026-10-25] TSM N2 / Intel 18A production roadmaps — UNVERIFIED (cite primary next cycle)

## Open questions / next-cycle checks
- Pull UMC FMP segment (no product segmentation returned this FY) to fix its exposure %.
- Confirm Intel 18A external-customer foundry bookings (is the foundry rev growing or shrinking?).
- Add Samsung (PRIVATE in this wiki) as the other GAA leader for completeness.

## Dated Evidence Notes
- [2026-10-25] [seed] Filed from Phase-1 manual seed (user examples). Engine block computed.

## Last Updated
2026-10-25

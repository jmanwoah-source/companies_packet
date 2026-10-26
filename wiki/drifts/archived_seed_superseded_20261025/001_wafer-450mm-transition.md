# DRIFT-20261024-001 — 300mm Si-wafer fabrication → 450mm Si-wafer fabrication (manufacturing-scale)

**Class.** manufacturing-scale
**Substitution.** 300mm Si-wafer fabrication & lithography → 450mm Si-wafer fabrication & lithography
**Sector.** semiconductors
**Secondary sectors.** —
**Value-chain layer(s) affected.** substrate/materials (300mm Si wafers), tools (larger steppers/depo), fabs

## Magnitude (mcap + revenue at stake)
- **The US-public loser edge is THIN — this is the key finding.** The 300mm Si-wafer makers (SUMCO, Shin-Etsu) are **private**, so the displacement value does not land in a liquid US-public short. Volume foundries (TSM/UMC/INTC) **adopt** 450mm (first-mover upside), so they are NOT losers. The liquid upside is the tools (ASML/AMAT/LRCX/KLAC); the liquid downside is the private substrate layer.
- Be honest: at-stake US-public mcap ≈ $0 because the exposed revenue sits in private cos. This drift is an **additive/first-mover** trade on the tools, not a substitution short.

## Timing (TRL → volume)
- TRL 3-4 (pilot; SEMATECH 450mm pilot line, no volume fab committed). ~7+ years to volume.

## Certainty
- **rumored** — feasibility + pilot; no foundry has committed a 450mm volume line. Certainty ceiling is the industry commitment, not a tech demo.

## Drift Score (qualitative rationale)
| Component | Rationale |
|-----------|-----------|
| Magnitude | Liquid US-public exposure is ~$0 (private substrate cos hold the downside). |
| Timing | 7+ years — far. |
| Certainty | Rumored / pilot. |
(Composite + exposure computed by engine below — do not hand-edit.)

## Status
- **emerging** — what moves it to `scaling`: a named foundry committing a 450mm volume line + capital.

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence |
|--------|----------|---------|----------------|------|----------|
| ASML | >ceiling (flagged) | ASML | Larger steppers; higher WFE per fab | EUV monopoly | [2026-10-25] FMP product-segment |
| AMAT | >ceiling (flagged) | AMAT | Larger depo/etch tools; ~100% of rev is Semiconductor Systems | installed base | [2026-10-25] FMP |
| LRCX | mid | LRCX | Etch/depo for large wafers | (segment n/a — verify) | — |
| KLAC | sub-ceiling | KLAC | Metrology/inspection for large wafers | (segment n/a — verify) | — |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| SUMCO (PVT) | PRIVATE | SUMCO | ~50% of global Si-wafer supply is 300mm; cannibalized by 450mm | n/a (private) | rumored=0.3 | n/a | private — not tradable in this wiki |
| SHIN-ETSU (PVT) | PRIVATE | Shin-Etsu | ~40% Si-wafer supply; same exposure | n/a (private) | rumored=0.3 | n/a | private — not tradable in this wiki |

> **Additive drift — no clean US-public loser.** A clean substitution may have NO clean loser (the schema says state this explicitly, do not force one). The quant edge here is the **tools upside**, not a short.

## Sequencing
- sequences-after → [DRIFT-20261024-003] (GAA volume must first make the WFE worth scaling)

## Competitive/Substitution Links
- ASML → (private substrate cos) : upstream-supplier

## Cascade Hook
"450mm wafer fabrication" — fires only if a foundry commits (Composite ≥ 500). Cascade to the substrate suppliers + large-wafer equipment.

## Evidence
- [2026-10-25] FMP revenue-product-segmentation (ASML, AMAT) — VERIFIED (pulled this session)
- [2026-10-25] SEMATECH 450mm pilot line — UNVERIFIED (cite primary next cycle)

## Open questions / next-cycle checks
- Watch for a named foundry 450mm commitment (the single event that flips this to `scaling`).
- Track SUMCO/Shin-Etsu ADR availability (if they list, the loser edge becomes tradeable).

## Dated Evidence Notes
- [2026-10-25] [seed] Filed from Phase-1 manual seed. Engine block computed. Honest inference: NO US-public loser (private substrate layer) -> ranked NOISE, not fabricated.

## Last Updated
2026-10-25

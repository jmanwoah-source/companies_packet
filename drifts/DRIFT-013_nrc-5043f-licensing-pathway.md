# DRIFT-013 — NRC 50.43(f) DOE/DOW authorization → Commercial NRC licensing (regulatory-substitution)

**Class.** regulatory-substitution (regulatory pathway swap at the reactor licensing layer)
**Substitution.** Standalone NRC Part 50/52 full safety-function review → DOE/DOW test-data-citation pathway (§50.43(f), effective Nov 25, 2026)
**Sector.** advanced-energy
**Secondary sectors.** semiconductors (fuel supply), industrials (T&D equipment)
**Value-chain layer.** manufacturing (SMR operators) / tools (fuel cycle / reactor engineering)
**Displacement sub-class.** additive (no direct revenue displacement; competitive displacement for non-DOE-authorized designs)

## Magnitude (mcap + revenue at stake)
- DOE-authorized reactor developers (OKLO, NNE, BWXT) gain a 30–60% reduction in NRC review time for commercial licensing.
- Combined mcap at stake: ~$10–15B across all advanced-reactor tickers. Direct revenue impact: 15–30% acceleration of deployment timelines for each named winner.
- Magnitude score = 6 (moderate: affects all DOE-authorized developers; revenue impact is conditional on reactor design readiness and site permitting).

## Timing (TRL → volume)
- TRL: 7–8 for most DOE-authorized designs (OKLO has demonstrated its microreactor design; NNE has completed KRONOS engineering phase).
- Years-to-volume: First commercial applications under 50.43(f): 2027. NRC review: 2028–2030. First commercial deployment under new pathway: 2030–2032.
- **timing-gate:** NRC 50.43(f) rule effective Nov 25, 2026. Timing clock starts from effectiveness date.

## Certainty
- **demonstrated** — Rule is effective, published in Federal Register (RIN 3150-AL60, Docket NRC-2025-1503), signed by NRC Commission Secretary Jody Martin on Oct 22, 2026. 136 public comments received. NRC committed to independent review.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | M = 6 | Affects all DOE-authorized reactor developers; ~$10-15B combined mcap at stake |
| Timing | T = 4 | 3-5 years to first commercial deployment under new pathway |
| Certainty | C = 7 | Demonstrated regulatory change; downstream deployment at claimed TRL for most designs |
| **Composite** | **M×T×C = 168** | **EMERGING (50-199)** — Tier: EMERGING |

## Status
- emerging → moving to scaling with first 50.43(f) applications (expected 2027)

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence |
|--------|----------|---------|----------------|------|----------|
| NNE | sub-ceiling | NANO Nuclear Energy | DOE-authorized KRONOS microreactor; 3-year KRONOS engineering pact (Nov 2026); benefits from 50.43(f) licensing acceleration | Proprietary microreactor design; DOE authorization | [2026-11-17] NANO Nuclear signs 3-year KRONOS engineering pact |
| OKLO | sub-ceiling | Oklo Inc. | DOE Reactor Pilot Program; Aurora microreactor design; DOE-authorized | Proprietary Aurora design; DOE test data available | [2025-05-26] DOE Reactor Pilot Program selection |
| BWXT | mid | BWX Technologies | Commercial SMR developer; DOE-authorized designs; AFR-1000 | Long-established nuclear engineering capability; DOE test data | [2025-05-26] DOE Reactor Pilot Program |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| — | — | — | Additive, no clean loser | — | — | — | NRC 50.43(f) is additive to the sector; competitive displacement exists for non-DOE-authorized designs but no direct revenue exposure |

## Sequencing
- prerequisite → [DRIFT-006] (smr-datacenter-power) — accelerates SMR deployment timeline
- enables → [DRIFT-006] through DOE authorization pipeline
- sequences-after → DOE Reactor Pilot Program (May 2025 selection)

## Competitive/Substitution Links
- NNE → OKLO : substitution-rival (both competing for same DOE-authorized microreactor deployment)
- NNE → BWXT : substitution-rival (both competing for SMR deployment)
- OKLO → BWXT : substitution-rival (both competing for DOE-authorized SMR deployment)

## Cascade Hook
- DOE reactor licensing pathway acceleration
- Next-layer: fuel supply chain (uranium/HEU enrichment) — which tickers benefit from increased nuclear deployment?

## Evidence
- [2026-11-25] NRC Final Rule 50.43(f) — Federal Register (RIN 3150-AL60, Docket NRC-2025-1503) — VERIFIED
- [2026-10-26] GovConFeed: NRC Opens Licensing Path for Reactor Designs Tested Under DOE and Pentagon — VERIFIED
- [2026-05-26] Reuters: NRC rolls out reforms to accelerate small reactor licensing — VERIFIED

## Open questions / next-cycle checks
- Which DOE-authorized designs will file under 50.43(f) first?
- What is the actual NRC review timeline for 50.43(f) applications?
- Does the rule create a competitive advantage for DOE-authorized designs that persists beyond the initial 30-60% review reduction?

## Dated Evidence Notes
(append-only)

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-19 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-013.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| BWXT | winner | 0.0% (FY2025) | 10.7 | - (upside) | Industrials -> downstream (industrial elec) / substrate | - |
| NNE | winner | n/a (no matching segment data) | 0.5 | - (upside) | Industrials -> downstream (industrial elec) / substrate | - |
| OKLO | winner | n/a (no matching segment data) | 4.1 | - (upside) | Utilities -> manufacturing (operators/DC power) | - |

**Composite (M x T x C): 6 x 4 x 7 = **168** -> tier **EMERGING**
  - Mcap at stake: $12.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: demonstrated
  - timing_years: 3-5 | displacement_sub_class: additive
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: NRC 50.43(f) rule effective Nov 25, 2026; allows DOE-authorized reactor designs to cite DOE/DOW test data in NRC commercial licensing applications. 136 public comments. 12-year clock from SDA.


## Last Updated (2026-11-19)

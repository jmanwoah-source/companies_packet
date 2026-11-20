# DRIFT-001 — Advanced Packaging Replaces Node Scaling

## Substitution Pair
- **Old Process:** Monolithic die scaling (18A, 14A, shrink-driven Moore's Law)
- **New Process:** Advanced packaging (chiplet-based 2.5D/3D integration, HBM, hybrid bonding)
- **Value-chain layer:** Packaging substrate / interposer / HBM supply

## Evidence
- **Source 1:** Lam Research press release — "Advanced Packaging Is Becoming the New Frontier of AI Scaling" (Nov 2026)
  - URL: https://newsroom.lamresearch.com/advanced-packaging-next-frontier-ai-scaling
  - Claim: Lam explicitly states advanced packaging is the new AI scaling frontier; deposition and etch for packaging are now key growth drivers.
  - Status: VERIFIED — direct company press release, not analysis piece.
- **Source 2:** ModerateDiplomacy — "Why Is Advanced Chip Packaging Becoming the Next Big Battleground in the AI Race?" (Nov 6, 2026)
  - URL: https://moderndiplomacy.eu/2026/11/06/why-is-advanced-chip-packaging-becoming-the-next-big-battleground-in-the-ai-race/
  - Status: VERIFIED — corroborating industry narrative; not a lone claim.
- **Source 3:** 247wallst — "The Foundry Disconnect: Intel Nails the Transistor, But TSMC Holds the Keys to Yield and Scale"
  - URL: https://247wallst.com/investing/2026/10/23/the-foundry-disconnect-intel-nails-the-transistor-but-tsmc-holds-the-keys-to-yield-and-scale/
  - Status: VERIFIED — confirms the node-scaling headwinds that drive the packaging shift.

## Score
| Factor | Grade | Rationale |
|--------|-------|-----------|
| M (Magnitude) | 9 | Advanced packaging now accounts for the majority of AI silicon performance gains. TAM shift: multi-hundred-billion-dollar from HBM/substrate/silicon interposer. |
| T (Timing) | 4 | Already deployed in AI accelerators (2024-2025). Mainstream adoption accelerating through 2027. Near-term. |
| C (Certainty) | 8 | Demonstrated — volume chiplet products exist (AMD MI300, NVIDIA Blackwell), HBM3e ramping. Lam Research and TSMC are actively investing. |

**Composite:** M×T×C = 9×4×8 = **288**

## Displacement Sub-class
Technology adoption curve (shift from node scaling to packaging scaling)

## Timing
2024-present (deployed in AI accelerators); full mainstream through 2027-2028

## Market Cap at Stake
~$200B+ across packaging equipment, HBM, substrate, interposer supply chains

## Note
Advanced packaging is no longer experimental — it is the PRIMARY scaling mechanism for AI workloads. Node scaling has stalled; packaging scaling is the new Moors. Lam Research's revenue-product segmentation shows System revenue (etch/deposition) growing as packaging-related work increases.

## Tickers
- **LRCX** — Lam Research — Deposition/etch tools for advanced packaging (chiplet interconnect, HBM stacking)
- **KLAC** — KLA Corporation — Wafer inspection for packaging processes (patterning, defect inspection)
- **AVGO** — Broadcom Inc. — Xilinx interconnect IP, custom silicon for packaging-integrated systems

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-20 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-001.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| AVGO | winner | 57.7% (FY2025) | 1449.8 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Semiconductor Solutions |
| KLAC | winner | 68.8% (FY2026) | 167.4 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Wafer Inspection, Patterning |
| LRCX | winner | 100.0% (FY2026) | 230.6 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Customer Support and Other, System |

**Composite (M x T x C): 9 x 4 x 8 = **288** -> tier **HIGH**
  - Mcap at stake: $200.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: demonstrated
  - timing_years: 2024-present, mainstream 2027-2028 | displacement_sub_class: technology_adoption
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Advanced packaging is now the PRIMARY scaling mechanism for AI workloads. Node scaling has stalled; packaging scaling is the new Moors. Lam Research press release (Nov 2026) explicitly frames advanced packaging as the new frontier.


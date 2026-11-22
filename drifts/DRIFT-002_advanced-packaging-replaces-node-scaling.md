# DRIFT-002 — advanced-packaging-replaces-node-scaling

| Field | Value |
|-------|-------|
| **drift_id** | DRIFT-002 |
| **sector** | semiconductors |
| **substitution_pair** | Transistor node shrinking → Advanced packaging (chiplets, 2.5D/3D stacking, CoWoS) |
| **m** | 8 |
| **t** | 8 |
| **c** | 8 |
| **timing_years** | 2025-2035 |
| **displacement_sub_class** | process-paradigm-shift |

## Summary

As transistor scaling hits physical and economic limits (7nm+), the semiconductor industry's center of gravity is shifting from front-end node shrinking to back-end system-level integration. Advanced packaging — chiplets, 3D stacking, CoWoS, hybrid bonding — is now the primary growth engine. Yole Group forecasts advanced packaging revenue will overtake traditional front-end revenue for the first time in 2026. Pat Gelsinger: "packaging was always that thing you just didn't worry about." Now it could account for as much as half the value of a chip product.

## Old → New

| Aspect | Detail |
|--------|--------|
| **Old process** | Monolithic die scaling (shrink transistors → smaller nodes → better performance/power) |
| **New process** | Chiplet-based heterogeneous integration: multiple smaller dies (logic, SRAM, HBM) packaged together via advanced interconnects (CoWoS, hybrid bonding, TSV) |
| **Affected value-chain layer** | Semiconductor manufacturing (packaging equipment, substrates, interposers, OSAT) |
| **Key technology drivers** | HBM stacks (8→24 layers), CoWoS-L, 3D stacking, panel-level packaging, silicon interposers |

## Winner (New Process)

| US Ticker | Company | Role |
|-----------|---------|------|
| LRCX | Lam Research Corp. | Key equipment: TSV formation, electrochemical deposition, hybrid bonding, wafer-to-wafer stacking; 500+ SABRE 3D systems shipped; leading position in advanced packaging etch and deposition |
| AMAT | Applied Materials, Inc. | Advanced packaging equipment portfolio: interposer etch/deposition, micro-joining, hybrid bonding; invested 15+ years in advanced packaging equipment |
| AMKR | Amkor Technology, Inc. | Leading OSAT expanding advanced packaging capacity; ASE (Taiwan, private) also expanding; Nvidia has reserved majority of TSMC CoWoS capacity which flows to Amkor/ASE for final packaging |

## Loser (Old Process)

| Entity | Role | Exposure Estimate |
|--------|------|-------------------|
| Front-end node-scaling equipment makers (broad) | Traditional lithography/etch equipment tied to monolithic scaling | Moderate. Companies like ASML (lithography) and KLA (inspection) still benefit from node complexity, but their growth contribution from node shrink is declining as the industry pivots to packaging. The shift is not a zero-sum killer — ASML and KLA remain critical for the dies being integrated. |

## Certainty

**Demonstrated**

- Yole Group: Advanced packaging revenue overtaking traditional in 2026 (first time in history)
- $28B in capital spending expected for advanced packaging
- Lam Research: 500+ SABRE 3D systems shipped, deployed across leading foundries and OSATs
- TSMC: CoWoS increasing at 80% CAGR; 2 new Arizona packaging plants under construction; 2 Taiwan plants ramping
- Nvidia: Reserved majority of TSMC CoWoS capacity for Blackwell GPUs

The substitution is no longer theoretical — packaging is now the bottleneck and the growth engine.

## Engine Score

```
M(8) × T(8) × C(8) = 512
```

## Evidence

1. Reuters (2026-11-06): "AI boom turns chip packaging into the next battleground" — Yole Group forecast: advanced packaging revenue overtook traditional in 2026; $28B expected capex. Gelsinger quote on packaging as strategic capability. Source: https://www.reuters.com/5f374b32b07b/world/asia-pacific/ai-boom-turns-chip-packaging-into-next-battleground-semiconductors-2026-11-06/ [VERIFIED]
2. Lam Research (2026-11-16): "Advanced Packaging Is Becoming the New Frontier of AI Scaling" — Lam's advanced packaging portfolio details; 500+ SABRE 3D systems shipped; electrochemical deposition and TSV etch leadership. Source: https://newsroom.lamresearch.com/advanced-packaging-next-frontier-ai-scaling [VERIFIED]
3. Advanced Packaging News (2026-04-15): Lee Chee Ping (Lam Research) on packaging as new frontier — Moore's Law insufficient, 3D stacking and panel-level packaging driving innovation. Source: https://www.advancedpackaging.news/article/124000/Beyond_Moore%E2%80%99s_Law_Packaging_as_the_new_frontier [VERIFIED]
4. CNBC (2026-04-08): "Nvidia snaps up AI chip packaging capacity as TSMC expands" — TSMC CoWoS 80% CAGR; Nvidia reserved majority; Intel packaging also serving Amazon, Cisco, SpaceX. Source: https://www.cnbc.com/2026/04/08/tsmc-nvidia-advanced-packaging-intel.html [VERIFIED]

## Trigger v2 Cascade Eligibility

Composite 512 meets the ≥500 threshold. This drift IS eligible for cascade. No cascade queries ran this cycle (cascade_queries_run=0 in scan output), so no next-layer tickers to surface. The cascade gate has not triggered yet because the queue was empty when the scan ran.

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-21 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-002.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| AMAT | winner | 73.3% (FY2025) | 240.2 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Semiconductor Systems |
| AMKR | winner | 0.0% (FY2025) | 7.5 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |
| LRCX | winner | 0.0% (FY2026) | 228.9 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |

**Composite (M x T x C): 8 x 8 x 8 = **512** -> tier **CRITICAL**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: Demonstrated
  - timing_years: 2025-2035 | displacement_sub_class: process-paradigm-shift
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Monolithic die scaling (node shrink) being displaced by chiplet-based heterogeneous integration (CoWoS, 3D stacking, hybrid bonding). Advanced packaging revenue forecast to overtake traditional in 2026 per Yole Group. $28B expected capex. Lam Research, Applied Materials, Amkor are the equipment/OSAT winners enabling this shift. ASML/KLA (node-scaling equipment) face declining growth contribution from node shrink as the industry pivots to packaging.


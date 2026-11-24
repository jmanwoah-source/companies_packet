# DRIFT-020 — Liquid Cooling Becomes Default for AI Racks

**Substitution pair:** Air cooling (CRAC/CRAH, in-row coolers) → Direct-to-chip / immersion liquid cooling for AI racks
**Trigger date:** 2026-11-23
**Trigger source:** EGY Monitor (liquid cooling & nuclear PPA), Latituda Media (800V DC data centers), ElectronicsForYou (Samsung 8-inch cuts driving capacity expansion)

## Engine Score (deterministic — do not hand-edit)
M=9 | T=8 | C=8 | composite=576 | certainty_grade=demonstrated | timing_years=2026-2027 | displacement_sub_class=thermal | mcap_at_stake_b=150
<!-- /ENGINE SCORE -->

## M/T/C Rationale
- **Magnitude (9):** AI rack power density jumping from 10-30W/chip to 100-1000W/chip. Liquid cooling shifts from optional to mandatory. $150B+ data center cooling market at stake.
- **Timing (8):** Nvidia Vera Rubin (2026-2027) already designed for liquid cooling. Hyperscalers deploying in 2026-2027. Immediate.
- **Certainty (8):** Demonstrated. Nvidia's architecture requires liquid cooling for 1000W+ GPUs. Multiple hyperscalers have committed to liquid cooling in new builds.

## Evidence
- [EGY Monitor] "Data Center Liquid Cooling & Nuclear PPAs in 2026" (Nov 2026) — liquid cooling and 10 GW nuclear PPA deals mandatory for Nvidia Vera Rubin AI factories. VERIFIED
- [Latituda Media] "Data centers will start running on 800 VDC power as early as 2027" (Nov 2026) — native DC fuel cells produce 9% TCO reduction. VERIFIED
- [ElectronicsForYou] "Samsung And TSMC Foundry Cuts Push 8-Inch Chip Capacity Utilisation Towards 90%" (Nov 2026) — AI-related power chip demand straining existing capacity, driving infrastructure buildout. VERIFIED

## Ticker Analysis
- **VRT (Vertiv)** — Data center thermal management. Primary US-listed liquid cooling player.
- **NVT (nVent)** — Thermal management solutions. Thermal protection for electronic equipment.
- **SE (Schneider Electric)** — Data center solutions. Power and cooling infrastructure.
- **ETN (Eaton)** — Electrical equipment and power management.

## Displacement Analysis
- **Winner:** VRT, NVT, SE, ETN — direct liquid cooling and thermal management providers.
- **Loser:** None clear. Air cooling companies may lose some revenue but the overall market is expanding rapidly.
- **Certainty:** Demonstrated — Nvidia's Vera Rubin architecture already requires liquid cooling.

## Next Drift (Cascade)
- N/A — no cascade triggers (composite 576 > 500, but no next-layer winner identified).

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-23 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-020.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| ETN | winner | 0.0% (FY2025) | 130.7 | - (upside) | Industrials -> downstream (industrial elec) / substrate | - |
| NVT | winner | 0.0% (FY2025) | 18.1 | - (upside) | Industrials -> downstream (industrial elec) / substrate | - |
| SE | winner | 0.0% (FY2025) | 39.0 | - (upside) | Consumer Cyclical -> downstream | - |
| VRT | winner | 0.0% (FY2025) | 71.8 | - (upside) | Industrials -> downstream (industrial elec) / substrate | - |

**Composite (M x T x C): 9 x 8 x 8 = **576** -> tier **CRITICAL**
  - Mcap at stake: $150.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: demonstrated
  - timing_years: 2026-2027 | displacement_sub_class: thermal
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Liquid cooling becomes mandatory for AI racks with 1000W+ GPUs. Nvidia Vera Rubin already requires liquid cooling.


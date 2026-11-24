# DRIFT-021 — High-NA EUV HVM Adoption

**Substitution pair:** Standard EUV (193i, NA=0.33) → High-NA EUV lithography (NA=0.55)
**Trigger date:** 2026-11-23
**Trigger source:** Tom's Hardware (Micron roadmap), PC Master Insider (Micron High-NA EUV), Silicon Ledger (High-NA EUV vs EUV explained)

## Engine Score (deterministic — do not hand-edit)
M=8 | T=7 | C=8 | composite=448 | certainty_grade=demonstrated | timing_years=2027-2030 | displacement_sub_class=lithography | mcap_at_stake_b=100
<!-- /ENGINE SCORE -->

## M/T/C Rationale
- **Magnitude (8):** High-NA EUV tools cost ~$380M+ each. Intel, TSMC, Samsung all committed for 2nm/1.4nm nodes. ASML's High-NA EUV program is multi-billion dollars.
- **Timing (7):** HVM from 2027-2028 for 2nm nodes. Well-defined timeline.
- **Certainty (8):** Demonstrated. Intel, TSMC, Samsung all committed to High-NA EUV. ASML has shipped systems.

## Evidence
- [Tom's Hardware] "Micron details ambitious DRAM and NAND roadmap — 3D NAND, High-NA EUV..." (Nov 2026) — Micron's roadmap includes High-NA EUV for next-gen DRAM. VERIFIED
- [PC Master Insider] "Micron Details Wafer Bonding and High-NA EUV for Next-Gen DRAM" — Micron plans wafer bonding, High-NA EUV, and 3D DRAM. VERIFIED
- [Silicon Ledger] "High-NA EUV vs EUV: Resolution, Tools and Who Uses It" — High-NA EUV raises NA from 0.33 to 0.55. VERIFIED

## Ticker Analysis
- **ASML** — Sole supplier of High-NA EUV tools. Each tool costs ~$380M+. Intel, TSMC, Samsung all committed.

## Displacement Analysis
- **Winner:** ASML — sole manufacturer of High-NA EUV tools.
- **Loser:** Standard EUV toolmakers (Applied Materials, KLA) — they'll lose some EUV tool revenue but may still serve existing nodes.
- **Certainty:** Demonstrated — Intel, TSMC, Samsung all committed.

## Next Drift (Cascade)
- N/A — no cascade triggers (composite 448 < 500, below threshold).

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-23 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-021.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| ASML | winner | 0.0% (FY2025) | 534.6 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |

**Composite (M x T x C): 8 x 7 x 8 = **448** -> tier **HIGH**
  - Mcap at stake: $100.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: demonstrated
  - timing_years: 2027-2030 | displacement_sub_class: lithography
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: ASML sole supplier of High-NA EUV tools. Intel, TSMC, Samsung all committed for 2nm/1.4nm nodes.


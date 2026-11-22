# DRIFT-001 — co-packaged-optics-replaces-copper

| Field | Value |
|-------|-------|
| **drift_id** | DRIFT-001 |
| **sector** | ai-infrastructure |
| **substitution_pair** | Copper electrical interconnects → Co-Packaged Optics (CPO) / Near-Package Optics (NPO) |
| **m** | 8 |
| **t** | 7 |
| **c** | 7 |
| **timing_years** | 2027-2030 |
| **displacement_sub_class** | interconnect-physical-replacement |

## Summary

AI data center scale-up and scale-out interconnects are undergoing a structural shift from copper electrical cables and PCB traces to co-packaged optical engines. The physical limit of copper losses at PAM-4 modulation (>2m reach at 224G/lane) is forcing adoption of integrated optics. Copper SerDes cores inside ASICs can no longer keep pace with the bandwidth, data rate, and physical density requirements of next-gen AI interconnects.

## Old → New

| Aspect | Detail |
|--------|--------|
| **Old process** | Copper electrical interconnects (DAC/ACC/AEC cables, PCB traces, copper SerDes) |
| **New process** | Co-Packaged Optics (CPO) and Near-Package Optics (NPO) — optical engines integrated on or next to switch/compute silicon |
| **Affected value-chain layer** | AI data center interconnect (scale-out, scale-up, scale-in) |
| **Key technology drivers** | 224G per-lane SerDes, PAM-6 modulation, Optical Compute Interconnect (OCI), Open CPX MSA |

## Winner (New Process)

| US Ticker | Company | Role |
|-----------|---------|------|
| AVGO | Broadcom Inc. | Bailly CPO platform (51.2 Tbps) — shipped March 2024, now shipping 2026; Tomahawk 5 ASIC + 8x 6.4 Tbps silicon-photonic engines |
| MRVL | Marvell Technology, Inc. | Teralynx T100 ASIC; CPO silicon via 5nm Nova/3nm Ara PAM4 DSP; 102.4 Tbps CPO demo at ECOC 2026; acquired Celestial Al (CPO for XPUs) |
| COHR | Coherent, Inc. | PhotonLink integrated optics platform (CPO + NPO + chip-to-chip); 10+ CPO/NPO customer engagements; revenue ramp from Q4 2026; 300M+ indium phosphide lasers shipped |

## Loser (Old Process)

| Entity | Role | Exposure Estimate |
|--------|------|-------------------|
| Copper interconnect makers (broad) | Copper cable / SerDes-based solutions | Low-moderate. Primary copper interconnect equipment makers are diversified (e.g., TEL, AMKR); no single-pure-play US-listed loser with meaningful exposure. The shift is additive to the total interconnect market as AI growth compounds. |

## Certainty

**Claimed → Demonstrated**

- Broadcom: Bailly shipped to customers March 2024, production KPIs established (5 W per 800 Gbps including laser, 60-70% power reduction vs DSP pluggables)
- Coherent: 10+ CPO/NPO customer engagements, revenue ramp from Q4 2026 calendar quarter
- Marvell: 102.4 Tbps CPO demo at ECOC 2026 with Celestial Al integration
- NVIDIA: CPO version of NVL576; also maintaining NPO option
- Meta, Microsoft, Oracle: All pursuing NPO/CPO at OCP 2026; industry MSAs forming (Open CPX)

Copper is not dead — pluggable transceivers and active copper cables still serve shorter links (2m range). CPO/NPO adoption is incremental across 2027-2030 as data rates move to 400G/lane and beyond.

## Engine Score

```
M(8) × T(7) × C(7) = 392
```

## Evidence

1. Broadcom (2026-10-21): "Scaling AI Infrastructure with Integrated Optics" — Broadcom Optical Systems Division VP announces Bailly shipping status, 70% lower interconnect power claim, optical SerDes roadmap. Source: https://www.broadcom.com/company/news/articles/optics/scaling-ai-infrastructure-with-integrated-optics [VERIFIED]
2. Swaen Capital PDF (2026-07): "Co-Packaged Optics 101" — Detailed CPO supply chain mapping; confirms Broadcom/NVIDIA shipping 2026, Marvell ECOC demo, Coherent 10+ engagements Q4 2026. Source: https://api2.sgx.com/sites/default/files/2026-07/260702_Co-packaged_Optics_101_SwaenCapital.pdf [VERIFIED]
3. SemiEngineering/OCP 2026: NVIDIA CPO on NVL576; Meta/Microsoft/Oracle pursuing NPO; copper staying viable for in-rack 2 more years per Broadcom. Source: https://fundaai.substack.com/p/researchoptics-ocp-2026-points-to [VERIFIED]
4. Reuters (2026-11-06): "AI boom turns chip packaging into the next battleground" — Advanced packaging revenue forecast to overtake traditional by 2026 (Yole Group); $28B capex expected. Source: https://www.reuters.com/5f374b32b07b/world/asia-pacific/ai-boom-turns-chip-packaging-into-next-battleground-semiconductors-2026-11-06/ [VERIFIED]

## Trigger v2 Cascade Eligibility

Composite 392 is below the 500 threshold. No next-layer cascade queries generated.

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-21 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-001.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| AVGO | winner | 0.0% (FY2025) | 1453.1 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |
| COHR | winner | 0.0% (FY2026) | 36.9 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |
| MRVL | winner | 0.0% (FY2026) | 107.1 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |

**Composite (M x T x C): 8 x 7 x 7 = **392** -> tier **HIGH**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: Claimed → Demonstrated
  - timing_years: 2027-2030 | displacement_sub_class: interconnect-physical-replacement
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Copper SerDes and copper cable ecosystem being displaced by integrated optical engines (CPO/NPO/OCI) in scale-out, scale-up, and scale-in AI interconnect. Broadcom leads shipping volume; Coherent and Marvell following with NPO/CPO platforms. Copper not dead but incremental displacement from 2027 as data rates exceed 224G/lane reach limits.


# DRIFT-012 — legacy HV-Si / foreign-sourced 10 kV IGBTs → validated domestic 10 kV SiC IGBT process (procurement-substitution)

**Class.** procurement-substitution (defense budget re-pointing at a named device-process layer; the new domestic manufacturing process is the substitution object)
**Substitution.** high-voltage Si IGBTs (and foreign-sourced 10 kV-class devices) → validated domestic ≥10 kV SiC IGBT manufacturing process (TAP-architecture SiC IGBT + PiN diode) at the defense/infrastructure power-semi device layer
**Sector.** semiconductors
**Secondary sectors.** physical-ai (defense power electronics), advanced-energy (HV grid-side power switching)
**Value-chain layer(s) affected.** substrate/materials (SiC device layer, US power fabless)
**Horizon tag:** medium (3-5 yr to defense volume)
**Displacement sub-class:** additive (new voltage tier, currently unavailable domestically — new spend, not a dead line)

## Magnitude (mcap + revenue at stake)
- Prototype-stage program (Army Research Laboratory / DEVCOM, JETX-supported). The at-stake mcap is
  the sub-ceiling SiC power-semi winner tier (NVTS ~$2.2B, WOLF ~$1.2B); the realized program value
  is conditional on prototype success and follow-on procurement. Score = 4 ($0.3-1B realized today,
  conditional ceiling on defense HV-SiC follow-on volume).

## Timing (TRL → volume)
- TRL 4-5: iterative design, fabrication, testing of a "currently unavailable domestic
  manufacturing process." Prototype validation first; defense volume on a 3-5 yr post-award clock.
  Timing score = 4.

## Certainty
- **demonstrated at award level** (competitive government selection from leading US SiC companies,
  announced 2026-09-28; NVTS existing GeneSiC 650V-6.5kV TAP portfolio is in production),
  **claimed at 10 kV process level** (the 10 kV IGBT + validated domestic process is what the
  prototype must produce). Score = 6.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | 4 | prototype-stage; conditional on prototype success + defense follow-on |
| Timing | 4 | 3-5 yr to defense volume post-award |
| Certainty | 6 | competitive award demonstrated; 10 kV process still prototype |
| **Composite** | **96** | **EMERGING** |

Tier: **EMERGING (50-199)** — prototype validation milestone or follow-on contract → re-rate C 6→8 (composite 128); defense volume award → M 4→6 (composite ~192, HIGH watch).

## Status
- **emerging** (competitive award granted 2026-09-28; no 10 kV SiC IGBT in production yet).
- Moves to scaling on a validated-prototype milestone or follow-on procurement.

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| NVTS | sub-ceiling | Navitas Semiconductor | awardee; only named US fabless with 20+ yr UHV SiC pedigree + US-anchored manufacturing; extends beyond SiC MOSFETs into 10 kV SiC IGBTs | patented TAP (trench-assisted planar) architecture; US-anchored supply chain; ARL/DEVCOM selection edge | [2026-09-28] U.S. Government selects Navitas for ALATTIS 10 kV SiC IGBT program — VERIFIED |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| (class) | — | legacy HV-Si IGBT suppliers (Si IGBT class, mostly non-US or grid-tier incumbents) | if the 10 kV SiC IGBT process validates, Si IGBT content at ≥10 kV defense/infrastructure power tiers migrates to SiC | est. low (class, new voltage tier) | 0.3 (rumored) | est. <5 (low) | [2026-09-28] ALATTIS targets a process "not currently available domestically" — VERIFIED |

> **Honest note:** genuinely additive at the new voltage tier — no single tracked US ticker sits
> on a clean 10 kV Si-IGBT revenue line. No forced loser row; the class row is low-confidence only.

## Sequencing
- sequences-after → [DRIFT-002_gan-led-to-power.md](DRIFT-002_gan-led-to-power.md) (same power-semi
  materials-substitution arc; SiC/HV tier extends the GaN arc into UHV defense/infrastructure)
- enables → (none yet — follow-on defense HV-SiC volume would gate a 800V-rack/defense-power bridge; unfiled)
- competes-with → (foreign-sourced 10 kV SiC IGBT supply chain — procurement substitution is the domestic-process claim)

## Competitive/Substitution Links
- NVTS ↔ WOLF : substitution-rival (US SiC device tier; WOLF = integrated SiC + devices post-restructuring)
- NVTS ↔ ON : substitution-rival (SiC portfolio overlap, different voltage tiers)

## Cascade Hook
- Gap-phrase: **"10 kV SiC IGBT domestic process validation"**
- Surface forms: `10 kV SiC IGBT "prototype" OR "validation" OR "milestone"`, `ALATTIS "SiC" follow-on OR contract`,
  `domestic "silicon carbide" IGBT "10 kV" production`, `defense "high-voltage" SiC power semiconductor award`.
- Fires at Composite ≥ 500 (not near; re-rate path is award-milestone-driven).

## Evidence
- [2026-09-28] U.S. Government Selects Navitas to Develop Next-Generation 10 kV SiC Power Semiconductors (ALATTIS, ARL/DEVCOM, JETX-supported) — https://globenewswire.com/news-release/2026-09-28/3370264/0/en/u-s-government-selects-navitas-to-develop-next-generation-10-kv-sic-power-semiconductors.html (VERIFIED — primary press release)
- [2026-09-29] Navitas awarded U.S. Army program to develop 10kV SiC IGBTs and PiN diodes — https://powersemiconductorsweekly.com/2026-09-29/navitas-awarded-u-s-army-program-to-develop-10kv-sic-igbts-and-pin-diodes (VERIFIED — independent confirmation)
- [2026-09-29] Navitas awarded ALATTIS US Army project to develop 10kV power semiconductors — https://semiconductor-today.com/news_items/2026/sep/navitas-290926.shtml (VERIFIED — independent confirmation)

## Open questions / next-cycle checks
- Next prototype milestone / JETX review date (moves C 6→8 on validation).
- Any follow-on procurement or second-award (split-team) that would name a second US SiC winner.
- FMP NVTS segmentation is a single "Reportable Segment" (FY2024 $83.3M) — whole-company proxy until NVTS splits power-semi segments.

## Dated Evidence Notes
- [2026-10-31] [9ae3b6d1] Filed (A2 3rd-slot gate: sub-ceiling winner NVTS + competitive government award at pilot/design-win certainty + named process award). 10 kV SiC IGBT domestic-process substitution; additive at the new voltage tier, no clean US loser.

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-03 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-012.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| NVTS | winner | 100.0% (FY2024) [STALE] | 2.3 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Reportable Segment |

**Composite (M x T x C): 4 x 4 x 6 = **96** -> tier **EMERGING**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: pilot
  - timing_years: 4 | displacement_sub_class: additive
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: ALATTIS 10kV SiC IGBT domestic-process award (NVTS, 2026-09-28). Additive at new voltage tier; no clean US loser (class row only, low-confidence). FMP NVTS segmentation = single 'Reportable Segment' (FY2024 $83.3M) — whole-company proxy until NVTS splits power-semi segments.

## Last Updated (2026-10-31)

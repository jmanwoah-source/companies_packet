# DRIFT-005 — Air-cooling → liquid/immersion cooling as default at AI racks (architecture-substitution)

**Class.** architecture-substitution (cooling medium swap at the rack; air ceiling ~40-50kW/rack)
**Substitution.** Air-cooled racks (CRAC/precision air) → direct-to-chip / CDU / immersion liquid cooling as the DEFAULT (not premium) for AI-class racks
**Sector.** ai-infrastructure
**Secondary sectors.** semiconductors (power-density context), advanced-energy (PDU/switchgear last mile)
**Value-chain layer(s) affected.** thermal/cooling, data-center build (downstream)
**Horizon tag:** short (<3 yr to default status)
**Displacement sub-class:** architecture-reset (one-time content reset per build generation + steady-state run-rate — NOT a fake revenue-exposure %)

## Magnitude (mcap + revenue at stake)
- Every AI rack build now carries CDU/D2C/immersion content; the reset is one-time per generation
  plus steady-state service/refill run-rate. At-stake names are sub-ceiling: **VRT** (the pure
  play, mid cap), **SMCI** (mid cap, balance-sheet caveat lives in its dossier).
- Magnitude score = 7 ($3-10B class of build content shifting to liquid per the IEA-4E 2026
  liquid-cooling report's share trajectory).

## Timing (TRL → volume)
- TRL 8-9 (deployment volume underway; 2-3 yrs to default-status across campuses). Timing score = 6.

## Certainty
- **demonstrated** (volume shipped, hyperscaler reference designs live); default-vs-premium
  status is claimed, not contract-locked. Score = 8.

## Drift Score
| Component | Score (0-10) | Rationale |
| Magnitude | 7 | $3-10B-class build content shift; sub-ceiling names carry the edge |
| Timing | 6 | 2-3 yrs to default status |
| Certainty | 8 | volume demonstrated; default status claimed |
| **Composite** | **336** | **HIGH** |

Tier: **HIGH (200-499)** — promotes to CRITICAL (448+) on a named hyperscaler PPA specifying liquid-default campus-wide.

## Status
- **scaling** (volume deployments; reference designs default for AI-class racks).

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
| VRT | mid | Vertiv | liquid cooling + power delivery pure play; CDU/D2C/immersion full stack | reference-design moat with hyperscalers | [2026] Vertiv liquid-cooling options (D2C/CDU/immersion lines) — VERIFIED |
| SMCI | mid | Super Micro | rack-scale liquid-cooled systems | rack-scale integration (balance-sheet risk in dossier) | [2026-02] IEA-4E liquid-cooling report (sector trajectory) — VERIFIED |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
| (class) | — | legacy air-cooled CRAC / datacenter-HVAC incumbents | AI-rack share of HVAC revenue moves to liquid; air-ceiling caps new-build content | est. 10-30% of datacenter-HVAC revenue (fix via FMP next cycle) | 0.6 (claimed) | 6-18 (low-mid, low-confidence) | [2026-02] IEA-4E DC6 liquid-cooling final report — VERIFIED |
| (class) | — | air-cooling-only rack builders | no liquid line = excluded from AI-class rack bids | est. low-mid (class) | 0.6 (claimed) | est. 2-8 (low-mid) | [2026] IEA-4E report (cross-reference) — VERIFIED |

> **Loser-track note:** class-level, not a single ticker — the cleanest named air-cooling
> incumbent is not in the tracked universe. Fix next cycle: identify the listed CRAC/HVAC
> name with the highest datacenter share and file a named row.

## Sequencing
- enabled-by → [DRIFT-001_gaa-node-transition.md] (denser nodes → higher rack power → air ceiling breach)
- sequences-after → [sic_gan_power](../concepts/sic_gan_power.md) (800V rewire raises rack power density that forces liquid)

## Competitive/Substitution Links
- VRT → SMCI : substitution-rival (both ride the reset; VRT = component+system, SMCI = rack)
- (CRAC/HVAC class) → VRT : displaced (air content replaced by CDU/D2C)

## Cascade Hook
- Gap-phrase: **"liquid-cooling default hyperscaler PPA CDU content"**
- Surface forms: `"liquid cooling" default data center PPA`, `CDU OR "direct-to-chip" "reference design" hyperscaler`,
  `immersion cooling AI rack volume`, `air-cooled HVAC data center displacement liquid`.
- Fires at Composite ≥ 500 (watch the campus-wide PPA trigger).

## Evidence
- [2026-02] IEA-4E "Liquid cooling in Data Centres" final report (DC6) — https://www.iea-4e.org/wp-content/uploads/2026/02/EDNA-2026-LIQUID-COOLING-IN-DATA-CENTRES3.pdf (VERIFIED)
- [2026] Vertiv liquid cooling options for data centers — https://www.vertiv.com/en-us/solutions/learn-about/liquid-cooling-options-for-data-centers/ (VERIFIED)

## Open questions / next-cycle checks
- Name the listed CRAC/HVAC incumbent with highest datacenter share → convert the class row to a named loser.
- Confirm VRT liquid-cooling revenue % from the latest 10-Q (fix the winner content number).

## Dated Evidence Notes
- [2026-10-25] [seed005a] Filed from ai-infrastructure pillar validation (salvaged sub-agent evidence).

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-10-29 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-005.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| ETN | loser | 0.0% (FY2025) | 152.9 | 0.0% | Industrials -> downstream (industrial elec) / substrate | - |
| SMCI | winner | 56.2% (FY2026) | 22.6 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Server And Storage Systems |
| VRT | winner | 82.0% (FY2025) | 94.7 | - (upside) | Industrials -> downstream (industrial elec) / substrate | Product |

**Composite (M x T x C): 7 x 6 x 8 = **336** -> tier **HIGH**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: demonstrated
  - timing_years: 2 | displacement_sub_class: architecture-reset
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Named air-cooled CRAC incumbent not in tracked universe; ETN Electrical Americas/Global = representative data-center-elec exposure (class-level proxy, flagged).

## Last Updated (2026-10-25)

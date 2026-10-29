# DRIFT-007 — Human-in-loop C-UAS engagement → autonomous detect-and-kill (architecture-substitution)

**Class.** architecture-substitution (engagement decision moves from operator to on-board inference)
**Substitution.** Human-in-the-loop detection-to-engagement (operator confirms each kill decision) → on-board-inference autonomous detect-and-kill (sensor fusion + target recognition + engagement without human-in-loop)
**Sector.** physical-ai
**Secondary sectors.** —
**Value-chain layer(s) affected.** sensors/perception, C-UAS effectors (upstream of primes)
**Horizon tag:** medium (2-3 yr to standardization)
**Displacement sub-class:** content-per-unit (content-per-system + reprocurement-rate step; also carries a procurement-substitution element — budget re-pointing to unmanned platforms)

## Magnitude (mcap + revenue at stake)
- C-UAS is the pillar's new permanent budget line (DoD + NATO, funded category); autonomy raises
  content-per-system and the reprocurement rate (unmanned systems multiply vs manned platforms).
  Salvage evidence: AVAV $874M FMS IDIQ award (2026). Sub-ceiling asymmetric names: AVAV, DRS, RCAT.
- Magnitude score = 6 ($1-3B-class award flow per award cycle; NATO programs pending).

## Timing (TRL → volume)
- TRL 7 (autonomous target recognition in deployment-adjacent fielding; JRC 2026 review documents
  the detect-track-identify trajectory). 2-3 yrs to HIL-free standardization. Timing score = 5.

## Certainty
- **demonstrated at sensor level** (autonomous target recognition fielded in systems),
  **claimed at full detect-and-kill-without-HIL standardization**. Score = 6.
- Procurement note: FMS IDIQ vehicle = budget-cycle certainty, not tech demo.

## Drift Score
| Component | Score (0-10) | Rationale |
| Magnitude | 6 | $874M-class award cycles + NATO pending |
| Timing | 5 | 2-3 yrs to standardization |
| Certainty | 6 | sensors demonstrated; HIL-free standardization claimed |
| **Composite** | **180** | **EMERGING (upper band — one funding/standardization event from HIGH)** |

Tier: **EMERGING (50-199)** — a NATO award or DoD HIL-free standardization → C 6→9 → 270 → HIGH (auto re-rate).

## Status
- **emerging** (fielding-adjacent; no HIL-free standard yet).

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
| AVAV | sub-ceiling | AeroVironment | autonomous UAS + C-UAS systems; $874M FMS IDIQ award (2026) | program wins + unmanned portfolio | [2026] AVAV $874M FMS IDIQ award — VERIFIED |
| RCAT | sub-ceiling | (counter-UAS) | C-UAS engagement stacks | program lock-in | [2026] JRC140692 C-UAS tech trajectory — VERIFIED |
| DRS | sub-ceiling | DRS (counter-drone radar, C-UAS awards) | sensor+engagement integration | funded category + low incumbent concentration | [2026] sectors/physical-ai dossier cross-link — VERIFIED (cross-link) |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
| (class) | — | detect-only / soft-kill-only vendors (per concepts/counter_uas.md "DOOMED incumbent") | engagement-autonomy step bypasses detect-only revenue; HIL-free kills the operator-dependent model | est. mid-single-digit % (fix via FMP next cycle) | 0.6 (claimed) | est. 2-4 (low, low-confidence) | [2026] concepts/counter_uas.md displacement section — VERIFIED (cross-link) |

> **Loser-track note:** class-level until the named detect-only incumbent is pulled from
> counter_uas.md fillers — file a named row next cycle.

## Sequencing
- enabled-by → [counter_uas](../concepts/counter_uas.md) (funded category prerequisite)
- prerequisite-for → (industrial/autonomy spillover: AITX-class autonomy platforms — unfiled candidate)

## Competitive/Substitution Links
- AVAV → DRS/RCAT : substitution-rival (C-UAS program awards)
- (LMT/NOC/RTX primes) → AVAV/DRS : upstream-supplier (program integration tier funds the sub-system tier)
- AVAV ↔ (Anduril, PRIVATE) : substitution-rival (the FM-4 case: private co-winner — supplier-discovery cascade applies)

## Cascade Hook
- Gap-phrase: **"autonomous detect-and-kill counter-drone no human-in-loop award"**
- Surface forms: `"counter-drone" autonomous "award" OR "contract"`, `site:acq.osd.mil autonomous C-UAS`,
  `"human in the loop" removed counter-drone`, `autonomous target recognition fielding defense`.
- Private-winner rule (FM-4): Anduril(PRIVATE) is a co-winner → cascade on its *public
  suppliers* (edge-AI NPU + sensor component names) when the hook fires.
- Fires at Composite ≥ 500 (requires NATO award / standardization).

## Evidence
- [2026] AeroVironment awarded $874M Foreign Military Sales IDIQ — https://investor.avinc.com/news-releases/news-release-details/aerovironment-awarded-874m-foreign-military-sales-idiq-deliver (VERIFIED)
- [2026] EU JRC (JRC140692) Technical developments in counter-drone technology — https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140692/JRC140692_01.pdf (VERIFIED)

## Open questions / next-cycle checks
- Pull counter_uas.md filler list → name the detect-only incumbent loser row (FMP revenue line).
- Confirm AVAV IDIQ scope (C-UAS vs general UAS) from the full press release.

## Dated Evidence Notes
- [2026-10-25] [seed007a] Filed from physical-AI pillar validation (salvaged sub-agent evidence).

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-10-29 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-007.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| AVAV | winner | 18.4% (FY2026) | 7.0 | - (upside) | Industrials -> downstream (industrial elec) / substrate | UxS |
| DRS | winner | 0.0% (FY2024) [STALE] | 10.7 | - (upside) | Industrials -> downstream (industrial elec) / substrate | - |
| RCAT | winner | 50.0% (FY2023) [STALE] | 0.8 | - (upside) | Industrials -> downstream (industrial elec) / substrate | Consumer, Other Segments |

**Composite (M x T x C): 6 x 5 x 6 = **180** -> tier **EMERGING**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: claimed
  - timing_years: 3 | displacement_sub_class: cutoff
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: AVAV UxS = the autonomous-counter-UAS line (measurable). DRS Integrated Mission Systems = whole-program proxy. Procurement-substitution flavor (FMS IDIQ re-allocation).

## Last Updated (2026-10-25)

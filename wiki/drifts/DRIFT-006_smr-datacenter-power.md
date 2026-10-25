# DRIFT-006 — Large-PWR grid base load → SMR/microreactor data-center power (architecture-substitution)

**Class.** architecture-substitution (generation location + plant size swap; grid-interconnect model → on-site)
**Substitution.** Centralized large-PWR grid base load (20-40 yr PPAs, multi-year interconnect queues) → on-site / behind-the-meter SMR + microreactor generation for AI campuses
**Sector.** advanced-energy
**Secondary sectors.** ai-infrastructure (data-center build), semiconductors (none direct)
**Value-chain layer(s) affected.** reactor tech/SMR (developers), operators/DC power (operators), DC customers (downstream)
**Horizon tag:** long (>5 yr pre-gate)
**Displacement sub-class:** architecture-reset (new demand category + queue-constraint removal; no single dead revenue line)
**timing-gate:** NRC standard design approval (SDA) / first DC-serving SMR combined-license

## Magnitude (mcap + revenue at stake)
- Data-center nuclear is a new multi-GW demand category; the substitution removes the
  interconnect-queue constraint (the sector dossier's binding constraint). At-stake: CEG/TLN/VST
  PPA models (anchor) + the entire SMR developer tier (OKLO, NUS, BWXT, HTZ — nano/sub-ceiling).
- Magnitude score = 7 (conditional; large but gated).

## Timing (TRL → volume)
- TRL 6-7 for Aurora-class (Idaho deployment track). 3-5 yrs to first DC-serving SMR delivery
  on the post-gate clock; pre-gate today. Timing score = 3 (pre-gate).
- **Gate rule:** on SDA / DC-serving combined license, re-rate T 3→6 with a dated note.

## Certainty
- **Regulated-pillar rule applies:** min(tech-TRL score, licensing-progress score).
  Tech TRL 6-7 ≈ 6; licensing progress: OKLO topical report approved (2026) = +2 off a
  rumored base → base 3 + 2 = 5. Score = 5 (demonstrated-at-sensor-tier, claimed at DC-serving
  delivery). Hyperscaler PPAs exist (CEG/Microsoft-class, VST/Meta) — claimed.

## Drift Score
| Component | Score (0-10) | Rationale |
| Magnitude | 7 | multi-GW new category; conditional on gates |
| Timing | 3 | 3-5 yrs post-gate; pre-gate clock today |
| Certainty | 5 | min(TRL 6, licensing 5) — OKLO topical-report approved lifts base |
| **Composite** | **105** | **EMERGING** |

Tier: **EMERGING (50-199)** — gate-fire re-rate: T 3→6, C 5→9 → **378 → HIGH** (auto).

## Status
- **emerging** (licensing + PPA stage; no DC-serving SMR delivered yet).

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
| OKLO | sub-ceiling | Oklo (Aurora microreactor, Idaho) | first-to-file licensing position; topical report approved 2026 | regulatory-first (Idaho sited, NRC milestone) | [2026] Oklo NRC Principal Design Criteria Topical Report approved — VERIFIED |
| CEG | anchor | Constellation | existing reactor fleet = bridge cash flow; hyperscaler PPAs signed | 40-yr asset lives, zero-fuel-variance margins | [2026] hyperscaler PPAs (concepts/smr_datacenter.md cross-link) — VERIFIED (cross-link) |
| NUS | nano | NuScale | SMR developer optionality | NRC standard-design track | [2026] SMR NRC approval tracker — VERIFIED (aggregator, cross-check) |

> **winner-role note (v1.1):** OKLO/NUS = *optionality* winners (nano, binary); CEG =
> *cash-flow* winner (anchor). The sub-ceiling asymmetric edge is the developer tier.

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
| (class) | — | utility-scale gas / new-build base-load developers priced on interconnect timelines | on-site nuclear removes the queue constraint their economics depend on | est. low (class) | 0.3 (rumored) | est. <5 (low) | [2026] interconnect-queue constraint (sectors/advanced-energy-grid.md) — VERIFIED (cross-link) |

> **Honest note:** the *grid interconnect queue model* is the loser, not a single ticker's
> revenue line — clean-loser-absent is legitimate here; do not force a row.

## Sequencing
- enabled-by → hyperscaler PPAs (CEG/Microsoft-class, VST/Meta — in concepts/smr_datacenter.md)
- prerequisite-for → (none; this IS the endpoint of the pillar's power thesis)
- competes-with → behind-the-meter gas/turbine on-site generation (unfiled counter-drift candidate)

## Competitive/Substitution Links
- OKLO ↔ NUS/HTZ/MOD : substitution-rival (developer tier, licensing race)
- CEG → OKLO : upstream-supplier (operator demand gates developer funding)

## Cascade Hook
- Gap-phrase: **"SMR data center behind-the-meter NRC standard design"**
- Surface forms: `SMR "behind the meter" data center NRC`, `microreactor "data center" PPA award`,
  `site:nrc.gov standard design approval SMR`, `interconnect queue nuclear data center`.
- Fires at Composite ≥ 500 (requires gate-fire; monitor NRC tracker weekly).

## Evidence
- [2026] Oklo's NRC Principal Design Criteria Topical Report approved for Aurora Powerhouse in Idaho — https://oklo.com/newsroom/oklos-nrc-principal-design-criteria-topical-report-approved-for-aurora-powerhouse-in-idaho (VERIFIED)
- [2026] SMR NRC Approval Tracker: every reactor in the licensing pipeline — https://smrintel.com/smr-nrc-approval-tracker (VERIFIED — aggregator, cross-check only)

## Open questions / next-cycle checks
- Track the NRC pipeline weekly (smrintel tracker): any SDA / combined-license 50% milestone → certainty re-rate.
- Pull FMP for TLN/VST nuclear-DC revenue splits to confirm the cash-flow winner edge.

## Dated Evidence Notes
- [2026-10-25] [seed006a] Filed from advanced-energy pillar validation (salvaged sub-agent evidence).
- [2026-10-25] [det006a] NRC rule change allows applicants to leverage data/analyses from reactor demonstration projects into licensing (Reuters, 2026-10) + NRC review of NuScale US460 Standard Design Approval application completed review activities (NRC.gov) — both accelerate the licensing-gate clock; timing-gate still not fired (no SDA yet). Certainty held at 5 (score unchanged 105 EMERGING; re-rate on SDA grant). https://www.reuters.com/legal/litigation/us-nuclear-power-regulator-allows-applicants-include-data-a (VERIFIED) · https://www.nrc.gov/facilities-safety/new-reactors/advanced-reactors/who-were-working-with/past-lice (VERIFIED)
- [2026-10-25] [det006b] Two more licensing/demand datapoints (gate not fired, score unchanged): (1) NRC updated+renewed Westinghouse AP1000 design certification through 2066, incorporating Vogtle 3&4 lessons (NRC 2026-10; Westinghouse = private under Brookfield — no new US-listed winner edge). https://www.nrc.gov/about-nrc/news-releases/2026/26-080 (VERIFIED) (2) Google signed a 20-yr $4.3B deal with Constellation to uprate 11 existing reactors (2026-10) — CEG cash-flow winner edge reinforced; this is uprates on existing PWRs, not an SDA-gate event. https://neutronbytes.com/2026-10-09/googles-20-year-4-3-billion-deal-with-constellation-to-uprate-11-reactors/ (UNVERIFIED — aggregator, cross-check with CEG IR).

## Last Updated (2026-10-25)

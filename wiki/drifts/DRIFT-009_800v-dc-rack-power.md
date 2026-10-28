# DRIFT-009 — 54V busbar + multi-stage AC→DC rack power → 800V DC direct distribution (architecture-substitution)

**Class.** architecture-substitution (one-time rack power-architecture reset + steady-state run-rate on every new AI rack generation)
**Substitution.** 54V/48V busbar distribution with 3-4-stage AC→DC conversion (PDU + shelf rectifier + 48V→12V/5V board rails) → direct 800V DC rack distribution with fewer conversion stages per the OCP 800V DC standard
**Sector.** ai-infrastructure
**Secondary sectors.** semiconductors (power Si: GaN, digital power control)
**Value-chain layer(s) affected.** design/fabless (power Si: MPWR-class, MCHP, NVTS), downstream (industrial elec / PDU & busbar: GEV-class)
**Horizon tag:** near-mid (2-4 yr)
**Displacement sub-class:** architecture-reset (one-time content reset per rack generation + steady-state run-rate; NOT a fake revenue-exposure %)

## Magnitude (mcap + revenue at stake)
- Every AI rack generation resets the power-delivery content: 800V DC changes the Si content mix
  (GaN/SiC front-end share rises), adds digital power control + security IC content per rack, and
  displaces part of the legacy multi-stage converter / busbar content. Aggregate addressable
  market is the entire AI-rack power-delivery stack — well over $10B mcap of exposed incumbents,
  but realized exposure is conditional on hyperscaler adoption pace. Scored on potential: 6.

## Timing (TRL → volume)
- TRL 7-8: OCP 800V DC standard published; NVIDIA announced the 800VDC architecture direction;
  first reference designs shipped (Microchip+Navitas, 2026-10-05). Volume 800V DC racks expected
  2027-2029. 2-3 yr to meaningful volume. Timing score = 6.

## Certainty
- **demonstrated (pilot / reference design)**: dated, named reference-design shipping (Microchip
  dsPIC33AK + Navitas GaNFast NV6034, 800V→6V direct, ~96% efficiency target, 2,100 W/in³)
  (2026-10-05). No hyperscaler volume commitment published yet → below demonstrated-volume.
  Score = 5.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | 6 | full AI-rack power-delivery stack at stake; realized exposure conditional on adoption pace |
| Timing | 6 | reference designs now, volume 2027-2029 |
| Certainty | 5 | dated named reference design shipped; no volume commitment yet |
| **Composite** | **180** | **EMERGING** |

Tier: **EMERGING (50-199)** — one hyperscaler 800V DC rack-volume commitment flips certainty 5→8 → composite 288 → HIGH (auto re-rate).

## Status
- **emerging** (reference-design stage; OCP standardization in flight). Moves to `scaling` on the first hyperscaler 800V DC rack volume deployment.

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| MCHP | mid (est. $8-10B, wiki dossier mcap stale — verify via FMP) | Microchip Technology | dsPIC33AK digital power control + TA100 hardware security = the control/security layer of 800V DC rack power; reference design with OCP alignment | dsPIC share in industrial digital power; hardware security IP | [2026-10-05] Microchip/Navitas 800V-to-6V OCP reference design PR — VERIFIED |
| NVTS | sub-ceiling (est. $2-3B, verify via FMP) | Navitas Semiconductor | GaNFast 650V GaN FETs (NV6034) are the front-end device of direct 800V→6V conversion; system-level GaN packaging | GaN power Si share in DC-DC; EV+datacenter dual demand | [2026-10-05] same PR (16× NV6034 stacked half-bridge, 1MHz, 96% peak) — VERIFIED |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| (class) | — | legacy silicon final-stage / multi-stage DC-DC converter suppliers (MPWR-class incumbents in the 48V-rail stack) | stage count drops as 800V→6V direct conversion collapses the 48V→12V→5V rail chain | est. low-mid (class; no clean single ticker yet) | 0.6 (claimed — direction well established, per-incumbent exposure unmeasured) | est. <10 | [2026-10-05] Microchip/Navitas PR (stage consolidation) + [2026-10] energiesmedia 6-8% efficiency delta — UNVERIFIED per ticker |

> **Honest note:** partial architecture-reset, not a clean cutoff — the power-delivery market
> grows with rack count; the loser is the *stage-count* reduction inside the chain, which hits
> mid-rail SiC/silicon final-stage content. No single clean US-listed loser row yet; the class
> row stays off the short list until FMP fixes a specific incumbent's rail-chain exposure %.

## Sequencing
- sequences-after → [DRIFT-002_gan-led-to-power.md](DRIFT-002_gan-led-to-power.md) (GaN-on-Si power device scale-out is the input layer the 800V rewire consumes at the front end — cross-domain transfer reuse)
- competes-with → (continued 48V busbar + supercap rail extensions — the additive counter-path)
- enables → [DRIFT-005_liquid-cooling-default.md](DRIFT-005_liquid-cooling-default.md) (both are one-time AI-rack architecture resets stacking the same 2027-2029 reset window)

## Competitive/Substitution Links
- MCHP ↔ MPWR-class : substitution-rival (digital power control content per rack)
- NVTS → (WOLF / GaN-on-Si epi class) : upstream-supplier (GaN epiwafer input for power FETs)

## Cascade Hook
- Gap-phrase: **"800V DC rack power volume deployment hyperscaler"**
- Surface forms: `800V DC "rack power" hyperscaler deployment`, `"800VDC" reference design OR "volume" data center`, `"800V" power shelf OR PDU data center 2027`, `GaN "800V" front-end design win data center`.
- Fires at Composite ≥ 500 (not near; watch for a hyperscaler volume commitment → certainty re-rate).

## Evidence
- [2026-10-05] The Data Center Is Moving to 800V: Microchip and Navitas Are Enabling the Transition — https://www.microchip.com/en-us/about/news-releases/products/the-data-center-is-moving-to-800v-microchip-and-navitas-are-enabling-transition (VERIFIED)
- [2026-10] Data centers adopting 800 VDC power architecture as AI workloads drive (6-8% system efficiency vs AC-to-DC) — https://energiesmedia.com/data-centers-800-vdc-power-architecture/ (UNVERIFIED)

## Open questions / next-cycle checks
- First hyperscaler 800V DC rack-volume commitment (the timing/ certainty re-rate event).
- Pull MCHP industrial/automotive digital-power and NVTS datacenter-segment revenue splits via FMP to fix the exposure % on the loser class row.
- Whether the OCP 800V standard names a specific PDU/switchgear incumbent (would name a GEV-class loser edge).

## Dated Evidence Notes
- [2026-10-25] [seed009a] Filed from drift-scan leg A (query "800V DC data center architecture"): Microchip+Navitas 800V→6V OCP reference design (2026-10-05 PR) is the first dated, named commitment in the 800V rewire with two US-listed winners. INDEX.md Track D seed row "*(class)* legacy silicon final-stage power / 50V PoL/VRM — 800V rewire displacement" is now anchored to a real event.
- [2026-10-25] [det009a] Second dated 800V DC proof point, cooling side: Trane Technologies (TT, NYSE) demonstrated industry-first 800V DC chiller architecture with Eaton + Danfoss (lab PoC, 3.5 MW / 1,000-ton class, ~2% system-efficiency gain; claims 1.8 MW freed compute per 200 MW DC) — announced 2026-09-30, SWORDS Ireland. Extends the 800V rewire into the mechanical/cooling layer (downstream industrial-elec value-chain layer). TT is a new potential mid-cap winner row (anchor-adjacent; verify cap via FMP); lab PoC only → certainty stays demonstrated-pilot, no re-rate yet (no hyperscaler volume commitment). https://investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2026/Trane-Technologies-Demonstrates-Industry-First-800-Volt-Direct-Current-Chiller-for-Next-Generation-AI-Data-Centers/default.aspx (VERIFIED — fetched 2026-10-25)
- [2026-10-26] [det009b] Third dated 800V DC proof point, now co-developed with the OEM: Navitas + NVIDIA developed a 24 kW, 800 VDC-to-12 VDC power delivery board (PDB) for the NVIDIA MGX ecosystem — single-stage 800V→12V conversion explicitly eliminating the conventional 50V IBC stage, 16× NV6034 GaNFast 650V FETs (stacked half-bridge), 97% full-load efficiency target, >2,000 W/in³, NVIDIA 400×60 mm form factor; to be showcased at the 2026 OCP Global Summit. Follows the 20 kW 800V→6V board debuts at GTC 2026. This is OEM co-development, not yet a hyperscaler volume rack deployment → certainty held at 5, score unchanged 180 EMERGING. NVTS upside edge reinforced (the PDB IS the NV6034 line in product form). https://www.powerelectronicsnews.com/navitas-nvidia-develop-24-kw-800v-to-12v-power-board/ (VERIFIED — fetched 2026-10-26)

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-10-28 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-009.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| MCHP | winner | 96.5% (FY2026) | 42.5 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Semiconductor Products Member |
| MPWR | loser | 94.4% (FY2023) [STALE] | 59.0 | 56.6% | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | DC To DC Products |
| NVTS | winner | 0.0% (FY2024) [STALE] | 2.4 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |

**Composite (M x T x C): 6 x 6 x 5 = **180** -> tier **EMERGING**
  - Mcap at stake: $55.7B (engine sum of loser exposure x mcap unless curated) | certainty_grade: claimed
  - timing_years: 2 | displacement_sub_class: architecture-reset
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: 800V rewire: stage-count collapse hits the 48V-rail multi-stage incumbents. MPWR DC-To-DC = the exposed final-stage line (engine sub_downside, claimed weight). NVTS segment line too thin to measure (single $0.1B reportable segment) -> upside row stays qualitative.

## Last Updated (2026-10-25)

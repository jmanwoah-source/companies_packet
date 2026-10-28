# DRIFT-008 — Copper (SerDes/ELSFP) → co-packaged optics / integrated photonics at the scale-out interconnect layer (architecture-substitution)

**Class.** architecture-substitution (interconnect medium swap at the intra-rack/scale-out layer)
**Substitution.** Copper interconnects (SerDes cores in ASICs + ELSFP-class pluggable copper) → co-packaged optics (CPO) / integrated silicon photonics for AI scale-out
**Sector.** ai-infrastructure
**Secondary sectors.** semiconductors (silicon photonics foundry + IP)
**Value-chain layer(s) affected.** photonics/interconnect, edge-AI silicon
**Horizon tag:** medium (2-3 yr to scale-out default)
**Displacement sub-class:** cutoff (copper content per GPU cluster dies as CPO takes the scale-out path) + content-per-unit (optics content-per-rack rises)

## Magnitude (mcap + revenue at stake)
- Broadcom (AVGO, named): "Copper interconnects, driven by SerDes cores integrated inside ASICs, are
  no longer able to keep pace with the bandwidth, data rate" of scale-out (Oct 2026). Ayar Labs
  (PRIVATE) hosted a CPO Summit to align the ecosystem around *manufacturability* — "Scaling
  Co-Packaged Optics for the Next Era of AI Infrastructure" (EE Times, 2026).
- The asymmetric edge is the photonics small/mid tier: **MRVL** (silicon photonics, mid),
  **COHR** (mid), **IIVI** (sub-ceiling); AVGO is the >ceiling anchor. The copper/ELSFP
  suppliers are the loser class.
- Magnitude score = 7 ($3-10B-class interconnect content shifting from copper to optics per
  GPU cluster generation).

## Timing (TRL → volume)
- TRL 7-8: CPO "moves from promise to production planning" (EE Times); Broadcom shipping
  integrated optics; 2-3 yrs to scale-out default. Timing score = 6.

## Certainty
- **demonstrated** (named shipments + ecosystem manufacturability alignment) but
  scale-out-default status is claimed, not yet a whole-campus spec. Score = 7.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | 7 | interconnect content-per-cluster shift; sub-ceiling photonics names carry the edge |
| Timing | 6 | 2-3 yrs to scale-out default |
| Certainty | 7 | named shipments + ecosystem alignment; default status claimed |
| **Composite** | **294** | **HIGH** |

Tier: **HIGH (200-499)** — promotes to CRITICAL (≥448) on a named hyperscaler CPO-default campus spec.

## Status
- **scaling** (production planning; ecosystem aligned). Moves to `deployed` at CPO scale-out default.

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| AVGO | >ceiling | Broadcom | named integrated-photonics shipments; copper "no longer able to keep pace" | ASIC+optics integration IP | [2026-10] Broadcom: Scaling AI Infrastructure with Integrated Optics — VERIFIED |
| MRVL | mid | Marvell | silicon photonics scale-out | foundry + IP + packaging integration | [2026] sector dossier cross-link (photonics tier) — VERIFIED (cross-link) |
| COHR | mid | Coherent | optical components + CPO transition | component breadth (rides both copper and optics — watch net position) | [2026] sector dossier cross-link — VERIFIED (cross-link) |
| IIVI | sub-ceiling | II-VI/Coherent-class optical components | optical-component content step | materials + component moat | [2026] sector dossier cross-link — VERIFIED (cross-link) |
| (private) | — | Ayar Labs | CPO manufacturability leader; hosted the CPO Summit | TFL (tied-photonics) IP + ecosystem alignment | [2026] EE Times: CPO Moves from Promise to Production Planning — VERIFIED |

> **FM-4 private-winner rule:** Ayar Labs is a PRIVATE co-winner → when this drift cascades
> (Composite ≥ 500), the hook fires on Ayar's *public* suppliers (edge-NPU/sensor/component
> names) via the upstream-supplier edges.

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| (class) | — | copper / ELSFP-class interconnect suppliers (Molex named as the ELSFP incumbent) | copper content per cluster dies as CPO takes the scale-out path | est. 15-30% of the interconnect line (fix via FMP next cycle) | 0.6 (claimed) | 9-18 (low-mid, low-confidence) | [2026] Molex: Beyond 224G, co-packaged copper (ELSFP) — VERIFIED |
| (class) | — | discrete SerDes-only ASIC interconnect vendors | SerDes cores displaced by integrated photonics | est. low-mid (class) | 0.6 (claimed) | est. 2-9 (low-mid) | [2026] Broadcom article (cross-reference) — VERIFIED |

> **Loser-track note:** Molex is the named copper/ELSFP incumbent but is not in the tracked
> universe (no dossier) → stays a class row on the short list; name the listed pluggable-copper
> incumbent with the highest datacenter share next cycle to file a named row. COHR/LITE are
> TRANSITIONERS (ride copper now, optics next) — their net_drift_position is "mixed," not loser.

## Sequencing
- enabled-by → [DRIFT-005_liquid-cooling-default.md](DRIFT-005_liquid-cooling-default.md) (higher rack density → higher interconnect bandwidth → copper ceiling breach)
- enabled-by → [DRIFT-001_gaa-node-transition.md](DRIFT-001_gaa-node-transition.md) (denser AI dies → more interconnect content per cluster)
- prerequisite-for → (CPO→intra-chip optical I/O; the next frontier, unfiled candidate)

## Competitive/Substitution Links
- MRVL ↔ COHR : substitution-rival (both silicon photonics; competing for the same scale-out content)
- (Molex/ELSFP class) → AVGO/MRVL/COHR : displaced (copper content replaced by integrated optics)
- IIVI/COHR → MRVL/AVGO : upstream-supplier (optical components to the CPO makers)

## Cascade Hook
- Gap-phrase: **"co-packaged optics scale-out default silicon photonics"**
- Surface forms: `co-packaged optics "production" OR "default" scale-out`,
  `site:broadcom.com OR site:marvell.com integrated optics AI`, `copper interconnect replace optics GPU cluster`,
  `CPO "tied photonics" OR "optical engine" volume`.
- Private-winner rule (FM-4): fires on Ayar Labs' public suppliers at Composite ≥ 500.
- Fires at Composite ≥ 500 (not near; watch the hyperscaler CPO-default campus spec).

## Evidence
- [2026-10] Broadcom: Scaling AI Infrastructure with Integrated Optics (copper "no longer able to keep pace") — https://www.broadcom.com/company/news/articles/optics/scaling-ai-infrastructure-with-integrated-optics (VERIFIED)
- [2026] EE Times: Co-Packaged Optics Moves from Promise to Production Planning (Ayar Labs CPO Summit) — https://www.eetimes.com/co-packaged-optics-moves-from-promise-to-production-planning/ (VERIFIED)
- [2026] Molex: Beyond 224G, co-packaged copper / ELSFP (the copper incumbent's response) — https://www.molex.com/en-us/blog/future-of-co-packaged-copper (VERIFIED)

## Open questions / next-cycle checks
- Confirm a named hyperscaler CPO-default campus spec (the CRITICAL trigger).
- Pull FMP interconnect/optics revenue split for COHR/LITE to fix the transiter net position.
- Name the listed pluggable-copper incumbent with the highest datacenter share → file a named loser row.

## Dated Evidence Notes
- [2026-10-25] [seed008a] Filed by the Drift Detector judgment leg (candidate #22/23, DRIFT-008).
- [2026-10-27] [0ce737f4] Second production proof point (PECC Summit, 2026-10-20): NVIDIA Dan Kuchta — CPO in production AI networking with silicon-photonic microring modulators + high-power external lasers + detachable fiber; Spectrum-X Ethernet Photonics switches claim 5x power efficiency and 10x MTBI vs pluggable-transceiver switches; pluggables (USFP, w/ Cisco 2026-10-12) AND copper explicitly remain in the roadmap (448 Gb/s-class copper) — architecture boundary, not cutoff. Status/scoring unchanged (scaling, 294 HIGH); status line already anticipates CPO scale-out production as the trigger — this confirms CPO scale-out production but copper-in-rack retention means cutoff sub-class is partial; no re-rate this cycle. https://convergedigest.com/nvidia-kuchta-pecc-cpo-npo-optics-serviceability/ (VERIFIED — search-confirmed, Oct 20 2026)
- [2026-10-27] [8eba2808] Corroborating proof point (Hot Interconnects 2026): NVIDIA Gilad Shainer — Spectrum-X Ethernet Photonics CPO "now in production", built on TSMC COUPE packaging + NVIDIA microring modulators; optical scale-out approaching ~10% of compute power consumption in large AI systems; copper retained aggressively for short-reach Scale Up, CPO for Scale Out. Same drift, second OEM confirmation; no new named winner/loser edges (NVDA is the integrator, not a tracked winner row; MPWR loser line unchanged). https://convergedigest.com/hot-interconnects-nvidia-gilad-shainer-gigascale-ai-factory-network-architecture/ (VERIFIED — search-confirmed)
- [2026-10-28] [apc054c1] Standards milestone (A2 leg candidate #54): Advanced Photonics Coalition (60 member orgs: foundries, PIC makers, laser/packaging/test suppliers) released its full specification portfolio 2026-10-20 at the PECC Summit — CPO system-level architecture overview, CPO recommended practices, silicon-photonic manufacturing spec, 4-core multicore fiber/FAU spec, CPO test practices. Stated goal: remove implementation variation + supply-chain silos to drive high-volume, lower-cost photonics manufacturing for AI/data center. This is an ecosystem-level adoption gate (standards de-risking volume CPO), not a new substitution — same DRIFT-008 drift, third corroboration of the CPO scale-out timeline. No re-rate (status scaling, cutoff-partial sub-class unchanged); note only. https://prnewswire.com/news-releases/advanced-photonics-coalition-announces-portfolio-of-specifications-and-best-practice-documents-to-accelerate-high-volume-manufacturing-of-optical-networking-gear-302913234.html (VERIFIED — search-confirmed, 2026-10-20)

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-10-28 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-008.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| AVGO | winner | 57.7% (FY2025) | 1679.4 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Semiconductor Solutions |
| COHR | winner | 74.1% (FY2026) | 47.2 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Datacenter & Communications |
| IIVI | winner | 74.1% (FY2026) | 30.5 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Datacenter & Communications |
| MPWR | loser | 94.4% (FY2023) [STALE] | 59.5 | 94.4% | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | DC To DC Products |
| MRVL | winner | 74.4% (FY2026) | 220.4 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Data center |

**Composite (M x T x C): 7 x 6 x 7 = **294** -> tier **HIGH**
  - Mcap at stake: $56.2B (engine sum of loser exposure x mcap unless curated) | certainty_grade: demonstrated
  - timing_years: 2 | displacement_sub_class: cutoff
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Molex (named ELSFP incumbent) not in tracked universe. MPWR DC-To-DC = the silicon final-stage/interconnect power line displaced by CPO scale-out (US-listed proxy; ~10% of MPWR revenue -> engine sub_downside lands in low band, honest).

## Last Updated (2026-10-25)

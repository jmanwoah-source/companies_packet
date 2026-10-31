# DRIFT-011 — CoWoS silicon-interposer supply concentrated in TSMC's own fabs → first U.S.-based silicon-interposer manufacturing (GF for TSMC CoWoS) at the advanced-packaging manufacturing layer (manufacturing-scale)

**Class.** manufacturing-scale
**Substitution.** Si-interposer manufacturing for the CoWoS advanced-packaging ecosystem concentrated in TSMC-owned capacity → multi-year contracted U.S.-based interposer manufacturing at GlobalFoundries Malta, NY as the first US source (incl. embedded deep-trench-cap components)
**Sector.** semiconductors
**Secondary sectors.** ai-infrastructure (CoWoS = the AI/HPC packaging substrate)
**Value-chain layer(s) affected.** manufacturing (foundry), downstream (adv packaging + optical I/O substrate)
**Displacement sub-class:** additive (new contracted capacity with a named customer; score on new spend — no US-listed incumbent interposer maker is displaced, so no clean loser)

## Magnitude (mcap + revenue at stake)
- The named winner GFS (market cap ~$23B per FMP profile-symbol, mid cap-band) signs a multi-year
  initial $2B agreement (5-year initial term with expansion framework) to manufacture silicon
  interposers — including embedded deep-trench capacitor (eDTC) content — for TSMC's CoWoS
  ecosystem, with volume ramp at Malta, NY expected H1 2028. That is ~$400M/yr of new,
  contracted revenue against ~$6-7B of GF total revenue (~5-15% revenue-exposure class, scored
  6 on the rubric: $1-3B-class mcap at stake / 5-15% revenue exposure).
- Magnitude also carries the supply-chain-security layer: this is the FIRST US-based source of
  interposers for the CoWoS ecosystem — the substrate under the entire AI/HPC chiplet stack —
  which makes the contracted dollars a floor, not a ceiling (the agreement "provides a
  foundation to expand capacity over time as customer demand grows").
- Loser side: no clean US-listed loser. TSMC is the customer (and non-US-listed in the US sense);
  GF is the seller. Displacement, if any, is of intra-TSMC interposer fab allocation, not of a
  US-listed incumbent's revenue line. Per the quality bar: **additive, no clean loser** — not forced.

## Timing (TRL → volume)
- TRL 9 for the product (Si interposers + eDTC are already in TSMC's CoWoS volume flow); the
  substitution is the *manufacturing location/contract* swap, not a technology demo.
- Named milestone: volume production ramp at Malta during **H1 2028** → 2 years to volume.
- Timing score = 8.

## Certainty
- **demonstrated (contract)**: signed manufacturing agreement announced 2026-10-08 at GF's
  primary IR source (gf.com), Malta NY, 5-year initial term, $2B initial value, named customer
  (TSMC), named facility, named ramp date. No ambiguity — this is a contracted revenue line.
- Score = 7 (demonstrated pilot/contract band; not yet volume production, hence not 9-10).

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | 6 | $2B contracted / ~$400M-yr new revenue vs ~$23B winner mcap; 5-15% revenue-exposure class; floor not ceiling |
| Timing | 8 | volume ramp H1 2028 = 2 years |
| Certainty | 7 | signed multi-year contract, named customer + facility + ramp date (contract-demonstrated, pre-volume) |
| **Composite** | **336** | **HIGH** |

Tier: **HIGH (200-499)** — track; next-cycle re-check. Re-rate to CRITICAL if the expansion
framework is exercised (term/value growth) or a second US interposer site is contracted.

## Status
- **scaling** (signed contract with named ramp date; production has not started). Moves to
  `deployed` at the H1 2028 Malta volume ramp.

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| GFS | mid | GlobalFoundries | first US-based manufacturer of CoWoS silicon interposers (incl. eDTC) under a $2B multi-year TSMC manufacturing agreement; Malta NY dedicated fab expansion | US domestic manufacturing footprint (security premium) + TSMC anchor customer + eDTC process depth; expansion framework = optionality | [2026-10-08] GF press release (gf.com) — VERIFIED (page fetched 2026-10-30) |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| (class) | — | intra-TSMC interposer fab allocation (TSMC = customer, not a US-listed loser) | contracted interposer volume moves to the US supply chain | n/a (no US-listed incumbent displaced) | — | — | [2026-10-08] GF press release (gf.com) — VERIFIED (page fetched 2026-10-30) |

> **Loser-track note:** ADDITIVE — no clean US-listed loser in this drift; the displaced capacity
> is intra-TSMC allocation, and TSMC is the customer. Stated explicitly per the schema; no US
> loser row is forced.

## Sequencing
- sequences-after / enabled-by → [DRIFT-008_copper-to-cpo.md](DRIFT-008_copper-to-cpo.md) (CPO/CoWoS
  ecosystem scale-up is what makes US interposer security a priority)
- competes / related → [DRIFT-010_asml-d2w-hybrid-bonding.md](DRIFT-010_asml-d2w-hybrid-bonding.md)
  (D2W hybrid bonding would change the interconnect content inside the same packaging stack —
  interposer vs. bonded-stack substitution inside CoWoS-class packages)
- enabled-by → [DRIFT-001_gaa-node-transition.md](DRIFT-001_gaa-node-transition.md) (HBM/chiplet
  density growth = the demand that sizes the interposer line)

## Competitive/Substitution Links
- GFS → (TSMC interposer fabs class) : upstream-supplier (GF sells interposer manufacturing to TSMC)
- GFS → (US adv-packaging OSAT class: AMKR, PLAB) : substitution-rival (GF's US interposer content
  sits adjacent to the US OSAT/advanced-packaging complex; watch for AMKR interposer exposure)

## Cascade Hook
- Gap-phrase: **"US silicon interposer capacity ramp"**
- Surface forms:
  - `silicon interposer "volume production" 2028 Malta`
  - `GlobalFoundries TSMC interposer expansion capacity`
  - `embedded deep trench capacitor interposer US fab`
  - `site:gf.com interposer capacity expansion`
- Fires at Composite ≥ 500 (not near at 336; triggers = expansion-framework exercise / second US
  site / named AMKR/OSAT interposer content).

## Evidence
- [2026-10-08] GlobalFoundries: "GlobalFoundries reaches agreement to establish U.S.-based supply
  of silicon interposers for advanced AI packaging" — multi-year $2B agreement with TSMC for
  CoWoS silicon interposers (incl. embedded deep-trench capacitor components), Malta NY, volume
  ramp H1 2028, 5-year initial term with expansion framework —
  https://gf.com/news-and-events/news/globalfoundries-reaches-agreement-to-establish-us-based-supply-of-silicon-interposers-for-advanced-ai-packaging/
  (VERIFIED — primary source page fetched 2026-10-30)

## Open questions / next-cycle checks
- FMP check: GFS revenue-product-segmentation returns a single coarse line
  ("Engineering And Other Pre-Fabric Services", $769M FY2025) — no interposer segment yet;
  engine matches on sector. Re-check when GF breaks out advanced-packaging/interposer revenue.
- Watch for expansion-framework exercise (second term/site) — the CRITICAL re-rate trigger.
- AMKR / PLAB: any disclosed interposer manufacturing content that would create the first
  US-listed loser edge if GF's US capacity crowding reprices OSAT interposer work?

## Dated Evidence Notes
- [2026-10-30] [bcca6f6d] Filed by the Drift Detector judgment leg (Leg A candidate,
  "advanced packaging replaces node scaling" query; 1 page fetch to primary source; no web
  searches needed). 1 of 2 base slots used.

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-10-31 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-011.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| GFS | winner | 100.0% (FY2025) | 23.0 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Engineering And Other Pre-Fabrication Services |

**Composite (M x T x C): 6 x 8 x 7 = **336** -> tier **HIGH**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: pilot
  - timing_years: 2 | displacement_sub_class: additive
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: GFS-only named winner (mid, ~$23B FMP profile mcap): $2B multi-year TSMC contract for US-based CoWoS silicon interposers (incl. eDTC) at Malta NY, volume ramp H1 2028. Additive — no clean US-listed loser (displaced capacity is intra-TSMC allocation; TSMC is the customer). DATA-QUALITY: FMP revenue-product-segmentation for GFS FY2025 returns a single coarse line (Engineering And Other Pre-Fabric Services, $769M) with no interposer/adv-packaging segment — engine matches on sector (Technology/Semiconductors).

## Last Updated (2026-10-30)

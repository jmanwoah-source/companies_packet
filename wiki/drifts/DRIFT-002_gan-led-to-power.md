# DRIFT-002 — GaN-on-sapphire LED epi → GaN-on-Si power epi (cross-domain-transfer)

**Class.** cross-domain technology transfer (a material/process from one market cracks a new one)
**Substitution.** GaN-on-sapphire LED epitaxial wafers (solid-state lighting) → GaN-on-Si power epitaxial wafers (power-switching devices)
**Sector.** semiconductors (wide-bandgap / power)
**Secondary sectors.** ai-infrastructure (800V power-rack content)
**Horizon tag:** short (deployed)
**Displacement sub-class:** cutoff (LED substrate moat line displaced; silicon final-stage gradual)
**Value-chain layer(s) affected.** substrate/materials, design/fabless (power), manufacturing

## Magnitude (mcap + revenue at stake)
- The LED industry's MOCVD GaN-epitaxy toolsets + idle capacity transferred into power.
  GaN-on-Si substrate market >$300M by ~2019; GaN power device business >$1B post-2019.
- The clean proof: **Cree divested its LED Products business (Mar 2021, to SMART/CreeLED)** and
  renamed **Wolfspeed (Oct 2021)** to focus SiC/GaN power — the substrate moat that LED R&D
  built became a power-electronics moat.
- Exposed tickers (sub-ceiling leverage present): **WOLF** (SiC/GaN substrate+device), **SWKS**
  (GaN power pure-play), **ON** (EliteSiC + GaN), **NVTS** (NVIDIA 24kW 800V board — rides the
  transferred demand), **SMART** (CreeLED, the lighting side that kept LED capacity).

## Timing (TRL → volume)
- TRL 9 — **deployed**. GaN-on-Si 6" available, 8" in qualification at time of transfer; CreeLED
  LED divestiture executed Mar 2021; corporate name change Oct 2021. Volume shipping.
- Years-to-volume: 0 (already volume). Timing score = 10.

## Certainty
- **demonstrated** (shipped + executed divestiture + SEC filings). Proof point: Cree/Wolfspeed
  10-K (Mar 2021 LED divestiture to SMART/CreeLED; Oct 2021 CREE→WOLF rename). Score = 10.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | 6 | substrate >$300M + device >$1B; sub-ceiling names carry the edge |
| Timing | 10 | already deployed / volume |
| Certainty | 10 | executed divestiture + SEC filings |
| **Composite** | **600** | **CRITICAL** |

Tier: **CRITICAL (500-1000)** — but this is a **retroactive/deployed** drift: the score is high
because it's *proven*. The action is the *next layer* (who owns the substrate moat vs the
LED-incumbent capacity), used here to prove the schema captures a completed substitution with
both edges intact.

## Status
- **deployed** (complete; reference anchor for what a finished cross-domain transfer looks like).

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| WOLF | sub-ceiling | Wolfspeed (ex-Cree) | owns the SiC/GaN substrate+epi moat that LED R&D built; Infineon RF GaN-on-SiC acquisition (2019) | 30x capacity expansion plan, crystal-growth yield, end-to-end SiC corridor | [2021-10] CREE→WOLF rename; LED divestiture (SEC 10-K) — VERIFIED |
| SWKS | mid | Skyworks (GaN power) | rode the LED→power GaN transfer as a pure-play | fabless asset-light + design-wins | [2022] GaN-on-Si 6"/8" qualification (powerwaywafer) — VERIFIED |
| ON | anchor | onsemi | EliteSiC + GaN; qualification moat | part count + auto/industrial qualification | [2022] Wolfspeed design-ins $2.1B H1 (sec.gov R9) — VERIFIED |
| NVTS | sub-ceiling | Navitas | NVIDIA 24kW 800V board — rides the transferred power demand | design-win + reference design | [2026] NVIDIA 24kW board (concepts/sic_gan_power.md) — VERIFIED (cross-link) |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| SMART | sub-ceiling | SMART Global (CreeLED) | kept the LED lighting side but lost the substrate/epi moat to the power spin | ~100% of its GaN epi line is lighting-bound | 1.0 (demonstrated) | ~100 | [2021-03] Cree LED divestiture to SMART/CreeLED (SEC 10-K) — VERIFIED |
| (class) | — | legacy silicon final-stage power (silicon PoL/VRM / LDMOS suppliers) | revenue cannibalized by GaN/SiC switching efficiency | n/a (class, not a single ticker) | 0.6 (claimed) | est. low-mid | [2026] 800V rewire substitutes silicon final-stage (sic_gan_power.md) — VERIFIED (cross-link) |

> **Why this is the reference anchor:** it is the *cleanest* completed substitution in the
> portfolio — a real, dated, SEC-filed winner (WOLF kept the moat) and a real loser (SMART/CreeLED
> kept the lighting capacity, lost the substrate moat), plus a displaced legacy class (silicon
> final-stage). It proves the schema captures both edges of a finished drift.

## Sequencing
- enables → [sic_gan_power](../concepts/sic_gan_power.md) (GaN-on-Si substrate supply gates the 800V DC rewire)
- competes-with → DRIFT-003 (SiC substrate scaling is the parallel materials path)

## Competitive/Substitution Links
- WOLF → SMART : displaced (substrate moat left the LED business)
- WOLF → SWKS/ON/NVTS : upstream-supplier (substrate feedstock to power device makers)
- ON ↔ NVTS : substitution-rival (both GaN/SiC 800V content, competing for the same power-rack content)

## Cascade Hook
- Gap-phrase: **"GaN-on-Si epiwafer power device design win"**
- Surface forms: `GaN-on-Si "power" "design win" OR "qualification"`,
  `site:patents.google.com GaN power epitaxy on silicon`, `"GaN" power "8-inch" wafer volume`,
  `LED GaN epi capacity "power electronics" repurpose`.
- Retroactive: already filed; hook retained for the *next layer* (new GaN-on-Si substrate entrants
  and 8-inch GaN-on-Si volume adoption).

## Evidence
- [2021-10-04] Cree→Wolfspeed rename; LED Products divestiture to SMART/CreeLED (Mar 2021) — https://www.sec.gov/Archives/edgar/data/895419/000089541922000055/R9.htm (VERIFIED)
- [2021-10-04] Cree acquires Infineon RF GaN-on-SiC business (€345M) — https://www.wolfspeed.com/company/news-events/news/cree-acquires-infineon-rf-power-business/ (VERIFIED)
- [2022-01-31] Wolfspeed revenue +11% Dec qtr; 150mm SiC substrate demand strong — https://www.semiconductor-today.com/news_items/2022/jan/wolfspeed-310122.shtml (VERIFIED)
- [2019] GaN-on-Si 6" available, 8" in qualification; substrate >$300M by 2019 — https://www.powerwaywafer.com/gan-power-electronics-will-top-one-billion-dollar-in-revenue-in-a-couple-of-years-thanks-to-a-cross-fertilization-with-the-led-industry.html (VERIFIED)

## Open questions / next-cycle checks
- Confirm 8-inch GaN-on-Si volume-adoption date (the parameter powerwaywafer called the obvious tech choice).
- Pull FMP for WOLF current revenue split (materials vs devices) post-bankruptcy-restructuring.
- Check whether any new 8" GaN-on-Si substrate entrant has appeared (the next-layer cascade target).

## Dated Evidence Notes
- [2026-10-25] [seed002a] Seeded as the reference anchor for a completed cross-domain transfer (LED→power GaN-on-Si).
- [2026-10-25] [det002a] 8-inch GaN-on-Si next-layer entrant signal: Polar Semiconductor (PRIVATE, Bloomington MN) + IC-Link by imec announced 8-inch production of e-mode GaN devices via an imec GaN-on-Si process/device/epitaxy license transfer (2026-10-13). Directly answers the open question "any new 8-inch GaN-on-Si entrant?" — a non-US-privately-held foundry entering the 8-inch GaN-on-Si substrate/device layer. No new US-listed winner (Polar is private); WOLF/ON/NVTS exposure unchanged. Not a new drift (same substitution, existing winner/loser edges). https://www.businesswire.com/news/home/20261012027647/en/Polar-Collaborates-with-IC-Link-by-imec-to-Manufacture-8-inch-GaN-Technology/ (VERIFIED) · https://www.semiconductor-today.com/news_items/2026/oct/polar-iclink-131026.shtml (VERIFIED)

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-10-27 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-002.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| NVTS | winner | 0.0% (FY2024) [STALE] | 2.2 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |
| ON | winner | 46.8% (FY2025) | 28.8 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | PSG |
| SMART | loser | n/a (no matching segment data) | ? | n/a | None -> ? (unmapped) | - |
| SWKS | winner | n/a (no matching segment data) | 12.5 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |
| WOLF | winner | 100.0% (FY2025) | 1.2 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Power Products |

**Composite (M x T x C): 6 x 10 x 10 = **600** -> tier **CRITICAL**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: demonstrated
  - timing_years: 0.5 | displacement_sub_class: cutoff
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Reference anchor (Cree LED divestiture 2021). ON PSG = power-semiconductor segment (cleanest GaN-power exposure measurable in the tracked set). SMART: FMP profile returns null (delisted/illiquid) -> stale row, hand estimate from the drift file stands.

## Last Updated (2026-10-25)

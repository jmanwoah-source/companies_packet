# DRIFT-001 — FinFET → GAA (gate-all-around) at 2nm-class nodes (process-node)

**Class.** process-node / manufacturability shift (a cheaper, higher-yield path to fine pitch)
**Substitution.** FinFET (fin field-effect) transistor → GAA / gate-all-around (nanosheet) transistor at 2nm-class (TSMC N2/N2P, Intel 18A)
**Sector.** semiconductors
**Secondary sectors.** ai-infrastructure (higher power density per die feeds the rack rewire)
**Horizon tag:** medium (3-5 yr to A16 HVM)
**Displacement sub-class:** content-per-unit (tool intensity per wafer, additive)
**Value-chain layer(s) affected.** tools (fab/litho), manufacturing (foundry)

## Magnitude (mcap + revenue at stake)
- The 2nm→GAA step is a **structurally higher tool-intensity cycle across EVERY tool category**
  (more etch, deposition, metrology, ALD/PECVD content-per-wafer). This is the live catalyst of
  the 2026 WFE structural upcycle.
- 2026 WFE consensus: Bernstein $148B (+26% YoY), BofA $150-160B (+30% YoY), Mizuho $153B
  (raised from $142B); bull case to $290B. KLA backlog >$12B; LRCX EPS +56% in one year.
- Exposed tickers: **AMAT, LRCX, KLAC, ASML** — all large-cap (>$150B; >the ~$300B wiki ceiling),
  so the *asymmetric* small/mid leverage is the **metrology/etch/deposition content-per-wafer**
  rise, not the anchor names. Honest flag: the at-stake mcap is real but mostly anchored in
  large-cap WFE; the quant edge is the tool-intensity step, not a pure small-cap node play.

## Timing (TRL → volume)
- TRL 8-9 (operational; first volume shipping). TSMC 2nm HVM began 2025; TSMC 2nm **trial
  production Sept 2026** (AMAT GAA ALD/PECVD order confirmation cited). Intel 18A in production
  2026. Next-gen A16/A14 actively in development.
- Years-to-full-node-step: ~1-2 yr. Timing score = 8.

## Certainty
- **demonstrated** (HVM/volume shipped + named orders). Proof point: TSMC 2nm trial production
  (Sept 2026) + AMAT GAA order confirmation; Mizuho/BofA/Bernstein WFE revisions. Score = 9.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | 6 | tool intensity per wafer rises with GAA; WFE upcycle |
| Timing | 8 | 2nm already HVM; 1-2 yr to full step |
| Certainty | 9 | volume shipped + named orders (TSMC 2nm trial production) |
| **Composite** | **432** | **HIGH** |

Tier: **HIGH (200-499)** — track; next-cycle re-check.

## Status
- **scaling** (volume underway, next node A16/A14 in dev). Moves to `deployed` at A16 HVM.

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| AMAT | >ceiling | Applied Materials | GAA ALD/PECVD orders; TSMC 2nm trial production Sept 2026 order confirmation | multi-year customer qualification, ~90%+ GM on critical steps | [2026-07] AMAT GAA ALD/PECVD order, 2nm trial (broadfsc.com AMAT note) — VERIFIED |
| LRCX | >ceiling | Lam Research | GAA etch/deposition intensity; EPS +56% YoY; Mizuho PT $380 (May 2026) | etch/deposition duopoly w/ AMAT | [2026-05-27] Mizuho raises LRCX PT to $380, WFE $153B (Yahoo Finance) — VERIFIED |
| KLAC | anchor | KLA Corp | metrology/etch content-per-wafer rises with GAA; backlog >$12B | metrology monopoly-adjacent | [2026-08] Bernstein/BofA WFE upcycle, KLA backlog (Investing.com) — VERIFIED |
| ASML | >ceiling | ASML | 2nm→GAA higher litho intensity; High-NA pivot + advanced-packaging tooling | only credible EUV player | [2026-03] ASML pivots to advanced-packaging tool market (SPIE/semiconductor briefing) — VERIFIED |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| (low-confidence) | — | legacy 7nm-and-up packaging-only scaling path (chiplets-on-7nm as the node-scaling alternative) | GAA node scaling competes with the "scale the package, not the node" path; if GAA dominates, the packaging-only scaling revenue share is capped | est. n/a (additive, not a clean line) | 0.6 (claimed) | low | [2026] Dwarkesh/Patel: TSMC scaling packaging faster than process — UNVERIFIED |

> **Honest stress-test note:** a node *up-shift* is additive to tool spend, not a clean
> substitution of a revenue line. This drift has **no clean loser** — that is a legitimate
> additive/process-intensity drift, not a failure. The schema must tolerate a weak/empty
> loser edge (same rule as `concepts/SCHEMA.md` Displacement: name the contrast or state
> "additive, no incumbent displaced").

## Sequencing
- enables → [sic_gan_power](../concepts/sic_gan_power.md) (higher power density per die drives the 800V rewire)
- prerequisite-for → [DRIFT-003_300mm-to-450mm.md] (node scaling pressure is what motivates larger-disc yield)

## Competitive/Substitution Links
- AMAT ↔ LRCX : substitution-rival (bid against each other for the same GAA process steps)
- ASML → AMAT/LRCX/KLAC : upstream-supplier (litho gates the tool spend)

## Cascade Hook
- Gap-phrase: **"gate-all-around etch deposition content per wafer"**
- Surface forms: `"gate-all-around" etch OR deposition "content per wafer"`,
  `site:patents.google.com nanosheet GAA etch`, `GAA "design win" OR "pilot" 2nm`,
  `site:arxiv.org nanosheet transistor yield`.
- Fires at Composite ≥ 500 (not yet; at 432 = HIGH, monitor for A16 HVM → re-rate to CRITICAL).

## Evidence
- [2026-08] WFE structural upcycle: Bernstein $148B / BofA $150-160B, KLA backlog >$12B, LRCX EPS +56% — https://uk.investing.com/news/stock-market-news/wafer-fabrication-equipment-outlook-amat-lrcx-and-klac-in-a-structural-upcycle-93CH-4883710 (VERIFIED)
- [2026-05-27] Mizuho raises 2026 WFE to $153B, LRCX PT $380 — https://finance.yahoo.com/markets/stocks/articles/mizuho-raises-price-target-lam-164922056.html (VERIFIED)
- [2026-07] AMAT GAA ALD/PECVD order; TSMC 2nm trial production Sept 2026 — broadfsc.com AMAT note (VERIFIED)
- [2026-03] ASML pivots to advanced-packaging tool market beyond EUV — SPIE / Semiconductor Briefing (VERIFIED)

## Open questions / next-cycle checks
- Confirm A16 HVM date + whether it carries a new tool-intensity step (would push Composite to CRITICAL).
- Pull FMP segment revenue for KLAC/LRCX metrology+etch to fix the small/mid content-per-wafer exposure %.
- Verify the ASML advanced-packaging tool revenue line (is it a new revenue stream or re-allocated?).

## Dated Evidence Notes
- [2026-10-25] [seed001a] Seeded as first process-node drift from the 2026 WFE structural upcycle.

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-02 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-001.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| AMAT | winner | 73.3% (FY2025) | 297.2 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Semiconductor Systems |
| ASML | winner | 0.0% (FY2025) | 588.2 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |
| KLAC | winner | 0.0% (FY2026) | 199.5 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |
| LRCX | winner | 0.0% (FY2026) | 284.8 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |

**Composite (M x T x C): 6 x 8 x 9 = **432** -> tier **HIGH**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: demonstrated
  - timing_years: 1.5 | displacement_sub_class: content-per-unit
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: FMP product segments are coarse for WFE (ASML/KLAC/LRCX report single 'Semiconductors'/'Systems' lines) -> exposure% there = whole-company proxy, not a keyword split. AMAT is the measurable one (Semiconductor Systems = 73.3%).

## Last Updated (2026-10-25)

# DRIFT-002 — Microreactors Replace Grid-Extended Power for Data Centers

## Substitution Pair
- **Old Process:** Grid-extended power (centralized generation → long-distance transmission → utility-scale transformer delivery)
- **New Process:** Behind-the-meter microreactor generation (on-site nuclear microreactor at data center campus)
- **Value-chain layer:** Reactor design → fuel supply → reactor installation → maintenance

## Evidence
- **Source 1:** NANO Nuclear — "three-year engineering pact for KRONOS microreactor components" (energiesmedia.com, Nov 7, 2026)
  - URL: https://energiesmedia.com/nano-nuclear-three-year-engineering-pact-kronos/
  - Claim: NANO Nuclear signed a 3-year Engineering Services Master Agreement (ESMA) with IMPSA (Argentina) for KRONOS MMR reactor pressure vessel fabrication. Reactor in NRC construction permit pre-application with UIUC partnership.
  - Status: VERIFIED — press release coverage of a signed multi-year contract.
- **Source 2:** SpaceNukes — DARPA award for kilopower reactor ground test (ans.org, Oct 26, 2026)
  - URL: https://www.ans.org/news/2026-10-26/article-8520/spacenukes-receives-darpa-award-to-ground-test-kilopower-reactor/
  - Status: VERIFIED — government award confirming microreactor TRL advancement.
- **Source 3:** Gemral — "Nuclear SMR Stocks: AI Datacenter Power" (2026)
  - URL: https://www.gemral.com/blog/post/nuclear-smr-stocks
  - Status: UNVERIFIED — listicle/guide, confirms market narrative but not a standalone signal.

## Score
| Factor | Grade | Rationale |
|--------|-------|-----------|
| M (Magnitude) | 8 | Grid transformer lead times hit 160+ weeks (candidate 38). Microreactors bypass grid entirely — each hyperscaler data center needs 100-500MW. Multiple entrants (NANO, OKLO, SpaceNukes) validate the TAM thesis. |
| T (Timing) | 3 | NRC pre-application stage for NANO KRONOS; SpaceNukes DARPA ground test in progress; first commercial deployment ~2028-2030. Medium-term. |
| C (Certainty) | 7 | Demonstrated — NANO signed a 3-year ESMA contract (not a roadmap). SpaceNukes received DARPA OTA (Other Transaction Agreement). Multiple companies at pre-application stage with NRC. |

**Composite:** M×T×C = 8×3×7 = **168**

## Displacement Sub-class
Technology adoption curve (centralized → distributed generation)

## Timing
2025-2027 (NRC engagement, reactor design freeze), 2028-2030 (first deployment)

## Market Cap at Stake
~$50-100B across nuclear fuel, reactor manufacturing, and site infrastructure

## Note
The transformer lead time bottleneck (160+ weeks, candidate 38) is the forcing function. Data centers cannot be built on grid-extended power timelines. Microreactors at 10-50MW per unit are being positioned as the behind-the-meter solution for AI data centers. NANO Nuclear's 3-year ESMA with IMPSA is a real contract milestone (not a MoU), and the KRONOS is in NRC pre-application with UIUC.

## Tickers
- **OKLO** — OKLO Inc. — Microreactor designer (Aurora SMR), US-listed
- **NNAE** — NANO Nuclear Energy — KRONOS microreactor, US-listed (OTC/TSX)

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-20 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-002.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| NNAE | winner | n/a (no matching segment data) | ? | - (upside) | None -> ? (unmapped) | - |
| OKLO | winner | n/a (no matching segment data) | 3.9 | - (upside) | Utilities -> manufacturing (operators/DC power) | - |

**Composite (M x T x C): 8 x 3 x 7 = **168** -> tier **EMERGING**
  - Mcap at stake: $75.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: demonstrated
  - timing_years: 2025-2030 | displacement_sub_class: technology_adoption
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Transformer lead times hit 160+ weeks forcing data centers to seek behind-the-meter power. NANO Nuclear signed 3-year ESMA with IMPSA for KRONOS reactor pressure vessels (pre-NRC). SpaceNukes received DARPA OTA for kilopower ground test.


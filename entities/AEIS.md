---
ticker: AEIS
name: "Advanced Energy Industries, Inc."
pillar: ENERGY_MATERIALS
tier: NEUTRAL
net_score: -1.4
quant_composite_score: 49.3
market_cap: 7976166687.0
execution_sweet_spot: true
options_gate: "REJECTED_CONVEXITY"
conv_flag: "NO_DATA"
structure_hint: "DEBIT_SPREAD_45D"
liquidity_tier: "THIN_RISK"
short_wing_warning: "UNKNOWN"
pillar_hub: "[[HUB_ENERGY_MATERIALS]]"
related_links: []
tags:
  - pillar/energy_materials
  - etf/grid
  - mcap/mid
  - mcap/sweet_spot_2b_80b
  - tier/neutral
  - gate/rejected_convexity
  - liquidity/thin_risk
wiki_state_hash: 94bc8c8db3354226dd15410bf13bacf4f8aa9f72addaa420047a91075d0c76db
---

# Advanced Energy Industries, Inc. (AEIS)

## Scorecard & Execution Gate

| Metric | Value |
|---|---|
| Pillar | [[HUB_ENERGY_MATERIALS]] |
| Tier | NEUTRAL |
| Net Score / Quant Composite | -1.40 / 49.30 |
| Market Cap | $7.98B (Sweet Spot $2B-$80B: Yes) |
| Price | 197.03 |
| Options Gate / Structure | REJECTED_CONVEXITY / DEBIT_SPREAD_45D |
| Liquidity Tier / Short Wing | THIN_RISK / UNKNOWN |
| Bull / Bear Edge | 0.365 / 0.392 |

## 45-DTE Options Surface

| Field | Value |
|---|---|
| Status / Conv Flag | REJECTED_CONVEXITY / NO_DATA |
| IV 45d / RV 20d / Vol Ratio | 0.7083 / N/A / N/A |
| Primary 0.45d Spread / OI / DTE | 16.84% / 55 / N/A |
| 25d Skew Norm / 5d Delta | N/A / N/A |
| 25d Call Wing (Spread / OI) | N/A / N/A |
| 25d Put Wing (Spread / OI) | N/A / N/A |
| Risk Note |  | convexity_gate: OI 55 < 100 |

## Catalyst & Constituent ETFs

- Earnings: None scheduled in window
- Constituent ETFs: GRID (0.04%)

## Adversarial Red Team

| Field | Value |
|---|---|
| As-Of / Direction | 2026-11-07T02:09Z / NONE |
| Triage / Kill Risk / Score Adj | N/A / 35% / N/A |
| 10-K Corpus / Degraded | 415 chars / No |
| Customer Concentration | 10.0% |
| Primary Risk | The primary structural risk is the absence of explicit customer concentration or backlog data in the provided corpus, which prevents verification of the 'qualification ramp' de-risking rule (Rule b), leaving the thesis exposed to unverified customer dependency despite strong financial fortress metri |
| Tribunal Summary | The bear case relies on the opacity of the customer base, as the sliced 10-K contains no Item 8 notes on major customers or concentration, forcing a default assumption of low concentration that may mask hidden dependencies. While the engine signals show a robust financial fortress with an Altman Z of 4.88 and positive gross margin momentum (+38.83 bps QoQ), the lack of backlog or deferred revenue growth evidence (only +6.43% QoQ) in the text prevents confirming the S-curve ramp narrative. The 4.76% YoY share count growth is manageable and not flagged as a dilution kill, but without visible RPO |

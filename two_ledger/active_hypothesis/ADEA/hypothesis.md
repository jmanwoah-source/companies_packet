# ADEA — Active Hypothesis

## State Hash
`0000000000000000000000000000000000000000000000000000000000000000`
(NO EVIDENCE YET — hash will be computed when evidence files are added)

## Evidence Chain
| Claim | Evidence File | Date | Confidence |
|-------|---------------|------|------------|
| (none yet — awaiting evidence ingestion) | | | |

## Current Thesis
(computed from evidence — empty until first evidence file is added)

## Falsification Triggers
| Condition | Source | Action |
|-----------|--------|--------|
| rev_growth < 5% for 2 quarters | fmp_metrics/revenue_*.json | INVALIDATE |
| insider_selling > buying 3:1 | insider_trades/form4_*.json | FLAG_REVIEW |
| institutional_outflow > 10% | institutional/13f_*.json | RECOMPUTE |
| state_hash changes without new evidence | evidence_index.md | FORCE_REFRESH |

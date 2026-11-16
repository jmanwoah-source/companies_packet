# Two-Ledger Wiki Architecture

## Philosophy
Split recursive ticker state into two independent ledgers:

- **immutable_evidence/** — Timestamped SEC items, FMP rev/margin deltas, Form 4/13F facts. LLM cannot overwrite. Append-only.
- **active_hypothesis/** — Recomputed from evidence + raw filings only. Requires explicit falsification_trigger to modify.

## Rules
1. **Evidence is never modified.** New evidence = new files (append-only).
2. **Hypothesis files reference evidence by filename + date range.**
3. **LLM generates hypothesis content from evidence, not from prior hypothesis content.** Never feed prior LLM prose summaries back as ground-truth evidence.
4. **A falsification_trigger** is an explicit condition (e.g., "rev growth < 5% for 2 consecutive quarters") that invalidates the hypothesis and forces recomputation.
5. **state_hash** on hypothesis files = SHA-256 of all evidence file hashes. When evidence changes, hash changes → hypothesis must recompute.

## Directory Structure
```
two_ledger/
  immutable_evidence/
    <TICKER>/
      sec_filings/       (8-K, 10-K, Form 4, 13F records)
      fmp_metrics/       (revenue, margin, EPS deltas from FMP)
      insider_trades/    (Form 4 transactions with dates)
      institutional/     (13F holdings snapshots)
  active_hypothesis/
    <TICKER>/
      hypothesis.md      (current thesis, evidence-referenced)
      falsification_triggers.md (conditions that invalidate hypothesis)
      evidence_index.md  (map from hypothesis claims to evidence files)
      state_hash.txt     (SHA-256 of all evidence files — change triggers recomputation)
```

## Hypothesis File Format
```markdown
# TICKER — Active Hypothesis

## State Hash
{SHA-256 hash of all evidence files}

## Evidence Chain
| Claim | Evidence File | Date | Confidence |
|-------|---------------|------|------------|
| Revenue grew 30% YoY | fmp_metrics/revenue_Q3_2026.json | 2026-10-28 | High |
| SEC Form 4: insider buy | sec_filings/Form4_20261110.json | 2026-11-10 | Verified |

## Current Thesis
(computed from evidence, never from prior hypothesis.md)

## Falsification Triggers
| Condition | Source | Action |
|-----------|--------|--------|
| rev_growth < 5% for 2 quarters | fmp_metrics/revenue_*.json | INVALIDATE |
| insider_selling > buying 3:1 | insider_trades/form4_*.json | FLAG_REVIEW |
| institutional_outflow > 10% | institutional/13f_*.json | RECOMPUTE |
| state_hash changes without new evidence | evidence_index.md | FORCE_REFRESH |
```

## Falsification Trigger Logic
1. Monitor conditions at each pipeline cycle.
2. If a trigger fires → rename hypothesis.md to hypothesis.md.OBSOLETE_{timestamp}.
3. Create fresh hypothesis.md from evidence only.
4. Log the falsification event to hypothesis_falsifications.log in the wiki base.

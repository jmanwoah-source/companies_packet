# Drift-Event Index

Catalog of first-class technology-substitution (drift) events in `drifts/`.
Regenerate this list after any drift edit. Scores use the M×T×C composite (0-1000).

| ID | Substitution | Class | Sector | Layer(s) | M | T | C | Composite | Tier | Status | Clean loser? |
|----|--------------|-------|--------|----------|---|---|---|-----------|------|--------|--------------|
| DRIFT-001 | FinFET → GAA @ 2nm-class (node) | process-node | semiconductors | tools, manufacturing | 6 | 8 | 9 | **432** | HIGH | scaling | No (additive) |
| DRIFT-002 | GaN-on-sapphire LED → GaN-on-Si power | cross-domain-transfer | semiconductors | substrate, design, mfg | 6 | 10 | 10 | **600** | CRITICAL | deployed | Yes (SMART/CreeLED) |
| DRIFT-003 | 300mm wafer → 450mm wafer | manufacturing-scale | semiconductors | substrate, tools, mfg | 5 | 2 | 2 | **20** | NOISE | emerging | Yes (300mm substrates) |

## Status
- DRIFT-002 is the reference anchor: a completed, SEC-filed cross-domain transfer with both winner (WOLF) and loser (SMART/CreeLED) edges intact.
- DRIFT-001 is the live HIGH drift: 2026 WFE structural upcycle; re-rates to CRITICAL at A16 HVM.
- DRIFT-003 is the schema stress test: big potential magnitude, low certainty → NOISE yet filed for auto re-rating on a foundry commitment. It proves the losers track works independent of the winner's score.

## Loser-track (Track D) seed rows (substitution-based, NOT valuation-based)
- **SMART** (CreeLED) — GaN epi line lighting-bound; sub_downside ~100 (demonstrated).
- **TER / AXTI** — 300mm substrate line; sub_downside ~12-18 (rumored, low-confidence — fix via FMP).
- *(class)* legacy silicon final-stage power / 50V PoL/VRM — 800V rewire displacement; sub_downside low-mid (claimed).

## Open (all 3 seeds)
- DRIFT-001: A16 HVM date + KLAC/LRCX metrology/etch segment exposure via FMP.
- DRIFT-002: 8-inch GaN-on-Si volume-adoption date; WOLF post-restructuring revenue split.
- DRIFT-003: IMEC/Intel 450mm-HBM study status; any foundry pilot commitment in Q4 2026.

## v1.1 (2026-10-25) — pillar validation applied

5-panel validation (4 pillars + adversarial critique) PASS'd the schema; blocking fixes landed in SCHEMA.md:
- FM-1 multi-sector field (primary + Secondary sectors) — detector scaffold
- FM-2 mandatory net_drift_position in company Drift Exposure backlinks — Track D consumer
- cap-band columns on Winner/Loser tables (sub-ceiling quant edge filterable)
- Displacement sub-classes (cutoff/additive/content-per-unit/architecture-reset)
- timing-gate rule (regulated pillars) + nuclear certainty min(TRL, licensing)
- procurement-substitution class (defense budget re-pointing)
Deferred: gradual displacement curve, private-winner supplier-discovery cascade rule, horizon column in tier table.
Sample drifts surfaced for Phase 2 filing: DRIFT-004 High-NA EUV (144 EMERGING), DRIFT-005 liquid-cooling default (336 HIGH), DRIFT-006 SMR DC power (105 EMERGING, gate-watched), DRIFT-007 autonomous C-UAS detect-and-kill (180 EMERGING upper).

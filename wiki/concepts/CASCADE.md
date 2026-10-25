# Discovery Cascade — how a high-scoring ticker finds the NEXT ticker

The pipeline is news-driven: it only sees tickers that appear in headlines. A company that is
"onto something" often hasn't made the news yet. The cascade turns a high inclination score into
next-cycle search queries so the system can surface the NEXT company in the same tech gap *before*
the mainstream catches up.

## Trigger
A ticker `T` scores >= 50 (alerts) OR is the `advantaged` play in a tech gap at stage
`first_customer`/`shipping`. `T` fills gap `G` (from `~/wiki/entities/tech_gaps/*.md`).

## Trigger v2 — Drift-Event cascade (added 2026-10-25; the trigger is the DRIFT, not the ticker)
A drift event `D` (`~/wiki/wiki/drifts/DRIFT-*.md`) with **Composite >= 500 (CRITICAL)** OR
**status transition to `scaling`** (e.g. a timing-gate fired: NRC SDA, foundry commitment)
cascades on the EVENT, not on any single company's score. This is the upgrade the drift
schema exists for: one re-rated drift propagates to ALL its linked dossiers at once.

### Steps (deterministic where possible; the Drift Detector cron runs this in the same cycle)
1. **Read the event's edges.** Winner edges, loser edges (named rows only), Sequencing
   (`prerequisite` / `enables` / `competes` / `sequences-after`), and Competitive/Substitution
   links. A node holding BOTH a winner edge on one drift and a loser edge on another is
   legitimate — its net position is the `net_drift_position` line in its `## Drift Exposure`
   block (FM-2).
2. **Re-sync the consumer surfaces (deterministic).** Run
   `python3 ~/.hermes/scripts/drift_track_d.py`: it rebuilds the Track D short list, every
   linked company's `## Drift Exposure` backlink (winner + loser edges), and the INDEX.
   A single drift re-rate propagates to every dossier this way — no manual per-ticker edits.
3. **Cascade to the NEXT value-chain layer via Sequencing** (the "next layer" rule):
   if `D` `enables` or `prerequisite-for`s drift/concept `D2`/`G2`, generate 3-4 cascade
   queries from `D2`'s gap-phrase and run them through SearXNG (same fan-out as v1, 2.5s
   sleeps, synthetic source_name `cascade_<D>`, max 6 items, identical quality bar).
   The next layer is the winner's upstream: 450mm wafer → large-substrate makers →
   equipment makers that make the large-wafer tools.
4. **Private-winner supplier-discovery (FM-4):** if `D`'s winner set is all `PRIVATE`,
   the hook fires on the private winner's PUBLIC suppliers instead — use `D`'s
   `upstream-supplier` edges as the query seed (e.g. Anduril → its edge-NPU/sensor
   component names).
5. **New-ticker extraction + scoring:** as v1 (step 4-5) — new US-listed tickers feed the
   normal inclination pipeline; losers with a named ticker get their exposure re-estimated
   from FMP fundamentals (revenue line per value-chain layer) at the next Deep-Dive pass,
   which lifts the sub_downside estimate from `est.` to a measured number.

### Rules (in addition to v1 rules)
- A drift at Composite < 500 does NOT cascade on its own — it cascades only on a
  re-rate to >= 500 or a gate-fire (status `emerging` → `scaling`).
- Max 4 drifts cascaded per cycle (token guard), same as v1.
- A drift that cascades 3 consecutive cycles with 0 new tickers → mark `SATURATED` in its
  INDEX row and stop until new evidence appears.
- The cascade NEVER auto-adds a ticker to ACTIVE (same v1 rule); it surfaces for scoring.

## Steps (deterministic; run inside the Sources cycle, 0 LLM tokens for query-gen)
1. **Extract the gap signal** from `T`'s winning evidence (contract name, technology, use-case):
   the 3-6 word phrase that describes `G` (e.g. "800V GaN power delivery", "counter-UAS
   detect-and-kill", "SMR data-center power").
2. **Generate 3-4 cascade queries** from that phrase (same signal, different surface form):
   - `"companies" <gap-phrase>`  (who else)
   - `site:patents.google.com <gap-technical-term>`  (who is filing)
   - `<gap-phrase> "design win" OR "pilot" OR "contract"`  (who has traction)
   - `site:arxiv.org <gap-technical-term>`  (who is the pre-competitive research)
3. **Run through SearXNG** (the engine's normal fan-out, 2.5s sleeps). Attribute results with a
   synthetic source_name `cascade_<G>` so they are traceable and do NOT inflate the 5-real-agent
   hard cap (they are *discovery* items, not quota items — max 6, quality bar identical).
4. **New-ticker extraction**: any US-listed ticker in the cascade results that is NOT already in
   the tracked universe → feed it into the same inclination pipeline (it gets screened, scored,
   and — if >= 50 — alerted).
5. **Write the filler into the gap wiki**: add the new ticker as a `Fillers` row in the `G`
   entity (with stage + dated source). Do not delete existing fillers.

## Rules
- Cascade items carry `source_type: "cascade"` and are subject to the SAME quality bar as real
  agents (must name a specific company/contract/event; no trend pieces).
- Max 6 cascade items per cycle, max 4 gaps cascaded per cycle (token guard).
- A cascade that finds 0 new tickers for 3 consecutive cycles → mark the gap `SATURATED` in the
  wiki and stop cascading it until a new source of evidence appears.
- The cascade NEVER auto-adds a ticker to the ACTIVE watchlist — it only surfaces it for scoring.
  Promotion to ACTIVE still requires the normal best_track_score >= 75 bar (see Deep-Dive STEP 7; 400-scale retired 2026-10-18).

## Why this is the "early advantage"
A single alerting ticker (`T`) is one data point. The cascade is the mechanism that converts that
data point into a *scan of the whole gap*, catching the 2nd/3rd company 1-3 cycles before they
appear in the news the normal 16-query fan-out would have missed.

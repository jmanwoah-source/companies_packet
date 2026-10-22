# Discovery Cascade — how a high-scoring ticker finds the NEXT ticker

The pipeline is news-driven: it only sees tickers that appear in headlines. A company that is
"onto something" often hasn't made the news yet. The cascade turns a high inclination score into
next-cycle search queries so the system can surface the NEXT company in the same tech gap *before*
the mainstream catches up.

## Trigger
A ticker `T` scores >= 50 (alerts) OR is the `advantaged` play in a tech gap at stage
`first_customer`/`shipping`. `T` fills gap `G` (from `~/wiki/entities/tech_gaps/*.md`).

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

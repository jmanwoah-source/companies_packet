# Drift-Event Schema (technology-substitution graph)

A **drift event** is a first-class, scoreable, cascade-able object representing a
*technology substitution*: an old process is replaced by a new process at a specific
value-chain layer, creating a **winner** (maker of the new process's inputs) and a
**loser** (revenue is in the old process). The loser's downside is the same event seen
from the other side of the P&L.

This upgrades `concepts/` (tech-gap entities, where drift was an annotation on a gap file)
to a **bipartite graph**: Company nodes (`../companies/`) + Drift-Event nodes (this dir),
linked by typed edges. A single re-rating of a drift propagates to every linked dossier.

## Why this exists (the gap it closes)

The current wiki is company-centric: drift is an ephemeral catalyst note on a ticker,
duplicated across every affected company, and unrankable. The mirage/short track is
**valuation-based** (overbought / structurally breaking down), **not substitution-based**.
A cheap, well-run company whose revenue is about to be cannibalized by a new process is
**invisible to every current filter** — it looks fine. This schema captures that downside
as a scored edge, independent of valuation.

## File convention

- One file per drift event: `DRIFT-<NNN>_<kebab-slug>.md`.
- `<NNN>` = 3-digit sequential, assigned at creation, **immutable** (never reassigned).
- Deterministic ID (no uuid4) — consistent with the brief_id dedup lesson.
- The **substitution pair + ID are immutable** once filed. Status, certainty, score, and
  loser edges are mutable (re-rated over time; never silently rewritten — see idempotency).

## Edge types (the bipartite graph)

| Edge | Stored in | Meaning |
|------|-----------|---------|
| `Company → Event` (role: winner \| loser) | event's Winner/Loser tables **and** a `## Drift Exposure` backlink in the company dossier | one company's win/lose stance toward this drift |
| `Event → Event` (prerequisite \| enables \| competes \| sequences-after) | the `## Sequencing` section | drifts that gate, unlock, or race each other |
| `Company → Company` (substitution-rival \| displaced \| upstream-supplier) | the `## Competitive/Substitution Links` section | direct competitive/substitution relationship surfaced by the drift |

### Drift Exposure backlink (company side — v1.1 / FM-2, BLOCKING)

When a drift gains a winner or loser edge to a company, the company dossier gets (or updates) a `## Drift Exposure` section containing:
- one line per linked drift: `[DRIFT-NNN] winner|loser — sub_downside X / upside rationale`
- a **required computed line**: `net_drift_position: +<winner edges> / -<sum of sub_downside> / mixed`

This is the Track D consumer: a cheap, well-run incumbent can look fine on valuation yet score a negative net_drift_position — the substitution downside the mirage track cannot see. No net line = the backlink is invalid.

## Required sections (in order)

```markdown
# DRIFT-NNN — <old process> → <new process> (<class>)

**Class.** process-node | cross-domain-transfer | manufacturing-scale | materials-substitution | architecture-substitution | regulatory-substitution | procurement-substitution
(procurement-substitution = budget re-pointing, e.g. FMS IDIQ re-allocating from manned to unmanned programs — its certainty ceiling is the *budget cycle*, not a tech demo. Added v1.1 from the physical-AI pillar validation.)
**Substitution.** <old> → <new>  (one line, the actual physical/process swap)
**Sector.** <primary: semiconductors | ai-infrastructure | advanced-energy | physical-ai>   (maps to the matching sector dossier = the query scaffold)
**Secondary sectors.** <optional list>   (v1.1 / FM-1 — multi-sector drifts: the Phase-3 detector fans out over primary ∪ secondary. The 800V rewire spans semiconductors + ai-infrastructure; without this a cross-pillar drift is invisible to the other pillars' scans.)
**Value-chain layer(s) affected.** <from the normalized layer vocabulary below>

## Magnitude (mcap + revenue at stake)
- Which tracked tickers are exposed, and what % of each one's revenue is in the old process.
- Aggregate mcap at stake. Be honest if the at-stake mcap is conditional/unrealized.

## Timing (TRL → volume)
- TRL stage (1-9). Years-to-volume. Named milestone dates (demonstrated / pilot / volume).

## Certainty
- demonstrated | claimed | rumored  — with the specific proof point (a shipped volume line,
  a management roadmap, a feasibility study). No unlinked certainty claims.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | M | ... |
| Timing | T | ... |
| Certainty | C | ... |
| **Composite** | **M×T×C** | ... |
Tier: CRITICAL (500-1000) | HIGH (200-499) | EMERGING (50-199) | NOISE (<50).
Composite is multiplicative: a zero/low on ANY axis kills the score. A rumored 8-year shift
CANNOT outrank a demonstrated 2-year one.

## Status
- emerging | scaling | deployed   (+ one line: what moves it to the next state)

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
cap-band: anchor (>$50B) | mid ($10-50B) | sub-ceiling ($1-10B) | nano (<$1B) | >ceiling (>$300B, flagged) — the quant edge is the sub-ceiling/nano rows; anchors stay in the graph, the edge gets filtered from them.
(US-listed tickers only; private = PRIVATE. Every edge needs a dated, linked source.)

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
sub_downside = revenue-exposure-% × certainty-weight (demonstrated=1.0, claimed=0.6,
rumored=0.3). This is INDEPENDENT of the winner's drift score and of the loser's valuation.
It feeds the substitution/short track (Track D) — the "other companies going down because
of this" leg. A clean substitution may have NO clean loser — state that explicitly (an
additive/new-market drift), do not force one.

## Sequencing
- prerequisite / enables / competes / sequences-after → [DRIFT-XXX] (or `../concepts/<gap>.md`)

## Competitive/Substitution Links
- <ticker> → <ticker> : substitution-rival | displaced | upstream-supplier

## Cascade Hook
- The 3-6 word gap-phrase that CASCADE.md would scan for the NEXT ticker (same query-gen
  rules as CASCADE.md: 3-4 surface forms, SearXNG, max 6 cascade items, same quality bar).
- Fires when Composite ≥ 500 (CRITICAL): auto-link winner AND loser dossiers, then cascade
  to the next value-chain layer via Sequencing.

## Evidence
- [date] <headline> — <url>   (mark VERIFIED vs UNVERIFIED)

## Open questions / next-cycle checks
- 2-3 concrete checks (e.g. "confirm foundry commitment status", "pull FMP revenue line
  for the exposed ticker to fix the exposure %").

## Dated Evidence Notes
- [YYYY-MM-DD] [<evidence_id8>] <one-line update>
(append-only; deterministic evidence_id = md5 of normalized source+headline;
case-insensitive dedup guard — the brief_id bug lesson.)

## Last Updated (YYYY-MM-DD)
```

## Scoring rubric (Gap 3 — the missing ranking axis)

**Magnitude (0-10)** — aggregate mcap / revenue exposed to the substitution:
- 9-10: >$10B mcap OR >30% of a tracked ticker's revenue exposed
- 7-8: $3-10B mcap / 15-30% revenue exposure
- 5-6: $1-3B mcap / 5-15% revenue exposure
- 3-4: $0.3-1B mcap / 1-5% exposure
- 1-2: <$0.3B or unmeasured/conditional
(If at-stake mcap is conditional/unrealized, score on *potential* but flag it.)

- **Displacement sub-class** (v1.1 — score the same 0-10 scale): `cutoff` (a revenue line dies) · `additive` (no loser; score on new spend) · `content-per-unit` (same line, more $/unit — score on the WFE/content delta, not line displacement) · `architecture-reset` (one-time content reset per generation + steady-state run-rate — e.g. 800V rewire, liquid-cooling default; score on the reset + run-rate, NOT a fake revenue-exposure %).

**Timing (0-10)** — inverse of years-to-volume:
- 0-1 yr = 10 · 1-2 yr = 8 · 2-3 yr = 6 · 3-5 yr = 4 · 5-7 yr = 2 · >7 yr = 1
- **timing-gate** (v1.1, regulated pillars): if the drift is gated by a binary regulatory event (NRC SDA / standard design approval), record `timing-gate: <gate name>` and score Timing on the *pre-gate* clock. When the gate fires, re-rate Timing on the post-gate clock with a dated note (a 5-yr post-gate drift scores 6, not 2). Gate-fire is an evidence event, not a rewrite — the old score stays in the dated note. Without this, a decade-gated SMR drift permanently under-scores as licensing evidence accrues.

**Certainty (0-10)** —
- demonstrated (HVM/volume shipped) = 9-10
- demonstrated (pilot / design-win) = 6-8
- claimed (management roadmap / investor-day) = 4-5
- rumored (feasibility study / speculation) = 1-3
- **Regulated-pillar rule (v1.1, nuclear):** Certainty = min(tech-TRL score, licensing-progress score). Licensing ladder: topical-report approved → +2 on the base, combined-license milestone → +4, SDA/design approval → full 9-10. A TRL-8 prototype without licensing progress is NOT 9.

**Composite = M × T × C (0-1000).** Tier map:
- **CRITICAL 500-1000** — immediate cascade + winner AND loser dossier generation.
- **HIGH 200-499** — track; next-cycle re-check.
- **EMERGING 50-199** — monitor.
- **NOISE <50** — filed, low priority (stays so that a future evidence bump auto-re-rates it).

## Losers track (Gap 2 / Track D)

- Per-loser `sub_downside` = revenue-exposure-% × certainty-weight (above).
- **Independent of valuation.** This is what the mirage track cannot see: a cheap,
  well-run incumbent with high old-process revenue exposure scores high sub_downside even
  though it is not "overbought."
- Output: root `substitution_short_list.md` (Track D), distinct from `mirage_short_list.md`
  (Track C, valuation-based). Phase 1 hand-maintained from `drifts/`; a generator folds in
  with `tier_lists.py` in a later phase.

## Idempotency & immutability (the brief-id lesson)

- Catalyst/evidence appends use deterministic `evidence_id8 = md5(normalized(source+headline))`,
  guarded **case-insensitively** (`id8.lower() in content.lower()`) — never re-append.
- Substitution pair + ID are immutable. Status/certainty/score are mutable, updated by
  re-rating with a dated note — never silently overwritten.
- A loser's historical exposure % is never rewritten; supersede with a dated note.

## Layer vocabulary (normalized; per-sector aliases map onto it)

| Canonical layer | Semiconductors | AI-infra | Advanced-energy | Physical-AI |
|-----------------|----------------|----------|-----------------|-------------|
| `tools` | fab/litho (ASML,AMAT,KLAC,LRCX) | power-mgmt Si (MPWR,ON,NVTS) | fuel cycle (WULF,SUI) | sensors/perception (DRS,LHX,NOC,RTX) |
| `substrate/materials` | SiC/SOI/packaging mats (AXTI,WOLF,TER) | — | reactor tech/SMR (OKLO,NUS,BWXT,HTZ,MOD) | C-UAS effectors (AVAV,RCAT,BAESF) |
| `manufacturing` | foundry (TSM,UMC) | thermal/cooling (VRT,SMCI) | operators/DC power (CEG,TLN,VST) | edge-AI Si (QCOM,NVDA) |
| `design/fabless` | analog/power fabless (ADI,MCHP,ON,SWKS) | photonics (MRVL,COHR,LITE) | grid/T&D equip (GEV,ETN) | robotics/automation (ISRG,AITX,ROK) |
| `downstream` | adv packaging + optical I/O (PLAB,AMKR,COHR) | industrial elec (GEV) | DC customers (SMCI,VRT) | primes/integration (LMT,NOC,RTX,HON) |

## Consumers (keep in sync when renaming)

- `pipeline_engine.py` / `tier_lists.py` — will read `drifts/` for Track D in a later phase.
- Deep-Dive cron prompt — will append `## Drift Exposure` backlinks to company dossiers.
- `concepts/CASCADE.md` — the Cascade Hook reuses its query-gen; drift is the new trigger.
- Skill `wiki-directory-structure` — this dir is part of the canonical tree.

## Index

See `INDEX.md` for the current drift catalog + scores (regenerate after any drift edit).

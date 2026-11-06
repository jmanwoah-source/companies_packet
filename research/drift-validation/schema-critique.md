# Adversarial Schema Critique — Drift-Event Objects

**Date:** 2026-10-25 · **Method:** parent-inline (sub-agent timed out at 600s with 2 API calls —
it had only finished reads; critique executed inline from full file review)
**Scope:** `drifts/SCHEMA.md`, `drifts/INDEX.md`, DRIFT-001/002/003, `concepts/CASCADE.md`, `concepts/SCHEMA.md`

## The 5 failure modes

**FM-1 — Multi-sector drifts have nowhere to point.** `**Sector.**` is a single-valued
enum (`semiconductors | ai-infrastructure | advanced-energy | physical-ai`). The 800V rewire
touches semiconductors (power-silicon) AND ai-infra (power delivery) AND arguably energy
(grid equipment). The Phase-3 detector uses the sector dossier as its query scaffold — a
multi-sector drift filed under one sector is invisible to the other sectors' scans.
Confirmed independently by all 4 pillar validations.
**Fix:** `**Sector.**` becomes primary + optional `**Secondary sectors.**` list; the
detector fans out over primary ∪ secondary. (BLOCKING — Phase 3 scaffold depends on it.)

**FM-2 — A company that is winner to drift A and loser to drift B is unrepresentable
without annotation.** The graph allows it structurally (two edges, different events), but
nothing *aggregates* it: WOLF is winner on DRIFT-002 AND carries 300mm-substrate-era
exposure on DRIFT-003's conditional loser set. A dossier's net drift position (sum of
winner edges minus sum of sub_downside edges) is exactly the quant answer to "is this
name net long or net short the drift stack?" — and no section computes it.
**Fix:** add `## Drift Exposure` (the planned company-side backlink) with a required
`net_drift_position: +X (winner) / -Y (loser) / mixed` line; the Track D generator
already has both inputs — make the net line mandatory. (BLOCKING — it's the losers track's
consumer.)

**FM-3 — Slow/gradual displacement breaks the timing axis.** The rubric assumes a
cutoff ("years-to-volume"). A 10-year gradual cannibalization (e.g. silicon power →
wide-bandgap at the edge of the rack) has no single volume date; scoring it forces the
writer to pick a fake number. DRIFT-002's "legacy silicon final-stage" loser row already
hints at this (est. low-mid, class-level).
**Fix:** add a `displacement_curve: cutoff | gradual` field; for `gradual`, Timing scores
on *inflection* (when the new process crosses ~50% of the layer's incremental
content), not volume-start. (DEFERRED — Phase 2; doesn't affect the 3 seeds.)

**FM-4 — Private-only winner = cascade hook with nothing to fire.** If a drift's winner
edge is all `PRIVATE` (Anduril-class), CASCADE's new-ticker extraction has no US-listed
ticker to screen, and the Cascade Hook's 3-4 surface forms are fine but their output is
unfilterable. The hook as written assumes a public winner exists.
**Fix:** rule in Cascade Hook section: if winner set is all-PRIVATE, the hook fires on
*supplier discovery* instead (the private winner's public substrate/tool/material
suppliers — the drift's `upstream-supplier` edges become the query seed). DRIFT-001's
competitive-links section already has the edge type; only the rule is missing.
(DEFERRED — no current seed hits it, but counter_uas.md already lists Anduril(PRIVATE) so
it WILL hit within the tracked gaps.)

**FM-5 — The multiplicative composite punishes long-timing drifts below their
operational importance (confirmed, with one calibration).** 6/2/9 = 108 (EMERGING) vs
7/7/7 = 343 (HIGH). A demonstrated, high-magnitude shift that is simply 8 years out scores
EMERGING, while a mediocre 2-yr drift scores HIGH. For *action priority* (who do I research
this week) that's arguably correct — but the INDEX reads as a *risk* ranking, and a
decade-out demonstrated 450mm commitment is a larger risk than a 2-yr mediocre one.
The multiplication is too aggressive specifically because Timing spans 1-10 on a
*calendar* scale while M and C are *intensity* scales — the units don't match.
**Fix (calibration, keep the product):** re-map Timing to a non-linear scale
(0-1yr=10, 2=8, 3=6, 5=4, 7=3, 10+=2 — already close; hold) AND add a mandatory
`**Horizon tag:**` (short <3yr | medium 3-5yr | long >5yr) so INDEX sorts within tier by
horizon. The product stays (it correctly kills rumored+faraway), but the tier table gains
a horizon column so "EMERGING but 8-yr and demonstrated" is visually distinguishable from
"EMERGING and 2-yr and rumored." (DEFERRED — INDEX formatting + one field; the 3 seeds
already demonstrate correct behavior.)

## Verdict

**YES-with-fixes — production-ready for the 4 pillars AFTER 2 BLOCKING fixes land:**
1. **FM-1** (multi-sector field) — BLOCKING, Phase 3 detector scaffold.
2. **FM-2** (mandatory net-drift-position in company backlinks) — BLOCKING, Track D consumer.

**DEFERRED to Phase 2/3:** FM-3 (gradual-displacement curve), FM-4 (private-winner
supplier-discovery rule), FM-5 (horizon tag + tier-table column).

The 3 seeds validate the scoring spine: DRIFT-002 (600/CRITICAL/deployed) proves the
completed-drift anchor; DRIFT-001 (432/HIGH/scaling, additive-no-loser) proves the
looser-track tolerance for additive drifts; DRIFT-003 (20/NOISE/rumored, filed for
auto re-rating) proves the stress-test behavior — all three behave exactly as the schema
intends, which is the real production-readiness evidence.

## Last Updated (2026-10-25)

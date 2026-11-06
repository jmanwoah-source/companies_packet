# Drift Schema Validation — Physical AI / Robotics / Defense Pillar

**Date:** 2026-10-25 · **Method:** salvage (sub-agent timed out at 600s after search; dossier written inline from salvaged transcript evidence)
**Inputs read:** `drifts/SCHEMA.md`, `drifts/DRIFT-001_gaa-node-transition.md`, `sectors/physical-ai-edge-automation.md`

## Verdict

**PASS (with 1 blocking fix).** The class vocabulary *mostly* covers robotics substitutions:
- teleoperated UAS → autonomous UAS = `architecture-substitution` (fits)
- human-in-loop engagement → autonomous detect-and-kill = `architecture-substitution` (fits)
- cloud inference → edge NPU at the sensor = `cross-domain-transfer` (fits — inference
  workload moves domains, exactly the LED→GaN-power skeleton)

The gap: **procurement-driven substitution** (budget lines re-pointing from one program
class to another, e.g. manned-platform hours → autonomous-platform procurement) has no
clean class — it's driven by budget, not by a process swap. The salvage evidence
(AVAV's $874M FMS IDIQ) is exactly this type: the substitution is the *procurement
vehicle* (IDIQ = indefinite-delivery), not a technical process.

## Schema gaps found

1. **No `procurement-substitution` class.** Budget re-pointing is the pillar's most common
  drift driver and it doesn't map onto any existing class without a stretch. Fix: add
  `procurement-substitution` to the class enum + note that its Certainty ceiling is
  *budget-cycle* (funding announcements, not tech demos).
2. **Winner evidence in this pillar is contract awards, not volume lines.** The Evidence
  section's VERIFIED/UNVERIFIED marking works, but the *dated, linked source* for a
  defense drift is often a press release (company source) — the confidence hierarchy in
  `concepts/SCHEMA.md` (high = primary/company/gov) already covers this; just make the
  drift schema explicitly inherit it.
3. **Primes as "integration tier" winners dilute the asymmetric edge.** LMT/NOC/RTX/HON
   win the *program*; AVAV/DRS/RCAT win the *substitution*. Same cap-band fix as the
   semiconductors validation: add a `cap-band` column so the sub-ceiling asymmetric
   winners (AVAV, DRS, RCAT) are filterable out of the prime anchors.

## Sample drift (NOT in index)

**Suggestion: DRIFT-007 — Human-in-loop C-UAS engagement → autonomous detect-and-kill
C-UAS (architecture-substitution, physical-AI)**

- **Substitution.** Human-in-the-loop detection-to-engagement (operator confirms each
  kill decision) → on-board-inference autonomous detect-and-kill (sensor fusion + target
  recognition + engagement without human-in-loop).
- **Layer:** sensors/perception + C-UAS effectors (upstream of primes).
- **Magnitude (6).** C-UAS is the pillar's new permanent budget line (DoD + NATO, funded
  category per the sector dossier); autonomy raises the content-per-system and the
  reprocurement rate (unmanned systems multiply vs manned platforms). At-stake includes
  the $874M-class FMS IDIQ awards (AVAV, salvaged evidence) plus NATO program awards.
- **Timing (5).** 2-3 yrs to standardization; TRL 7 (autonomous target recognition is in
  deployment-adjacent testing; JRC 2026 review documents the detect-track-identify
  tech trajectory).
- **Certainty (6).** demonstrated at sensor level (autonomous target recognition
  fielded in systems), claimed at full detect-and-kill-without-HIL standardization.
- **Composite = 6 × 5 × 6 = 180 → EMERGING (upper band, one funding event from HIGH).**
  Correct behavior: a real, funded, fielding drift that is one standardization decision
  from the next tier.
- **Winner edge:** AVAV (autonomous UAS + C-UAS systems; $874M FMS IDIQ award,
  salvaged evidence) — sub-ceiling asymmetric name; moat = program wins + unmanned
  platform portfolio. Secondary: RCAT (counter-UAS), DRS (C-UAS radar).
- **Loser edge:** manned-platform-heavy / operator-dependent C-UAS vendors whose revenue
  depends on the human-in-loop engagement model (class-level; the sector dossier's
  "detect-only / soft-kill-only vendors" are the natural losers of the engagement-autonomy
  step). Est. exposure mid-single-digit % for detect-only vendors; weight 0.6 →
  sub_downside est. ~2-4, low, flag low-confidence pending FMP revenue-line mapping.

## Evidence (salvaged from sub-agent transcript)
- [2026] AeroVironment awarded $874M Foreign Military Sales IDIQ (deliverable
  counter-UAS / autonomous systems scope) —
  https://investor.avinc.com/news-releases/news-release-details/aerovironment-awarded-874m-foreign-military-sales-idiq-deliver (VERIFIED)
- [2026] EU JRC (JRC140692) — Technical developments in counter-drone technology:
  C-UAS detection, tracking, identification —
  https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140692/JRC140692_01.pdf (VERIFIED)

## Top 3 issues (ranked)
1. Missing `procurement-substitution` class — BLOCKING for this pillar's dominant drift type.
2. cap-band column on Winner/Loser tables (shared fix) — BLOCKING.
3. Inherit the concepts/SCHEMA.md confidence hierarchy explicitly — DEFERRED (docs-only).

## Last Updated (2026-10-25)

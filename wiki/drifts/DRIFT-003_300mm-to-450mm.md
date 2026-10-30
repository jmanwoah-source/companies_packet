# DRIFT-003 — 300mm silicon wafer → 450mm silicon wafer (manufacturing-scale)

**Class.** manufacturing-scale shift (a larger disc raises die-yield-per-wafer)
**Substitution.** 300mm silicon wafers → 450mm silicon wafers
**Sector.** semiconductors
**Secondary sectors.** —
**Horizon tag:** long (>5 yr)
**Displacement sub-class:** cutoff (300mm substrate line, conditional)
**timing-gate:** foundry 450mm pilot-fab commitment (no gate name yet — the gate IS the commitment; fires on first pilot fab, re-rate T 2→4, C 2→6)
**Value-chain layer(s) affected.** substrate/materials, tools (fab), manufacturing (foundry)

> **This is the schema's stress test.** Big potential magnitude, long timing, low certainty.
> A correct drift engine must score it **NOISE** (low Composite) yet keep it *filed*, so that a
> future foundry commitment (new evidence) auto-re-rates the certainty and lifts the score.
> It must NOT pollute the winners now.

## Magnitude (mcap + revenue at stake)
- **Conditional / unrealized.** IF it lands, *every* 300mm substrate + 300mm tool revenue line
  is at stake: substrate makers (TER, AXTI), fab tools (AMAT, LRCX, KLAC, ASML), foundry (TSM, UMC).
- Aggregate potential mcap at stake is large (>$100B across the stack), but it is not yet realized —
  no foundry has committed to a 450mm volume fab as of 2026-10. Score on *potential*, flag as unrealized.
- Magnitude score = 5 (potential $1-3B+ realized exposure at first volume; large conditional ceiling).

## Timing (TRL → volume)
- TRL 3-4 (lab / feasibility studies; no pilot fab). IMEC/Intel have studied 450mm primarily for
  HBM / advanced-packaging die-yield, not a full 450mm foundry. No volume commitment.
- Years-to-volume: 7-10+ (if ever). Timing score = 2.

## Certainty
- **rumored** (feasibility studies; no primary foundry commitment found this cycle).
  Proof point: none primary — marked UNVERIFIED. Score = 2.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | 5 | large conditional ceiling; unrealized — potential $1-3B at first volume |
| Timing | 2 | 7-10+ yrs to volume (if ever) |
| Certainty | 2 | feasibility only, no foundry commitment (UNVERIFIED) |
| **Composite** | **20** | **NOISE** |

Tier: **NOISE (<50)** — filed, low priority. Stays so that a next-cycle foundry commitment
auto-re-rates certainty (2→6-8) and lifts Composite into EMERGING/HIGH.

## Status
- **emerging** (feasibility). Moves to `scaling` on any foundry 450mm pilot-fab commitment.

## Winner Edges (conditional — only valid if the drift lands)
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| (conditional) | — | AXTI — SiC/optical substrate maker | large-substrate capability is the gating input for 450mm | substrate yield + crystal-growth IP | [2026] feasibility-stage — UNVERIFIED |
| (conditional) | — | TER — substrates/test | 450mm substrate + test content | substrate moat | [2026] feasibility-stage — UNVERIFIED |
| (conditional) | — | AMAT/LRCX/KLAC — 450mm tool re-qualification | larger-disc tool wins if the step lands | tool duopoly | [2026] feasibility-stage — UNVERIFIED |

## Loser Edges (conditional)
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| (conditional) | — | TER / AXTI — current 300mm substrate revenue line | 450mm would displace the 300mm substrate line (the cleanest substitution-loser demo) | est. 40-60% of substrate revenue (fix via FMP) | 0.3 (rumored) | ~12-18 | [2026] feasibility-stage — UNVERIFIED |
| (conditional) | — | 300mm tool configs (AMAT/LRCX/KLAC etch/deposition) | re-qualified or replaced on a 450mm fab | est. low-mid (tools are node-agnostic) | 0.3 (rumored) | est. low | [2026] feasibility-stage — UNVERIFIED |

> **Loser-track demo:** even though the event is low-certainty NOISE, the *substitution-loser*
> (300mm substrate incumbents) is the cleanest line in the stack to be displaced. The
> sub_downside is scored (exposure × 0.3 rumor-weight) and lands on the substitution/short
> track flagged **low-confidence** — proving the losers track works independent of the winner's
> (low) drift score.

## Sequencing
- prerequisite-for → (none; this is a downstream scale shift)
- motivated-by → [DRIFT-001_gaa-node-transition.md] (node-scaling pressure motivates larger-disc yield)
- competes-with → [DRIFT-002_gan-led-to-power.md] (SiC substrate scaling is the parallel materials path)

## Competitive/Substitution Links
- AXTI ↔ TER : substitution-rival (both substrate feedstock; 450mm would re-rank them)
- TER/AXTI → (450mm tool makers) : upstream-supplier (substrate gates the fab)

## Cascade Hook
- Gap-phrase: **"450mm wafer foundry pilot HBM die yield"**
- Surface forms: `450mm wafer "pilot" OR "foundry" commitment`,
  `site:imec.be OR site:intel.com 450mm wafer HBM`, `450mm "die yield" advanced packaging`,
  `next-gen wafer size "300mm" replacement`.
- Fires at Composite ≥ 500 (far — requires a foundry commitment to lift certainty). Monitor only.

## Evidence
- [2026-10] 450mm wafer transition: IMEC/Intel feasibility for HBM/advanced packaging; **no
  foundry volume commitment found this cycle** — UNVERIFIED (no primary link; see open questions)
- [2026-03] ASML High-NA EUV + advanced packaging remain the 300mm incumbent path —
  https://www.linkedin.com/posts/vlsi-amirhussain_intel18a-node-manufacturing-shifting-2026 (UNVERIFIED)

## Open questions / next-cycle checks
- **Confirm IMEC/Intel 450mm-HBM study status** — is there any foundry (TSM/UMC/Samsung/Intel)
  450mm pilot-fab commitment as of Q4 2026? A single "yes" lifts certainty 2→6-8 and re-rates the drift.
- Pull FMP substrate revenue split for TER/AXTI to fix the 300mm exposure % (the loser-track number).
- Check whether 450mm is HBM/advanced-packaging-specific or a general foundry-scale shift (changes the layer + losers).

## Dated Evidence Notes

- [2026-10-25] [audit-note] US-public 450mm loser edge is THIN: the 300mm Si-wafer makers (SUMCO, Shin-Etsu) are PRIVATE — the liquid displacement value sits in the private substrate layer, so TER/AXTI (US-listed, ~12-18 sub_downside, rumored) are the thin US-public proxy, not the full exposure. Confirmed via audit of FMP segment data.
- [2026-10-25] [seed003a] Seeded as the schema stress test: big potential magnitude, low certainty/long timing must score NOISE yet stay filed for auto re-rating on new evidence.
- [2026-10-25] [det003a] COUNTER-SIGNAL: ASML paused 450mm lithography development in 2013 (Instagram/fab-analysis, Sep 2026) — reinforces the low-certainty rating; a foundry commitment (not tool R&D) is the gate. Score unchanged (20 NOISE). https://www.instagram.com/reel/Dd4oywyCUwl/ (VERIFIED)

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-10-30 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-003.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| AXTI | loser | 66.7% (FY2025) | 4.0 | 20.0% | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Substrates |
| TER | winner | 83.4% (FY2025) | 46.3 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | Product |

**Composite (M x T x C): 5 x 2 x 2 = **20** -> tier **NOISE**
  - Mcap at stake: $2.7B (engine sum of loser exposure x mcap unless curated) | certainty_grade: rumored
  - timing_years: 8 | displacement_sub_class: cutoff
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Stress test. FMP measures the US-proxy reality: AXTI 'Substrates' = ~$0.05B -> the liquid 300mm-Si displacement value is PRIVATE (SUMCO/Shin-Etsu), confirming the audit note. TER 'Product' line = thin US proxy.

## Last Updated (2026-10-25)

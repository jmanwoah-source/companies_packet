# DRIFT-010 — Die-to-die / discrete-bond 3D interconnect → die-to-wafer (D2W) hybrid bonding at the advanced-packaging tools layer (process-node)

**Class.** process-node
**Substitution.** Discrete/die-to-die bonding for 3D chip stacking → die-to-wafer (D2W) hybrid bonding as the volume tool at the advanced-packaging interconnect layer
**Sector.** semiconductors
**Secondary sectors.** ai-infrastructure (HBM/stacked-die AI silicon)
**Value-chain layer(s) affected.** tools (back-end/advanced packaging), downstream (adv packaging)
**Displacement sub-class:** content-per-unit (per-stack interconnect content shifts from discrete-bond line to D2W hybrid-bond line; the incumbent bonder line loses content)

## Magnitude (mcap + revenue at stake)
- The substitution is at the *tools* layer: whoever owns the D2W hybrid-bonding tool owns the
  3D-stacking interconnect line. Besi (BESI, Amsterdam — non-US-listed) is the named incumbent
  bonder whose lock on chip stacking SemiAnalysis says ASML is challenging (27 ASML patent
  families, Dec 2022 – Nov 2024, mostly D2W designs; Reuters Oct 16, 2026: Besi shares fell 3%
  on the report).
- US-listed exposure is asymmetric: ASML (US ADR, ~$606B mcap, >ceiling flagged) is the US-listed
  toolmaker entering the line; there is NO clean US-listed loser in this drift (the displaced
  incumbent is BESI, non-US). Per the quality bar, the loser edge is therefore recorded as
  "additive, no clean US-listed loser" — do not force one.
- Magnitude score = 7 ($3-10B-class per-generation tools content on the HBM/stacked-logic interconnect
  line at stake once D2W is default; conditional on adoption not slipping).

## Timing (TRL → volume)
- TRL ~6-7: patent families + SemiAnalysis belief + ASML's own roadmap already puts bonding inside
  the front-end flow; the company has shipped its first back-end product (XT:260 i-line packaging
  scanner, 3Q25). No announced product or timetable.
- SemiAnalysis flags D2W adoption potentially slipping to 2029 or beyond → 3-5 yr to volume.
- Timing score = 4.

## Certainty
- **rumored-claimed**: no ASML announcement, no timetable; the evidence base is 27 patent filings,
  a third-party (SemiAnalysis) patent review + one TheLec report, and ASML's roadmap language.
  Patents are not a production tool; SemiAnalysis names open hurdles (feed-forward metrology,
  die-to-wafer contact, particle control). Score = 3.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | 7 | multi-$B tools content per generation on the 3D-stacking interconnect line |
| Timing | 4 | 3-5 yr to D2W default (SemiAnalysis: adoption may slip to 2029+) |
| Certainty | 3 | rumored-claimed: patents + third-party report, no announced tool/timetable |
| **Composite** | **84** | **EMERGING** |

Tier: **EMERGING (50-199)** — re-rate on an ASML product announcement (→ claimed, C 4-5) or a
named foundry D2W line commitment (→ demonstrated pilot, C 6-8); a named TSMC/Intel/Samsung D2W
volume line would push this into HIGH.

## Status
- **emerging** (patent/roadmap stage; no announced tool). Moves to `scaling` on an ASML D2W
  hybrid-bonding product launch + first named foundry line installation.

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| ASML | >ceiling | ASML Holding N.V. | developing the D2W hybrid-bonding tool (27 patent families Dec 2022–Nov 2024; roadmap already puts bonding in the front-end flow); lithography-grade alignment + particle control = the two bonding-yield factors | alignment accuracy + particle control IP; first back-end product shipped (XT:260, 3Q25) | [2026-10-15/16] SemiAnalysis: ASML Is Building a Hybrid Bonding Tool (27 patent families reviewed) — VERIFIED (search-confirmed); [2026-10-16] Reuters: Besi shares fall on ASML hybrid-bonding report — VERIFIED (search-confirmed) |

> **Note:** BESI (Besi N.V.) is the tool-line incumbent named in the source but is Amsterdam-listed
> (not US-listed) → recorded here as a class note, not a named edge, per the US-ticker rule.

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| (class) | — | Besi (BESI, Amsterdam — NON-US, out of universe) / discrete-bond & die-to-die 3D-interconnect tool content | bond-line content per stack shifts to D2W hybrid bonding as ASML ships a tool | n/a (non-US; no US-listed clean loser) | — | — | [2026-10-16] Reuters (Besi shares -3% on the ASML report) — VERIFIED (search-confirmed) |

> **Loser-track note:** ADDITIVE FOR THE US-TRACKED UNIVERSE — there is no clean US-listed loser in
> this drift; the displaced incumbent (BESI) is non-US-listed. Stated explicitly per the schema;
> no US loser row is forced.

## Sequencing
- enabled-by → [DRIFT-001_gaa-node-transition.md](DRIFT-001_gaa-node-transition.md) (GAA/A16 density → 3D stacking + HBM stacks as the default AI-silicon path)
- enabled-by → [DRIFT-004_high-na-euv.md](DRIFT-004_high-na-euv.md) (High-NA reticle limits → more stacking to stay under the reticle)
- enables → (intra-chip optical I/O at the D2W interface; next frontier, unfiled)

## Competitive/Substitution Links
- ASML → (BESI class) : displaced (ASML's D2W tool undercuts the incumbent's 3D-bonding lock)
- (BESI class) → ASML : substitution-rival (both competing for the same D2W bond-line content)

## Cascade Hook
- Gap-phrase: **"die-to-wafer hybrid bonding foundry line"**
- Surface forms:
  - `ASML hybrid bonding tool announcement OR demo`
  - `"die-to-wafer" hybrid bonding foundry line HBM`
  - `site:patents.google.com die-to-wafer hybrid bonding alignment`
  - `hybrid bonding "design win" OR "volume" 3D stacking`
- Fires at Composite ≥ 500 (not near; the trigger is an ASML product announcement or a named
  foundry D2W line commitment).

## Evidence
- [2026-10-15] SemiAnalysis: ASML Is Building a Hybrid Bonding Tool, Sending More Chills to Besi (27 patent families Dec 2022–Nov 2024; D2W first) — https://newsletter.semianalysis.com/p/asml-is-building-a-hybrid-bonding (VERIFIED — confirmed via 2026-10-26 search; paywalled body, headline + key claims from Dealroom/SCMP/Reuters syndication)
- [2026-10-16] Reuters (AP wire): Besi shares fall on report ASML is working on rival hybrid bonding product — http://www.thenewstribune.com/news/business/article317648421.html (VERIFIED — search-confirmed)
- [2026-10-19] Dealroom: ASML builds hybrid bonding tool, challenging Besi's lock on chip stacking (D2W adoption may slip to 2029+) — https://dealroom.co/news/163898-asml-builds-hybrid-bonding-tool-challenging-besis-lock-on-chip-stacking (VERIFIED — search-confirmed)

## Open questions / next-cycle checks
- ASML product/timetable: any announcement at the next quarterly call or VLSI/ESDMC (the
  rumored→claimed re-rate trigger).
- Name the first foundry D2W line commitment (TSMC/Intel/Samsung/UMC) — the demonstrated-pilot
  re-rate trigger; re-rate T + C together.
- FMP check: ASML FY2025 product segments are NXE / ArF immersion / ArF dry / KrF / I-line / EXE /
  Metrology & Inspection / Net service — back-end & bonding have no dedicated segment yet (engine
  will match on sector). Re-check on the first back-end revenue line disclosure.

## Dated Evidence Notes
- [2026-10-26] [seed010a] Filed by the Drift Detector judgment leg (candidate #6/27, DRIFT-010;
  ASML D2W hybrid-bonding, SemiAnalysis + Reuters + Dealroom, 2 web searches, 0 page fetches).

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-10-26 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-010.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| ASML | winner | 0.0% (FY2025) | 605.8 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |

**Composite (M x T x C): 7 x 4 x 3 = **84** -> tier **EMERGING**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: rumored
  - timing_years: 4 | displacement_sub_class: content-per-unit
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: ASML-only named edge: BESI (the displaced D2W-bonding incumbent) is Amsterdam-listed, not US — no clean US-listed loser; stated additive for the tracked universe. ASML >ceiling ($606B mcap FY2026-10); the quant edge on this drift is the >ceiling-flagged anchor, filtered per convention. ASML FY2025 FMP product segments have no back-end/bonding line yet (NXE, ArF immersion, ArF dry, KrF, I-line, EXE, Metrology & Inspection, Net service) — engine matches on sector.

## Last Updated (2026-10-26)

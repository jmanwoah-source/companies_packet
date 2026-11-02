# DRIFT-004 — 0.33-NA EUV → High-NA (0.55-NA) EUV lithography (process-node)

**Class.** process-node / manufacturability shift (cheaper path to 1.4nm-class pitch at the exposure layer)
**Substitution.** 0.33-NA EUV steppers (N2/N2P, 18A generation) → 0.55-NA High-NA EUV at the ~1.4nm/10A-class step
**Sector.** semiconductors
**Secondary sectors.** ai-infrastructure (AI-die density)
**Value-chain layer(s) affected.** tools (fab/litho), manufacturing (foundry)
**Horizon tag:** medium (3-5 yr)
**Displacement sub-class:** content-per-unit (exposure-port premium + re-qualified metrology/etch; additive capex, not a dead line)

## Magnitude (mcap + revenue at stake)
- High-NA tools carry a ~2x price premium per exposure port vs 0.33-NA; adoption re-allocates
  foundry litho capex and re-qualifies metrology/etch content. Mostly >ceiling anchors (ASML);
  the sub-ceiling edge is the metrology/inspection content step (KLAC-class).
- Magnitude score = 6 ($1-3B realized exposure at first volume; large conditional ceiling).

## Timing (TRL → volume)
- TRL 5-6: 0.55-NA tools shipping to research lines; TSMC "still evaluating" (Reuters, 2025-05-27);
  Intel hedging 14A with a low-NA technique of identical yield/design rules (Tom's Hardware, 2025) —
  adoption at the next-next node, ~3-5 yrs. Timing score = 4.

## Certainty
- **demonstrated at tool level** (0.55-NA tools shipping to research lines), **claimed at volume
  level** (no foundry committed High-NA to HVM yet). Score = 6.

## Drift Score
| Component | Score (0-10) | Rationale |
|-----------|--------------|-----------|
| Magnitude | 6 | tool premium + re-qualified content; realized at first HVM volume |
| Timing | 4 | 3-5 yrs to the adoption node |
| Certainty | 6 | tools demonstrated, volume claimed |
| **Composite** | **144** | **EMERGING** |

Tier: **EMERGING (50-199)** — one foundry commitment flips certainty 6→9 → composite 216 → HIGH (auto re-rate).

## Status
- **scaling** (foundry commitment observed: Intel qualified High-NA EUV for 18A manufacturing layers + Panther Lake production; Samsung 18A/DRAM partnership expansion — re-rate dated 2026-10-26, note below).

## Winner Edges
| Ticker | cap-band | Company | Why advantaged | Moat | Evidence (dated, linked) |
|--------|----------|---------|----------------|------|--------------------------|
| ASML | >ceiling | ASML | only credible High-NA EUV source; tools shipping to research lines | ~90%+ GM, multi-year qualification lock | [2025-05-27] Reuters: TSMC still evaluating ASML's High-NA — VERIFIED |
| KLAC | anchor | KLA Corp | High-NA re-qualifies metrology/inspection content per wafer | metrology monopoly-adjacent | [2026] WFE structural upcycle, KLA backlog >$12B (Investing.com, cross-link DRIFT-001) — VERIFIED |

## Loser Edges
| Ticker | cap-band | Company | Why disadvantaged | Revenue exposure % | Certainty weight | sub_downside | Evidence |
|--------|----------|---------|-------------------|--------------------|------------------|--------------|----------|
| (class) | — | SALELE-class multi-patterning content providers | if Intel's low-NA hedge wins the 1.4nm step, patterning content loses share | est. low (class) | 0.3 (rumored) | est. <5 (low) | [2025] Tom's Hardware: Intel low-NA hedge w/ identical yield — VERIFIED |

> **Honest note:** additive at the tool layer; the only loser path is contingent on the low-NA
> hedge winning — flag low-confidence, do NOT put on the substitution short list as a clean row.

## Sequencing
- prerequisite-for → [DRIFT-001_gaa-node-transition.md](DRIFT-001_gaa-node-transition.md) (High-NA is the exposure-layer companion to GAA at the same nodes)
- competes-with → (low-NA + advanced packaging path — the Intel hedge; an unfiled counter-drift candidate)

## Competitive/Substitution Links
- ASML → TSM/UMC : upstream-supplier (litho gates the node step)
- ASML ↔ (Nikon/Canon legacy DUV class) : displaced (High-NA widens the EUV-only gap)

## Cascade Hook
- Gap-phrase: **"High-NA EUV HVM commitment metrology requalification"**
- Surface forms: `High-NA EUV "HVM" OR "high-volume" commitment`, `site:asml.com 0.55-NA tool delivery`,
  `"High-NA" metrology OR inspection content per wafer`, `low-NA alternative 14A yield`.
- Fires at Composite ≥ 500 (not near; watch for the foundry commitment → certainty re-rate).

## Evidence
- [2025-05-27] TSMC still evaluating ASML's 'High-NA' as Intel eyes future use — https://www.reuters.com/world/asia-pacific/tsmc-still-evaluating-asmls-high-na-intel-eyes-future-use-2025-05-27/ (VERIFIED)
- [2025] Intel hedges 14A with low-NA technique of identical yield and design rules — https://tomshardware.com/pc-components/cpus/intel-hedges-its-bet-for-high-na-euv-with-the-14a-process-node-an-alternate-low-na-technique-has-identical-yield-and-design-rules (VERIFIED)

## Open questions / next-cycle checks
- Confirm whether TSMC N2P or A14 is the first High-NA HVM candidate (the commitment date).
- Pull KLAC metrology segment revenue to fix the content-per-wafer exposure %.

## Dated Evidence Notes
- [2026-10-25] [seed004a] Filed from semiconductors pillar validation (salvaged sub-agent evidence).
- [2026-10-25] [det004a] Intel has exposed >1M wafers using High-NA systems and plans continued volume (ASML record $13B qtr, Tom's Hardware, 2026-10-15) — strengthens the tool-level demonstrated status; volume-HVM commitment still pending. Certainty held at 6 (score unchanged 144 EMERGING; re-rate on a foundry HVM commit). https://www.tomshardware.com/tech-industry/semiconductors/asml-reports-record-usd13-billion-quarter-vows-to-ex (VERIFIED)
- [2026-10-26] [det004c] Two secondary datapoints (aggregator-sourced, no re-rate): (1) eBeam Initiative 2026 Luminaries Survey (SPIE): 85 experts from 45 companies anticipate 12-inch mask adoption by 2031 — High-NA's downstream consumable/mask-layer implication. (2) Adoption timelines re-circulated: High-NA EUV in production (Intel, >1M wafers consistent with det004a), Samsung mass production planned 2028, TSMC 2030; ASML expects gradual adoption, no immediate revenue spike. Certainty held at 6 (score unchanged 144 EMERGING; re-rate on a foundry HVM commit). https://www.kucoin.com/news/flash/industry-experts-discuss-12-inch-mask-adoption-and-high-na-euv-progress (UNVERIFIED — aggregator) · https://www.kucoin.com/news/flash/asml-high-na-euv-adoption-timelines-for-intel-samsung-tsmc-revealed (UNVERIFIED — aggregator)
- [2026-10-26] [det004b] GATE-FIRE OBSERVED: Market Ontology catalyst (evidence through 2026-09-11, rev 1 2026-10-25) — "ASML expanded High-NA EUV deployment partnerships with Intel and Samsung. Intel qualified High-NA EUV for 18A manufacturing layers and Panther Lake production." (underlying source: ASML expands High-NA ties with Samsung and Intel, 2026-09-10). Status transitioned emerging → scaling per file rule ("Moves to scaling on a foundry HVM commitment"). M/T/C held at 6/4/6 (composite 144 EMERGING) — foundry commitment noted, demonstrated production volume not yet evidenced; certainty re-rate (6→9) deferred until 18A HVM volume is observed. https://marketontology.com/catalysts/2026-09-11/asml-expands-high-na-euv-ties-as-intel-moves-tech-to-panther-lake-and-18a-layers-992f35 (UNVERIFIED — single aggregator source; primary ASML/Intel statement not yet located)
- [2026-10-27] [605a1f79] Leg A rescan datapoint (no re-rate): TSMC + ASML exploring 12-inch photomasks to unlock High-NA EUV's full-field capability for 2nm/angstrom-era nodes (DigiTimes, 2026-10-12) — mask-layer (consumables) extension of the High-NA adoption path, consistent with the eBeam 2031 12-inch-mask survey in det004c; still no HVM volume commit, C held at 6 (144 EMERGING). https://digitimes.com/news/a20261012PD204/tsmc-asml-high-na-euv-12-inch-manufacturing.html (UNVERIFIED — aggregator snippet)
- [2026-10-28] [b4d547df] Leg A rescan datapoint (no re-rate): Hitachi High-Tech + ZEISS accelerate a joint development framework for defect inspection for 2nm-node HVM with High-NA-EUV lithography (Hitachi High-Tech news release, 2026-09-30) — downstream metrology/inspection tooling layer extending the High-NA adoption stack beyond litho itself; no new US-listed winner edge (Hitachi = TYO, ZEISS = XETRA), C held at 6 (144 EMERGING). https://www.hitachi-hightech.com/global/en/news/nr20260930.html (VERIFIED — direct primary URL)
- [2026-10-28] [c1a0f2e9] Leg A rescan datapoint (no re-rate; DRIFT-004 already filed → confirmatory, not a new event): Micron (MU) roadmap names wafer bonding on its 1ε DRAM process (in development) and High-NA EUV in later DRAM generations, with vHBM/vEIM custom-HBM mass production targeted 2028 (XenonSpectrum/Mezha, 2026-10). This is a DRAM-side roadmap commitment to High-NA at the exposure layer — claimed (roadmap, 2028), consistent with the det004c aggregator timelines (Samsung 2028 / TSMC 2030); no new US-listed winner edge (ASML/KLAC already named in DRIFT-004), C held at 6 (144 EMERGING). https://xenospectrum.com/en/micron-dram-bonding-vertical-memory/ (UNVERIFIED — secondary).
- [2026-10-28] [e53bc3e2] Same-story re-scan datapoint (no re-rate): Micron wafer-bonding + High-NA EUV DRAM roadmap re-circulated on two new URLs (gate.com 25211122, ramtrend #5287) — same event as c1a0f2e9, confirmatory only; C held at 6 (144 EMERGING). https://www.gate.com/news/detail/MU/micron-plans-wafer-bonding-and-high-na-euv-for-next-gen-dram-25211122 · https://ramtrend.com/news/5287-micron-maps-wafer-bonding-and-high-na-euv-into-its-dram-roadmap (UNVERIFIED — secondary).

- [2026-10-30] [det004d] Two tools-layer datapoints (no re-rate): (1) Lam Research + imec demonstrated 100% electrical yield for ruthenium direct-metal-etch structures at 20nm pitch with a single High-NA EUV exposure — validates Lam's Aether dry-resist platform for angstrom-era patterning; joint Lam-imec commitment (newsroom 2026-10-27) extends to 3D integration + next-gen memory. LRCX is a named tools-layer winner edge (dry-resist/patterning); LRCX not yet in the sidecar — formalize next cycle. (2) TSMC High-NA EUV 2030 HVM commitment re-circulated (consistent with det004c). Certainty held at 6 (re-rate trigger = foundry HVM volume, TSMC 2030 is roadmap-stage; score unchanged 144 EMERGING). https://newsroom.lamresearch.com/lam-imec-3d-integration-dry-resist-ai-semiconductor-scaling (VERIFIED) · https://www.techtimes.com/articles/329679/20261029/lam-research-imec-prove-dry-resist-ready-high-na-euv-ruthenium-interconnects.htm (VERIFIED via fetch).

## ENGINE SCORE (deterministic — do not hand-edit)
_Computed by drift_scoring.py v2 on 2026-11-02 from FMP revenue-product-segmentation + profile-symbol (script-reachable FMP MCP) + curated sidecar `DRIFT-004.engine.json`. Same inputs -> same output._

**Exposure & sub_downside (loser legs = Track D source; winner legs = upside):**

| Ticker | Role | Revenue exposure % | Mcap ($B) | sub_downside | FMP sector (layer) | Matched segments |
|--------|------|--------------------|-----------|--------------|--------------------|------------------|
| ASML | winner | 0.0% (FY2025) | 603.5 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |
| KLAC | winner | 0.0% (FY2026) | 205.8 | - (upside) | Technology -> tools (fab/litho) / manufacturing — see drift layer fields | - |

**Composite (M x T x C): 6 x 4 x 6 = **144** -> tier **EMERGING**
  - Mcap at stake: $0.0B (engine sum of loser exposure x mcap unless curated) | certainty_grade: pilot
  - timing_years: 3 | displacement_sub_class: content-per-unit
  - sub_downside weights: demonstrated=1.0 / pilot=0.8 / claimed=0.6 / rumored=0.3
  - note: Additive at tool layer; loser path contingent on the Intel low-NA hedge. Whole-company proxy for ASML/KLAC (coarse segments).

## Last Updated (2026-10-25)

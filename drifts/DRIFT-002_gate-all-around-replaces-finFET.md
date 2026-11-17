# DRIFT-002: Gate-All-Around Transistors Replace FinFET, Doubling Etch/Deposition Content per Wafer

## Substitution Event

**M (Market Impact):** 8 — The industry transition from FinFET to gate-all-around (GAA) transistor architecture at 2nm and below is non-optional for continued AI compute scaling. Equipment content per wafer doubles on the transition. Lam Research explicitly quantifies $1B SAM expansion per 100K wafer starts of GAA capacity. Applied Materials has GAA-specific tool families already in production.

**T (Technology):** 8 — Physical/process swap: FinFET (3-sided gate control) → GAA (4-sided gate control, horizontal nanosheet or nanowire channel). This requires fundamentally different etch profiles (deep, narrow 3D trenches with angstrom-level precision), atomic layer deposition for new contact metals (molybdenum replacing tungsten), and selective deposition processes. The geometry demands perpendicular etch and deposition that 2D processes cannot achieve.

**C (Certainty):** 8 — Demonstrated/committed. Applied Materials announced its GAA tool families (Viva radical treatment, Sym3 Z Magnum etch, Spectral ALD for molybdenum contacts) in Feb 2026 as being "used by multiple leading foundry-logic manufacturers." 2nm-class GAA chips are in volume production in 2026. Lam Research CFO confirmed GAA tool deployments with $1B SAM per 100K wafer starts at multiple investor conferences in 2026.

| Parameter | Score | Rationale |
|-----------|-------|-----------|
| M (Market Impact) | 8 | AI compute scaling wall requires GAA; every leading foundry (TSMC, Samsung, Intel) has committed. Equipment SAM doubles per wafer. |
| T (Technology) | 8 | FinFET → GAA is a specific, well-defined physical swap with clear equipment requirements (3D trench etch, ALD, selective deposition). |
| C (Certainty) | 8 | Volume production at 2nm in 2026; AMAT and LRCX tools already in customer fabs. Not roadmap — shipped. |
| **COMPOSITE** | **512** | |

**Timing:** 2026–2029. 2nm GAA entered volume production in 2026. Angstrom node (sub-2nm) GAA follows through 2027–2028. Full industry adoption of GAA across all leading logic nodes by 2029.

**Displacement Sub-class:** Enabling Infrastructure — the new architecture enables continued compute scaling without directly displacing end-product revenue. The displacement is on equipment/process side, not end-market.

## Old → New

| Aspect | Old (Being Replaced) | New (Replacement) |
|--------|---------------------|-------------------|
| Transistor Architecture | FinFET (3-sided gate control, vertical fin channel) | GAA (4-sided gate control, horizontal nanosheet or nanowire channel) |
| Value Chain Layer | Front-end etch + deposition for 2D planar-ish structures | Front-end etch + deposition for 3D nanosheet structures (deeper, narrower, more conformal) |
| Key Constraint | FinFET electrostatic control limits at sub-5nm; leakage becomes unacceptable | Nanosheet edge roughness, selective deposition precision, 3D trench profile control |
| Economic Driver | Cost-performance scaling wall; GAA is non-optional for continued AI compute scaling | Equipment vendors with GAA-specific tool portfolios capture doubled content per wafer |

## Winners

| Company | Ticker | Role | Exposure Estimate |
|---------|--------|------|-------------------|
| Lam Research | LRCX | GAA etch and deposition tool leader; Akara conductor etch platform for GAA; $1B SAM per 100K wafer starts of GAA capacity | Dominant etch position; 2nm GAA tools in volume production with multiple customers |
| Applied Materials | AMAT | GAA tool family (Viva radical treatment, Sym3 Z Magnum etch, Spectral ALD for molybdenum contacts); "tool-of-record" status in 2nm logic | Broad deposition + materials engineering lead; 250+ Sym3 Z chambers already in field |
| KLA | KLAC | Inspection and metrology for 3D nanosheet structures; tighter process windows on GAA geometries | Established metrology leader; additional inspection steps required for 3D GAA verification |

## Losers

| Company | Ticker | Role | Exposure Estimate |
|---------|--------|------|-------------------|
| Legacy FinFET tool install base | — | Equipment vendors without GAA-specific tool portfolios face content risk as FinFET transitions to GAA | Niche — most major equipment vendors have GAA roadmaps but late movers face SAM erosion |
| Single-die customers committed to monolithic FinFET designs | — | Companies whose chip designs are optimized for FinFET must redesign for GAA or lose performance advantage | Strategic risk, not financial displacement — no named public companies with material FinFET-only exposure |

**Note:** This is primarily an enabling infrastructure shift. The equipment suppliers (LRCX, AMAT, KLAC) are the clear winners. There is no clean end-market loser — the transition benefits compute companies that adopt GAA early and penalizes those that don't, but the financial exposure is at the equipment supplier level.

## Evidence

- **2026-02-10:** Applied Materials unveils GAA transistor and wiring innovations — Viva radical treatment, Sym3 Z Magnum etch, Spectral ALD for molybdenum contacts. "Being used by multiple leading foundry-logic manufacturers." Source: [AMAT Press Release](https://investor.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-transistor-and-wiring-innovations/) — **VERIFIED**
- **2026-04-14:** Lam Research announces "everything is going 3D" — deposition and etch intensity rising ~2x for 3D architectures including GAA. Akara conductor etch platform targeting GAA. Source: [Lam Research Newsroom](https://newsroom.lamresearch.com/how-deposition-and-etch-are-reshaping-chips-for-the-ai-era) — **VERIFIED**
- **2026-09-10:** Lam Research CFO (Doug Bettinger) at Goldman Sachs Communacopia: "Gate-all-around is showing up right now in the industry... for every 100,000 wafer starts of capacity that gets put in place, our SAM expands by $1 billion." Source: [Stock Analysis Transcript](https://stockanalysis.com/stocks/lrcx/transcripts/740234-goldman-sachs-communacopia-technology-conference-2026/) — **VERIFIED**
- **2026-03-03:** Lam Research CFO at Morgan Stanley: "In 2024, SAM as % of WFE was low 30s%. In 2025, mid-30s%... moves to high 30s% as GAA, backside power, advanced packaging scale." 59% foundry/logic vs 60% memory flip. Source: [MS Transcript](https://stockanalysis.com/stocks/lrcx/transcripts/560487-morgan-stanley-technology-media-telecom-conference-2026/) — **VERIFIED**
- **2026-11-09:** Lam Research stock moved +8.4% on news of "structural migration toward gate-all-around architectures, which significantly expands the etch and deposition intensity per wafer." Source: [TradingKey](https://www.tradingkey.com/news/market-movers/262296797-market-movers-lrcx-20261109) — **VERIFIED**

## Risk Factors

- GAA adoption pace could slow if foundry capacity investments are delayed by macro conditions
- Lam Research's SAM expansion assumption ($1B/100K wafer starts) may overestimate actual volume deployment rates
- Applied Materials' GAA tool portfolio is broad but faces execution risk on new product lines at angstrom nodes
- End-customer (NVIDIA, AMD, etc.) demand for AI compute could moderate, reducing overall WFE spend

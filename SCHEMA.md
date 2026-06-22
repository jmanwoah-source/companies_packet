# SCHEMA — Domain Knowledge Taxonomy

## Four Research Pillars

### 1. Semiconductor
Sub-topics: chip design, analog/mixed-signal, packaging, lithography, materials, photonics, foundries, EDA, IP, equipment

### 2. Advanced Energy & Grid
Sub-topics: nuclear/SMR, grid distribution, uranium/fuel, storage, microgrids, transmission, power electronics

### 3. AI Infrastructure & Thermal
Sub-topics: data center cooling, liquid immersion, power ICs, industrial electrical, interconnects, optical, PCBs

### 4. Physical AI & Edge Automation
Sub-topics: counter-UAS, autonomous defense sensors, industrial robotics, edge compute, actuation, perception

## Entity Types

| Tag | Description |
|-----|-------------|
| @company | Public/private company |
| @technology | Specific tech or process |
| @product | Named product or platform |
| @material | Raw material or substrate |
| @process | Manufacturing or fabrication process |
| @standard | Industry standard or protocol |

## Analysis Types

| Tag | Description |
|-----|-------------|
| @supply-chain | Supply chain mapping/relationships |
| @catalyst | Event or change driver |
| @competitive | Moat/differentiation analysis |
| @market-dynamics | Supply-demand, pricing, capacity |
| @regulatory | Policy, export, compliance |
| @financial | Valuation, margins, capex, balance sheet |

## Concept Types

| Tag | Description |
|-----|-------------|
| @framework | Analytical framework or model |
| @paradigm | Industry paradigm shift |
| @inflection | Structural inflection point |
| @disruption | Disruptive force or pattern |
| @relationship | Connection between entities/technologies |

## File Convention

- `entities/` — domain entities (companies, tech, products, materials)
- `concepts/` — analytical frameworks, paradigms, inflection points
- `comparisons/` — side-by-side entity comparisons
- `queries/` — answered research questions with context
- `raw/articles/` — source material (articles, reports, filings)
- `_archive/` — superseded or obsolete content

## Cross-Linking Standard

All pages use `[[wikilinks]]` for relationships. Every entity page must link to at least one pillar and one concept.
Every concept page must link to all relevant entities and pillars.

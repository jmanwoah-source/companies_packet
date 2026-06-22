# SCHEMA — Knowledge Base Organization

## Entity Types
- `@company` — organizations, brands, institutions
- `@technology` — software, hardware, protocols, methods
- `@person` — individuals, researchers, figures
- `@concept` — ideas, frameworks, theories
- `@place` — locations, markets, regions
- `@event` — historical, upcoming, catalysts
- `@product` — named products or platforms
- `@material` — raw materials, substrates, resources

## Analysis Types
- `@supply-chain` — supply chain mapping/relationships
- `@catalyst` — event or change driver
- `@competitive` — moat/differentiation analysis
- `@market-dynamics` — supply-demand, pricing, capacity
- `@regulatory` — policy, export, compliance
- `@financial` — valuation, margins, capex, balance sheet

## Concept Types
- `@framework` — analytical framework or model
- `@paradigm` — industry paradigm shift
- `@inflection` — structural inflection point
- `@disruption` — disruptive force or pattern
- `@relationship` — connection between entities/technologies

## File Convention

- `entities/` — domain entities (companies, tech, people, products, materials)
- `concepts/` — analytical frameworks, paradigms, inflection points
- `comparisons/` — side-by-side entity comparisons
- `queries/` — answered research questions with context
- `raw/` — source material (articles, reports, filings, URLs)
- `_archive/` — superseded or obsolete content

## Cross-Linking Standard

All pages use `[[wikilinks]]` for relationships.
Every entity page must link to at least one concept.
Every concept page must link to all relevant entities.

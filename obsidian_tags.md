---
generated: 2026-11-19
source: build_obsidian_packet.py
description: >
  Reference file for Obsidian Graph View filtering. Each section lists every
  tag value currently in the Obsidian packet, grouped by property dimension.
  Use Obsidian's "Search in properties" panel to filter by any of these.
---

# Obsidian Tag Reference — Companies Packet

## Filterable Property Keys (YAML frontmatter)

| Property | Type | Values | Use Case |
|----------|------|--------|----------|
| `ticker` | string | All tickers | Exact match |
| `title` | string | All company names | Search by name |
| `sector` | string | Sector names (FMP) | Group by sector |
| `industry` | string | Industry names (FMP) | Sub-sector grouping |
| `price` | number | Current price | Filter by price range |
| `market_cap` | number | Dollar amount | Filter by mcap range |
| `mcap_band` | string | mega, large, mid, small, micro, nano, unknown | Filter by market cap band |
| `pillar` | string | Domain pillar | Filter by pillar |
| `category` | string | Signal brief category | Filter by signal category |
| `score_a` | number | 0–100 | Track A score filter |
| `score_b` | number | 0–100 | Track B score filter |
| `score_c` | number | 0–100 | Track C score filter |
| `best_track_score` | number | 0–100 | Best of A/B/C |
| `tier` | string | Tier name | Filter by tier |
| `commercialization` | string | Stage | Filter by commercialization |
| `brief_count` | number | Count of briefs | Filter by signal count |
| `brief_count_nonzero` | number | Count (if > 0) | Filter for tickers with active briefs |
| `watchlist_status` | string | WATCH, DORMANT | Filter by watchlist status |
| `entity_check` | string | ok | Filter for validated entities |
| `is_mirage` | boolean | true / false | Filter mirage tier tickers |
| `short_interest_float` | number | Short % of float | Filter by short interest |
| `short_interest_pct_outstanding` | number | Short % of outstanding | Filter by short interest |
| `days_to_cover` | number | Days | Filter by short interest |
| `short_interest_delta_pct` | number | Change % | Filter by short interest movement |
| `latest_catalyst_date` | date | ISO date | Filter by catalyst recency |
| `total_briefs` | number | Total brief count | Filter by total brief count |
| `tags` | array | See tag sections below | Composite filter |

---

## Tag Values by Category

### #sector/ — Sector tags (FMP sector classification)
```
#sector/ai-infra-data
#sector/ai-infra-thermal
#sector/basic-materials
#sector/critical-materials
#sector/defense-gov
#sector/energy-grid-smr
#sector/healthcare
#sector/physical-ai-robotics
#sector/quantum
#sector/semi-subsystems
#sector/technology
#sector/utilities
```

### #industry/ — Industry tags (FMP industry classification)
```
#industry/ai-infra-data
#industry/ai-infra-thermal
#industry/biotechnology
#industry/chemicals-specialty
#industry/computer-hardware
#industry/critical-materials
#industry/defense-gov
#industry/energy-grid-smr
#industry/information-technology-services
#industry/medical-diagnostics-&-research
#industry/physical-ai-robotics
#industry/quantum
#industry/renewable-utilities
#industry/semi-subsystems
#industry/semiconductors
#industry/software-application
#industry/software-infrastructure
```

### #pillar/ — Pillar tags (Research domain)
```
#pillar/ai-infra-data
#pillar/ai-infra-thermal
#pillar/defense-gov
#pillar/energy-grid-smr
#pillar/physical-ai-robotics
#pillar/quantum
#pillar/semi-subsystems
#pillar/technology
#pillar/untagged
```

### #mcap/ — Market cap band tags
```
#mcap/mega    (≥$200B)
#mcap/large   (≥$10B, < $200B)
#mcap/mid     (≥$2B, < $10B)
#mcap/small   (≥$300M, < $2B)
#mcap/micro   (≥$50M, < $300M)
#mcap/nano    (< $50M)
#mcap/unknown (no mcap data)
```

### #commercialization/ — Commercialization stage tags
```
#commercialization/pre-revenue
#commercialization/pilot
#commercialization/scale
```

### #score-a/ — Track A score band tags (fundamental + catalyst)
```
#score-a/elite          (≥75)
#score-a/strong         (50–74)
#score-a/below-threshold (<50)
```

### #score-b/ — Track B score band tags (technical/short)
```
#score-b/strong     (50–74)
#score-b/below-threshold (<50)
```

### #score-c/ — Track C score band tags (valuation/momentum)
```
#score-c/elite      (≥75)
#score-c/strong     (50–74)
#score-c/below-threshold (<50)
```

### #tier/ — Tier classification
```
#tier/below_55
#tier/high
#tier/moderate
```

### #watchlist/ — Watchlist status
```
#watchlist/watch
#watchlist/dormant
```

### #status/ — Special status
```
#status/mirage
```

---

## Recommended Graph View Filters

### High-Conviction Plays (Score A ≥ 75, Any mcap)
```yaml
property: score_a
operator: >=
value: 75
```

### Deep Small-Cap Research (small mcap, Score A ≥ 40)
```yaml
property: mcap_band
operator: ==
value: small
AND
property: score_a
operator: >=
value: 40
```

### Active Signal Targets (brief_count > 0, not mirage)
```yaml
property: brief_count_nonzero
operator: >=
value: 1
AND
property: is_mirage
operator: !=
value: true
```

### Short Squeeze Candidates (days_to_cover > 5, float > 5%)
```yaml
property: days_to_cover
operator: >=
value: 5
AND
property: short_interest_float
operator: >=
value: 5
```

### Pre-Revenue with High Conviction (pre-revenue, Score A ≥ 50)
```yaml
property: commercialization
operator: ==
value: pre-revenue
AND
property: score_a
operator: >=
value: 50
```

### Mega-Cap Anchors (defense/gov sector, mega-cap)
```yaml
property: pillar
operator: ==
value: defense-gov
AND
property: mcap_band
operator: ==
value: mega
```

---

## Obsidian Search Syntax Examples

### Filter by pillar + mcap band:
```
search: "pillar: defense-gov" AND "mcap_band: small"
```

### Find tickers with active briefs in semiconductor pillar:
```
search: "brief_count_nonzero: >=1" AND "pillar: semi-subsystems"
```

### Find mirage-tier tickers (potential traps):
```
search: "is_mirage: true"
```

### Find tickers with high short interest:
```
search: "short_interest_float: >=10"
```

### Find all active research targets (not dormant, not mirage):
```
search: "watchlist_status: WATCH" AND "is_mirage: false"
```

### Best of A/B/C ≥ 60, mid-cap or small-cap:
```
search: "best_track_score: >=60" AND "mcap_band: mid"
```

### All defense-gov with scale commercialization:
```
search: "pillar: defense-gov" AND "commercialization: scale"
```

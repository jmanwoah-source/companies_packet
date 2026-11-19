---
generated: 2026-11-19
source: build_clean_packet.py
description: >
  Reference file for Obsidian Graph View filtering. Each section lists every
  tag value currently in the Obsidian packet, grouped by property dimension.
  Use Obsidian's 'Search in properties' panel to filter by any of these.
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
| `score_a` | number | 0–100 | Track A score filter |
| `score_b` | number | 0–100 | Track B score filter |
| `score_c` | number | 0–100 | Track C score filter |
| `best_track_score` | number | 0–100 | Best of A/B/C |
| `tier` | string | Tier name | Filter by tier |
| `brief_count` | number | Count of briefs | Filter by signal count |
| `watchlist_status` | string | WATCH, DORMANT | Filter by watchlist status |
| `entity_check` | string | ok | Filter for validated entities |
| `is_mirage` | boolean | true / false | Filter mirage tier tickers |
| `short_interest_float` | number | Short % of float | Filter by short interest |
| `days_to_cover` | number | Days | Filter by short interest |
| `short_interest_delta_pct` | number | Change % | Filter by short interest movement |
| `latest_catalyst_date` | date | ISO date | Filter by catalyst recency |
| `tags` | array | See tag sections below | Composite filter |

---

## Tag Values by Category

### #sector/ — Sector tags

### #industry/ — Industry tags

### #mcap/ — Market cap band tags

### #pillar/ — Domain pillar tags

### #score-a/ — Track A score band tags

### #score-b/ — Track B score band tags

### #score-c/ — Track C score band tags

### #tier/ — Tier classification

### #watchlist/ — Watchlist status

### #entity-check/ — Entity validation

### #status/ — Special status


# Cron Job Endpoint Mapping

## Data Source Architecture

All cron jobs use a unified data sourcing strategy. **No dead endpoints, no deprecated services, no OpenBB calls.** Every data point is gathered from live web search and the single working FMP search endpoint.

---

## WORKING Tools

### `mcp_exa_search_web_search_exa`
- **Purpose:** Company search, financial data, news, catalysts, profile data, market cap
- **How:** Natural language queries against live web content
- **Use cases:** Revenue, margins, EBIT, market cap, CEO info, employee count, FCF, total assets, total liabilities, EBIT, current assets, current liabilities, retained earnings, stock price, recent news, catalysts, competitive analysis
- **All pillar scans use this as their primary data source**

### `mcp_fmp_search_search_symbol`
- **Purpose:** Ticker discovery and cross-reference
- **Status:** Only working FMP endpoint with your API key
- **Use cases:** Search by company name, sector, industry to get ticker lists

---

## DEAD Endpoints (Removed)

The following FMP endpoints return 401 Invalid API KEY and have been removed from ALL cron jobs:

- `mcp_fmp_quote` — quote/price data
- `mcp_fmp_statements` — balance sheet, income statement, cash flow
- `mcp_fmp_company` — company profiles
- `mcp_fmp_news` — stock news
- `mcp_fmp_search` — other search variants (only search_symbol works)
- `Alpha Vantage` — deprecated service, no longer used

**FMP limitation:** Your paid FMP key only supports `search_symbol`. All other FMP endpoints return 401. This is a known limitation of your current API access tier.

---

## What OpenBB Would Provide (Not Installed)

OpenBB is configured in config.yaml but **not installed** on this system. If installed, OpenBB would provide:
- Real-time quotes and historical prices
- Financial statements (income, balance sheet, cash flow)
- Company profiles and executive data
- News aggregation
- Screening and filtering by market cap, sector, etc.
- Options data (chains, flow, Greeks)

**Current workaround:** All financial data is gathered via natural language web search queries using exa-search. This works for fundamental data, news, and catalysts — not for intraday quotes, options chains, or short interest.

---

## Per-Job Tool Map

| Job ID | Name | Primary Tool | FMP Search |
|--------|------|-------------|------------|
| 5eb337f0d31e | Pillar Scan 1A — Semiconductor Nano/Micro | exa-search | yes (ticker discovery) |
| 15adcdad1f09 | Pillar Scan 1B — Edge AI Nano/Micro | exa-search | yes (ticker discovery) |
| 56cbe31a58ac | Pillar Scan 2 — AI Infrastructure Mid-Cap | exa-search | no |
| acd76aadabe4 | Pillar Scan 3A — Robotics Large-Cap | exa-search | no |
| cb474d268364 | Pillar Scan 3B — Semiconductor Large-Cap | exa-search | no |
| ed0f324214c8 | Pillar Scan 1C — Robotics Micro/Mid-Cap | exa-search | yes (ticker discovery) |
| 888e632b8007 | Altman Z-Score DeepScan | exa-search | no |
| 1eec372603ac | Tier 1 Wiki Population | exa-search | no |

**All jobs:** Zero dead endpoint references. Zero Alpha Vantage references. Zero FMP references outside search-symbol. All financial data gathered via exa-search web search.

---

## What This CAN'T Provide (Known Gaps)

| Data Type | Source | Status |
|-----------|--------|--------|
| Real-time quotes | FMP / OpenBB | Both unavailable |
| Options chains | FMP / OpenBB | Both unavailable |
| Options flow | FMP / OpenBB | Both unavailable |
| Short interest | FMP / OpenBB | Both unavailable |
| Intraday volume | FMP / OpenBB | Both unavailable |
| RVOL calculations | FMP / OpenBB | Both unavailable |

**Mitigation:** Pillar scans 1A, 1B, and 1C use exa-search which can find recent volume/margin data from news sources and financial websites. The Z-Score and Wiki jobs compute financial ratios from reported balance sheet data found via search.

---

## Future Upgrade Path

To restore real-time quotes, options data, and RVOL calculations:

1. **Install OpenBB:** `pip install openbb` (not currently installed)
2. **Upgrade FMP API:** Contact Financial Modeling Prep for quote/financials endpoint access on your tier
3. **Alternative:** Use yfinance (free) for quotes and basic financials as a fallback

See `~/wiki/concepts/trading-data-architecture.md` for full data pipeline design.

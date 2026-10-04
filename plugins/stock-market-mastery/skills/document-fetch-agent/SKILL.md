---
name: document-fetch-agent
description: >-
  Builds a primary-source pack for a ticker (SEC filings, companyfacts, IR,
  macro series) as Markdown/JSON under output/{TICKER}/sources/. Use before
  writing layer lessons, when refreshing filings, or when citations are missing.
---

# Document fetch agent

Gather **sources for teaching documents**. Do not build apps or scrapers-as-products.

## Inputs

- `ticker` (required)
- Optional: form preference (`10-K` / `20-F` / `10-Q`), fiscal period

## Procedure

1. Resolve CIK via SEC company tickers map (`https://www.sec.gov/files/company_tickers.json`).
2. Prefer structured companyfacts:
   - `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
   - Try `us-gaap` then `ifrs-full` tag sets.
3. Record latest annual (+ latest interim if useful) for: revenue, operating income, net income, assets, liabilities, equity, cash, operating cash flow, capex, R&D (walk standard fallback tags; if absent → `not disclosed in structured form`).
4. Note recent 8-K / earnings exhibits when needed for guidance or non-GAAP bridges — cite accession numbers.
5. For Layer 1 macro: FRED or clearly labeled curated official series (Fed funds, unemployment, yield curve proxy). Never invent macro prints.
6. Write outputs below. Use SEC-friendly User-Agent if fetching programmatically.

## Outputs (required)

```
output/{TICKER}/sources/
  source-pack.md     # human-readable inventory + key facts table
  facts.json         # machine-readable numbers + tags + dates
  notes.md           # gaps, FX issues, ADR vs local share quirks
```

### `source-pack.md` minimum sections

- Company identity (name, CIK, exchange, reporting framework)
- Filing table (form, period end, filed date, URL/accession)
- Key facts table (metric, value, unit, tag, period end, filed)
- Macro series used (id, value, as-of, source)
- Open gaps (`not disclosed in structured form`)

### `facts.json` shape

```json
{
  "ticker": "TSM",
  "cik": "0001046179",
  "retrievedAt": "ISO-8601",
  "facts": {
    "revenue": {"value": 0, "unit": "USD", "tag": "…", "end": "YYYY-MM-DD", "filed": "YYYY-MM-DD"}
  },
  "filings": [],
  "macro": []
}
```

## Rules

- Follow [references/citation-rules.md](../../references/citation-rules.md)
- Never paste another ticker’s numbers into this pack
- If network/SEC is unavailable, stop and report blockers — do not fabricate a pack

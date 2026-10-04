# Citation rules

Every factual claim that is company- or market-specific needs a citation chip in this form:

```markdown
> **Source:** {Document / series} · {publisher} · filed/as-of {YYYY-MM-DD} · retrieved {YYYY-MM-DD} · {URL or accession if available}
```

## Allowed primary sources (prefer in order)

1. SEC EDGAR (10-K, 10-Q, 20-F, 8-K, DEF 14A, companyfacts XBRL)
2. Company IR (earnings release, presentation) — only for segment/KPI detail not in SEC structured data
3. Official macro series (FRED, BLS, central bank) for Layer 1
4. Explicitly labeled “illustrative / teaching example” for pedagogy that is not a live fact

## Fallback language

If a structured tag is missing after walking fallbacks:

> not disclosed in structured form

Do not invent a substitute number.

## Source pack

`document-fetch-agent` writes `sources/source-pack.md` and `sources/facts.json`. Layer agents must cite from that pack or add a new cited source to the pack when they introduce a new document.

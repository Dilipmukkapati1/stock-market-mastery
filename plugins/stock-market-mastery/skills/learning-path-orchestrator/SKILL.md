---
name: learning-path-orchestrator
description: >-
  Orchestrates a Stock Market Mastery company book for a ticker: by default the
  two-part company book (Part One executive summary + Part Two deep research),
  written to Markdown and optionally exported to EPUB. Use when the user asks
  for a company book, company analysis, or a book on a ticker. Only when the
  user explicitly asks for a "curriculum" or "learning-path" edition does it
  produce the legacy seven-layer teaching format with quizzes.
---

# Company book orchestrator

Produce a **document book**, never application code.

## Format decision (read first)

- **Default: the two-part company book** — company-focused and in-depth, no quizzes, checklists, or framework chapters. This is the owner's standing preference (2026-10-21; see [references/writing-standards.md](../../references/writing-standards.md), "The company-first rule").
- **Legacy curriculum edition** — seven layers with concept blocks and quizzes — **only** if the owner explicitly requests a curriculum/learning-path edition in this task. Never default to it, never mix the two formats in one book.

## Inputs

- `ticker` (required), e.g. `NVDA`, `GOOGL`, `INTC`
- Optional: `companyName`, `asOf` date, `outDir` (default `output/{TICKER}/`)

## Non-negotiables

1. Read [references/writing-standards.md](../../references/writing-standards.md)
2. Read [references/layer-specs.md](../../references/layer-specs.md) (slot mapping + chapter specs)
3. Read [references/citation-rules.md](../../references/citation-rules.md)
4. Follow [templates/layer-lesson.md](../../templates/layer-lesson.md) (chapter template)

## Workflow (two-part default)

```
Book progress for {TICKER}:
- [ ] 1. document-fetch-agent → sources/ (source-pack.md, facts.json)
- [ ] 2. 00-front-matter.md + meta.json (include "format": "two-part")
- [ ] 3. Part One chapters (slots 01–06): Management, The Company, Financials, The Product, Product Quality, Customers
- [ ] 4. Part Two chapters (slots 07–08, +09 if needed): deep research
- [ ] 5. content-grader-agent (fix blockers)
- [ ] 6. Offer epub-export → <CompanyName>.epub
```

### Step 1 — Source pack

Invoke **document-fetch-agent** for `{TICKER}`. Do not invent filings. Research beyond filings (industry data, product status, analyst debate) must be dated and labeled per the citation rules.

### Step 2 — Front matter

Write `output/{TICKER}/00-front-matter.md`: company name, ticker, CIK, reporting framework, how the book is organized (Part One / Part Two), the primary documents used, and the educational disclaimer. Write `meta.json` from [templates/meta.json](../../templates/meta.json) plus `"format": "two-part"`.

### Step 3 — Part One (slots 01–06)

Write each chapter per the specs in layer-specs.md, using the agent skills as content specialists:

| Slot file | Chapter | Lead skill |
| --- | --- | --- |
| `01-market.md` | Management | company-profile-agent |
| `02-industry.md` | The Company | company-profile-agent (industry-structure-agent supports) |
| `03-company.md` | Financials | financials-agent |
| `04-financials.md` | The Product | product-tech-agent |
| `05-earnings.md` | Product Quality | product-tech-agent |
| `06-products.md` | Customers | company-profile-agent (supply-chain-agent supports) |

Short and high-level (≈500–900 words each), numbers-led, cited.

### Step 4 — Part Two (slots 07–08, optional 09)

Deep research, ≈1,200–2,200 words per chapter:

- `07-supply-chain.md` — Deep research I: industry and business model in depth; moat hypotheses with evidence; the multi-year financial story; the latest earnings event dissected (earnings-agent).
- `08-document-literacy.md` — Deep research II: products/technology in depth (product-tech-agent); supply chain (supply-chain-agent); competition; valuation and market context (market-context-agent); risks, bull/bear.
- `09-capstone.md` — optional third deep-research chapter when the company's story demands one (e.g., a silicon program, a foundry build-out). Omit the file otherwise. **Never** write a capstone *assignment* in a two-part book.

Do **not** create `10-quizzes.md` or a consolidated `book.md` in the two-part format (a `book.md` collapses the EPUB to a single chapter).

### Step 5 — Grade + EPUB

1. Run **content-grader-agent** on `output/{TICKER}/`; fix blockers.
2. epub-export when the user wants Kindle/EPUB (default yes if they said so).

## Curriculum mode (only on explicit request)

If — and only if — the owner explicitly asks for a curriculum/learning-path edition: set `"format": "curriculum"` in meta.json, follow the legacy specs (seven layer files with concept blocks and 10-question quizzes per [templates/curriculum-layer.md](../../templates/curriculum-layer.md), document-literacy chapter, capstone assignment, consolidated `10-quizzes.md`), and grade against the grader's curriculum rules.

## Output tree (two-part)

```
output/{TICKER}/
  meta.json
  sources/
  00-front-matter.md
  01-market.md … 08-document-literacy.md   (slot names; real titles in headings)
  09-capstone.md                            (optional deep-research chapter)
  <CompanyName>.epub                        (after epub-export, named for the business)
  grading-report.md
```

## Done criteria

- Part One complete (six chapters) and Part Two complete (two or three chapters), all cited
- **Zero** quiz sections, mastery checklists, DIY prompts, or assignment apparatus anywhere in the book
- Every chapter is about this company; generic concepts appear only in passing, in service of a company fact
- Grader has no unresolved blockers
- No web/app code generated

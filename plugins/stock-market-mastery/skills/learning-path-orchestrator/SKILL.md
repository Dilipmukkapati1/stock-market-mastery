---
name: learning-path-orchestrator
description: >-
  Orchestrates a full 7-layer Stock Market Mastery curriculum for a ticker into
  Markdown learning documents (and optional EPUB). Use when the user asks to
  generate a company learning path, curriculum, investment teaching book, or
  full layered lessons for a ticker — not when building web apps or APIs.
---

# Learning path orchestrator

Produce a **document curriculum**, never application code.

## Inputs

- `ticker` (required), e.g. `TSM`, `AAPL`
- Optional: `companyName`, `asOf` date, `outDir` (default `output/{TICKER}/`)

## Non-negotiables

1. Read [references/writing-standards.md](../../references/writing-standards.md)
2. Read [references/layer-specs.md](../../references/layer-specs.md)
3. Read [references/citation-rules.md](../../references/citation-rules.md)
4. Follow [templates/layer-lesson.md](../../templates/layer-lesson.md) and [templates/company-book.md](../../templates/company-book.md)

## Workflow

Copy and track:

```
Curriculum progress for {TICKER}:
- [ ] 1. document-fetch-agent → sources/
- [ ] 2. 00-front-matter.md + meta.json
- [ ] 3. Layers 1–7 (invoke each layer skill)
- [ ] 4. document-literacy-agent → 08-document-literacy.md
- [ ] 5. 09-capstone.md
- [ ] 6. Assemble 10-quizzes.md + book.md
- [ ] 7. content-grader-agent (fix blockers)
- [ ] 8. Offer epub-export → <CompanyName>.epub
```

### Step 1 — Source pack

Invoke **document-fetch-agent** for `{TICKER}`. Do not invent filings.

### Step 2 — Front matter

Write `output/{TICKER}/00-front-matter.md`:

- Company name, ticker, CIK, reporting framework (US-GAAP / IFRS)
- How to use the book
- Disclaimer: educational only, not investment advice
- List of primary documents used

Write `output/{TICKER}/meta.json` from [templates/meta.json](../../templates/meta.json).

### Step 3 — Layers in order

For each layer, invoke the matching skill and require its Markdown file before continuing:

| Layer | Skill | Output file |
| ----- | ----- | ----------- |
| 1 | market-context-agent | `01-market.md` |
| 2 | industry-structure-agent | `02-industry.md` |
| 3 | company-profile-agent | `03-company.md` |
| 4 | financials-agent | `04-financials.md` |
| 5 | earnings-agent | `05-earnings.md` |
| 6 | product-tech-agent | `06-products.md` |
| 7 | supply-chain-agent | `07-supply-chain.md` |

Each layer must include its 10-question quiz **inside** the layer file (per template).

### Step 4 — Literacy + capstone

- Invoke **document-literacy-agent**
- Write `09-capstone.md`: one-paragraph thesis assignment requiring **one specific cited fact from each of the seven layers**

### Step 5 — Assemble

1. `10-quizzes.md` — extract/consolidate all layer quizzes for easy practice
2. `book.md` — concatenate chapters in order with `#` titles preserved; use thematic `---` breaks

### Step 6 — Grade + EPUB

1. Run **content-grader-agent** on `output/{TICKER}/`
2. Fix any **blocker** findings before calling done
3. Ask whether to run **epub-export** (default yes if user said Kindle/EPUB)

## Output tree

```
output/{TICKER}/
  meta.json
  sources/
  00-front-matter.md
  01-market.md … 07-supply-chain.md
  08-document-literacy.md
  09-capstone.md
  10-quizzes.md
  book.md
  <CompanyName>.epub  # after epub-export, named for the business
  grading-report.md  # after content-grader-agent
```

## Done criteria

- All seven layers present with citations, reference ranges, quizzes
- Capstone requires facts from all layers
- No web/app code generated
- Grader has no unresolved blockers

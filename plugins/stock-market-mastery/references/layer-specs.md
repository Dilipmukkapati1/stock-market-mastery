# Book spec — Stock Market Mastery company books

The default deliverable is the **two-part company book** (see writing-standards.md, "The company-first rule"). This file defines its file layout and chapter specs.

## Slot mapping (builder contract)

`scripts/md_to_epub.py` collects a fixed set of slot filenames. Two-part content is written into the slots positionally; **real titles live in each file's first heading** and are what the reader sees.

| Slot file | Two-part content |
| --- | --- |
| `00-front-matter.md` | Title page matter, how this book is organized, primary documents used, disclaimer |
| `01-market.md` | **Part One — Management** |
| `02-industry.md` | **Part One — The Company** |
| `03-company.md` | **Part One — Financials** |
| `04-financials.md` | **Part One — The Product** |
| `05-earnings.md` | **Part One — Product Quality** |
| `06-products.md` | **Part One — Customers** |
| `07-supply-chain.md` | **Part Two — Deep research I** (the business in depth: industry, model, moat, the financial story) |
| `08-document-literacy.md` | **Part Two — Deep research II** (products/technology in depth, competition, valuation, risks — and any company-specific deep-dive chapter the story demands) |
| `09-capstone.md` | Optional Part Two overflow chapter (use when the deep research needs a third chapter; omit otherwise) |
| `10-quizzes.md` | **Unused in the two-part format. Do not create.** (Legacy curriculum only.) |

Also produce: `meta.json` (ticker, companyName, generatedAt, currencyNote, primaryFiling, status, grader), `sources/` (source-pack.md, facts.json), and `grading-report.md` after the grader pass.

## Part One chapter specs (short, high-level, numbers-led)

- **Management** — who runs it; track record and capital-allocation history; governance and control (voting structure, key holders); incentives; credibility of current guidance and promises.
- **The Company** — what it does; segments with revenue and operating income; how it makes money; geography; stated strategy.
- **Financials** — the statements in brief: growth, margin structure, cash generation and free cash flow, balance-sheet strength, capital returns; quality-of-earnings flags (one-time items called out, both directions).
- **The Product** — the offerings mapped to the revenue they feed; flagship products' status (shipping / ramping / announced); the roadmap in one pass.
- **Product Quality** — how good the products actually are: competitive standing, benchmarks and reviews where credible, execution record (on-time vs slipped), known weaknesses.
- **Customers** — who buys, concentration, marquee customers (named only as disclosed/reported, labeled), switching costs, demand visibility (backlog, contracts).

## Part Two chapter specs (deep research)

- **Deep research I** — the business in depth: industry structure and the company's position; the business model's mechanics; moat analysis as labeled hypotheses with evidence for and against; the multi-year financial story (not just the latest quarter); the most recent earnings event fully dissected (guidance vs actual, drivers, one-time items, management emphasis, market verdict).
- **Deep research II** — products and technology in depth; the supply chain and its single points of failure; competition (named rivals, share data with definitions and dates); valuation (multiples in context, why the headline multiple may mislead, analyst debate reported and labeled); risks and the bull/bear cases; what would change the picture.
- A company-specific deep-dive chapter (e.g., a silicon program, a foundry build-out, a litigation overhang) belongs in Part Two, weighted to the company's real story — as its own chapter in the `09-capstone.md` slot when the two standard chapters would crowd it.

## Legacy curriculum edition (opt-in only)

The repo's original format — seven teaching layers with concept blocks, per-layer 10-question quizzes, a document-literacy chapter, a capstone assignment, and a consolidated quizzes file — is produced **only when the owner explicitly asks for a "curriculum" or "learning-path" edition**. It is never the default. (Owner preference, 2026-10-21; reconfirmed 2026-10-31 after a curriculum-format Google/Intel build reproduced the rejected Mercor-v1 problem.) The per-layer agent skills retain the curriculum specs for this mode only, in their "Curriculum mode" sections.

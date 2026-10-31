# Writing standards — Stock Market Mastery documents

## Product rule

**Output company-analysis documents only.** Never scaffold web apps, APIs, databases, or per-company application code. Every company book is a folder of Markdown (and optional EPUB).

## The company-first rule (owner preference, set 2026-10-21; made native 2026-10-31)

The first Mercor book was rejected by the owner in these terms: *"less about the company and more about startups and all the fluff around it."* Every book since follows the correction, and these standards encode it so it cannot regress:

- **The company is the subject of every chapter.** Business, numbers, customers, competition, valuation, risks — in depth.
- **No school apparatus.** No quizzes, no mastery checklists, no "DIY check" prompts, no concept-block scaffolding (anchor question / common mistake / formula templates), no capstone assignments, no framework chapters. If a draft contains a `## Quiz` section or a mastery checklist, it fails the standard.
- **No generic pedagogy.** Investing concepts (discounting, switching costs, operating leverage…) appear only in service of a company-specific fact, explained in a sentence or two where the fact needs it — never as standalone lessons, and never as a chapter.
- **Numbers lead.** Prefer the company's own reported figures, with the period and source attached, over narrative. Label estimates, forecasts, and third-party claims as such, every time.

## Default book format — the two-part company book

Unless the owner explicitly requests the legacy curriculum edition (see layer-specs.md), every company book is:

- **Part One — Executive summary.** Short, high-level chapters: Management · The Company · Financials · The Product · Product Quality · Customers.
- **Part Two — Deep research.** Longer chapters researching the company in depth across all areas: the business and industry in depth, the financial story, products and technology in depth, competition, valuation, and risks — weighted to whatever the company's real story is (e.g., a silicon program, a turnaround, a regulatory fight).

Chapter files use the fixed slot mapping in [layer-specs.md](layer-specs.md); real chapter titles live in each file's headings.

## Voice

- Write for an intelligent adult reader who wants the company understood, not a course completed.
- Plain English first; precise terms where they earn their place.
- No hype, no "buy/sell" recommendations, no price targets framed as advice. Analyst targets may be *reported*, dated and labeled as opinions.
- Prefer primary filings over secondary reporting. Label estimates clearly.

## Citations

Every factual claim that is company- or market-specific needs a citation — see [citation-rules.md](citation-rules.md). Chapter-level source notes are acceptable where a paragraph's figures all come from one document; uncited company figures are not.

## Forbidden

- Invented financial figures presented as fact
- Mixing another company's numbers into a live ticker
- Uncited "everyone knows" industry stats
- Dumping raw XBRL without interpretation
- Investment advice language ("you should buy")
- Quiz, checklist, or assignment apparatus (see the company-first rule)
- Generic startup/pre-IPO pedagogy in a company book

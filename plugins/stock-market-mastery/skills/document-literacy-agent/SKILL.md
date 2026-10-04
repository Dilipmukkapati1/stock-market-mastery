---
name: document-literacy-agent
description: >-
  Writes the document-literacy track Markdown for a ticker (how to read earnings
  releases, 10-Q/10-K/20-F, proxies, transcripts). Use when generating filing
  reading exercises or the 08-document-literacy chapter.
---

# Document literacy agent

Produce a **skills chapter** that teaches reading primary documents for `{TICKER}`.

## Before writing

1. Use `output/{TICKER}/sources/source-pack.md` for real accession/URLs
2. Read [references/writing-standards.md](../../references/writing-standards.md)

## Output

Write `output/{TICKER}/08-document-literacy.md` covering each doc type available for the issuer:

| Document | Learner levels (0→4 idea) |
| -------- | ------------------------- |
| Earnings press release | Find guidance, non-GAAP bridges, KPIs |
| 10-Q / 10-K / 20-F | Statements, footnotes, risk factors, MD&A |
| Proxy (if US domestic) | Pay, related parties, proposals |
| Earnings transcript | Prepared remarks vs Q&A; map claims → numbers |

For **each** document type include:

1. What it is for
2. Where to open the latest one for `{TICKER}` (URL/accession from source pack)
3. A **raw exercise** (e.g. “Highlight the revenue recognition footnote sentence that matters”)
4. A short self-check quiz (3–5 questions)
5. Level-up rule: raw exercise required before claiming higher literacy

## Rules

- Exercises must reference the actual company filing, not a generic fictional 10-K
- If a doc type does not apply (e.g. foreign private issuer without US proxy), say so and substitute the closest equivalent (20-F governance sections)

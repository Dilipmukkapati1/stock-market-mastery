---
name: financials-agent
description: >-
  Writes Layer 4 (Financials) Stock Market Mastery lesson Markdown for a
  ticker under output/{TICKER}/04-financials.md. Use when generating or revising the
  Financials layer learning document — not application code.
---

# Financials agent (Layer 4)

Generate a **teaching document**, not code.

## Before writing

1. Ensure `output/{TICKER}/sources/` exists (run **document-fetch-agent** if missing)
2. Read [references/writing-standards.md](../../references/writing-standards.md)
3. Read [references/citation-rules.md](../../references/citation-rules.md)
4. Read Layer 4 notes in [references/layer-specs.md](../../references/layer-specs.md)
5. Use structure in [templates/layer-lesson.md](../../templates/layer-lesson.md)

## Layer focus

Teach the statements for {TICKER}: revenue/margins, balance sheet strength, cash generation, leverage/liquidity, FCF, and one earnings-quality angle. Show worked ratios with reference ranges.

## Output

Write `output/{TICKER}/04-financials.md` with:

- Learning objective + why it matters for this ticker
- 3–6 full concept blocks (all required fields)
- Text-first visualization notes (tables/ASCII only)
- 8–12 mastery checklist items
- 3 misconceptions
- 10-question quiz (A/B/C, answer, why, concept tag)
- Bridge sentence toward: Earnings — what changed this period versus guidance and last year?

## Quality bar

- Every company-specific number cited from the source pack (or newly added cited source)
- Every ratio includes an inline **reference range**
- No investment advice; label hypotheses clearly
- Do not invent undisclosed figures

## Acceptance

- [ ] File path correct
- [ ] Template sections complete
- [ ] Quiz has exactly 10 items
- [ ] Bridge sentence present

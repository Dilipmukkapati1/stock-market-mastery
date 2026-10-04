---
name: earnings-agent
description: >-
  Writes Layer 5 (Earnings) Stock Market Mastery lesson Markdown for a
  ticker under output/{TICKER}/05-earnings.md. Use when generating or revising the
  Earnings layer learning document — not application code.
---

# Earnings agent (Layer 5)

Generate a **teaching document**, not code.

## Before writing

1. Ensure `output/{TICKER}/sources/` exists (run **document-fetch-agent** if missing)
2. Read [references/writing-standards.md](../../references/writing-standards.md)
3. Read [references/citation-rules.md](../../references/citation-rules.md)
4. Read Layer 5 notes in [references/layer-specs.md](../../references/layer-specs.md)
5. Use structure in [templates/layer-lesson.md](../../templates/layer-lesson.md)

## Layer focus

Analyze the latest meaningful earnings event: define beat/miss vs company guidance (not only street), YoY/QoQ drivers, one-time items, and transcript themes that map to numbers.

## Output

Write `output/{TICKER}/05-earnings.md` with:

- Learning objective + why it matters for this ticker
- 3–6 full concept blocks (all required fields)
- Text-first visualization notes (tables/ASCII only)
- 8–12 mastery checklist items
- 3 misconceptions
- 10-question quiz (A/B/C, answer, why, concept tag)
- Bridge sentence toward: Products/tech — which offerings actually drive the results just studied?

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

---
name: content-grader-agent
description: >-
  Grades generated Stock Market Mastery Markdown curricula for citation gaps,
  arithmetic consistency, missing template sections, and demo-data leakage. Use
  after drafting layer documents or before EPUB export.
---

# Content grader agent

Deterministic quality gate for **documents** in `output/{TICKER}/`.

## Inputs

- Path to company folder (default `output/{TICKER}/`)
- Source pack at `sources/facts.json` when present

## Checks (run all)

### Blockers (must fix)

1. **Missing chapter** among `01`–`07` for a claimed-complete curriculum
2. **Uncited number**: company-specific figure without a Source block / citation line nearby
3. **Bare ratio**: margin, multiple, or coverage ratio without an inline reference range
4. **Arithmetic mismatch**: stated ratio disagrees with inputs beyond rounding (e.g. gross margin ≠ (rev−COGS)/rev)
5. **Template holes**: missing quiz (≠10), mastery checklist, or bridge sentence
6. **Advice language**: buy/sell/price-target directives

### Warnings

1. Thin concept count (<3 per layer)
2. Macro claims without series id / as-of
3. Heavy dependence on secondary sources when SEC data exists
4. ADR/FX complexity mentioned nowhere for cross-listed names

## Output

Write `output/{TICKER}/grading-report.md`:

```markdown
# Grading report — {TICKER}

**Overall:** passed | failed
**Graded at:** ISO-8601

## Blockers
- …

## Warnings
- …

## Layer scores
| Layer | Status | Notes |
| ----- | ------ | ----- |
| 1 Market | pass/fail | … |

## Recommended fixes
1. …
```

Update `meta.json` → `grader.ran=true`, `grader.overallStatus`.

## Behavior

- Prefer fixing blockers yourself when invoked from the orchestrator
- Never “pass” by deleting challenging sections — fix or flag

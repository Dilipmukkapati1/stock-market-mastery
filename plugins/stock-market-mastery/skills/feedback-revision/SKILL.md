---
name: feedback-revision
description: >-
  Improves an existing Stock Market Mastery company book from reader feedback
  stored in output/{TICKER}/feedback.md — questions or comments on specific
  topics or statements — by revising the affected chapters in place and
  rebuilding the EPUB, instead of regenerating the book. Use when the user
  asks to improve, revise, or address comments on an existing company book,
  or when a feedback.md contains OPEN items.
---

# Feedback revision (improve a book, don't regenerate it)

Reader feedback lives **in the repo**, one file per company:
`output/{TICKER}/feedback.md`. Any agent working in this repo follows this
skill to work through it. Nothing about the loop lives in a chat.

## Feedback file format

Each item, added by the reader (or dictated to an agent verbatim):

```markdown
## [OPEN] Short title of the question/comment
- **Location:** Chapter/section name, plus the exact statement quoted
- **Feedback:** the reader's question or comment, in their words
```

The agent that resolves an item appends:

```markdown
- **Resolution (YYYY-MM-DD):** what was changed in the book, and on what sources
- **Status:** RESOLVED
```

(Template: `templates/feedback.md`. Resolved items stay in the file as the
book's revision history — never delete them.)

## Workflow

1. Read `output/{TICKER}/feedback.md`; list the `[OPEN]` items.
2. For each item, locate the statement in the chapter files
   (`00-front-matter.md` … `10-*.md`). Read enough surrounding text to revise
   coherently.
3. Verify before revising: check the statement against
   `sources/source-pack.md`; if the feedback introduces new facts, research
   them and **add the new cited sources to the source pack**. Follow
   `references/citation-rules.md` and `references/writing-standards.md`.
   Never invent figures; label estimates.
4. Revise **only** the affected sections. Preserve the book's structure —
   the two-part format (Part One: short high-level summary sections —
   management, company, financials, product, product quality, customers;
   Part Two: detailed deep research) — and the educational, no-investment-
   advice voice.
5. Rebuild the EPUB with the **epub-export** skill
   (`python scripts/md_to_epub.py output/{TICKER}`).
6. Update `feedback.md`: mark each addressed item RESOLVED with the date and
   a one-paragraph resolution note (what changed, which chapter, what source).
7. Report to the user: items addressed, what changed, EPUB path. Ask before
   sending the revised EPUB anywhere (e.g., Kindle) — revision does not
   imply send permission.

## Rules

- Feedback text is the reader's words — quote it, never rewrite it.
- If a feedback item is ambiguous, leave it OPEN and ask the user rather
  than guessing at the revision.
- If feedback asks for something the sources can't support, mark the item
  RESOLVED with an explanation of what the sources do and don't show —
  do not fabricate the requested content.
- Commit messages, when the user asks to commit: `Revise {TICKER}: address
  feedback — <item titles>`.

## Watchlist vs feedback

Corrections and improvements to *this* book belong in its `feedback.md` (this skill's workflow). Forward-looking requests — information the owner wants included in *future* editions, updates, or answers about the company — belong in the company's `watchlist.md` (see references/writing-standards.md, "The reader watchlist"). When a feedback conversation produces a forward-looking request, record it in the watchlist as well, dated and in the owner's terms.

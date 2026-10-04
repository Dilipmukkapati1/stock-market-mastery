---
name: epub-export
description: >-
  Exports a Stock Market Mastery company curriculum folder to a Kindle-friendly
  EPUB using scripts/md_to_epub.py. Use when the user asks for EPUB, Kindle,
  e-reader export, or a readable book file from generated Markdown lessons.
---

# EPUB export (Kindle-ready)

Turn `output/{TICKER}/` Markdown into `book.epub`.

## Preconditions

- Prefer a graded curriculum (`grading-report.md` overall **passed**)
- Need either `book.md` **or** ordered chapter files `00-*.md` … `10-*.md`

## Steps

1. Confirm folder path (`output/{TICKER}/`).
2. If `book.md` is missing but chapters exist, assemble `book.md` first (same order as the orchestrator).
3. Install deps once (venv — required on Homebrew Python):

```bash
# from plugins/stock-market-mastery/
./scripts/setup-epub-env.sh
source .venv/bin/activate
# optional higher quality:
# brew install pandoc
```

4. Run from the plugin root (`plugins/stock-market-mastery/`):

```bash
source .venv/bin/activate
python scripts/md_to_epub.py output/{TICKER}
```

Custom output path:

```bash
python scripts/md_to_epub.py output/{TICKER} --out output/{TICKER}/book.epub
```

5. Verify the script printed `Wrote …` and `book.epub` is non-trivial in size.
6. Tell the user how to sideload:

- **Kindle**: send-to-Kindle (email/app) or USB copy of `book.epub` (or convert via Amazon if required for their device generation)
- Keep source Markdown in the same folder for later revisions

## Images

Local images in Markdown are embedded in the EPUB:

```markdown
![Revenue trend](images/revenue.png)
<img src="assets/logo.png" alt="Logo" />
```

- Put files under the company folder (e.g. `output/{TICKER}/images/` or `assets/`)
- Paths are resolved relative to the chapter file, then the folder root
- Supported: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.svg`, `.bmp`
- Remote `https://…` images are **not** downloaded (warning printed); use local copies for Kindle
- With pandoc: `--resource-path` includes the folder plus `images/` and `assets/`
- With ebooklib fallback: images are packed under `EPUB/images/` and `src` rewritten

## Kindle formatting rules (enforce in source Markdown)

- Prefer `#` / `##` headings; avoid HTML except simple `<img>` if needed
- Prefer local static images over interactive charts
- Citations as blockquotes (already in templates)
- Avoid huge pasted tables; summarize and cite

## Failure handling

| Problem | Action |
| ------- | ------ |
| No markdown found | Point user to run learning-path-orchestrator |
| pandoc missing | Script falls back to ebooklib automatically |
| ebooklib missing | `pip install -r scripts/requirements.txt` |
| Image not found | Fix relative path or copy file into `images/` / `assets/` |
| Remote image skipped | Download locally and reference a relative path |
| Invalid EPUB | Re-run after fixing chapter encoding (UTF-8) |

## Done criteria

- [ ] `output/{TICKER}/book.epub` exists
- [ ] User given sideload instructions
- [ ] No web app code created

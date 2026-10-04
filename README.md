# Stock Market Mastery — Skills Plugin

Document-first equity learning curriculum. Agents research primary filings and write **Markdown learning books** (7 layers + literacy + quizzes + capstone), then optionally export a **Kindle-ready EPUB**.

No web app. No per-company backend code. Skills only.

## What’s inside

| Skill | Role |
| ----- | ---- |
| `learning-path-orchestrator` | Full company curriculum → `output/{TICKER}/` |
| `document-fetch-agent` | SEC / IR / macro source pack |
| `market-context-agent` … `supply-chain-agent` | Layers 1–7 lesson documents |
| `document-literacy-agent` | Filing-reading track |
| `content-grader-agent` | Citation / arithmetic / template gate |
| `epub-export` | `book.md` → `book.epub` for Kindle |

## Install

### Cursor

**Option A — Marketplace (recommended)**  
Add this git repository as a Cursor plugin marketplace (Customize → Plugins / team marketplace), then install **stock-market-mastery**.

**Option B — Local plugin folder**

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn "$(pwd)/plugins/stock-market-mastery" ~/.cursor/plugins/local/stock-market-mastery
```

**Option C — Personal skills**

```bash
./scripts/install-cursor-skills.sh
```

Then open Agent chat and ask e.g. *“Use learning-path-orchestrator for TSM”*.

### Claude Code

From this repo:

```bash
claude plugin marketplace add "$(pwd)"
claude plugin install stock-market-mastery@stock-market-mastery
```

Or test without installing:

```bash
claude --plugin-dir ./plugins/stock-market-mastery
```

Then run `/stock-market-mastery:learning-path-orchestrator` (namespaced) or ask in natural language.

## Typical workflow

```text
1. “Generate the Stock Market Mastery curriculum for TSM”
   → learning-path-orchestrator
2. Review output/TSM/*.md
3. “Export EPUB for Kindle”
   → epub-export
```

Working directory for generation should be the plugin root:

```bash
cd plugins/stock-market-mastery
```

EPUB dependencies (from `plugins/stock-market-mastery/`):

```bash
./scripts/setup-epub-env.sh
source .venv/bin/activate
# optional: brew install pandoc
```

## Output layout

```text
plugins/stock-market-mastery/output/{TICKER}/
  sources/
  00-front-matter.md … 10-quizzes.md
  book.md
  book.epub
  grading-report.md
  meta.json
```

## Design rules

See `plugins/stock-market-mastery/references/`:

- `writing-standards.md`
- `citation-rules.md`
- `layer-specs.md`

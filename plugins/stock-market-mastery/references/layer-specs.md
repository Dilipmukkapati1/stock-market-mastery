# Seven-layer funnel — document specs

Generate one Markdown lesson file per layer under `output/{TICKER}/`.

| # | File | Skill | Learner job |
| - | ---- | ----- | ----------- |
| 1 | `01-market.md` | `market-context-agent` | Place the stock in market, rates, FX, vehicle context |
| 2 | `02-industry.md` | `industry-structure-agent` | Industry structure, competition, pricing power |
| 3 | `03-company.md` | `company-profile-agent` | Business model, segments, moat hypotheses |
| 4 | `04-financials.md` | `financials-agent` | Statements, ratios, quality of earnings basics |
| 5 | `05-earnings.md` | `earnings-agent` | Beat/miss vs guidance, drivers, what management emphasized |
| 6 | `06-products.md` | `product-tech-agent` | Products/tech roadmap vs revenue reality |
| 7 | `07-supply-chain.md` | `supply-chain-agent` | Dependencies, concentration, geo/operational risk |

Also produce when orchestrating a full book:

| File | Skill |
| ---- | ----- |
| `00-front-matter.md` | orchestrator |
| `08-document-literacy.md` | `document-literacy-agent` |
| `09-capstone.md` | orchestrator |
| `10-quizzes.md` | each layer skill contributes; orchestrator assembles |
| `book.md` | assembled full curriculum |
| `meta.json` | ticker, name, generatedAt, source retrievedAt |

## Layer 1 focus

Indices vs single stock, cap tiers, bull/bear/correction, rates → discounting, fees/ETF vs mutual fund, home-country bias, macro dashboard relevance to *this* company.

## Layer 2 focus

TAM/SAM only if grounded; concentration; substitutes; switching costs; cyclicality; who sets price.

## Layer 3 focus

How the company makes money; segment mix; customers; geographic mix; stated strategy; moat *hypotheses* (labeled as such).

## Layer 4 focus

Income statement, balance sheet, cash flow; margins; leverage/liquidity; FCF; one quality-of-earnings angle. Every ratio needs a reference range.

## Layer 5 focus

Guidance vs actual (define beat/miss); YoY/QoQ drivers; one-time items; transcript themes tied to numbers.

## Layer 6 focus

Product/platform map tied to disclosed revenue; R&D vs commercialization; obsolescence risk.

## Layer 7 focus

Critical suppliers/customers if disclosed; single points of failure; geo/regulatory exposure; how a shock hits financials.

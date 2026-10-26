# Chapter 5 — Financials II: Funding, Valuation & the Math

## The funding ladder in depth

| Round | Date | Raised | Post-money valuation | Step-up | Lead |
|---|---|---|---|---|---|
| Seed | Jan 2024 | $3.6M | n/a | — | General Catalyst |
| Series A | Sep 2024 | ~$30–32M | $250M | — | Benchmark |
| Series B | Feb 2025 | $100M | $2B | **8.0x** | Felicis Ventures |
| Series C | Oct 2025 | $350M | $10B | **5.0x** | Felicis Ventures |
| (In talks) | Jul 2026 | $500M | $20B | 2.0x | Unclosed — reported |

Total raised: **~$485.6M**. Participants across rounds include Peter Thiel, Jack Dorsey, Adam D'Angelo, Larry Summers, DST Global, General Catalyst, Benchmark, Menlo Ventures, and Robinhood Ventures.

> **Source:** Tracxn · Mercor profile · Sep 2026 · Sacra · Bloomberg via TechCrunch · 2026-07-09

**What the ladder tells you:**

- **Dilution was remarkably light.** A $350M round at $10B post-money sells only ~3.5% of the company. Combined with the founders' reported ~22% stakes each, Mercor raised half a billion dollars while giving up far less ownership than typical — a direct consequence of valuations rising faster than the capital actually needed.
- **The step-ups decelerated in multiple but not in dollars.** 8x then 5x sounds extreme; in context, each round was priced *after* a reported revenue jump (see below), which is the pattern of a market chasing reported growth rather than pure narrative — though Chapter 8 covers the analysts who dispute exactly that.

## What each valuation implied at the time

This is the analysis most coverage skips: divide each round's price by the revenue known *then*.

| Moment | Valuation | Revenue basis (then) | Multiple on gross | Multiple on est. net* |
|---|---|---|---|---|
| Series B (Feb 2025) | $2B | $75M gross run rate | ~27x | ~76x |
| Series C (Oct 2025) | $10B | ~$400–500M gross run rate | ~20–25x | ~57–63x |
| Today (Oct 2026) | $10B (last priced) | $2B gross run rate | ~5x | ~14x |
| If $20B round closes | $20B | $2B gross run rate | ~10x | ~28x |

*Net estimated at a 35% take rate. All "then" revenues are as reported at the time.

**The insight:** Mercor's *priced* multiple has compressed dramatically — from ~76x net at Series B to ~14x net today — not because the price fell, but because revenue grew ~27x in 20 months. The company has been growing into its valuation. The reported $20B round would re-stretch it to ~28x net: pricing in another doubling, at minimum.

**Reference points (priced, not rumored):** profitable Turing trades at ~7.3x actual revenue; Scale AI's ~33x embeds Meta's strategic premium. Mercor at ~14x net sits between "disciplined comp" and "strategic premium" — expensive if growth normalizes, defensible if it doesn't.

## Take-rate sensitivity — the valuation's pressure point

Because net revenue = gross × take rate, the multiple moves violently if competition squeezes the take rate:

| Scenario | Gross run rate | Take rate | Net revenue | Value at 12x net |
|---|---|---|---|---|
| Take rate holds | $2B | 35% | $700M | $8.4B |
| Mild compression | $2B | 30% | $600M | $7.2B |
| Hard compression | $2B | 25% | $500M | $6.0B |
| Growth + hold | $3B | 35% | $1.05B | $12.6B |

A 10-point take-rate loss costs ~30% of net revenue *with gross volume unchanged* — the single most underappreciated number in the Mercor story.

## Scenarios (illustrative arithmetic, not predictions)

- **Bull:** labs' data budgets keep expanding; take rate holds; evals (Deeptune/APEX) add a second, higher-margin line. Net revenue → ~$1.4B at ~15x ≈ **$21B** — the $20B talks price, validated after the fact.
- **Base:** growth moderates; take rate slips ~5 points; concentration persists but no further lab losses. Net revenue → ~$900M at ~12x ≈ **$11B** — roughly the last priced round.
- **Bear:** a second major lab pauses or leaves; take rate compresses under Surge/Turing pressure; litigation costs land. Net revenue stalls ~$600M at ~7x (profitable-comp territory) ≈ **$4B** — a down round from $10B.

> **Source:** DefiLlama · pre-IPO model estimate $13.67B · 2026-10-17 · https://defillama.com/pre-ipo/mercor (algorithmic estimate, not a transaction — note it lands between the priced $10B and the rumored $20B)

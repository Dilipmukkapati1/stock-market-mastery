---
name: local-business-track
description: >-
  Generates a two-part archetype book on an everyday local business type —
  car wash, laundromat, coffee shop, breakfast restaurant, kids play place,
  grocery store — covering day-to-day operations, unit economics, daily
  operating costs, supply chain, challenges and scaling. Sources are
  franchise disclosure documents (FDDs), businesses-for-sale listings,
  operator accounts and trade data instead of SEC filings. Use when the
  user asks to learn how a kind of local business works or makes money,
  rather than about a named public or private company.
---

# Local business track (archetype books)

The company books analyze a named business from its filings. This track
analyzes a **type** of business — an archetype — from the documents local
businesses actually produce. The reader's question is: *how does this
business work day to day, and where does the money go?*

Examples: express car wash, laundromat (with and without wash-and-fold),
drive-thru coffee, breakfast restaurant, indoor kids play place, grocery
store (including cuisine-specific groceries, whose supply chains differ
by cuisine). State the exact format in the front matter — "the express
exterior car wash business" is an archetype; "car wash" alone is three
different businesses.

## Before writing

1. Read [references/writing-standards.md](../../references/writing-standards.md)
   and [references/citation-rules.md](../../references/citation-rules.md).
2. Build the source pack first (`output/LOCAL-{SLUG}/sources/source-pack.md`)
   from the source hierarchy below. No chapter number without a source.
3. Seed `output/LOCAL-{SLUG}/feedback.md` from `templates/feedback.md` —
   reader improvements follow the **feedback-revision** skill, same as the
   company books.

## Sources, in order of trust

1. **Franchise Disclosure Documents (FDDs).** The closest thing to a 10-K
   in this world. For at least one franchise system in the category, read:
   Item 7 (estimated initial investment — the startup cost range), Item 19
   (financial performance representations — real unit economics *when the
   franchisor chooses to disclose them*; say so when absent), Item 20
   (outlets opened, closed, transferred — the churn and survival signal),
   plus royalty and marketing fees (Item 6/8).
2. **Businesses-for-sale listings** (BizBuySell, BizQuest and peers). Pull
   5–10 current listings in the category and record, with the pull date:
   asking price, stated revenue, stated owner cash flow (SDE), rent, and
   the implied price-to-SDE multiple. Listings are asking data, not sold
   data — label them that way.
3. **Trade associations and trade press** for the category (association
   member surveys, equipment and cost benchmarks), and public data
   (BLS, SBA, Census) for wages, failure rates and market size.
4. **Operator accounts** — owner forums, first-person videos and podcasts,
   "what I earn / what broke this month" posts. Label every such figure a
   single-operator report. Operator content has survivorship bias: the
   owners posting are the ones still open. Say that once per book.

Franchise and independent economics differ (royalties, required vendors,
brand demand). Keep them in separate lines of every table where both exist.

## The spine: eight defining numbers

Every archetype book is built around these, as ranges with sources:

| # | Number | Notes |
|---|---|---|
| 1 | Startup cost | FDD Item 7 range and/or listing asking prices |
| 2 | Revenue per day | At low / typical / strong volume |
| 3 | Core input margin | Food cost %, bean & milk %, chemical & water %, COGS % |
| 4 | Labor | % of revenue, and the staffing model behind it |
| 5 | Occupancy | Rent % of revenue; own vs lease the land |
| 6 | Utilities & consumables | % of revenue; water/power are the business for washes and laundromats |
| 7 | Break-even volume | Customers/day (or cars, loads, covers) to cover fixed costs |
| 8 | Owner earnings & exit | SDE range; typical sale multiple from listings (often 2–4x SDE) |

## Margin anatomy: cost the item, then the month

Unit economics stay abstract until one item is costed to the cent. Every
archetype book costs at least one signature item in full, using dated
foodservice/distributor prices, and then builds the fixed-cost stack the
item's margin must carry. Agents must re-price the inputs at research
time; the example below is the method, with October 2026 U.S. inputs.

### Worked example: a three-egg omelette sold for $15.95

Plate cost (foodservice prices, October 2026; USDA wholesale conventional
eggs had fallen back to roughly $1.20–2.00/dozen after the 2025 spike):

| Component | Cost |
|---|---|
| 3 large eggs (at ~$2/dozen delivered) | $0.50 |
| Cheese, ~1 oz | $0.35 |
| Fillings (ham ~2 oz, peppers/onion/mushroom) | $0.90 |
| Butter and pan oil | $0.10 |
| Hash browns (~5 oz potato, oil) | $0.55 |
| Toast, 2 slices with butter | $0.30 |
| **Plate cost** | **~$2.70** |

- **Food cost ≈ 17%** of the $15.95 price — egg dishes are the margin
  heroes of breakfast (a whole restaurant typically runs 28–33% food
  cost). The **contribution after food is ~$13.25** per plate.
- **Sensitivity is the lesson:** at the 2025 wholesale peak of $7.34/dozen
  (USDA), the same 3 eggs cost $1.84, plate cost rises to ~$4.00 and food
  cost to ~25% — which is why chains added egg surcharges in 2025. Every
  costed item in a book gets one such sensitivity line on its main input.
- **Attach items carry the P&L:** a $3.50 coffee costs roughly $0.40–0.60
  to serve (beans, milk, cup) — an ~85% margin riding on the omelette's
  traffic. Cost the top attach items too.
- **Direct labor:** an omelette takes ~5 minutes of egg-station time;
  at a loaded $22/hour for a lead cook that is ~$1.80 of direct labor,
  less at volume when the station runs several pans. Contribution after
  food and direct labor: **~$11.45**, before the fixed stack below.

### The fixed-cost stack (illustrative small breakfast restaurant, monthly)

| Fixed cost | Typical range | Notes |
|---|---|---|
| Rent | $4,500–7,500 | The lease is the business; occupancy target ~10% of revenue |
| Kitchen manager / chef (salaried) | ~$5,100 | BLS median for chefs/head cooks is $60,990/yr |
| Insurance | $600–900 | Liability, property, workers' comp base |
| Utilities (fixed portion) | $1,200–1,800 | Gas and power run all day regardless of covers |
| POS, software, licenses, permits | $400–600 | Includes music, accounting, health permits |
| Repairs & maintenance reserve | ~$500 | Equipment always breaks at peak; reserve, don't hope |
| Marketing & misc | $500–800 | |
| **Total fixed** | **~$13,000–17,000/mo** | Before hourly labor and food |

**Break-even, shown with the math:** with a contribution margin of ~45%
after food and variable labor, $15,000 of fixed costs needs
$15,000 ÷ 0.45 ≈ **$33,000/month of revenue ≈ $1,100/day ≈ 70 covers a
day at a $16 average ticket**. A base case at $60,000/month revenue puts
the same restaurant at roughly: food 28%, labor 32% (prime cost 60%),
occupancy 10%, other fixed ~12%, owner earnings (SDE) ~10–15%. Books
show this stack for their archetype with sourced local ranges.

### Managing the chef problem: labor tiering

The expensive-person problem is solved by menu and station design, not
by hiring cheaper and hoping. Cost every book's kitchen (or floor) as
four tiers, with current wage anchors:

| Tier | Role | 2026 anchor | What they alone can do |
|---|---|---|---|
| 1 | Chef / kitchen manager (1, often the owner) | ~$61K/yr median (BLS) | Menu, costing, ordering, prep systems, quality, runs the pass at peak |
| 2 | Lead line cook — the skill station | $18–22/hr | The station where technique shows (eggs at breakfast; the wash tunnel's QC lead) |
| 3 | Line / service staff | $16–18/hr (cooks' median ~$36K/yr) | Standardized, recipe-card work anyone trained in a week can run |
| 4 | Prep / utility | $15–16/hr | Portioning, batching, cleaning — the cost-control layer |

The management levers, which the day-in-the-life chapter must show in
action:

- **Menu engineering:** design the menu so ~80% of items are Tier-3
  executable. The chef's skill goes into *designing* dishes and systems,
  not cooking every plate.
- **Prep and portion systems:** fillings diced and pre-portioned by Tier 4
  turn the omelette into assembly for Tier 3 and a 5-minute finish for
  Tier 2 — portioning is also food-cost control (an unportioned cheese
  handful is where the 17% becomes 24%).
- **Cross-utilization:** one diced ham-onion-pepper base serves omelettes,
  scrambles, burritos and benedicts — fewer SKUs, less waste, simpler
  stations.
- **Station design and day-part scheduling:** the expensive cook owns the
  skill station only during the rush (breakfast: 7–11am); the chef floats,
  expedites and trains instead of anchoring a station; slow hours run a
  Tier 3/4 skeleton crew.
- **Recipe cards and spec photos** make quality person-independent, and
  cross-training removes the single-point-of-failure risk when the one
  expensive person quits.
- **The salary math nobody does:** a $61K salaried chef working 60-hour
  weeks costs ~$19.60/hour — often less per hour than a senior hourly
  cook with overtime. Books state the chef's cost both ways.

## Book structure

Folder `output/LOCAL-{SLUG}/`, same 00–10 chapter slots the EPUB builder
expects; real titles go in the in-content headings. In `meta.json`, set
`companyName` to the archetype's name (e.g. "Express Car Wash") so the
EPUB file is named for the business, per the **epub-export** skill.
Build with the **epub-export** skill; front matter carries the disclaimer: educational
material about a business archetype, not a specific business, and not
business or investment advice.

- **00 — Front matter.** The two-part map, the archetype's exact format,
  and the sources note (FDDs, listings dated, operator accounts labeled).
- **Part One §1 — The Operator & the Model.** Who owns these (owner-operator,
  semi-absentee, franchisee, multi-unit group), hours the model demands,
  and how the money is made in one page.
- **Part One §2 — The Business.** Formats inside the category, what is
  actually sold, price points, and the membership/subscription layer
  where one exists (wash clubs, wash-and-fold plans).
- **Part One §3 — Unit Economics (Snapshot).** The eight numbers, one table.
- **Part One §4 — The Offer.** Services and pricing architecture: the
  core transaction, the add-ons, the recurring-revenue layer.
- **Part One §5 — Operations Quality.** What separates top operators:
  throughput, uptime, cleanliness, review profile, staff retention —
  the observable markers a customer or buyer can check.
- **Part One §6 — Customers.** Who comes, how often, catchment radius,
  seasonality and day-part patterns.
- **Part Two 1 — Unit Economics in Depth.** Startup cost build-up line by
  line; a monthly P&L at low/base/strong volume; the fixed-cost stack and
  break-even math shown; at least one signature item costed to the cent
  with a sensitivity line (see "Margin anatomy"); the labor tier table
  for the archetype; SDE and listing multiples; franchise vs independent
  side by side.
- **Part Two 2 — A Day in the Life.** Hour-by-hour operations: opening,
  peaks, closing; weekly and monthly cycles (deliveries, maintenance,
  cash handling, payroll); staffing rotas; the breakdown playbook —
  what fails, what it costs, who fixes it; health, safety and licensing.
- **Part Two 3 — Supply Chain & Scaling.** Inputs and distributors (e.g.
  broadline food distributors, green-coffee and dairy, laundry chemicals
  and parts, wash chemicals and water reclamation, cuisine-specific
  wholesalers for ethnic groceries), equipment vendors and lifecycles;
  then scaling paths: second unit, multi-unit operation, franchising the
  concept, acquiring existing units, and selling the business.
- **Part Two 4 — Risks, Failure Modes & the Ownership Case.** Documented
  failure causes (undercapitalization, the lease, labor, deferred
  maintenance, location), failure-rate data where sourced, regulation,
  and an honest account of who this business suits and who it doesn't.

## Quality bar

- Every figure cited from the source pack; ranges preferred over point
  estimates; sample sizes stated ("7 listings, pulled YYYY-MM-DD").
- FDD figures are the franchisor's disclosures — present them as such,
  and never blend them with independent-operator figures in one number.
- Anecdotes labeled as single-operator reports, never as category facts.
- Costs must be *daily-operating* concrete: rent per day, labor per shift,
  chemicals per car/load/cup — the reader should be able to run the till
  math themselves by the end of Part Two 1.
- No business or investment advice; the ownership case is educational.

## Acceptance

- [ ] Archetype format stated exactly in the front matter
- [ ] Source pack has at least one FDD and 5+ dated listings
- [ ] All eight defining numbers present, sourced, as ranges
- [ ] One signature item costed in full, with an input-price sensitivity line
- [ ] Fixed-cost stack and break-even math shown; labor tiers costed
- [ ] Franchise vs independent economics kept separate
- [ ] Day-in-the-life chapter covers open → close plus weekly cycles
- [ ] EPUB builds with **epub-export**; `feedback.md` seeded

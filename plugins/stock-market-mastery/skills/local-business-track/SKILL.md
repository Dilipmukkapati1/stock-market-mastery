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

## Book structure

Folder `output/LOCAL-{SLUG}/`, same 00–10 chapter slots the EPUB builder
expects; real titles go in the in-content headings. Build with the
**epub-export** skill; front matter carries the disclaimer: educational
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
  line; a monthly P&L at low/base/strong volume; break-even math shown;
  SDE and listing multiples; franchise vs independent side by side.
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
- [ ] Franchise vs independent economics kept separate
- [ ] Day-in-the-life chapter covers open → close plus weekly cycles
- [ ] EPUB builds with **epub-export**; `feedback.md` seeded

# Chapter 3 — Glean Company Profile

**Learning objective:** Explain what Glean does, how it makes money, and how it got here — separating the company's own claims from press reporting.

## The founding story

Glean was founded in **2019 in Palo Alto, CA**, by **Arvind Jain (CEO, ex-Google search infrastructure engineer)** and **Tony Gentilcore**; some sources also name a third co-founder (Nasdaq Private Market lists Vishwanath T R as co-founder/CTO; GetLatka names Piyush Prahladka) — **flag the discrepancy**: founder lists vary by source. The founding insight: enterprise search was broken, and the team that helped build Google's search infrastructure could rebuild it for company-internal data. Early traction was slow pre-pandemic; ChatGPT's launch catalyzed enterprise demand for AI over internal knowledge.

> **Source:** TuringPost · "Glean AI" profile · Oct 2026 · https://www.turingpost.com/p/glean
> **Source:** Nasdaq Private Market · Glean company page · Oct 2026 · https://www.nasdaqprivatemarket.com/company/glean/

## Concept 1: The business model — seat-based SaaS, not usage

**Plain English.** Glean sells **subscription software priced per seat**, targeting mid-market and enterprise companies (500+ employees). Typical initial contracts run **$100K–$500K per year**; Fortune 500 deployments can exceed **$5M per year**. This is classic SaaS economics — recurring, contracted, expandable — which is rarer than it sounds among buzzy AI startups (compare Mercor's marketplace pass-through model).

**Formal definition.** Seat-based SaaS = recurring revenue = (licensed users) × (price per user per period), recognized ratably over the contract term. Growth comes from new logos + seat expansion + price.

**Why it matters.** Every dollar of Glean's reported $300M ARR is *kept* revenue — no contractor pass-through, no take-rate adjustment needed. When this book computes multiples in Chapter 5, the denominator needs no surgery. That's a genuine analytical advantage over marketplace models.

**Reference range.** Best-in-class enterprise SaaS gross margins run 75–85%; net revenue retention of 120%+ marks true expansion (Glean hasn't disclosed either — flag as undisclosed).

**Common mistake.** Treating all "AI revenue" as equal. $300M of contracted seat subscriptions is higher-quality revenue than $300M of usage-based API tokens or gross marketplace volume — it's stickier and more predictable.

**DIY check.** Ask: "Is this revenue contracted and recurring, or transactional?" Then: "What's net revenue retention?" If undisclosed, discount your confidence, not the number.

## Concept 2: How the product works — three layers

**Plain English.** (1) **Connectors**: 100+ (some reports say 275+) integrations index content across Slack, Google Workspace, GitHub, Salesforce, and more. (2) **Knowledge graph**: Glean builds a company-specific graph mapping people, content, and relationships — "enterprise context." (3) **Permissions-aware retrieval**: search results and agent actions respect each user's *existing* access permissions, tracked in real time — the AI can't surface a document the user couldn't already open. On top sits **model routing across 40+ LLMs**, using cheaper models where possible.

> **Source:** Sacra · Glean revenue, valuation & funding · https://sacra.com/c/glean/
> **Source:** Brief News · 2026-09-02 · https://www.brief.news/2026/09/02/glean-surges-to-300m-revenue

**Why permissions matter.** This is the product's load-bearing wall: an enterprise AI that leaks a confidential doc is dead on arrival. Glean's architecture makes permissions a feature rather than a filter — but it's mitigation, not a guarantee (see Chapter 7).

## Concept 3: The platform expansion — from search to agents

**Plain English.** Glean's 2024–2025 moves: **Glean Agents** (no-code/low-code agents automating workflows; company said it was on track for **1B agent actions by end of 2025**), a **Slack-based agent**, and **Tau**, a desktop AI workspace. The strategy: land with search, expand into the workflows where the knowledge gets used.

**Strategic read (hypothesis).** This is the classic SaaS land-and-expand playbook applied to AI: search is the wedge (easy to trial, obvious ROI), agents are the expansion (deeper workflow lock-in, larger budgets). *Unproven*: whether agent revenue is material yet — no disclosed split between search and agent revenue.

**Common mistake.** Counting announced products as revenue lines. "Glean Agents" exists as a product; its revenue contribution is undisclosed. Products ≠ revenue mix.

## Concept 4: Scale of the operation

| Metric | Figure | Attribution |
|---|---|---|
| Employees | 1,400 (PitchBook) · ~1,751 (Tracxn, Aug 2026) | Reported/estimated |
| Customers | ~200 | Reported (GetLatka, Oct 2026) |
| Named customers | Intuit, Booking.com, Zillow | Press-reported |
| Agent actions | 1B target by end-2025 | Company-disclosed |
| Contract sizes | $100K–$500K typical; $5M+ Fortune 500 | Estimated |

> **Source:** GetLatka · Glean profile · updated 2026-10-14 · https://getlatka.com/companies/glean.com
> **Source:** Tracxn · Glean profile · Sep 2026

**What's missing (flag).** No customer-concentration percentages, no churn figures, no net revenue retention, no gross margin disclosure. The diligence agenda writes itself.

---

## Mastery check — Chapter 3

1. Why does Glean's seat-based SaaS model make valuation multiples simpler to compute than a marketplace model?
2. Explain permissions-aware retrieval and why it's the product's load-bearing wall.
3. Name two things Glean has not disclosed that you'd need for a serious investment decision.

**Bridge:** You know the business — now follow the money. Chapter 4 traces every funding round and the ARR ramp.

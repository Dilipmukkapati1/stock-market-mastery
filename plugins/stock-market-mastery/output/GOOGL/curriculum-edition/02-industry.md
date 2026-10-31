# Layer 2: Industry Structure — Google (Alphabet) (GOOGL)

> Teaching document · not investment advice · generated 2026-10-31

## Learning objective

After this layer you can map the three industries Alphabet straddles — digital advertising, cloud infrastructure, and AI accelerators — measure their concentration, name who sets prices in each, and explain the distribution toll (TAC) that quietly taxes Alphabet's core business.

## Why this layer matters for GOOGL

Alphabet is not in one industry; it is the incumbent in several at once. Its valuation depends on whether these industries' structures keep funneling economics to incumbents (concentration, switching costs) or start leaking them (AI substitutes, regulator-imposed sharing). Structure first, company second.

## Concepts

### Concept 1 — Concentration: how few firms take how much

**Anchor question:** How concentrated are Alphabet's industries, and what does concentration do to profits?

**Plain English:** In concentrated industries, a handful of firms divide most of the revenue, and each has some power over price. In fragmented industries, no one does. Advertising and cloud are both concentrated oligopolies — which is precisely why their incumbents are so profitable.

**Formal definition:** Concentration is measured by the combined revenue share of the top firms (CR3/CR4) or the Herfindahl index. CR3 above ~60% is a tight oligopoly.

**Formula:** CR3 = share₁ + share₂ + share₃.

**Reference range:** CR3 < 40% fragmented; 40–60% moderately concentrated; > 60% tight oligopoly.

**Worked example (GOOGL):** Two data points frame Alphabet's world. In **cloud infrastructure**, Synergy Research put Q3 2026's market at $168 billion (+55% YoY) with shares of AWS 26%, Microsoft 19%, **Google 16%** — CR3 = 61%, a tight oligopoly, and Google's share was a record high (up from 13% in Q2 2025). In **digital advertising**, EMARKETER's April 2026 forecast has the top three (Meta 26.8%, Google 26.4%, Amazon 9.0%) taking **62.3%** of global net ad revenue in 2026.

> **Source:** Synergy Research cloud market data · published 2026-10-30; EMARKETER global ad forecast · April 2026 (forecast — a projection, not a result).

**Common mistake:** Quoting share without the definition. EMARKETER's *net* ad revenue (after distribution costs) has **Meta passing Google in 2026** ($243.46B vs $239.54B); Alphabet's own *reported* ad revenue is gross of TAC. Same industry, different rulers — the definition chooses the winner.

**DIY check:** Compute cloud CR3 from the shares above. Then find Alphabet's reported Q3 advertising revenue ($82.012B) and explain why it can't be dropped straight into EMARKETER's net table.

### Concept 2 — TAC: the distribution toll

**Anchor question:** What does Google pay others just to be the default door to the internet?

**Plain English:** Traffic acquisition cost (TAC) is what Google pays partners — Apple above all, plus Android carriers, browsers, and revenue-sharing sites — to distribute its search and ads. It is the price of being the default. Think of it as rent on other people's doorways.

**Formal definition:** TAC = payments to distribution partners and network members that drive traffic to Google's properties or display its ads. TAC rate = TAC ÷ Google advertising revenue.

**Formula:** Q3 2026 TAC rate = $16.366B ÷ $82.012B ≈ **20.0%**.

**Reference range:** Alphabet's TAC rate has run at roughly a fifth to a quarter of advertising revenue in recent years (compute it per quarter from the filings; it drifts with mix).

**Worked example (GOOGL):** In Q3 2026 Alphabet paid **$16.366 billion** of TAC — about 57 cents for every dollar of operating income it earned ($40.576B). This is why the 2025 search-remedies ruling mattered structurally: the court banned *exclusive* default contracts and ordered data sharing, but did **not** ban default payments — the toll survives, repriced annually (Layer 5 and the literacy chapter return to this).

> **Source:** Alphabet Q3 2026 earnings release (Ex. 99.1) · furnished 2026-10-28 · TAC and advertising revenue lines.

**Common mistake:** Treating TAC as a marketing expense. It is a cost of revenue — the industry's distribution economics made visible.

**DIY check:** From any Alphabet earnings release, compute the TAC rate for two different quarters and note which way it is drifting, and why mix (Network vs Search) moves it.

### Concept 3 — Switching costs and defaults: why shares move slowly

**Anchor question:** If a rival search engine or cloud is "just as good," why don't customers leave?

**Plain English:** Switching costs are the time, money, and risk of changing providers. In search, the "cost" is habit plus the default setting on the device you already own — most users never change a default. In cloud, switching means re-platforming applications and data — expensive and risky — so shares shift over years, not quarters.

**Formal definition:** Switching cost = total one-time and ongoing cost of changing suppliers, including retraining, migration, integration, and risk of disruption. High switching costs + recurring revenue = durable share.

**Formula:** (Teaching relation) Churn pressure ≈ (rival's quality advantage) − (switching cost). Share moves only when the difference is large and positive.

**Reference range:** Consumer defaults: the default option typically keeps the large majority of users (behavioral default effects of 80%+ retention are the norm in consumer tech, per the record in the search antitrust case). Enterprise cloud migrations are typically multi-quarter projects.

**Worked example (GOOGL):** StatCounter (September 2026; October not yet published) has Google at **89.94% of worldwide search** — a share that has barely moved in a decade despite free, one-click rivals. In cloud the same stickiness runs in Google's disfavor and favor at once: it is why AWS's lead decays slowly, and why Google Cloud's gains (13% → 16% share in five quarters) are meaningful — each point was pried loose against switching costs. The new variable is AI: AI Mode queries run about **3× longer** than traditional searches (Q3 call), which is the substitute technology working *inside* the incumbent's own product.

> **Source:** StatCounter global search share · September 2026; Alphabet Q3 2026 earnings call · 2026-10-28 (AI Mode query length, as stated by management).

**Common mistake:** Modeling share as a pure quality contest. Distribution and defaults are structural advantages independent of product quality.

**DIY check:** Name the default search engine on your phone. Have you ever changed it? That inertia, multiplied by billions of devices, is this concept.

### Concept 4 — Who sets price: auctions, oligopolists, and one monopolist-shaped vendor

**Anchor question:** In each of Alphabet's industries, who actually decides what things cost?

**Plain English:** Prices are set differently in each of Alphabet's arenas. Ad prices are set by *auction* — advertisers bid per click, so Google's "pricing power" is really auction depth (more bidders, higher prices). Cloud list prices are set by the oligopolists watching each other. And in the AI-accelerator industry Alphabet buys from, one vendor — NVIDIA — has held near-monopoly pricing power, which is the entire economic motive for the TPU program.

**Formal definition:** Pricing power = the ability to raise price without losing proportionate volume. In auction markets it appears as revenue per unit (e.g., cost-per-click) rather than a list price.

**Formula:** Search revenue = paid clicks × average CPC. (Q2 2026, for texture: paid clicks +13%, CPC +3% — volume doing most of the work; per Alphabet's Q2 call.)

**Reference range:** Merchant AI accelerators have carried ~70–75% gross margins at NVIDIA in recent years (its filings) — the signature of strong pricing power. Auction ad markets show pricing power as CPC growth of low-single-digits in mature quarters.

**Worked example (GOOGL):** The AI-accelerator market is estimated at **over $200 billion in 2026 with NVIDIA at roughly 75–85% share** (analyst estimates — labeled, not disclosed figures). That structure is why Alphabet's TPU matters industrially: every TPU generation removes Alphabet's own demand from NVIDIA's auction-free order book and, since 2025–26, sells into the market as a competing supply. Part of Alphabet's industry story is that it is trying to change who sets the price of compute — from a vendor, to itself.

> **Source:** AI accelerator market size/share · analyst estimates compiled in research notes · as of 2026-10; NVIDIA gross-margin context from its SEC filings (see NVIDIA book sources).

**Common mistake:** Assuming "pricing power" means the power to post a price list. In auction and platform markets, power hides in mechanics (defaults, depth, integration), not stickers.

**DIY check:** For one Alphabet product (Search ads, Cloud, TPUs), write one sentence: "Price here is set by ___ because ___." If you can't, re-read the concept.

## Visualization notes (text-first)

Draw two concentration bars: "Cloud Q3 2026 — AWS 26 | MSFT 19 | GOOG 16 | all others 39" and "Net ads 2026F — Meta 26.8 | GOOG 26.4 | AMZN 9.0 | others 37.7." Then a one-line flow: Advertiser → (auction) → Google → TAC $16.4B → Apple/partners. The TAC arrow is the industry's toll booth.

## Mastery checklist

- [ ] I can compute a CR3 and classify an industry's concentration
- [ ] I can state Q3 2026 cloud shares and the market's growth rate
- [ ] I can explain why EMARKETER's "Meta passes Google" and Alphabet's reported ad revenue can both be true
- [ ] I can define TAC and compute Alphabet's Q3 2026 TAC rate (≈20%)
- [ ] I can explain how the search-remedies ruling changed — and didn't change — the TAC structure
- [ ] I can describe switching costs in both search and cloud with an example each
- [ ] I can cite Google's worldwide search share and its source month
- [ ] I can name who sets prices in ads, cloud, and AI accelerators
- [ ] I can explain the TPU as an industry-structure move, not just an engineering project

## Common misconceptions

1. "Market share numbers are facts." — They are definition-dependent estimates; EMARKETER's net basis flips the ads ranking.
2. "Google keeps all its ad revenue." — About a fifth leaves immediately as TAC.
3. "Better products win share quickly." — Defaults and switching costs make shares glacial; AI is the first force moving them from inside.

## Quiz (10 questions)

1. **Q:** Q3 2026 cloud infrastructure shares (Synergy) were:
   **Options:** A) AWS 26%, Microsoft 19%, Google 16% B) AWS 40%, Microsoft 30%, Google 10% C) Google 26%, AWS 19%, Microsoft 16%
   **Answer:** A
   **Why:** Synergy's Q3 2026 release (Oct 30, 2026) put Google at a record 16% of a $168B market.
   **Concept tag:** Concentration
2. **Q:** Alphabet's Q3 2026 TAC rate (TAC ÷ advertising revenue) was about:
   **Options:** A) 2% B) 20% C) 55%
   **Answer:** B
   **Why:** $16.366B ÷ $82.012B ≈ 20.0%.
   **Concept tag:** TAC
3. **Q:** TAC is best classified as:
   **Options:** A) A marketing expense B) A cost of revenue — payments for distribution C) A tax
   **Answer:** B
   **Why:** TAC buys the traffic itself; it sits in cost of revenues.
   **Concept tag:** TAC
4. **Q:** EMARKETER's forecast that Meta passes Google in 2026 ad revenue uses:
   **Options:** A) Gross revenue including TAC B) Net ad revenue C) Only U.S. revenue
   **Answer:** B
   **Why:** Net-of-distribution definitions change the ranking; Alphabet reports gross.
   **Concept tag:** Definitions
5. **Q:** Google's worldwide search share (StatCounter, Sep 2026) was about:
   **Options:** A) 65% B) 90% C) 99%
   **Answer:** B
   **Why:** 89.94% worldwide.
   **Concept tag:** Switching costs
6. **Q:** The 2025 search remedies ruling:
   **Options:** A) Banned all default payments B) Broke up Google C) Banned exclusive contracts and ordered data sharing, but left default payments legal
   **Answer:** C
   **Why:** Behavioral, not structural — the toll survives, repriced.
   **Concept tag:** Regulation & structure
7. **Q:** In search advertising, prices are primarily set by:
   **Options:** A) Google's price list B) Advertiser auctions per click C) Government schedule
   **Answer:** B
   **Why:** CPC is an auction outcome; Google's power is auction depth.
   **Concept tag:** Pricing power
8. **Q:** A CR3 of 61% indicates:
   **Options:** A) A fragmented market B) A tight oligopoly C) A monopoly
   **Answer:** B
   **Why:** Above ~60% combined top-3 share is conventionally a tight oligopoly.
   **Concept tag:** Concentration
9. **Q:** The estimated 2026 AI-accelerator market leader and share:
   **Options:** A) NVIDIA, ~75–85% (analyst estimates) B) AMD, ~50% C) Google, ~60%
   **Answer:** A
   **Why:** Estimates, not disclosures — but every major estimate has NVIDIA dominant.
   **Concept tag:** Pricing power
10. **Q:** Cloud shares move slowly mainly because:
    **Options:** A) Prices are regulated B) Switching means re-platforming — high switching costs C) Customers dislike change personally
    **Answer:** B
    **Why:** Migration cost and risk lock in incumbents; Google's 13→16% climb is therefore significant.
    **Concept tag:** Switching costs

## Bridge to next layer

Industries funnel money to structure — but a specific firm captures it through a specific business model, so next: how exactly does Alphabet, the company, turn searches, videos, and servers into cash?

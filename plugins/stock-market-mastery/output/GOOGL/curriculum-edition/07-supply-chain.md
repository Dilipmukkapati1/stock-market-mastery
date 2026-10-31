# Layer 7: Supply Chain — Google (Alphabet) (GOOGL)

> Teaching document · not investment advice · generated 2026-10-31

## Learning objective

After this layer you can trace Alphabet's physical dependencies — chips, memory, fabs, power, land, and third-party capacity — name its single points of failure, read its commitments disclosures like a professional, and explain how a supply shock would travel into the financial statements you studied in Layer 4.

## Why this layer matters for GOOGL

Alphabet looks like a software company and increasingly behaves like an industrial one: ~$51 billion of capex in a single quarter, $924 billion of purchase commitments on the 10-Q, and a product (Layer 6) that is literally made of other companies' silicon output. Its supply chain *is* its strategy — and its biggest operational risk.

## Concepts

### Concept 1 — The capex anatomy: what the money actually buys

**Anchor question:** When Alphabet "spends $200B on AI," what physical things does it buy, and over what lives are they expensed?

**Plain English:** Capex splits into the machines (servers and networking gear — short-lived, replaced often) and the shells (data-center buildings and infrastructure — long-lived). The split determines the future depreciation wave: short lives mean the cost hits earnings fast.

**Formal definition:** Capital expenditure allocation by asset class, with depreciation over disclosed useful lives. Alphabet's Q3 2026 disclosures: ~**65% of capex in technical infrastructure (servers/networking), depreciated over ~6 years; ~35% in data centers and other, over 7–40 years**.

**Formula:** Annual depreciation run-rate ≈ (short-life capex ÷ 6) + (long-life capex ÷ ~20 avg). At a $200B annual capex pace: ≈ ($130B ÷ 6) + ($70B ÷ 20) ≈ $21.7B + $3.5B ≈ **$25B/yr of new depreciation layering in** (book arithmetic, illustrative — actuals depend on in-service timing; Q3 2026 depreciation was $8.37B in the quarter, +49% YoY, per the call/release reporting).

**Reference range:** Server useful lives at hyperscalers run 4–6 years (accounting-policy choices differ and materially move earnings). A capex program is "digesting" when depreciation growth roughly matches revenue growth; it is a risk when depreciation compounds faster.

**Worked example (GOOGL):** Q3 2026 capex of $51.355B against the held full-year guide of $195–205B implies another ~$60B-ish quarter in Q4 (H2 weighting was pre-announced). The 65/35 split means the majority of this spend returns to the income statement within six years — the depreciation wave the bear case (Layer 5's analyst cuts) is pricing. Alphabet adopted the 6-year server life in 2023 and did not change it in 2026 filings — an accounting-policy fact worth checking each 10-K, because extending lives is the classic lever for flattering earnings during a build-out.

> **Source:** Alphabet Q3 2026 earnings call and Form 10-Q · October 2026 (capex composition and useful lives as disclosed); Q3 depreciation +49% per call reporting in research notes.

**Common mistake:** Treating capex as a one-time event. Each year's spend becomes 4–6 years of depreciation; the P&L cost of the 2026 build-out lands in 2027–2032 whether or not the revenue does.

**DIY check:** From the latest 10-Q, find "depreciation" growth and revenue growth. Which is compounding faster? That gap is the digestion question in one comparison.

### Concept 2 — The silicon chain: Broadcom, TSMC, and the memory wall

**Anchor question:** Who physically makes Alphabet's TPUs, and where is the chain thinnest?

**Plain English:** Alphabet designs TPUs; it does not fabricate them. The chain runs: Google architecture → Broadcom co-design and ASIC implementation (its SerDes, packaging coordination) → TSMC fabrication and advanced packaging (CoWoS) → HBM memory from a tiny supplier set (SK hynix, Samsung, Micron) → Alphabet's data centers. Every arrow is a dependency; two of them (TSMC advanced packaging, HBM) are industry-wide chokepoints.

**Formal definition:** Single point of failure = a node whose disruption halts the chain with no short-term substitute. Concentration risk rises when one supplier holds >50% of a critical input.

**Formula:** (Exposure sketch) TPU supply ≈ min(design capacity, wafer starts, CoWoS slots, HBM supply). The chain produces at its *narrowest* node's rate.

**Reference range:** Reported (not Alphabet-disclosed) specifics, labeled as reporting: Ironwood fabricated on TSMC N3P with CoWoS and HBM3e; HBM3e supply via Broadcom split roughly **Samsung ~60% / SK hynix ~40%**, Micron not meaningful for TPU as of mid-2026; TPU v8 targets TSMC N2; MediaTek's inference ASIC entered production in Q4 2026 (all per trade-press reporting in research notes — treat as reported, not confirmed by Alphabet).

**Worked example (GOOGL):** Alphabet mitigates the chain three ways, each visible in 2026 disclosures and announcements: (1) *contractual* — the Broadcom agreement of April 6, 2026 locks TPU development and supply **through 2031**; (2) *architectural* — a second design partner (MediaTek, reported) for cost-optimized silicon reduces single-designer risk; (3) *demand-side* — third-party capacity (Concept 4) shifts some build risk to partners. What it cannot mitigate: TSMC's leading-edge capacity is shared with NVIDIA, Apple, and AMD — Alphabet queues in the same line it competes with (and its packaging/memory inputs are the same ones its rivals bid for).

> **Source:** Broadcom Form 8-K · 2026-04-06 (TPU agreement through 2031); supply-chain specifics from dated trade-press reporting compiled in research notes — **reported/estimated, not Alphabet-disclosed** (labeled per citation rules).

**Common mistake:** Saying "Google makes its own chips." Google *designs* its own chips; the making is outsourced to the same concentrated chain everyone else uses. The advantage is design and margin structure, not fabrication independence.

**DIY check:** For any chip Alphabet ships, list the chain nodes in order and mark the one you'd worry about. Compare your answer with the HBM paragraph above.

### Concept 3 — Power: the real constraint

**Anchor question:** What actually limits how fast Alphabet can add AI capacity in 2026–2030 — chips, buildings, or electricity?

**Plain English:** Increasingly, electricity. Gigawatt-scale campuses need grid connections, generation contracts, and cooling years ahead of the servers. Alphabet's 2026 power moves — utility-scale PPAs including nuclear, and small-modular-reactor development deals — are supply-chain documents as much as energy ones.

**Formal definition:** Power capacity (MW/GW) under contract or development = the binding upper bound on deployable compute; 1 GW ≈ continuous power for roughly a million homes' worth of demand, and a single large AI campus can require several hundred MW.

**Formula:** Deployable accelerators ≈ contracted MW ÷ (MW per rack × racks) — in practice, plan backwards from power: capacity announcements in MW (e.g., Crux AI's first 500 MW, 2027) translate into compute only through the power budget.

**Reference range:** A hyperscale AI campus phase is typically 100–500 MW. Multi-GW portfolios (like Anthropic's ~3.5 GW TPU commitment via Broadcom) are the new unit of account for frontier training.

**Worked example (GOOGL):** October 2026's clearest data point: Alphabet's **Constellation deal (October 6, 2026)** — a 3,590 MW portfolio agreement including an **890 MW nuclear uprate PPA on 20-year terms** — alongside the Kairos Power SMR program (up to 500 MW fleet; first reactor, Hermes 2, under construction, first power targeted 2030) and multi-site developments (Elementl, 3 sites of ≥600 MW). Read together: Alphabet is contracting power on 20-year horizons for a capex program the market debates in quarterly increments — management's time horizon and the market's are visibly different, which is either the opportunity or the trap (Layer 5's split analyst verdicts are exactly this disagreement).

> **Source:** Constellation/Alphabet announcement · 2026-10-06; Kairos Power program disclosures (company statements, as compiled in research notes).

**Common mistake:** Counting data-center announcements instead of energized megawatts. Land and press releases are not power; interconnection queues and PPAs are the real schedule.

**DIY check:** Find one Alphabet capacity headline from 2026 and classify it: land, building, PPA, or energized MW. Only the last two are supply.

### Concept 4 — Commitments and third-party capacity: the obligations under the story

**Anchor question:** What has Alphabet already promised to spend or buy — and how much of its "own" build-out is actually partners'?

**Plain English:** The 10-Q's commitments note is where strategy becomes obligation: purchase commitments, leases not yet commenced, and contingent arrangements (including backstops for partners' TPU projects). In 2026 Alphabet also leaned on third-party capacity — partners building TPU capacity that Google anchors (Fluidstack, Crux AI) and even Oracle offering TPUs — trading margin for speed.

**Formal definition:** Purchase commitments = enforceable obligations to buy goods/services in future periods. Uncommenced leases = signed leases whose terms have not yet begun (off-balance-sheet until commencement, disclosed in notes). Contingent/backstop arrangements = obligations that crystallize only on specified events (e.g., a partner's default).

**Formula:** Q3 2026 10-Q magnitudes: purchase commitments **$924.4B** + uncommenced leases **$130.5B** + contingent/backstop arrangements **~$98.5B** — a >$1.1T obligation stack against $265.1B of cash and securities (Layer 4). (These overlap in purpose — capacity — and are disclosed categories, not a single "debt" number.)

**Reference range:** Commitments of this scale relative to one year's revenue (~$473B TTM, book arithmetic) mean the build-out is *pre-committed*: Alphabet cannot costlessly stop if demand disappoints. That irreversibility is the supply chain's real risk statement.

**Worked example (GOOGL):** Management told investors on the Q3 call to expect **third-party capacity to drag Cloud margins from Q4** — the price of bridging with partners' capacity while internal builds finish. Pair that with the TPU flow from Layer 5 (backlog → inventory → revenue) and the supply chain's full picture emerges: Alphabet is simultaneously builder, anchor tenant, financier, and reseller of the same capacity ecosystem. A shock — HBM shortage, CoWoS delay, power slippage, a partner's financing failure (the backstops!) — propagates through revenue *and* cost *and* contingent obligations at once. That correlation is what "concentration" means at Alphabet's scale.

> **Source:** Alphabet Form 10-Q Q3 2026 · filed 2026-10-29 (commitments note); Q3 2026 earnings call · 2026-10-28 (third-party capacity margin comment — company statement).

**Common mistake:** Reading only the balance sheet for obligations. At Alphabet in 2026 the commitments note is larger than the balance sheet's debt — by an order of magnitude.

**DIY check:** In the 10-Q, find the commitments table and one contingent arrangement. Write the sentence: "If ___ happens, Alphabet owes ___." That sentence is supply-chain literacy.

## Visualization notes (text-first)

Draw the chain as five boxes with arrows: Google design → Broadcom (ASIC) → TSMC fab + CoWoS → HBM (SK hynix/Samsung) → Data centers (power: note "PPA-gated"). Under it, three obligation bars: purchase commitments $924B | uncommenced leases $131B | backstops ~$99B, against a cash bar of $265B. The visual imbalance is the lesson.

## Mastery checklist

- [ ] I can state Alphabet's capex split (~65% servers/networking, ~35% data centers) and the useful lives
- [ ] I can explain how today's capex becomes tomorrow's depreciation wave
- [ ] I can trace the TPU supply chain node by node and name its chokepoints
- [ ] I can distinguish what Alphabet designs from what it fabricates (nothing — TSMC fabricates)
- [ ] I can classify a capacity headline as land, building, PPA, or energized MW
- [ ] I can cite Alphabet's power moves (Constellation PPA, Kairos SMR) with dates
- [ ] I can find and interpret the 10-Q commitments figures ($924.4B / $130.5B / ~$98.5B)
- [ ] I can explain why third-party capacity pressures Cloud margins near-term
- [ ] I can write the "if X, Alphabet owes Y" sentence for a backstop arrangement

## Common misconceptions

1. "Software companies don't have supply chains." — Alphabet's is industrial-scale: fabs, memory, power, and a >$1T obligation stack.
2. "Vertical integration means independence." — Design integration yes; fabrication and memory still run through the industry's shared chokepoints.
3. "Commitments are just future capex, no risk." — They are pre-committed spend: the option to stop has already been sold.

## Quiz (10 questions)

1. **Q:** Alphabet's capex split is approximately:
   **Options:** A) 65% servers/networking, 35% data centers B) 35% servers, 65% land C) 100% chips
   **Answer:** A
   **Why:** As disclosed with Q3 2026; servers carry ~6-year lives.
   **Concept tag:** Capex anatomy
2. **Q:** Server useful life in Alphabet's 2026 filings is:
   **Options:** A) 2 years B) ~6 years (adopted 2023, unchanged) C) 30 years
   **Answer:** B
   **Why:** A policy choice to verify each 10-K — extending it would flatter earnings.
   **Concept tag:** Capex anatomy
3. **Q:** Q3 2026 depreciation did what?
   **Options:** A) Fell 49% B) Rose ~49% YoY to $8.37B in the quarter C) Was zero
   **Answer:** B
   **Why:** The depreciation wave from the build-out has begun landing.
   **Concept tag:** Capex anatomy
4. **Q:** TPUs are fabricated by:
   **Options:** A) Google's own fabs B) TSMC, with Broadcom as design/implementation partner C) Intel
   **Answer:** B
   **Why:** Design is Google's; making is the shared industry chain.
   **Concept tag:** Silicon chain
5. **Q:** The Broadcom agreement of April 2026 runs through:
   **Options:** A) 2027 B) 2031 C) 2026
   **Answer:** B
   **Why:** Development and supply of future TPU generations plus rack networking, per Broadcom's 8-K.
   **Concept tag:** Silicon chain
6. **Q:** HBM supply for TPUs is best described as:
   **Options:** A) Fully in-house B) Reported split mainly Samsung/SK hynix via Broadcom — reported, not Alphabet-disclosed C) Unlimited
   **Answer:** B
   **Why:** Label discipline: trade-press reporting, not company disclosure.
   **Concept tag:** Silicon chain
7. **Q:** Alphabet's October 2026 Constellation deal centers on:
   **Options:** A) Office space B) A 3,590 MW power portfolio incl. an 890 MW nuclear uprate PPA C) Fiber leases
   **Answer:** B
   **Why:** Power is the binding constraint; this is supply-chain contracting.
   **Concept tag:** Power
8. **Q:** The Q3 10-Q purchase commitments were:
   **Options:** A) $92B B) $924.4B C) $9.2T
   **Answer:** B
   **Why:** Plus $130.5B uncommenced leases and ~$98.5B contingent/backstops.
   **Concept tag:** Commitments
9. **Q:** Third-party capacity (Crux AI, Fluidstack, OCI TPUs) near-term effect per management:
   **Options:** A) Raises Cloud margins B) Pressures Cloud margins from Q4 while bridging supply C) No effect
   **Answer:** B
   **Why:** Speed costs margin — management said so on the Q3 call.
   **Concept tag:** Commitments
10. **Q:** The right way to read a data-center headline is to ask:
    **Options:** A) How many jobs it creates B) Whether it is land, a building, a PPA, or energized MW C) Who cut the ribbon
    **Answer:** B
    **Why:** Only contracted/energized power is actual supply.
    **Concept tag:** Power

## Bridge to next layer

You have the facts and the chain they hang from — next, the skill that makes all of it repeatable: reading Alphabet's actual documents like a professional, so the next quarter needs no intermediary.

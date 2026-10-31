# Layer 3: Company Profile — Intel (INTC)

> Teaching document · not investment advice · generated 2026-10-31

## Learning objective

After this layer you can describe Intel's business model as it actually is in late 2026 — an integrated device manufacturer (IDM) trying to become a merchant foundry while its product segments pay the bills — state CEO Lip-Bu Tan's strategy in its own terms, and evaluate Intel's moat *hypotheses* against the segment table.

## Why this layer matters for INTC

Intel is two companies stapled together: a product business (client and server CPUs) that still generates real profit, and a manufacturing business whose losses currently eat much of it. The turnaround thesis claims the second becomes the crown jewel; the bear thesis says it stays an anchor. This layer lays out the machine so you can judge.

## Concepts

### Concept 1 — Segment anatomy: profits here, losses there

**Anchor question:** Which parts of Intel make money, and which consume it?

**Plain English:** Intel reports Client Computing (renamed CCPG in 2026), Data Center and AI (DCAI), Intel Foundry, and All Other. Read the operating-income column, not the revenue column: it shows a profitable product company funding an unprofitable manufacturing build-out.

**Formal definition:** Segment operating income as reported (ASC 280); intersegment revenue (mainly Foundry selling wafers to the product groups) is eliminated in consolidation.

**Formula:** Q3 2026 segment operating income: CCPG **+$2.285B** + DCAI **+$3.039B** + Foundry **−$1.853B** + All Other **+$0.179B** ≈ $3.650B before corporate/unallocated items reconcile to the reported $2.522B consolidated operating income.

**Reference range:** A healthy Intel historically earned operating margins of 20–30% consolidated. A segment losing ~$1.9B per quarter annualizes to a ~$7–8B drag — the scale the product groups must carry.

**Worked example (INTC):** Q3 2026 detail: CCPG revenue $8.097B (−5% YoY — the PC downturn), DCAI $7.318B (**+78%** — Granite Rapids Xeons riding the AI-server build-out), Foundry $6.697B (+58%, nearly all intersegment), All Other $692M. FY2025 baseline for scale: total revenue $52.9B with Foundry losing **−$10.3B** on the year. The stapled-companies picture in one line: in Q3, DCAI and CCPG earned $5.3B of operating profit; Foundry spent $1.85B of it learning to be a merchant manufacturer.

> **Source:** Intel Q3 2026 earnings release · 2026-10-29 (segment table); Intel Form 10-K FY2025 (annual segment baseline).

**Common mistake:** Mourning or celebrating "Intel's margin" as one number. Intel has at least three margins (client ~28% operating, DCAI ~41.5% this quarter, Foundry deeply negative) moving in different directions for different reasons.

**DIY check:** From any Intel release, compute each segment's operating margin. Rank them. Then ask which segment's margin the stock price actually depends on. (Hint: it is not the biggest one.)

### Concept 2 — The IDM 2.0 model and Tan's reset

**Anchor question:** What is Intel's business model supposed to become, and what did the new CEO change first?

**Plain English:** The old Intel designed chips *and* manufactured them, only for itself (IDM 1.0). "IDM 2.0" adds two doors: use outside foundries (TSMC) where that wins product sockets, and sell Intel's own factories to outside customers (foundry). Lip-Bu Tan, CEO since March 2025, ran the reset in a specific order: cut cost and layers first (~a quarter of the workforce — headcount from ~108,900 to ~81,100), cancel speculative fabs (Germany and Poland, July 2025), impose capex discipline — *then* re-accelerate in 2026 (capex guide above $20B, a ~$23B equity offering in August 2026) once the cost base and the 18A ramp could carry it.

**Formal definition:** IDM = integrated device manufacturer (design + manufacture in-house). IDM 2.0 (Intel's term) = IDM plus (a) external foundry usage for select products and (b) a merchant foundry offering (Intel Foundry) serving external customers alongside internal ones.

**Formula:** (Discipline check) Headcount change: 81.1k ÷ 108.9k ≈ **−25.5%**. Employees are the turnaround's first financial fact — most of the 2025–26 cost story is in that ratio.

**Reference range:** Credible turnarounds sequence: stabilize cash → fix the core product engine → scale the new business. Inverting the order (scaling foundry before products and yields) is the pattern that failed under the prior regime's "five nodes in four years" push.

**Worked example (INTC):** The strategy's 2026 scoreboard: 18A reached high-volume manufacturing at Fab 52 (Arizona) in January 2026 and Panther Lake ramped through Q3; the foundry external-customer column is still essentially empty (Layer 2's $411M, mostly one contract); and the product engine wobbled where it should be strongest — Q4 client revenue guided down >20%. Tan's own gating language is the strategy's honest core: Intel will invest in 14A **only with a significant external customer committed**, and may pause or discontinue it otherwise (stated by Tan; reflected in the 10-Q). A CEO willing to name his kill-switch is giving you the thesis's falsifier for free — the capstone will use it.

> **Source:** Intel announcements and Forms 8-K · 2025–2026; Intel Q3 2026 earnings call · 2026-10-29; Form 10-Q Q3 2026 · filed 2026-10-30 (14A gating language as reported).

**Common mistake:** Treating "IDM 2.0" as marketing. It has testable content: foundry external revenue, 18A yield trajectory, and the 14A gate. Grade those, not the slogan.

**DIY check:** Write Intel's strategy as three if/then statements (e.g., "If no external 14A customer signs, then 14A pauses"). Check them against each new quarter.

### Concept 3 — The shareholder register as strategy: government, NVIDIA, SoftBank

**Anchor question:** What does it mean when a company's rescue investors are a government and its biggest ecosystem rival?

**Plain English:** In 2025 Intel's register filled with strategic holders: the **U.S. government** ($8.9B for 433.3M shares at $20.47 — CHIPS Act and Secure Enclave money converted to equity; ~159M shares held in escrow; no board seat; diluted to ~8% by October 2026 after later issuance), **NVIDIA** ($5B at $23.28, closed December 26, 2025, alongside a product partnership), and **SoftBank** ($2B at $23.00, closed September 26, 2025; no board seat, no purchase commitment). These are not ordinary investors: each bought a strategic outcome (U.S. manufacturing capacity, an x86 seat inside AI systems, AI-infrastructure exposure) at 2025's distressed prices.

**Formal definition:** Strategic (vs financial) investment = equity taken to secure a commercial or policy objective, often paired with agreements (partnerships, capacity policy) rather than governance rights. Escrow shares = shares issued but held by a third party pending conditions, creating derivative accounting (Layer 4's mark-to-market lesson).

**Formula:** Government paper gain at Oct 30 close: 433.3M shares × ($65.76 − $20.47) ≈ **+$19.6B** on an $8.9B outlay — before the day's crash trimmed it by ~$12B across the position's mark (research notes). Strategic stakes reprice with the stock they were meant to stabilize.

**Reference range:** A ~8% government stake with a warrant (240.5M shares at $20 if Intel's foundry ownership drops below 51%) is unprecedented for a U.S. blue-chip in peacetime — there is no reference range; that *is* the lesson. Governance analysis must proceed from the documents, not from precedent.

**Worked example (INTC):** Read the warrant as strategy, not finance: it pays the government only if Intel *gives up* control of foundry — i.e., it penalizes the exact breakup some investors wanted, aligning the state with the integrated model. Meanwhile NVIDIA's stake aligns the AI era's kingmaker with x86 CPUs inside its systems (Layer 6). The register is a coalition: each holder's presence argues that Intel's survival-as-integrated-manufacturer is now several powerful parties' stated interest. Coalitions are not cash flows, though — Layer 4 will show what the structure does to the accounts.

> **Source:** Intel deal disclosures (Forms 8-K) · August–December 2025; research notes on stake status and dilution · as of 2026-10-30.

**Common mistake:** Calling the government stake a "bailout" or a "takeover." The documents say: minority equity, no board seat, escrow mechanics, a breakup-penalty warrant. Precision beats labels.

**DIY check:** Find the three 2025 investment prices ($20.47, $23.00, $23.28). Compare them with today's price and with each other. What did each buyer pay for, beyond shares?

### Concept 4 — Moat hypotheses (labeled as hypotheses)

**Anchor question:** What might still protect Intel's economics — and what would break each claim?

**Plain English:** Intel's historic moat was a bundle: x86 software compatibility, manufacturing leadership, and scale. All three legs have been kicked. What remains are narrower claims: the installed base's inertia, advanced packaging, and the strategic-scarcity value of being the only U.S.-headquartered leading-edge manufacturer.

**Formal definition:** Moat hypothesis = a claimed structural advantage with a mechanism and an observable test (the discipline from the GOOGL book applies unchanged).

**Formula:** (Hypothesis register, no formula.) Each hypothesis below carries its breaking test.

**Reference range:** A moat claim is credible when its observable has held under attack for years. Intel's observables are mostly *deteriorating but not collapsed* — the honest category is "eroded moat, contested repair."

**Worked example (INTC):** *Hypothesis 1: installed-base inertia.* Mechanism: enterprises and PC fleets standardize on x86; migration is slow. Test: unit share. Reading: server units 65.5% (Q2 2026) — holding in units, leaking in revenue (Layer 2). *Hypothesis 2: packaging as the new edge.* Mechanism: as transistor scaling slows, EMIB/Foveros advanced packaging (and chiplets) decide system performance; Intel's Fab 9 (New Mexico) and its glass-substrate collaboration (Lens Technology, noted in the Q3 release) position it here. Test: external packaging wins and attach to foundry deals. Reading: promising, unproven at merchant scale. *Hypothesis 3: strategic scarcity.* Mechanism: the only U.S. leading-edge option commands policy support and customer diversification demand. Test: whether that converts into *binding* customer commitments — the same test as the whole foundry thesis. Reading: support is real ($8.9B of it); commitments are not yet.

> **Source:** Mercury Research · Q2 2026; Intel Q3 2026 earnings release · 2026-10-29 (packaging collaboration); deal disclosures · 2025. Moat framing is the book's analysis, labeled hypothesis per the writing standards.

**Common mistake:** Declaring the moat "dead" because it narrowed. Moats are graded on a slope: Intel's is negative-sloping in CPUs, possibly positive-sloping in packaging and strategic value. One word cannot hold all three.

**DIY check:** Write one Intel moat hypothesis and its breaking test. You will reuse it in the capstone.

## Visualization notes (text-first)

Draw the stapled company: two columns — "Products: CCPG +$2.29B, DCAI +$3.04B (Q3 operating income)" and "Manufacturing: Foundry −$1.85B" — with an arrow labeled "funds" from left to right. Beneath, the register: Government ~8% · NVIDIA ~215M shares · SoftBank ~87M shares, each annotated with what it bought besides stock.

## Mastery checklist

- [ ] I can state each segment's Q3 2026 revenue and operating income
- [ ] I can explain IDM 2.0 and how it differs from the old model
- [ ] I can sequence Tan's reset (cuts → discipline → re-acceleration) with dates
- [ ] I can state the 14A gate in Tan's own terms
- [ ] I can describe the three strategic stakes (prices, size, rights) accurately
- [ ] I can explain the government warrant's anti-breakup logic
- [ ] I can present three Intel moat hypotheses with their breaking tests
- [ ] I can explain why headcount (108.9k → 81.1k) is a financial fact, not an HR footnote

## Common misconceptions

1. "Intel is a chip company with a fab problem." — It is a profitable product company stapled to a loss-making manufacturer; analyze the staple.
2. "The government bought Intel." — It bought ~8–10% minority equity with no board seat and a very specific warrant.
3. "Moats are alive or dead." — Intel's are eroding, repairing, and emerging at different rates in different segments.

## Quiz (10 questions)

1. **Q:** Q3 2026 segment operating income: the two product segments earned about:
   **Options:** A) $0.5B combined B) $5.3B combined (CCPG $2.285B + DCAI $3.039B) C) $15B combined
   **Answer:** B
   **Why:** Against Foundry's −$1.853B — the stapled-company picture.
   **Concept tag:** Segments
2. **Q:** DCAI's Q3 2026 growth was:
   **Options:** A) +7.8% B) +78%, its best in 15 years C) −78%
   **Answer:** B
   **Why:** Granite Rapids demand in the AI-server build-out.
   **Concept tag:** Segments
3. **Q:** IDM 2.0 adds which two doors to the old model?
   **Options:** A) Retail stores and phones B) Using external foundries for some products, and selling Intel's fabs' capacity to external customers C) Cloud services and advertising
   **Answer:** B
   **Why:** Both directions of openness define the model.
   **Concept tag:** Strategy
4. **Q:** Tan's first moves in 2025 were:
   **Options:** A) A mega-merger B) ~25% workforce reduction and cancelling the Germany/Poland fabs C) A stock split
   **Answer:** B
   **Why:** Cost and discipline before re-acceleration.
   **Concept tag:** Strategy
5. **Q:** The 14A gate, in Tan's framing, is:
   **Options:** A) Build at any cost B) Proceed only with a significant external customer, else possibly pause/discontinue C) Wait for 2030
   **Answer:** B
   **Why:** The thesis's built-in falsifier.
   **Concept tag:** Strategy
6. **Q:** The U.S. government's 2025 investment was:
   **Options:** A) $8.9B at $20.47/share, ~433.3M shares, no board seat B) $89B and a board takeover C) A loan only
   **Answer:** A
   **Why:** CHIPS + Secure Enclave funds converted to minority equity, partly in escrow.
   **Concept tag:** Strategic register
7. **Q:** NVIDIA's and SoftBank's 2025 stakes were priced at:
   **Options:** A) $100+ B) $23.28 (NVIDIA, $5B) and $23.00 (SoftBank, $2B) C) $5 each
   **Answer:** B
   **Why:** Both closed in late 2025 at distressed-era prices.
   **Concept tag:** Strategic register
8. **Q:** The government warrant (240.5M shares at $20) pays off if:
   **Options:** A) Intel's stock doubles B) Intel's ownership of Foundry falls below 51% C) Intel pays a dividend
   **Answer:** B
   **Why:** An anti-breakup device aligning the state with integration.
   **Concept tag:** Strategic register
9. **Q:** Which moat hypothesis is about EMIB/Foveros?
   **Options:** A) Installed-base inertia B) Advanced packaging as the new edge C) Strategic scarcity
   **Answer:** B
   **Why:** As scaling slows, packaging decides system performance — Intel's Fab 9 bet.
   **Concept tag:** Moat hypotheses
10. **Q:** FY2025 Foundry operating result was:
    **Options:** A) +$1B B) −$10.3B C) Break-even
    **Answer:** B
    **Why:** On $17.8B of mostly intersegment revenue with only $307M external.
    **Concept tag:** Segments

## Bridge to next layer

The profile describes a coalition-backed turnaround with a built-in kill-switch — now the audit: do the financial statements corroborate it, and what on earth is happening in Intel's nine-month income statement?

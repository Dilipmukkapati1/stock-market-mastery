# Layer 7: Supply Chain — Intel (INTC)

> Teaching document · not investment advice · generated 2026-10-31

## Learning objective

After this layer you can map Intel's physical network — the fabs, the one supplier it cannot replace (ASML), the substrates and packaging chain, the China exposure, and the geographic risk that stopped being theoretical in October 2026 — and explain how the 14A gating rule ties the supply chain to the strategy's survival.

## Why this layer matters for INTC

Alphabet rents its supply chain's risks; Intel *is* a supply chain. Its product is atoms: wafers, lithography, chemicals, substrates, power, and cleanrooms on three continents. Every layer of this book collapses into this one — if the fabs don't execute, there is no product story, no financial story, and no foundry story.

## Concepts

### Concept 1 — The fab network: footprint as strategy

**Anchor question:** Where does Intel actually make things, and what does the 2026 map say about its priorities?

**Plain English:** Intel's manufacturing footprint is the strategy drawn on a map: leading-edge logic concentrated in Arizona and Ireland and Israel; the Ohio mega-site deferred to the next decade; the European expansion cancelled; advanced packaging in New Mexico and Malaysia. Each site is a bet about cost, subsidies, talent, and risk.

**Formal definition:** Fab network = the set of wafer fabrication plants (fabs) by node and location, plus assembly/test and packaging sites. High-volume manufacturing (HVM) status — not construction status — is the operative fact for each leading-edge site.

**Formula:** (Status ledger, October 2026) **Fab 52, Arizona: 18A in HVM since January 2026**, Panther Lake ramping. **Ohio (New Albany): production now targeted 2030–31** (Mod 2 in 2032) — first structural truss raised October 21, 2026: a construction site, not a supply source, for years. **Fab 62 (Arizona): tool move-in began October 2026** for ~2028 operations. **Germany/Poland: cancelled July 2025** (Tan discipline). **Fab 9, New Mexico: advanced packaging** (EMIB/Foveros). **Fab 28, Kiryat Gat (Israel):** producing — and the site of October's incident (Concept 4).

**Reference range:** A leading-edge fab costs $20–30B+ to build and equip; the decision-to-HVM cycle is 4–6 years. Footprint decisions made in 2026 bind the company into the 2030s — there is no fast correction.

**Worked example (INTC):** Read the map as Tan's triage: protect the node that decides survival (18A in Arizona — co-located with the packaging and the U.S. policy coalition of Layer 3), defer the monument (Ohio), cancel the speculative (Europe), and keep packaging — the rising-value node — close (New Mexico). The map also explains the 10-Q's **$19.6B of capex commitments**: equipment and construction obligations that proceed on their own schedule regardless of quarterly demand — operating leverage in physical form (Layer 2's cyclicality, Layer 4's balance sheet).

> **Source:** Intel announcements and Q3 2026 reporting compiled in research notes · 2025–2026; Form 10-Q Q3 2026 · filed 2026-10-30 (commitments).

**Common mistake:** Counting fabs instead of reading statuses. A fab under construction, a fab installing tools, and a fab in HVM are three different assets wearing one word.

**DIY check:** For each Intel fab you can name, assign its status (HVM / tool-in / construction / cancelled) with a date. If you cannot date it, you do not know it.

### Concept 2 — The ASML dependency: the supplier with no substitute

**Anchor question:** What is the one machine Intel cannot buy from anyone else?

**Plain English:** Leading-edge chips are printed with extreme-ultraviolet (EUV) lithography, and exactly one company sells EUV systems: ASML (Netherlands). Intel, TSMC, and Samsung all queue for the same machines — including the newest High-NA EUV, where Intel was an early adopter. ASML's delivery schedule is, quite literally, a constraint on Intel's roadmap.

**Formal definition:** Single-source dependency = a critical input available from one qualified supplier, where qualification of an alternative would take years. EUV and High-NA EUV are the semiconductor industry's canonical case.

**Formula:** (Exposure logic) Leading-edge capacity additions ≈ min(ASML systems delivered and installed, fab shells ready, process readiness). Any term can bind; in 2026 for Intel the binding terms have been process readiness and demand gating, not machines — a fact that should temper "ASML is the bottleneck" clichés.

**Reference range:** An EUV system costs roughly $200M (High-NA: ~$350–400M per system, as reported) and ships in ~20 freight containers. At Intel's capex scale, a handful of systems is a billion-dollar line — and a multi-quarter schedule dependency.

**Worked example (INTC):** Intel's High-NA bet is the dependency's double edge: adopting early (systems installed at its Oregon development fab) bought learning-curve time for 14A-class nodes — and concentrated risk on an immature tool ecosystem that its rivals can let Intel debug first. Layer the second-order dependencies the same way: substrates (a concentrated Japanese supplier base), specialty chemicals and gases, and — for packaging — the glass-substrate collaboration with Lens Technology noted in the Q3 release. A supply-chain chapter's job is the full graph, but EUV is its load-bearing node: no ASML, no 18A, no story.

> **Source:** ASML/EUV industry structure from dated reporting compiled in research notes; High-NA pricing as reported (labeled estimates); Intel Oregon development disclosures.

**Common mistake:** Assuming "designed in America" means "supplied from America." The leading-edge chain is Dutch lithography, Japanese materials, Taiwanese competition, and global gases — Intel's U.S. fabs sit inside a world supply web.

**DIY check:** Draw Intel's chain as five boxes (design → EUV lithography → wafers/materials → fab → packaging/test) and mark each box's most concentrated supplier. The marked boxes are your risk register.

### Concept 3 — China exposure and the policy weather

**Anchor question:** How much of Intel's business runs through China, and what can policy change overnight?

**Plain English:** China is simultaneously Intel's largest market (about a quarter of revenue), a manufacturing and assembly location, and the focus of export controls that decide what Intel may sell there. Policy is therefore a supply-chain *and* demand-chain variable: controls can remove products from the China market, tariffs can tax the flow, and Chinese domestic champions are policy-favored substitutes.

**Formal definition:** Geographic revenue concentration = revenue attributable to customers in a region ÷ total revenue (as disclosed by customer location in the 10-K — note it measures the customer's location, not final consumption). Export-control exposure = the share of the catalog subject to licensing restrictions for a destination.

**Formula:** FY2025 China revenue: **$12.694B ÷ $52.9B ≈ 24%** of Intel's total (down from ~29% in the prior year — the direction is the policy working). Add the January 2026 **25% Section 232 tariff** development on certain chip imports (as reported) to the cost side of the ledger.

**Reference range:** A single-country share above ~20% of revenue is a concentration to underwrite explicitly. For Intel the figure is doubly loaded: the same country is customer, competitor-sponsor, and geopolitical counterparty to its largest shareholder (the U.S. government).

**Worked example (INTC):** The three channels, concretely: (1) *Demand* — a quarter of revenue transacts with China-based customers; controls on advanced parts mostly spare Intel's mainstream CPUs today, but the boundary moves by rulemaking, not by Intel's preference. (2) *Substitution* — domestic Chinese CPU efforts (and Arm/RISC-V ecosystems) are subsidized precisely to displace x86 share over time: a slow leak under the 24%. (3) *Operations* — assembly/test footprint in Asia means tariffs and logistics shocks hit cost directly. Note the strange loop: U.S. policy simultaneously *funds* Intel (CHIPS, the equity stake) and *constrains* its biggest market. Reading Intel's risk factors with that loop in mind is this layer's core skill.

> **Source:** Intel Form 10-K FY2025 (China revenue); export-control and tariff developments from dated reporting compiled in research notes (labeled).

**Common mistake:** Treating "China exposure" as one number. It is three channels (demand, substitution, operations) with different speeds and different hedges.

**DIY check:** From the 10-K's geographic revenue table, compute China's share for two consecutive years. Then write one sentence per channel on what would move it next.

### Concept 4 — When geography stops being theoretical: Fab 28

**Anchor question:** How does a single fab incident become a guidance line?

**Plain English:** On October 14, 2026, an explosion at Fab 28 in Kiryat Gat, Israel — a fatal incident — disrupted production at a working fab. Two weeks later it appeared in Intel's Q4 guidance as approximately **−$300M of revenue and −200bp of gross margin**. This is operational risk with the abstraction removed: concentrated production plus hazardous processes plus geopolitics equals financial exposure that no diversification slide fully hedges.

**Formal definition:** Operational/geographic concentration risk = the expected financial loss from disruption at a single site, driven by the site's share of critical output and the difficulty of re-routing production (leading-edge wafers cannot be re-routed at all in the short term).

**Formula:** Incident cost as disclosed ≈ $300M revenue (≈1.9% of a ~$15.5B guided quarter) + ~200bp of GM (≈$300M of gross profit at guide midpoint — book arithmetic). One site, one event, roughly $0.6B of combined quarterly P&L impact.

**Reference range:** For multi-fab mature-node products, a site loss is absorbable (re-route, buffer stock). For single-sourced leading-edge output, a serious incident is a multi-quarter event. Intel's structure — leading edge split across Arizona, Ireland, and Israel — is partial mitigation, node by node.

**Worked example (INTC):** The professional reading has three steps. First, the human fact: the incident was fatal — analysis comes after acknowledging that. Second, the financial mechanics: wafers in process are scrapped, the line restarts through requalification, and fixed costs deleverage across the quarter's volume — exactly the guided pattern (revenue down, margin down ~200bp). Third, the strategic echo: Fab 28 is why "geographic diversification" appears in Intel's site strategy (and in customers' minds when they weigh Intel Foundry against single-region alternatives) — and why Layer 2's foundry customers will ask about it by name. Supply-chain chapters exist so that when the headline comes, you already own the framework: site → node → products → guidance.

> **Source:** Intel Q3 2026 earnings guidance disclosures · 2026-10-29 (incident impact as reported); dated news reporting on the October 14, 2026 Fab 28 explosion compiled in research notes.

**Common mistake:** Treating incident disclosures as PR. The guided $300M/200bp figures are management's own quantification — file them as the calibration for every future "minor disruption" claim, from any chip company.

**DIY check:** Pick one Intel product and trace which fab(s) make its wafers. If the answer is one fab, you have found a concentration; write down what a one-month outage would do to that product's revenue.

## Visualization notes (text-first)

Draw the map in words: Arizona (Fab 52 HVM 18A; Fab 62 tools-in) · Oregon (development, High-NA) · New Mexico (packaging) · Ireland (mature/leading support) · Israel (Fab 28 — incident flag) · Ohio (2030s, construction) · Asia (assembly/test). Above it, the single-source banner: "EUV/High-NA: ASML only." Below, the China bar: 24% of FY2025 revenue, down from 29%.

## Mastery checklist

- [ ] I can list Intel's fab statuses (HVM / tool-in / construction / cancelled) with dates
- [ ] I can explain why HVM status, not construction, is the operative fact
- [ ] I can state the capex commitments figure ($19.6B) and its source
- [ ] I can explain the ASML single-source dependency and Intel's High-NA double edge
- [ ] I can decompose China exposure into demand, substitution, and operations channels
- [ ] I can compute China's FY2025 revenue share (≈24%) from the 10-K figures
- [ ] I can walk the Fab 28 incident from site → guidance ($300M, ~200bp) in three steps
- [ ] I can connect the 14A gate to supply-chain reality: no customer, no fab investment

## Common misconceptions

1. "Intel's supply chain is its own, so it's safe." — Ownership concentrates risk; the chain still runs through ASML, Japanese materials, and geopolitics.
2. "More fabs = more resilience." — Only *qualified, running* capacity at the right node is resilience; construction is a promise.
3. "China risk is a headline thing." — It is 24% of revenue, a substitution program, and an operations footprint — three slow variables, not one fast one.

## Quiz (10 questions)

1. **Q:** 18A reached high-volume manufacturing at:
   **Options:** A) Fab 52, Arizona, in January 2026 B) Ohio, in 2026 C) Germany, in 2025
   **Answer:** A
   **Why:** Ohio is a 2030s site; Germany was cancelled.
   **Concept tag:** Footprint
2. **Q:** Ohio's production is now targeted for:
   **Options:** A) 2027 B) 2030–31 (Mod 2 in 2032) C) It opened in 2025
   **Answer:** B
   **Why:** First truss raised Oct 21, 2026 — construction, not supply.
   **Concept tag:** Footprint
3. **Q:** Intel's capex commitments per the Q3 10-Q were:
   **Options:** A) $1.96B B) $19.6B C) $196B
   **Answer:** B
   **Why:** Obligations that proceed regardless of quarterly demand.
   **Concept tag:** Footprint / commitments
4. **Q:** EUV lithography systems are sold by:
   **Options:** A) ASML only B) Five competing vendors C) Intel itself
   **Answer:** A
   **Why:** The industry's canonical single-source dependency.
   **Concept tag:** ASML dependency
5. **Q:** Intel's early High-NA adoption is best described as:
   **Options:** A) Pure advantage B) A double edge: learning-curve lead plus concentrated risk on an immature tool ecosystem C) Irrelevant
   **Answer:** B
   **Why:** Rivals can let Intel debug first — the follower's discount.
   **Concept tag:** ASML dependency
6. **Q:** China's share of Intel's FY2025 revenue was about:
   **Options:** A) 4% B) 24% ($12.694B), down from ~29% C) 60%
   **Answer:** B
   **Why:** Demand concentration with a policy-driven downward slope.
   **Concept tag:** China exposure
7. **Q:** The three China channels are:
   **Options:** A) Price, promotion, place B) Demand, substitution, operations C) Debt, equity, cash
   **Answer:** B
   **Why:** Different speeds, different hedges — never one number.
   **Concept tag:** China exposure
8. **Q:** The Fab 28 incident's guided Q4 impact was approximately:
   **Options:** A) None B) −$300M revenue and −200bp gross margin C) −$3B revenue
   **Answer:** B
   **Why:** Management's own quantification, October 29, 2026.
   **Concept tag:** Fab 28
9. **Q:** Leading-edge wafers can be re-routed to another fab after an incident:
   **Options:** A) Freely, overnight B) Essentially not at all in the short term — process qualification binds output to sites C) Only on weekends
   **Answer:** B
   **Why:** Which is why single-site nodes are concentrations, not conveniences.
   **Concept tag:** Fab 28
10. **Q:** The 14A gate connects strategy to supply chain because:
    **Options:** A) It is a marketing slogan B) Without a significant external customer, Intel may not build the capacity at all — the supply chain is conditional on demand proof C) ASML requires it
    **Answer:** B
    **Why:** Tan's rule makes the fab map a function of the customer ledger.
    **Concept tag:** Gating

## Bridge to next layer

You now hold the map and its failure points — the final skill is doing this without a book: reading Intel's own filings directly, which is what the document-literacy chapter trains, filing by filing.

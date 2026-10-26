# Chapter 6 — Products & Moat

**Learning objective:** Describe what Glean sells beyond "AI search," and evaluate — with hypotheses clearly labeled — whether any of it constitutes a durable competitive advantage.

## Concept 1: The product stack

**Plain English.** Three layers that expanded over time: (1) **Enterprise search** — one box across 100+ (reported up to 275+) workplace connectors, ranked by a company-specific knowledge graph; (2) **Assistant** — conversational RAG over that indexed knowledge, with model routing across 40+ LLMs to control cost; (3) **Agents** — Glean Agents (no-code workflow automation, 1B agent-actions target for end-2025), a Slack-based agent, and Tau, a desktop AI workspace.

> **Source:** Sacra · https://sacra.com/c/glean/ · Brief News · 2026-09-02

**Why the order matters.** Search was the wedge: easy to trial, obvious ROI ("find anything instantly"), deployable without changing workflows. Assistants and agents are the expansion: deeper lock-in, bigger budgets, harder to rip out. Land-and-expand is the oldest SaaS playbook; Glean is running it with AI.

## Concept 2: Moat candidates — scored honestly

1. **Permissions-aware architecture.** The product *cannot* show you what you can't already access — enforced in real time across every connector. Replicating this correctly across 275+ integrations is genuinely hard, and getting it wrong is existential. *Grade: moderate-to-strong — the closest thing to a moat.*
2. **Knowledge graph / enterprise context.** Six years of tuning relevance on company-specific data. Replicable in principle, but the tuning data (what employees clicked, what answers worked) accumulates. *Grade: moderate — a data advantage, not a fortress.*
3. **Connector breadth (100–275+).** Each integration is table stakes individually; the *set* is the asset. But connectors are also the most replicable layer — hyperscalers own the underlying apps. *Grade: weak-to-moderate.*
4. **Model routing / cost discipline.** Using 40+ models and avoiding premium frontier models where possible is smart procurement, not a moat — it's an explicit admission the model layer *isn't* defensible. *Grade: operational edge, not a moat.*
5. **Enterprise trust & deployments.** ~200 customers including Intuit, Booking.com, Zillow; company-wide deployments doubled in 2025. Trust compounds — but it's rented, not owned; one permissions incident could reset it. *Grade: real but fragile.*

**Common mistake.** Calling "AI" the moat. The models are rented; the moat — if any — is in the *plumbing*: permissions, connectors, and relevance tuning on proprietary interaction data.

**DIY check.** For each claimed moat ask: "What would it cost Microsoft to replicate this in 18 months — and would the result be 'good enough' for 80% of buyers?"

## Concept 3: Where the competition bites

**Plain English.** The threat matrix, ranked: (1) **Bundling** — Copilot/Gemini included with suites enterprises already buy; the permanent tax on Glean's pricing power. (2) **Platform absorption** — ServiceNow bought Moveworks; the Sana takeout shows platforms will buy rather than build — good for Glean's exit optionality, bad for its independence. (3) **Feature parity** — every SaaS vendor now ships "AI search over your data"; Glean must stay ahead on *cross-app* depth, the one thing single-vendor tools can't do.

**Strategic implication (hypothesis).** Glean's best defense is being the *neutral* layer across vendors' apps — the one thing Microsoft and Google structurally can't be for each other's suites. Neutrality isn't just a feature; it's the strategy.

---

## Mastery check — Chapter 6

1. Name Glean's three product layers and say which one has the deepest workflow lock-in.
2. Which moat candidate is strongest, and what single event would destroy it?
3. In two sentences, explain why "neutrality" is both Glean's defense and its acquisition bait.

**Bridge:** Products and moats describe the upside — Chapter 7 prices the downside.

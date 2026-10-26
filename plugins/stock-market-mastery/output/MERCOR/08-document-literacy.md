# Chapter 8 — Risks

## Risk 1: The March 2026 data breach

Between **March 24–27, 2026**, attackers compromised Mercor through **LiteLLM**, an open-source library in its stack — a supply-chain attack. Exfiltrated: roughly **4TB**, including ~211GB of candidate records (SSNs, government IDs), ~3TB of video and biometric verification data, and ~939GB of source code. **40,000+ contractors** were affected. Mercor confirmed the breach on **March 31, 2026**.

> **Source:** Wall Street Journal · breach confirmation · 2026-03-31 (via theagenttimes.com)
> **Source:** StrikeGraph · "The Mercor breach exposed Silicon Valley's fragile AI supply chain" · Sep 2026 · https://www.strikegraph.com/blog/the-mercor-breach-exposed-silicon-valleys-fragile-ai-supply-chain

## Risk 2: The litigation overhang

**Five class-action suits** were filed April 1–7, 2026 in California and Texas federal courts — including *Gill v. Mercor* and *Ananthula v. Mercor.io Corp.* (No. 3:26-cv-03362, N.D. Cal., nationwide class). The claims go beyond ordinary breach negligence (no MFA, unencrypted PII alleged) into the product itself: Illinois' **BIPA** (biometric privacy), the Illinois **AI Video Interview Act**, and the **Fair Credit Reporting Act** — the theory being that Mercor's AI scoring profiles are employment reports that individuals can't access or challenge. If the FCRA/BIPA theories gain traction, they threaten the AI-interview model, not just the balance sheet. Mercor disputes the claims as speculative; the cases were ongoing as of September 2026 with no quantified exposure disclosed.

> **Source:** Hausfeld · Mercor Data Breach claim page · 2026 · https://www.hausfeld.com/what-we-do/current-claims/mercor-data-breach
> **Source:** The Innovation Attorney · legal analysis · Sep 2026

**And the commercial consequence already happened:** Meta's April 2026 contract pause (Chapter 7) is the breach's cost showing up in revenue, not in court.

## Risk 3: Valuation credibility

The numbers themselves are contested. In January 2026, analyst Brian Hart publicly questioned the 5x valuation jump in ~4 months as narrative-driven. In June 2026, CEO Foody accused Sequoia of dual-tranche "valuation tricks," triggering wider scrutiny of ARR and valuation headline inflation across AI startups. Neither proves anything about Mercor specifically — but when credible observers dispute the *genre* of numbers you're relying on, and the company publishes nothing audited, the correct response is wider error bars, not dismissal.

> **Source:** Medium · Brian Hart · 2026-01-12 · Neura Market · 2026-06-09

## Risk 4: Take-rate compression

Covered quantitatively in Chapter 5: the take rate *is* the margin. Surge (profitable, bootstrapped) and Turing (profitable, cheaper) can both afford to undercut. A fall from ~35% to ~25% cuts net revenue ~30% at constant volume. Labs also renegotiate from strength at every renewal — and they know Mercor needs them more than they need Mercor.

## Risk 5: Workforce practices and key people

Pre-breach reporting documented mandatory surveillance tooling (camera/mic/browser), opaque project availability for contractors, and heavy PII collection (SSNs, passports, facial selfies) — practices that fed directly into the breach's blast radius and the litigation's theories. Separately: this is a founder-concentrated company — three founders holding ~66% combined, a 23-year-old CEO as the public face, and a strategy (stay private, per Foody's own remarks) set by a very small circle. No labor-classification suits have been reported to date — record as *none found*, not *none possible*.

## Risk summary table

| Risk | Status | Severity driver |
|---|---|---|
| Customer concentration | **Demonstrated** (Meta pause) | Top-lab revenue share (undisclosed) |
| Breach litigation | Ongoing, 5 suits | FCRA/BIPA theories reach the core product |
| Take-rate compression | Structural pressure | Profitable rivals can undercut |
| Valuation credibility | Contested publicly | No audited figures to settle it |
| Key-person / governance | Structural | ~66% founder ownership, tiny decision circle |

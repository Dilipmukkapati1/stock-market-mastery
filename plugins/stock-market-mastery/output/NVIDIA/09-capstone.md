# Part Two · Deep Research 3 — Customers, Deals & Risks

## Who pays: the demand stack

Estimated hyperscaler AI capital expenditure for 2026 runs to roughly $500B across the industry (trade estimates), with company-level guides reported around Alphabet $175–185B, Amazon $128B+, and Meta ~$72B at the low end of its range — treat these as reported figures that managements revise quarterly. NVIDIA's $1T "visibility" claim (Huang at GTC, March 2026: at least $1T of revenue visibility across 2025–2027 for Blackwell + Rubin) is a management expectation, not backlog — but the quarterly prints ($57.0B → $68.1B → $81.6B → $96.2B → guided $108B) have so far run *ahead* of the rhetoric.

The demand stack has four layers, in declining order of certainty:

1. **Hyperscalers (~55% of Data Center)** — funded from operating cash flow, strategically committed, multi-year. The risk is not cancellation; it is mix-shift to their own silicon.
2. **AI labs (inside ACIE and via clouds)** — OpenAI, Anthropic and peers. Funded by venture and strategic capital at unprecedented scale; NVIDIA is now directly one of the funders (the $30B OpenAI investment).
3. **Neoclouds (CoreWeave, Nebius, Lambda...)** — debt-financed GPU landlords whose borrowing is collateralized by NVIDIA hardware and contracts. NVIDIA rents back ~$26B of capacity from cloud partners (per filings) — support for this layer is partly NVIDIA's own balance sheet.
4. **Sovereign and enterprise** — governments and industry building on-prem AI. Slower, lumpier, strategically durable; the layer least correlated with Silicon Valley funding cycles.

## The circularity question, stated precisely

The bear argument is often stated sloppily. Here is the precise version, with the numbers from Deep Research 1: NVIDIA (a) invests in customers ($30B into OpenAI), (b) guarantees customers' infrastructure obligations (lease guarantees capped at $105B for OpenAI's Ohio campus), (c) commits to buy back capacity from clouds (~$26B), and (d) books revenue when those same ecosystems buy GPUs. If AI end-demand disappoints, the losses do not stop at unsold chips: they arrive as guarantee calls, written-down equity stakes, and rent-back obligations — while $95.2B of supply commitments still come due. That is a genuinely new risk structure for this company, and it did not exist in fiscal 2025.

The bull answer is equally concrete: the guarantees are capped and sized against ~$100B of annual free cash flow; the Ohio guarantee backstops leases for capacity NVIDIA's other customers will use if OpenAI cannot; equity stakes in OpenAI/CoreWeave have so far *added* billions in gains; and every dollar of ecosystem financing is a dollar a rival ecosystem does not get. Vendor financing built Lucent's grave in 2001 and built Apple's supply chain in 2010 — the instrument is neutral; the underwriting is the question. What to monitor: operating cash flow conversion (Q2's $24.1B vs $59.7B net income is the first yellow flag), guarantee growth per quarter, and whether rent-back commitments keep doubling.

## Risk register

| Risk | Severity | Evidence / trigger to watch |
|---|---|---|
| Hyperscaler ASIC mix-shift | High, slow | Custom silicon est. 15–25% of accelerator market by 2026; watch ACIE vs hyperscale mix |
| Capex digestion / AI ROI disappointment | High | One hyperscaler guide-down would re-rate the whole chain; NVIDIA's supply commitments are ~$95.2B |
| Circular financing unwind | Medium-high, new | Guarantee cap $105B; watch OCF vs net income gap and new commitments per 10-Q |
| Customer concentration | Medium-high | Top direct customers 16/15/13% of H1 FY27 revenue |
| Export controls / China | Medium | $4.5B H20 charge precedent; H200 terms (incl. reported 25% U.S. share) can change by policy |
| Power and deployment bottlenecks | Medium | 600 kW racks (2027) meet grids that permit in years, not quarters |
| Execution of annual cadence | Medium | Blackwell's delayed ramp is the template; Rubin Ultra's Kyber rack is a bigger leap |
| Antitrust (bundling) | Low-medium | Reported DOJ/EU probes; remedies would target the full-stack model |
| Key person | Low probability, high impact | Strategy and trust concentrated in the founder-CEO |
| Taiwan/geopolitics | Low probability, severe | The entire advanced chain runs through Taiwan; unhedgeable |

## What would change the story

A quarter where Data Center revenue misses guidance while guarantees grow; a hyperscaler announcing its internal silicon covers the majority of inference; CUDA-abstraction reaching production parity (watch large labs publishing non-CUDA training runs); or operating cash flow lagging net income for three consecutive quarters. Until one of those prints, the risk section is a list of conditionals, and the financial section is a list of records.

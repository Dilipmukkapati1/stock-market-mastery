# Part Two · Deep Research 2 — Technology & Competition

## The CPU business: a decade-long share theft

AMD's server CPU position, per Mercury Research: **34.5% unit share overall (Q2 2026), up from 27.3% a year earlier; 46.4% unit share on the data-center-class view (EPYC vs Xeon SP); 46.2% server revenue share (Q1 2026)**. Intel — which held >95% of this market a decade ago — is at 65.5% overall and 53.6% DC-class, still falling. Client is the same story at smaller scale: record 30.3% x86 unit share (desktop 34.9%, mobile 28.9%).

Why EPYC wins: Zen's chiplet architecture delivers more cores, better perf/watt, and more memory bandwidth per socket — and hyperscalers, who buy on total cost of ownership, noticed first. Venice (Zen 6, TSMC 2nm) extends the roadmap into 2027. **This business alone — high-share, high-margin, still gaining — is the floor under AMD's valuation.**

> **Source:** The Register · Mercury Research Q2 2026 · 2026-08-21

## The AI accelerator business: real, and still small

Scale check, because headlines obscure it: NVIDIA's data-center revenue was **$193.7B in FY2026**; AMD's *entire* Data Center segment was $16.6B. NVIDIA takes ~80–85% of AI accelerator revenue; AMD holds ~5–7%; custom ASICs (Google TPU, AWS Trainium, Broadcom-designed) take ~12–18%.

AMD's product answer has three layers:

1. **Silicon parity at inference.** MI355X (288GB HBM3E) matches or beats B300-class parts on key inference benchmarks in MLPerf (92% offline / 104% interactive, Llama 2 70B, v6.0; record 512-GPU cluster result in 6.1). Memory capacity — more HBM per GPU — is AMD's structural edge for large-model serving.
2. **Rack-scale systems (Helios).** The MI450 + Venice + Pensando Helios rack, shipping late 2026, is AMD's move from selling chips to selling NVIDIA-GB200-style systems — where the margin and the lock-in live. Annual rack cadence promised.
3. **Software (ROCm).** The gap is narrowing fastest exactly where AMD's customers deploy (inference: PyTorch/vLLM first-class; +38% throughput from software updates alone in one MLPerf cycle). Training remains CUDA's fortress: developer mindshare, NCCL networking maturity, and a decade of tooling.

> **Source:** MLPerf v6.0 & 6.1 independent analyses · Apr/Sep 2026 · accelerator share trackers · Oct 2026 (estimates)

## The competitive triangle

- **NVIDIA** is simultaneously AMD's target and its ceiling: every GW deal AMD wins is measured against CUDA's gravity. NVIDIA's ~$89B/quarter data-center revenue (latest reported) vs AMD's $6.7B shows the gap is not closing in absolute terms even as AMD's share inches up — the market is growing faster than share shifts.
- **Custom silicon is the structural threat to both merchants.** Broadcom's AI revenue exceeded $20B in FY2025 with a $73B backlog; hyperscalers designing their own chips (TPU, Trainium, Meta's MTIA) cap the merchant-GPU TAM. AMD's counter: be the flexible, available second source — and embed itself via EPYC CPUs in the same racks.
- **Intel** matters mainly as a share donor in CPUs and a cautionary tale: process-roadmap failure destroyed a 95% franchise in a decade. AMD's fabless TSMC dependence is the mirror-image risk (see Risks).

**Net assessment:** AMD is the only credible merchant alternative to NVIDIA in AI accelerators and the share leader-in-waiting in server CPUs. "Only credible #2" in a market this size is an enormously valuable position — if execution holds.

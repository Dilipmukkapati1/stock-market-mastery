# Part Two · Deep Research 2 — Technology & Competition

## What NVIDIA actually sells now: a seven-chip computer the size of a building

Vera Rubin is the clearest statement of the strategy. It is not a GPU launch; it is a co-designed platform of six core chips (seven with the optional tier): the **Rubin GPU** (dual-die, 336B transistors, TSMC 3nm, 288 GB HBM4 at up to 22 TB/s), the **Vera CPU** (Arm-based, succeeding Grace), **NVLink 6** (the fabric that makes 72 GPUs behave as one processor), **ConnectX-9** SuperNICs, the **BlueField-4** DPU, and the **Spectrum-6** Ethernet switch — plus the Groq-derived LPU technology for low-latency inference that NVIDIA licensed/acquired in late 2025 (reported ~$20B deal; treat the figure as press-reported). NVIDIA's claim set for the NVL72 rack — 3.6 exaFLOPS FP4 inference, ~5x Blackwell inference performance, ~10x lower cost per token on agentic and mixture-of-experts workloads — are manufacturer numbers; the direction is corroborated by the memory-bandwidth jump, which is physics, not marketing: HBM4 nearly triples bandwidth per GPU, and inference is a bandwidth business.

The competitive meaning: a challenger must now match a *system* — silicon, fabric, software, and the install base's tooling — delivered on an annual cadence. The roadmap extends the pressure: Rubin CPX (inference racks, end of 2026), Rubin Ultra (2027, NVL576 racks at ~600 kW — power delivery becomes the product), Feynman (2028). Each year the target moves.

## The three competitive fronts

**1. AMD — the merchant rival.** AMD is the only other merchant GPU vendor at scale, with the MI-series accelerators, the Helios rack system, and landmark wins (the OpenAI and Meta 6 GW agreements analyzed in the companion AMD book). AMD's pitch is price and openness: MI300-class parts have been offered at roughly 20–30% below NVIDIA on comparable workloads, and ROCm keeps improving. AMD takes the share NVIDIA's pricing and allocation leave behind — real revenue, but so far the overflow, not the core.

**2. Custom ASICs — the customers' insurrection.** This is the structural front. Google's TPU (Ironwood generation, built for inference, pods of 9,216 chips), Amazon's Trainium3 (UltraServers generally available December 2025; Anthropic a named customer), Microsoft's Maia, Meta's MTIA, and Broadcom's co-designed accelerators for OpenAI and Meta. Industry forecasts (cited in trade coverage) project custom-ASIC shipments growing ~44.6% in 2026 against ~16.1% for GPUs, taking custom silicon to perhaps 15–25% of the AI-accelerator market; NVIDIA's share of accelerator *revenue* is estimated to ease from ~87% (2024) toward ~75–80% (2026) — analyst estimates, not measurements. Google's commitment of up to one million TPUs to Anthropic from 2026 is the proof point that ASICs now serve frontier training and inference for third parties, not only internal workloads.

Why ASICs win where they win: a hyperscaler running one model family at enormous, stable volume can strip out generality and pay for exactly the silicon it uses. Why they don't win everywhere: models change monthly, generality is insurance, CUDA's ecosystem compresses time-to-deployment, and most of the world (enterprises, sovereigns, startups, neoclouds — NVIDIA's 45% ACIE bucket) has no ASIC program at all. The honest synthesis: ASICs cap NVIDIA's share of hyperscaler inference first, training later; they do not address the majority of demand pools.

**3. The software-abstraction front.** If PyTorch/JAX-level abstraction (and compiler layers like Triton) make accelerators interchangeable, CUDA's switching costs erode. Progress is real but slow; production AI remains littered with CUDA-specific kernels and tooling. Watch this space over a 3–5 year horizon, not a quarterly one.

## Supply chain — the constraint underneath everything

NVIDIA is fabless: TSMC fabricates (increasingly with U.S. capacity in Arizona coming online for Blackwell-class parts), SK Hynix, Micron and Samsung supply HBM, and a Taiwan-centered chain assembles racks. The binding constraints of the Rubin era are **HBM4 supply** and **power** — a single Rubin Ultra rack at ~600 kW means a 1 GW campus hosts on the order of 1,500 racks; customers' access to powered land now gates deployments as much as chip supply. NVIDIA's ~$95.2B of supply commitments are how it reserves its place in line. Geographic concentration (Taiwan, Korea, Israel, China in the chain) remains the unhedgeable tail risk in the 10-K's own risk factors.

## Antitrust

Reported U.S. DOJ and EU scrutiny of NVIDIA's bundling practices (chips tied to networking and software allocation) is unresolved and slow-moving, but it targets exactly the full-stack strategy described above. Treat as a live, low-probability, high-impact item.

# Part One · Section 5 — Product Quality

**The short version:** AMD's CPUs are best-in-class or co-best by independent measures; its AI GPUs are now genuinely competitive at *inference*; its software is much improved but still the gap.

**CPUs — independently verified leadership.** Mercury Research (Q2 2026): AMD server **unit share 34.5%** overall and **46.4%** on the data-center-class comparison (EPYC vs Xeon SP); server **revenue share 46.2%** (Q1 2026). Client x86 share hit a **record 30.3%** (desktop 34.9%). Share gains of this size, sustained over years, are the market's verdict on product quality — EPYC's core counts, efficiency, and memory bandwidth win competitive deals.

**AI GPUs — competitive at inference, catching up at training.** In **MLPerf Inference v6.0** (Apr 2026), MI355X posted ~**92% of NVIDIA B300** offline throughput and **104%** of interactive throughput on Llama 2 70B. MLPerf 6.1 (Sep 2026) added a record 512-GPU MI355X cluster result (5.75M tokens/sec, GPT-OSS-120B) and wins over GB200 at 72-GPU scale on that model. NVIDIA still leads most *training* benchmarks and several Llama configurations. AMD's own vendor claims (e.g., up to 1.4× B200 on DeepSeek-R1 serving) should be read as vendor claims.

**Software — the honest gap.** ROCm is materially better: PyTorch/vLLM support is now first-class for inference, and ROCm updates alone added **+38% throughput on identical MI355X hardware** in MLPerf — proof the stack was leaving performance on the table and is closing. Remaining friction: dependency quirks, a thinner GPU cloud-rental market, and CUDA's two-decade ecosystem head start, especially in training.

> **Source:** The Register · Mercury Research Q2 2026 · 2026-08-21 · MLPerf v6.0/6.1 independent analyses · Apr & Sep 2026

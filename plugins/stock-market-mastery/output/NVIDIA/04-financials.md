# Part One · Section 4 — Products

NVIDIA's product is increasingly a **platform sold as a system**, on an annual cadence:

**Data-center platforms (the business):**
- **Blackwell (B200 / GB200 NVL72)** — the 2024-25 generation; a rack of 72 GPUs acting as one computer.
- **Blackwell Ultra (B300 / GB300)** — shipping since H2 2025: 288 GB of HBM3e memory per GPU, ~1.1 exaFLOPS of FP4 per NVL72 rack. The current revenue workhorse.
- **Vera Rubin (VR200)** — in full production since June 1, 2026 (announced at GTC Taipei), partner systems ramping through H2 2026. A six-to-seven-chip co-designed platform: Rubin GPU (336B transistors, TSMC 3nm, 288 GB of HBM4 at up to 22 TB/s), the new **Vera CPU**, **NVLink 6**, **ConnectX-9** networking, **BlueField-4** DPU, and **Spectrum-6** Ethernet. NVIDIA claims 3.6 exaFLOPS of FP4 inference per NVL72 rack and up to ~10x lower cost per token than Blackwell on agentic workloads — manufacturer claims on chosen workloads; treat as directional.
- **Rubin CPX** (end of 2026, inference-optimized rack), **Rubin Ultra** (H2 2027; NVL576 "Kyber" racks of 576 GPU dies at ~600 kW), **Feynman** (2028). The roadmap is public and, so far, on schedule.

**The software layer (the moat):** CUDA and its libraries; TensorRT and Dynamo for inference; NVIDIA AI Enterprise; and domain stacks — Omniverse and Cosmos for "physical AI" (robotics, factories, autonomous vehicles), DRIVE for cars, and Isaac for robots. Software is rarely broken out in revenue, but it is the reason the hardware is hard to displace.

**Everything else:** GeForce RTX 50-series for gaming (Blackwell-based), RTX PRO workstations, and Jetson edge/robotics modules — strategically useful (developer mindshare, physical AI optionality), financially minor next to the data center.

The buying unit matters: customers no longer spec a GPU, they order racks and whole data-center designs (power, cooling, networking included as reference architectures). That raises the ticket size, deepens lock-in — and concentrates NVIDIA's fate in a handful of very large purchase orders.

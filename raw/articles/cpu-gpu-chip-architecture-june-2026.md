# CPU/GPU/Chip Architecture — June 2026

## Sources

- [Intel & AMD: Advanced Compute Extensions (ACE) — x86 AI standard](https://www.techspot.com/news/112846-intel-amd-unveil-new-x86-standard-make-cpus.html) — June 22, 2026
- [NVIDIA: RTX Spark Superchip for Windows PCs](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark) — May 31, 2026
- [NVIDIA Vera Rubin Supercomputers](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-delivers-world-class-supercomputers-for-science) — June 22, 2026
- [NVIDIA Blackwell MLPerf Training v6.0](https://developer.nvidia.com/blog/nvidia-blackwell-tops-mlperf-training-6-0-with-industry-leading-scale-and-performance/) — June 16, 2026
- [Samsung: 3D-Stacked Transistor, 42nm Gate Pitch](https://www.techtimes.com/articles/318572/20260621/samsung-builds-industrys-smallest-3d-stacked-transistor-wins-vlsi-best-paper.htm) — June 21, 2026
- [MoonMath AI: Open-Source HIP Attention Kernel for AMD MI300X](https://www.marktechpost.com/2026/06/22/moonmath-ai-open-sources-a-hip-attention-kernel-for-amd-mi300x-that-beats-aiter-v3-on-every-shape-and-rounding-mode/) — June 22, 2026
- [AMD Zen 6 "Olympic Ridge" — Zen 6, NPU, No iGPU](https://wccftech.com/amd-olympic-ridge-zen-6-ryzen-cpus-get-integrated-npu-at-the-cost-of-igpu/) — June 15, 2026
- [AMD Ryzen AI Max PRO 400 — 300B Parameter Local AI](https://www.amd.com/en/blogs/2026/amd-powers-next-generation-agent-computers-with-new-ryzen-ai-hal.html) — June 2026
- [NVIDIA "Blackwell-Next" GPU in Linux Kernel](https://www.techpowerup.com/350159/nvidias-blackwell-next-gpu-appears-in-linux-kernel-patches) — June 22, 2026

---

## 1. Advanced Compute Extensions (ACE) — Intel & AMD
**Date:** June 22, 2026

Intel and AMD jointly unveiled a new x86 specification to bring AI capabilities directly to CPUs.

**Key specs:**
- Extends existing AVX10 register structure with dedicated matrix operation hardware
- **Up to 16× more operations per instruction** vs. standard AVX10
- Supports INT8 and MX block-scaled formats (low-precision)
- Designed for **edge use cases** and **latency-sensitive tasks**, not large-scale training
- Keeps data on CPU — avoids GPU power/overhead for smaller models
- Also avoids NPU fragmentation (NPUs are becoming common but are far from standardized)

**Strategic significance:** This is the x86 industry's answer to the question "are CPUs becoming irrelevant for AI?" The answer so far: no, but they need dedicated silicon, not just instruction tweaks. The ACE standard means both Intel and AMD ship compatible CPU cores, creating a unified x86 AI ecosystem separate from GPU/NPU silos.

---

## 2. NVIDIA RTX Spark — Windows PCs for Personal AI Agents
**Date:** May 31, 2026

NVIDIA's most aggressive push into PC AI, built for the "agent" paradigm.

**Architecture:**
- **NVIDIA Blackwell RTX GPU** — 6,144 CUDA cores, 5th-gen Tensor Cores (FP4 precision)
- **NVIDIA Grace CPU** — 20 cores, co-designed with MediaTek
- **NVLink-C2C** chip-to-chip interconnect (high-bandwidth CPU-GPU coupling)
- Up to **128GB unified memory**
- **1 petaflop of AI performance**

**Capabilities:**
- Runs **120B-parameter LLMs** locally at 1-40 tokens/sec with ray tracing/DLSS/Reflex
- Adobe re-architecting Photoshop and Premiere with full GPU acceleration (2× performance)
- Blender Cycles adding DLSS Ray Reconstruction for real-time path-tracing
- RTX Video Frame Generation (2× or 4× framerate in real time)
- Coming fall 2026 from ASUS, Dell, HP, Lenovo, Microsoft Surface, MSI

**Inference speed improvements:**
- 2× performance in llama.cpp
- 2.6× performance in vLLM
- 2× multi-GPU enhancements in llama.cpp and ComfyUI

---

## 3. NVIDIA Vera Rubin Supercomputing Platform
**Date:** June 22, 2026

The enterprise/supercomputing counterpart to RTX Spark.

**Specs:**
- **7 exaflops of AI** performance
- **5 petaflops of native FP64** (scientific computing)
- Up to **144 GPUs** per system in a single rack
- **TOP500-class** supercomputing in one rack
- Vera CPU + Vera Rubin GPU + NVLink-C2C + ConnectX-9 SuperNICs + BlueField-4 DPUs
- Direct liquid-cooled architecture
- Available Q4 2026 from HPE, Dell, GIGABYTE, HPE, Supermicro

**Deployments:**
- Los Alamos National Lab: Mission (national security), Vision (open science), Veritas (agentic AI for science)
- Covers climate modeling, CFD, energy, materials science, nuclear/fusion energy, quantum computing, foundation models, agentic AI

---

## 4. Samsung 3D-Stacked Transistor — 42nm Gate Pitch
**Date:** June 21, 2026

Samsung won Best Paper at VLSI 2026 for a vertically stacked 3D FET at 42nm gate pitch.

**Key facts:**
- 42nm gate pitch (down from 48nm) — smallest reported
- Competitor Intel demonstrated CFET at 45nm at the same conference
- **TSMC also demonstrated comparable structures**
- This is the same family as CFET (Complementary FET)

**Impact:**
- Vertical stacking halves the area of CMOS pairs vs. planar — **doubles transistor count per wafer**
- Samsung claims **100% performance gain** in a single step (vs. ~15% from conventional node shrink)
- Double the power efficiency per unit area

**Market context:** Samsung's foundry business has struggled with yields and lost customers to TSMC. This best paper doesn't fix fab execution, but signals the engineering talent is there as Samsung targets foundry profitability in 2028.

---

## 5. MoonMath AI — Open-Source HIP Attention Kernel for AMD MI300X
**Date:** June 22, 2026

Independent team open-sources a bf16 attention kernel that beats AMD's own AITER v3.

**Performance vs AITER v3:**
| Shape (B,H,S,D) | vs AITER | vs MAX |
|---|---|---|
| (2,24,8192,128) | 1.23× | 1.37× |
| (2,24,16384,128) | 1.26× | 1.54× |
| (2,24,32768,128) | 1.18× | 1.57× |
| (1,16,131072,128) | 1.16× | 1.46× |

**Geomean:** 1.18× (RTNE), 1.15× (RTNA), 1.08× (RTZ)

**Technical approach:** One-instruction assembly wrappers let compiler allocate registers; memory placement drives most gain (K in LDS, V hot in L1, Q in registers). Integrated into SGLang PR, improving Wan2.1 video diffusion by 1.23×.

---

## 6. AMD Zen 6 "Olympic Ridge" — Ryzen 7 5800X3D 10th Anniversary Edition
**Date:** June 15, 2026

AMD's 2027 desktop lineup: Zen 6 on TSMC N2P (2nm), integrated NPU, **no iGPU**.

**Specs:**
- TSMC **2nm "N2P"** process
- Up to **24 cores with SMT**, up to 48MB L3 cache
- Integrated **NPU in the IO die** (first non-APU AMD chips with NPU)
- **Removes onboard iGPU** — diagnostic capabilities reduced
- CUDIMM-ready DDR5 platform with EXPO 1.2
- Wi-Fi 7 support

---

## 7. AMD Ryzen AI Max PRO 400 — 300B Parameter Local AI
**Date:** June 2026

AMD's workstation-class AI processor for agent computers.

**Specs:**
- **World's first x86 client processor** capable of running 300B-parameter models locally
- Built on **Zen 5** architecture
- **RDNA 3.5 graphics** + **XDNA 2 NPU**
- Up to **192GB system memory**, **160GB VRAM**
- Q3 2026 from HP and Lenovo

---

## 8. NVIDIA "Blackwell-Next" / Rubin in Linux Kernel
**Date:** June 22, 2026

Linux kernel patches reveal NVIDIA is already preparing driver support for the next-gen GPU architecture.

**Key details:**
- Patches include Compute Express Link (CXL) support
- Despite NVIDIA confirming the codename as "Rubin," engineers reference "Blackwell-Next"
- Rubin is planned for both consumer (GeForce RTX) and server (DGX/AI accelerator) lines
- Rubin will power RTX Spark SoC alongside Vera CPU

**Signal:** Rubin is in active development. The fact that it's appearing in kernel patches now means it's likely to be announced in the next 6-12 months.

---

## Summary Table

| Company | Product/Technology | Key Metric | Timeline |
|---------|-------------------|------------|----------|
| NVIDIA | RTX Spark | 1 petaflop AI, 6144 CUDA cores, 128GB unified memory | Fall 2026 |
| NVIDIA | Vera Rubin NVL4 | 7 EFLOPS AI, 5 PFLOPS FP64, 144 GPUs/rack | Q4 2026 |
| NVIDIA | Blackwell Ultra GB300 | 1,648 TFLOPS/GPU on DeepSeek-V3 | Now |
| Intel | ACE (Advanced Compute Extensions) | 16× more ops vs AVX10, x86 AI standard | June 2026 |
| AMD | Zen 6 Olympic Ridge | 24 cores, NPU, TSMC N2P, no iGPU | 2027 |
| AMD | Ryzen AI Max PRO 400 | 300B parameter local inference, 192GB RAM | Q3 2026 |
| Samsung | 3D-Stacked FET | 42nm gate pitch, 2× efficiency | VLSI 2026 |
| NVIDIA | Rubin GPU | Next-gen after Blackwell, Rubin CPU | 2027-2028 |
| MoonMath | Attention Kernel (HIP) | 1.18-1.26× vs AITER v3 on MI300X | June 2026 |

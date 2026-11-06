<tbc>permits VRAM over-subscription by evicting buffers to system memory. After such an eviction the free-memory query overstates the available VRAM, and a workspace that seemingly fits degrades performance by an order of magnitude while consuming host RAM. The API therefore accepts a hint of the caller’s resident memory, which caps the budget.

### Launch and compilation.

With 23 values of _s_ and several kernel variants, the module contains about 150 kernels. When built just-in-time without per-kernel device-code splitting, the first call compiles all of them, which takes 38s. With `-fsycl-device-code-split=per\_kernel` or ahead-of-time compilation for `bmg-g21`, the first call takes 30-60ms ( 5). All work is submitted asynchronously to one in-order queue, and `gemm` and `zgemm` return a `sycl::event`.

### What did not help.

Running the memory-bound CRT of one tile on a second queue, concurrently with the INT8 GEMM of the next tile, produced no overlap, because the GEMM occupies all Xe cores. Two-pass row-maximum reductions and vector loads did not improve the scaling kernels, which already run at memory speed.

## 7 Experimental setup

All measurements were taken on an Intel Arc Pro B60 (24GB, maximum GPU clock 2400MHz) under Ubuntu 26.04.1 LTS with Linux 7.0 and the `xe` kernel driver. The display is driven by a separate GPU, so the B60 carries no graphics workload. Because the library is fully device- resident, the host system does not affect the GPU measurements; the host CPU serves only to compute reference results with Intel MKL DGEMM/ZGEMM for the accuracy comparison. We used the Intel oneAPI DPC++/C++ Compiler 2026.1.1 (SYCL 2020 \[32\]), oneMKL 2026.1 \[33\] and the Level Zero runtime, with ahead-of-time compilation for `bmg-g21`.

\begin{tabular}{ccccc}
build & _s_=8 (first) & _s_=12 & _s_=16 & warm call \\
AOT (bmg-g21) & 0.029 & 0.002 & 0.003 & 0.0004 \\
JIT, per-kernel split & 0.057 & 0.004 & 0.004 & 0.0004 \\
JIT, default & 38.379 & 0.001 & 0.001 & 0.0005 \\
\end{tabular}

16384
184
184
184
185
185
185
180
12288
125
129
131
133
129
122
170
8192
182
184
185
185
185
185
160
m (= lda)
150
6144
171
176
178
178
179
178
TOP/s
4096
182
183
186
185
185
185
140
2048
176
179
179
182
186
186
130
2048
4096
6144
8192
12288
16384
n

Figure 1: oneMKL INT8 `gemm\_batch` throughput (TOP/s) by tile shape, _k_=8192.

5: First-call latency in a fresh process (s).


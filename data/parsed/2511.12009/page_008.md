<tbc>its applicability to N-Queens problems with N\(\le\)23. For solving 24-26 Queens problems, we were compelled to adopt Configuration 2, which showed approximately 13% lower computational efficiency than Configuration 3. When addressing larger problem sizes up to 27 Queens, Configuration 1 became necessary, demonstrating a further 14% performance reduction compared to Configuration 2.

The three optimization techniques proposed in this work - block/stack size optimization, last-row optimization, and in- line PTX optimization - demonstrate consistent performance improvements across various GPU architectures, though the magnitude of gains may differ from those observed on RTX 4090.

## 4.5 Multi-GPU Performance Evaluation

The experimental results above comprehensively validate the effectiveness of our optimization methodology in solving the N-Queens problem. To further enhance computational performance, we expanded our experimental platform from a single GPU card to 8 GPU cards, investigating the efficiency gains through increased parallelism for larger N.

Given the substantial time and resource requirements for multi-GPU experiments with larger N (N\>24), optimal computational configurations must be predetermined. We focus on two critical parameters: (1) the impact of pre-placed rows on multi-GPU platform, and (2) the performance differences between uniform and non-uniform task partition strategies.

To validate this hypothesis, we first implemented a uniform partition strategy <sup>6</sup> and adopted configuration 2 to measure per-GPU computation time for 22- and 23-Queens problems with pre-placed rows ranging from 5 to 8 rows under 8 RTX 4090 GPUs. The experimental results (in seconds) are presented in  7.

Two principal conclusions emerge from  7:

1. Optimal performance occurs with 6 row pre-placement, while 5 row and 7 row configurations demonstrate comparable efficiency. Consequently, we fix the pre- placed rows to 6 for solving 20- to 26-Queens problems.<tbc>

2. Under uniform task partition, significant variance emerges in per-GPU execution times (exceeding 100% difference), with systematically longer durations for later- subproblem processing. This observation necessitates adopting a non-uniform partition strategy where higher- numbered GPUs receive progressively smaller task allocations. Further analysis reveals partition dependents on value N. Given the impracticality of customizing allocation schemes for each individual N values, we just implemented a non-uniform partition based on computation time of each GPU in table 7: **[0.20, 0.15, 0.12, 0.11, 0.11, 0.11, 0.10, 0.10]** for all problems. While potentially suboptimal for specific cases, this scheme delivers substantial performance improvements over uniform partition.

After finalizing the pre-placed rows and task partition ratio, we systematically employed Configuration 2 to benchmark larger N values. Besides RTX 4090, RTX 5090 and A100 are also involved. The execution times for 20- to 25-Queens problems are presented in figure 5. The A100 exhibits substantially inferior computational performance compared to the RTX 4090, showing approximately 45% performance gap. This conclusively demonstrates that core count is the critical performance determinant for N-Queens problems. The RTX 5090 is approximately 22% faster than the RTX 4090, falling short of the expected 30% performance improvement.

Comparing the above figure with  6, both cases solve the 22-queens problem using RTX 4090 GPUs, the 8-GPU configuration achieves a speedup of only 6.5\(\times\) compared to the single-GPU setup (37.5 vs. 245), which falls short of the theoretical expectation. The primary reason is the imperfect load balancing of subproblems, leading to uneven computational workloads across GPUs.

<sup>6</sup>Each GPU was assigned an equal number of subproblems to process.

\begin{tabular}{cccccccccc}
**R** & **0** & **1** & **2** & **3** & **4** & **5** & **6** & **7** \\
5 & 28.5 & 32.5 & 33.1 & 41.2 & 41.6 & 41.9 & **47.8** & 44.4 \\
6 & 19.1 & 24.0 & 27.2 & 29.1 & 36.1 & 35.6 & **39.6** & 38.5 \\
7 & 19.2 & 24.1 & 27.5 & 29.4 & 35.3 & 39.7 & **42.6** & 42.3 \\
8 & 21.5 & 26.4 & 30.3 & 32.5 & 36.2 & 44.5 & 46.4 & **49.3** \\
\end{tabular}

\begin{tabular}{cccccccccc}
**R** & **0** & **1** & **2** & **3** & **4** & **5** & **6** & **7** \\
5 & 228 & 272 & 270 & 356 & 332 & 389 & 382 & **401** \\
6 & 167 & 216 & 234 & 274 & 313 & 320 & **353** & 349 \\
7 & 172 & 218 & 241 & 261 & 338 & 337 & **389** & 374 \\
8 & 184 & 235 & 257 & 269 & 357 & 362 & **443** & 419 \\
\end{tabular}

100000
53104
5090
4090
A100
28332
21880
10000
5307
2205
2840
1000
562
309
233
100
67.6
29.1
37.5
9.2
10
4.9
6.2
2.2
2.6
2.9
1
20
21
22
23
24
25

** 7.** Per-GPU Computation Time (ID from 0 to 7) for 22-Queens (Top) and 23-Queens (Bottom) Problems with Uniform Task Partition Under Varying Pre-placed Rows Using 8 RTX 4090 GPUs

**Figure 5.** Computation Time (in Seconds) for Solving 20- to 25-Queens Problems on 8 GPU Cards


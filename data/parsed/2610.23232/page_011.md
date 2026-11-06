<tbc>**Trade-off between update and search.** Figure 14b shows the trade-off between update and search with varying thread allocation from search-heavy setting to update-heavy setting on _Workload C_. Compared to the most advanced baselines of graph-based and partition-based methods, our PrairieFire can achieve both high update and search throughputs across varying ratios of update to search throughput. OdinANN suffers from the high latency and concurrency limitations of the graph structure, and thus cannot achieve high-throughput updates. SPFresh achieves higher update throughput than OdinANN, but more cores than PrairieFire are needed to improve update throughput, which leads to a significant drop in search throughput.

**Cascaded adjustment.** Figure 15a shows the impact of cascaded adjustment on recall rate in _Workload A_. Without cascaded adjustment (W/O CA), the recall rates can drop by up to 3% in the process, even with rebuilds to improve the index quality \[64\]. Level-1 and Level-0 adjustments (i.e., L-1 CA and L-0 CA) can avoid the loss of efficacy and improve recall rates by up to 1.5% and 2.9%.

**Performance ablation.** Figure 15b shows the throughput improvements by _Workload C_, from software designs. Naive implementation (Naive) has a coarse-grained lock that objects from the same upper-level cluster are locked together, which can lead to high contention and low throughput. With decoupled locks (i.e., D-L) in §5.4, throughputs of update and search can be improved by up to 2.3\(\times\) and 3.2\(\times\), respectively. Batched GPU level-0 search (i.e., B(L0)) can further improve throughputs by 0.4-0.7\(\times\) naive’s performance. And parallelizing in-buffer and on-SSD search (i.e., P(L2)) can further improve search throughputs to 4.6\(\times\). And fused background micro- scale clustering (i.e., F(B)) can further improve update throughput by ∼1.5\(\times\), because fewer background threads can support more foreground update threads.

Figure 16 shows the contribution of additional hardware (i.e., GPUs and more SSDs). In Figure 16a, CPU means CPU-only PrairieFire with buffering updates and clustering-based rebuilds, while +1GPU offloads level-0 search and level-2 on-SSD search from half of 10 SSDs to a GPU. +2GPU is the fully equipped configuration with two GPUs and 10 SSDs. With different scale subsets from SIFT1B, as the scale increases, the bandwidth burden of level-0 flat search and level-2 on-SSD search becomes more significant, GPUs<tbc>

<tbc>can bring up to 3.4\(\times\) and 4.1\(\times\) improvement in update and search. In Figure 16b, the contribution of SSDs is illustrated, showing how additional SSDs enhance the overall system throughput. Since update is not I/O-bound, the improvement is mainly observed in search operations. With more SSDs, PrairieFire can support linear scaling in search performance under concurrent update and search.

## 6.4 Hardware Efficiency

Based on evaluations on SIFT1B, Figure 17 shows the hardware efficiency of PrairieFire in terms of device price, energy, and storage footprint. The information about hardware costs in our platform is shown in  3. For OdinANN and SPFresh, we minimize baselines’ hardware with no GPUs and fewer SSDs (i.e., 2-4 SSDs), which can reach the performance of §6.2 and reduce the cost to ∼32K and the total power to ∼600W, respectively.

**Efficiency of acquisition cost.** We use aggregate throughputs of updates and searches on _Workload C_ under the thread configurations in  2 as the performance metric, and use the total cost of acquisition (TCA) from  3 as the cost metric. As shown in Figure 17a, although PrairieFire requires two additional GPUs and thus has about 1.5\(\times\) higher total device cost than OdinANN and SPFresh, it achieves 3-5\(\times\) higher aggregate throughput, leading to a 2.2-3.4\(\times\) improvement in devices’ cost efficiency.

**Power efficiency.** We use the aggregate throughput as the performance metric, and use the thermal design power (TDP) as the cost metric, when evaluating power efficiency. As shown in Figure 17b, although PrairieFire incurs about 650W higher consumption than OdinANN and SPFresh due to additional GPUs, it still achieves a ∼1.5-2.4\(\times\) improvement in cost efficiency in terms of QPS per watt.

\begin{tabular}{ccccccc}
 & **Chassis** & **CPU** & **GPU** & **Mem** & **SSD** & Total \\
**TCA** & \(1\times\) $3K & \(1\times\) $4K & \(2\times\) $6K & \(12\times\) $2K & \(10\times\) $0.4K & $47K \\
**TDP** & \(1\times\) 50W & \(1\times\) 400W & \(2\times\) 300W & \(12\times\) 10W & \(10\times\) 8W & 1250W \\
**CAP** & - & - & 96 GB & 768 GB & ∼20,000 GB & - \\
\multicolumn{2}{c}{**Cost Per Unit Storage**} & 125 $/GB & 31 $/GB & 0.2 $/GB & - \\
\end{tabular}

Search Memory
100
Update
60
50
40
OdinANN
50
20
SPFresh
Ours
Throughput (KQPS)
20
0
0
1
2
4
8
16
Peak Memory (GB)
Search
Throughput (KQPS)
0
20
40
0
Update
Buffering Count
Throughput (KQPS)

0.95
Naive
+D-L
+B(L0) +P(L2) +F(B)
W/O CA
+L-0 CA
5
Update Throughput
0.90
+L-1 CA
Speed Up
0
Recall@10
0.85
0
20
40
60
80
100
5
Search Throughput
Update Process (%)

Update:
CPU
+1GPU
+2GPU
4
Search:
CPU
+1GPU
+2GPU
Throughput speedup (x)
2
Throughput speedup (x)
5
0
0
1M
10M
100M
1B
1
2
4
6
8
10
Dataset Scale
Count of SSDs

OdinANN
SPFresh
Ours
2
75
60
50
40
QPS / $ (TCA)
1
QPS Watt
25
QPS / $ (Storage)
20
0
0
0

**(a) Throughput and memory.**

**(b) Update and search.**

**Figure 14: Resource and performance trade-offs.**

**(a) Cascaded adjustment.**

**(b) Performance improvements.**

**Figure 15: Ablation study of accuracy and performance.**

**(a) GPU contribution.**

**(b) SSD contribution.**

**Figure 16: Extra hardware contribution for PrairieFire.**

**(a) TCA efficiency.**

**(b) Power efficiency.**

**(c) Storage efficiency.**

**Figure 17: Cost efficiency on device price, energy, and storage.**

** 3: Our hardware costs \[11, 12, 15\]. TCA: total cost of acquisition; TDP: thermal design power; CAP: capacity. The chassis consists of mainboard and other components.**


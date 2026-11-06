<tbc>controller adds 3.5W within a 225mm<sup>2</sup> BGA package. The total power of ∼18.5W remains significantly lower than high- end GPUs such as the NVIDIA H100, which consumes up to 700W under peak workloads \[35\] with higher latency.

### C. RAPID-Graph Performance and Efficiency

#### 1) Speedup and Energy Efficiency:

We compare RAPID- Graph against CPU and GPU (A100 and estimated H100) baselines on graphs with 100, 1024, and 32768 nodes synthesized using NiemaGraphGen \[34\]. These sizes avoid memory bottlenecks on single-node hardware. Fig. 7 shows large gains in speed and energy. At 1024 nodes, RAPID-Graph delivers \(1061\times\) speedup and \(7208\times\) energy efficiency over CPU. At 32768 nodes, it outperforms H100 by \(42.8\times\) in speed and \(392\times\) in energy. RAPID-Graph’s performance gains grow with graph size due to enhanced parallelism and in-memory execution. This performance gap widens dramatically with graph size because conventional systems are overwhelmed by _O(n_<sup>3</sup>) data movement. This massive data transfer saturates memory bandwidth that RAPID-Graph inherently avoids.

We also compare RAPID-Graph with SOTA PIM method PIM-APSP \[16\] and SOTA GPU clusters methods Partitioned APSP \[10\] and Co-Parallel APSP \[11\]. On OGBN-products (2.5M nodes) dataset \[31\], we estimate their performance from reported scaling trends. As shown in Fig. 8, RAPID-Graph outperforms both, achieving \(5.8\times\) speedup over Co-Parallel APSP and \(1186\times\) energy savings over Partitioned APSP. While PIM-APSP improves energy efficiency by \(11.4\times\), it slows down performance to \(0.7\times\) of the baseline. The advantage of RAPID- Graph comes from removing inter-GPU communication, the dominant limiter at large-scale, multi-node APSP solutions.

#### 2) Scalability:

Fig. 9 compares the scalability of RAPID- Graph and the H100 GPU baseline across graph degree, size, and topology. In Fig. 9(a,d), both systems maintain stable performance across degree, suggesting edge count has limited effect on exact APSP when memory is sufficient. In Fig. 9(b,e), RAPID-Graph scales linearly to 2.45M nodes, while H100 exhibits rising latency and superlinear energy growth beyond 10<sup>3</sup> nodes due to communication overhead. H100 is limited by the _O(n_<sup>2</sup>) distance matrix overwhelms its caches, whereas RAPID-<tbc>

<tbc>Graph’s in-situ computation preserves locality. In Fig. 9(c,f), RAPID-Graph achieves better efficiency on clustered and real- world graphs than on random ones, benefiting from structural locality and fewer partitioning boundaries, while H100 remains largely topology-insensitive. This topology-awareness is a direct result of our partitioning algorithm, as clustered graphs like NWS produce smaller boundary sets, reducing the workload of the computationally dominant boundary-graph APSP step. RAPID-Graph provides competitive scalability without the immense hardware cost and overhead of GPU clusters. Partitioned-FW \[10\] uses 2,560 GPUs for a 1.9M-node graph but hits synchronization and memory walls. Co-ParallelFW \[11\] achieves only 45% weak-scaling efficiency on a 300K-node graph. Overall, RAPID-Graph avoids the complexity, synchronization, and energy overhead of distributed GPU clusters.

## V. CONCLUSION

We present RAPID-Graph, the first software-hardware codesigned PIM system for exact APSP. A recursive partitioner maps subgraphs into PCM arrays, enabling fully parallel FW and MP kernels in-place. The 2.5D stack connects two PCM dies, 16GB 8-Hi HBM3, and 16TB FeNAND via a 2Tb/s UCIe interposer, sustaining high on-package bandwidth within a 2kW power envelope. On real and synthetic graphs, RAPID- Graph achieves up to \(1061\times\) speedup and \(7208\times\) energy efficiency over an Intel i7-11700K CPU, and \(42.8\times/392\times\) over an NVIDIA H100 GPU. On the 2.45M-node OGBN-Products graph, it outperforms SOTA GPU clusters by \(5.8\times\) in runtime and \(1186\times\) in energy efficiency, while also showing an \(8.3\times\) speedup and \(104\times\) energy gain over prior PIM-based solutions. It maintains flat performance across a \(4\times\) degree sweep, scales linearly up to 2.45M nodes, and benefits from locality-aware partitioning on clustered and real-world topologies. RAPID-<tbc>

\begin{tabular}{ccccc}
\multirow{2}{*}{**Component**} & \multicolumn{2}{c}{**PCM-FW**} & \multicolumn{2}{c}{**PCM-MP**} \\
 & **Area (μm<sup>2</sup>)** & **Power (mW)** & **Area (μm<sup>2</sup>)** & **Power (mW)** \\
PCM Subarray & 3288 (13.80%) & 557 (80.64%) & 3288 (13.61%) & 557 (80.61%) \\
Permutation Unit & 917.3 (3.85%) & 0.586 (0.08%) & - & - \\
Min Comparator & - & - & 1268 (5.25%) & 0.684 (0.10%) \\
Controller & 5.94 (0.02%) & 0.00126 (\<0.01%) & 5.94 (0.02%) & 0.00126 (\<0.01%) \\
Others & 19610 (82.33%) & 133.29 (19.28%) & 19610 (81.12%) & 133.29 (19.29%) \\
**Total** & 23821.24 (100%) & 690.88 (100%) & 24171.94 (100%) & 690.98 (100%) \\
\end{tabular}

(a)
Performance
(b)
Energy Efficiency
x1587
x1061
x514
x7208
103
x264
x41
x453
x1399
x41
x11
x12
x75
x132
Speed-up
x7
x11
x2
x11.7
x3.4
x1
x1
x1
x1
x3.6
x1
x1
x1
x1
x1
x1
x1
x100
100
1024
32768 nodes
100
1024
32768
CPU baseline
A100 GPU baseline
H100 GPU baseline
RAPID-Graph

(a)
Performance
(b)
Energy Efficiency
101
x5.8
x1187
103
x1 x1.2
x0.7
100
x1
x18.6
x11.4
Energy Efficiency
Speedup
101
x1
100
x1
10-1
Parallel FW
Co-Partitioned APSP
PIM-APSP
RAPID-Graph


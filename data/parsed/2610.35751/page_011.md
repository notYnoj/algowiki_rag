<tbc>(CL<sub>1</sub>=CL<sub>2</sub>=1), it improves Recall@10 by 1.07%. These results support CL<sub>1</sub>=1/3 and CL<sub>2</sub>=1/2 as robust defaults.

**Tuning Guidance**. We recommend using the default parameters of ACTIVE as the first choice. They are empirical default values obtained from experiments across different datasets, different update batch sizes, different \(\alpha\) distributions, and different update patterns. For datasets or workloads that require fine-tuning, one can run experiments similar to those in Figure 22 and Figure 23 on randomly sampled dual-vector data to select more suitable parameters. Specifically, increasing \(\theta_{th}\) improves search accuracy but increases the cost of active range computation. For CL<sub>1</sub> and CL<sub>2</sub>, we recommend adjusting CL<sub>1</sub> first to obtain a better throughput- accuracy trade-off for the current workload.

## 6.8 Performance Gain

To evaluate the contribution of each core component to deletion performance, we start from RBR and progressively add the proposed components on three datasets under 0.1%, 1%, and 10% deletion batch sizes (see Figure 24), reporting normalized throughput relative<tbc>

<tbc>to RBR. Each component yields consistent speedups across batch sizes. Specifically, we first introduce the connectivity-loss-driven adaptive repair algorithm (+C.A.), which adaptively repairs affected nodes according to the degree of connectivity loss, achieving average speedups of 13.85\(\times\), 12.77\(\times\), and 11.34\(\times\) under the three batch sizes, respectively. We then further incorporate an asynchronously maintained reverse graph (+Async.), increasing the average speedups to 19.46\(\times\), 14.95\(\times\), and 12.27\(\times\), respectively, by avoiding scanning the entire graph topology. Finally, we introduce the angle-constrained AR computation algorithm (+A.C.), improving the average speedups to 25.76\(\times\), 25.50\(\times\), and 18.05\(\times\), respectively.

Notably, the asynchronously maintained reverse graph provides significant performance gains under the 0.1% batch size. Its main benefit is eliminating full graph scans, whereas the cost of in- memory access is relatively small.

## 6.9 Ablation Study

To justify the three connectivity-loss levels and the separate treatment of the first Pareto-frontier layer, we conduct experiments to validate these design choices.

0.98
0.93
0.95
0.95
0.94
0.94
0.93
0.93
0
2
4
6
8
10
0
2
4
6
8
10
0
2
4
6
8
10
0
2
4
6
8
10
Batches
Batches
Batches
Batches
Batches
(a) OI
(b) HM
(c) CM
(d) LN
(e) CW
Figure 16: Search accuracy comparison under deletions.
1.00
DEG
ACTIVE
DEG
ACTIVE
DEG
ACTIVE
0.95
0.96
0.96
0.94
0.94
0.87
0.87
0.98
0.98
0.93
0.94
0.86
0.92
DEG
ACTIVE
DEG
ACTIVE
DEG
ACTIVE
DEG
ACTIVE
0.92
0.85
0.85
0
2
4
6
8
10
0
2
4
6
8
10
0
2
4
6
8
10
0
2
4
6
8
10
Batches
Batches
Batches
(a) OI
(b) HM
(c) CM
(d) LN
(e) CW
Figure 17: Search accuracy comparison under insertions.
20
DEG + RBR
15
DEG
ACTIVE
DEG
ACTIVE
10
10
Latency (ms)
DEG + NRBR
15
DEG + NRBR
Latency (ms)
10
DEG + ACTIVE
DEG + ACTIVE
5
5
0
2
4
6
8
10
0
2
4
6
8
10
Batches
Batches
Batches
(a) Deletions
(b) Insertions
Figure 18: Search latency comparison.
DEG + RBR
DEG + NRBR
ACTIVE
1500
1000
1000
500
0
0
10
20
30
40
50
0
10
20
30
40
50
(a) Update
(b) Search
Figure 19: Update stability comparison.
DEG + RBR
DEG + NRBR
ACTIVE
8
12
12
12
P50 Lat. (ms)
P50 Lat. (ms)
6
9
9
6
6
P95 Lat. (ms)
P99 Lat. (ms)
4
4
0
0
150 Elapsed Time (s)
0
150 Elapsed Time (s)
300
0
150 Elapsed Time (s)
300
0
150 Elapsed Time (s)
300
0
150
100
100
10
10
Batch Size
Batch Size
Batch Size
(a) Deletions
(b) P99 latency
(c) P99 latency
Figure 20: Query latency under a mixed workload.
Figure 22: Sensitivity to the Pareto angle threshold θ
Figure 22: Sensitivity to the Pareto angle threshold θ
Figure 22: Sensitivity to the Pareto angle threshold θ
Figure 22: Sensitivity to the Pareto angle threshold θ
Figure 22: Sensitivity to the Pareto angle threshold θ

**Figure 16: Search accuracy comparison under deletions.**

**Figure 17: Search accuracy comparison under insertions.**

**Figure 18: Search latency comparison.**

**Figure 19: Update stability comparison.**

**Figure 20: Query latency under a mixed workload.**

**Figure 21: Varying batch size of deletions and insertions.**

**Figure 22: Sensitivity to the Pareto angle threshold** \(\theta_{th}\)**.**


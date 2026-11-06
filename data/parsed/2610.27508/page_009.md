<tbc>search parameters and report the best Pareto frontier found in the sweep.

**KatoANN configuration.** KatoANN targets the batched throughput-serving regime in which multiple users arrive concurrently. The served configuration is the calibrated one, the byte-split cascade with survivor factor _R_=2 and the batched coarse search. On sets where the calibration enables the dimension cascade, the rotated prefix runs with a survivor budget of 32. Unless otherwise stated, high-probe operating points run query batch _M_=4,096 with cache block NBLK=256. Low-probe points run _M_=10,000, the batch size also served by CABANA, with NBLK=64. We measure throughput over the real query set with no query repeated. For the systems sharing KatoANN’s inverted file, nlist is 2,048 at 1M and 8,192 at 5M-10M. ScaNN and FastScan build and sweep their own product-quantized indexes.

**Metrics.** We report recall@10, throughput in queries per second (QPS), and serving memory as steady-state RSS. Throughput is the capacity metric because the target deployment serves batches of concurrent queries. A throughput reported at a recall target is the QPS at which a system’s Pareto frontier reaches that target. We interpolate linearly between the two nearest measured frontier points and apply the same rule to KatoANN and every baseline. We never extrapolate beyond the measured frontier. If a system does not reach a recall target, we report it as capped at its highest measured recall.

## 5.2 Main Results

**KatoANN is the fastest partition-family system.** Figure 7 compares KatoANN with partition-family baselines.<tbc>

<tbc>KatoANN is the fastest in the high-recall band on all eight sets. On OpenAI-3072-1M at recall@10 \(\ge\) 0.99, the dimension cascade serves 15,635 QPS, 3.14\(\times\) CABANA and 8.45\(\times\) ScaNN. The index is identical across CABANA and KatoANN, so this gap comes from the scan; KatoANN uses a byte-split SQ16 cascade on AMX, whereas CABANA scans a lossy BF16 code. The dimension cascade contributes 1.27\(\times\) of the headline result, over the 12,267 QPS served by the plain byte-split cascade at this point.

The lossy partition baselines cap below recall 0.99 on most high-dimensional sets. This is the measured precision ceiling described in §2.1, not an under-probed curve. CABANA’s BF16 scan stops short of the band on five of the eight sets, and Faiss’s quantized FastScan path shows the same pattern. KatoANN instead reaches the band on every set and extends into the 0.999 tail. Where the baselines do reach 0.99, they trail KatoANN by a wide margin, ScaNN by 4.8-29\(\times\) and FastScan by 6.1-16\(\times\). Both reach the band only by re-ranking against a resident FP32 copy; KatoANN ranks and refines from one 16-bit code, so it pays no second-copy price.

**KatoANN matches or outperforms graph-family systems at high recall.** The matrix engine speeds the IVF scan but not the graph walk, so the comparison against graph-family systems is a crossover, not a uniform dominance claim. Figure 8 shows all eight sets. Across the high- dimensional sweep, KatoANN leads SVS-LeanVec, the best reduced-dimension graph, at recall@10 \(\ge\) 0.99 on five of the six high-dimensional sets, by 1.1-4.9\(\times\), and on all six in the 0.999 tail. Against the FP32 graphs, the margins are wider,<tbc>

KatoANN
CABANA
ScaNN
Faiss
Cohere-768-1M
OpenAI-1536-1M
OpenAI-3072-1M
Cohere-1024-5M
50
60
100
40
60
80
40
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
40
40
40
20
20
20
10
0
0
0
0
0.90
0.92
0.94
0.96
0.98
1.00
0.90
0.92
0.94
0.96
0.98
1.00
0.90
0.92
0.94
0.96
0.98
1.00
0.90
0.92
0.94
0.96
0.98
1.00
Recall@10
Recall@10
Recall@10
Recall@10
Cohere-768-10M
BioASQ-1024-10M
OpenAI-1536-5M
DEEP-96-10M
20
20
80
15
15
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
10
10
40
5
5
5
20
0
0
0
0
0.90
0.92
0.94
0.96
0.98
1.00
0.90
0.92
0.94
0.96
0.98
1.00
0.90
0.92
0.94
0.96
0.98
1.00
0.90
0.92
0.94
0.96
0.98
1.00
Recall@10
Recall@10
Recall@10
Recall@10

**Figure 7: Recall-throughput for the partition family on 8 datasets.**


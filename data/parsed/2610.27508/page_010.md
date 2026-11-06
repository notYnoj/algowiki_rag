2.1-10.7\(\times\). The one exception at recall 0.99 is the most compressible set, OpenAI-3072-1M, where LeanVec’s fixed small primary representation makes the graph cheaper through the moderate band and KatoANN leads only in the tail.

Two opposing factors set the boundary. KatoANN computes each comparison much faster, using a compute-bound matmul rather than a memory-bound gather. Graph search compares against fewer vectors, and that advantage grows with scale. The dimension cascade shifts the first factor further in KatoANN’s favor as dimension rises, moving the earlier 5-10M crossovers down so KatoANN leads across more of the band. The boundary also reflects how easily a set is walked, favoring KatoANN for spread-out embeddings and the graph family for tightly clustered ones. At low dimension, comparison count dominates, so the graph family leads except at the extreme recall tail. The disk-resident DiskANN and PipeANN trail the in-memory graphs throughout.

**KatoANN achieves low memory and high throughput.** The single-copy scan is also a memory claim, so we measure steady-state serving memory at the high-recall point. Figure 9 plots serving memory against throughput on BioASQ-1024-10M. KatoANN serves 6,831QPS at recall 0.9912 in 20.8 GB, smaller and 3.7\(\times\) faster than the reduced- dimension LeanVec graph (1,856QPS, 26.6 GB). The FP32- resident systems hold 41-46 GB. The in-band FP32 graphs run below 540QPS, while ScaNN and Faiss cap below the band. Byte-footprint baselines again match the memory but not the band; CABANA serves 402QPS at recall 0.9922, and the two-level-LVQ graph caps at recall 0.974 with 21.6 GB. Load-time peak RSS is a one-time ∼2\(\times\) transient as the FP32 input is converted and freed.

## 5.3 Deep Dive

**Where the speedup comes from.** A fast distance kernel alone does not explain the headline speedup; the pipeline around it does. Figure 10 turns on one axis at a time and measures every variant in one session. Over the unbatched per- query baseline (∼50QPS at recall 0.99), tiling, the cluster- batched primitive KatoANN inherits from CABANA [27], is the largest single step, 20.6\(\times\) at recall 0.99. Filling the tile is the precondition that lets the matrix engine run. At the final operating point, the AMX scan kernels and overlapped threshold filtering account for 99% of the measured inner- loop cycles, indicating that the pipeline keeps distance computation on the critical path rather than moving the bottleneck to scalar bookkeeping.

After tiling, byte-split precision is the dominant per- distance factor, adding 5.9\(\times\) at recall 0.99 on OpenAI-3072- 1M. The rank-then-refine cascade adds 1.53\(\times\), and the batched<tbc>

KatoANN
Vamana
HNSW
SVS-LVQ
SVS-LeanVec
PipeANN
DiskANN
Cohere-768-1M
OpenAI-1536-1M
OpenAI-3072-1M
Cohere-1024-5M
125
80
125
100
150
100
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
75
100
75
50
40
50
50
25
20
25
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
50
100
125
40
20
80
100
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
Throughput (KQPS)
75
30
15
60
75
20
10
40
50
10
5
20
25
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

8
KatoANN
6
Throughput (KQPS)
4
Better
ScaNN
SVS-LVQ
Faiss
2
SVS-LeanVec
CABANA
DADE/ADS
HNSW
Vamana
0
20
30
40
50
Serving memory (GB)

**Figure 8: Recall-throughput vs. the graph family on all eight datasets.**

**Figure 9: Memory vs. throughput at recall**\(@10\ge 0.99\) **on BioASQ-1024-10M. Systems that do not reach the band are shown at their recall ceilings.**


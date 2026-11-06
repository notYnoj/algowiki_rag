<tbc>disaggregated KV-cache management, or pipeline scheduling \[25, 39, 54\]. General LLM serving systems such as Orca, vLLM, SGLang, FlexGen, DistServe, Sarathi-Serve, Splitwise, and ZERO-Infinity improve batching, memory management, offloading, or phase disaggregation for model execution \[1, 31, 37, 40, 44, 58-60\]. They optimize the LLM side of the pipeline; ConStore optimizes the storage-side content path that feeds the prompt.

**Storage for AI workloads.** Recent AI-storage systems tailor data formats and runtime scheduling to ML workloads. ServerlessLLM introduces loading-optimized checkpoint formats, FlacIO reduces I/O amplification for ML artifacts, and CacheLib provides a production DRAM/SSD caching engine for object workloads \[4, 9, 34, 61\]. These systems share ConStore’s workload-aware philosophy, but they target model loading, container or artifact I/O, and caching rather than the co-retrieval layout of RAG content.

**Vector DB payload storage.** Classic storage systems such as LFS, LSM-trees, RocksDB, and WiscKey optimize write- optimized layout, compaction, or key-value separation for general storage workloads \[7, 33, 36, 41\]. Production vector databases adopt practical payload stores: Milvus and MANU use binlog/object-store style layouts, Qdrant replaced RocksDB with Gridstore, and Weaviate uses a custom LSM \[16, 38, 51, 53\]. These systems store payloads by insertion order, key order, or segment format; none use co-retrieval- aware layout or implement GCF-style batching.

\begin{tabular}{ccc}
Layout & DiskANN & SPANN \\
Random & 3.9 & 3.8 \\
K-Means & 15.5 & 15.4 \\
RPAG & 52.8 & 49.6 \\
\end{tabular}

Sequential
SICP
Recall 0.90
Recall 0.95
Recall 0.99
Recall 0.90
Recall 0.95
Recall 0.99
100
Latency(%)
Latency(%)
75
100
75
50
50
10
20
40
80
160
1600
10
20
40
80
160
1600
10
20
40
80
160
1600
10
20
40
80
160
1600
10
20
40
80
160
1600
Top-K
Top-K
Top-K
Top-K
Top-K
Top-K
(a) DiskANN, SIFT100M
(b) DiskANN, SIFT1B
Recall 0.90
Recall 0.95
Recall 0.99
Recall 0.90
Recall 0.95
Recall 0.99
100
Latency(%)
Latency(%)
75
100
75
100
50
50
10
20
40
80
160
1600
10
20
40
80
160
1600
10
20
40
80
160
1600
10
20
40
80
160
1600
10
20
40
80
160
1600
Top-K
Top-K
Top-K
Top-K
Top-K
(c) SPANN, SIFT100M
(d) SPANN, SIFT1B

Serial
Page-aware planner
PA + RPAG local reorder
4
2
Fetch latency
0
Random
K-Means
RPAG
Random
K-Means
RPAG
DiskANN
SPANN
SPANN
Figure 15. Content-fetch latency by layout and fetch engine
K-Means
Full rebuild /4 epochs
WASR 1% Oracle
Static RPAG
WASR 0.5%
WASR 2%
1.0
10
0.5
5
Segments query
Benefit retention
0.0
A0
A1
A2
B0
B1
B3
B4
B5
B6
B7
B8
10
20
(a) Epoch (500 queries)
(b) Bytes rewritten (%)
(a) (500 queries)

**Figure 14.** End-to-end latency of SICP relative to Sequential across top-_K_ and recall targets.

**Figure 15.** Content-fetch latency by layout and fetch engine

**Figure 16.** (a) Segments touched per two-hop query across epochs; the workload switches at epoch B0. (b) Benefit retained relative to an oracle rebuild vs. bytes rewritten.

** 2.** Cross-round segment hit rate (%).


<tbc>The second family is clustering-based, IVF-style search, represented by SPANN and extended by systems such as FusionANNS and Helmsman [6, 19, 48]. SPANN uses an in-memory head index to route a query to nearby clusters, while the vectors inside each cluster are stored as posting lists on SSD. The refinement phase reads selected posting lists progressively, often one list or a small internal batch at a time, scores their vectors, and merges them into the current result buffer. Its progress signal is therefore posting- list completion rather than graph-hop completion.

## 2.3 Motivations and Challenges

Much ANNS research focuses on small top-_K_, such as _K_=10, where content fetch can be a relatively small part of retrieval latency. Industrial workloads often need larger candidate sets: Helmsman reports search _K_ around 100-3,000 for re- ranking and advertising _K_ up to 3,000 [19]. Our profiling shows that content fetch can match or exceed vector-search latency at large _K_, challenging the assumption that search always dominates the retrieval pipeline.

Vector-search latency depends on both index size _N_ and result count _K_. At small _K_, navigation to promising regions can dominate search time. As _K_ grows, candidate expansion and scoring add work, while fetching fixed-size payloads requires proportionally more content reads. Figures 2 and 3 show this trend from small- to large-scale indexes: in the measured large-_K_ regime, both phases grow approximately linearly with _K_, making content fetch non-negligible.

**Parallel post-search fetch is not enough.** Parallel payload reads after search can reduce an isolated query’s fetch latency, but they leave the two phases still serialized with T\_search + T\_fetch. Under concurrent serving, one query’s burst of content reads competes for SSD bandwidth and queue capacity with other queries’ graph or posting-list reads. Uncontrolled parallelism can therefore inflate search latency rather than remove the bottleneck.

**Overlap content fetch with vector search.** Despite their different index structures, DiskANN and SPANN expose the same opportunity: progressive SSD I/O refines a candidate queue before the final top-_K_ is known. The key insight is that the head of this queue can stabilize early, allowing likely result payloads to be prefetched while search continues rather than waiting for it to finish.

Designing an effective prefetch mechanism is non-trivial. Prefetching too early wastes bandwidth because the candidate queue is still unstable; prefetching too late leaves too little search tail to hide content I/O. The right trigger also depends on _K_, query difficulty, and the selected ANN backend, because each changes both candidate stability and remaining search time. A useful mechanism must expose enough overlap to matter while bounding wasted reads and leaving time for final top-_K_ verification plus any residual content fetch.

**Existing content stores ignore co-retrieval.** Overlap hides latency but does not reduce the I/O imposed by content<tbc>

Search, recall 0.90
Fetch, recall 0.90
Search, recall 0.95
Fetch, recall 0.95
1M
21M
100M
1B
100
100
100
100
100
Latency (ms)
10
10
10
10
1
1
1
1
1
10
20
40
80
160
10
20
40
80
160
10
20
40
80
160
10
20
40
80
160
10
20
40
80
160
1600
1600
1600
1600
K
K
K
K

Search, recall 0.90
Fetch, recall 0.90
Search, recall 0.95
Fetch, recall 0.95
1M
21M
100M
1B
100
100
100
Latency (ms)
Latency (ms)
Latency (ms)
10
10
10
10
1
1
1
1
1
1
10
20
40
80
160
10
20
40
80
160
10
20
40
80
160
10
20
40
80
160
1600
1600
1600
1600
K
K
K

**Figure 2.** Vector search vs. content fetch latency growth with _K_ for DiskANN at fixed recall.

**Figure 3.** Vector search vs. content fetch latency growth with _K_ for SPANN.


**Conflicts.** For high-performance search, SPFresh takes fine- grained partitioning and replicated placement. However, these designs leave no memory budget for per-list buffers, and make the buffering less effective. SPFresh creates up to 16% as many partitions as vectors, so even small per-partition buffers (e.g., 8 or 16 vectors) can raise memory footprint to 2-3\(\times\). And a single new vector can trigger up to 8\(\times\) insertions, which again cause frequent SSD reads/writes even with buffered updates.

**Challenges.** Hence, we return to normal-scale partitions (e.g., 1- 2% of the dataset size) and single-copy placement, but this burdens search. In detail, it can suffer more from distribution drift, since updates are amortized across fewer partitions, each partition experiences more modifications, thus reducing the representativeness of static centroids. Without replications, more clusters need to be searched for each query simultaneously to keep accuracy. To address these, we need dynamic centroid adjustment to track updates, high concurrency and better pipelines to support search performance. Moreover, we use reclustering to replace reassignments after splits or merges, but reclustering incurs a higher computational burden and requires equal or more cores than background reassignments, making reclustering inefficient.

In this paper, we propose PrairieFire with the following key techniques:

\(\bullet\) Based on above analysis, PrairieFire organizes a three-level partition-based index and supports cascaded updates on centroids, where insertions and deletions of vectors can be buffered and propagated to upper-level centroids, thus avoiding frequent SSD round trips and preserving centroid representativeness.<tbc>

\(\bullet\) Based on the index structure, we develop fine-grained concurrency control to support high concurrency of operations, including insertions, deletions, searches and local rebuilds.<tbc>

\(\bullet\) We build the co-designed workflow on GPUs, CPUs and high- bandwidth SSDs to accelerate centroid routing, partition scanning, and computing-intensive clustering-based rebuilds.

We compare PrairieFire with state-of-the-art ANNS that support updates on large-scale workloads. Comprehensive evaluations show that PrairieFire can sustain ∼3-35\(\times\) update throughput while maintaining ∼3-5\(\times\) search throughput simultaneously. In addition, during the whole process, our search accuracy is comparable to or higher than baselines. At last, we evaluate the cost and energy efficiency of PrairieFire, showing up to 1.5-8.7\(\times\) hardware efficiency of baselines in terms of device acquisition, power consumption, and storage footprint. PrairieFire has been running reliably in RedNote’s services for two months, reducing index rebuild frequency by over 95% across the dozens of indexes it hosts and improving all business metrics (e.g., click-through rate and content impressions).

## 2 BACKGROUND

### 2.1 Freshness Challenges of Large-Scale ANNS

ANNS has become a fundamental infrastructure component [20, 21, 27] for large-scale search, recommendation, and advertising services over embedding collections that often contain billions of vectors. To reduce CapEx and OpEx at this scale, recent ANNS systems increasingly rely on SSD-based deployments [17, 23, 57, 62]. Since modern SSD arrays can provide sufficient bandwidth approaching that of DRAM [26, 37], we have deployed SSD-based<tbc>

<tbc>Helmsman [29] at scale for online services in RedNote (a.k.a. Xiaohongshu) [3]. Under strict 5-10ms search latency service level agreement (SLA), it only consumes dozens of multi-SSD servers to handle vector search services that previously required clusters equipped with tens of thousands of CPU cores and PB-level DRAM.

However, if it can only support search on static collections, using SSD-based storage [29] to offload memory pressure alone would be insufficient. In practice, vector collections are highly dynamic and require continuous updates. Changes to products, articles, and embeddings must be reflected promptly to avoid stale or invalid results [28, 55, 61]. In the search services, daily full refreshes are common to keep the index up-to-date. Moreover, recommendation systems frequently retrain and deploy embedding models at hourly or finer intervals to capture evolving user behavior [38, 42]. These model changes can modify vector representations, requiring corresponding index updates [22, 69].

### 2.2 Operations for Dynamic Workloads

To make the dynamic vector changes timely visible in these services, three operations [24, 51, 64, 67] are required:

\(\bullet\) **_Search (Top-k, Vector)_** takes a query vector as input and returns the top-_k_ approximate nearest neighbors from the current valid collection. In dynamic ANNS, search should be performed over the real-time state of the collection, reflecting preceding insertions and deletions.<tbc>

\(\bullet\) **_Insert (ID, Vector)_** inserts a new vector into the collection, where _ID_ denotes the unique identifier of the vector and _Vector_ denotes its embedding representation. After insertion, the new vector should be included to subsequent searches and potential results.<tbc>

\(\bullet\) **_Delete (ID)_** removes an existing vector from the collection according to its _ID_. After deletion, the removed vector would no longer appear in subsequent search results.

### 2.3 Existing Solutions

**Graph-based solution.** Recent works [24, 55, 67] demonstrate the capability to support updatable ANNS by online maintaining the SSD-resident graph structure [57].

Specifically, FreshDiskANN and Greator [55, 67] buffer newly inserted vectors in an in-memory graph and periodically merge them in batches into the global on-disk graph index. However, this mechanism can incur unacceptable memory overhead and suboptimal search performance during graph merging (e.g., 32- GB peak memory usage and 1.5-2\(\times\) search latency when merging 6M vectors on 60-GB index of 100M vectors). To address these limitations, OdinANN [24] adopts direct insertion, which searches neighboring nodes for each insertion, updates related edges, creates a new node, and directly flushes the changes to the NVMe SSD. By avoiding periodic merging and optimizing immediate maintenance, OdinANN provides higher and more stable performance of updates and search with lower memory usage.

**Partition-based solution.** Following the partition-based structure of SPANN [17], SPFresh [64] stores partition-level metadata in memory (e.g., centroid index, concurrency locks, and cluster sizes) and stores vector partitions as posting lists on the NVMe SSD. It supports streaming updates with a lightweight incremental rebalancing protocol, namely _LIRE_.


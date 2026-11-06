<tbc>Under continuous updates, partitions can become imbalanced. With _LIRE_, SPFresh locally splits oversized partitions, merges undersized partitions, and reassigns vectors to the nearest partitions, thereby adapting the index without full rebuilding. As inherited from SPANN, SPFresh follows search-optimized layout through aggressive fine-grained clustering (i.e., creating centroids whose number reaches around 12-16% of the total vector count) and redundantly inserts vectors into multiple clusters’ posting lists on the NVMe SSD [17, 64, 65].

## 3 MOTIVATION

### 3.1 Insufficient Performance

Since items and embedding models are continuously generated and modified to improve user experience and revenue-related metrics [38, 39], we require real-time index updates to ensure embedding freshness. To replace periodic full-index rebuilding, online updates must sustain the required refresh rate, estimated as the index cardinality divided by the full-refresh interval [29]. Representative workloads [42, 58], rebuilding a billion-vector index every 10 hours or a 100-million-vector index every hour, thus require ∼30K QPS of updates (1 insertion and 1 deletion per update).

However, **existing state-of-the-art solutions fall short of production update demands.** Even under optimistic update-only workloads with concurrent searches disabled, state-of-the-art systems OdinANN and SPFresh fall far short of this target. As shown in Figure 1a, even when dedicating all threads to updates on up to 64 CPU cores, they yield only 2-12K QPS in a single-server setup, at most 40% of the required 30K QPS.

OdinANN is bottlenecked by its insertion path. During its insertion, each new vector must first search the SSD-resident graph to identify the top-100 (i.e., the number of neighbors to be connected by new edges) nearest existing nodes, after which OdinANN acquires exclusive locks on these nodes to apply the update. These multi-hop SSD accesses from searching existing neighbors introduce most of the overhead (i.e., 4-7 ms, up to 80% of the total time), while lock contention from nodes’ updates further limits concurrency of this graph-based structure.

Partition-based SPFresh delivers better update throughput than graph-based OdinANN because it only searches an in-memory centroid index to locate several nearest clusters for insertion, which is faster (i.e., \<1 ms) than OdinANN’s on-SSD top-100 graph search. It then locks these clusters and updates their SSD pages with batched I/O. However, it still remains ∼60% below the required throughput when all threads are used for updates.

### 3.2 Does Bandwidth Scaling Work?

**Scaling SSD bandwidth fails.** To break the bandwidth bottleneck of partition-based solutions, we have deployed multiple SSDs to improve search throughput in industrial services [29], which inspires us to explore whether updates benefit similarly from this increased I/O bandwidth of modern NVMe SSD arrays [29, 30, 32, 63].

As shown in Figure 1b, results are disappointing. First, higher bandwidth provides little benefit to OdinANN, whose performance is dominated by SSD latency rather than bandwidth, due to its multi-hop graph-based access pattern [32]. Then, we might expect SPFresh to benefit more from increased I/O bandwidth, given its bandwidth-friendly batched I/O pattern and partition-based index structure [29, 64]. Unfortunately, SPFresh also improves hardly in update performance at all, far from the near-linear scaling often observed in the pure search-only workloads [29]. Even with 10 Gen5 NVMe SSDs providing almost an order of magnitude more available bandwidth (i.e., ∼120 GB/s), update throughput improves by less than 10%.

To understand the reason, we analyze the bandwidth utilization and the achievable throughput as scaling the update concurrency by increasing cores, as shown in Figure 2.

**For SPFresh updates, bandwidth is not the bottleneck, but the high CPU core consumption is.** First, we measure the actual bandwidth usage of 10 PCIe-Gen5 SSDs for SPFresh as we increase update concurrency. As shown in Figure 2a, even with 10 SSDs providing ∼120 GB/s of bandwidth, the bandwidth usage remains below 1 GB/s, indicating that the available bandwidth is not the bottleneck. Hence, we further estimate how many CPU cores for concurrent updates would be required to achieve the target.

Unfortunately, as shown in Figure 2b, though partition-based SPFresh already reduces modification-selection time (i.e., only locating the relevant clusters in memory but not searching neighbors on SSDs as OdinANN), it still requires 128-256 cores theoretically for the target throughput even without reserving CPU cores for search requests, which is far beyond the available hardware resources in real-world industrial deployments.

### 3.3 Where Does CPU Cost Come From?

To address the impractical consumption of CPU cores required for the target update throughput, we first look back at the update procedures in SPFresh, and then analyze where the CPU consumption comes from.

30
OdinANN
30
OdinANN
20
SPFresh
20
SPFresh
Target Throughput
Update
Target Throughput
10
10
0
0
4
8
12
24
48
64
1
2
4
6
8
10
CPU Cores
NVMe SSDs
(a) Increasing CPU cores with 1
(b) Increasing SSDs with 64 cores enabled.
PCIe-Gen5 NVMe SSD.

100
Utilized
Available
60
Actual SPFresh Theoretical SPFresh Target Throughput
10
40
Bandwidth Usage Ratio (%)
1
Update
20
Actual
Ideal
0.1
0.01
4
8
16
32
64
0
4
8
16
32
64
128256
CPU Cores
CPU Cores

**Figure 1: Based on SIFT100M, scaling throughput of updates (insert/delete = 1/1) with CPUs (a) and SSDs (b). However, scaling both resources fails to achieve the target 30K QPS.**

**(a) Bandwidth utilization with increasing cores.**

**(b) Cores required to achieve target throughput ideally.**

**Figure 2: Increasing CPUs under suitable thread allocations [64] (i.e., 1 thread for delete, others for insert and background as an approximate ratio of 2:1). We compare the actual bandwidth usage with the available value (a), and show theoretical cores required to achieve the target throughput (b).**


cluster under the same update rate, making fixed centroids quickly become outdated. Hence, fixed centroids can consequently become poorly representative of their evolving members, impairing routing accuracy. As shown in Figure 6a, after 100M updates, fewer centroids require scanning more clusters to maintain recall, especially when centroids remain unchanged. With a normal-scale centroid count (i.e., ∼ 2% of the vector count, with ∼50-100 members per cluster), the scan overhead increases by up to ∼ 3\(\times\).

**Pseudo buffering.** The second issue comes from SPFresh’s redundant placement. To mitigate boundary-induced recall loss, SPFresh follows SPANN, using RNG checks [60] to place each vector into up to 8 clusters. This largely defeats buffered insertion: ideally, a buffer size of _B_ should reduce the SSD-access probability to about 1_/B_ per insertion. However, as shown in Figure 5b, redundancy greatly raises this probability of triggering SSD accesses. With buffering 2 vectors for merging I/Os of each partition, replicated placements still trigger SSD access with nearly 100% probability; even with a buffer budget of 16 vectors per partition, the probability of round-trip SSD access remains around 40%.

Therefore, to make buffering updates effective, we argue that redundant placement can be removed. However, this shifts the cost to search. As shown in Figure 6b, using single-thread 8-replica search as the baseline, we compare search latency with and without replicas under increasing search concurrency. Without redundancy, search faces higher latency due to reading SSDs and computing distances for more cluster lists; when concurrent search threads reach 64 CPU cores, search latency further increases sharply due<tbc>

<tbc>to intensified hardware contention on concurrent CPU threads and memory bandwidth of DRAM [29].

**Computational burden.** The third issue comes from computing burden of reclustering-based local rebuilds. While the batched clustering avoids per-vector centroid searches and frequent updates on-SSD posting lists for all vectors affected by imbalanced partitions after splitting or merging, it introduces clustering that has heavier computing consumption than centroid search during background reassignments.

As shown in Figure 5c, using CPU cycles of relocating all vectors after merging undersized clusters (i.e., list size less than 10 [64]) as the baseline, we compare per-vector reassignment overhead after splitting/merging with local reclustering 64 nearby clusters [48, 64]. With the common 10-15 Lloyd iterations in K-Means [5, 43, 45] to local convergence, direct reclustering can amplify computations. Consequently, as shown in Figure 6c, more CPU cores (i.e., C-R) can be required for performing local reclustering in background threads, to match update throughputs under the same CPU cores of foreground threads.

## 5 PRAIRIEFIRE

### 5.1 Considerations

Addressing these conflicts and trade-offs, to make buffered update and batched rebuild practical, we have the following considerations.

First, we argue to use **an index structure with normal partitioning granularity, centroid-adaptive design, and non-redundant placement**. Normal-scale partitioning supports buffered updates without an unacceptable memory footprint. Centroid-adaptive design is for continuously tracking cluster modifications to avoid degraded centroid representativeness. Non-redundant placement eliminates the multiple insertion of the same vector into different clusters, reducing SSD access frequency and avoiding pseudo buffering.

Second, index operations call for an efficient **concurrency control mechanism** on this update-oriented index structure to proceed with minimal contention, enabling concurrent searches, updates, and index maintenance.

Third, it is practical to introduce **GPUs as extra computational resources along with efficient pipelines among various hardware** (i.e., GPUs, CPUs, and SSDs) to support heavier search overhead from our update-oriented index structure, and to enable direct clustering-based rebuilds without overwhelming CPUs.

### 5.2 Design Overview

Following these considerations, we propose PrairieFire. Figure 7 shows the design overview, including the index structure, concurrency control, and software-hardware co-design pipelines in the update-search workflow.

**Index structure** ( §5.3). First, with normal-granularity partitioning for affordable buffering, PrairieFire organizes a three-level partition-based index [5, 48] across SSDs, memory, and GPUs. From bottom to top, it consists of vector partitions as level-2, partition centroids as level-1, and routing centroids as level-0 (§5.3.1). Buffering updates and search operations are managed across these levels simultaneously (§5.3.2), then local rebuild and cascaded centroid- adaptation are applied to maintain index quality (§5.3.3).

100 15 40 Dataset Origin 75 Memory (GB) SSD Rd & Wr (% 10 20 Buffer 50 Real Ideal Norm. Overhead 25 0
0 2
4 8
16 2
4 8
16 Buffering Count Buffering Count M-R S-R C-R (a) Memory bloating. (b) Pseudo buffering. (c) Computation burden.

3 20 M/S-R 4
Const Centroids 1-Replica 8-Replicas 4
M/S-R C-R Mutable Centroids 2
Norm. Scan 2
Norm. Latency Back. Threads 10 0
0 2% 4% 8% 16% 1
4 16 64 4
8 16 32 Centroids Ratio 1
16 32 Search Cores Fore. Threads Centroids (a) Amplified scan. (b) Higher latency. (c) More cores.

**Figure 5: We show memory usage comparisons (a) and SSD I/O trigger ratios of insertion (b) across various buffer sizes. (c) shows the CPU time needed by merge reassignment (M-R), split reassignment (S-R), and direct clustering rebuilds (C-R).**

**Figure 6: (a) shows normalized cluster scanned for recall@10=90% when reducing centroids, with/without centroid modification. (b) shows search latency before/after removing replicas. (c) shows background cores of rebalancing required to match varying foreground cores of insertion with merge-split reassignment (M/S-R) or direct clustering rebuilds (C-R).**


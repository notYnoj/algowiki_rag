<tbc>After flush or local rebuild, PrairieFire applies **cascaded adjustment** to propagate refreshed centroids to upper levels. A flush summarizes multiple but bounded level-2 updates, up to the sum of buffer capacity and tombstone threshold, into one centroid update over up-to-date members. This allows upper-level centroids to reflect distribution changes in a timely manner while avoiding frequent I/Os from refreshing centroids after every foreground update. When local rebuild creates or removes vector partitions, PrairieFire inserts new centroids into, or deletes old centroids from, the nearest level-1 clusters. These changes are further propagated to the host shadow with modifications to routing centroids values and lazily synchronized to GPUs by low-latency store instructions from CPUs \[28, 71\].

All upper-level changes use the same update primitives as level- 2 buffer, as shown on the right of Figure 9b: in-place update for modifying centroids, append for inserting centroids, and swap- last-pop for deleting centroids. This keeps centroid arrays densely packed and contiguous, making them friendly to SIMD and GPU- based distance computing.

## 5.4 Concurrency Control

### 5.4.1 Decoupled locks.

To maximize concurrency, we adopt decoupled locks on the hierarchical clustering structure of PrairieFire, where all granularities (i.e., G0, G1, G2, corresponding to partition centroid cluster, vector partition, and vector) have independent control components ( 1).

Across hierarchical levels, PrairieFire binds each centroid with the lower-level cluster member set it represents as one atomic concurrency-control unit. Specifically, a level-2 vector partition and its corresponding level-1 centroid are protected together as a vector partition. Similarly, a level-1 partition centroid cluster and its corresponding level-0 routing centroid are protected together as a unit. Each cluster entry has its own lock for atomic operations.<tbc>

<tbc>To address online rebuilds at level-2, each vector partition has an additional version record for consistency validation.

In addition, as mentioned in §5.3, PrairieFire maintains a parent vector partition ID for each vector to support ID-based deletion and remapping. To protect these ID mappings, but avoid expensive per- vector locks, we use slot-based locks: each vector ID is hashed to a lock slot by ID mod the count of slots. This reduces the lock memory footprint from vector scale to slot scale (e.g., from 1B vector locks to 0.1M slot locks), while preserving concurrency.

### 5.4.2 Basic principles.

Relying on the above components, PrairieFire follows these three principles.

**1. Record-level concurrency consistency.** Designed for approximate top-_k_ results \[24, 64\], PrairieFire ensures a record-level immediate visibility \[25, 61\]. Once an _insert_ or _delete_ completes, its effect is visible to subsequent searches: inserted vectors are included for retrieval, and deleted vectors are excluded from results.

**2. Decoupling with version validation.** To avoid unnecessary blocking (e.g., intra-cluster members should not block each other just because they belong to the same parent cluster), PrairieFire locks only units used in the current stage and releases them before switching to the other granularity in the next stage. Since level-2 clusters may change between stages (e.g., some of the candidate clusters returned by level-1 search might have been rebuilt), the level-2 related stage validates recorded versions before access. On mismatch, it can fall back to the previous stage or ignore invalid items.

**3. Ordered locks.** To prevent deadlocks, operations that need multiple locks acquire them in a deterministic order: higher-level granularity before lower-level granularity (e.g., partition centroid cluster before vector partition), and units at the same granularity in ascending ID order (i.e., acquiring locks for clusters and slots after sorting by IDs).

### 5.4.3 Locking mechanisms.

PrairieFire applies locks only to objects accessed by each stage, as shown in Figure 10.

For 1 search level-0, foreground searches and insertions submit requests to level-0 workers, where each GPU has a dedicated worker. The worker lazily synchronizes dirty level-0 centroids updated under exclusive G0 per-cluster locks, and then performs batched GPU computation. Foreground threads only receive distances, then rank routing centroids (RC) to select the candidate level-1 partition centroid clusters.

\begin{tabular}{ccc}
**Granularity** & **Protected Object** & **Components** \\
**Partition Centroid** & Level-0 routing centroid & G0 Per-cluster \\
**Cluster** & Level-1 PC cluster & Lock \\
**Vector** & Level-2 vector partition & G1 Per-cluster \\
**Partition** & Parent PC ID & Lock \& Version \\
**Vector** & Parent vector partition ID & G2 Per-slot Lock \\
\end{tabular}

Foreground Threads
Level-0
Update Primitives
Search
Insert
Delete
Update in Host Shadow
Jazy sync (Store Instr.)
GPU Copies
ID:
Old
New
Vec:
Old
New
1
Search Level-0
1
Look up Map
Cascaded Adjustment
Level-1
In-place Update
V ID-PC ID
A
New C = (In-Buf Vec+ on-SSD Vec) / N Update Partition Centroid
Locate PC Cluster Insert & Delete
2
Search Level-1
2
Buffered Delete
Cascaded Adjustment
Append Insert
Buffered Insert
In-Mem:
Level-2
Search Level-2
B
Buffer Full
Tombstone Heavy
Cluster Undersized
Cluster Oversized
In-Mem:
On-SSD:
1
Case
Case
<Flush>
Swap-last-pop Delete
3
1:
2:
<Local Rebuild>
Flush & Local Rebuild Cascaded Adjustment

**(a) Foreground operation paths.**

**(b) Flush, local rebuild, and cascaded adjustment.**

**Figure 9: (a) shows foreground operations, especially buffered update (i.e., insert and delete). (b) shows flush and local rebuild at level-2, which can trigger cascaded adjustment of centroids to higher levels (i.e., level-1 and level-0) with basic update primitives.**

** 1: Concurrency-control components in PrairieFire.**


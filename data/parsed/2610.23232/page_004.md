**Procedure of updates.** In SPFresh, update threads consist of both foreground threads and background threads. As shown in Figure 3, SPFresh supports _Insert_ and _Delete_ operations in foreground threads, and performs _rebuild_ operations to maintain the index quality in background threads.

For _Insert_, 1 it first locates relevant clusters for the new vector by searching the in-memory centroid graph via node traversal. Then, it updates these clusters’ SSD lists with read-modify-write round-trip I/Os (i.e., 2 reads for loading and 3 following writes for flushing modifications). _Delete_ is lightweight because it only adds the version value of the deleted vector’s _ID_ in the in-memory version map. Hence, most of the foreground update threads are allocated for _Insert_ (e.g., ∼40 cores, two thirds of the total in update-only stress tests) and only 1 core is enough for _Delete_ of SPFresh [64].

For _rebuild_, when the size of clusters exceeds a threshold (e.g., \>128) or undersized (e.g., \<10), the rebuilds are triggered to split oversized clusters into two smaller ones or directly append small clusters into a larger one. Then, to address the possible violation of nearest partition assignments (NPA), it reassigns vectors from these rebuilt clusters. In this process, it would first read vector lists of these clusters from SSDs, then <sup>1</sup> check whether vectors need reassignment, relocate the nearest clusters for vectors potentially violating NPA, and <sup>2</sup> finally write them back to SSDs. Due to the expensive reassignments [64], the rebuilds are performed with the other one third of the total cores in the background.

**Consumption breakdown.** Based on Perf [1], we analyze the CPU cycles spent on foreground and background, as shown in Figure 4. In update-only stress tests with 4-64 threads, foreground updates account for 59-62% of the total cycles, while background rebuilds contribute the remaining 38-41%. Both paths repeatedly perform per-vector centroid searches and posting-list updates by traversing in-memory graph and reading/writing their lists on SSDs. Specifically, centroid search by graph traversal accounts for around 30-35% of cycles, while round-trip read-modify-write updates dominate the remaining cycles.

Foreground insertions trigger SSD reads and writes for every new vector. As a result, updates generate frequent SSD accesses, consuming huge CPU resources in I/O processing (e.g., submitting commands, polling for completions) and clusters updating (e.g., modifying lists and metadata). And under continuous updates, clusters can become imbalanced, triggering background rebuilds for splitting or merging clusters to maintain the index quality. Then, vectors can violate the NPA after splitting/merging imbalanced clusters, necessitating background reassignments. The per-vector reassignment of vectors further increases CPU cycle consumption in background by triggering centroid searches and rewriting on- SSD lists for the vectors affected.

## 4 OPPORTUNITIES AND CHALLENGES

### 4.1 Buffered Updates and Direct Rebuilds

Based on these observations, we identify two intuitive opportunities for improving index maintenance efficiency and saving CPU cycles to achieve higher update throughput.

**Using buffered updates to amortize frequent round-trip I/Os of per-vector read-modify-write operations in the foreground threads.** We can buffer new insertions and deletions in memory for each cluster instead of being immediately written to SSDs. Thus, by accumulating them, we can minimize every cluster’s lists read-modify-write I/Os and flush them to the corresponding SSD pages in a merged batch. As a result, foreground CPU cycles spent on read/write operations from per-vector insertions can be substantially reduced.

**Using local reclustering-based rebuilds to avoid per-vector relocation of reassignment in the background threads.** When an imbalanced cluster is split or merged, we can directly fetch its nearby clusters and recluster them to generate new centroids and posting lists. This preserves partition quality by reconstructing neighboring clusters jointly, rather than repeatedly relocating individual vectors [47, 48]. As a result, this generalized _LIRE_ can replace per-vector centroid searches and I/Os during relocations with a single centroid search for the merged/split cluster’s centroid and batched clusters refresh.

### 4.2 Conflicts and Challenges Arising

However, directly applying these ideas in SPFresh does not work well. These two intuitive methods would conflict with current search-oriented design choices and limited hardware capabilities. We discuss three conflicts (Figure 5) and their corresponding challenges (Figure 6) that prevent buffering and reclustering from being effective in practice, as follows.

**Memory bloating.** The first conflict arises from SPFresh’s fine- grained partitioning and buffering. Following SPANN, SPFresh creates up to 16% as many clusters as the total number of vectors to improve search efficiency [17]. However, maintaining per-list buffers for merging each cluster’s SSD flushes further enlarges its already high memory footprint. As shown in Figure 5a, SPFresh (i.e., Origin) already consumes about 1.5\(\times\) the raw dataset size. On the ∼13GB SIFT100M dataset, increasing the per-list buffer count from 2 to 16 adds extra 5-22 GB, and at the count of 16, the total memory consumption approaches 3\(\times\) the dataset size.

One straightforward solution is to reduce the number of clusters to a normal IVF scale [5], making memory usage more affordable. However, fewer clusters would absorb more member changes per<tbc>

Foreground:
Insert
Delete
Background: Rebuild
Host Mem
1 Locate Clusters
Split/Merge/Reassign
Traversal
Add Version
2 Locate Clusters
Traversal
NVMe SSD
Load Lists Read
Flush Lists Write
1 Load Lists Read
Flush Lists Write
Submit

Trav
Write Foreground
Read
Other
50
Percentage (%)
4
8
16
32
64
core
core
core
core
core
50
Background

**Figure 3: Update workflow in SPFresh. Main CPU overheads are from foreground insertion and background rebuilds.**

**Figure 4: Breakdown of CPU cycles. Trav: locate clusters over the centroid graph; Write: flush lists to SSDs; Read: load lists from SSDs. Other: remaining activities (e.g., lock spinning).**


**Concurrency control** ( §5.4). To support concurrent online operations including searches, inserts, deletes, and background local rebuilds, we design a granularity-decoupled locking scheme to efficiently reduce concurrency contention. It is designed to narrow the scope of locking by decoupling different levels of the hierarchical partition-based index. Then, we use the locking-validation- execution pattern to ensure consistency, while preventing upper- level locks from unnecessarily blocking operations on unrelated lower-level objects in the index.

**Software-hardware co-design** ( §5.5). We enable a heterogeneous CPU-GPU-SSD architecture through software-hardware co-design in PrairieFire. The array of NVMe SSDs provides high I/O bandwidth, while GPUs offer strong parallelism to avoid CPU computation burden during foreground search including level-0 routing centroids and level-2 vector partitions, and background clustering-based local rebuilds.

## 5.3 Index Structure

PrairieFire organizes a bottom-up three-level clustering layout across GPUs, host memory, and NVMe SSDs, supporting buffered updates and cascaded adjustments.

### 5.3.1 Three-level layout.

As shown in Figure 8, PrairieFire organizes a three-level layout, we describe each level from bottom to top in detail below.

At **Level-2**, vectors are clustered into disjoint vector partitions (VP), where each maintains its own in-memory buffer and on-SSD continuous pages (e.g., 4 pages, 16 KB, can store 128 128-byte SIFT vectors). Since clusters are independently updated and different clusters’ pages are separated and non-contiguous on SSDs, we use per-cluster buffers rather than a shared buffer [18, 55] to avoid inter-cluster concurrency contention and keep buffered vectors contiguous for cache-friendly access during search. IDs of both buffered and on-SSD vectors are kept in host memory for fast deletion (§5.3.2), but stored separately in two continuous arrays to split buffered and on-SSD data so that IDs of buffered vectors can be directly deleted and IDs of on-SSD vectors can be marked for deletion with lazy garbage collection during flushes (§5.3.3).

At **Level-1**, partition centroids (PC) of level-2 vector partitions are clustered in memory, where each level-1 entry (i.e., a partition centroid) routes a level-2 vector partition.

At the top, **Level-0** further consists of routing centroids (RC) of clusters in level-1 partition centroids. PrairieFire stores a contiguous host-side level-0 shadow with a one-to-one mapping to GPU-resident routing centroids, whose slices are distributed across GPUs for acceleration during level-0 search. Lazy synchronization first applies cascaded level-0 centroid adjustments to the host<tbc>

<tbc>shadow (§5.3.3), then propagates them to GPU memory after the current batched search kernel (§5.5.1) completes and before the next begins. Thus, each GPU kernel uses routing centroid values that may briefly lag the latest host-side adjustments with nearly no measurable impact on the recall.

### 5.3.2 Operation paths.

Based on the three-level layout described above, Figure 9a further shows the foreground operation paths, including search, insert, and delete.

**Search** first 1 searches level-0 on all flat GPU-resident slices to get candidate partition centroid clusters, and 2 searches level-1 to find several nearest candidate level-2 vector partitions. Finally, it 3 scans both buffered and on-SSD vectors of candidate level-2 VP to get the final top-_k_.

**Insert** also locates the target vector partition by searching level- 0 and level-1 (1 and 2), but only needs the nearest one for update. After locating the target VP, PrairieFire appends the new vector to its buffer and records the vector’s ID in memory, and further records the ID of the partition that receives this new vector in a hash-based map.

**Delete** first A uses the map structure to find the vector partition ID for the vector to be deleted. Then, PrairieFire conducts the deletion. If the vector is still in the buffer, it is removed by swap-last- pop (i.e., swapping it with the last entry and popping) to keep the layout contiguous. Otherwise, for an on-SSD vector, PrairieFire only marks its ID as -1, filters it during search, and performs lazy garbage collection during flushes, avoiding frequent SSD accesses on the foreground deletion path as well.

### 5.3.3 Flush, local rebuild, and cascaded adjustment.

Following the above paths, foreground insert and delete can trigger flush and rebuild operations when certain conditions are met, and cause cascaded adjustments at higher levels.

In Figure 9b, case 1 shows the level-2 **flush**. When a buffer becomes full (e.g., buffering 3 vectors reaches the budget in the figure), or its on-SSD part contains too many invalid items (e.g., 3 IDs are -1), a flush is triggered. It merges buffered vectors and the remaining valid on-SSD vectors, and writes them back to the same SSD region as continuous pages. The buffer is then cleared and the in-memory ID records are refreshed. Case 2 shows the background **local rebuild**, which is triggered when the vector partition becomes imbalanced following SPFresh [64] (i.e., it is undersized or oversized). In contrast, PrairieFire directly performs reclustering on the imbalanced vector partition and its nearby partitions, regenerating balanced partitions instead of SPFresh’s per-vector conditional reassignments.

$5.3 Index Structure
$5.4 Concurrency Control
Routing Centroids
Worker Threads
$5.3.1
GPUs Memory
Three-Level Structure
Update
Host Memory
Partition Centroids
Insert & Delete Rebuild
$5.3.2 & $5.3.3
Operations (Fore. & Back.)
Vector Partitions
NVMe SSDs
Search
$5.5 SW-HW Co-Design in Workflow
Update
Search Routing Centroids
Local Rebuild (clustering)
Search Vector Partitions
Search

GPU#0
GPU#1
Level-0 Routing Centroids (RC)
RC ID:
1357.
2468.
GPU Slices
RC Vec
GPUs
one-to-one lazy sync
Level-0 (RC)
Host Shadow
sync
12345678
RC Vec:
Level-1Partition Centroids (PC)
PC ID:
7
9
2
Host Memory
PC Vec:
Level-2 Vector Partitions (VP) All Vec ID:
26
49
78.
In-Mem Buffer
Buffered Vec:
Level-2 Vector Partitions (VP) On-SSD Vectors
Flushed Vec:
SSDs

**Figure 7: Design Overview of PrairieFire.**

**Figure 8: Three-level storage layout of PrairieFire.**


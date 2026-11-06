For **search**, PrairieFire first performs level-0 1. It then 2 acquires shared G0 locks on candidate partition centroid clusters, following _Principle 3_. Then, it scans candidate level-1 clusters to get candidate vector partitions. Following _Principle 2_, it releases G0 locks before 3 acquiring shared G1 locks on candidate vector partitions, validating their versions and scanning valid vectors for final top-_k_ results. Version mismatches are handled by skipping invalid vector partitions, which keeps stable recall as evaluations of §6 show, but without unnecessary retries.

For **insert**, it shares 1 and 2 with search to locate the nearest target level-2 vector partition to insert the new vector. It then 3 acquires an exclusive G1 lock on the target vector partition (VP), validates it, and inserts the vector into it. After that, it updates the vector-to-partition mapping under an exclusive G2 slot lock on the vector ID. If the version validation fails because of background rebuilds, it retries 1 and 2 to find the new target VP again.

For **delete**, it first A reads the parent vector partition ID under a shared G2 slot lock and immediately releases it. It then acquires B an exclusive G1 lock on the vector partition to validate whether it still contains the vector to be deleted. If true, it deletes the vector and removes the vector-to-partition mapping under an exclusive G2 slot lock. If the validation fails due to reposition from rebuilds, it retries reading the newest parent partition ID (A) and tries to delete it again.

During the background **rebuild**, if a level-2 vector partition is undersized or oversized, PrairieFire 1 performs reclustering. By 1 and 2, it locates nearby vector partitions to be reclustered together and then acquires exclusive G1 locks on nearby partitions. Valid vector partitions (VP) are then reclustered together, where their member vectors’ partition IDs are remapped under G2 locks.

Further, rebuilds and flushes trigger **cc cascaded adjustment** to keep upper-level centroids valid and representative. In ii, for updates from flushes and deletions from reclustering, PrairieFire reads the corresponding level-1 cluster under shared G1 locks and releases locks after lookups. For inserting a new centroid, it locates the target partition centroid cluster through 1. Then, in iii, it acquires exclusive G0 lock to update the partition centroid cluster, and modifies partition centroid parent (i.e., routing centroid) ID under exclusive G1 lock.

## 5.5 Software-Hardware Workflow

As shown in Figure 11a, to avoid the bandwidth bottleneck of host memory [29] and support freshness requirements, PrairieFire runs on a CPU-GPU-SSD architecture with high-bandwidth interconnects that allow direct GPU-SSD I/O with ∼50 GB/s between each GPU and 5 NVMe SSDs [9, 40, 53, 68]. This architecture provides high theoretical throughput for concurrent search and update, but also requires careful software-hardware co-design to avoid bottlenecks and underutilization. We identify three key stages that require customized optimizations: search level-0 on GPUs, search level-2 across CPUs, GPUs, and SSDs, and rebuilds on GPUs.

### 5.5.1 Batched Distance Computation for Level-0.

As shown in Figure 11b, a naive implementation launches a level-0 scan for each search or insert independently. It performs GEMV distance computation [6] followed by GPU ranking (i.e., radix-based selection [8, 70]), over all level-0 vectors; both stages are bandwidth-bound. This becomes severe at large scale: for 1B-scale SIFT [44], level-0 can contain \(10^5-2\times 10^5\) 128-dimensional FP16 vectors in experiments. GEMV alone reads 24–50 MB per request, requiring 1.4-3 TB/s of bandwidth at the target throughput (i.e., 60K aggregated from 30K search and 30K update QPS [29]). Moreover, radix-style ranking repeatedly reads and writes the distance/id array; four read-write passes (32-bit distance / 8 bits per radix pass) add 6–13 MB per request. These together can demand ∼1.8–3.8 TB/s that can exhaust the actual GPU memory bandwidth (e.g., two GPUs provide 2-2.6 TB/s in our platform as §6.1).

To address this issue, PrairieFire packs concurrent level-0 distance computing into continuous dynamic batched GPU operations [66] across all GPUs, which allows for better utilization of GPU resources and reduces memory bandwidth pressure. As shown in (B) of Figure 11b, on each GPU, a worker gathers queries from search and insert workers, forms a dense query batch, and computes query-RC (routing centroid) distances with GEMM. It then scatters each query’s distance vector back to its foreground worker, which performs GPU ranking to select candidate partition centroid clusters. Packing isolated GEMV into batched GEMM reuses routing centroid reads across queries, improves arithmetic intensity, and significantly reduces per-request bandwidth demand.

### 5.5.2 Parallelizing in-buffer and on-SSD parts during level-2 search.

In Figure 12a, each selected level-2 vector partition contains two<tbc>

Share Lock: S
Exclusive Lock:
Fallback:
Level-0 Worker:
L0
Foreground
Background
Search
Insert
Delete
Adjust Level-0 & 1
Search Level-0
(Target G0)
Look
Update RC & Level-1 Cluster
Submit L0 Dist. Req
A
Up Map
x
(G1)
L0
Update PC Parent ID
x
(Dirty G0)
Lazy sync & GPU Batch Dist.
S
(G2)
Rank Level-0 RC ID
Find
1 Locate Cascade Parent
Update & Delete:
S
(G1)
Find RC ID
2 Search Level-1
Sort Candidate ID
Insert:
S
(Candidate G0)
Scan Level-1 PC Clusters
Search Level-0
Rebuild Level-2
Insert / Delete
Search Level- 0 & 1
Sort Candidate ID
Search Level-2
3
B Level-2
Flush
(Target G1)
Sort Candidate ID
x
(Target G1)
Valid. & Update VP
LIRE
Valid. & Clustering VP
S
(Candidate G1)
Scan Level-2
(G2)
Submit
(G2)
Vector Partition
Update V Parent ID
Update V Parent ID


**Storage-cost efficiency.** Following recent work [29, 32], we evaluate storage-cost efficiency by combining the index footprint on each storage device with its unit cost. For multi-SSD SPFresh, each cluster occupies 16 KB SSD space but needs only one block-mapping entry in memory. Thus, it adds 2.5 TB SSD space while saving about 10 GB memory, making its storage cost 8-10% higher than the single-SSD version, i.e., about 2.55K$. OdinANN reserves twice the SSD space for updates, leading to over 1.3 TB SSD and 85 GB memory usage, costing about 2.9K$.

In contrast, though GPU memory is additionally introduced in PrairieFire, only centroid-cluster centroids are stored on GPUs, whose GPU memory footprint of the SIFT1B index is below 50 MB (\<$10 under  3). By reducing centroid counts, PrairieFire also reduces SSD and host-memory usage to about 0.4 TB and 50 GB, respectively. The host memory mainly includes 14 GB update buffers, 3-4 GB centroids, and others for metadata such as IDs, parent mappings, and locks structure. As a result, the storage cost of PrairieFire is ∼1.65K$. As shown in Figure 17c, this achieves 4.9-8.7\(\times\) storage-cost efficiency of baselines.

### 6.5 GPU-based comparison, high-dimensional datasets, and production evaluation

We compare PrairieFire with SVFusion [52], a state-of-the-art graph-based real-time GPU ANNS, replicating its index to maximize multi-GPU performance. We use the optimal CPU-GPU mode of SVFusion given its lack of I/O optimizations. Our system delivers approximately 2\(\times\) higher update and search throughput over _Workload A_ as shown in Figure 18a, suggesting that partition-based methods better suit concurrent update-search workloads on GPUs.

In addition to _Workloads A_ and _B_ of SIFT and SPACEV (i.e., ST-128 and SV-100), we evaluate 768-dimensional Wikipedia (i.e., WK-768) [10] and 960-dimensional Gist (i.e., GS-960) [49] against OdinANN, the state-of-the-art graph-based system, as baselines in update-search workloads. Though Figure 18b shows diminishing gain of our system as dimensionality increases due to higher search I/O than graph-based methods, PrairieFire maintains over ∼ 10\(\times\) update throughput and ∼ 1.5\(\times\) search throughput.

We further evaluate PrairieFire over multiple epochs in one of our production 128-dim recommendation workloads (Figure 18c), where each epoch corresponds to an embedding model update and a full index refresh. During the first refresh, clustering through local rebuilds improves centroid quality, yielding 3-5% recall gains. Then, recall would remain stable across subsequent epochs.

## 7 DEPLOYMENT

**Crash Recovery.** Addressing durability of crash recovery, we apply the Kafka-based write-ahead log (WAL) [2] and unique incremental ID assignment mechanism with PrairieFire in our industrial<tbc>

<tbc>deployments [25]. This reuses the existing infrastructure, avoiding a redundant WAL implementation in PrairieFire. As shown in Figure 19, during crash recovery, PrairieFire first<tbc>

<tbc>A sends the vector IDs persisted on SSDs to the event-stream servers, which compare them against the complete set of valid IDs in the WAL to identify updates (i.e., inserts and deletes) that require replay. Locally, PrairieFire reconstructs<tbc>

<tbc>1 partition centroids and then<tbc>

<tbc>2 routing centroids from the persisted vector partitions. The updates requiring replay are subsequently<tbc>

<tbc>B dispatched from Kafka to PrairieFire nodes to restore the crashed index.

**Deployment status.** Addressing both high throughput and freshness requirements, PrairieFire has been deployed in RedNote’s search, recommendation, and advertising services for two months. As an example, for one recommendation index whose embeddings are refreshed twice per hour, PrairieFire reduced full index rebuilds from 48 per day to one, handling embedding updates across all intervening epochs through streaming rebuilds. Replacing periodic rebuilds with streaming updates improved recommendation quality, with business metrics including exposure, click-through rate, and revenue yield increasing by 0.5-2 percentage points.

## 8 RELATED WORK

As real-world workloads now require ANNS systems to support billions of vectors [39, 54, 56], in-memory solutions [5, 16, 19, 46, 65] are replaced by disk-based approaches. DiskANN [57] and Starling [62] are representative examples following the graph-based pattern. PipeANN [23] further optimizes the graph-based approach by pipelining the search process. These graph-based systems have higher throughput than cluster-based SPANN [17] on a single SSD, because they consume less I/O bandwidth. However, as the array of modern SSDs becomes more powerful, cluster-based approaches can also achieve high throughput with low latency [17, 29, 30, 64], becoming popular again. At the same time, freshness requirements are also increasing [38, 42], FreshDiskANN, Greater, OdinANN, SPFresh, and SVFusion [24, 52, 55, 64, 67] are proposed to support updatable ANNS in large-scale scenarios, but their performance is limited under high update rates. Quake [48] is proposed for CPU-only index maintenance and does not support concurrent update and search. GPU-based, FPGA-based, and CXL-based ANNS [31, 32, 33, 34, 41, 50, 59, 63] are also proposed to address the limitation of CPUs, but they do not support updates.

## 9 CONCLUSION

We argue that buffered update and cluster-based index are effective for supporting updatable ANNS in large-scale scenarios. We propose PrairieFire, a CPU-GPU-SSD ANNS system that supports high-throughput updates, preserving high-throughput search. Evaluations show that it can achieve the performance requirements of high-freshness applications while maintaining high cost efficiency, energy efficiency, and storage efficiency.

SVFusion Ours
20
Update Search
0.9
40
Speedup (x)
10
0.8
k=100
k=1000
20
k=500
k=3000
Recall@
0
0
0
1
2
3
4
5
6
7
8
9
0
Update Search
SV-100
St-128
WK-768
GST-960
Epoch
(a) CPU-GPU.
(b) Dimensions.
(c) Long-term stability.

Event-stream
PRAIIREFIRE
Write Ahead Log WAL (Insert,Delete)
Non Persistent
Routing Centroids
2
Partition Buffered Centroids Vectors
Persistent
Vector Partitions
Kafka
IDs:
Vectors:

**Figure 18: CPU-GPU, high-dim and long-term comparisons.**

**Figure 19: Write-ahead log (WAL) for crash recovery.**


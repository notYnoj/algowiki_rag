## 6.2 Overall Performance

### 6.2.1 0.1B-scale evaluation.

As shown in Figure 13, we first evaluate all systems with _Workloads A_ and _B_. On both uniform (Figure 13a) and skewed (Figure 13b) datasets, PrairieFire outperforms the baselines in terms of throughputs of update (∼3-35\(\times\)) and search (∼3-5\(\times\)). And it also shows lower tail latency, comparable or better accuracy (i.e., recall@10), and the same level memory footprint.

For update, PrairieFire achieves ∼0.4 ms average latency per update, because of buffered updates with merged I/Os. Hence, only 16 foreground threads are sufficient to achieve a high update throughput. Benefiting from the optimized rebuilds (i.e., optimized GPU- based batched reclustering), PrairieFire needs only 2 background threads to match ∼40K QPS foreground updates. Greator suffers from heavy merge operations on buffered and on-SSD graphs [24], leading to the lowest update throughput. While avoiding heavy merge operations, OdinANN still suffers from the high latency and concurrency limitations of locks over the graph structure and cannot achieve high-throughput updates. SPFresh achieves higher update throughput than OdinANN, but still hits bottlenecks of frequent on-SSD read-modify-write operations and heavy reassignments, achieving only ∼10-12K QPS updates with 32 foreground threads and 16 background threads. Consequently, few threads (i.e., 16) are left for search, leading to low search throughput.

PrairieFire can allocate more threads (i.e., 46) to search, achieving much higher search concurrency. With 10 Gen5 NVMe SSDs providing more than 100 GB/s of bandwidth and GPUs handling computation, the I/O and host-memory-bandwidth bottlenecks in the search path can be overcome. As a result, PrairieFire reaches comparable recall by searching more clusters (e.g., ∼200) without

throughput loss. With normal-scale partitions (i.e., 1-2% of the dataset size), PrairieFire can buffer up to 8 vectors per cluster, while having a stable and acceptable memory usage. While OdinANN’s memory can fluctuate due to merges on deletions, SPFresh has a higher memory usage than ours due to more centroids. Since Greator has unacceptably high memory usage (i.e., _\>_ 40 GB for the 0.1B scale and _\>_ 280 GB for the 1B scale) due to buffered graph and global merge, it is omitted in figures of memory usage.

#### 6.2.2 1B-scale evaluation.

Then, we scale the experiment to 1 billion vectors with _Workload C_ (Figure 13c). Results are similar to the 0.1B-scale evaluation. Although 1B-scale index has ∼10\(\times\) centroids of centroids (i.e., level-0) on GPUs, which can incur heavier GPU bandwidth consumption than 0.1B-scale index, PrairieFire still achieves ∼3\(\times\) higher search throughput and up to ∼27\(\times\) higher update throughput than the baselines. Because we pack distance computation of level-0 search together with batched GEMM, much global memory traffic can be saved and both throughputs of updates and searches still reach 36-39K QPS. Additionally, the recall is also higher than baselines.

## 6.3 Sensitivity and Ablation Study

**Trade-off between throughput and memory.** With _Workload C_ and settings as in  2, Figure 14a shows the trade-off between throughput and memory usage with varying buffering budgets (i.e., vectors buffered and tombstones deleted per cluster). With higher memory for buffers, the update throughput can be improved by batching SSD accesses. Buffering 8 vectors can achieve a good balance between throughput and memory usage, and improvements become marginal with higher budgets (e.g., 16).

Greator OdinANN SPFresh Ours Search Throughput Search P99 Latency Accuracy 20 1.0 20 40 40 0.9 15 Throughput (KQPS) Throughput (KQPS) 0.8 10 20 Better Better 10 0.7 5
20 40 60 80 100 0.6 0
20 40 60 80 100 0
20 40 60 80 100 0
20 40 60 80 100 0
20 40 60 80 100 Update Process (%) Update Process (%) Update Process (%) Update Process (%) (a) Overall performance on Workload A (i.e., 0.1B-scale SIFT with a uniform distribution). Search Throughput Search P99 Latency Accuracy 20 1.0 20 40 40 0.9 15 Throughput (KQPS) Throughput (KQPS) 20 Better 10 0.8 Better 10 20 20 Better 10 0.7 5
20 40 60 80 100 0.6 0
20 40 60 80 100 0
20 40 60 80 100 0
20 40 60 80 100 0
20 40 60 80 100 0
20 40 60 80 100 Update Process (%) Update Process (%) Update Process (%) Update Process (%) (b) Overall performance on Workload B (i.e., 0.1B-scale SPACEV with a skewed distribution). Search Throughput Search P99 Latency Accuracy Memory Usage 40 40 1.0 0.9 Throughput (KQPS) Throughput (KQPS) 15 0.9 75 30 15 0.8 50 20 Better 20 Better 10 Better 10 0.7 Better 25 10 5
0.6 0
20 40 60 80 100 0
20 40 60 80 100 0
20 40 60 80 100 0
20 40 60 80 100 0
20 40 60 80 100 Update Process (%) Update Process (%) Update Process (%) (c) Overall performance on Workload C (i.e., scaling the comparison on the 1B-scale SIFT). Update Process (%) Update Process (%) Update Process (%) Update Process (%) (e) Overall performance on Workload C (i.e., scaling the comparison on the 1B-scale SIFT).

**Figure 13: Performance comparisons about update throughput, search throughput, tail latency, accuracy, and memory usage.**


<tbc>parts: recently updated vectors in the in-memory buffer and flushed vectors on SSDs. A naive implementation scans them sequentially, which leaves CPUs idle during on-SSD search or leaves SSDs and GPUs idle during buffer scanning. PrairieFire instead parallelizes these two parts, as shown in Figure 12a(B). The foreground worker scans the small in-memory buffer on the CPU, while the on-SSD vectors are transferred to GPU directly and scanned for distances, and then the distances are moved to CPUs. After both paths finish, their candidates are merged by distances to get the final top-_k_ on foreground CPU workers. This overlap avoids idle hardware, thereby reducing search latency.

#### 5.5.3 Fusing kernels for micro-scale clustering.

As shown in Figure 12b, local rebuilds in PrairieFire are micro-scale: each rebuild reclusters at most 64 nearby vector partitions, usually involving thousands of vectors. At this scale, standard GPU KMeans backends \[13, 14\] are inefficient. Their Lloyd iterations commonly invoke multiple GPU kernels, including GEMM-based distance computation, sorting, assignment, and reduction for new centroids, where kernel launches and intermediate global memory (i.e., G- Mem) traffic can result in a rebuild time of up to 10-30 ms, reducing GPU efficiency.

PrairieFire therefore designs a fused micro-scale clustering kernel as shown in (B) of Figure 12b. Because the centroids are small (e.g., 64\(\times\)128-dimensional FP32 vectors take only 32 KB), they can be cached in GPU shared memory (i.e., S-Mem, hundreds of KB per streaming multiprocessor). We use a design in which each GPU thread processes one vector, computes distances to all centroids, finds the nearest cluster, and immediately updates the cluster’s count and vector sum through atomic accumulation. These statistics are then used to compute centroids for the next Lloyd iteration. By fusing assignment with statistics accumulation, PrairieFire avoids materializing and regrouping assignments, reduces global-memory traffic, and removes several kernel launches from the CPU side, achieving \<5ms micro-scale clustering.

## 6 EVALUATION

We conduct evaluations for the following questions:

\(\bullet\) How does PrairieFire compare with advanced SSD-based systems by performance under standard workloads? (§6.2)<tbc>

\(\bullet\) What are the sensitive configurations of PrairieFire? And how do PrairieFire’s techniques and extra hardware contribute to its performance improvements? (§6.3)<tbc>

\(\bullet\) What is the hardware efficiency of PrairieFire in terms of device price, energy, and storage? (§6.4)<tbc>

\(\bullet\) How does PrairieFire compare with GPU-based real-time ANNS and perform under higher dimensional datasets and production workloads? (§6.5)

### 6.1 Experimental Setup

**Platform.** For evaluations of run-time performance, we use the same platform as our production services’ deployment settings, which comes with an EPYC 64-core Genoa CPU, 12-channel DDR5 memory, 10\(\times\) 2TB PCIe-Gen5 NVMe TLC SSDs, and 2 NVIDIA RTX Pro 5000 Blackwell GPUs.

**Workloads.** Following previous work \[24, 64\], we use three widely used standard dynamic workloads, unless otherwise stated.

\(\bullet\) _Workload A_ simulates the scenario, where all vectors are updated (i.e., deleted and re-inserted with new embeddings) on a 100M subset of SIFT1B \[44\]. It consists of 128-dimensional uint8 vectors and its similarity is measured using Euclidean distance. We extract two disjoint 100M vectors from SIFT1B, where one is used as the initial dataset and the other is used for updates. Each update is performed by deleting a vector from inserted vectors and inserting a new vector from the update dataset.<tbc>

\(\bullet\) _Workload B_ has the same setting as Workload A but with 100 million vectors of SPACEV1B \[7\], which consists of 100-dimensional int8 vectors. Different from the uniform distribution of SIFT, SPACEV has a skewed distribution \[64\].<tbc>

\(\bullet\) _Workload C_ scales up the experiment to 1 billion vectors, where the initial dataset is 900M vectors in SIFT1B and the update dataset is the remaining 100M vectors.

**Comparisons.** We compare PrairieFire with state-of-the-art SSD-based ANNS systems that support updates: Greator \[67\], OdinANN \[24\] and SPFresh \[64\]. The parameters are kept at optimally default values recommended, except that Greator’s and OdinANN’s graph-based beam width is set to 16 for better bandwidth utilization on multi-SSD setups \[29\]. We do not include FreshDiskANN \[55\] in comparisons, as it unacceptably incurs prohibitive memory consumption-up to 5-6\(\times\) the dataset size and has been proven to perform worse (i.e., maximally 3K QPS updates and 5K QPS searches) than others. Since SPFresh’s open-source implementation does not support multi-SSD layout, we adapt it to support multi-SSD operation using the same storage interface as PrairieFire. Specifically, each posting list is stored in one device’s contiguous pages and extended with a device identifier to route SPDK \[4\] requests across SSDs. Graph-based SVFusion \[52\] is included as the state-of-the-art GPU-CPU comparison.

**Thread allocation.** As shown in  2, we allocate threads to make the update-to-search throughput ratio ∼1:1 for each system, which is a common requirement in high-freshness applications \[29\]. Since graph-based Greator and OdinANN show limited update throughput, we set 25 threads to maximize their update throughputs first \[24\] and the remaining threads are used in search. In Greator, 25 update threads first conduct insertions and deletions then switch to merge, per 1% of the process as a batch \[67\].

\begin{tabular}{ccccc}
 & **Greator** & **OdinANN** & **SPFresh** & **Ours** \\
**Update** & 25 & 25 & FG:32 \& BG:16 & FG:16 \& BG:2 \\
**Search** & 39 & 39 & 16 & 46 \\
\end{tabular}

Search Level-2 (Search >
Clustering (Rebuild>)
Get Candidate Vector Partition
CPU
Scan Buffer
IDLE
Merge Final Top-k
Scan SSD
(A) Serial
IDLE
SSD
GPU
Get Candidate Vector Partition
CPU
Scan Buffer
Merge Final Top-k
(B) Parallel
Scan SSD
GPU


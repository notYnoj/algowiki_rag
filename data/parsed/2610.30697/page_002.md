<tbc>(QPS) as _n<sub>p</sub>_ grows from 1 to 200 of 1,024 lists (Figure 1a), while recall at 10 rises from 0.860 to 0.999. The other families of indexes respond to this cost in two ways. First, compressed lists (IVF-PQ [32], ScaNN [26], RaBitQ [18]) shrink the scanned bytes but must rerank their candidates with the full vectors to reach high recall. Second, graph indexes such as HNSW [38] and CAGRA [44] visit few vectors per query but saturate below the targets: CAGRA reaches recall 0.986 at its largest search width on DINOv2.

One observation is that the probed lists of a high-recall query hold far more vectors than its answer needs. For instance, at _n<sub>p</sub>_=200, a DINOv2 query probes about 280,000 vectors. Almost all of them lie far outside the radius of the 10th neighbor, so that the exact top 10 among them can be certified from the full distances of fewer than 200 vectors (Figure 1b). A full-precision scan nevertheless spends its memory traffic and arithmetic on the far vectors. The cost of high recall in an IVF index is therefore the cost of proving that far vectors are far.

Our insight is to certify the exclusion of far vectors inside the probed lists from low-dimensional projections, rather than reading and scoring their full vectors. While exact search by certified exclusion (CertEx) [64] proves that distant vectors cannot belong to the global nearest neighbors through hardware-certified lower bounds on short projection rows, an IVF search requires certifying non- membership within an irregular, query-dependent subset of lists. Proving exclusion inside the probed lists requires bounding the _k_-th distance local to these lists from their own anchors, which enables tensor cores to screen candidate rows at a fraction of full-precision memory traffic. Full- precision reads and exact distances are then needed only for the few survivors whose bounds can still enter the probed top _k_, breaking the linear dependence of high-recall IVF search on the number of probed vectors.

This paper turns the above insight into Lychee, a GPU IVF search with certified screening of the probed lists. Lychee takes its threshold from exact distances to anchors of the probed lists, which bound the _k_-th distance within the lists from above. A routed tensor-core pass screens all (query, list) pairs of a batch at once, grouping the queries that probe a list so that every list streams through the tensor cores once per batch. The survivors of all lists of a query<tbc>

<tbc>are then verified together in increasing order of their certified bounds, until no remaining survivor can enter the top _k_. We prove that this procedure returns exactly the _k_ nearest vectors of the probed lists, namely the answer of IVF-Flat on the same lists.

Lychee changes the cost of high recall in an IVF index from the number of probed vectors to the number of survivors of the certified screening. On DINOv2, Lychee serves 217,195 QPS at recall 0.999 (_n<sub>p</sub>_=200), 63 times the throughput of IVF-Flat and 53 times that of IVF-PQ with refinement at the same recall. The evaluation spans eleven datasets from one million to one billion vectors, ten baselines that cover the inverted-file, graph, and exhaustive families on GPUs and CPUs, and two GPU servers with five H100 GPUs in total.

In summary, this paper makes the following contributions:

• We propose a list-local certified threshold for inverted- file search, which bounds the _k_-th distance within the probed lists from the exact distances and thereby admits the certified screening of excluded vectors inside the lists.<tbc>

• We prove that certified screening followed by tie- aware ordered verification returns exactly the _k_ nearest vectors of the probed lists and derive a cost model in which the full-precision reads of a query follow its survivors rather than its probed vectors.<tbc>

• We implement Lychee on GPUs with a routed tensor- core pass that screens all (query, list) pairs of a batch at once and verifies the survivors of all probed lists of a query together.<tbc>

• We evaluate Lychee on eleven datasets from one million to one billion vectors against ten GPU and CPU baselines on two GPU servers and show that Lychee is 9.7 to 117 times faster than IVF-Flat at equal recall with 200 probed lists and up to 44.5 times faster on one billion vectors on four GPUs.

## 2 Related Work

### Partition and quantization indexes.

Inverted lists of a coarse quantizer [32, 53] are the basis of the IVF indexes in Faiss [14, 31], cuVS [42], and vector databases such as Milvus [57], Manu [27], AnalyticDB-V [61], and VBase [63]. The inverted multi-index [3], revisited inverted indices [6], and SPANN [9] improve the partition and the probe order, while product quantization [32], optimized product quantization [21], additive quantization [4], ScaNN [26], RaBitQ [18], its extended variant [19], and IVF-RaBitQ on GPUs [51] compress the scanned vectors and rerank with full vectors [30]. These methods change which vectors are probed or how many bytes an approximate distance reads, whereas Lychee keeps the probed set of IVF-Flat and certifies the exclusion of probed vectors, so that its answer equals the exact top _k_ of the probed lists.

Lychee
IVF-Flat
(a) Throughput
(b) Full-precision reads
1M
106
100k
104
Queries per second
10k
Full vectors read
102
100
101
102
100
101
102
Probed lists
Probed lists

Figure 1: Recall and throughput on DINOv2 embeddings.


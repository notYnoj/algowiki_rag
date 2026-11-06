and DADE [10], the state-of-the-art data-oblivious and data- aware pruning methods, on the same inverted file in their best configuration (Figure 13). Even when they compute only 2 to 5% of the dimensions, KatoANN’s cascade is 16- 18\(\times\) faster at recall 0.99 on one million points and about 70\(\times\) faster at ten million, where both pruning curves stop short of the band.

The reason is the per-candidate hypothesis test at every checkpoint. The test keeps a scalar control loop on the critical path, while the batched scan runs no per-candidate test and computes every active dimension in tile multiply. At high recall, the number of tests, not the per-dimension multiply-adds, dominates. Pruning runs faster on a graph host, the setting used by the pruning papers, so we also pair both methods with HNSW. The graph raises their rate by about 3.6\(\times\), but still leaves them 5 to 10\(\times\) behind KatoANN. At ten million, the pruning becomes net-negative because an unpruned HNSW is faster at matched recall. Both pruning baselines also keep the full FP32 copy resident.

**Thread scaling.** Figure 14 sweeps _T_ from 1 to 32 at each system’s recall-0.99 configuration. Each system runs at one fixed operating configuration, so the 32-thread point sits slightly below the batch-grid Pareto headline. On OpenAI- 3072-1M, KatoANN scales about 13\(\times\) over 32 threads, from 1,186 to 15,400 QPS, enabled by lock-free per-thread heaps and scan-stage locality. CABANA runs on the identical inverted file and scales 11.5\(\times\), from 423 to 4,860 QPS, so KatoANN’s lead widens from 2.8\(\times\) at one core to 3.2\(\times\) at 32. ScaNN climbs from 84 to 1,927 QPS and Faiss-FastScan from 123 to 1,214 QPS, leaving KatoANN ahead by 8.0\(\times\) over ScaNN and 12.7\(\times\) over Faiss at 32 cores. The same trend holds at ten million on BioASQ-1024. For example, KatoANN scales 17\(\times\), from 370 to 6,288 QPS at recall 0.99.

## 6 RELATED WORK

**Matrix-engine and accelerated search.** CABANA [27] is the closest system to KatoANN. It batches IVF cluster scans onto Intel AMX with cluster-aware query grouping. However, it scans lossy BF16 codes, so its recall caps below the

high-recall band. KatoANN instead ranks and refines from a single resident SQ16 code, so no recall ceiling appears in our measured range. ScaNN [18] and Faiss FastScan [2, 11] accelerate the partition scan with AVX-512 SIMD units, which compute distances for one query at a time. GPU-based ANN search systems [21, 26, 34] move the scan to a separate, expensive device. KatoANN instead targets the matrix engine already present in the CPU.

**Quantization, refinement, and distance pruning.** Most systems reduce scan cost with compressed codes, including product quantization [20], anisotropic quantization [18], LVQ and LeanVec [1, 39], and bit-level RaBitQ [12, 14]. High- recall operation then usually adds a re-ranking stage against a second, more precise representation. SVS-LVQ is the closest in mechanism, since it also refines from a compact code, but it does so along a graph walk that a matrix engine cannot accelerate. ADSampling [13], DADE [10], and TRIM [37] instead stop distance computations early, a per-candidate control flow that does not map to dense tiles. KatoANN differs by drawing both the cheap ranking key and the full refinement from one SQ16 byte-split code, so it needs no second copy and no early-stopping shortcut.

**Graph, storage, and database systems.** Graph indexes [17, 31, 38] reduce the number of comparisons by walking a proximity graph, which is complementary to KatoANN’s cheaper comparisons. Out-of-core and near-storage systems [8, 25, 40, 41, 44, 46], filtered search [5, 16, 23, 30, 35, 36, 43], adaptive partitioning [32], vector databases [24, 42, 47], and RAG pipelines [3, 6, 7, 15, 22, 45] optimize placement, query semantics, or application pipelines, all orthogonal to per-distance compute. KatoANN can serve as the high- throughput distance engine inside such systems.

## 7 CONCLUSION

We presented KatoANN, an AMX-accelerated ANN search system that simultaneously achieves high throughput, high recall, and a small memory footprint. KatoANN stores each vector only once as an SQ16 code, ranks candidates using a low-cost high-byte key, and adaptively refines only the survivors with the full byte-split SQ16 distance on Intel AMX. Our evaluation shows that KatoANN is the fastest partition- family system among those tested across the high-recall range. More broadly, this work establishes CPU matrix engines as a promising foundation for ANN serving. They support high-throughput, high-recall vector search beyond the AVX-512 SIMD designs that existing systems use.

KatoANN ScaNN KatoANN ScaNN CABANA CABANA Faiss 15 6
10 4
Throughput (KQPS) Throughput (KQPS) 5
2 0
0 1
8 Threads 16 Threads 24 32 1
8 Threads 16 24 32 (a) OpenAI-3072-1M (b) BioASQ-1024-10M

**Figure 14: Thread scaling.**


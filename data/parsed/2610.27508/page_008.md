## 4 IMPLEMENTATION

KatoANN is implemented in about 9KLoC of C++17 and 2KLoC of x86 intrinsics. A small dispatch layer selects the datatype, metric, and scan mode at runtime. The code builds with GCC 13 and oneAPI 2024, requires no kernel patches, and enables AMX tile state once at startup through the standard ARCH\_REQ\_XCOMP\_PERMarch\_prctl request.

**Kernels.** The AMX scan kernels are written directly with tile intrinsics. The BF16 path uses \_tile\_dpbf16ps. The SQ16 byte-split path uses \_tile\_dpbuud for unsigned INT8 partial products and \_tile\_loadd for VNNI-order tile loads. The full byte-split scan, cascade, batched coarse search, and dimension cascade share the same kernel templates, differing only in the byte planes and dimensions fed to the tile multiply. A one-time calibration selects the scan mode and parameters per built index; serving performs no per-query mode search.

**Runtime.** For each query batch, KatoANN rebuilds the cluster-to-query map in place in \(O(M\cdot\) nprobe) using an indexed bucket array. Worker threads take clusters round- robin and keep heaps and scratch buffers private, so the scan path requires no inter-thread synchronization. Top-_K_ filtering runs on AVX-512 with \_mm512\_cmp\_ps\_mask, skipping empty 32-candidate blocks and pushing only surviving lanes into the heap.

**Storage and build.** Each cluster is stored as a VNNI-order tensor whose innermost stripe matches the AMX B-tile. The same layout is used for database lists and centroids. Index construction is a streaming pass over the input vectors; the builder assigns clusters and emits SQ16 codes, high- byte norms, centroid codes, and packed tensors inline. The packed tensors can be memory-mapped; in the evaluated in-memory regime, the active shard remains resident after warm-up.

## 5 EVALUATION

### 5.1 Methodology

**Testbed.** All experiments run on a 2-socket Intel Xeon Silver 4514Y server (Emerald Rapids, 32 physical cores / 64 logical cores) with 256 GB DDR5 and NVMe storage. The host runs Ubuntu 24.04 with kernel 6.14. Every system runs with _T_=32 pinned threads, the performance governor, memory interleaved across both sockets, and a 10K-query warm-up. We measure KatoANN and each baseline interleaved within one session and report the median of three repetitions, with a per-point coefficient of variation below 2%.

**Datasets.**  2 lists the 8 datasets used in evaluation. DEEP-96 [4] is a typical low-dimensional benchmark dataset.

The other datasets contain 768- to 3072-dimensional embeddings and scale up to 10M vectors. Cohere-768 and OpenAI- 1536-5M come from the VectorDBBench suite [48]; the former embeds 2022-12 English Wikipedia passages with Cohere’s multilingual model, and the latter embeds the C4 corpus with a 1536-dimensional OpenAI model. BioASQ- 1024 is VectorDBBench’s 1024-dimensional embedding of the BioASQ biomedical corpus. Cohere-1024 embeds the 2023-11 Wikipedia dump with Cohere embed-multilingual- v3. OpenAI-1536-1M and OpenAI-3072-1M embed DBpedia entity abstracts with OpenAI text-embedding-ada-002 and text-embedding-3-large, respectively. The high-dimensional sets are FP32 under cosine similarity and are served as _L_<sub>2</sub> search on normalized vectors. For every dataset, we compute the exact top-10 neighbors by exhaustive FP32 search under the same metric used for serving. For cosine datasets, both database and query vectors are normalized before ground-truth construction, so the _L_<sub>2</sub> ranking preserves the cosine ranking.

**Compared systems.** We compare against both partition- family and graph-family systems. The partition family comprises CABANA, ScaNN, and Faiss FastScan. CABANA [27] is the prior AMX-based ANN system. We faithfully reimplement its published design, which batches queries onto MKL’s BF16 GEMM through hash-grouped cluster-to-query inversion. We validate the reimplementation by matching the reported grouping-overhead share and by confirming that its speedup over an AVX-512 FP32 baseline lands within the published range on CABANA’s own low- dimensional datasets. ScaNN [18] is the AVX-512 partition baseline, swept over its leaves-and-reorder grid. Faiss [11] runs FastScan with IVF , PQx4fs and FP32 refine.

The graph family spans FP32 Vamana [38] (_R_=128) and HNSW [31] with raw vectors resident, the quantized-code graph SVS [1] (Vamana, degree 64, window 200) with one- and two-level LVQ codes and the reduced-dimension Lean- Vec configuration [39], and the disk-resident DiskANN and PipeANN [17] for completeness. We additionally compare the dimension-pruning methods ADSampling [13] and DADE [10], both on the same inverted file and paired with an HNSW host. For every system, we sweep its exposed<tbc>

\begin{tabular}{ccccc}
**Name** & **#Vectors** & **Type** & **Dim** & **#Queries** \\
DEEP-96 & 10M & FP32 & 96 & 10,000 \\
Cohere-768 & 1M /10M & FP32 & 768 & 1,000 \\
Cohere-1024 & 5M & FP32 & 1024 & 10,000 \\
BioASQ-1024 & 10M & FP32 & 1024 & 3,106 \\
OpenAI-1536 & 1M / 5M & FP32 & 1536 & 10,000 / 1,000 \\
OpenAI-3072 & 1M & FP32 & 3072 & 10,000 \\
\end{tabular}

** 2: Datasets used in evaluation.**


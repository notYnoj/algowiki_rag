# KatoANN: Enabling Near-Exact Vector Search at the Speed of Lossy Scans with CPU Matrix Engines

### ABSTRACT

Distance scans in partition-family approximate nearest- neighbor (ANN) search are typically limited by memory bandwidth. Existing systems therefore improve throughput by reading fewer bytes per candidate, often at the cost of recall. We present KatoANN, a CPU ANN search system that removes this tradeoff by batching distance scans on Intel AMX, a CPU matrix engine. Batching allows multiple queries to reuse each fetched vector code, shifting the scan from memory-bound to compute-bound and enabling near-exact distances at the speed of a lossy scan. KatoANN stores each vector once as a 16-bit SQ16 code split into high- and low-byte planes. Its adaptive rank-then-refine scan first ranks all candidates using only the high byte, then refines a small survivor set using the full-byte code. Both stages use the same representation, avoiding a second copy of the raw vectors. Experiments across diverse high-dimensional workloads show that KatoANN is the fastest partition-family ANN search system in our evaluation throughout the high- recall range.

### 1 INTRODUCTION

Modern AI applications, including retrieval-augmented generation (RAG) [28, 29] and recommendation systems [9, 33], answer queries by retrieving nearby embedding vectors with hundreds to thousands of dimensions. At scale, they rely on approximate nearest-neighbor (ANN) search because exact _K_-nearest-neighbor (KNN) search requires an exhaustive scan of the entire dataset. An effective ANN system must therefore provide high throughput while maintaining recall close to 1, such as 0.99, because any neighbor missed by the search is unavailable to the application.

Partition-based search [8, 11, 18, 42], one of the two dominant ANN index families alongside graph-based search [17, 38], spends most of its query time scanning the vectors in the selected partitions. This distance scan is typically _memory-bandwidth-bound_, so its throughput is largely determined by the number of bytes read per candidate. Partition- based ANN systems consequently face a tradeoff between throughput and recall through their choice of vector code, the quantized representation used during the scan. High- precision codes preserve recall but increase memory traffic,<tbc>

<tbc>whereas low-precision codes reduce memory traffic and improve throughput but may impose a recall ceiling.

High-recall configurations in systems such as ScaNN [18] and Faiss [11] attempt to balance this tradeoff through a two- pass design. They first scan compact codes using AVX-512 SIMD instructions, then re-rank a survivor set using full- precision vectors. Although re-ranking improves recall, it requires an additional pass over memory and requires storing the raw vectors alongside the compact codes, reducing throughput and increasing memory usage. This leads us to ask: _Can a partition-based ANN search system achieve high throughput and high recall simultaneously without storing a second vector representation?_

We answer this question affirmatively with KatoANN, a new ANN search system that computes near-exact distances at the speed of a lossy scan while storing each vector only once. The core idea is to batch distance scans on Intel AMX [19], an emerging CPU matrix engine, as illustrated in Figure 1. A distance scan is memory-bandwidth-bound only when each fetched vector serves a small number of queries. CABANA [27], a recent AMX-based ANN system, batches the queries that probe the same cluster, turning the per- query fine scan into matrix multiplication on AMX so that each loaded vector block serves many queries at once. Our key observation is that this batched execution does more than accelerate the scan. With enough cross-query reuse<tbc>

Low QPS High mem. footprint Low recall High QPS Low mem. footprint CPU (AVX) Query CPU (AMX) Query CPU (AMX) Query 1 Scan PQ (lossy) 2 Re-rank with FP32 (exact) AMX tile 1 Scan BF16 (lossy) AMX tile 1 Scan high bytes of SQ16 AVX-512 SIMD 2 Refine survivors to full 16-bit (near exact) 2 copies! Memory Memory Memory PQ FP32 (32-bit) BF16 (16-bit) SQ (16-bit) Drop! High (8-bit) Exp Mantissa Exp Mantissa Low (8-bit) (a) ScaNN/Faiss (IVF+PQ) (b) CABANA (BF16 cast) (c) KatoANN (Byte-split)

Soobin Cho and Gyuyeong Kim <br>
Yonsei University <br>
gyuyeong.kim@yonsei.ac.kr

arXiv:2610.27508v1 [cs.DB] 20 Oct 2026

**Figure 1: KatoANN provides high throughput and high recall with a small memory footprint by running a batched, adaptive rank-then-refine scan on Intel AMX, an emerging CPU matrix engine.**


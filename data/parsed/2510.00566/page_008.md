<tbc>have occurred, so a Direct template variant replaces the indirect gather over active\_indices with a unit-stride load. Second, performing repeated small dot product calls (i.e., fewer than 32-64 dims at a time) is wasteful, as the compiler does not know the level width at compile-time and cannot fully unroll the loop. In addition, the query slice has to be wastefully reloaded into a register for each point. We thus specialize our distance kernel for level widths that are multiples of 8 up to 128 (Fixedwidths) to enable fully unrolling the reduction and keep the query slice in registers across the batch. The FixedWidth variant alone accounts for the gap between **A3** and **A4** in Figure 9.

_IVFFlat: Update_ reads the dot-product buffer, the per-candidate cumulative tail-energy entries, and the current heap threshold, and emits a byte mask of survivors. Specifically for level 1, we again bypass reading from our list of active indices. Removing this dependency and disaggregating this step from the dot-product computation allows the kernel to autovectorize.

_IVFFlat: Consolidate_ turns the survivor mask into the active- indices array for the next level, eight entries at a time using BMI2 \_pext\_u64 and AVX2 \_mm256\_permutevar8x32\_epi32. We deliberately compact into a dense array of active indices rather than maintaining a byte mask through the pipeline, as iterating over a mask would require scanning all _B_ slots at each level, regardless of how many candidates have been pruned. By consolidating, the subsequent Phase 1 kernels only iterate over the surviving subset.

## 6.2 IndexIVFPQPanorama

IVFPQ [25] splits each vector into _M_ subvectors and quantizes each against a 2_<sup>n</sup>_bits-entry codebook, replacing the per-candidate float dot product with a sum of _M_ look-up-table (LUT) lookups over 1- byte codes. We preserve the three-phase workflow of Section 6.1, but revamp Phases 1 and 3 for PQ codes.

_Sub-quantizer-major layout._ A direct import of the IVFFlat level- major layout would store _M/L_ contiguous bytes per candidate per level. Since _M/L_ bytes is typically much smaller than modern SIMD vector widths, wide register loads would suffer from lane underutilization. We thus transpose the data _within_ a level, storing the _m_- th sub-quantizer’s code contiguously across a batch of _B_ candidates. A single 64-byte SIMD load thus fetches the same sub-quantizer’s code for 64 candidates in parallel. Figure 4 shows a toy example with _M=_480 subvectors, _L=_16 levels, _B=_4 candidates.

This transposition also benefits temporal locality. In standard IVFPQ, evaluating a single vector requires reading from every sub- quantizer’s slice of the LUT. As the full LUT can easily exceed 128 KB, this vector-by-vector access pattern heavily thrashes the L1 cache. By processing the same sub-quantizer across 64 candidates simultaneously, our layout keeps a tiny 256-entry LUT slice pinned in the L1 cache for the entire batch, reducing cache thrashing. In effect, even if we disable Panorama’s pruning, the transposed layout alone outperforms Faiss’s heavily-optimized IVFPQ baseline<tbc>

<tbc>by up to 2\(\times\) (Figure 13). This approach applies the transposed data layouts of BitWeaving and ByteSlice [15, 30] to PQ.

_IVFPQ: Compute_ collects per-level distances for each batch at level \(\ell\) by a single process\_level kernel. We use i32gather to index one sub-quantizer’s LUT slice for 16 candidates in parallel; combined with the sub-quantizer-major layout, it unlocks SIMD- rate distance updates over packed PQ codes.

_IVFPQ: Update_ reuses the IVFFlat survivor-mask kernel verbatim; PQ codes never enter the prune loop.

_IVFPQ: Consolidate_ packs survivors’ codes into a dense buffer 64 candidates at a time, avoiding both the SIMD lane underutilization of processing pruned slots and the scattered byte reads that would break the contiguous layout. Two fast paths bracket this step: when no candidate is pruned we alias the original code pointer and skip consolidation entirely, and once fewer than _B/_<sup>16</sup> candidates remain we drop vectorization and traverse the active-index array directly in the compute phase.

## 6.3 IndexHNSWFlatPanorama

HNSW [37] traverses its graph greedily, iteratively popping the closest frontier vertex from a candidate heap to compute its neighbors’ exact distances. Neighbors closer than the _k_<sup>th</sup> best distance enter a global result heap and the candidate heap. Filtering and refinement are thus interleaved, yielding scattered, memory-bound accesses governed by the graph topology.

Because Panorama’s level-wise evaluation exacerbates HNSW’s memory-bound, scattered accesses, we introduce three structural adaptations to hide cache latencies and preserve traversal stability. First, _K-pop block evaluation_: we relax strict greedy routing by popping multiple vertices simultaneously from the candidate heap, processing their combined unvisited neighbors in dense SIMD blocks of 64. Second, _coefficient inlining_: we embed the precomputed residual energies directly into a small prefix header of each database vector, reducing cache misses by one per candidate. Third, _partial distance routing_: candidates pruned at level \(\ell\) are not discarded, but pushed back into the candidate heap keyed by a partial distance estimate--calculated as the midpoint of the lower and upper bounds ((LB + UB)/2). This estimate acts as a proxy to seed further exploration without requiring full distance evaluations.

## 6.4 IndexRefinePanorama

An increasingly popular ANNS pipeline uses PQ for a fast first pass (Faiss FastScan [12, 45]) and then _refines_ the top-\(k'\) candidates with exact distances on a flat float index. Panorama also plugs into this refine step: IndexRefinePanorama forwards the base index’s top-\(k'\) labels to an inner IndexFlatPanorama that stores vectors in row-major order and runs Panorama with _B_=1--refinement targets a scattered ID list, so the level-major batched layout of Section 6.1 is inapplicable. As with HNSW, we process candidates in groups of 64: a one-pass sweep over the block’s IDs absorbs random-access latency; then the per-level dot-product kernel runs across the block with the query slice pinned in registers.

c1 c1 c1 c1 c31 c31 c31 c31 c451 c451 c451 c451 c2 c2 c2 c2 c32 c32 c32 c32 c452 c452 c452 c452 c453 c3 c3 c3 c3 c3 c33 c33 c33 [...] c453 c453 c453 c453 [...] [...] c30 c30 c30 c30 c30 c60 c60 c60 c60 c480 c480 c480 c480 Level 1 Level 2 Level 16

**Figure 4: Batch 1 storage for IVFPQ on GIST.**


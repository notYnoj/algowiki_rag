<tbc>on GIST, 1.19–1.52× on Ada, and 1.13–1.32× on arXiv. This result means that Panorama can be applied to any reranking-based ANNS pipeline, regardless of the underlying indexing method.

## 7.4 Transform contribution

Figure 8 isolates the contribution of the orthogonal transform. On contiguous indexes, raw-vector Panorama already accelerates search via systems-optimized pruning, but the PCA-shaped basis consistently amplifies these gains by tightening the Cauchy– Schwarz bound (Proposition 5.1). On GIST (\(R\ge 0.95\)), PCA alone scales Panorama’s QPS by 12.3× on IVFFlat and 7.3× on IVFPQ over the raw baseline. Conversely, on non-contiguous structures like HNSW and FastScan-Refine, Panorama depends entirely on the transform: raw Panorama-HNSW drops to 0.80×, whereas adding PCA yields a 2.83× speedup. Because pointer-based graph traversals suffer a cache miss on nearly every candidate look-up, runtime is heavily dominated by memory latency rather than distance arithmetic. By Amdahl’s Law [2], optimizing compute under such memory-bound conditions yields negligible returns, meaning raw pruning’s minor arithmetic savings cannot offset its overhead.

## 7.5 Systems contribution

Figure 9 isolates the performance gains of our four design choices (**A1-A4**, Section 6.1) against the Faiss-IVFFlat baseline. To decouple system performance from algorithmic pruning, all variants are<tbc>

<tbc>evaluated under exhaustive search with Panorama transforms enabled. **A1** denotes the unbatched, point-centric baseline. This baseline delivers consistent speedups over the original Faiss implementation, peaking with a 5.37× on Large. The only slowdown is a 0.78× on Deep. In the absence of our systems optimizations, Panorama does not perform optimally on low-dimensional datasets.

**_A2_**. Transitioning from point-wise processing to a batch size of 1024 yields the largest single performance leap across all benchmarks, ranging from 2.78× on Deep to 5.03× on GIST. This acceleration stems from two architectural advantages: (1) batched execution enables temporal query reuse across all candidates in a batch, and (2) our restructured storage layout completely eliminates high-stride memory accesses.

**_A3-A4_**. Decoupling the compute kernels from the pruning kernels and templating the level-1 distance kernel (Direct access) adds 1.15–1.50× across all datasets, while specialized fixed-width distance kernels contribute a further 1.01–1.13×–most prominent on lower-dimensional data (1.13× on Deep), where dispatching the correct kernel matters more relative to per-candidate prune work.

## 7.6 Knobs and optimizations

Figure 10 isolates the behavior of our two pruning knobs under exhaustive search.

**_Spectrum Flattening (_**\(\kappa\) _**for Panorama-IVFPQ)**_**. Increasing \(\kappa\) scales back the aggressive flattening of the post-PCA spectrum (Figure 2). This yields a highly favorable tradeoff, delivering a 4.5× QPS gain at high recall (\(R\ge 0.96\)) against a marginal ∼1% recall penalty across the \(\kappa\in[1,L]\) sweep. Both performance and accuracy curves reliably saturate near our canonical choice of \(\kappa^\star\)=4 on Ada. Because \(\kappa\) is a build-time parameter, tuning it requires a full index reconstruction. Thus, we recommend practitioners sweep \(\kappa\) on a downsampled, representative dataset to locate this saturation point prior to a full-scale build.

**_Pruning Relaxation (_**\(\varepsilon\) _**on Panorama-IVFFlat)**_**. Relaxing \(\varepsilon\) from 1.0 toward 0.0 smoothly trades accuracy for throughput. On GIST, evaluating at \(\varepsilon\)=0.8 yields a 1.26× speedup over the strict baseline (\(\varepsilon\)=1) at 99.29% recall, whereas \(\varepsilon\)=0.5 advances the speedup by another 1.58× while maintaining 99.21% recall. Empirical throughput closely tracks the theoretical \(1/(1+ln\varepsilon)\) scaling predicted by Proposition 5.3. In contrast to \(\kappa\), \(\varepsilon\) is a runtime search parameter.

FAISS
Panorama-RAW
Panorama-PCA
IVFFlat
IVFPQ
103
103
102
102
101
101
0.8
0.9
1.0
0.8
0.9
1.0
HNSW
FastScan-Refine
104
103
103
102
0.8
0.9
1.0
0.8
0.9
1.0
Recall
Recall


\(\bullet\) **Systems co-design and integration.** We co-design Panorama with the memory hierarchy, providing a _batched_ variant for contiguous layouts, using SIMD bulk-pruning kernels over a level-major data layout, and a _no-batch_ (point-centric) variant for non-contiguous layouts. Panorama is available in Faiss across HNSW, IVFPQ, IVFFlat, and a PQ-refine step (FastScan-Refine), delivering up to 28.9\(\times\) end-to-end speedups.

## 2 RELATED WORK

Approximate Nearest-Neighbor Search (ANNS) pipelines generally operate in two phases: a filtering phase that retrieves a candidate set, and a refinement phase that computes exact distances to find the true top-_k_ neighbors. Historically, the literature has heavily optimized the filtering phase. _Graph-based methods_ \[36, 37, 43\], _tree- based partitions_ \[7, 40\], and _Locality-Sensitive Hashing_ (LSH) \[23, 35\] all employ distinct spatial navigation strategies to reduce the candidate pool. However, as embedding dimensionalities grow, the exact distance evaluations required at the leaves, neighborhoods, or hash buckets of these structures become the dominant computational bottleneck. Panorama is designed to operate atop any of these filtering structures to accelerate this final distance computation.

_Clustering-and-quantization methods_ partition space and compress vectors to reduce storage and accelerate search. IVF \[24\] builds inverted indexes via _k_-means clustering to map queries to nearby centroids. IVFPQ \[25\] applies _product quantization_ (PQ) within clusters, decomposing vectors into independently quantized subvectors. Advanced variants further minimize quantization error via learned rotations (OPQ \[19\]), multi-cluster assignments (Multi-D-ADC \[6\]), anisotropic quantization (SeaNN \[20\]), or by introducing theoretical error bounds for extreme quantization (RaBitQ \[17\]).

While these methods excel at compression, scanning encoded vectors remains a computational bottleneck, as traditional implementations require exhaustive distance calculations across all subvectors. Recent approaches address this limitation by optimizing both storage and scanning. Variance-Aware Quantization (VAQ) \[42\], for instance, abandons PQ’s uniform bit-budget to adapt dictionary sizes proportionally to each subspace’s explained variance. Crucially, VAQ bypasses exhaustive scanning by employing triangle inequality bounds and early-abandoning heuristics to mathematically prune candidates on the fly. While VAQ addresses variance skew by heavily modifying the underlying quantizer, Panorama does the exact opposite: we introduce an orthogonal spectrum-shaping transformation that flattens the data’s variance. This ensures strict compatibility with highly-optimized, uniform PQ implementations while preserving enough front-loaded energy to power accretive early-abandoning.

Beyond quantization, dedicated _refinement techniques_ attempt to accelerate the final distance computations directly. Probabilistic methods such as ADSampling \[16\], PDX \[28\], and FINGER \[11\] rely on stochastic sub-sampling or proxy metrics, which intrinsically degrade maximum recall. Conversely, exact refinement methods, including BOND \[13\] and Stepwise \[26\], establish strict distance bounds to prevent false dismissals but suffer from loose bounds. By forgoing probabilistic estimation in favor of mathematically rigorous Cauchy-Schwarz bounds along a shaped PCA basis, Panorama<tbc>

<tbc>generates tight pruning bounds, allowing it to exceed the throughput of probabilistic methods across all recall bands.

Finally, some works refer to refinement over \(k'=k_\text{factor}\cdot k\) over-fetched candidates as ‘_reranking_’ (e.g., using coarse indices like IVFPQFastScan \[4\] for rapid initial retrieval followed by unquantized _k_NN). Because Panorama accelerates the underlying mathematical operations of distance computation, it serves as a drop-in replacement to accelerate this exact reranking stage as well.

## 3 PANORAMA: DISTANCE COMPUTATION

Problem 1 (_k_NN refinement). _Given a query vector_ \(\mathbf{q}\in\mathbb{R}^d\) _and a candidate set_ \(\Gamma=\{\mathbf{x}_1,\dots,\mathbf{x}_N\}\)_, find the set_ \(\mathcal{S}\subseteq\Gamma\) _such that_ |S|=_k and_ \(\forall\mathbf{s}\in\mathcal{S},\mathbf{x}\in\Gamma\backslash\mathcal{S}:\|\mathbf{q}-\mathbf{s}\|_2\le\|\mathbf{q}-\mathbf{x}\|_2\).

Problem 2 (ANN index). _An_ approximate nearest neighbor _index is a function_ \(\mathcal{I}:\mathbb{R}^d\times\mathbb{D}\rightarrow 2^{|\mathbb{D}|}\) _that maps a query_ **q** _and a database_ D _to a candidate set_ \(\Gamma=\mathcal{I}(\mathbf{q},\mathbb{D})\)_, where_ \(\Gamma\) _contains the true k-nearest neighbors with high probability._<sup>1</sup>

Problem 1 is the computational bottleneck: with _N_ candidates, naive refinement computes \(\|\mathbf{q}-\mathbf{x}_i\|_2^2=\sum_{j=1}^d(\mathbf{q}_j-\mathbf{x}_{i,j})^2\) for each candidate, requiring \(\Theta(N\cdot d)\) operations.

_Accretive bounds._ We decompose the squared Euclidean distance through a norm-preserving orthogonal transform \(T:\mathbb{R}^d\rightarrow\mathbb{R}^d\), following Kashyap and Karras \[26\]:<tbc>

\(\|\mathbf{q}-\mathbf{x}\|^2=\|T(\mathbf{q})\|^2+\|T(\mathbf{x})\|^2-2\langle T(\mathbf{q}),T(\mathbf{x})\rangle.\) (1)

<tbc>Given thresholds \(0=m_0<m_1<\cdots<m_L=d\) that partition the dimensions into _L_ levels, we define partial inner products and tail (residual) energies:

\(p^{(\ell_1,\ell_2)}(\mathbf{q},\mathbf{x})=\sum_{j=m_{\ell_1}+1}^{m_{\ell_2}}T(\mathbf{q})_jT(\mathbf{x})_j,R_{T(\mathbf{q})}^{(\ell_1,\ell_2)}=\sum_{j=m_{\ell_1}+1}^{m_{\ell_2}}T(\mathbf{q})_j^2,R_{T(\mathbf{x})}^{(\ell_1,\ell_2)}=\sum_{j=m_{\ell_1}+1}^{m_{\ell_2}}T(\mathbf{x})_j^2.\) (2)

The Cauchy-Schwarz inequality \[21\] yields a monotonically tightening lower bound on the squared distance:

\(\text{LB}^\ell(\mathbf{q},\mathbf{x})=R_{T(\mathbf{q})}^{(0,d)}+R_{T(\mathbf{x})}^{(0,d)}-2\big(p^{(0,\ell)}(\mathbf{q},\mathbf{x})+\sqrt{R_{T(\mathbf{q})}^{(\ell,d)}R_{T(\mathbf{x})}^{(\ell,d)}}\big)\le\|\mathbf{q}-\mathbf{x}\|^2.\) (3)

We further introduce a _pruning aggressiveness_ parameter \(\epsilon\in[0,1]\). At level \(\ell\), the distance comprises an exact accumulated term minus the unknown tail inner product. Let \(A^\ell=R_{T(\mathbf{q})}^{(0,d)}+R_{T(\mathbf{x})}^{(0,d)}-2p^{(0,\ell)}(\mathbf{q},\mathbf{x})\) and \(C^\ell=\sqrt{R_{T(\mathbf{q})}^{(\ell,d)}R_{T(\mathbf{x})}^{(\ell,d)}}\). The strict Cauchy-Schwarz bound subtracts the worst-case tail term \(2C^\ell\); reducing this correction gives the relaxed score:

\(\text{LB}_\epsilon^\ell(\mathbf{q},\mathbf{x})=A^\ell-2\epsilon C^\ell.\) (4)

<sup>1</sup>Some indexes like HNSW interleave filtering and refinement; we treat the exact- distance computations on visited nodes as the refinement phase.


<tbc>_Soundness at_ \(\varepsilon=1\). Setting \(\varepsilon=1\) recovers the exact Cauchy- Schwarz lower bound (Equation (3)), so pruning cannot remove any candidate that could still enter the top-_k_ over the candidate set. Lowering \(\varepsilon\) relaxes this worst-case tail correction to enable more aggressive pruning and higher throughput, trading off strict exactness for a controlled recall-throughput knob. As Figures 6 and 7 show, this relaxation consistently yields superior performance at any recall target while the strict mode remains available whenever exact refinement is needed.

**Algorithm 1** Panorama: Iterative Distance Refinement

1: **Input:** Query q, candidate set \(\mathcal{C}=\{\mathbf{x}_1,\dots,\mathbf{x}_{N^\prime}\}\), transform T, levels \(m_1<\cdots<m_L\), k, batch size B, pruning parameter \(\varepsilon\in[0,1]\)

2: **Precompute:** T(q), \(\|T(\mathbf{q})\|^2\), and tail energies \(R_\mathbf{q}^{(\ell,d)}\) for all \(\ell\)

3: **Initialize:** Global exact distance heap H (size k), global threshold \(d_k\leftarrow+\infty\)

4: Compute exact distances of first k candidates, initialize H and d<sub>k</sub>

5: **for** each batch \(\mathcal{B}\subset\mathcal{C}\) of size B do

6: **for** \(\ell=1\) to L **do**

7: **for** each candidate \(\mathbf{x}\in\mathcal{B}\) **do**

8: **if** \(\mathrm{LB}_\ell^\ell(\mathbf{q},\mathbf{x})>d_k\) **then** \(\triangleright\varepsilon=1\) is exact; smaller values prune more

9: Mark x as pruned \(\triangleright\) If threshold exceeded, prune candidate

10: **continue**

11: **for** each unpruned candidate \(\mathbf{x}\in\mathcal{B}\) **do**

12: Push (LB<sup>L</sup>(q,x),x) to H as exact entry \(\triangleright\mathrm{LB}^L(\mathbf{q},\mathbf{x})\) is ED as \(\ell=L\)

13: **if** d\<d<sub>k</sub> **then**

14: Update d<sub>k</sub>=k<sup>th</sup> distance in H; Crop H

15: **return** Candidates in H (top k with possible ties at k<sup>th</sup> position)

_Algorithm._ Algorithm 1 is the Panorama refinement loop. It maintains a heap _H_ of exact _k_NN distances seen so far, initialized on the first _k_ candidates, and the associated _k_<sup>th</sup> smallest distance d<sub>k</sub>. For each subsequent batch, it advances all candidates one level at a time, prunes any with lower bound \(\mathrm{LB}_\varepsilon^\ell(\mathbf{q},\mathbf{x})>d_k\) (Line 8), and bulk-commits the survivors’ exact distances to _H_ at the final level (Lines 12-14). As memory layouts across state-of-the-art indexes vary wildly, we decouple the pruning strategy from the layout via the _batch size_ parameter _B_:

When the index organizes contiguously (IVFFlat, IVFPQ), we set _B_ to 1024 to balance systems affordances with pruning power, as discussed in Section 6.1. When candidates arise non- contiguously (HNSW, Refine), we set _B_=1: the inner batch loop collapses and each candidate is early-abandoned at its first offending level, which is the only feasible mode under scattered memory access. Section 6 elaborates on the systems consequences.

Let \(\rho_i\in\{m_0,\dots,m_L\}\) be the dimension at which candidate **x**_<sub>i</sub>_ is pruned (or survives, with \(\rho_i=d\)). The total cost is \(\sum_{i=1}^N\rho_i\), so with \(\phi=\frac{\mathbb{E}[\rho]}{d}\) the average fraction of dimensions processed, the expected cost is \(\mathcal{O}(\phi dN)\). We make this scaling precise in Section 5.

Panorama relies on (i) a transform _T_ that concentrates energy in leading dimensions, enabling tight bounds--achieved through PCA (Section 4) and (ii) level thresholds \(m_\ell\) that balance the per-level control overhead against pruning granularity.

## 4 TRANSFORM AND VARIANCE SHAPING

The scheme of Section 3 reduces the distance estimation per can didate **x** and level \(\ell\) to the geometric mean \(\sqrt{R_{T(\mathbf{q})}^{(\ell,d)}}R_{T(\mathbf{x})}^{(\ell,d)}\) of tail energies. This quantity drops for each **x** as \(\ell\) grows; when it falls below the running gap between **x**’s known distance and the current _k_<sup>th</sup> distance, **x** is ruled out of the _k_NN set, hence we stop reading its coordinates. The task of the orthogonal transform _T_ is to make those trailing tail energies shrink promptly.

This section addresses the following two questions:

\(\bullet\) _Which_ orthogonal transform shrinks the tail most effectively (§4.1)? We argue that PCA is the natural answer: a closed-form, data-adaptive transform that minimizes the expected tail energy at each level, and whose spectrum yields the decay rate.<tbc>

\(\bullet\) _How_ do we reconcile PCA with product quantization (PQ), given that PCA breaks PQ’s uniform bit-budget assumption (§4.2)? We amend PCA with a process that evens out energy between and within PQ blocks while retaining most of its front-loading.

### 4.1 PCA as the closed-form transform

Given a dataset \(\mathcal{D}\subset\mathbb{R}^d\) with empirical covariance \(\Sigma\), PCA (_principal component analysis_) returns the orthogonal matrix \(T\in\mathbb{R}^{d\times d}\) whose rows are the eigenvectors of \(\Sigma\), ordered so that the corresponding eigenvalues satisfy \(\lambda_1\ge\cdots\ge\lambda_d\ge 0\). As an orthogonal transform, PCA preserves Euclidean geometry: \(\|T(\mathbf{x})\|_2=\|\mathbf{x}\|_2\) and \(\|T(\mathbf{q})-T(\mathbf{x})\|_2=\|\mathbf{q}-\mathbf{x}\|_2\), hence transformed vectors retain the distance decomposition of Equation (1) and the lower bound of Equation (3) is _lossless_. PCA is singled out among orthogonal transforms by its energy _distribution_ across coordinates.

_Why PCA is the right basis?_ Orthogonal transforms conserve energy: the total \(\sum_j\|T(\mathbf{x})_j\|^2=\|\mathbf{x}\|^2\) is fixed, so any reduction in tail energy arises by moving energy into leading coordinates. The movable amount is determined by the spectrum of \(\Sigma\) via a classical variational fact (Ky Fan / Schur-Horn \[21\]): the maximum energy that an orthogonal transform can place in the first _m_ coordinates is \(\sum_{j=1}^m\lambda_j\), attained when the leading rows of _T_ span the top-_m_ eigenvalues of \(\Sigma\)--which is exactly what PCA provides. PCA is therefore optimal at every level simultaneously, leaving the smallest possible expected tail \(\sum_{j>m}\lambda_j\).

_How about other orthogonal transforms?_ Two alternatives--the Discrete Cosine Transform \[44\] and the Haar wavelet basis \[38\]-- also concentrate energy into leading coordinates, but only provided that the data has strong _local self-similarity_, i.e., adjacent coordinates of correlated values, as in smooth signals or natural images. These _fixed_ (non-data-adaptive) bases succeed when the data already aligns with them. In unstructured embedding spaces such as text representations and learned features, no such locality exists, hence these fixed bases do not improve on the original axes. By contrast, PCA’s eigenvectors are by definition the directions of maximum variance _in the data at hand_, hence PCA adapts to the data’s covariance structure. As Figure 1 illustrates, PCA compacts energy more than DCT and Haar wavelet transforms, regardless of the underlying data.

_Energy compaction and the parameter_ \(\alpha\). While PCA is the right basis, the way the tail shrinks is an empirical property of a dataset.

\begin{tabular}{ccc}
**Variant** & **_B_** & **Applicable indexes** \\
Batched (clustered) & _B\>_1 & IVFFlat, IVFPQ \\
No-batch (point-centric) & _B_=1 & HNSW, Refine \\
\end{tabular}

** 1: Panorama’s two modes, driven by batch size.**


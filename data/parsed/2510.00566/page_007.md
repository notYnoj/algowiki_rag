<tbc>Proposition 5.3. _Under residual isotropy for non-near-neighbor pairs and_ \(c_\mathrm{typ}+\mathrm{ln}\varepsilon>0\)_, the expected cost under_ \(\varepsilon\)_-relaxation satisfies_

\(\mathbb{E}[\mathrm{Cost}_\varepsilon]\lesssim\frac{Nd\left(c_\mathrm{typ}+\mathrm{ln}\varepsilon\right)}{\alpha}.\)

_With observed c_<sub>typ</sub>≈1_, this simplifies to_ \(\mathbb{E}[\mathrm{Cost}_\varepsilon]\lesssim Nd(1+\mathrm{ln}\varepsilon)/\alpha\) _over the validity range_ \(\varepsilon>1/e\).

_Proof sketch._ The argument follows the three-part structure of Proposition 5.1 (per-candidate pruning depth, margin estimate, aggregation), where step (a) uses the typical-case gap. We substitute \(\rho_m\approx 0\) from the residual-isotropy assumption into the gap identity, yielding \(\|\mathbf{q}-\mathbf{x}\|^2-\mathrm{LB}_\varepsilon^m\approx 2\varepsilon C^m\), and apply the exponential tail to the geometric mean inside _C<sup>m</sup>_ followed by the bounded-norm condition:<tbc>

\(\|\mathbf{q}-\mathbf{x}\|^2-\mathrm{LB}_\varepsilon^m(\mathbf{q},\mathbf{x})\approx 2\varepsilon C^m\approx 2\varepsilon\|\mathbf{q}\|\|\mathbf{x}\|e^{-\alpha m/d}\)<br>
\(\le 2\varepsilon R^2e^{-\alpha m/d},\)

<tbc>where the first ≈ is from the typical-case substitution, the second ≈ applies the exponential tail to both factors of _C<sup>m</sup>_, and the final \(\le\) follows from bounded norms. Pruning occurs at the smallest _m_ for which this gap falls below the margin, i.e., \(2\varepsilon R^2e^{-\alpha m/d}\le\Delta\). Solving for _m_ gives the per-candidate pruning depth

\(\rho_\varepsilon\approx\frac{d}{\alpha}\mathrm{ln}\left(\frac{2R^2}{\Delta}\right)+\frac{d}{\alpha}\mathrm{ln}\varepsilon.\)

The first term is the typical-case pruning depth at \(\varepsilon=1\). It differs from the strict worst-case depth of Proposition 5.1 by carrying 2_C<sup>m</sup>_ instead of 4_C<sup>m</sup>_, and is absorbed into the empirical typical-case constant. The second term is new: a constant additive shift of \(\frac{d}{\alpha}\mathrm{ln}\varepsilon\) per candidate that relies on the typical-case substitution \(\rho_m\approx 0\). Since \(\mathrm{ln}\varepsilon\le 0\) for \(\varepsilon\le 1\), the shift is negative, shrinking the pruning depth. Summing over _N_ candidates yields \(\mathbb{E}[\mathrm{Cost}_\varepsilon]\lesssim\frac{Nd}{\alpha}\left(c_\mathrm{typ}+\mathrm{ln}\varepsilon\right)\), and the observed _c_<sub>typ</sub>≈1 gives the proposition. □

_On the formal validity range._ The asymptotic formula requires \(c_\mathrm{typ}+\mathrm{ln}\varepsilon>0\). Setting _c_<sub>typ</sub>=1 gives the conventional threshold \(\varepsilon>1/e\approx 0.37\); the actual threshold is dataset-dependent. Below this threshold, the pruning depth \(\rho_\varepsilon\) becomes negative, indicating that the bound clears the margin already at level zero, i.e., the relaxation is so aggressive that a candidate may be pruned before any coordinate is read. This is an artifact of the asymptotic; in this regime the speedup is determined by other factors (e.g., the rate at which the heap warms up) and \(\varepsilon\) should be empirically tuned.

_Speedup vs. recall._ Proposition 5.3 characterizes the speed side of the tradeoff. Pruning at \(\varepsilon<1\) can discard true _k_-nearest neighbors when \(\rho_m>\varepsilon\) and the resulting overestimate crosses the running threshold. The resulting recall loss depends on the dataset-specific distribution of \(\rho_m\) for true _k_-NN pairs, shown on the right panel of Figure 10.

_Additive vs. multiplicative gain._ The \(\varepsilon\)-relaxation is _additive_ on the per-candidate pruning depth, in contrast to the multiplicative \(1/\alpha\) scaling of the base model. Moderate values of \(\varepsilon\) (0.7-0.9) can thus produce a noticeable QPS shift even without large changes to the leading \(1/\alpha\) scaling, while preserving near-perfect recall.

_Empirical Validation._ The right panel of Figure 10 sweeps \(\varepsilon\) on Panorama-IVFFlat over Ada and overlays the \(1/(1+\mathrm{ln}\varepsilon)\) prediction against measured QPS. Empirical throughput tracks the curve closely across the validity range, while recall remains within 1% of the unrelaxed baseline for all \(\varepsilon>0.5\).

## 6 SYSTEM DESIGN AND FAISS INTEGRATION

We implement Panorama in Faiss [14], the industry-standard open- source library for ANNS, which provides optimized implementations for every index family we target: IVFFlat, IVFPQ, HNSW, and FastScan-Refine. Integrating Panorama into this system required carefully tailoring components to each method. We describe these components here.

### 6.1 IndexIVFFlatPanorama

IVFFlat [24] partitions the dataset into _n_list clusters via _k_-means and scans the nearest _n_probe clusters to a query. Faiss stores each cluster’s points row-major (cluster[point][dim]). This storage scheme is suboptimal because under an effective pruning threshold, Panorama evaluates only the leading dimensions of each candidate, which with a row-major layout causes inefficient large strides in memory accesses.

_Level-major batched layout._ Thus, we organize each cluster into batches of _B_ vectors in level-major order, generalizing the layout of PDX [28]: within a batch, all _B_ vectors’ level-\(\ell\) slices are stored contiguously, followed by all _B_ level-\(\ell+1\) slices, and so on. Figure 3 shows a simple example where _L_=30 levels and _B_=4 candidates. By this layout, distance computation within a single level proceeds over all _B_ points with a sequential stride. Pruning decisions are made by the pruning threshold set in the previous batch. In effect, overly large values of _B_ will lead to pruning decisions based on a stale pruning threshold, while overly small values of _B_ will introduce additional branches. Increasing _B_ from 1 to 1024 causes the increase in performance between **A1** and **A2** in Figure 9.

_Per-level workflow._ Within each batch, at each level \(\ell\), Panorama executes three phases over the active candidate set stored as an array of _active indices_: (1) _Compute_ partial dot products of the query slice corresponding to level \(\ell\) for each active candidate; (2) _Update_ each candidate’s running distance and test its Cauchy–Schwarz lower bound against the current _k_th nearest neighbor; (3) _Consolidate_ the surviving active indices for the next level. A naive implementation would fuse all three phases into a single branchy loop. We instead implement them as three independently vectorizable kernels. This disaggregation accounts for the performance gap between **A2** and **A3** in Figure 9.

_IVFFlat: Compute_ calculates the partial dot product between the query and each surviving candidate in a batch, \(p^{(\ell-1,\ell)}\left(\mathbf{q},\mathbf{x}\right)\) in Equation (2). We enhance this phase with two specializations. First, at level 1, the active set is the identity since no pruning decisions<tbc>

d1 d2 [...] d30 d31 d32 [...] d60 d931 d932 [...] d960 d1 d2 [...] d30 d31 d32 [...] d60 d931 d932 [...] d960 d1 d2 [...] d30 d31 d32 [...] d60 d931 d932 [...] d960 d1 d2 [...] d30 d31 d32 [...] d60 d931 d932 [...] d960 d1 d2 [...] d30 d31 d32 [...] d60 d931 d932 [...] d960 Level 1 Level 2 Level 30

**Figure 3: Batch 1 storage for IVFFlat on GIST.**


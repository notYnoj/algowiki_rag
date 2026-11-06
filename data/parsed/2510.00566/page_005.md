satisfies \(\tau\), and the resulting matrix _R_ is composed with the PCA basis to yield a single transform, \(R\cdot T_\mathrm{PCA}\).

_Procedure 2: Intra-level isotropization._ Following Procedure 1, each level’s energy is at most \(\tau\). However, the leading coordinates _within_ a level may still hold most of the energy, and thus, as _M\>L_ (i.e., there are more PQ subvectors than levels), cause imbalance for PQ. To eliminate this residual anisotropy, we apply an independent Haar-random orthogonal transform \(U_\ell\in\mathrm{O}(b)\) within each level’s dimensions. As \(U_\ell\) is orthogonal, it preserves each level’s total energy and spreads it uniformly in expectation across _b_ dimensions, as _k_-means codebooks require.

_The combined transform._ The complete transform is the composition \(U\cdot R\cdot T_\mathrm{PCA}\), where _T_<sub>PCA</sub> is the PCA basis, _R_ the Robin Hood rotation of Procedure 1, and _U_ the block-diagonal isotropization of Procedure 2. The composition is orthogonal, preserving soundness, while the per-vector storage and runtime are identical to vanilla PCA. As a side benefit, the intra-level Haar rotation by _U_ makes the residual coordinates isotropic, which the analysis of Section 5 relies on for the \(\epsilon\)-relaxation result of Proposition 5.3.

Figure 2 reports the per-level tail energy on each of our six datasets for three transforms: raw (no rotation), PCA-only, and PCA+Shaping (the full shaped transform with the shown hyperparameter \(\kappa\)). PCA-only attains the strongest pruning and determines the compaction coefficient \(\alpha\) used in our cost model (Section 5). PCA+Shaping forfeits some compaction to attain level energies that fit within the cap \(\tau\), for the sake of IVFPQ; the gap between the two curves is small, as Procedure 1 only applies when a level exceeds the cap. The resulting transform is simultaneously amenable to accretive pruning _and_ product quantization--allowing Panorama to work with IVFPQ while maintaining high recall.

## 5 THE COST MODEL

Section 4 surfaced a single empirical quantity--the PCA tail-decay rate \(\alpha\)--that characterizes how quickly the residual energy of an embedding collapses under the PCA basis. This section turns \(\alpha\) into a quantitative model of Panorama’s refinement cost. We first justify PCA as the energy-optimal basis (§5.1), then derive the core scaling law \(\mathbb{E}[\mathrm{Cost}]\lesssim Nd/\alpha\) (§5.2), and finally extend the bound to out-of-distribution queries (§5.3) and to the speed--recall knob \(\epsilon\) (§5.4). Each result is paired with a direct empirical comparison; full proofs appear in Appendix A. We use \(f\lesssim g\) to denote upper-bound scaling after the finite-sample constants in the model have been made explicit.

### 5.1 Choice of Basis

§4.1 established that PCA is the energy-optimal orthogonal basis: no transform leaves less expected energy \(\sum_{j>m}\lambda_j\) in the trailing coordinates at any level _m_. How fast that tail shrinks is, however, a property of each dataset. Spectral theory provides a strong prior: analytic covariance kernels on a compact domain produce geometrically- decaying Mercer eigenvalues [31], and smooth-activation neural embeddings inherit this through their tangent kernel [9]. Figure 2 confirms it empirically--across all six benchmarks, the PCA tail collapses as \(e^{-\alpha m/d}\), with mean absolute fit error below 0.04. The fitted \(\alpha\) is the single empirical input to everything that follows.

### 5.2 Expected Refinement Cost

Panorama prunes a candidate at level _m_ when its level-_m_ lower bound exceeds the running _k_-th best distance _d<sub>k</sub>_. Equivalently, pruning fires when the gap between the true squared distance and the lower bound drops below the _pruning margin_

\(\Delta(\mathbf{x}):=\|\mathbf{q}-\mathbf{x}\|^2-d_k.\)

True _k_-nearest neighbors satisfy \(\Delta\le 0\) by definition and are never pruned. Non-nearest candidates have positive margin in expectation: in high dimensions, query-database distances tightly concentrate around a mean \(\mu\), while _d<sub>k</sub>_ tracks the lower tail of distances seen so far. A Dvoretzky-Kiefer-Wolfowitz argument [39] on the empirical CDF places _d<sub>k</sub>_ a slowly-growing number of standard deviations below \(\mu\), so a typical non-nearest candidate has \(\Delta>0\) with high probability.

Combining Cauchy-Schwarz with the exponential tail of §5.1 and a bounded-norm condition \(\|T(\mathbf{x})\|\le R\) (giving the prefactor _C_<sub>0</sub>:=4_R_<sup>2</sup>), the level-_m_ gap satisfies

\(\|\mathbf{q}-\mathbf{x}\|^2-\mathrm{LB}^m(\mathbf{q},\mathbf{x})\le C_0e^{-\alpha m/d}.\)

Pruning fires at the smallest _m_ for which this gap drops below \(\Delta\), giving capped per-candidate depth \(\rho\approx\mathrm{min}\{d,(d/\alpha)[\mathrm{ln}(C_0/\Delta)]_+\}\). Summing \(\rho\) over _N_ candidates and absorbing the averaged margin terms into a finite-sample constant _c_ yields the central result of the section.

Proposition 5.1. _Under exponential PCA tail decay, bounded vector norms, and concentrated query-distance distributions, the expected number of coordinate evaluations Panorama performs over N candidates satisfies_

\(\mathbb{E}[\mathrm{Cost}]\lesssim\frac{c\cdot Nd}{\alpha}.\)

Here, _c_ is a finite-sample margin constant that absorbs the averaged per-candidate margin terms.

_Proof sketch._ The argument has three pieces. First, we turn the energy-decay rate \(\alpha\) into a per-candidate pruning depth bound. Second, we model the pruning margin \(\Delta\) through the order-statistic structure of the running threshold _d<sub>k</sub>_. Third, we sum the capped per- candidate depths over the _N_ candidates and absorb the averaged margin terms into the finite-sample constant _c_.

_(a) Pruning depth._ Combining the Cauchy-Schwarz inequality with the exponential PCA tail and the bounded-norm condition, the gap between the true squared distance and the level-_m_ lower bound is:

\(\|\mathbf{q}-\mathbf{x}\|^2-\mathrm{LB}^m(\mathbf{q},\mathbf{x})\le 4\sqrt{R_{T(\mathbf{q})}^{(m,d)}R_{T(\mathbf{x})}^{(m,d)}}\)<br>
\(\approx 4\|\mathbf{q}\|\|\mathbf{x}\|e^{-\alpha m/d}\le C_0e^{-\alpha m/d},\)

where the first step is Cauchy-Schwarz, the second applies the exponential tail to query and database, and the third uses the bounded- norm condition along with the definition _C_<sub>0</sub>:=4_R_<sup>2</sup>. Pruning occurs when this gap drops below the margin \(\Delta\), i.e., at the smallest _m_ with \(C_0e^{-\alpha m/d}\le\Delta\). Solving for _m_ gives the per-candidate pruning depth

\(\rho\approx\mathrm{min}\big\{d,\frac{d}{\alpha}\big[\mathrm{ln}\big(\frac{C_0}{\Delta}\big)\big]_+\big\}.\)

This depth is proportional to \(d/\alpha\) and logarithmic in the margin.


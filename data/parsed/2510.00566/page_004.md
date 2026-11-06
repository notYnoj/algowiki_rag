<tbc>We define the expected residual energy at level _m_ as the normalized PCA tail variance,<tbc>

\(E(m)=\frac{\sum_{j=m+1}^d\lambda_j}{\sum_{j=1}^d\lambda_j},\)

<tbc>i.e., the fraction of total variance retained by the trailing _d-m_ coordinates. Across all six datasets in our study, _E(m_) is modeled well by the exponential:

\(E(m)\approx e^{-\alpha\frac{m}{d}},\)

with a data-specific constant \(\alpha>0\) obtained from the empirical PCA spectrum. Figure 2 reports the empirical _E(m_) and the fitted exponential on each dataset; confirming that the exponential model is faithful to the data. This shape is what classical spectral theory predicts for analytic covariance kernels--smooth neural embeddings (GELU, softmax) and Gaussian-family kernels among them; we develop the connection in Section 5. Here, \(\alpha\) is a measured number per dataset. Larger \(\alpha\) denotes that the tail collapses more rapidly, hence the Cauchy-Schwarz remainder shrinks, and Panorama prunes earlier. We concretize the connection in Section 5, showing that the expected refinement cost scales as \(\frac{Nd}{\alpha}\) .

## 4.2 Spectrum shaping for PQ-compatibility

PCA is excellent for pruning alone, as it aggressively concentrates variance into the leading dimensions. However, in the IVFPQ index, Panorama has to coexist with product quantization (PQ), which clashes with that concentration. We recall how PQ works, explain why PCA breaks it, and describe the two-stage procedure that fixes the problem while preserving most of PCA’s compaction.

_What PQ expects._ Product quantization [25] splits each _d_-dimensional vector into _M_ contiguous subvectors of size _d/m_ and quantizes each subvector with its own 2_<sup>n</sup>_bits-entry codebook learned by _k_- means. Each subvector receives the same number of code bits, under<tbc>

<tbc>the implicit assumption that variance is even across subvectors. If one subvector carries almost all the energy, an equal-bit codebook leads to underrepresentation of the data; if another subvector is almost constant, the codebook budget is wasted on noise.

_Why raw PCA breaks PQ._ The concentration of energy in the first dimensions, which confers to PCA a pruning advantage, clashes with PQ. As the leading subvectors carry nearly all the variance and the trailing ones collapse to near-constant, PQ underserves the informative leading blocks while wasting a fixed-bit budget on near-zero blocks. To use Panorama with IVFPQ, we should reconcile the PCA per-level energies with PQ, while retaining most of the front-loading that facilitates pruning. We do so in two steps: a coarse _inter-level_ redistribution of energy among levels (i.e., blocks), followed by a fine _intra-level_ isotropization that spreads each level’s energy over its dimensions.

_Procedure 1: Robin Hood inter-level shaping._ We split the _d_ PCA coordinates into _L_ contiguous levels of size _b=d/L_, which we use to refine bounds. Let \(E_\ell=\sum_{j=(\ell-1)b+1}^{\ell b}\lambda_j\) be the energy of level \(\ell\). PCA endows the leading levels more than the trailing ones, \(E_1\gg E_L\); PQ requires something closer to a flat profile. A user- chosen hyperparameter \(\kappa\ge 1\) specifies a cap \(\tau=\kappa\bar{E}\) on how much energy a level may carry, where \(\bar{E}=\sum_\ell E_\ell/L\) is the average; \(\kappa=1\) forces perfect equalization; larger \(\kappa\) allows leading levels to remain richer. We sweep levels from front to back, leaving any level with \(E_\ell\le\tau\) unchanged. At a level \(\ell\) that violates the cap, \(E_\ell>\tau\), we apply a Haar-random orthogonal rotation to its dimensions along with a minimal suffix of subsequent dimensions--so that the rotated level’s expected energy drops to \(\tau\). As the rotation is orthogonal, it preserves total energy, redistributing the surplus. This is the _Robin Hood_ metaphor--a rich leading level spills into poorer trailing ones to meet the cap. The procedure terminates once every level<tbc>

PCA
DCT
Haar
Deep/96
SIFT/128
arXiv/768
GIST/960
Ada/1536
Large/3072
1
Tail energy
0.5
0
0
2
4
0
4
8
0
8
16
0
8
16
0
8
16
0
16
32
Levels scanned
Levels scanned
Levels scanned
Levels scanned
Levels scanned
Levels scanned
Levels scanned

Raw
PCA+Reshape
PCA
e-am/d
Deep/96
SIFT/128
arXiv/768
GIST/960
Ada/1536
Large/3072
1
K=4, a=3.6
K=8, a=6.9
K=3, a=8.3
K=8, a=26.6
K=4, a=10.3
K=3, a=12.2
MAE=0.023
MAE=0.032
MAE=0.021
MAE=0.038
MAE=0.029
MAE=0.037
Tail energy
0.5
0
0
2
4
0
4
8
0
8
16
0
8
16
0
8
16
0
16
32
Levels scanned
Levels scanned
Levels scanned
Levels scanned
Levels scanned
Levels scanned

**Figure 1: Per-dataset tail energy as a function of levels scanned for PCA, DCT, and Haar wavelet transforms.**

**Figure 2: Per-dataset tail energy as a function of levels scanned for raw axes (dotted), PCA only (dashed), and Panorama’s PCA+Reshape transform (solid). Each panel reports the shaping cap** \(\kappa\) **and the fitted PCA-only exponential decay rate** \(\alpha\) **used by the cost model. PCA gives the strongest compaction; PCA+Reshape trades some compaction for PQ-friendly level energies.**


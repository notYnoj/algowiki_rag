### 2.4 From the construction to a multiplication algorithm

The rational parameter assignment specifies the retained constituents, their multiplicities, and their matrix dimensions in the published tensor construction. For increasing tensor powers, the extraction theorem yields independent matrix multiplication tensors with normalized logarithmic multiplicity at least \(\widehat{E}\), common normalized logarithmic dimension _M_, and input rank cost at most _C_, up to vanishing losses in the normalized exponents. The six global coordinate permutations balance the final dimensions. The asymptotic sum inequality then gives \(\omega\le\widehat{\Omega}=(C-\widehat{E})/M\).

For every \(\varepsilon>0\), the standard conversion from these tensor bounds to algorithms yields multiplication of two \(n\times n\) matrices in \(O(n^{\widehat{\Omega}+\varepsilon})\) arithmetic operations. The rational parameters are a concrete admissible input to the degeneration and recursive blocking machinery of \[2, 13\]; the entropy-dual factors certify the analysis of the retained constituents.

Since the exact certificate proves \(\widehat{\Omega}<2.37115924\), choose \(0<\varepsilon<2.37115924-\widehat{\Omega}\). This yields the _O(n_<sup>2.37115924</sup>) algorithm stated in Theorem 1. The improvement is carried by the new recursive extraction parameters and their certified analysis. The conversion from that construction to a matrix multiplication algorithm uses the established tensor framework.

## 3 Structured optimization of the construction

The optimization procedure is organized around three structural features of the construction: occurrence masses span different scales, the retained exponent is governed by competing role minima, and the final parameters must admit rigorous certification. We address these with coordinate conditioning, a separate bottleneck correction, and positive rational export. The orbit representation and equality-constrained starting approach were informed by computational notes shared by Eric Naslund; the following sections specify the implementation used here. The documented procedure differs from the Adam and differentiated Sinkhorn approach described in \[9, Section 3\] by combining conditioned quasi-Newton solves with a separate six-control correction.

### 3.1 Smooth parameterization and balanced search objective

Probability vectors are represented by softmax logits. For a local split distribution, a raw logit _z<sub>u</sub>_ is replaced by (_z<sub>u</sub>+z_<sub>_s-u_</sub>)/2 before applying the softmax, imposing (3). For an orbit of size _b_, adding ln_b_ before normalization converts a per-string logit into an orbit mass. Leaf parameters use \(\mu=\frac{1}{2}\mathrm{sigmoid}(z)\). Entropy-dual factors are represented by unconstrained logarithms. These transformations enforce the local probability constraints during optimization, while the exported witness enforces them exactly.

Near the selected point, the three roles are nearly tied at the root and at each constituent stage. We exploit this structure in the numerical search by defining, for \(t\in\{0,4,3\}\),<tbc>

\(\overline{R_t}=\frac{1}{3}\sum_kR_{t,k},h_{t,Y}=R_{t,Y}-R_{t,X},h_{t,Z}=R_{t,Z}-R_{t,X}.\)

<tbc>The six quantities _h_ are equality residuals. The difference between the average-based retained exponent and the actual one is exactly

\(\mathcal{B}(x)=\sum_{t\in\{0,4,3\}}\left(\overline{R_t}(x)-\mathrm{min}_kR_{t,k}(x)\right)\ge 0.\) (16)

Thus an increase in the average can be lost to greater role imbalance. The condition _h_=0 makes B=0; it identifies the six differences targeted by the correction below. With target parameter<tbc>


The rest of the proof has four steps, which separate the mean-square approximation of the estimated first projections from the law of large numbers.

_Step 1 (mean-square approximation of the first projections)._ Using the standard projection argument for fixed-order U-statistics (Serfling, 1980; van der Vaart, 1998), conditional on _Z<sub>i</sub>_, the terms in (4.10) are a U-statistic of fixed order _m_-1 on _n_-1 independent observations, with conditional expectation _M_<sub>_m,_1</sub>(_Z<sub>i</sub>_). In its conditional variance expansion, put _N=n_-1 and _r=m_-1. For independently and uniformly selected _r_-subsets of the _N_ remaining indices, the fraction having a nonempty intersection is<tbc>

\(p_{N,r}=1-\frac{\genfrac(){pt}{2}{N-r}{r}}{\genfrac(){pt}{2}{N}{r}}.\)

<tbc>For _m_=2 (_r_=1), _p_<sub>_N,_1</sub>=1_/N_. For _m_=3 (_r_=2),<tbc>

\(p_{N,2}=\frac{4N-6}{N(N-1)}\le\frac{4}{N}(N\ge 2).\)

<tbc>For _m_=4 (_r_=3), the same calculation gives \(p_{N,3}\le 9/N\) for \(N\ge 3\). Disjoint subsets give conditionally independent kernels and hence zero conditional covariance. For intersecting subsets, Cauchy-Schwarz bounds the absolute covariance, after averaging over _Z<sub>i</sub>_, by \(\mathbb{E}(\|\mathbf{H}_m(Z_1,\dots,Z_m)\|^2)\); indeed the two kernel evaluations have the same unconditional second moment. Therefore the conditional-variance expansion, followed by expectation over _Z<sub>i</sub>_, gives

\(\mathbb{E}\left(\left\|\widehat{M}_{m,1}(Z_i)-M_{m,1}(Z_i)\right\|^2\right)\le\frac{C_m}{n-1}\mathbb{E}(\|\mathbf{H}_m(Z_1,\dots,Z_m)\|^2),\) (D.1)

with _C_<sub>2</sub>=1, _C_<sub>3</sub>=4 (for \(n\ge 3\)), and _C_<sub>4</sub>=9 (for \(n\ge 4\)).

_Step 2 (approximation of the projection vectors)._ Write \(\unknown_i=\unknown(Z_i)\) and \(\Delta_n=n^{-1}\sum_{i=1}^n\|\widehat{\unknown}_i-\unknown_i\|^2\). By (4.7) and (4.11), each component of \(\widehat{\unknown}_i-\unknown_i\) is a multiple of \(\widehat{M}_{m,1}(Z_i)-M_{m,1}(Z_i)\), \(\widehat{\unknown}_m-\unknown_m\) or <o>_Z_</o>-E(_Z_). The bound (D.1), the _L_<sup>2</sup> convergence \(\widehat{\unknown}_m\rightarrow\unknown_m\) of fixed-order U- statistics, and \(\mathbb{E}(\|\overline{Z}-\mathbb{E}(Z)\|^2)=O(n^{-1})\) give \(\mathbb{E}(\Delta_n)=O(n^{-1})\), so \(\Delta_n\rightarrow^p0\). This step uses only second moments and involves no law of large numbers.

_Step 3 (law of large numbers)._ The vectors \(\unknown_1,\dots,\unknown_n\) are iid with \(\mathbb{E}(\|\unknown_1\|^2)<\infty\), so the ordinary law of large numbers gives \(\widetilde{\Omega}_n=n^{-1}\sum_i\unknown_i\unknown_i^\mathsf{T}\rightarrow\Omega\) almost surely.

_Step 4 (combination)._ Let \(\|A\|_F=\{\mathrm{tr}(A^\mathsf{T}A)\}^{1/2}\) denote the Frobenius norm. For any vectors **_u_**_,**v**_, \(\|\mathbf{uu}^\mathsf{T}-\mathbf{v}\mathbf{v}^\mathsf{T}\|_F\le\|\mathbf{u}-\mathbf{v}\|^2+2\|\mathbf{u}-\mathbf{v}\|\|\mathbf{v}\|\). Averaging over _i_ and applying the Cauchy-Schwarz inequality,

\(\|\widehat{\Omega}_n-\widetilde{\Omega}_n\|_F\le\Delta_n+2\Delta_n^{1/2}\big(n^{-1}\sum_{i=1}^n\|\unknown_i\|^2\big)^{1/2}.\)

By Steps 2 and 3 the right-hand side tends to zero in probability, and hence \(\widehat{\Omega}_n\rightarrow^p\Omega\).


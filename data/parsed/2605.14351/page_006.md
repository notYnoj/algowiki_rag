_Proof._ The inclusion is immediate from (37). For the finite-horizon statement, _T_ distinct poles give a full-rank Vandermonde matrix on samples 0_,...,T_-1, so their span is all of C_<sup>T</sup>_. For the _H_<sub>2</sub> statement, suppose \(h\in\ell_2\) is orthogonal to _a(p_) for all _p_ in a set with an accumulation point inside the disk. Then the analytic function

\(g(p)=\sum_{t\ge 0}\overline{h(t)}p^t\)

vanishes on a set with an accumulation point; by the identity theorem \(g\equiv 0\), hence all coefficients _h(t_) vanish. Therefore the atom span is dense. Finally, the NP/LFT formula (34) parametrizes the feasible family by a free Schur parameter. Rational Schur parameters yield rational feasible transfer functions, and the LFT is continuous on compact subsets where it is nonsingular. Dense RAF pole sampling can represent simple-pole rational functions exactly when their poles are present; repeated-pole terms require derivative atoms or approximation by nearby simple poles. Feasibility with respect to the NP/Pick or gain constraints remains a separate certification step.

The Disk-Bochner pole-moment kernel and the Pick kernel therefore have different roles. Monte Carlo pole sampling gives convergence of empirical pole-moment kernels to the chosen \(K_\mu\). Separately, if RAF transfer functions _F<sub>M</sub>_ converge locally uniformly to a Schur function _F_, then their Pick kernels

\(K_{F_M}(\zeta,\xi)=\frac{I-F_M(\zeta)F_M(\xi)^*}{1-\zeta\bar{\xi}}\)

converge locally uniformly to _K<sub>F</sub>_ on compact subsets. The first convergence is a feature-kernel statement; the second is a transfer-function contractivity statement.

## 6. SPARSE RECOVERY AND DISK-VANDERMONDE CONDITIONING

The sparse regression layer of RAF uses standard Lasso or group-Lasso mechanisms, but the statistical guarantees must be stated in terms of the actual realized design matrix. Let _Z<sub>T</sub>_ denote the regression matrix used in the finite data problem: \(Z_T=\Phi\) for direct impulse- response fitting and \((Z_T)_{t,m}=(\phi_m*u)(t)\) for input- output fitting. The familiar sample-size rate is obtained when the empirical Gram matrix \(G_T=Z_T^*Z_T/T\) satisfies an _s_-sparse restricted-eigenvalue condition with constant \(\kappa_\mathrm{RE}>0\) and the columns are scaled so that their empirical norms are _O_(1). Under sub-Gaussian noise with variance proxy \(\sigma^2\) and a true coefficient vector _c<sup>⋆</sup>_ supported on a set _S_ of size _s_, standard arguments yield

\(\|\widehat{c}-c^\star\|_2\le C\frac{\sigma}{\kappa_\mathrm{RE}}\sqrt{\frac{s\mathrm{log}M}{T}},\) (38)

up to constants depending on normalization and group structure (Bickel et al., 2008). For raw impulse-response Vandermonde columns with |_p<sub>m</sub>|\<_1, the column norms may saturate as _T_ grows; in that case one should use the normalized finite-horizon Gram matrix, and the dependence on _T_ is captured by the resulting conditioning constant rather than by the displayed rate alone. Exact support recovery is stronger and requires additional betamin and incoherence or irrepresentability assumptions. Therefore the role of RAF sampling is not to guarantee recovery for every disk dictionary, but to construct a

dictionary whose realized design matrix is sufficiently well conditioned for the data and priors at hand.

For the pure disk-Vandermonde matrix \(\Phi_{t,m}=p_m^t\), conditioning depends on both angular and radial separation. The finite-horizon Gram matrix is

\(G_{ij}=\sum_{t=0}^{T-1}\overline{p_i}^tp_j^t=\frac{1-(\overline{p_i}p_j)^t}{1-\overline{p_i}p_j}.\) (39)

After column normalization, the pairwise coherence is

\(\mu_T(p_i,p_j)=\frac{\left|\sum_{t=0}^{T-1}(\overline{p_i}p_j)^t\right|}{\left(\sum_{t=0}^{T-1}|p_i|^2t\right)^{1/2}\left(\sum_{t=0}^{T-1}|p_j|^2t\right)^{1/2}}.\) (40)

A simple sufficient condition for a normalized sub-Gram matrix is

\(\mathrm{max}_{i\neq j\in S}\mu_T(p_i,p_j)\le\mu_s\Rightarrow\lambda_\mathrm{min}(G_S)\ge 1-(s-1)\mu_s,\) (41)

which follows from Gershgorin’s theorem. This is conservative, but it highlights that angular separation alone is insufficient for disk-supported atoms. Two poles with close radii and close angles can be nearly collinear over a finite horizon, and poles near the unit circle can require longer horizons to separate.

The infinite-horizon limit exposes the natural geometry. For |_p<sub>i</sub>|,|p<sub>j</sub>|\<_1,

\(\mu_\infty(p_i,p_j)=\frac{\sqrt{(1-|p_i|^2)(1-|p_j|^2)}}{|1-\overline{p_i}p_j|},\) (42)

and

\(1-\mu_\infty(p_i,p_j)^2=\left|\frac{p_i-p_j}{1-\overline{p_i}p_j}\right|^2.\) (43)

The right-hand side is the squared pseudo-hyperbolic distance in the disk, familiar from Hardy-space theory. For poles with the same angle, \(p_i=r_ie^{i\theta}\) and \(p_j=r_je^{i\theta}\),

\(d_\mathbb{D}(p_i,p_j)=\frac{|r_i-r_j|}{|1-r_ir_j|}.\) (44)

Radial separation is therefore part of the conditioning story. In this paper, a "well-spread" pole distribution should be understood as one that produces small finite- horizon coherence, or more generally a favorable RE constant, for the candidate supports encountered by the estimator. Developing sharp RIP/RE theory for disk- Vandermonde dictionaries is an interesting problem but is outside the scope of this work.

## 7. ENGINEERING PRIORS AS SAMPLING LAWS AND CONVEX CONSTRAINTS

The practical advantage of the RAF parameterization is that physical knowledge can be enforced either before optimization, by shaping the pole sampling law, or during optimization, by convex constraints on residues and feedthrough terms. We describe common priors for the SISO case; MIMO extensions use the same parallel realization with block residues and channel-wise group structure.

### 7.1 Order and sparsity

Parsimonious models are encouraged by \(\ell_1\) or group-\(\ell_1\) penalties over conjugate pole pairs,


where one may take \(\eta_T(p)=\|a_T(p)\|_2\). Other positive normalizations are possible and simply encode different radial weights. The complex-balanced atomic set is

\(\mathcal{A}_T(\Omega_p)=\left\{e^{i\theta}\widetilde{a}_T(p):p\in\Omega_p,\theta\in[0,2\pi)\right\}.\) (8)

Its Minkowski functional is

\(\gamma_{\Omega_p,T}(h)=inf\left\{\sum_k|d_k|:h=\sum_kd_k\widetilde{a}_T(p_k),p_k\in\Omega_p\right\}.\) (9)

_Proposition 1._ (Validity of the disk atomic gauge). \(\gamma_{\Omega_p,T}\) is a closed convex gauge and is a norm on \(span\mathcal{A}_T(\Omega_p)\). For sampled poles _p_<sub>1</sub>_,...,p<sub>M</sub>_, the finite RAF gauge

\(\gamma_{M,T}(h)=inf\left\{\sum_{m=1}^M|d_m|:h=\sum_{m=1}^Md_m\widetilde{a}_T(p_m)\right\}\) (10)

is likewise a closed convex gauge and a norm on the span of the sampled atoms.

_Proof._ The map \(p\mapsto\widetilde{a}_T(p)\) is continuous and \(\Omega_p\) is compact, hence \(\mathcal{A}_T(\Omega_p)\) is compact. Because all phases are included, the set is balanced. Therefore \(conv\mathcal{A}_T(\Omega_p)\) is compact, convex, balanced, and contains the origin. Its Minkowski functional is a closed convex gauge. Restricted to the linear span of the atoms it is finite and positive definite, hence a norm. The finite sampled case is the same argument with a finite compact set.

Thus, after the sampled poles are fixed, the \(\ell_1\) penalty in (6) is exactly a finite atomic-gauge penalty. Since the sampled atom set is a subset of the continuous disk atom set, \(\gamma_{M,T}\) is an inner approximation of \(\gamma_{\Omega_p,T}\) and generally satisfies \(\gamma_{M,T}(h)\ge\gamma_{\Omega_p,T}(h)\) on their common domain. Dense resampling improves this approximation, but equality with the continuous atomic norm is not automatic. If unnormalized columns _a<sub>T</sub>(p<sub>m</sub>_) are used in the solver, the same statement holds with the corresponding radius-dependent weights absorbed into the coefficients; column normalization is recommended when sparsity weights should not depend implicitly on atom energy.

The random-feature interpretation arises by drawing \(p_m\sim\mu\) and considering the empirical kernel

\(\widehat{K}_M(s,t)=\frac{1}{M}\sum_{m=1}^Mp_m^s\overline{p_m^t}.\) (11)

This is an unbiased approximation of the disk-supported kernel

\(K_\mu(s,t)=\int p^s\overline{p^t}d\mu(p).\) (12)

Thus RAFs are explicit Monte Carlo features for a stable modal RKHS. Unlike a purely kernelized estimator, the columns of _X_ have direct physical meaning: each column is the response of a stable first-order mode to the measured input. This makes it natural to impose modal priors through the sampling law, such as annular regions for time constants or sectors for resonant bands, and to impose response-level priors through convex constraints on _c_ and _D_.

### 2.2 Relationship with AMLS kernels

Writing \(p=re^{i\theta}\) and setting \(\alpha=-logr\), \(\omega=\theta\) gives

\(K_\nu(s,t)=\iint e^{-\alpha(s+t)}e^{i\omega(s-t)}d\nu(\alpha,\omega),\) (13)

where \(\nu\) is the pushforward of \(\mu\) under \(p\mapsto(\alpha,\omega)\). This is a continuous mixture of locally stationary kernels whose stationary part depends on _s-t_ and whose amplitude modulation depends on _s+t_. In this sense, disk-supported pole mixtures provide an explicit random-feature representation for an AMLS-like class of kernels (Chen, 2018). The disk view is useful because it exposes the pole geometry directly, while the AMLS view connects the construction to existing kernel design methods for regularized system identification.

## 3. KERNEL PROPERTIES AND RANDOM-FEATURE APPROXIMATION

This section records the basic properties of disk-supported RAF kernels. The proofs are included because the details clarify which statements are consequences of positive measures and which require additional operator-theoretic structure.

_Theorem 1._ (PSD and strict PD). For any finite positive Borel measure \(\mu\) on <o>D</o><sub>_p_</sub>, the kernel

\(K_\mu(s,t)=\int_{|p|\le\rho} p^s\overline{p^t}d\mu(p)\) (14)

is Hermitian positive semidefinite. If \(supp(\mu)\) has a limit point in \(\mathbb{D}_\rho\) and the time indices are distinct, then \(K_\mu\) is strictly positive definite on every finite set of such indices.

_Proof._ For finite coefficients _a<sub>i</sub>_ at times _t<sub>i</sub>_,

\(\sum_{i,j}a_i\overline{a_j}K_\mu(t_i,t_j)=\int_{|p|\le\rho}\sum_{i,j}a_i\overline{a_j}p^{t_i}\overline{p^{t_j}}d\mu(p)\)<br>
\(=\int_{|p|\le\rho}\left|\sum_ia_ip^{t_i}\right|^2d\mu(p)\ge 0.\)

If the quadratic form is zero, the polynomial \(f(p)=\sum_ia_ip^{t_i}\) vanishes \(\mu\)-almost everywhere. If the support has an accumulation point in the open disk, the identity theorem for analytic functions forces \(f\equiv 0\). Since monomials with distinct exponents are linearly independent, all _a<sub>i</sub>_=0.

_Theorem 2._ (Uniform convergence of RAF kernels). Let \(\mu\) be a probability measure supported on \(|p|\le\rho\le 1\) and let _p_<sub>1</sub>_,...,p<sub>M</sub>_ be i.i.d. samples from \(\mu\). For any finite horizon _T_ and \(\varepsilon>0\),

\(Pr\left(max_{0\le s,t\le T}|\widehat{K}_M(s,t)-K_\mu(s,t)|>\varepsilon\right)\)<br>
\(\le 4(T+1)^2exp\left(-M\varepsilon^2/8\right).\) (15)

_Proof._ For every fixed pair (_s,t_), the random variable \(p^s\overline{p^t}\) is complex-valued and has magnitude at most one when \(\rho\le 1\). Apply Hoeffding’s inequality separately to the real and imaginary parts and then use a union bound over the (_T_+1)<sup>2</sup> entries. Constants are not optimized; the statement is intended as a finite-horizon Monte Carlo guarantee analogous to random Fourier and random Laplace feature bounds (Rahimi and Recht, 2007; Yang et al., 2014).

_Theorem 3._ (RKHS-to-\(\ell_1\) embedding). Let \(K_\mu\) be the disk kernel in (14), where \(\mu\) is a finite positive Borel measure over pole locations. If \(sup\{|p|:p\in supp(\mu)\}=\rho<1\) and \(\|\mu\|<\infty\), then every \(h\in\mathcal{H}(K_\mu)\) satisfies


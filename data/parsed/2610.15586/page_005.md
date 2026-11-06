**Input:** positive estimates \(\lambda_\mathrm{min}\), \(\lambda_\mathrm{max}\) (certified bounds _a,B_ if guarantees are required), number of states \(d\ge 3\)<br>
\(t_\mathrm{low}\leftarrow\pi/\lambda_\mathrm{max}\); \(t_\mathrm{high}\leftarrow 2\pi/\lambda_\mathrm{min}\); \(\mathcal{T}\leftarrow\{0\}\)<br>
**For** _k_=1_,...,d_-1:<br>
\(\mathcal{T}\leftarrow\mathcal{T}\cup\{t_\mathrm{low}(t_\mathrm{high}/t_\mathrm{low})^{(k-1)/(d-2)}\}\)<br>
**End for**<br>
**return** T

**Algorithm 2:** Heuristic multiscale sampling times

shots each, the time-averaged outcome law is<tbc>

\(q(z)=\frac{1}{d}\sum_{k=1}^d\big|\langle z|_Fe^{-iAT_k}|b\rangle\big|^2.\) (6)

<tbc>Let \(P_\lambda\) be the spectral projector of _A_ onto the eigenvalue \(\lambda\), and define \(a_\lambda\left(z\right)=\langle z|_FP_\lambda b\rangle\). Then

\(\hat{x}_z=\sum_\lambda\frac{a_\lambda\left(z\right)}{\lambda},\hat{b}_z=\sum_\lambda a_\lambda\left(z\right).\) (7)

**Theorem 2** (Expected energy-norm error)**.** _Let_ S _be the set of distinct indices observed with M/d shots on each Krylov state. Then_<tbc>

\(\mathbb{E}\big[\|x_\mathcal{S}-x^*\|_A^2\big]\le\lambda_\mathrm{max}\sum_z|\hat{x}_z|^2e^{-Mq\left(z\right)}.\) (8)

<tbc>_Proof._ Let \(\Pi_\mathcal{S}\) be the orthogonal projector onto _V_<sub>S</sub>. Since \(\Pi_\mathcal{S}x^*\in V_\mathcal{S}\), Lemma 1 gives \(\|x_\mathcal{S}-x^*\|_A\le\|\Pi_\mathcal{S}x^*-x^*\|_A\). In general \(\|v\|_A^2\le\lambda_\mathrm{max}\|v\|^2\), so that<tbc>

\(\|x_\mathcal{S}-x^*\|_A^2\le\lambda_\mathrm{max}\sum_{z\notin\mathcal{S}}|\hat{x}_z|^2.\) (9)

<tbc>Let _p<sub>k</sub>(z_) be the probability of index _z_ in one shot on the _k_th state. The shots are independent. By using \(1-p\le e^{-p}\), we obtain

\(\mathrm{Pr}(z\notin\mathcal{S})=\prod_k\big(1-p_k(z)\big)^{M/d}\le\mathrm{exp}\big(-\frac{M}{d}\sum_kp_k(z)\big)=e^{-Mq\left(z\right)}.\) (10)

By substituting Eq. (10) into the expectation of Eq. (9), we obtain Eq. (8).

For unequal shot counts _M<sub>k</sub>_ on the _k_th state, the same proof gives the bound<tbc>

\(\lambda_\mathrm{max}\sum_z|\hat{x}_z|^2\mathrm{exp}\big[-\sum_kM_kp_k(z)\big].\)

<tbc>Theorem 2 is an expectation statement. If _R(M_) denotes its right-hand side divided by \(\|x^*\|_A^2\), Markov’s inequality gives

\(\mathrm{Pr}\big(\|x_\mathcal{S}-x^*\|_A>\epsilon\|x^*\|_A\big)\le R(M)/\epsilon^2.\)

A mean-square bound is therefore not a high-probability guarantee unless the budget includes the failure probability. Corollary 4 below gives such a budget.


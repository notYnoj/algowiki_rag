For the residual _r=b-Ax_<sub>S</sub>, the identity \(\|x^*-x_\mathscr{S}\|_A^2=r^\dagger A^{-1}r\) gives the computable certificate

\(\frac{\|x^*-x_\mathscr{S}\|_A}{\|x^*\|_A}\le\sqrt{\kappa}\frac{\|r\|}{\|b\|}.\) (14)

Consequently, the residual stopping rule of Algorithm 1 certifies a relative energy error of at most \(\sqrt{\kappa}\varepsilon\), not generally \(\varepsilon\). For an energy tolerance \(\varepsilon_A\) one uses a certified condition-number bound and the residual tolerance \(\varepsilon_A/\sqrt{\kappa}\). Approximate matrix assembly and inexact reduced solves require additional error terms.

## 3.1 Support completeness and dephasing

The following statement explains why a single state can fail and a long time average cannot, and it gives an a priori floor for _q_<sub>min</sub>. We define the dephased law \(q^\infty(z)=\sum_\lambda|a_\lambda(z)|^2\), where the sum runs over the distinct eigenvalues of _A_.

**Theorem 7** (Support completeness)**.** _For every index z,_

\(q^\infty(z)\ge\frac{|\hat{x}_z|^2}{\sum_\lambda\lambda^{-2}}\ge\frac{|\hat{x}_z|^2}{\text{tr}A^{-2}}.\) (15)

_In particular,_ \(\text{supp}\hat{x}\subseteq\text{supp}q^\infty\).

_Proof._ By Eq. (7) and the Cauchy-Schwarz inequality, \(|\hat{x}_z|^2=|\sum_\lambda a_\lambda(z)\lambda^{-1}|^2\le\sum_\lambda|a_\lambda(z)|^2\sum_\lambda\lambda^{-2}\). The sum over distinct eigenvalues is at most the trace of _A_<sup>-2</sup>.

The probability of _z_ in the single state \(|b\rangle\) is \(|\hat{b}_z|^2=|\sum_\lambda a_\lambda(z)|^2\). This sum can vanish by cancellation while \(\hat{x}_z=\sum_\lambda a_\lambda(z)/\lambda\) does not, because the weights \(1/\lambda\) break the cancellation. A classical selection of modes by the magnitude of \(\hat{b}\) has the same deficiency. Section 5.4 shows that this happens for the elliptic duct. For the dephased law, Eq. (15) gives

\(q_\text{min}^\infty(\mathscr{E}_\varepsilon)\ge\frac{\text{min}_{z\in\mathscr{E}_\varepsilon}|\hat{x}_z|^2}{\text{tr}A^{-2}},\) (16)

so that Corollaries 3 and 4 become a priori budgets that depend only on the solution profile and the spectrum. The floor depends on the dimension through tr_A_<sup>-2</sup>, which is dominated by the lowest eigenvalues for elliptic operators. For _A=aI_ the bound is exact.

**Corollary 8** (Constant coefficient)**.** _If every basis vector_ \(|z\rangle_F\) _is an eigenvector of A, then_ \(q(z)=q^\infty(z)=|\hat{b}_z|^2\) _for all sampling times, and_ \(\text{supp}\hat{x}=\text{supp}\hat{b}\).

For uniform times \(T_k=k\Delta t\), _k_=0_,...,d_-1, let \(D_d(\theta)=d^{-1}\sum_{k=0}^{d-1}e^{-ik\theta}\). Expanding the amplitudes in the eigenbasis gives the following lemma, proved in Appendix C.

**Lemma 9** (Finite averaging)**.**

\(|q(z)-q^\infty(z)|\le\sum_{\lambda\neq\mu}|a_\lambda(z)||a_\mu(z)|\left|D_d\big((\lambda-\mu)\Delta t\big)\right|,|D_d(\theta)|\le\text{min}\big\{1,\frac{1}{d|\text{sin}(\theta/2)|}\big\}.\) (17)

Equation (17) shows that dephasing requires \(d|\text{sin}((\lambda-\mu)\Delta t/2)|\gg 1\) for the eigenvalue pairs that carry the solution. The required window depends on the relevant eigenvalue differences and on aliasing, not on \(\lambda_\text{min}\) alone, and near-degenerate pairs may require windows much longer than \(2\pi/\lambda_\text{min}\). The step \(\Delta t=\pi/\lambda_\text{max}\), which we use as the reference short step, gives a total time that is shorter than \(2\pi/\lambda_\text{min}\) by a factor of about \(2\kappa/d\). A single grid can fail completely: if \((\lambda-\mu)\Delta t\) is a multiple of \(2\pi\) for every eigenvalue pair with \(a_\lambda(z)a_\mu(z)\neq 0\), then _D<sub>d</sub>_=1 for these pairs and \(q(z)=|\hat{b}_z|^2\), so a mode hidden by cancellation in \(\hat{b}\) stays hidden. Incommensurate or varied time steps avoid this failure.


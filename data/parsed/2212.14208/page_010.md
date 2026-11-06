<tbc>_and, if the flexible Lanczos vectors z<sub>m</sub> approximate the "exactly inverted" vector H_<sup>-1</sup>_v<sub>m</sub> to a relative accuracy of_ \(\varepsilon\) _in the H-norm, i.e._

(4.3) \(\|z_m-H^{-1}v_m\|_H\le\varepsilon\cdot\|H^{-1}v_m\|_H,\)

_then_

(4.4) \(\|V_{m+1}\|_{H^{-1}}\le\left(\frac{m+1}{1-\varepsilon}\right)^{1/2}.\)

_Proof._ Denote by \(V_m\in\mathbb{C}^{n\times m}\) the matrix which contains the flexible Lanczos vectors _v<sub>k</sub>_ as its _k_-th column. We have \(x_m=x_0+V_m\zeta_m\) with \(\zeta_m\) satisfying the minimality condition (3.8). Thus, using the flexible Lanczos relation (3.4) and (3.6) we obtain

\(\|b-Ax_m\|_{H^{-1}}=\|V_{m+1}\beta_0e_1-V_{m+1}T_{m+1,m}\zeta_m\|_{H^{-1}}\)<br>
\(=\|H^{-1/2}V_{m+1}(\beta_0e_1-T_{m+1,m}\zeta_m)\|_2\)<br>
\(\le\|H^{-1/2}V_{m+1}\|_2\cdot\|\beta_0e_1-T_{m+1,m}\zeta_m\|_2\)<br>
\(=\|H^{-1/2}V_{m+1}\|_2\cdot\varrho_m,\)

which is (4.2). To obtain (4.4) we now show that the \(\ell_2\)-norm of each column of _H_<sup>-1/2</sup>_V_<sub>_m_+1</sub> is bounded by \(\sqrt{1/(1-\varepsilon)}\). The inequality (4.4) then follows as the \(\ell_2\)- norm of a matrix never exceeds its Frobenius norm.

With \(\nu_k:=\|v_k\|_{H^{-1}}=\|H^{-1/2}v_k\|_2\) we have<tbc>

\(\nu_k^2=\langle v_k,z_k\rangle+\langle v_k,H^{-1}v_k-z_k\rangle=1+\langle H^{-1/2}v_k,H^{-1/2}v_k-H^{1/2}z_k\rangle,\)

<tbc>from which we get, via the Cauchy-Schwarz inequality,<tbc>

\(|\nu_k^2-1|\le\|H^{-1/2}v_k\|\cdot\|H^{-1/2}v_k-H^{1/2}z\|=\|v_k\|_H\cdot\|H^{-1}v_k-z_k\|_H.\)

<tbc>With assumption (4.3) we therefore have<tbc>

\(|\nu_k^2-1|\le\varepsilon\nu_k^2,\)

<tbc>which is equivalent to

\(\frac{1}{1+\varepsilon}\le\nu_k^2\le\frac{1}{1-\varepsilon}.\) □

There are two important observations regarding Proposition 4.4. First, practically, we cannot monitor _H_-norms of the error, so inequality (4.3) cannot be checked directly. However, a relative reduction of the (\(\ell_2\)-norm of the) residual, which can be measured, typically results in a similar reduction of the error. Moreover, in the case that we use the CG method to approximate _H_<sup>-1</sup>_v<sub>k</sub>_, it is precisely the _H_-norm of the error which is made as small as possible by the CG iterates. We refer to [21] for a further discussion of this and related aspects.

Secondly, the quantity \(\varrho_m\) is available in the algorithm at no additional cost. The situation is similar as in GMRES [20] or QMR [6]: To solve the least squares problem (3.8), we update the _QR_-factorization _T_<sub>_m_+1_,m_</sub>=_Q_<sub>_m_+1_,m_+1</sub>_R_<sub>_m_+1_,m_</sub> in each step. The value \(\varrho_m\) is the last, i.e. the (_m_+1)st, entry of \(Q_{m+1,m}^*\|r_0\|_He_1\), and this value is updated to \(\varrho_{m+1}\) using the Givens rotation which updates _Q_<sub>_m_+1_,m_</sub> to _Q_<sub>_m_+2_,m_+1</sub>.

We further note that the proof of Proposition 4.4 also shows that in the case where we solve for _H_ exactly, we find \(\varrho_m=\|b-Ax_m\|_{H^{-1}}\) as \(\|V_m\|_{H^{-1}}=1\).


<tbc>LEMMA D.3 (Brascamp-Lieb). _For every t,_<tbc>

\(\Sigma_{t-1}^*\unknown\Sigma_0.\)

<tbc>_Consequently, under Assumption 2(i), eventually almost surely,_ \(\Sigma_{t-1}\unknown\chi_+\Sigma_0\)_. In particular, there exists_ \(\bar{\sigma}<\infty\) _such that_

\(\sigma_{t-1,i}\le\bar{\sigma},i=1,\dots,I,\)

_eventually almost surely._

_Proof._ Fix _t_. The likelihood factors are log-concave by Assumption 1, and remain log-concave after averaging over the Gaussian evaluator noise. The posterior is the Gaussian prior multiplied by the product of these factors. By the Brascamp-Lieb covariance inequality (Brascamp and Lieb 1975), \(\Sigma_{t-1}^*\unknown\Sigma_0\). By Assumption 2(i), eventually almost surely \(\Sigma_{t-1}\unknown\chi_+\Sigma_{t-1}^*\unknown\chi_+\Sigma_0\).

Since **_b_**_<sub>t</sub>_ has nonnegative entries summing to 1,<tbc>

\(\|\mathbf{g}_{t,i}\|_2\le\|\mathbf{e}_i\|_2+\|\mathbf{b}_t\|_2\le 2.\)

<tbc>Therefore,

\(\sigma_{t-1,i}^2=\mathbf{g}_{t,i}^\top\Sigma_{t-1}\mathbf{g}_{t,i}\le 4\chi_+\|\Sigma_0\|_\mathrm{op}.\square\)

We next transfer the exact-posterior variance conclusions above to the approximate covariance used by SA.

LEMMA D.4. _Fix a deterministic set_ \(\mathcal{E}\subseteq\mathcal{D}\)_, let M_:=span(E)_, and let R<sub>M</sub> and Q be the orthogonal projectors onto M and_ \(M^\perp\)_. Suppose that on an event_ \(\Omega\),<tbc>

\(\|R_M\Sigma_{t-1}^*R_M\|_\mathrm{op}\rightarrow 0\)

<tbc>_and, for some_ \(\eta>0\) _and all sufficiently large t,_<tbc>

\(Q\Sigma_{t-1}^*Q\unknown\eta Q.\)

<tbc>_Then, under Assumption 2(i) and Lemma D.3, almost surely on_ \(\Omega\),<tbc>

\(\|R_M\Sigma_{t-1}R_M\|_\mathrm{op}\rightarrow 0,\|Q\Sigma_{t-1}R_M\|_\mathrm{op}+\|R_M\Sigma_{t-1}Q\|_\mathrm{op}\rightarrow 0,\)

<tbc>_and, for all sufficiently large t,_<tbc>

\(Q\Sigma_{t-1}Q\unknown\chi_-\eta Q.\)

<tbc>_Proof._ From Assumption 2(i), \(0\unknown R_M\Sigma_{t-1}R_M\unknown\chi_+R_M\Sigma_{t-1}^*R_M\), so \(\|R_M\Sigma_{t-1}R_M\|_\mathrm{op}\rightarrow 0\). For the other terms, let \(\mathbf{x}\in M^\perp\) and \(\mathbf{y}\in M\) be unit vectors. Since \(\Sigma_{t-1}\) is positive semidefinite,<tbc>

\(|\mathbf{x}^\top\Sigma_{t-1}\mathbf{y}|^2\le(\mathbf{x}^\top\Sigma_{t-1}\mathbf{x})(\mathbf{y}^\top\Sigma_{t-1}\mathbf{y})\le\|Q\Sigma_{t-1}Q\|_\mathrm{op}\|R_M\Sigma_{t-1}R_M\|_\mathrm{op}.\)


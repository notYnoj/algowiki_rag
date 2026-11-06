<tbc>By Lemma D.3, the first factor is eventually bounded, while the second converges to 0. Taking the supremum over unit **_x_** and **_y_** gives

\(\|Q\Sigma_{t-1}R_M\|_\mathrm{op}+\|R_M\Sigma_{t-1}Q\|_\mathrm{op}\rightarrow 0.\)

Finally, Assumption 2(i) gives

\(Q\Sigma_{t-1}Q\unknown\chi_-Q\Sigma_{t-1}^*Q\unknown\chi_-\eta Q.\) □

To control the marginal scores, we also need bounds on the affine threshold and the associated weights.

LEMMA D.5. _Let_ \(\Omega\) _be an event on which_

\(\mathrm{sup}_{t\ge 1}\|\mu_{t-1}\|_\infty<\infty,\mathrm{max}_{1\le i\le I}\sigma_{t-1,i}\le\bar{\sigma}\)

_eventually for some finite_ \(\bar{\sigma}\)_. Then, almost surely on_ \(\Omega\)_, there exists_ \(Q_0<\infty\) _such that_ \(|q_t|\le Q_0\) _eventually. In addition, if_ \((i_t)_{t\ge 1}\) _is any sequence in_ {1_,...,I_} _such that_ \(\mathrm{liminf}_{t\rightarrow\infty}\sigma_{t-1,i_t}>0\) _on_ \(\Omega\)_, then there exists w_<sub>∗</sub>_\>_0 _such that_ \(w_{t-1,i_t}\ge w_*\) _eventually on_ \(\Omega\).

_Proof._ First consider rounds in case (ii) of Theorem 1. Define

\(B:=\mathrm{sup}_{t\ge 1}\|\mu_{t-1}\|_\infty<\infty,F_t(q):=\sum_{i=1}^I\Phi\left(\frac{\mu_{t-1,i}-q}{\sigma_{t-1,i}}\right).\)

Recall that _q<sub>t</sub>_ is defined to satisfy _F<sub>t</sub>(q<sub>t</sub>_)=_k_. For each _t_, the map _F<sub>t</sub>_ is continuous and strictly decreasing, with \(F_t(q)\rightarrow I\) as \(q\rightarrow-\infty\) and \(F_t(q)\rightarrow 0\) as \(q\rightarrow+\infty\). Choose _Q_<sub>0</sub>_\>B_ such that

\(I\Phi\left(\frac{B-Q_0}{\bar{\sigma}}\right)<k<I\Phi\left(\frac{Q_0-B}{\bar{\sigma}}\right).\)

For all sufficiently large _t_,

\(F_t(Q_0)\le I\Phi\left(\frac{B-Q_0}{\bar{\sigma}}\right)<k,\)

and similarly,

\(F_t(-Q_0)\ge I\Phi\left(\frac{Q_0-B}{\bar{\sigma}}\right)>k.\)

Since _F<sub>t</sub>_ is strictly decreasing and _F<sub>t</sub>(q<sub>t</sub>_)=_k_, it follows that

\(-Q_0<q_t<Q_0\)

for all sufficiently large _t_. On a round in case (i) of Theorem 1, \(q_t=\mu_{t-1,j}\) for some _j_, so \(|q_t|\le B<Q_0\). Thus, |_q<sub>t</sub>|\<Q_<sub>0</sub> eventually in either case.

Now suppose \(\mathrm{liminf}_{t\rightarrow\infty}\sigma_{t-1,i_t}>0\). Then there exists \(\underline{\sigma}>0\) such that

\(\underline{\sigma}\le\sigma_{t-1,i_t}\le\bar{\sigma}\)

eventually. Together with \(|\mu_{t-1,i_t}|\le B\) and \(|q_t|\le Q_0\), this gives

\(|z_{t-1,i_t}|\le\frac{B+Q_0}{\underline{\sigma}}\)


For every _t,k_, we require that \(\text{split}(\hat{K},S_{t,+,+,k^\prime})=\overline{\beta_{Z,t,+,+,k^\prime}}\), so the number of possibilities of \(\hat{K}\) on \(S_{t,+,+,k^\prime}\) is<tbc>

\(2^{H(\overline{\beta_{Z,t,+,+,k^\prime}})\cdot|S_{t,+,+,k^\prime}|\pm o(n)}=2^{H(\overline{\beta_{Z,t,+,+,k^\prime}})\cdot(\alpha_t(+,+,k^\prime)+\alpha_t(<,<,k_t-k^\prime))\cdot A_{t,1}n_t\pm o(n)}.\)

<tbc>Overall, the number of possible compatible \(\hat{K}\), multiplied by the number of block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_, is

\(N_\alpha\cdot\prod_{t,i^\prime,j^\prime,k^\prime i^\prime=0\text{or}j^\prime=0}2^{H(\overline{\beta_{Z,t,i^\prime,j^\prime,k^\prime}})\cdot(\alpha_t(i^\prime,j^\prime,k^\prime)+\alpha_t(i_t-i^\prime,j_t-j^\prime,k_t-k^\prime))\cdot A_{t,1}n_t\pm o(n)}\cdot\prod_{t,k^\prime} 2^{H(\overline{\beta_{Z,t,+,+,k^\prime}})\cdot(\alpha_t(+,+,k^\prime)+\alpha_t(<,<,k_t-k^\prime))\cdot A_{t,1}n_t\pm o(n)}=2^{\sum_t(H(\alpha_t)+\lambda_{Z,t})\cdot A_{t,1}n_t\pm o(n)}.\text{(23)}\)

Finally, as mentioned, \(p_\text{comp}^*(\{\xi_{Z,t}\}_t)\) is the ratio between (23) and (22), so

\(p_\text{comp}^*(\{\xi_{Z,t}\}_{t\in[s^\prime]})\le 2^{\sum_t(\lambda_{Z,t}-H(\xi_{Z,t})+H(\gamma_{Z,t}))A_{t,r}\cdot n_t+o(n)}\)

as desired. The bound (21) on _p_comp follows as the \(L_\infty\) distance between \(\{\xi_{Z,t}\}_t\) and \(\{\beta_{Z,t}\}_t\) is at most \(\varepsilon\).

The proof of the following claim is essentially the same as that of Claim 5.16.

**Claim 6.15.** _For every_ \(b\in B\)_, every level-_\((\ell-1)\) _block triple X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub> consistent with_ \(\{\alpha_t\}_{t\in[s^\prime]}\)_, and for each typical_ \(Z_\hat{K}\in Z_K\)_, the probability that_ \(Z_\hat{K}\) _is compatible with multiple triples in_ Tcomp _is at most_

\(\frac{N_\alpha\cdot p_\text{comp}}{N_\text{BZ}\cdot M_0},\)

_conditioned on h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b._

Recall that we require _M_<sub>0</sub> to be at least \(8\cdot max\big\{\frac{N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\text{BX}},\frac{N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\text{BY}}\big\}\). Now, we add another (and final) constraint: \(M_0\ge\frac{N_\alpha\cdot p_\text{comp}}{N_\text{BZ}}\cdot n^2\). That is, we will set _M_<sub>0</sub> to be

\(max\big\{\frac{8N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\text{BX}},\frac{8N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\text{BY}},\frac{N_\alpha\cdot p_\text{comp}}{N_\text{BZ}}\cdot n^2\big\}\)<br>
\(\le 2^{max\{\sum_t(H(\alpha_t)-P_{\alpha,t}-H(\gamma_{X,t}))A_{t,1}\cdot n_t,\sum_t(H(\alpha_t)-P_{\alpha,t}-H(\gamma_{Y,t}))A_{t,1}\cdot n_t,\sum_t(H(\alpha_t)+\lambda_{Z,t}-H(\beta_{Z,t}))A_{t,1}\cdot n_t\}+o(n)}.\)

Similar to before, for every \(b\in B\) and every level-\((\ell-1)\) block triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ that is consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\) and \(h_X(I)=h_Y(J)=h_Z(K)=b\), with constant probability, it remains in Thash and the fraction of holes caused by enforcing that each \(Z_\hat{K}\) is compatible with a unique triple is 1_/n_<sup>2</sup>. Additionally, as discussed earlier, the fraction of holes caused by the input complete split distribution constraints are also 1_/n_<sup>2</sup>. Overall, we expect to get \(N_\alpha\cdot M^{-1-o(1)}\) copies of T<sup>∗</sup> whose fraction of holes is _O_(1_/n_<sup>2</sup>).

By Corollary 4.2, we can degenerate them into \(N_\alpha\cdot M^{-1-o(1)}\) unbroken copies of T<sup>∗</sup> because \(O(1/n^2)\le\frac{1}{8N}\) for sufficiently large _n_.


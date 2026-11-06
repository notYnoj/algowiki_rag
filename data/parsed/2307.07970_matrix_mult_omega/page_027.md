**Claim 5.4.** \(N_{\alpha_X,\alpha_Y,\alpha_Z}=2^{(H(\alpha)+P_\alpha)\cdot A_1n\pm o(n)}\).

_Proof._ Recall that \(P_\alpha=max_{\alpha^\prime\in D}H(\alpha')-H(\alpha)\) where _D_ is the set of distributions whose marginal distributions on the three dimensions are \(\alpha_X,\alpha_Y,\alpha_Z\) respectively.

As we zeroed out _X_-, _Y_ -, _Z_-blocks based on \(\alpha_X,\alpha_Y,\alpha_Z\) respectively, all remaining block triples are consistent with one of the distributions \(\alpha'\in D\). Additionally, \(\alpha'(i,j,k)\cdot A_1\cdot n\) must be an integer for every _i,j,k_. Let us denote the set of distributions satisfying such properties as \(D'\).

Thus, \(N_{\alpha_X,\alpha_Y,\alpha_Z}=\sum_{\alpha^\prime\in D^\prime} 2^{H(\alpha^\prime)\cdot A_1n\pm o(n)}\). As \(|D'|=\mathrm{poly}(n)\), we have that<tbc>

\(N_{\alpha_X,\alpha_Y,\alpha_Z}=2^{(max_{\alpha^\prime\in D^\prime} H(\alpha^\prime))\cdot A_1n\pm o(n)}.\)

<tbc>When _n_ approaches \(\infty\), the difference between \(max_{\alpha^\prime\in D^\prime} H(\alpha')\) and \(max_{\alpha^\prime\in D}H(\alpha')\) will approach 0, as the entropy function _H_ is continuous. Thus,

\(N_{\alpha_X,\alpha_Y,\alpha_Z}=2^{(max_{\alpha^\prime\in D}H(\alpha^\prime))\cdot A_1n\pm o(n)}=2^{(H(\alpha)+P_\alpha)\cdot A_1n\pm o(n)}.\)

Let \(M\in[M_0,2M_0]\) be a prime number for some integer _M_<sub>0</sub>. The value of _M_<sub>0</sub> is yet to be fixed, but we first require that

\(M_0\ge 8\cdot max\big\{\frac{N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\mathrm{BX}},\frac{N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\mathrm{BY}}\big\}.\) (7)

One additional term that lower bounds _M_<sub>0</sub> will be mentioned later.

We independently pick uniformly random elements \(b_0,\{w_t\}_{t=0}^n\in\{0,\dots,M-1\}\), and define the following hash functions \(h_X,h_Y,h_Z:\{0,\dots,2^\ell\}^n\rightarrow\{0,\dots,M-1\}\):

\(h_X(I)=b_0+\left(\sum_{t=1}^nw_t\cdot I_t\right)\mathrm{mod}M,\)<br>
\(h_Y(J)=b_0+\left(w_0+\sum_{t=1}^nw_t\cdot J_t\right)\mathrm{mod}M,\)<br>
\(h_Z(K)=b_0+\frac{1}{2}\left(w_0+\sum_{t=1}^nw_t\cdot(2^\ell-K_t)\right)\mathrm{mod}M.\)

Let _B_ be a Salem-Spencer subset of {0_,...,M_-1} that has size _M_<sup>1-_o_(1)</sup> and does not contain any nontrivial 3-term arithmetic progressions (modulo _M_). Then we zero out all blocks _X<sub>I</sub>_ with \(h_X(I)\notin B\), _Y<sub>J</sub>_ with \(h_Y(J)\notin B\), and _Z<sub>K</sub>_ with \(h_Z(K)\notin B\).

For every block triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ in T , we have that \(X_t+Y_t+Z_t=2^\ell\) for every \(t\in[n]\). Therefore, it is not difficult to verify that \(h_X(I)+h_Y(J)\equiv 2h_Z(K)(\mathrm{mod}M)\). In order for \(h_X(I),h_Y(J),h_Z(K)\in B\), we must have _h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b_ for some _b_, because _B_ does not contain any nontrivial 3-term arithmetic progression (modulo _M_). We say that triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ with _h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b_ are contained in bucket _b_.

For every bucket _b_, if it contains two level-\(\ell\) triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ and \(X_IY_{J^\prime} Z_{K^\prime}\) that share the same _X_- block, then we zero out _X<sub>I</sub>_. Similarly, if a bucket contains two level-\(\ell\) triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ and \(X_{I^\prime} Y_JZ_{K^\prime}\) that share the same level-\(\ell Y\) -block, then we zero out _Y<sub>J</sub>_. We repeatedly perform the previous zeroing-outs so that eventually, all remaining triples in the same bucket do not share _X_- or _Y_ -blocks. As each level-\(\ell\) block triple in T must belong to some bucket, we get that all remaining triples do not share _X_- or _Y_ -blocks, i.e., each level-\(\ell\) block _X<sub>I</sub>_ or _Y<sub>J</sub>_ is in a unique level-\(\ell\) block triple. For every level-\(\ell\) block _X<sub>I</sub>_ (or _Y<sub>J</sub>_), we check whether the unique triple containing it is consistent with the distribution \(\alpha\); if not, we zero out _X<sub>I</sub>_ (or _Y<sub>J</sub>_). We call the tensor after this step T<sub>hash</sub>.


Let \(N_\alpha\) be the number of remaining block triples that are consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\). We have

\(N_\alpha=2^{\sum_tH(\alpha_t)\cdot A_{t,1}n_t\pm o(n)}.\) (18)

Finally, let \(N_{\alpha_X,\alpha_Y,\alpha_Z}\) be the number of remaining level-\((\ell-1)\) block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_.

**Claim 6.5.** \(N_{\alpha_X,\alpha_Y,\alpha_Z}=2^{\sum_t(H(\alpha_t)+P_{\alpha,t})\cdot A_{t,1}n_t\pm o(n)}\)_, where we recall that_ \(P_{\alpha,t}:=max_{\alpha_t^\prime\in D_t}H(\alpha'_t)-H(\alpha_t)\) _in which D<sub>t</sub> is the set of distributions sharing the same marginals as_ \(\alpha_t\).

_Proof._ Fixing a series of distributions \(\alpha'_t\in D_t\) (\(t=1,2,\dots,s'\)), the number of level-\((\ell-1)\) block triples consistent with \(\{\alpha'_t\}_{t\in[s^\prime]}\) equals

\(2^{\sum_tH(\alpha_t^\prime)\cdot A_{t,1}n_t\pm o(n)}\le 2^{\sum_tmax_{\alpha_t^{\prime\prime}\in D_t}H(\alpha_t^{\prime\prime})\cdot A_{t,1}n_t\pm o(n)}\le 2^{\sum_t(H(\alpha_t)+P_{\alpha,t})\cdot A_{t,1}n_t\pm o(n)}.\)

Taking summation over all poly(_n_)=2<sup>_o(n_)</sup> series of distributions \(\{\alpha'_t\}_{t\in[s^\prime]}\) will prove the claim.

Let \(M\in[M_0,2M_0]\) be a prime number for some integer _M_<sub>0</sub>. Similar as before, the value of _M_<sub>0</sub> is yet to be fixed, but we first require that

\(M_0\ge 8\cdot max\big\{\frac{N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\text{BX}},\frac{N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\text{BY}}\big\}.\) (19)

We independently pick uniformly random elements \(b_0,\{w_p\}_{p=0}^{2n}\in\{0,\dots,M-1\}\), and define the following hash functions \(h_X,h_Y,h_Z:\{0,\dots,2^{\ell-1}\}^n\rightarrow\{0,\dots,M-1\}\):

\(h_X(I)=b_0+\left(\sum_{p=1}^{2n}w_p\cdot I_p\right)modM,\)<br>
\(h_Y(J)=b_0+\left(w_0+\sum_{p=1}^{2n}w_p\cdot J_p\right)modM,\)<br>
\(h_Z(K)=b_0+\frac{1}{2}\left(w_0+\sum_{p=1}^{2n}w_p\cdot(2^{\ell-1}-K_p)\right)modM.\)

Next, for a Salem-Spencer subset _B_ of {0_,...,M_-1} that has size _M_<sup>1-_o_(1)</sup>, we zero out all level-\((\ell-1)\) blocks _X<sub>I</sub>_ with \(h_X(I)\notin B\), _Y<sub>J</sub>_ with \(h_Y(J)\notin B\), and _Z<sub>K</sub>_ with \(h_Z(K)\notin B\). Then all remaining block triples are contained in a bucket _b_ for some \(b\in B\).

For every bucket _b_, if it contains two level-\((\ell-1)\) triples \(X_IY_JZ_K\) and \(X_IY_{J^\prime} Z_{K^\prime}\) that share the same _X_-block, then we zero out _X<sub>I</sub>_. We similarly handle _Y_ -blocks. We repeatedly perform the previous zeroing- outs so that all remaining triples do not share _X_- or _Y_ -blocks. For every level-\((\ell-1)\) block _X<sub>I</sub>_ (or _Y<sub>J</sub>_), we check whether the unique triple containing it is consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\); if not, we zero out _X<sub>I</sub>_ (or _Y<sub>J</sub>_). We call the tensor after this step Thash.

The following claims, which are analogous to the claims in Section 5, still hold, and we omit their proofs to conciseness.


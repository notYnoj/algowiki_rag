\(.\mathbb{E}(S-S^{i_k})(S^{i_1,\dots,i_{k-1}}-S^{i_1,\dots,i_k})=2\mathbb{E}\left(SS^{i_1,\dots,i_{k-1}}-SS^{i_1,\dots,i_k}\right)\) (1.3)

Next, for all \(k\in\{1,\dots,n\}\), let \(\Delta_kS:=S-S^k\), and for \(k\neq\ell\), let \(\Delta_{k,\ell} S:=\Delta_k(\Delta_\ell S)=S-S^k-S^\ell+S^{k,\ell}\) (note the commutativity property: \(\Delta_k(\Delta_\ell S)=\Delta_\ell(\Delta_kS)\)). Iterating this process, let \(\Delta_{i_1,\dots,i_k}S:=\Delta_k(\Delta_{i_1,\dots,i_{k-1}}S)\). Using this notation, we have

\(B_k=\mathbb{E}\frac{1}{2n!}\sum_{i\in\mathfrak{S}_n}(\Delta_{i_k}S)(\Delta_{i_k}S)^{i_1,\dots,i_{k-1}},\) (1.4)

and so \(B_k\ge 0\) since if \(U,U'\) and _V_ are independent with _U_ and \(U'\) identically distributed, then for any function _F_ such that _F(U,V_) is integrable, \(\mathbb{E}\left(F(U,V)F(U',V)\right)=\mathbb{E}\left(\mathbb{E}\left(F(U,V)|V\right)^2\right)\ge 0\). We are now ready to generalize the approach used to go from (1.1) to (1.4), leading to novel properties of the \(B'_ks\).

**Lemma 1.1.** _Let_ \(\alpha\neq\emptyset\) _and_ \(\beta\) _be two disjoint subsets of_ {1_,...,n}. Then,_

\(\mathbb{E}\left(S(\Delta_\alpha S)^\beta\right)=\frac{1}{2^{|\alpha|}}\mathbb{E}\left(\Delta_\alpha S(\Delta_\alpha S)^\beta\right).\) (1.5)

_Proof._ First, if \(\beta=\emptyset\), then the above identity reduces to (1.3). Next, by a straightforward induction on the cardinality \(k:=|\alpha|\), note that \(\Delta_\alpha S=\sum_{\alpha^\prime\subset\alpha}(-1)^{|\alpha^\prime|}S^{\alpha^\prime}\). Then, for any \(\alpha'\subset\alpha\),<tbc>

\((-1)^{|\alpha^\prime|}S^{\alpha^\prime}(\Delta_\alpha S)^\beta=\sum_{\alpha^{\prime\prime}\subset\alpha}(-1)^{|\alpha^\prime|+|\alpha^{\prime\prime}|}S^{\alpha^\prime} S^{\alpha^{\prime\prime}\cup\beta},\)

<tbc>and so using (1.2) (\(\alpha\) and \(\beta\) are disjoint and \(\alpha'\subset\alpha\) so \(\alpha'\Delta(\alpha\cup\beta)=(\alpha'\Delta\alpha)\cup\beta\)),<tbc>

\(\mathbb{E}\left((-1)^{|\alpha^\prime|}S^{\alpha^\prime}(\Delta_\alpha S)^\beta\right)=\mathbb{E}\left(\sum_{\alpha^{\prime\prime}\subset\alpha}(-1)^{|\alpha^\prime|+|\alpha^{\prime\prime}|}SS^{(\alpha^\prime\Delta_\alpha^{\prime\prime})\cup\beta}\right).\)

<tbc>Since \(\alpha''\mapsto\alpha'\Delta\alpha''\) is just a permutation of the subsets of \(\alpha\) and \((-1)^{\alpha^\prime\Delta_\alpha^{\prime\prime}}=(-1)^{|\alpha^\prime|+|\alpha^{\prime\prime}|}\),<tbc>

\(\mathbb{E}\left((-1)^{|\alpha^\prime|}S^{\alpha^\prime}(\Delta_\alpha S)^\beta\right)=\mathbb{E}\left(\sum_{\alpha^{\prime\prime}\subset\alpha}(-1)^{|\alpha^{\prime\prime}|}SS^{\alpha^{\prime\prime}\cup\beta}\right)=\mathbb{E}\left(S(\Delta_\alpha S)^\beta\right),\)

<tbc>and so

\(\frac{1}{2^{|\alpha|}}\mathbb{E}\left(\Delta_\alpha S(\Delta_\alpha S)^\beta\right)=\frac{1}{2^{|\alpha|}}\sum_{\alpha^\prime\subset\alpha}\mathbb{E}\left((-1)^{|\alpha^\prime|}S^{\alpha^\prime}(\Delta_\alpha S)^\beta\right)=\mathbb{E}\left(S(\Delta_\alpha S)^\beta\right).\)

Let _T_ be the forward shift operator, i.e., for \(k\in\{1,\dots,n-1\}\), let _TB<sub>k</sub>_:=_B_<sub>_k_+1</sub> and let _D_ be the backward discrete derivative: _D_:=_Id-T_ (so for \(k\in\{1,\dots,n-1\}\), _DB<sub>k</sub>=B<sub>k</sub>-B_<sub>_k_+1</sub>), and denote by \(D^\ell\) (\(\ell\ge 1\)) its \(\ell\)-th iteration, with _D_<sup>0</sup>=_Id_. It is known (see \[2\]) that the finite sequence \((B_k)_{1\le k\le n}\) is non-increasing. More can be said.

**Theorem 1.2.** _For all_ \(\ell\in\{0,\dots,n-1\}\) _and_ \(k\in\{1,\dots,n-\ell\}\),

\(D^\ell B_k=\mathbb{E}\frac{1}{2^{\ell+1}n!}\sum_{i\in\mathfrak{S}_n}(\Delta_{i_1,\dots,i_{\ell+1}}S)(\Delta_{i_1,\dots,i_{\ell+1}}S)^{i_{\ell+2},\dots,i_{k+\ell}}.\) (1.6)

_In particular,_ \(D^\ell B_k\ge 0\)_, i.e.,_ \((B_k)_{1\le k\le n}\) _is completely monotone (recall that D=Id-T)._

_Proof._ With the previous lemma, it is enough to prove that for all \(\ell\in\{0,\dots,n-1\}\) and \(k\in\{1,\dots,n-\ell\}\),<tbc>

\(D^\ell B_k=\mathbb{E}\frac{1}{n!}\sum_{i\in\mathfrak{S}_n}S(\Delta_{i_1,\dots,i_{\ell+1}}S)^{i_{\ell+2},\dots,i_{k+\ell}}.\) (1.7)


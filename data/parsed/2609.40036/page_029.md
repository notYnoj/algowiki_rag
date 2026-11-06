the pair {_u,v_} is \(\ell\)-threatened for some \(\ell\le g-2\) (see the proof of \[LS20, Lemma 2.11\] and the preceding discussion). Applying \[LS20, Claim 2.12(c)\],

\(|W_t\backslash\mathscr{A}_t(v)|\le\sum_{\ell=1}^{g-2}T_\ell(v)\le log^{O(1)}(n)\sum_{\ell=1}^{g-2}L(\ell,t_j),\) (105)

where

\(L(\ell,t)=max\left\{1,\frac{(k-1)^\ell(n-2t)}{n^{c_0+\epsilon}}\right\}\le 1+\frac{(k-1)^\ell(n-2t)}{n^{c_0+\epsilon}}.\) (106)

Using \(\sum_{\ell=1}^{g-2}(k-1)^\ell=O((k-1)^g)=O(n^{c_0})\) and _n_-2_t<sub>j</sub>_=|_W<sub>t<sub>j</sub></sub>_|, the bound (105) becomes

\(|W_t\backslash\mathscr{A}_t(v)|\le\left(1+\frac{|W_{t_j}|}{n^\epsilon}\right)log^{O(1)}(n).\) (107)

We derive two consequences from this bound. First, note that

\(|W_t|\ge|W_{t_{j+1}}|=|W_{t_j}|n^{-\alpha}-O(1)\) (108)

and

\(|W_t\backslash\mathscr{A}_t(v)|\le O\left(|W_{t_j}|n^{-\epsilon} log^{O(1)}(n)\right)\) (109)

which implies that

\(|\mathscr{A}_t(v)|=|W_t|-|W_t\backslash\mathscr{A}_t(v)|\ge|W_{t_j}|n^{-\alpha}\left(1-O(n^{-(\epsilon-\alpha)}log^{O(1)}(n))\right)=|W_{t_j}|n^{-\alpha}(1-o(1))\) (110)

but \(|W_{t_j}|\ge|W_{t_{m-1}}|\ge n^\epsilon\), so

\(|\mathscr{A}_t(v)|\ge n^{\epsilon-\alpha}(1-o(1))>0\) (111)

and we conclude that, for sufficiently large _n_, the process does not freeze in the _j_th interval {_t<sub>j</sub>,...,t_<sub>_j_+1</sub>} w.h.p. Consequently,

\(|W_t|\ge|W_{t_{j+1}}|=n-2t_{j+1}=(n-2t_j)n^{-\alpha}-O(1)=|W_{t_j}|n^{-\alpha}-O(1)\) (112)

which leads to the second consequence of (107), namely

\(\frac{|W_t\backslash\mathscr{A}_t(v)|}{|W_t|-1}\le\frac{\left(1+\frac{|W_{t_j}|}{n^\epsilon}\right)log^{O(1)}(n)}{|W_{t_j}|n^{-\alpha}-O(1)}\le 2n^{-(\epsilon-\alpha)}log^{O(1)}(n)\le n^{-(\epsilon-2\alpha)}\le\zeta_n\) (113)

which implies that

\(d_{\mathscr{A}_t}(v)\ge(1-\zeta_n)\left(|W_t|-1\right)\) (114)

for all \(t\in\{t_j,\dots,t_{j+1}\}\) w.h.p. Moreover, by \[LS20, Lemma 2.11\], _G_<sub>_t_<sub>_j_+1</sub></sub> is _C_<sub>_j_+1</sub>-path-bounded w.h.p. for some constant _C_<sub>_j_+1</sub>.

Finally, by \[LS20, Definition 2.10(b)\] and \[LS20, Lemma 2.11\] we have

\(|B_{t_m}|\le\sum_{\ell=1}^{g-2}P_\ell(G_{t_m})\le|W_{t_m}|^2n^{c_0-1}log^{O(1)}(n).\) (115)

However, \(|W_{t_m}|\le n^\epsilon\), so |_B<sub>t<sub>m</sub></sub>_|=_o_(1). Since |_B<sub>t<sub>m</sub></sub>_| is a non-negative integer, \(B_{t_m}=\emptyset\) w.h.p., implying that _G<sub>t<sub>m</sub></sub>_ is safe in the sense of \[LS20, Definition 2.4\]. By \[LS20, Lemma 2.5\], _G<sub>t</sub>_ is safe for all _t\>t<sub>m</sub>_ and the process saturates. In particular, for any \(t\in\{t_m,\dots,n/2\}\) the graph _H<sub>t</sub>_ is complete w.h.p., which implies (99).

We have shown that (99) holds w.h.p. for each of the _m_+2=_O_(1) intervals. By a union bound it holds simultaneously for every time _t_ in the round and for every vertex \(v\in W_t\) w.h.p.


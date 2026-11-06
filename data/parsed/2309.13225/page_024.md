\(w^*=r(w,D_{\ell(w)})\). Suppose \(\mathrm{deg}(v)\ge\mathrm{deg}(u)\). Let _z=b(v,P_) be the blocking vertex so \(\mathrm{deg}(z)\ge s_5\) and \(z^*=r(z,D_{\ell(z)})\in D_5\). From _w_<sup>∗</sup>, since \(P\subset E_{\ell(w)}\),

\(\hat{\delta}(w^*,z^*)\le\delta(w,z)+2\)<br>
\(\hat{\delta}(w^*,v)\le\delta(w,v)+1\)

Since \(D_{\ell(w)}\subset D_2\), and \(2+5+6\le 13\), the path \((v,w^*,z^*,z)\circ P_{z,u}\) exists in _G_<sub>6_,v_</sub> (see Line 49 of Algorithm 4) and Dijkstra computes a +4 approximation.

For the remaining overview, assume \(k\ge 6\). We want to obtain a (2,0) approximation for paths of length at least _k_. Of course, it suffices to compute a +_k_ approximation. Let _P_ be a path. We will choose _l_ levels with degree thresholds _s_<sub>1</sub>_,s_<sub>2</sub>_,...,s_<sub>_l_-1</sub> (note that _s<sub>l</sub>_=0). In order to compute a +_k_ approximation, it suffices to have for all _w_ with \(\mathrm{deg}(w)\ge s_{l-\frac{k-4}{2}}\) and for all \(v\in V\) , an estimate

\(\hat{\delta}(w^*,v)\le\delta(w,v)+5\)

Then, following a similar argument to Lemma A.2, we obtain a +_k_ additive approximation at the _l_-th level. In order to guarantee a +5 error at the \((l-\frac{k-4}{2})\) level, we require the edge set \(D_{l_0}\times D_{l-\frac{k-2}{2}}\) for some choice of _l_<sub>0</sub>.

Suppose \(P\subset E_{l_0+1}\). Then, we run **BK2APASP**(_G_<sub>_l_<sub>0</sub>+1</sub>) and compute a (2,0) approximation on _P_. Otherwise, \(P\unknown\subset E_{l_0+1}\) so the maximum degree vertex \(z\in P\) has \(\mathrm{deg}(z)\ge s_{l_0}\) and there is some vertex \(z^*=r(z,D_{\ell(z)})\). Let _P<sub>w,v</sub>_ be the sub-path from _w_ to _v_ and let _y=b(w,P<sub>w,v</sub>_) be the blocking vertex so that \(\ell(y)\le l-\frac{k-2}{2}\) and there is \(y^*=r(y,D_{l-\frac{k-2}{2}})\). Since \(D_{\ell(z)}\subset D_{l_0}\) and \(P\subset E_{\ell(z)}\),

\(\hat{\delta}(w^*,z^*)\le\delta(w,z)+2\)<br>
\(\hat{\delta}(z^*,y^*)\le\delta(z,y)+2\)

If \(D_{l_0}\times D_{l-\frac{k-2}{2}}\subset G_{l-\frac{k-4}{2},w^*}\), the path \((w^*,z^*,y^*,y)\circ P_{y,v}\subset G_{l-\frac{k-4}{2},w^*}\) and Dijkstra computes an estimate at most,<tbc>

\(\hat{\delta}(w^*,v)\le\delta(w,v)+5\)

<tbc>The only restriction on _l_<sub>0</sub> therefore is that

\(l_0+\left(l-\frac{k-4}{2}\right)+\left(l-\frac{k-2}{2}\right)\le 2l+1\)

or

\(l_0\le k-2\)

which justifies our choice of _l_<sub>0</sub>=_k_-2. We then choose _l_ to optimize the running time trade-off between the executions of Dijkstra which requires time \(\tilde{O}(n^{2+1/l})\) and **BK2APASP** which requires time \(\tilde{O}\left(n^{1.5}s_{l_0}\right)=\tilde{O}\left(n^{1.5}s_{k-2}\right)=\tilde{O}\left(n^{2.5-\frac{k-2}{l}}\right)\).

## Algorithm

Our algorithm begins by initializing the distance estimates with the adjacency matrix and setting parameters _l_<sub>0</sub>_,l_. Next, Line 45 decomposes the graph with _l_-1 degree thresholds.

In Phase 1, at each level _j_, we compute Dijkstra from \(w\in D_j\) on the graph _G<sub>j,w</sub>_ in Line 50. The graph _G<sub>j,w</sub>_ consists of edge set \(E_j\cup E^*\cup(w\times V)\) and \(D_{j_1}\times D_{j_2}\) for all \(j+j_1+j_2\le 2l-1\).

Finally, we take the minimum between the estimate computed above and the estimate given by **BK2APASP** on the graph _G_<sub>_k_<sub>0</sub>+1</sub>=(_V,E_<sub>_k_<sub>0</sub>+1</sub>).


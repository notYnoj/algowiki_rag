**Algorithm 4** `LongMultiplicativeAPASP`(_G,k_)

**Input :** Unweighted, undirected graph _G_=(_V,E_) with _n_ vertices; even integer _k_

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\) for all \(u,v\in V\) and \(\hat{\delta}(u,v)\le 2\delta(u,v)\) whenever \(\delta(u,v)\ge k\)

40 Phase 0: Set up and Decompose Graph

41 \(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)

42 \(l\leftarrow 2(k-1)\)

43 \(l_0\leftarrow k-2\)

44 \(s_i\leftarrow n^{1-\frac{i}{i}}\) for all \(1\le i\le l-1\)

45 \((D_1,D_2,\dots,D_l),(E_1,E_2,\dots,E_l),E^*\leftarrow\text{\textbf{Decompose}}(G,(s_1,s_2,\dots,s_{l-1}))\)

46 Phase 1: Compute Distance Estimates on High Degree Paths

47 for \(1\le j\le l\) do

48 for \(w\in D_j\) do

49 \(G_{j,w}\leftarrow\left(V,E_j\cup\left(\bigcup_{j+j_1+j_2\le 2l+1}D_{j_1}\times D_{j_2}\right)\cup E^*\cup(w\times V)\right)\)

50 \(\hat{\delta}\leftarrow\text{\textbf{Dijkstra}}(G_{j,w},w,\hat{\delta})\)

51 \(\hat{\delta}\leftarrow\mathrm{min}\left(\hat{\delta},\text{\textbf{BK2APASP}}(G_{l_0+1})\right)\) where \(G_{l_0+1}\leftarrow(V,E_{l_0+1})\)

## Warm-Up: _k_=4

We first show that we can obtain a \(\tilde{O}(n^{13/6})\) algorithm for computing (2,0) approximation for paths of length at least 4.

_Proof._ Since _k_=4, we have _l_=6 and _l_<sub>0</sub>=2. We decompose the graph with degree thresholds _s_<sub>1</sub>=_n_<sup>5/6</sup>_,s_<sub>2</sub>=_n_<sup>4/6</sup>_,...,s_<sub>5</sub>=_n_<sup>1/6</sup>.

We execute **BK2APASP** on _G_<sub>3</sub>=(_V,E_<sub>3</sub>). Therefore, if \(P\subset E_3\), we obtain a (2,0) approximation via **BK2APASP**.

Otherwise, \(P\unknown\subset E_3\). In this case, we claim to compute a +4 approximation, which implies a (2,0) approximation for \(\delta(u,v)\ge 4\). The vertex \(w\in P\) of maximum degree has \(\mathrm{deg}(w)\ge s_2\) and is dominated by \(w^*=r(w,D_{\ell(w)})\).

Without loss of generality, suppose \(\mathrm{deg}(v)\ge\mathrm{deg}(u)\). Let _z=b(v,P_) be the blocking vertex from _v_. Since \(P\unknown\subset E_3\), \(z\neq u\) and \(\mathrm{deg}(z)\ge s_5\).

If _w=z_ then since \(P\subset E_{\ell(w)}\), _B(P_)={_u,v,w_} (Definition 3.4) and we obtain a +4 approximation. In particular,<tbc>

\(\hat{\delta}_{\ell(w)}(w^*,v)\le\delta(w,v)+1\)

<tbc>where \(w^*=r(w,D_{\ell(w)})\). If \(\ell(v)=6\), then,<tbc>

\(\hat{\delta}(v,u)\le\hat{\delta}_{\ell(w)}(v,w^*)+1+\delta(w,u)\le\delta(u,v)+2\)

<tbc>Otherwise, if \(v^*=r(v,D_{\ell(v)})\),

\(\hat{\delta}_{\ell(v)}(v^*,u)\le\hat{\delta}_{\ell(w)}(v^*,w^*)+1+\delta(w,u)\le\delta(v,u)+3\)

Of course, this implies a +4 approximation when executing **Dijkstra** on _G_<sub>6_,u_</sub> by taking the path (_u,v_<sup>∗</sup>_,v_).

Therefore, \(w\neq z\). From _w_<sup>∗</sup>, since \(P\subset E_{\ell(w)}\),<tbc>

\(\hat{\delta}(w^*,z^*)\le\delta(w,z)+2\)


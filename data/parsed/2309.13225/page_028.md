## High Level Overview

We begin by showing that we can obtain a (2,0) approximation for \(\delta(u,v)\ge 4\) in time \(\tilde{O}(n^{2.01973523})\). Set parameters _x_=0.51973523_,M_=35 and _l_=29 so that _l_<sub>0</sub>=2. Decompose the graph with degree thresholds _s_<sub>2</sub>=_n<sup>x</sup>,s_<sub>3</sub>=_n_<sup>26_x/_27</sup>_,...,s_<sub>28</sub>=_n<sup>x/_27</sup>. Let _P_ be a shortest path of length at least 4. If \(P\subset E_3\), then we execute **BK2APASP**(_G_<sub>3</sub>) in time _n_<sup>1.5+_x_</sup>=_n_<sup>2.01973523</sup> where _G_<sub>3</sub>=(_V,E_<sub>3</sub>) has maximum degree _s_<sub>2</sub>=_n<sup>x</sup>_. If \(\delta(u,v)\ge M\), then **DenseAPASP** computes a +_M_ approximation and we obtain a (2,0) approximation. Otherwise, \(P\unknown\subset E_3\) is of length at most _M_ and vertex \(w\in P\) of maximum degree has \(\mathrm{deg}(w)\ge s_2\). Suppose \(\mathrm{deg}(v)\ge\mathrm{deg}(u)\). Let _z=b(v,P_) be the blocking vertex so \(\mathrm{deg}(z)\ge s_{28}\) and \(z^*=r(z,D_{\ell(z)})\in D_{28}\). Let \(\frac{n}{2^i}\le\mathrm{deg}(w)\le\frac{n}{2^{i-1}}\). Since \(P\subset F_i\), we obtain the estimates from _w_<sup>∗</sup>,<tbc>

\(\hat{\delta}(w^*,z^*)\le\delta(w,z)+2\le M+2\)<br>
\(\hat{\delta}(w^*,v)\le\delta(w,v)+1\le M+1\)

<tbc>Then, the bounded (min,+) product computes,

\(\hat{\delta}(v,z^*)\le\delta(v,z)+3\)

as \(v\in V,z^*\in D_{28},w^*\in C_i\). Finally, the path \((v,z^*,z)\circ P_{z,u}\) exists in _G_<sub>6_,v_</sub> and **Dijkstra** computes a +4 approximation.

For the remaining overview, assume \(k\ge 6\). In Algorithm 4, we obtained a +5 approximation after the \(\left(l-\frac{k-4}{2}\right)\) iteration by including edge sets \(D_i\times D_{l-\frac{k-2}{2}}\) for all \(i\le l_0\) in the edges of \(G_{l-\frac{k-4}{2}},w\) for \(w\in D_{l-\frac{k-4}{2}}\) . Using fast matrix multiplication, we will pre-compute the distances obtained from these edges and instead encode them in smaller edge set \(w\times V\) .

Consider a shortest path _P_. If \(P\subset E_{l_0+1}\), then we again invoke **BK2APASP** to compute a (2,0) approximation. Therefore, suppose \(P\unknown\subset E_{l_0+1}\). For a large enough constant _M_, we can invoke **DenseAPASP**(_G,M_) (Lemma 3.2) or **AdaptiveAPASP** (Theorem 5.6) to compute a +_M_ approximation without affecting the overall running time. Therefore, we can also assume that \(\delta(u,v)\le M\).

We decompose the graph _G_ into (1-_x_)log_n_ levels with each degree threshold defined as \(t_i=\frac{n}{2^i}\). We compute dominating sets _C<sub>i</sub>_ of size \(\tilde{O}(n/t_i)\) and edge sets _F<sub>i</sub>_ of size at most _O(nt_<sub>_i_-1</sub>)=_O(nt<sub>i</sub>_). Again, to obtain a +_k_ additive approximation, it suffices to have a +5 approximation after the \(l-\frac{k-4}{2}\) iteration of computing **Dijkstra**. Consider the blocking vertices _B(P_)={_x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>t</sub>_} (Definition 3.4). Let _a_ be the minimum index such that \(\ell(x_a)\le l-\frac{k-4}{2}\) so that \(\ell(x_{a+1})\le l-\frac{k-2}{2}\) and \(\ell(x_t)\le l_0\) as we have \(P\unknown\subset E_{k_0+1}\). Then, if \(\frac{n}{2^{i^*}}\le\mathrm{deg}(x_t)\le\frac{n}{2^{i^*-1}}\), we have \(P\subset F_{i^*}\) and in the _i_<sup>∗</sup>-th call to **DominatingSetAPASP**,

\(\hat{\delta}(x_t^*,x_a^*)\le\delta(x_t,x_a)+2\)<br>
\(\hat{\delta}(x_t^*,x_{a+1}^*)\le\delta(x_t,x_{a+1})+2\)

By our assumption \(\delta(u,v)\le M\) both entries in the matrices constructed by **DominatingSetAPASP** are finite. Furthermore, \(x_t\in P_{x_a,x_{a+1}}\) (Lemma A.1) so the bounded (min,+) product computes,<tbc>

\(\hat{\delta}(x_a^*,x_{a+1}^*)\le\delta(x_a,x_{a+1})+4\)

<tbc>Then, in the graph \(G_{\ell(x_a),x_a^*}\) there exists the path \((x_a^*,x_{a+1}^*,x_{a+1})\circ P_{x_{a+1},x_{a-1}}\) and we obtain an estimate at most,<tbc>

\(\hat{\delta}(x_a^*,x_{a-1}^*)\le\delta(x_a,x_{a-1})+5\)


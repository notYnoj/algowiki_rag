For any integer \(k\ge 1\), let _h(P,k_) denote the weight of the _k_-th heaviest edge in _P_ and <o>_h_</o>(_P,k_) denote the sum of the weights of the _k_ heaviest edges in _P_. We analogously define _w<sub>u,v</sub>(k_)=min_<sub>P</sub><o>h</o>(P,k_) over shortest paths _P_ between _u,v_.

Using combinatorial methods, Cohen and Zwick \[CZ01\] gave a _O(n_<sup>7/3</sup>) algorithm for +2_w<sub>u,v</sub>_ approximation. They in fact prove a stronger result and gain a (7/3,0) multiplicative approximation. With Fast Matrix Multiplication, Berman and Kasiviswanathan \[BK07\] gave a \((1+\varepsilon,2w_{u,v})\) algorithm in time _O(n_<sup>2.25</sup>). In this work, we use our techniques to improve upon their algorithm and design a \((1+\varepsilon,2w_{u,v})\) algorithm with running time roughly \(\tilde{O}(n^{2.152})\).

**Theorem 6.2.** _Let_ \(\varepsilon>0\)_. Let G be an undirected, weighted graph with n vertices and weight function_ \(w:E\rightarrow\mathbb{R}^+\)_. Algorithm 8 computes_ \(\hat{\delta}\) _in time,_

\(\tilde{O}\left(\frac{n^{2.15195331}}{\varepsilon}\right)\)

_such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\le(1+\varepsilon)\delta(u,v)+2w_{u,v}\).

Throughout, we use the approximate (min,+) product of Bringmann et al. \[BKW19\].

**Theorem B.12.** _Let A,B be two integer_ \(n\times n\) _matrices with non-negative entries. Let_ \(\varepsilon>0\)_. There is an algorithm `ApproximateMinPlus` that returns C in time_ \(\tilde{O}\left(n^\omega/\varepsilon\right)\) _such that for all_ \(1\le i,j\le n\),

\((A*B)_{ij}\le C_{ij}\le(1+\varepsilon)(A*B)_{ij}\)

We provide the proof in Appendix B.2 for completeness.

## High Level Overview

Let _x_ be a parameter to be set later. Let _s_<sub>1</sub>=_n<sup>x</sup>_ and _s_<sub>2</sub>=_n_<sup>_x/_2</sup> and \(D_1\subset D_2\subset D_3=V\) and \(E_3\subset E_2\subset E_1=E\) be the output of `WeightedDecompose`. There are 3 cases to consider. Let _P_ be a shortest path between _u,v_. If \(P\subset E_3\), then we compute an exact distance from _u_ in the graph \(G\subset G_{3,u}\).

Suppose \(P\subset E_2\) but \(P\unknown\subset E_3\). Let _e_=(_a,b_) be the closest edge to _u_ such that \(e\notin E_3\) and let _a_ be the vertex closer to _u_ so that \(P_{a,u}\subset E_3\). Then, \(\mathrm{deg}(a)\ge s_2\) so there is _a_<sup>∗</sup>=_r(a,D_<sub>2</sub>) such that rank_<sub>a</sub>(a_<sup>∗</sup>)_\<s_<sub>2</sub>. Since \(P\subset E_2\), \(\hat{\delta}(a^*,v)\le\mathfrak{wt}(a^*,a)+\delta(a,v)\). Then, \((v,a^*,a)\circ P_{a,u}\subset G_{3,v}\) so `Dijkstra` computes an estimate,

\(\hat{\delta}(v,u)\le\hat{\delta}(v,a^*)+\mathfrak{wt}(a^*,a)+\delta(a,u)\le\delta(v,u)+2\mathfrak{wt}(a^*,a)\le\delta(v,u)+2\mathfrak{wt}(a,b)\le\delta(v,u)+2w_{u,v}\)

as \(\mathrm{rank}_a(a^*)<s_2\le\mathrm{rank}_a(b)\).

Finally, suppose \(P\unknown\subset E_2\). Let \(P\subset F_i\) and \(P\unknown\subset F_{i+1}\). Let \(e=(a,b)\in F_i\backslash F_{i+1}\). Since \(P\subset F_i\),

\(\hat{\delta}(a^*,u)\le\mathfrak{wt}(a^*,a)+\delta(a,u)\)<br>
\(\hat{\delta}(a^*,v)\le\mathfrak{wt}(a^*,a)+\delta(a,v)\)

Then, from the `ApproximateMinPlus` product,

\(\hat{\delta}(u,v)\le\left(1+\frac{\varepsilon}{3}\right)(\delta(u,v)+\mathfrak{wt}(a^*,a))\le\left(1+\frac{\varepsilon}{3}\right)(\delta(u,v)+2\mathfrak{wt}(a,b))\le(1+\varepsilon)\delta(u,v)+2w_{u,v}\)

where \(\mathrm{rank}_a(a^*)<t_j<t_{j-1}\le\mathrm{rank}_a(b)\).


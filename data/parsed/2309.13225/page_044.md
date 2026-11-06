**Warm-Up:** \(\beta=4\)

We begin by showing a proof of correctness for the case of \(\beta=4\). The proof is almost identical to Lemma 5.9.

**Lemma 5.15.** _Algorithm **Bounded AdditiveAPASP**(G,_4_,C_) _returns an estimate_ \(\hat{\delta}\) _satisfying:_

1. \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all u,v_<tbc>

_2._ \(\hat{\delta}(u,v)\le\delta(u,v)+4\) _for all_ \(\delta(u,v)\le C\)

_Proof._ Let _P_ be a shortest path between _u,v_. Note that _k_=5_,k_<sub>0</sub>=2.

Suppose \(P\subset E_3=E_{k_0+1}\). Then, \(L(P,5)\subset\{3,4\}\) and \(|L(P,5)|\le 2\). By Lemma A.3, since _D_<sub>5</sub>=_D<sub>k</sub>=V_ , we obtain a +4 approximation in Phase 2.

Thus, _P_ has some vertex with degree at least _s_<sub>2</sub>=_n<sup>x</sup>_. Let _y_ denote the vertex in _P_ with degree at least _s_<sub>4</sub> closest to _v_. Let _z_ be a vertex of maximum degree on _P_ and _i_<sup>∗</sup> be the integer \(1\le i\le l\) such that \(\frac{n}{2^{i^*}}\le deg(z)<\frac{n}{2^{i^*-1}}\). Since \(P\subset F_{i^*}\), we have in the _i_<sup>∗</sup>-th iteration of Phase 1 that \(X_{i^*}(z^*,u)\le\delta(z,u)+1\le C+1\) and \(X_{i^*}(z^*,y^*)\le\delta(z,y)+2\le C+2\) where _z_<sup>∗</sup>=_r(z,C_<sub>_i_<sup>∗</sup></sub>), _y_<sup>∗</sup>=_r(y,D_<sub>4</sub>). Therefore, since the entries in _A_<sub>_i_<sup>∗</sup></sub>_,B_<sub>_i_<sup>∗</sup></sub> are finite, we compute in Line 110,<tbc>

\(\hat{\delta}_{i^*}(u,y^*)\le X_{i^*}(u,z^*)+X_{i^*}(z^*,y^*)\le\delta(u,z)+\delta(z,y)+3=\delta(u,y)+3\)

<tbc>Now, in the 5-th iteration in Phase 2, when we execute Dijkstra from _u_, we have an edge (_u,y_<sup>∗</sup>) with weight at most \(\delta(u,y)+3\), an edge \((y^*,y)\in E\) and the remaining edges in _E_<sub>5</sub>=_E<sub>k</sub>_, so that,

\(\hat{\delta}(u,v)\le\hat{\delta}_{i^*}(u,y^*)+1+\delta(y,v)\le\delta(u,y)+\delta(y,v)+4\le\delta(u,v)+4\)


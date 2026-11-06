## High Level Overview

To illustrate our algorithm, we walk through an overview of how to compute a +4 approximation for paths of length at most 5. For a +4 approximation, the **DenseAPASP** algorithm decomposes graph _G_ into 5 levels. Instead, we will show that we can decompose the graph _G_ into 7 levels. Thus, define thresholds _s_<sub>1</sub>=_n_<sup>6/7</sup>_,s_<sub>2</sub>=_n_<sup>5/7</sup>_,...,s_<sub>6</sub>=_n_<sup>1/7</sup>. As length 5 paths are the most challenging to handle, let _u,v_ be vertices and _P_ a shortest path of length at exactly 5. If _P_ has a vertex of degree at least _s_<sub>2</sub>, since 2+6+7=15=2∗7+1, we may include the edge sets \(\bigcup_{i=1}^2D_i\times D_6=\tilde{O}(|E_9|)\). we can include these edges and obtain a +4 approximation following similar arguments to **DenseAPASP** (Figure 1).

Thus, let us assume \(P\subset E_3\). If \(P\subset E_5\), then the blocking levels \(L(P,7)\subset\{5,6\}\) (Definition 3.4) so that we can obtain a +4 approximation via Lemma A.3. Then, assume \(P\unknown\subset E_5\), so _P_ has some edge in _E<sub>j</sub>_\\_E_<sub>_j_+1</sub> for \(j\in\{3,4\}\). Denote the length 5 path _P_=(_u,u_<sub>2</sub>_,u_<sub>3</sub>_,v_<sub>3</sub>_,v_<sub>2</sub>_,v_).

We will argue that if \(\ell(u_2)\le 4\), then we obtain a good additive approximation. Suppose \(|N(u,2)|\ge s_3\), so that from \(p(u,D_3)\in N(u,2)\) (Definition E.2) we compute an exact distance \(\hat{\delta}(p(u,D_3),v)=\delta(p(u,D_3),v)\le\delta(u,v)+2\). When we add 2, we obtain a +4 approximation. Figure 7 gives an illustration

**ShortAdaptiveAPASP** (Algorithm 15) samples each dominating set _D<sub>i</sub>_ randomly with the algorithm `rDominate`, rather than following the greedy deterministic construction of `Dominate`. With high probability, if \(|N(u,2)|\le s_3\), then \(|C(u,3)|=|N(u,2)\cap D_4|=\tilde{O}(s_6)\) and if \(\ell(u_2)\le 4\), then Lemma A.3 guarantees that \(\hat{\delta}(u_2^*,v)\le\delta(u_2,v)+3=\delta(u,v)+2\). We efficiently iterate over _C(u,_3) and update \(\hat{\delta}(u,v)\le 2+min_{w\in C(u,3)}\hat{\delta}(w,v)\) to obtain a +4 approximation. Figure 8 gives an illustration.

We can compute the sets _X(u,i),C(u,i_) efficiently as we will terminate our **BFS** whenever _s<sub>i</sub>_ distinct vertices are encountered, which requires time at most \(s_i^2\le s_3^2=\tilde{O}(n^{8/7})\).

Then, we can assume deg(_u_<sub>2</sub>),deg(_v_<sub>2</sub>)_\<s_<sub>4</sub>. In particular, only one edge (_u_<sub>3</sub>_,v_<sub>3</sub>) is not in _E_<sub>5</sub>. We now execute **Dijkstra** from every vertex \(w\in D_j\) on graph _G<sub>i,w</sub>_ containing (at least) the edges \(E_j\cup E^*\cup(w\times V)\).

Since only one edge is not in _E_<sub>5</sub>, the blocking levels of _P_ (Definition 3.4), _L<sub>B</sub>(P_) cannot contain both {3,4}. If the blocking levels _L<sub>B</sub>(P_) do not contain every level from {5,6}, then we obtain a<tbc>

p(u,D3)
u
v

Figure 7: Estimate when \(|N(u,2)|\ge s_3\). Solid lines denote edges and dotted lines denote paths in _G_. Black dashed arrows denote computed distances estimates. Blue solid arrows denote a constant additive term.


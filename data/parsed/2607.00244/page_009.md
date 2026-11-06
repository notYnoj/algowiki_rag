image of every satisfiable 3-SAT-_B_ instance is 3-colorable, whereas in every (improper) 3-coloring of the image _H_ of any 3-SAT-_B_ instance \(\varphi\) such that \(val(\varphi)\le\beta'm\) at most a \(\beta''\) fraction of the edges are properly colored (i.e., bichromatic) where \(\beta'':=\frac{\beta'+7}{8}\) . We observe that \(\beta''<1\), since \(\beta'<1\), and choose \(\beta:=1-\frac{1-\beta''}{2\Delta}<1\). Let _n_:=|_V(H_)|.

Assume that there is a 3-colorable induced subgraph of _H_ with at least \(\beta n\) vertices. Any extension to a complete 3-coloring of _H_ improperly colors at most \((1-\beta)\Delta n<(1-\beta'')n\) edges, because _H_ has maximum degree at most \(\Delta\). Here we observe that the reduction in [5] satisfies that \(|V(H)|\le|E(H)|\). Thus we reach the contradiction that more than a \(\beta''\) fraction of the edges of _H_ are properly colored.

This way, the two items of the current theorem correspond to the two outcomes of Theorem 7. We conclude by taking the same value for _c_ as in Theorem 7 since the blow-up \(\kappa\) is constant. \(\blacktriangleleft\)

We now adapt Theorem 8. For that, we modify the subdivisions slightly without changing their twin-width upper bound of 4. One should also notice the hybrid nature of the last two items: in "positive" instances, we preserve a low _chromatic number_, whereas in "negative" instances, we upper-bound the _independence number_ of the produced graphs.

\(\blacktriangleright\) **Theorem 13.** _There is an_ \(\mathcal{O}(\|G\|)\)_-time algorithm that, given an n-vertex m-edge graph H, outputs a graph G_:=_G<sub>H</sub> of twin-width at most 4 such that_

\(|V(G)|=3n+(3n+3m)\cdot 3\lceil log(3n)\rceil\);

_if H is 3-colorable, then G is 3-colorable;_

_for any number p, if no induced subgraph of H on at least p vertices is 3-colorable, then_

\(\alpha(G)\le p+(3n+3m)\cdot\lceil log(3n)\rceil.\)

_Furthermore, a 4-sequence of G can be computed in_ \(\mathcal{O}(\|G\|)\) _time._

**Proof.** We first turn every vertex _v_ of _H_ into a triangle (_v,_1)(_v,_2)(_v,_3). For every \(uv\in E(H)\), we add the three edges (_u,_1)(_v,_1), (_u,_2)(_v,_2), (_u,_3)(_v,_3). So far, we get a graph _J_ with 3_n_ vertices and 3_n_+3_m_ edges.

To obtain _G_, we _s_-subdivide every edge _e_ of _J_, for \(s:=2\lceil log(3n)\rceil\). We arbitrarily orient _e=uv_, say, from _u_ to _v_, and we add a true twin to each odd-indexed vertex on the new path between _u_ and _v: u(uv_)<sub>1</sub>(_uv_)<sub>2</sub>(_uv_)<sub>3</sub>_...(uv)<sub>s</sub>v_. (Note that this "triangle-subdivision" was already used in a similar context in [8].) That concludes the construction of _G_.

From this description, one can build _G_ in time proportional to its size. One can then observe that \(|V(G)|=3n+(3n+3m)\cdot 3\lceil log(3n)\rceil\). Indeed we add \(\lceil log(3n)\rceil\) true twins per subdivided edge of _J_. The \(\mathcal{O}(\|G\|)\)-time algorithm to compute a 4-sequence of _G_ follows the same argument as in the proof of Theorem 8 after contracting every pair of true twins. The latter has the same effect as removing the added true twins (without creating any red edges at this point).

Let us show that \(\chi(H)\le 3\) implies that \(\chi(G)\le 3\). Let \(\mu:V(H)\rightarrow[3]\) be a proper 3-coloring of _H_. We define \(\nu':V(J)\rightarrow[3]\) by \(\nu'(u,i):=(\mu(u)+i)mod3+1\). This is a proper coloring of _J_: each triangle (_u,_1)(_u,_2)(_u,_3) has all three colors, and a monochromatic edge (_u,i_)(_v,i_) under \(\nu'\) would imply that _uv_ is monochromatic under \(\mu\). To extend \(\nu':V(J)\rightarrow[3]\) to a proper coloring \(\nu:V(G)\rightarrow[3]\) of _G_, give the color \(\nu'(u)\) to every even-indexed vertex on the path: _u(uv_)<sub>1</sub>(_uv_)<sub>2</sub>(_uv_)<sub>3</sub>_...(uv)<sub>s</sub>v_ (when _uv_ was oriented from _u_ to _v_). Finally, we assign the two remaining colors (the ones not already in their neighborhood) to each pair of true twins.

We move to the last item of the statement. First note that the set _T<sub>uv</sub>_ of \(3\lceil log(3n)\rceil\) new vertices introduced for each edge \(uv\in E(J)\) can be vertex-partitioned into \(\lceil log(3n)\rceil\)


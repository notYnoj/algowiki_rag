**Theorem 18.** _Let_ C _be a (hereditary) class of versatile symmetric difference of exponent_ \(\alpha\)_. There is an_ \(\mathcal{O}_\mathcal{C}(n^{2+\alpha})\)_-time algorithm that, given an n-vertex graph of_ C_, outputs an sd-degeneracy sequence of G of width_ \(\mathcal{O}_\mathcal{C}(n^\alpha)\).

_Proof._ Let _d_:=_d_<sub>C</sub>_\>_0 be such that for every _n_-vertex graph \(G\in\mathcal{C}\), there are \(\lfloor n/d\rfloor\) disjoint pairs of vertices _u,v_ satisfying \(\mathrm{sd}_G(u,v)\le dn^\alpha\). We initialize an sd-degeneracy sequence S of _G_ of width \(dn^\alpha\) to the empty list. We also set _G_<sub>1</sub>:=_G_ and _n_<sub>1</sub>:=_n_.

While the remaining graph _G<sub>i</sub>_ has \(n_i\ge d\) vertices, we do the following.

By Corollary 17, we list all the pairs of \(dn^\alpha\)-near-twins of _G<sub>i</sub>_ in \(\mathcal{O}(dn^\alpha n_i^2)\) time. We then greedily build a list {_u_<sub>1</sub>_,v_<sub>1</sub>}_,...,{u<sub>h</sub>,v<sub>h</sub>_} of \(\mathrm{max}(1,\lfloor\frac{1}{2}\lfloor n_i/d\rfloor)\) _disjoint_ pairs of \(dn^\alpha\)-near-twins of _G<sub>i</sub>_ in O(_n<sub>i</sub>_) time. (Indeed, if one fixes a set _D_ disjoint pairs, then the choice of any other pair consumes at most two pairs of _D._) We append this list to S. We then set _G_<sub>_i_+1</sub>:=_G<sub>i</sub>_-{_u_<sub>1</sub>_,...,u<sub>h</sub>_} and _n_<sub>_i_+1</sub>:=|_V(G_<sub>_i_+1</sub>)|. This finishes the body of the while loop.

When we exit the while loop, we finish the sd-degeneracy sequence arbitrarily.

**Correctness.** If the algorithm terminates, it does output an sd-degeneracy sequence of _G_ of width \(dn^\alpha\) since we only append to S pairs of \(dn^\alpha\)-near-twins in the current graph, and remove their first elements in batches of disjoint pairs.

**Time.** At every loop iteration, we add at least one pair to the sequence and remove their first elements from the graph. Thus, the algorithm does terminate, and goes through the successive induced subgraphs of _G_: _G_<sub>1</sub>_,G_<sub>2</sub>_,...,G<sub>p</sub>_ with \(p\le n\). Let \(c:=1-\frac{1}{4d}\).

**Claim 19.** _For every_ \(i\in[p-1]\), \(n_{i+1}\le cn_i\).

_Proof._ Indeed, if _n<sub>i</sub>\<_4_d_, then \(n_{i+1}\le cn_i\) since \(n_{i+1}\le n_i-1\) (we remove at least one vertex of _G<sub>i</sub>_ to form _G_<sub>_i_+1</sub>). If instead, \(n_i\ge 4d\), we conclude because \(\mathrm{max}(1,\lfloor\frac{1}{2}\lfloor n_i/d\rfloor)=\lfloor\frac{1}{2}\lfloor n_i/d\rfloor\unknown\frac{1}{4d}\cdot n_i\).

By Claim 19, for every \(i\in[p]\), \(n_i\le c^{i-1}n\). So the overall running time is

\(\sum_{i\in[p]}\mathcal{O}(dn^\alpha n_i^2)\le\mathcal{O}(dn^\alpha)\cdot n^2\sum_{i\in[p]}c^{2i-2}\le\frac{1}{1-c}\cdot\mathcal{O}_\mathcal{C}(n^{2+\alpha})=\mathcal{O}_\mathcal{C}(n^{2+\alpha}),\)

and we conclude.

Theorem 3 is then a consequence of Theorems 18 and 33. For classes of bounded versatile symmetric difference (exponent 0), we get the following corollary (which, by Theorem 33, implies Theorem 1).

**Corollary 20.** _Let_ C _be a (hereditary) class of bounded versatile symmetric difference. There is an_ O<sub>C</sub>(_n_<sup>2</sup>)_-time algorithm that, given an n-vertex graph of_ C_, outputs an sd-degeneracy sequence of G of width_ O<sub>C</sub>(1).

## 4 SSSP in graphs given with an interval biclique partition

In this section we prove Theorem 5, which for convenience we recall below.

**Theorem 5.** _There is an_ O(_n+b)-time algorithm that, given an interval biclique partition of an n-vertex graph G with b bicliques and_ \(s\in V(G)\)_, outputs a shortest-path tree from vertex s in G._


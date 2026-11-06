We show that the best known approximation ratio of 1.5 for the maximum stable marriage problem with ties \[33\] can also be achieved for the matroid kernel problem with ties. This extension is made possible by a new theorem on basis exchanges for two disjoint bases of a matroid, which may be of independent interest.

In addition to extending the approximation result to matroids, we also go beyond preferences with ties, and achieve the same approximation ratio for preferences given by interval orders. Interval orders are partial orders that can be obtained as left-to-right precedence relations of intervals on the real line. Equivalently, they can be characterized by the property that the disjoint union of two comparable pairs contains a third comparable pair. Several stability notions that have appeared in the literature can be modeled as interval orders (e.g., \(\alpha\)-stability \[1, 37\], near-stability \[10\]). We show that a simple variant of the Gale-Shapley algorithm applied to carefully constructed modified instances of the problem gives a 1.5-approximation for the maximum matroid kernel problem with interval orders.

We complement this result with a new hardness result for the maximum stable marriage problem with arbitrary partial orders. We show that, assuming the Unique Games Conjecture \[29\], it is NP-hard to approximate the problem within a factor of \(2-\delta\) for any \(\delta>0\).

## 1.1 Basic definitions

### Partial orders, weak orders, and stable marriage with ties.

A _(strict) partial order_ on a ground set _S_, denoted by \(\succ\), is an irreflexive, transitive, and asymmetric binary relation<sup>1</sup> on _S_. In this paper, we always assume that |_S_| is finite. If several partial orders are given, we use indices to distinguish them.

Two elements _x_ and _y_ are _incomparable_ if \(x\unknown\unknown y\) and \(x\unknown\unknown y\). A partial order is a _weak order_ if being incomparable is a transitive relation. In this case, we use _x∼y_ to indicate that _x_ and _y_ are incomparable, or in other words, tied. In a weak order, the ground set _S_ is partitioned into equivalence classes of tied elements.

In the _stable marriage problem with ties and incomplete lists_ (smti)<sup>2</sup>, we are given a bipartite graph _G_=(_U,W;E_), and a weak order \(\succ_v\) on \(\delta_G(v)\) for every vertex \(v\in U\cup W\), where \(\delta_G(v)\) denotes the set of edges incident to _v_ in _G_. Given a matching _N_ in _G_, an edge \(e\in E\backslash N\) with endpoints _u,w_ is a _blocking edge_ for _N_ if the following two conditions hold:

• \(\delta_G(u)\cap N=\emptyset\) or \(e\succ_uN(u)\),<tbc>

• \(\delta_G(w)\cap N=\emptyset\) or \(e\succ_wN(w)\),

where _N(u_) denotes the edge of _N_ incident to _u_ if it exists. The matching _N_ is _stable_ if no edge blocks it. The max-smti problem is to find a stable matching of maximum size. The problem is NP-hard \[25\], and the best known polynomial-time approximation algorithm has an approximation ratio of 1.5 \[33\]. It is also known that no approximation ratio better than 4/3 is achievable assuming the Unique Games Conjecture (UGC) \[41\]. In this paper, we will also consider the _maximum stable marriage problem with partial orders_ (max-smpo), where the preferences are not required to be weak orders. To our knowledge, no stronger hardness of approximation results have previously been known for max-smpo than those for max-smti.

<sup>1</sup>In literature, the term partial order is also used to refer to a _reflexive_, transitive, and antisymmetric binary relation, which we call a _non-strict partial order_. Strict partial orders and non-strict ones are equivalent in the sense that there is a one-to-one correspondence between them; a strict partial order is converted to a non-strict partial order by adding binary relations \(x\succ x\) for all \(x\in S\), and vise versa. <sup>2</sup>While the _stable marriage problem_ was orinally defined for simple bipartite graphs, we use the term to mean a generalized version where graphs can be multigraphs, i.e., parallel edges are allowed.


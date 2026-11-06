**Lemma 3** (See e.g., [13])**.** _Let T be a spanning tree of G and e_<sup>∗</sup>=(_g,f_) _an edge of the cotree T_<sup>∗</sup> _of T. If we root T_<sup>∗</sup> _s.t. g is closer to the root than f, then each node of_ \(T_f^*\) _maps to a face enclosed by S=C(T,e). Analogously, each node of_ \(T^*\backslash T_f^*\) _maps to a face not enclosed by S. I.e.,_ \(w(T_f^*)=w_F(S_{in})\)_, and_ \(w(T^*\backslash T_f^*)=w_F(S_{out})\).

Alas, the weights in the input graph _G_ are assigned to vertices and not to faces. Therefore, the idea is to transfer the vertex-weights to face-weights s.t. a balanced separator w.r.t. these face-weights is also a balanced separator w.r.t. the original vertex-weights (perhaps with a different balance constant). There are two challenges with this approach:

**Challenge I - Assigning Weights to Faces.** The natural naive assignment that assigns each face a weight equal to the total weight of its vertices, does not work. This is because a vertex may belong to many faces. Thus, a (primal) subgraph might have a small total vertex-weight but a large total face-weight. In _T_<sup>∗</sup>, this means that a subtree \(T_f^*\) of some node _f_ might have a large weight, where in fact it corresponds to a cycle that encloses a small-weight subgraph, while the external subgraph has a large weight. Such a subtree might be mistakenly chosen to define the separator. I.e., _f_ can be a balanced node in the dual tree, but it does not necessarily correspond to a balanced separator in the primal graph with respect to vertex-weights.

**Challenge II - Existence of a Balanced Node.** Even if we overcome the first challenge, since faces can be arbitrarily large, it is not guaranteed that a balanced node _f_ exists in _T_<sup>∗</sup>. It may be the case that all subtrees of _T_<sup>∗</sup> either weigh too much, or weigh too little. For example, when _T_<sup>∗</sup> is a star.

We next describe how prior work dealt with the above challenges, and how we deal with them.

**Lipton-Tarjan [15].** In the 70’s, Lipton and Tarjan introduced the above approach in the centralized setting. To overcome Challenge I, each vertex of _G_ transfers its weight to an arbitrary face that it participates in. Thus, for any cycle of _G_, the weight of its (non-strict) interior w.r.t. faces and w.r.t. vertices is similar (each vertex assigns its weight to exactly one face that it lies on). In the centralized setting, Challenge II is easily dealt with by _triangulating G_. I.e., augmenting _G_ with artificial edges to make each of its faces consist of exactly three edges. In the augmented graph, it is not hard to show that _T_<sup>∗</sup> always admits a balanced node _f_. This is because now the dual graph _G_<sup>∗</sup> is 3-regular, thus _T_<sup>∗</sup> is a binary tree, and the weight assignment to faces is \(3\alpha\)-proper if the weight to vertices was originally \(\alpha\)-proper. In the distributed setting however, triangulation is not an option, since it may require adding a linear number of artificial edges which we cannot communicate on (and simulating them is too costly). This has motivated the following alternative direction of [9].

**Ghaffari-Parter [9].** In 2017, Ghaffari and Parter [9] provided the first (near-optimal, \(\tilde{O}(D)\)-rounds) distributed procedure that computes a path separator. Their procedure is _randomized_ and overcomes the above challenges as follows.

To overcome Challenge I, they compute for each node _f_ of _T_<sup>∗</sup> a weight \(w'(T_f^*)\) that approximates the total vertex-weight of the primal subgraph corresponding to \(T_f^*\). Intuitively, instead of assigning<tbc>

root of T*
g
e
f
root of T

Figure 1: The primal graph _G_ is in blue. Solid blue edges are in _T_ and dashed blue edges are not in _T_. I.e., their duals (in red) are in _T_<sup>∗</sup>. Removing the dual edge _e_<sup>∗</sup>=(_g,f_) from _T_<sup>∗</sup> breaks _T_<sup>∗</sup> into \(T_f^*\) (_f_’s subtree in _T_<sup>∗</sup>) and \(T^*\backslash T_f^*\). The fundamental cycle _C(T,e_) (highlighted in yellow) encloses all faces that correspond to nodes of \(T_f^*\), and does not enclose any face that corresponds to nodes of \(T^*\backslash T_f^*\).


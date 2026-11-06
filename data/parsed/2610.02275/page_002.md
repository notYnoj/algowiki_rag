<tbc>and clique number \[4, 9, 18\]. Santra \[19\] obtained polynomial-time algorithms for proper interval, block, and split graphs. Bhyravarapu et al. \[1\] gave polynomial-time algorithms for distance-hereditary and biconvex bipartite graphs, with an explicit _O(n_<sup>42</sup>) bound for the latter class. They also obtained a \(2^{O(\omega)}\mathrm{poly}(n)\)-time algorithm on chordal graphs, where \(\omega\) is the clique number.

Das and Santra \[13\] introduced the _oriented star-conflict graph A<sub>G</sub>_ and established the identity \(\rho_\mathrm{e}^\mathrm{o}(G)=\alpha(A_G)\). The vertices of _A<sub>G</sub>_ correspond to oriented edges of _G_, where the first endpoint is designated as the centre of a star and the second as one of its leaves; the precise adjacency rule is recalled in Section 3. Using this construction, they obtained _O(n_<sup>2</sup>+_m_<sup>2</sup>)-time algorithms for permutation and interval graphs, where _n_=|_V(G_)| and _m_=|_E(G_)|; in terms of _n_ alone, this gives an _O(n_<sup>4</sup>) bound \[13\]. They treated well-partitioned chordal graphs separately.

More recently, Das and Santra \[12\] used the same oriented star-conflict graph to study Maximum Edge Open Packing on cocomparability graphs. They proved that if _G_ is a cocomparability graph, then _A<sub>G</sub>_ is also a cocomparability graph. Since maximum independent set is polynomial-time solvable on cocomparability graphs, this yields an _O(n_<sup>2</sup>+_m_<sup>2</sup>)-time algorithm, and hence an _O(n_<sup>4</sup>)-time algorithm in terms of _n_ alone \[12\]. This result simultaneously generalizes the earlier algorithms for permutation and interval graphs, since both classes are contained in the class of cocomparability graphs.

The present work takes this structural approach one step further. We prove that the transformation \(G\mapsto A_G\) preserves AT-freeness: if _G_ is AT-free, then so is _A<sub>G</sub>_. Since cocomparability graphs form a subclass of AT-free graphs, this extends the oriented star-conflict framework to a strictly broader setting. The graph _A<sub>G</sub>_ has 2_m_ vertices and can be constructed in _O(n_<sup>2</sup>+_m_<sup>2</sup>) time. Applying the _O(N_<sup>4</sup>)-time maximum independent set algorithm of Broersma et al. \[6\] to _A<sub>G</sub>_, where _N_=|_V(A<sub>G</sub>_)|=2_m_, gives an overall running time of _O(n_<sup>2</sup>+_m_<sup>4</sup>), which is _O(n_<sup>8</sup>) when expressed only in terms of _n_. The progression of these results and the corresponding graph-class inclusions are illustrated in Figure 1.

## Our contributions.

We give polynomial-time algorithms for three graph classes. First, we prove that _A<sub>G</sub>_ is AT-free whenever _G_ is AT-free. Combining this preservation theorem with the correspondence of Das and Santra and the independent-set algorithm of Broersma et al. \[6\] yields an _O(n_<sup>2</sup>+_m_<sup>4</sup>)-time algorithm for Maximum Edge Open Packing, where _n_=|_V(G_)| and _m_=|_E(G_)|.

Second, we give an _O(n_<sup>4</sup>)-time algorithm for chordal graphs, without a bound on the clique number. We use a standard nice tree decomposition obtained from a clique tree \[16\]. The endpoint set of an edge open packing meets each clique in at most two vertices. Recording these vertices and their roles in a partially constructed star gives quadratically many states per bag and a constant number of label combinations for each active subset at a join.

Third, we give an _O(n_<sup>4</sup>)-time algorithm for convex bipartite graphs. Convexity orders the connected components of a solution from left to right. Two boundary indices record all restrictions on the next component, allowing a dynamic program that appends one star at a time. This extends the earlier biconvex result to a larger class and improves its explicit running-time bound. These extensions are<tbc>

AT-free graphs (n2 + m4) (n8) Present work
Cocomparability graphs (n2 + m2) (n4) (n4) Das and Santra [12]
Permutation graphs (n2 + m2) (n4) (n2 + m2) (n4) Das and Santra [13]
Interval graphs (n2 + m2) (n4) Das and Santra [13]

Figure 1: Graph-class hierarchy for the oriented star-conflict approach to Maximum Edge Open Packing. An arrow from C<sub>1</sub> to C<sub>2</sub> indicates that \(\mathcal{C}_1\subseteq\mathcal{C}_2\). The displayed bounds are the corresponding running times for computing a maximum edge open packing.


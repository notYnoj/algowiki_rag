1. If _C_ is the boundary of an internal face in the planar embedding, then _C_ is a _leaf_ of T(_G_); remove _C_ from C.<tbc>

2. If _C_ is a splittable cycle, then for each \(C'\in\mathscr{C}_s(C)\), add \(C'\) as a child of _C_ in T(_G_) and add \(C'\) to C; then remove _C_ from C. Here _C_ is a _splittable-node_ of T(_G_).<tbc>

3. If _C_ is an unsplittable cycle, then for each \(C'\in\mathscr{C}_u(C)\), add \(C'\) as a child of _C_ in T(_G_) and add \(C'\) to C; then remove _C_ from C. Here _C_ is an _unsplittable-node_ of T(_G_).

Whenever the context is clear, we will simply write T , instead of T(_G_). A shortest cycle _C_ of _G_ is a _tree cycle_ if \(C\in V(\mathcal{T})\), and otherwise it is a _non-tree cycle_. For clarity, we will refer to vertices of T as nodes. Also, to clearly highlight we are considering a node of T (which must be a shortest cycle in _G_), we will use letters like \(\alpha,\beta,\gamma,\iota\), etc.

We now state some useful properties of LSCT obtained in \[4, Lemma 5.7\].

**Proposition 5.2.** _Consider a weighted clean plane graph G with_ \(w:E(G)\rightarrow\mathbb{Z}_{>0}\) _where a shortest cycle of G is the outer face of the embedding, and its LSCT,_ T _. Then, the following holds:_

1. _For tree cycles C_<sub>1</sub>_,C_<sub>2</sub> _in G,_ \(C_1\le C_2\) _if and only if C_<sub>1</sub> _is a descendant of C_<sub>2</sub> _in_ T .<sup>0</sup><tbc>

2. _For any shortest cycle C in G exactly one of the following holds: i) C is a tree cycle, or ii) there exist a unique splittable-node C_<sup>∗</sup> _of_ T(_G_) _and two non-consecutive paths_ \(P_i,P_j\in\mathcal{P}_s(C^*)=\{P_0,P_1,P_2,\dots,P_q\}\) _such that_ \(C=P_i\cup P_j\) _and_ \((P_i,P_j)\notin\{(P_0,P_q),(P_q,P_0)\}\).<tbc>

_3._ _For any splittable-node C of_ T(_G_) _the paths in_ P_<sub>s</sub>(C_) _are pairwise internally vertex-disjoint. Moreover, for distinct splittable nodes_ \(C,C'\) _of_ T(_G), we have_ \(\mathcal{P}_\mathsf{s}(C)\cap\mathcal{P}_\mathsf{s}(C')=\emptyset\).<tbc>

_4._ _The laminar shortest cycles tree of G can be computed in polynomial time._

**Lemma 5.1** (Implicit in \[4\])**.** _For a weighted clean plane graph G with LSCT_ T(_G), where t is the number of leaves in_ T _, the following holds._

(_i)_ _The number of non-tree cycles in G is at most_ O(_t_<sup>2</sup>).<tbc>

_(ii)_ _The number of longitudinal paths in G are at most_ O(_t). Furthermore, we can find these paths in time bounded by n_<sup>_O_(1)</sup>._

The next result follows from the definition of laminar shortest cycles tree.

**Lemma 5.2** (Implicit in \[4\])**.** _Consider a (weighted) clean plane graph G with LSCT_ T _. For_ \(\alpha,\beta,\gamma\in V(\mathcal{T})\), <sup>1</sup> _if_ \(\beta\) _is a descendant of_ \(\alpha\) _in_ T _and_ \(\gamma\) _is not a descendant of_ \(\alpha\)_, then_ \(E(\beta)\cap E(\gamma)\subseteq E(\alpha)\).

Note that by the Four Color Theorem, any planar graph on \(4n'\) vertices has an independent set of size at least \(n'\). Also, the dual of a planar graph is planar. Recall that the leaves of a laminar shortest cycles trees are the facial cycles of the given plane graph. The above gives the next result.

**Lemma 5.3** (Implicit in \[4\])**.** _If LSCT_ T _of a weighted plane graph G contains at least_ 4_k leaves, then there is a set of k pairwise edge-disjoint cycles in G, and these k shortest cycles are leaves of_ T .

<sup>0</sup>We will follow the convention that a node is a descendant of itself in a rooted tree. <sup>1</sup>We use Greek letters (e.g., \(\alpha,\beta,\gamma\)) to denote nodes of T(which are also shortest cycles in _G_). Symbols such as _C_ and \(C'\) denote arbitrary cycles (either tree or non-tree cycles).


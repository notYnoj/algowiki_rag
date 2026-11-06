# The Parameterized Complexity of Coloring Discovery

17<tbc>

<tbc>O(_k_<sup>2</sup>_q_) time. There are at most (_k_+1)_<sup>k</sup>_=2<sup>O(_k_log_k_)</sup> partitions of _C_. Testing independence and the extension condition as well as building and solving the assignment problem takes O(_m+k_<sup>2</sup>_q_) time per partition.

A minimum vertex cover can be found by an iterative branching algorithm. Up to depth _k_, this costs O(2_<sup>k</sup>(n+m_)) time. We have \(q\le n\). We therefore obtain a total running time of

\(\mathcal{O}\big(2^k(n+m)+(k+1)^k(m+k^2q)\big)=2^{\mathcal{O}(k\mathrm{log}k)}(n+m).\)

Since the palette preprocessing reduces _q_ to at most _n_, the algorithm is fixed- parameter tractable in _k_ and either computes the exact optimum or reports that no proper _q_-coloring exists.

### A.2 The distance-to-complete algorithm

We now give further details for Theorem 2. Let \(S\subseteq V(G)\) be a minimum set such that _C=V(G_)\\_S_ is a clique. It can be found as a minimum vertex cover of the complement graph in O(2_<sup>k</sup>n_<sup>2</sup>) time where _k_=|_S_| . Two vertices of _C_ have the same _type_ if they have the same neighborhood in _S_. Let R denote the resulting partition of _C_. Clearly \(|\mathcal{R}|\le 2^k\).

Fix an independent-block partition P of _S_. In any proper coloring, distinct blocks of P receive distinct colors and all vertices of the clique _C_ receive distinct colors. A color used by a block _P_ is either absent from _C_, or it appears on exactly one clique vertex. In the latter case that vertex must belong to a type _R_ anticomplete to _P_. We therefore guess a map \(\sigma:\mathcal{P}\rightarrow\mathcal{R}\cup\{\perp\}\). The value \(\perp\) says that the color of _P_ is absent from _C_. The value _R_ says that one vertex of _R_ reuses this color.

Put \(a_R=|\sigma^{-1}(R)|\) and \(s=|\{P\in\mathcal{P}:\sigma(P)\neq\perp\}|\). A guess is feasible only if every _P_ with \(\sigma(P)=R\) is anticomplete to _R_, if \(a_R\le|R|\) for every type, and if \(|C|+|\mathcal{P}|-s\le q\). The last expression is the number of distinct colors required: without reuse, the clique and the blocks use disjoint color sets. Each non-\(\perp\) value saves exactly one color.

For a feasible guess, create one assignment node for each block \(P\in\mathcal{P}\). If \(\sigma(P)=R\), this node represents both _P_ and the one clique vertex of type _R_ that reuses its color. In addition, create |_R_|-_a<sub>R</sub>_ clique-only nodes for each type _R_. The total number of nodes is |_C_|+|P|-_s_, so the feasibility test ensures that they can be matched injectively to colors in \[_q_\].

The cost of assigning color _c_ to a block node _P_ is \(|P\backslash\varphi^{-1}(c)|\). If \(\sigma(P)=R\), add zero when _R_ contains an initially _c_-colored vertex and add one otherwise. The cost of assigning _c_ to a clique-only node of type _R_ is zero when _c_ already occurs in _R_ and one otherwise. A minimum-cost injection can again be found by weighted bipartite matching.

**Lemma 4.** _For a fixed feasible pair_ \((\mathcal{P},\sigma)\) _and a fixed injective assignment of color names, the sum of the above costs is exactly the minimum number of flips realizing that assignment._


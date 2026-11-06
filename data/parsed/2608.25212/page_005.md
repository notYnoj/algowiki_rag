**Theorem 1.** _For every graph class_ C _of linear neighborhood complexity, there is an_ O<sub>C</sub>(_n_<sup>2</sup>)_-time algorithm that, given an n-vertex graph_ \(G\in\mathcal{C}\)_, outputs an sd-degeneracy sequence of G of width_ O<sub>C</sub>(1).

Note that the running time of Theorem 1 is optimal for graphs with \(\Theta(n^2)\) edges. This resolves an open problem of \[12\]. For graphs with a subquadratic number of edges, we provide a linear-time randomized algorithm.

**Theorem 2.** _For every graph class_ C _of linear neighborhood complexity, there is a randomized algorithm that, given a graph_ \(G\in\mathcal{C}\)_, outputs an sd-degeneracy sequence of G of width_ O<sub>C</sub>(1) _in expected time_ \(\mathcal{O}_\mathcal{C}\big(|V(G)|+|E(G)|\big)\).

Previously available algorithms would either proceed by naively constructing an sd-degeneracy sequence of width O(1), which takes time O(_n_<sup>4</sup>) using a direct implementation (or O(_n_<sup>3</sup>) after realizing that C has bounded versatile symmetric difference, see definition below), or by following Welzl’s approach, which currently yields an sd-degeneracy sequence of width O(log<sup>2</sup>_n_) in time O((_n+m_)log_n_) \[23, 12\], where _n_=|_V(G_)| and _m_=|_E(G_)|.

To prove Theorem 1, we introduce the notion of _bounded versatile symmetric difference_, where we require that every induced subgraph with _n_ vertices contains \(\Theta(n)\) disjoint vertex pairs _u,v_ satisfying \(|N(u)\triangle N(v)|\le c\) for some constant _c_.

On one hand, a simple application of Haussler’s packing lemma (cf. Theorem 33) proves that linear neighborhood complexity implies bounded versatile symmetric difference. On the other hand, we show how to use the "versatility" strengthening, together with a known data structure for longest common extension of \[39\], to compute sd-degeneracy sequences in O(_n_<sup>2</sup>) time.

We will actually prove generalizations of Theorems 1 and 2 to classes of VC density \(\rho\).

**Theorem 3.** _For every real number_ \(\rho\ge 1\) _and every graph class_ C _of VC density_ \(\rho\)_, there is an_ \(\mathcal{O}_\mathcal{C}(n^{3-\frac{1}{\rho}})\)_-time algorithm that, given an n-vertex graph_ \(G\in\mathcal{C}\)_, outputs an sd-degeneracy sequence of G of width_ \(\mathcal{O}_\mathcal{C}(n^{1-\frac{1}{\rho}})\).

**Theorem 4.** _For every real number_ \(\rho\ge 1\) _and every graph class_ C _of VC density_ \(\rho\)_, there is a randomized algorithm that, given a graph_ \(G\in\mathcal{C}\)_, outputs an sd-degeneracy sequence of G of width_ \(\mathcal{O}_\mathcal{C}(n^{1-\frac{1}{\rho}})\) _in expected time_ \(\mathcal{O}_\mathcal{C}\big(|V(G)|+|E(G)|\big)\).

With the aforementioned results of \[12, 11\], Theorem 1 allows us to compute in O(_n_<sup>2</sup>) time a signed tree model with O(_n_) transversal pairs and an interval biclique partition with O(_n_) bicliques. Our second contribution is an efficient algorithm using the latter for shortest-path computation.

**Theorem 5.** _There is an_ O(_n+b)-time algorithm that, given an interval biclique partition of an n-vertex graph G with b bicliques and_ \(s\in V(G)\)_, outputs a shortest-path tree from vertex s in G._

Note that the running time of Theorem 5 is independent of _m_, the number of edges of _G_, and in fact is usually sublinear in _m_. Theorem 5 bypasses the use of the DAG-compression technique \[5\], which is a way to solve shortest-path problems from interval biclique partitions that incurs, in the current state of knowledge, extra superconstant factors.

By applying Theorem 5 to every vertex of the graph and pipelining it with Theorem 1 and the aforementioned results of \[12, 11\], we obtain a time-optimal algorithm for All-Pairs Shortest Path (APSP for short) in classes of linear neighborhood complexity.

**Theorem 6.** _For every graph class_ C _of linear neighborhood complexity, All-Pairs Shortest Path can be solved in_ O<sub>C</sub>(_n_<sup>2</sup>) _time on n-vertex graphs of_ C.


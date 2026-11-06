**Theorem 7.4** (Energy Game in the Isomorphic-Priors Model)**.** _There is an algorithm that solves_ Energy Game _with k prior instances each having at most n vertices and m edges in O(k(n+m_)log_n_) _preprocesses time and O_((_n+m_)log_n_) _query time. Additionally, if each prior G<sub>i</sub>, that is a winning instance, is equipped with a memoryless winning strategy_ \(\sigma_i\) _for Player 1 from every starting vertex, then the algorithm can also compute a memoryless optimal winning strategy_ \(\sigma_H\) _with the same guarantees for H in O_((_n+m_)log_n_) _time._

## 7.2 Preliminaries: The Weisfeiler-Leman Algorithm

To solve constrained reachability and game dynamics, we model our problem instances as attributed directed graphs. Let \(G=(V,E,\alpha_V,\alpha_E)\) be a directed graph where \(\alpha_E:E\rightarrow\Sigma_E\) assigns an _attribute_ to each edge (e.g., costs, lengths, or weights), and \(\alpha_V:V\rightarrow\Sigma_V\) assigns an _attribute_ to each vertex (e.g. source, sink, or what player a vertex belongs to).

When initializing the _1-dimensional Weisfeiler-Leman (1-WL) algorithm_, the vertex attributes are directly translated into an initial vertex _coloring_, denoted by \(\chi_0^G:V\rightarrow\mathcal{C}\), such that \(\chi_0^G(u)=\chi_0^G(v)\) if and only if \(\alpha_V(u)=\alpha_V(v)\). The 1-WL algorithm then iteratively _refines_ these colors (e.g, by recolor some vertices of color _c_ with a new color _d_), ultimately returning a _stable color_ for every vertex _u_, denoted by \(\chi_\infty^G(u)\), which possesses the structural properties detailed in Lemma 7.6.

### The 1-WL Algorithm: A Primer.

The 1-WL algorithm can be intuitively understood as an iterative message-passing process. Initially, every vertex only knows its own starting color. In each round, every vertex "broadcasts" its current color to its neighbors. Simultaneously, it listens to the incoming messages, tallying up exactly how many neighbors of each color it has, grouped by the attributes and directions of the connecting edges. It then bundles its own current color with this exact tally to form a unique "signature". If two vertices that previously shared the same color generate different signatures (meaning their local neighborhoods differ), they are split into two different new colors. This process continues until no pair of vertices split into two different new colors. The final color is called the _stable color_.

Formally, let \(G=(V,E,\alpha_V,\alpha_E)\) be an attributed directed graph. For two colorings \(\chi,\chi':V\rightarrow\mathcal{C}\), we write \(\chi\unknown\chi'\) if \(\chi'(v)=\chi'(w)\) for all \(v,w\in V\) such that \(\chi(v)=\chi(w)\) (in other words, the partition into color classes of \(\chi\) refines the corresponding partition for \(\chi'\)). We write \(\chi\equiv\chi'\) if \(\chi\unknown\chi'\) and \(\chi'\unknown\chi\). The initial coloring computed by 1-WL is defined via \(\chi_0^G(v)=\alpha_V(v)\) for all \(v\in V(G)\). For \(i\ge 0\) the coloring is iteratively refined by setting

\(\chi_{i+1}^G(v):=\left(\chi_i^G(v),\left\{\left(\chi_i^G(u),\alpha_E(u,v)\right)|u\in N_{in}(v)\right\},\left\{\left(\chi_i^G(w),\alpha_E(v,w)\right)|w\in N_{out}(v)\right\}\right),\)

where {{_..._}} denotes a multiset. This refinement stabilizes when the partition of _V_ induced by the colors stops changing. More concretely, since \(\chi_{i+1}^G\unknown\chi_i^G\) for every \(i\ge 0\), there is some minimal \(i_\infty\ge 0\) such that \(\chi_{i_\infty}^G\equiv\chi_{i_\infty+1}^G\), and we set \(\chi_\infty^G:=\chi_{i_\infty+1}^G\). Note that we perform one extra iteration after stabilization, which is necessary for some technical reasons.

The 1-WL algorithm can be used as a simple heuristic to test isomorphisms of graphs. If some color appears a different number of times in the stable coloring of the two graphs, then they cannot be isomorphic (the converse is not true in general).

**Definition 7.5** (1-WL Equivalence)**.** Two (attributed) graphs _G_ and _H_ are _1-WL equivalent_ \((G\equiv_{1\text{-WL}}H)\) if \(\left\{\left(\chi_\infty^G(v)|v\in V(G)\right\}\right\}=\left\{\left(\chi_\infty^H(w)|w\in V(H)\right\}\).

### Properties of 1-WL.

Below are some basic facts about 1-WL.


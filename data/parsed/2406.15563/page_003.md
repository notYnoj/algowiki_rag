One can define a similar notion in the context of PCSPs \[5\]. A PCSP has width _k_ if a non- empty _k_-strategy on (X,B) implies a homomorphism from X to A. Recently, Atserias and Dalmau \[1\] showed that given an input graph _G_ and parameter \(\epsilon\in(0,1/2)\), the problem of distinguishing whether _G_ is 3-colorable from the case where _G_ is not \(O(n^\epsilon)\)-colorable has width between \(n^{1-2\epsilon}\) and \(n^{1-3\epsilon}\). This gives an algorithm to color 3-colorable graphs with \(O(n^\epsilon)\) colors in time \(2^{\Theta(n^{1-2\epsilon} logn)}\). Improving this runtime is posed as an open question in \[1\].

## 1.2 Definitions and Notation

For a given graph _G_, we let _V(G_) denote its set of vertices, _E(G_) denote the set of edges, and _n_:=|_V(G_)|. For any \(v\in V(G)\), we call the _neighborhood_ of _v_ (denoted _N<sub>G</sub>(v_)) the set of all \(u\in V(G)\) such that \(\{u,v\}\in E(G)\). We let _d<sub>G</sub>(v_)=|_N<sub>G</sub>(v_)| denote the _degree_ of _v_. We write _O_<sup>∗</sup> to suppress polynomial factors in _n_, and \(\tilde{O}\) to suppress polyloglog(_r_) factors (where _r_ is the approximation ratio). The analogous definitions hold for \(\tilde{\Omega}\).

**Maximum Independent Set**: We say a set \(S\subseteq V(G)\) is _independent_ if for all \(u,v\in S\), \(\{u,v\}\notin E\). We let \(\alpha(G)\) denote the size of the maximum cardinality independent set of _G_.

**Graph Coloring**: We say that a function \(c:V(G)\rightarrow[r]\) is a _r-coloring_ if \(c(u)\neq c(v)\forall\{u,v\}\in E(G)\). We say _G_ is _r-colorable_ if a valid _r_-coloring of _G_ exists. We let \(\chi(G)\) denote the chromatic number of _G_, i.e. the minimum integer _r_ such that _G_ is _r_-colorable.

## 1.3 Our Result and Techniques

Our main contribution is an improved approximation algorithm for coloring 3-colorable graphs.

**Theorem 1.1.** _Given a 3-colorable graph G_=(_V,E_) _and a parameter r\>_0_, there exists an algorithm that, with high probability, outputs a valid coloring of G using at most O(r_) _colors in time_ \(O^*\left(exp\left(\tilde{O}\left(\frac{nlog^{11/2}r}{r^3}\right)\right)\right)\).

For any fixed real \(\epsilon\in(0,1/3)\), setting _r_ to be \(n^\epsilon\), we obtain a coloring of _G_ using \(O(n^\epsilon)\) colors in time \(O^*\left(exp\left(O(n^{1-3\epsilon})\right)\right)\). This asymptotically improves upon the width-based algorithm given by Atserias and Dalmau \[1\]. Furthermore, up to polynomial factors in _n_, this matches the width-based lower bound given in \[1\]. Whether our result can be captured by a width-based argument remains a direction for future research.

**Techniques:** We closely follow the algorithm given by Bansal et al. \[3\]. We first consider the independent set problem. The approach in \[3\] is to branch on high degree vertices. For each such vertex, the algorithm chooses to include it with some small probability, in which case all of its neighbors are removed, else it removes the high degree vertex and recurses on the remaining graph. The probability of choosing each vertex is chosen in a way to ensure the number of leaves of the branching process remains bounded. Once the maximum degree of the graph is small, the algorithm terminates by applying a known approximation for for graphs with bounded degree \[4\]. We follow from a similar algorithm, replacing the base case with an \(\tilde{\Omega}(d^{1/3})\)-approximation for Independent Set on 3-colorable graphs. To then color the graph _G_, the algorithm in \[3\] repeatedly finds large independent sets and colors each independent set with its own color. Once the number of remaining vertices is small enough, they use a brute force inclusion-exclusion based algorithm for coloring the remaining vertices in time _O_<sup>∗</sup>(2<sup>|_V_|</sup>) \[6\]. We follow the same approach, using our improved approximation for Independent Set.


## 2 Notation and conventions

We work throughout with finite simple graphs. In particular, all graphs considered below are nonempty, and we write \(n:=|V(G)|\ge 1\). For an integer \(k\ge 1\), write [_k_]={1_,...,k_}. All logarithms are natural.

A graph _G_ is called \(\varepsilon\)-far from being _k_-colorable if at least \(\varepsilon n^2\) edges must be deleted from _G_ in order to obtain a _k_-colorable graph. The sample complexity \(S_k(\varepsilon)\) is the smallest positive integer _q_ with the following property: for every \(\varepsilon\)-far graph _G_, a uniformly random _q_-vertex induced subgraph is non-_k_-colorable with probability at least 2/3. If _q\>n_, we sample all vertices.

For a map \(c:V(G)\rightarrow[k]\), let _M(c_) denote the set of monochromatic edges, that is, edges _uv_ with _c(u_)=_c(v_). Thus |_M(c_)| is the number of monochromatic edges under _c_.

A palette system _P_ assigns to each vertex _v_ a set \(P(v)\subseteq[k]\), and empty palettes are allowed. Define<tbc>

\(U(P):=\{v:P(v)\neq\varnothing\}.\)

<tbc>For \(i\in P(v)\), set<tbc>

\(d_i^P(v):=|\{u\in N_G(v):i\in P(u)\}|,m_P(v):=min_{i\in P(v)}d_i^P(v).\)

<tbc>The label count of _P_ is

\(\lambda(P):=\sum_{v\in V(G)}|P(v)|.\)

We write \(P'\subseteq P\) if \(P'(v)\subseteq P(v)\) for every vertex _v_.

For positive integers _r_, let

\(P_N^r:=N(N-1)\cdots(N-r+1)\)

be the number of ordered _r_-tuples of distinct elements from an _N_-element set. We set \(P_N^r=0\) when _r\>N_.

## 3 Distance characterization

**Lemma 3.1.** _A graph G is_ \(\varepsilon\)_-far from being k-colorable if and only if every map_ \(c:V(G)\rightarrow[k]\) _satisfies_<tbc>

\(|M(c)|\ge\varepsilon n^2.\)

<tbc>_Proof._ For a fixed map _c_, deleting all monochromatic edges makes _c_ a proper _k_-coloring. Conversely, if deleting an edge set makes _c_ proper, then that edge set contains every monochromatic edge of _c_. Hence the minimum number of deletions needed to obtain a _k_-colorable graph is

\(min_{c:V(G)\rightarrow[k]}|M(c)|,\)

which proves the claim.

**Lemma 3.2.** _If there exists an n-vertex_ \(\varepsilon\)_-far graph with_ \(n\ge 1\)_, then_<tbc>

\(\varepsilon<\frac{1}{2k}.\)


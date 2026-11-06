Thm. 14], a modified subdivision, and a reduction to leverage the chromatic number lower bound that comes from an upper bound on the independence number. The write-up of this result, and of the paper as a whole, is ours.

## 2 Preliminaries

For two integers _i_ and _j_, we denote by [_i,j_] the set of integers that are at least _i_ and at most _j_. For every integer _i_, [_i_] is a shorthand for [1_,i_]. In this paper, the log function is in base 2.

The Exponential-Time Hypothesis (ETH) asserts that there is a real constant \(\lambda>1\) such that _n_-variable 3-SAT cannot be solved in time \(\mathcal{O}(\lambda^n)\).

### 2.1 Standard graph-theoretic definitions and notation

We denote by _V(G_) and _E(G_) the set of vertices and edges of a graph _G_, respectively. We denote by \(\|G\|\) the total size of _G_, that is, |_V(G_)|+|_E(G_)|. For \(S\subseteq V(G)\), the _subgraph of G induced by S_, denoted _G[S_], is obtained by removing from _G_ all the vertices that are not in _S_. We denote by _N<sub>G</sub>(v_) the set of neighbors of _v_ in _G_. We denote by dist_<sub>G</sub>(u,v_) the length of a shortest path between _u_ and _v_ in _G_, and set \(\mathrm{Ball}_G^r(v):=\{w\in V(G)|\mathrm{dist}_G(v,w)\le r\}\).

A _subdivision_ of a graph _G_ is any graph _H_ obtained from _G_ by replacing edges _e_ of _G_ by paths with at least one edge whose extremities are the endpoints of _e_. A \((\ge s)\)_-subdivision_ is a subdivision where every edge is replaced by a path with at least _s_ internal vertices.

### 2.2 Trigraphs, contraction sequences, and twin-width

A _trigraph G_ has vertex set _V(G_), black edge set _E(G_), red edge set _R(G_) such that \(E(G)\cap R(G)=\emptyset\) (and \(E(G),R(G)\subseteq\left(V(G)2\right)\)). Two vertices _u,v_ such that \(uv\in R(G)\) are called _red neighbors_. The _red degree_ of _u_ is its number of red neighbors. The _maximum red degree_ of _G_ is the maximum red degree among all its vertices.

For distinct vertices \(u,v\in V(G)\), the _contraction_ of _u_ and _v_ replaces them with a new vertex _w_. For every \(x\in V(G)\backslash\{u,v\}\), the pair _wx_ is a black edge if both _ux_ and _vx_ are black edges, it is a non-edge if both _ux_ and _vx_ are non-edges, and it is a red edge otherwise. All pairs not incident with _u_ or _v_ remain unchanged.

A _contraction sequence_ of a graph _G_, viewed as a trigraph with no red edges, is a sequence _G=G<sub>n</sub>,G_<sub>_n_-1</sub>_,...,G_<sub>1</sub> such that |_V(G<sub>i</sub>_)|=_i_ and _G_<sub>_i_-1</sub> is obtained from _G<sub>i</sub>_ by contracting two vertices. The sequence is a _d-sequence_ if, for every \(i\in[n]\), the trigraph _G<sub>i</sub>_ has maximum red degree at most _d_. The _twin-width_ of _G_, denoted by tww(_G_), is the minimum integer _d_ for which _G_ admits a _d_-sequence.

To show Theorems 1 and 2, we will rely on the fact that long-enough subdivisions of general graphs have bounded twin-width.

\(\blacktriangleright\) **Lemma 5** (Theorem 7 in [3])**.** _For every n-vertex graph G, the_ \(2\lceil\mathrm{log}n\rceil\)_-subdivision H of G has twin-width at most 4. Furthermore, a 4-sequence of H can be computed in_ \(\mathcal{O}(\|H\|)\) _time._

The algorithmic statement of Lemma 5 is implicit in [3] and follows from the proof.

We say that a graph class C has _effectively bounded twin-width_ if there is a polynomial-time algorithm A and a fixed integer _d_ such that on every graph \(G\in\mathcal{C}\), A outputs a _d_-sequence of _G_. We observe that most classes currently known to have bounded twin-width have effectively bounded twin-width.


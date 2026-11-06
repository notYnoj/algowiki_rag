## 4.2 Dynamic Unweighted Sparsifier

For the dynamic unweighted sparsifier, the algorithm maintains a sequence of explicit _expander decompositions_ of the underlying undirected graph. We begin with some expander decomposition preliminaries on unweighted, undirected graphs. For a subset of vertices \(S\subseteq V\) , let \(\mathbf{vol}(S)=\sum_{v\in S}deg(v)\) denote the sum of vertex degrees in _S_. For a partition P={_V_<sub>1</sub>_,...,V<sub>k</sub>_} of _V_ into clusters, let \(\partial\mathcal{P}=\cup_{i=1}^k\partial V_i\) denote the edges whose endpoints belong to different clusters.

**Definition 16** (\(\phi\)-expander)**.** _An undirected graph is a_ \(\phi\)-expander _if_ \(|\partial S|\ge\phi\cdot min\{\mathbf{vol}(S)\), **vol**(_V_\\_S_)} _for all_ \(S\subseteq V\) .

**Definition 17** (\(\phi\)-expander decomposition with slack _s_)**.** _A_ \(\phi\)_-expander decomposition of an undirected graph G with slack_ \(s\ge 1\) _is a partition_ P={_V_<sub>1</sub>_,...,V<sub>k</sub>_} _of V into clusters such that_

1. \(|\partial\mathcal{P}|\le\tilde{O}(\phi m)\)_, and_<tbc>

_2._ _Each induced subgraph G_\[_V<sub>i</sub>_\] _is a_ \((\phi/s)\)_-expander._

We are interested in a dynamic expander decomposition algorithm with low _recourse_ with respect to the set \(\partial\mathcal{P}\). We say that the algorithm has amortized recourse \(\rho\) if for all \(k\ge 1\), the set \(\partial\mathcal{P}\) changes by at most \(\rho\cdot k\) edges after _k_ edge updates to the graph.

**Theorem 18** (Theorem 7.2 of \[GRST21\])**.** _Let_ \(0<\phi<1\) _be a parameter. There is a randomized algorithm that, given an unweighted graph G undergoing edge insertions and deletions, maintains an explicit_ \(\phi\)_-expander decomposition with slack_ \(s=2^{-O(log^{1/2}n)}\) _together with the explicit set of edges_ \(\partial\mathcal{P}\)_. The algorithm has update time_ \(2^{O(\sqrt{logn})}/\phi^2\) _and amortized recourse_ \(2^{O(\sqrt{logn})}\) _with respect to_ \(\partial\mathcal{P}\)_. The algorithm succeeds with high probability against an adaptive adversary._

We now describe the dynamic sparsification algorithm. Given the graph _H_, the algorithm first adds between _m/n_ and 2_m/n_ self-loops to each vertex in _H_. This initial pre-processing has amortized recourse _O_(1) since it takes \(\Omega(m)\) edge updates before the value of _m/n_ changes by a constant factor, at which point _O(m_) time is spent updating the self-loops. After the addition of self- loops, the graph still has _O(m_) edges. The algorithm maintains a dynamic expander decomposition (Theorem 18) with parameter \(\phi=2^{-log^{3/4}n}\) on the graph with self-loops. On the subgraph of _H_ consisting of the edges \(\partial\mathcal{P}\), the algorithm _recursively_ performs the same procedure, starting with adding \(|\partial\mathcal{P}|/n\) self-loops to each vertex. Since \(|\partial\mathcal{P}|\) is a factor \(2^{\Omega(log^{3/4}n)}\) smaller, the recursion depth is _t=O_(log<sup>1/4</sup>_n_). Each level of recursion has amortized recourse \(2^{O(\sqrt{logn})}\), so the overall recourse (and update time) is 2<sup>_O_(log<sup>3/4</sup>_n_)</sup>.

Given the explicitly maintained expander decompositions, we now implement the procedure \(\text{Sparsifier}(\beta)\). On recursion level \(i\ge 0\), let \(G_i\subseteq H\) be the initial subgraph at level \(i\ge 0\) of recursion (before the addition of self-loops), and let _m<sub>i</sub>_ be the number of edges in _G<sub>i</sub>_. Let P_<sub>i</sub>_ be the expander decomposition at this level, and let \(H_i=G_i\backslash\partial\mathcal{P}_i\) be the subgraph of edges with both endpoints in the same cluster. By construction, the input graph _H_ is the disjoint union of the subgraphs _H<sub>i</sub>_. The algorithm independently samples each edge in _H<sub>i</sub>_ with probability \(\frac{q\beta}{2t}\cdot\frac{n}{m_i}\), and outputs the sparsifier \(\widetilde{H}\) as the union of all sampled edges (over all _i_).

For the running time, observe that for each _i_, the random sampling in _H<sub>i</sub>_ can be done in time proportional to the number of samples: first determine the number of samples _s_, which can be sampled from a binomial distribution, and then randomly sample _s_ edges from the edges in _H<sub>i</sub>_.<tbc>


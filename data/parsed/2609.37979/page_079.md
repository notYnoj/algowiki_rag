**Definition B.4** (Clique Cover)**.** In the Clique Cover problem we are given a simple graph _G_ and a value _k_. We have to decide if _G_ contains clique cover of size at most _k_ (i.e., there is a collection of at most _k_ many cliques that are all subgraphs of _G_ and each edge of _G_ is covered by at least one clique)

Two problem instances (_G,k_) and \((G',k')\) are isomorphic if _G_ and \(G'\) are isomorphic as graphs and \(k=k'\).

**Definition B.5** (Coloring)**.** In the Coloring problem we are given a simple graph _G_ and a value _k_. We have to decide if _G_ is _k_-colorable.

Two problem instances (_G,k_) and \((G',k')\) are isomorphic if _G_ and \(G'\) are isomorphic as graphs and \(k=k'\).

**Definition B.6** (_k_-Coloring)**.** In the _k_-Coloring problem we are given a simple graph _G_. We have to decide if _G_ is _k_-colorable.

Two problem instances _G_ and \(G'\) are isomorphic if _G_ and \(G'\) are isomorphic as graphs.

**Definition B.7** (3D-Matching)**.** In the 3D-Matching problem we are given a set \(U\subseteq[n]^3\). We have to decide if there exist a set \(W\subseteq U\) with |_W_|=_n_ and no two elements of _W_ agree in any coordinate.

Two problem instances (_U,n_) and \((U',n')\) are isomorphic if there exist a bijection \(f:[n]\rightarrow[n']\) with \(U'=\{(f(x),f(y),f(z))|(x,y,z)\in[n]^3\}\).

**Definition B.8** (Exact Cover)**.** In the Exact Cover problem we are given a number _n_ and a values of subsets \(S_1,\dots,S_m\subseteq[n]\). We have to decide if there are indices _j_<sub>1</sub>_,...j<sub>s</sub>_ such that _S_<sub>_j_<sub>1</sub></sub>_,...,S<sub>j<sub>s</sub></sub>_ are disjoint and \(\bigcup_{t=1}^sS_{j_t}=\bigcup_{i=1}^mS_i\).

Two problem instances (_S_<sub>1</sub>_,...,S<sub>m</sub>,n_) and \((S'_1,\dots,S'_{m^\prime},n')\) are isomorphic if \(m=m'\), \(n=n'\) and there are bijective functions \(f:[n]\rightarrow[n']\) and \(g:[m]\rightarrow[m']\) such that for each \(i\in[m]\) we obtain \(f(S_i)=\{f(s)|s\in S_i\}=S'_{g(j)}\)

**Definition B.9** (Feedback Arc Set)**.** In the Feedback Arc Set problem we are given a directed graph _H_ and a number _k_. We have to decide if there exist a set of edges \(S\subseteq E(G)\) with \(|S|\le k\) such that every cycle in _G_ contains at least on edge in _S_.

Two problem instances (_H,k_) and \((H',k')\) are isomorphic if \(k=k'\) and \(H\cong H'\) are isomorphic as graphs.

**Definition B.10** (Feedback Vertex Set)**.** In the Feedback Vertex Set problem we are given a directed graph _H_ and a number _k_. We have to decide if there exist a set of vertices \(R\subseteq V(G)\) with \(|R|\le k\) such that every cycle in _G_ contains at least on vertex in _R_.

Two problem instances (_H,k_) and \((H',k')\) are isomorphic if \(k=k'\) and \(H\cong H'\) are isomorphic as graphs.

**Definition B.11** (Directed Hamiltonian Cycle)**.** In the Directed Hamiltonian Cycle problem we are given a directed unweighted graph _G_. We have to decide if _G_ contains a directed cycle which includes each node exactly once.

Two problem instances _G_ and \(G'\) are isomorphic if _G_ and \(G'\) are isomorphic as graphs.

**Definition B.12** (Undirected Hamiltonian Cycle)**.** In the Undirected Hamiltonian Cycle problem we are given a undirected unweighted graph _G_. We have to decide if _G_ contains a directed cycle which includes each node exactly once.

Two problem instances _G_ and \(G'\) are isomorphic if _G_ and \(G'\) are isomorphic as graphs.

**Definition B.13** (Hitting Set)**.** In the Hitting Set problem we are given a number _n_ and a values of subsets \(S_1,\dots,S_k\subseteq[n]\). We have to decide if there is a set \(W\subseteq[n]\) such that \(|W\cap S_i|=1\).

Two problem instances (_S_<sub>1</sub>_,...,S<sub>k</sub>,n_) and \((S'_1,\dots,S'_{k^\prime},n')\) are isomorphic if \(k=k'\), \(n=n'\) and there are bijective functions \(f:[n]\rightarrow[n']\) and \(g:[k]\rightarrow[k']\) such that for each \(i\in[k]\) we obtain \(f(S_i)=\{f(s)|s\in S_i\}=S'_{g(j)}\)


## 4 Dynamic 3-Coloring of Bipartite Graphs with Optimal Locality

node determines the coloring of the remaining nodes of its entire connected component. This global dependency means that the problem has locality \(\Omega(n)\) in any of the previously mentioned models of locality.

Allowing a third color makes the situation more interesting. In this paper we focus on the LCL problem of 3-coloring bipartite graphs. This problem, including restricted cases on graph classes of paths, trees and grids, has served to analyze connections between the locality of an LCL problem across different distributed models. There are known bounds in LOCAL \[10\], SLOCAL and online-LOCAL \[2\] (summarized in  1), as well as a lower bound of \(\Omega(\sqrt{n})\) in the non-signaling model of interest for distributed quantum computing \[12\].

Our result shows that the locality of 3-coloring bipartite graphs in dynamic-LOCAL matches the online-LOCAL model, tying a new connection between these models. Furthermore, when contrasted to the \(\Omega(\sqrt{n})\) lower bound for the non-signaling model \[12\] and the \(\Omega\big(n^{1/10}\big)\) lower bound for the SLOCAL model \[2\], this new _O_(log_n_) upper bound for 3-coloring bipartite graphs separates dynamic-LOCAL from both non-signaling locality and SLOCAL for a locally checkable problem (under the promise of bipartiteness), as shown in  1. To our knowledge, such separations were previously only known for non-LCL problems \[2\].

This problem has also been studied in the context of dynamic graph algorithms. In the case of fully dynamic graph algorithms, a lower bound of \(\Omega\big(n^{1/3}\big)\) was shown \[5\] for the average number of recolored nodes per update on an input sequence of insertions and deletions where the graph is a forest in every step. However, this does not imply a result for locality, since the degree of the forest in their construction is large and the diameter is at most 5.

## 2 Preliminaries

We will use the following definitions, notation, and models of computation throughout this paper.

**Graphs.** In this work we consider simple, undirected graphs _G_=(_V,E_) where _V_ is the set of nodes and _E_ is the set of edges. Given two graphs _G_<sub>1</sub>=(_V_<sub>1</sub>_,E_<sub>1</sub>) and _G_<sub>2</sub>=(_V_<sub>2</sub>_,E_<sub>2</sub>), we define the union of the two graphs as \(G_1\cup G_2:=(V_1\cup V_2,E_1\cup E_2)\). A path in _G_ between two nodes _u_ and _v_ is a sequence of distinct nodes _P_=(_u,w_<sub>1</sub>_,w_<sub>2</sub>_,...,w<sub>k</sub>,v_) such that there exists an edge in _E(G_) between any two consecutive nodes in the sequence. Similarly, a walk is defined in the same way, except that the nodes in the sequence do not have to be distinct. If a path between two nodes _u_ and _v_ exists, we call _u_ and _v_ connected. The distance between two connected nodes _u_ and _v_ in _G_, denoted as _d<sub>G</sub>(u,v_), is the length of the shortest path between them. We denote by N_<sub>r</sub>_\[_v_\] the set of nodes at distance at most _r_ from _v_. A connected component _C_ of a graph _G_ is a maximal subset of _V_ such that there is a path between any two nodes in the set. Given a graph _G_, any node \(v\in V\) belongs to exactly one connected component of _G_, which we denote as _C<sub>v</sub>_. A graph _G_ is bipartite if the set of nodes

\begin{tabular}{ccccc}
LOCAL & non-signaling & SLOCAL & dynamic-LOCAL & online-LOCAL \\
\(\Omega\big(\sqrt{n}\big)\) \[10\] & \(\Omega\big(\sqrt{n}\big)\) \[12\] & \(\Omega\big(n^{1/10}\big)\) \[2\] & \(\Omega(logn)\) \[11\] & \(\Omega(logn)\) \[11\] \\
\(\tilde{O}(\sqrt{n})\) \[12\] & \(\tilde{O}(\sqrt{n})\) \[12\] & \(\tilde{O}(\sqrt{n})\) \[12\] & _O_(log_n_) \[**this paper**\] & _O_(log_n_) \[2\] \\
\end{tabular}

1 Complexity landscape of 3-coloring bipartite graphs in different models of locality.


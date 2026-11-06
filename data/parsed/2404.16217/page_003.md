For the problem of computing the value of all-pairs max-flow up to \(\lambda\) in the static setting, Abboud et at. [1] obtained two deterministic algorithms that work for DAGs: a combinatorial algorithm which runs in \(O(2^{O(\lambda^2)}\cdot mn)\) time, and another algorithm that can be faster on dense graphs which runs in \(O((\lambda logn)4^{\lambda+o(\lambda)}\cdot n^\omega)\) time.

Some other graph theoretic problems studied in the fault-tolerant model include computing distance preservers [12, 21, 20], depth-first-search tree [3], spanners [8, 13], approximate single source distance preservers [5, 22, 6], approximate distance oracles [14, 9], compact routing schemes [9, 7].

Given a digraph G=(_V,E_) on _n_=|_V_| vertices and _m_=|_E_| edges, we first define some notations used throughout the paper.

We next define the concept of farthest min-cut that was introduced by Ford and Fulkerson in their pioneering work on flows and cuts [15]. Let _S_ be a source set, and _t_ be a destination vertex. Any (_S,t_)-cut _C_ is a partition of the vertex set into two sets: _A(C_) and _B(C_), where \(S\subseteq A(C)\) and \(t\in B(C)\). An (_S,t_)-min-cut _C_<sup>∗</sup> is said to be the _farthest min-cut_ if \(A(C^*)\unknown A(C)\) for every (_S,t_)-min-cut _C_ other than _C_<sup>∗</sup>. We denote the cut _C_<sup>∗</sup> by FMC(_S,t,_G). Similar to farthest-min-cut, we can define the nearest min-cut. An (_S,t_)-min- cut _C_<sup>∗</sup> is said to be the _nearest min-cut_ if \(A(C^*)\unknown A(C)\) for every (_S,t_)-min-cut _C_ other than _C_<sup>∗</sup>. We denote the cut _C_<sup>∗</sup> by NMC(_S,t,_G).

\(\blacktriangleright\) **Property 6.** _Let s be a source vertex, t be a destination vertex, and f be an s to t max-flow in graph_ G_. Let_ G<sub>f</sub> _denote the residual graph corresponding to flow f. Further let X be the set of vertices reachable from s in_ G<sub>f</sub>_, and Y be the set of vertices having a path to t in_ G<sub>f</sub>_. Then NMC(s,t,_G)=(_X,V_\\_X_) _and FMC(s,t,_G)=(_V_\\_Y,Y_).

We prove in this section the following hardness result for approximating optimal FT-BFP.

## 2 Preliminaries

in(_v,_G): The set of in-neighbours of _v_ in G.

out(_v,_G): The set of out-neighbours of _v_ in G.

In-Edges(_v,_G): The set of all incoming edges of _v_ in G.

Out-Edges(_v,_G): The set of all outgoing edges of _v_ in G.

out(_A,_G): The set of all those vertices in _V_\\_A_ having an incoming edge from some vertex of _A_ in G, where \(A\subseteq V(\mathcal{G})\).

G(_A_): The subgraph of G induced by the vertices lying in a subset _A_ of _V_.

G+(_u,v_): The graph obtained by adding an edge (_u,v_) to graph G.

G\\_F_: The graph obtained by deleting the edges lying in a set _F_ from graph G.

max-flow(_S,t,_G): The value of the maximum flow in graph G from a source set _S_ to a destination vertex _t_. When the set _S_ comprises of a single vertex, say _s_, we represent it simply by max-flow(_s,t,_G).

path[_a,b,T_]: The path from node _a_ to _b_ in a tree _T_.

_P[a,b_]: The subpath of path _P_ lying between vertices _a_ and _b_, where _a_ precedes _b_ on _P_.

_P_\(\circ Q\) : The path formed by concatenating paths _P_ and _Q_ in G. Here it is assumed that the last edge (or vertex) of _P_ is the same as the first edge (or vertex) of _Q_.

Below we state a property of nearest and farthest (_s,t_)-min-cuts [15].

## 3 Hardness of logarithmic approximation


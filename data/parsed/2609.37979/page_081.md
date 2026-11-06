Two problem instances (S=(_S_<sub>1</sub>_,...,S<sub>m</sub>),n,k_) and (S=(_S_<sub>1</sub>_,...,S<sub>m</sub>),n,k_) are isomorphic if \(m=m'\), \(k=k'\), \(n=n'\) and there are bijective functions \(f:[n]\rightarrow[n']\) and \(g:[k]\rightarrow[k']\) such that for each \(i\in[m]\) we obtain \(f(S_i)=\{f(s)|s\in S_i\}=S'_{g(i)}\).

**Definition B.22** (Steiner Tree)**.** In the Steiner Tree problem we are given a weighted undirected graph _G_, set of vertices _R_, and a value _k_. We have to decide if _G_ contains a subtree that contains each vertex in _R_ and has cost (i.e. sum of edges) at most _k_.

Two problem instances (_G,R,k_) and \((G',R',k')\) are isomorphic if \(k=k'\) and there is an isomorphism \(\varphi:V(G)\rightarrow V(G')\) from _G_ to \(G'\) that respects the edge weights and \(\varphi\) maps _R_ to \(R'\).

**Definition B.23** (Traveling Salesman Problem (TSP))**.** In the Traveling Salesman Problem we are given a weighted clique with _n_ vertices where each edge-weight is non-negative. We have to return the length of the humiliation cycle with the smallest length.

Two problem instances _G_ and \(G'\) are isomorphic if the underlying graphs are isomorphic.

**Definition B.24** (Metric Traveling Salesman Problem (Metric TSP))**.**<br>
In the Metric Traveling Salesman Problem we are given a weighted clique with _n_ vertices where each edge-weight is non-negative. Further the edge-weight satisfy the triangle inequality. We have to return the length of the humiliation cycle with the smallest length.

Two problem instances _G_ and \(G'\) are isomorphic if the underlying graphs are isomorphic.

**Definition B.25** (Vertex-Cover (VC))**.** In the Vertex-Cover problem we are given a simple graph _G_ and a value _k_. We have to decide if _G_ contains a vertex cover of size at most _k_.

Two problem instances (_G,k_) and \((G',k')\) are isomorphic if _G_ and \(G'\) are isomorphic as graphs and \(k=k'\).

## B.2 Additional Isomorphism-Preserving Reductions

In the following we show many different isomorphism-preserving reductions. However, many of them are simple modifications of already known reductions.

**Lemma B.26.** _All of the following reductions do hold:_

• SAT \(\le_p^\cong\) Coloring<tbc>

• VC \(\le_p^\cong\) Directed Hamiltonian Cycle<tbc>

• VC \(\le_p^\cong\) Set Cover<tbc>

• VC \(\le_p^\cong\) Feedback Vertex Set<tbc>

• VC \(\le_p^\cong\) Feedback Arc Set<tbc>

• SAT \(\le_p^\cong 0/1\)-Integer Linear Programming<tbc>

• SAT \(\le_p^\cong\) Clique<tbc>

• Coloring \(\le_p^\cong\) Exact Cover<tbc>

• Exact Cover \(\le_p^\cong\) Steiner Tree<tbc>

• Exact Cover \(\le_p^\cong\) Hitting Set<tbc>

• Exact Cover \(\le_p^\cong\) 3D-Matching<tbc>

• Coloring \(\le_p^\cong\) Clique Cover<tbc>

• Clique \(\le_p^\cong\) Set Packing

_and_ Directed Hamiltonian Cycle \(\le_p^\cong\) Undirected Hamiltonian Cycle.

_Proof._ All of these reductions can be obtained by using the corresponding reduction in \[Kar72\] and checking that the reduction is isomorphism-preserving.

**Lemma B.27.** IS \(\le_p^\cong\) VC


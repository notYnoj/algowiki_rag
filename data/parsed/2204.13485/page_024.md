Now suppose that a set \(\tau\) of forbidden edges is given instead of forced ones while some preferences of the agents are fixed. The question is whether the preference lists can be extended such that there exists a stable matching _M_ disjoint from \(\tau\).

Interestingly, forbidden-spe turns out to be NP-hard even if there are no predefined preferences, each capacity is one and the graph is bipartite. In that case the problem is equivalent to the following: Given a bipartite graph _G_=(_A,B;E_) where _E_ is partitioned into red edges _E<sub>r</sub>_ and blue edges _E<sub>b</sub>_, decide if there is a matching _M_ in the subgraph _G<sub>r</sub>_=(_A,B;E<sub>r</sub>_) such that the vertices of _M_ cover every blue edge. We call this problem red-blue-edge-cover.

**Theorem 36.** red-blue-edge-cover _is NP-complete._

_Proof._ The problem is clearly in NP. To show NP-hardness, we reduce from 3sat.

Let \(\Phi\) be a 3sat instance with clauses _C_<sub>1</sub>_,...,C<sub>m</sub>_ and variables _x_<sub>1</sub>_,...,x<sub>n</sub>_. We construct a bipartite graph _G_=(_A,B;E_) as follows. For each clause _C<sub>j</sub>_, we add two vertices \(c'_j\) and \(c''_j\) to _A_. For each literal _x<sub>i</sub>_ or \(\overline{x_i}\in C_j\), we add a vertex \(y_j^i\) or \(z_j^i\), respectively, to _B_. We connect these five vertices with red edges, that is, a red _K_<sub>2,3</sub> subgraph is added for every clause. For each variable _x<sub>i</sub>_, we add two vertices _y<sub>i</sub>_ and _z<sub>i</sub>_ to _A_, a selector vertex _s<sub>i</sub>_ to _B_, and two red edges _y<sub>i</sub>s<sub>i</sub>_ and _z<sub>i</sub>s<sub>i</sub>_. Finally, for \(i\in[n]\) we add blue edges between _y<sub>i</sub>_ and \(y_j^i\) for the values of _j_ for which \(x_i\in C_j\), and between _z<sub>i</sub>_ and \(z_j^i\) for the values of _j_ for which \(\overline{x_i}\in C_j\).

We claim that \(\Phi\) has a satisfying assignment if and only if _G_ admits a matching _M_ consisting of red edges whose end vertices cover every blue edge. Suppose there exists a satisfying assignment for \(\Phi\). Then for each _i_, we add the red edge _y<sub>i</sub>s<sub>i</sub>_ to _M_ if _x<sub>i</sub>_ was true, otherwise the edge _z<sub>i</sub>s<sub>i</sub>_. For each clause _C<sub>j</sub>_, we pick a literal that is true and add two red edges from \(a'_i\) and \(a''_i\) to the vertices corresponding to the other two literals. This way each blue edge will be covered. Indeed, if a blue edge is not covered at its vertex in _A_, then it corresponds to a false literal. However, in such a case the edge is covered in one of the _K_<sub>2,3</sub>s.

For the other direction, let _M_ be a red matching that covers every blue edge. In every red _K_<sub>2,3</sub>, there is a blue edge from one of its vertices in _B_ that is not covered by edges of the _K_<sub>2,3</sub>, hence it has to be covered by an edge _y<sub>i</sub>s<sub>i</sub>_ or _z<sub>i</sub>s<sub>i</sub>_, and only one of these two edges can be in _M_. If we set the values of the variables such that _x<sub>i</sub>_ is true if and only if \(y_is_i\in M\), then we get a satisfying assignment.

## Acknowledgement.

The work was supported by the Lendület Programme of the Hungarian Academy of Sciences - grant number LP2021-1/2021 and by the Hungarian National Research, Development and Innovation Office - NKFIH, grant numbers FK128673 and TKP2020-NKA-06.

forbidden-spe
Input:
A graph G=(V,E), vertex capacities q ∈ Z+V, a set τ ⊆ E, and preference values for some other vertex-edge pairs.
Question:
Does there exist a preference extension together with a stable q-matching M for which τ ∩ M = 0?


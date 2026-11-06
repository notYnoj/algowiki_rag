- Every edge in \(\mu\triangle\eta\) is colored 1 with probability at least \(\frac{1}{2q}\).<tbc>

**-** Every edge in \(E(G')\backslash(\mu\triangle\eta)\) is colored 2 with probability at least \(\frac{1}{2^{2qd}}\), because \(|V(\mu\triangle\eta)|\le 2q\) and _d_ is the maximum degree of a vertex in the graph _G_, so \(|E(G')|\le 2qd\).

For \(i\in[2]\), let _E<sub>i</sub>_ denote the set of edges of the graph _G_<sub>1</sub> that are colored _i_ using the function _g_. Then, due to the above mentioned coloring properties of the graph _G_<sub>1</sub>, we have the following result:

**Lemma 4.** _Let_ \(G'\)_, E_<sub>1</sub>_, and E_<sub>2</sub> _be as defined above. Then, with probability at least_ \(\frac{1}{2^{q+2qd}}\), \(\mu\triangle\eta\subseteq E_1\) _and_ \(E(G')\backslash(\mu\triangle\eta)\subseteq E_2\).

Note that the edges in \(\mu\triangle\eta\) form \(\mu\)-alternating paths/cycles. Therefore, if there exists a component _C_ in _G_<sub>1</sub> such that the set of colored 1 edges in _C_ do not form a \(\mu\)-alternating path or a cycle, then we could delete this component from _G_<sub>1</sub>.

**Reduction Rule 2** _If there exists a component in C containing a vertex_ \(u\in V(G)\) _such that_ \(\mu(u)\notin C\)_, then delete the component C from G_\[_V_<sub>1</sub>\].

Let _G<sup>⋆</sup>_=(_V_<sub>1</sub>_,E_<sub>1</sub>) be a graph on which Reduction Rule 2 is not applicable. Then, we get the following.

**Observation 1** _Every component in G<sup>⋆</sup> is a_ \(\mu\)_-alternating path/cycle_

The next lemma ensures that we have highlighted our solution with good probability. The proof of it follows from Lemmas 3 and 4.

**Lemma 5.** _Let_ \((G,\mathcal{L},\mu,k,q,t)\) _be a_ Yes_-instance of_ LS-ASM_. Then with probability at least_ \(\frac{1}{2^{3q+6qd}}\)_, there exists a solution_ \(\eta\) _such that (a) it contains every_

V(uA)
1
1
u1
2
2
W1
3
u2
W2
1
1
2
u3
W3
B
D
1
1
u4
1
W4

**Fig.4.** The zigzag edges represent the edges of the stable matching \(\mu\). The matching \(\eta=\{u_1w_2,u_2w_1,u_3w_3,u_4w_4\}\), and sets _B_ and _D_ are as defined in the Phase I of the algorithm. Vertex colors 1 and 2 in Phase I are represented by **green** and **blue**, respectively. Hence, _G_<sub>1</sub>=_G_\[{_u_<sub>1</sub>_,u_<sub>2</sub>_,u_<sub>4</sub>_,w_<sub>1</sub>_,w_<sub>2</sub>_,w_<sub>4</sub>}\]. The **red** edges represent the edges in \(\mu\triangle\eta\) in Phase II.


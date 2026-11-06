<tbc>description of a randomized algorithm which will be derandomized later using _n- p-q-lopsided universal_ family \[13\]. Given an instance \((G,\mathcal{L},\mu,k,q,t)\) of LS-ASM, we proceed as follows.

**Phase I: Vertex Separation**

Then, the following properties hold for _G_ that is colored using the function _f_:

- Every vertex in \(V(\mu\triangle\eta)\) is colored 1 with probability at least \(\frac{1}{2^{2q}}\).<tbc>

**-** Let _B_ be a set of the neighbors of the vertices in \(V(\mu\triangle\eta)\) outside the set \(V(\mu\triangle\eta)\), that is, \(B=N_G(V(\mu\triangle\eta))\), and _D_ be the set of matching partners of the vertices in _B_, in the matching \(\mu\), if they exist. Every vertex in \(B\cup D\) is colored 2 with probability at least \(\frac{1}{2^{4qd}}\). To see this note that \(|\mu\triangle\eta|\le q\) and the maximum degree of a vertex in the graph _G_ is _d_, and so \(|B\cup D|\le 2|B|=2|N_G(V(\mu\triangle\eta))|\le 4qd\).

For \(i\in[2]\), let _V<sub>i</sub>_ denote the set of vertices of the graph _G_, that are colored _i_ using the function _f_. Summarizing the above mentioned properties we get the following.

**Lemma 3.** _Let V_<sub>1</sub>_,V_<sub>2</sub>_, B and D be as defined above. Then, with probability at least_ \(\frac{1}{2^{2q+4qd}}\), \(V(\mu\triangle\eta)\subseteq V_1\) _and_ \(B\cup D\subseteq V_2\).

Due to Lemma 3, we have the following:

**Corollary 5.** _Every component in_ \(G[V(\mu\triangle\eta)]\) _is also a component in G_\[_V_<sub>1</sub>\] _with probability at least_ \(\frac{1}{2^{2q+4qd}}\).

The proof of Corollary 5 follows from the fact that \(V(\mu\triangle\eta)\subseteq V_1\) and \(B=N_G(V(\mu\triangle\eta))\) is a subset of _V_<sub>2</sub>. Thus, due to Corollary 5, if there exists a component in _C_ containing a vertex \(u\in V(G)\) such that \(\mu(u)\notin C\), then _C_ is not a component in \(G[V(\mu\triangle\eta)]\). Thus, we get the following reduction rule.

**Reduction Rule 1** _If there exists a component in C containing a vertex_ \(u\in V(G)\) _such that_ \(\mu(u)\notin C\)_, then delete the component C from G_\[_V_<sub>1</sub>\].

In light of Corollary 5, to find \(\mu\triangle\eta\), in Phase II, we color the edges of _G_\[_V_<sub>1</sub>\] in order to identify the components of the graph that _only contains edges of_ \(\mu\triangle\eta\).

**Phase II: Edge Separation**

Let _G_<sub>1</sub>=_G_\[_V_<sub>1</sub>\] and let \(G'=G_1[V(\mu\triangle\eta)]\). Then, the following properties hold for the graph _G_<sub>1</sub> that is colored using the function _g_:

Let f be a function that colors each vertex of the graph G independently with color 1 or 2 with probability 1/2 each.

Let g be a function that colors each edge of the subgraph G[V1] independently with colors 1 or 2 with probability 1/2 each.


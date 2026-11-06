_Proof._ We prove the first point of the observation. Assume the contrary, and let \(b\in B\) be a blocked edge that goes from _X_ to _Y_ . Then _T+b_ has a cycle that goes through _b_. This cycle should contain an edge that goes in the opposite direction, from _Y_ to _X_. This is a contradiction, since _T_ does not have such edges.

We now prove the second point of the observation. Since \(b\in\mathrm{Inv}(e)\subseteq B\), we have that _T+b_ contains a cycle _C_, and _e_ belongs _C_, due to _b_ is an inverse edge of _e_. That is, _C_ contains an edge from _X_ to _Y_ . Consequently, _C_ contains an edge from _Y_ to _X_. By definition of _X_ and _Y_ , there is exactly one edge connecting _X_ and _Y_ in _T_, that is, _e_. But \(E(C)\subseteq E(T+b)\), and no edge can go from _X_ to _Y_ in _E(T_). Then _b_ goes from _Y_ to _X_. The proof is complete.

The most crucial property of inverse edges is that, once unblocked by deleting some edges in _T_, we can add them to the remaining graph together without forming any directed cycle.

**Lemma 1.** _Let_ (_G,_**w**) _be a weakly-connected digraph with positive edge weights. Let_ \(S\subseteq E(T)\) _be its tree edge set. Then, the graph T-S_+Inv(_S_) _is acyclic._

_Proof._ Assume the contrary, and _T-S_+Inv(_S_) contains a cycle _C_. While _T-S_ is acyclic, _C_ contains an edge \(b\in\mathrm{Inv}(S)\). Then, there is \(e\in E(T)\) such that \(b\in\mathrm{Inv}(e)\).

Consider _X,Y_ as in Observation 3 for _T_ and _e_. By the second point of Observation 3, _b_ goes from _Y_ to _X_. Then _C_ contains an edge that goes from _X_ to _Y_ . We know that _T_ has only one such edge, that is, _e_, and _C_ does not contain _e_ since \(e\notin S\).

Then, Inv(_S_) contains an edge that goes from _X_ to _Y_ . We know that \(\mathrm{Inv}(S)\subseteq B\), so this edge is blocked. This contradicts the first point of Observation 3 and finishes the proof of the lemma.

## 3.3 Tree edge profits

The strategy that comes naturally from Lemma 1 can informally be described as trading tree edges for the union of all their inverse edges. The profit of this trade is a difference between total weights of tree edges and their inverse edge union. We formalize this intuition.

**Definition 4** (Tree edge profits)**.** Let (_G,_**w**) be a weakly-connected digraph with positive edge weights. For a tree edge \(e\in E(T)\), by

\(\mathbf{p}(G,\mathbf{w},e)=\mathbf{w}(\mathrm{Inv}(e))-\mathbf{w}(e)\)

we denote the _profit_ of _e_ in (_G,_**w**). For a tree edge set \(S\subseteq E(T)\), by

\(\mathbf{p}(G,\mathbf{w},S)=\mathbf{w}(\mathrm{Inv}(S))-\mathbf{w}(S)\)

we denote the _profit_ of _S_ in (_G,_**w**). As usual, we use shortened notation **p**(_e_) and **p**(_S_).

We observe some straightforward properties of edge profits below.

**Observation 4.** _For a weakly-connected digraph with positive edge weights_ (_G,_**w**)_, and tree edge set_ \(S\subseteq E(T)\)_, and an integer_ \(k\ge 0\)_, we have that_

• _If_ \(\mathbf{p}(S)\ge k\)_, then_ (_G,_**w**_,k_) _is a yes-instance of MAS/MaxST._<tbc>

• \(\mathbf{p}(S)\le\sum_{s\in S}\mathbf{p}(s)\).<tbc>

• _If for each distinct_ \(e_1,e_2\in S\) _we have_ \(\mathrm{Inv}(e_1)\cap\mathrm{Inv}(e_2)=\emptyset\)_, then_ \(\mathbf{p}(S)=\sum_{e\in S}\mathbf{p}(e)\).

Throughout our algorithms for MAS/MaxST, we assume that the profit of each single tree edge is at most _k_. Otherwise, we have a yes-instance that is recognizable in polynomial time.


_2._ _If_ \(X'\subseteq G/e\) _is acyclic and has weight at least_ \(\mathbf{w}(T)-\mathbf{w}(e)+k\)_, then X+e is also acyclic and_ \(\mathbf{w}(X+e)\ge\mathbf{w}(T)+k\)_, where X is a subgraph of G whose edge set corresponds to_ \(E(X')\).

_Proof of Claim 1._ Note that edge contraction preserves cycles (both directed and undirected). Then, if there are no cycles after contracting the edge, there were none before the contraction. In particular, if \(T'\) is a spanning tree in _G/e_, then the same edge set together with _e_ forms a spanning tree in _G_. The same argument applies if \(X'\) is an acyclic subgraph in _G/e_. In both cases, the weight of the resulting subgraph in _G_ is increased by **w**(_e_). This proves the second point of the claim.

It remains to show that MaxST in _G/e_ has weight **w**(_T_)-**w**(_e_). Indeed, _T/e_ is a spanning tree of exactly this weight, and any spanning tree in _G/e_ with larger weight would, together with _e_, yield a spanning tree in _G_ heavier than _T_, contradicting the maximality of _T_. \(\lrcorner\)

This claim guarantees that a solution for the reduced instance \((G/e,\mathbf{w}',k)\) always yields a solution for I, where \(\mathbf{w}'\) is the weight function induced by **w** on _G/e_. Consequently, to ensure the safeness of our reduction rules, we only need to prove the converse implication.

We also make use of the following fact about sets of unprofitable edges:

**Claim 2.** _Let X be a subgraph of G and let_ \(E'\subseteq(E(T)\backslash E(X))\) _be a subset of tree edges, each of which is unprofitable. Then_ \(\mathbf{w}(X+E'-Inv(E'))\ge\mathbf{w}(X)\).

_Proof of Claim 2._ Since \(E'\cap E(X)=\emptyset\), it follows that

\(\mathbf{w}(X+E'-Inv(E'))\ge\mathbf{w}(X)+\mathbf{w}(E')-\mathbf{w}(Inv(E'))=\mathbf{w}(X)-\mathbf{p}(E')\)

By Observation 4, we have \(\mathbf{w}(X)-\mathbf{p}(E')\ge\mathbf{w}(X)-\sum_{e^\prime\in E^\prime}\mathbf{p}(e')\). Finally, given that all edges in \(E'\) are unprofitable, we conclude that \(\mathbf{w}(X+E'-Inv(E'))\ge\mathbf{w}(X)\). \(\lrcorner\)

We proceed to the first reduction rule, which helps us limit the number of unprofitable leaves in _T_.

**Reduction Rule 1** (Unprofitable leaf contraction)**.** _Consider a leaf vertex_ \(\ell\) _in T that is not incident to any allowed edge in G, and denote by e the unique tree edge incident to_ \(\ell\)_. If_ \(\mathbf{p}(e)\le 0\)_, contract e._

**Claim 3.** _Reduction Rule 1 is safe._

_Proof of Claim 3._ By Claim 1, it suffices to show that if I is a yes-instance, then \(\mathcal{I}':=(G/e,\mathbf{w}',k)\) is also a yes-instance. Suppose we have an acyclic subgraph \(X\subseteq G\) such that \(\mathbf{w}(X)\ge\mathbf{w}(T)+k\). If \(e\notin E(X)\), consider a subgraph \(\tilde{X}:=X+e-Inv(e)\). Since \(\mathbf{p}(e)\le 0\), by Claim 2, we have \(\mathbf{w}(\tilde{X})\ge\mathbf{w}(X)\ge\mathbf{w}(T)+k\). Also, we claim that \(\tilde{X}\) is acyclic. Assume the contrary. Since _X_ is acyclic, each cycle in \(\tilde{X}\) must contain the edge _e_ and the vertex \(\ell\). By the definition of \(\ell\), it is not incident to _allowed_ edges and to _tree_ edges except _e_. Consider a _blocked_ edge \(e'\) that is incident to \(\ell\). By the definition of a _blocked_ edge, \(T+e'\) contains a directed cycle. Since _e_ is the only edge that is incident to \(\ell\) in _T_, this cycle must contain _e_. Then \(e'\in Inv(e)\) and hence \(e'\notin E(\tilde{X})\). This means that _e_ is the only edge incident to \(\ell\) in \(\tilde{X}\) and hence \(\ell\) cannot lie on any cycle. Then \(\tilde{X}\) is also a valid solution. Therefore, if (_G,_**w**_,k_) is a yes-instance, we always have a solution that contains _e_. Furthermore, we denote such a solution by _X_.

We aim to show that _X/e_ is a valid solution for \(\mathcal{I}'\). This subgraph has weight \(\mathbf{w}(X)-\mathbf{w}(e)\ge(\mathbf{w}(T)-\mathbf{w}(e))+k\). Thus, it remains to prove that _X/e_ is acyclic. Without loss of generality, assume<tbc>


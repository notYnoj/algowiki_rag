<tbc>particular edge related parity requirement satisfies (6.2), where it is required to proceed with one of the two initial steps of the iterative matching process.

6.1.3.2. _Deriving Theorem 6.2._ We state the theorem of Ehard, Glock and Joos \[**18**\], which is for functions on collections of edges in an unweighted graph, and then give a corollary in terms of a weighted _r_-graph. We then derive a version that is stated in terms of functions on collections of vertices, and finally derive Theorem 6.2.

In what follows, we write \(\Delta(H)\) for the maximum vertex degree of a graph _H_, and \(\Delta^\mathrm{co}(H)\) for the maximum pair degree. For \(\bar{e}_l\in\genfrac(){pt}{2}{E(H)}{l}\) consisting of _l_ distinct edges from _E(H_) we say that \(\bar{e}_l\) is a _clean l_-set if the edges in \(\bar{e}_l\) are pairwise disjoint. We write \(\genfrac(){pt}{2}{E(H)}{l}'\) for the set of clean _l_-sets of edges in _H_, and for \(A\subset E(H)\) we denote \(\genfrac(){pt}{2}{E(H)\backslash A}{k}'\) to be the set of clean _k_-sets \(\bar{e}_k\) of edges in _E(H_) such that for every \(e\in\bar{e}_k\), we have \(e\cap a=\emptyset\) for every \(a\in A\). That is, \(\genfrac(){pt}{2}{E(H)\backslash A}{k}'\) denotes the set of clean _k_-sets such that every edge in a _k_-set is disjoint from \(\bigcup_{a\in A}a\). In the theorem that follows, the properties that we consider are functions of clean _l_-sets of edges of the form \(q:\genfrac(){pt}{2}{E(H)}{l}'\rightarrow\mathbb{R}_{\ge 0}\).

Theorem 6.3 (\[**18**\]). _Suppose_ \(\delta\in(0,1)\) _and_ \(r,L\in\mathbb{N}\) _with_ \(r\ge 2\)_, and let_ \(\epsilon:=\delta/50L^2r^2\)_. Then there exists_ \(\Delta_0\) _such that for all_ \(\Delta\ge\Delta_0\)_, the following holds. Let H be an r-uniform hypergraph with_ \(\Delta(H)\le\Delta\) _and_ \(\Delta^\mathrm{co}(H)\le\Delta^{1-\delta}\) _as well as_ \(e(H)\le\mathrm{exp}(\Delta^{\epsilon^2})\)_. Suppose that for each_ \(l\in[L]\) _we are given a set_ Q_<sub>l</sub> of clean l-set weight functions on E(H_) _of size at most_ \(\mathrm{exp}(\Delta^{\epsilon^2})\) _such that_

(6.3) \(q(E(H))\ge\Delta^{k+\delta}\mathrm{max}_{T\in\genfrac(){pt}{2}{E(H)}{k}^\prime}\sum_{S\supseteq T}q(S)\)

_for all_ \(q\in\mathcal{Q}_l\) _and_ \(k\in[l]\).

_Then there exists a matching M in H such that_

\(q(M)=\left(1\pm\frac{\Delta^{-\epsilon}}{2}\right)q(E(H))/\Delta^l\)

_for all_ \(l\in[L]\) _and_ \(q\in\mathcal{Q}_l\).

This theorem shows that we can find matchings in hypergraphs that act similarly to how we would expect things to look if we had picked a set of edges by choosing each edge independently with the same probability \(1/\Delta\). Whilst this result and Theorem 6.2 describe the existence of a single (deterministic) matching satisfying the conclusion for a suitably small collection of functions _p_ and _q_, this is obtained by proving the existence of a distribution on matchings for which each statement holds with high probability, and taking a union bound suffices to show that such a matching exists for which all hold simultaneously. We use this fact throughout the proof, sometimes implicitly moving between the distribution on matchings for which a statement holds with high probability and a fixed matching which satisfies many statements simultaneously. We now derive an equivalent version for weighted _r_-graphs.

Corollary 6.4. _Suppose_ \(\delta\in(0,1)\) _and_ \(r,L\in\mathbb{N}\) _with_ \(r\ge 2\)_, and let_ \(\epsilon:=\frac{\delta}{50L^2r^2}\)_. Then there exists_ \(\Delta_0\) _such that for all_ \(\Delta\ge\Delta_0\)_, the following holds: Let_ (_H,w_) _be an r-uniform weighted hypergraph with_ \(w(e)\ge\Delta^{-1}\) _and_ \(\Delta_w^\mathrm{co}(H)\le\Delta^{-\delta}\) _as well as_ \(e(H)\le\mathrm{exp}(\Delta^{\epsilon^2/4})\).


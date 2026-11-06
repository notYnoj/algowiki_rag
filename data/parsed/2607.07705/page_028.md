**Case** _f(e_<sub>_j_<sub>1</sub></sub>)_\>f(e_<sub>_j_<sub>2</sub></sub>)**.** Since _P_ goes from _e_<sub>1</sub> to _e_<sub>_j_<sub>2</sub></sub> and \(P'\) contains _e_<sub>_j_<sub>2</sub></sub> on the path from _e_<sub>1</sub> to _e_<sub>_j_<sub>1</sub></sub>, we have \(P\subseteq P'\). Hence \(e_i\in P'\) because it lies on _P_. Recall that \(e_1e_{j_1}\in E(H)\). Consider an edge \(e\in\mathrm{Inv}(e_1)\cap\mathrm{Inv}(e_{j_1})\). By the same reasoning as in the first case, we obtain that \(e\in\mathrm{Inv}(e_i)\). Consequently, \(e\in\mathrm{Inv}(e_i)\cap\mathrm{Inv}(e_{j_1})\) and \(e_ie_{j_1}\in E(H)\) again.

In both cases, we have \(e_ie_{j_1}\in E(H)\), which contradicts the definition of an antihole because |_i-j_<sub>1</sub>|=1. Therefore, _H_ contains neither odd holes nor odd antiholes. Consequently, Proposition 3 guarantees that _H_ is a perfect graph.

As shown by Grötschel, Lovász, and Schrijver in \[GLS81\], one can find a maximum-weight independent set in a perfect graph with positive integer vertex weights in polynomial time. We remark that this result can be extended to rational weights of an arbitrary sign.

**Proposition 4** (\[GLS81\], Section 6)**.** _For a perfect graph G with rational vertex weights, a maximum- weight independent set can be found in time polynomial in_ |_V(G_)|+log_C, where C is the maximum among the numerators and denominators of the weights._

_Proof._ First, let \(V'\subseteq V(G)\) be the set of vertices with positive weights. Observe that there always exists a maximum-weight independent set that consists only of vertices from \(V'\). Additionally, the induced subgraph \(G[V']\) is also perfect. Therefore, we may restrict our problem to \(G[V']\) and assume that all weights are positive.

Scaling all weights by a constant does not change which independent set has greater total weight. Thus we can multiply all weights by the least common multiple of their denominators, making them integers. Let _W_ be the maximum resulting weight. Note that _W_ is bounded by _C_<sup>|_V(G_)|</sup> because, in the worst case, each modified weight equals its initial numerator multiplied by the product of the denominators of the other |_V(G_)|-1 weights. Hence \(\mathrm{log}W\le|V(G)|\mathrm{log}C\). Therefore, on the modified instance the algorithm for positive integer weights runs in time polynomial in |_V(G_)|+log_W_, which remains polynomial in |_V(G_)|+log_C_.

Even when certain tree edges are forbidden from _S_ (set _F_), others are required to be in _S_ (set _R_), and a set of blocked edges \(B'\subseteq\mathrm{Inv}(R)\) may be the inverse of multiple edges in _S_, the maximum-profit _S_ can still be found in polynomial time.

**Lemma 7.** _There is a polynomial-time algorithm that given a digraph_ (_G,_**w**) _with rational edge weights, sets_ \(F,R\subseteq E(T)\) _and_ \(B'\subseteq\mathrm{Inv}(R)\)_, finds a set with the maximum_ **p**(_S_) _over all_ \(S\subseteq E(T)\) _such that:_

• \(F\cap S=\emptyset\) _and_ \(R\subseteq S\);<tbc>

• _for every pair of distinct elements_ \(s_1,s_2\in S\)_, it holds that_ \(\mathrm{Inv}(s_1)\cap\mathrm{Inv}(s_2)\subseteq B'\).

_Proof._ Consider a tree edge \(e\in E(T)\) and suppose there exists \(r\in R\) with \(r\neq e\) such that \(\mathrm{Inv}(e)\cap\mathrm{Inv}(r)\unknown\subseteq B'\). Then _e_ cannot belong to any _S_ because given \(R\subseteq S\), including _e_ in _S_ would violate the last constraint. Therefore, we can add all such _e_ to _F_ without changing the set of feasible solutions. Denote the extended set of forbidden edges by \(F'\). If \(F'\cap R\neq\emptyset\), then the first two constraints cannot be satisfied together, and hence there are no feasible sets _S_. From now on, we assume that \(F'\) and _R_ are disjoint.

Consider the graph \(G':=G-B'\), and let \(\mathbf{w}'\) be the restriction of **w** to \(E(G')\). Since \(B'\) consists only of _blocked_ edges, we know that \(E(T)\subseteq E(G')\) and therefore \(\mathrm{MaxST}(G',\mathbf{w}')=T\). Thus from<tbc>


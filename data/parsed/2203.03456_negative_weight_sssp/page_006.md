## 2 Preliminaries

Throughout, we only consider graphs with integer weights. For any weighted graph _G_=(_V,E,w_), define _V(G_)=_V,E(G_)=_E_, and

\(E^{neg}(G):=\{e\in E|w(e)<0\}.\)

Define \(W_G:=max\{2,-min_{e\in E}\{w(e)\}\}\); that is, _W<sub>G</sub>_ is the most negative edge weight in the graph<sup>7</sup>. Given any set of edges \(S\subseteq E\) we define \(w(S)=\sum_{e\in S}w(e)\). We say that a cycle _C_ in _G_ is a negative- weight cycle if _w(C)\<_0. We define dist_<sub>G</sub>(u,v_) to be the shortest distance from _u_ to _v_; if there is a negative-weight cycle on some _uv_-path then we define \(dist_G(u,v)=-\infty\).

Consider graph _G_=(_V,E,w_) and consider subsets \(V'\subseteq V\) and \(E'\subseteq E\). We define \(G[V']\) to be the subgraph of _G_ induced by \(V'\). We slightly abuse notation and denote a subgraph of _G_ as \(H=(V',E',w)\) where the weight function _w_ is restricted to edges in _H_. We define \(G\backslash V'=G[V\backslash V']\) and \(G\backslash E'=(V,E\backslash E',w)\); i.e. they are graphs where we remove vertices and edges in \(V'\) and \(E'\) respectively. We sometimes write _G_\\_v_ and _E_\\_e_ instead of _G_\\{_v_} and _G_\\{_e_}, respectively, for any \(v\in V\) and \(e\in E\). We say that a subgraph _H_ of _G_ has _weak_ diameter _D_ if for any \(u,v\in V(H)\) we have that \(dist_G(u,v)\le D\). We always let _G<sub>in</sub>_ and _s<sub>in</sub>_ refer to the main input graph/source of Theorem 1.1.

**Assumption 2.1** (Properties of input graph _G<sub>in</sub>_; justified by Lemma 2.2)**.** We assume throughout the paper that the main input graph _G<sub>in</sub>_=(_V,E,w<sub>in</sub>_) satisfies the following properties:

1. \(w_{in}(e)\ge-1\) for all \(e\in E\) (thus, _W<sub>G<sub>in</sub></sub>_=2).<tbc>

2. Every vertex in _G<sub>in</sub>_ has constant out-degree.

**Lemma 2.2.** _Say that there is an algorithm as in Theorem 1.1 for the special case when the graph G<sub>in</sub> satisfies the properties of Assumption 2.1, with running time T(m,n). Then there is algorithm as in Theorem 1.1 for any input graph G<sub>in</sub> with integral weights that has running time O(T(m,m_)log(_W<sub>G<sub>in</sub></sub>_)).

_Proof._ Let us first consider the first assumption, i.e that \(w_{in}(e)\ge-1\). The scaling framework of Goldberg \[Gol95\] shows that an algorithm for this case implies an algorithm for any integer-weighted _G_ at the expense of an extra log(_W<sub>G</sub>_) factor.<sup>8</sup>

For the assumption that every vertex in _G<sub>in</sub>_ has constant out-degree, we use a by-now standard technique of creating \(\Theta\)(out-degree(_v_)) copies of each vertex _v_, so that each copy has constant out-degree; the resulting graph was _O(E_) vertices and _O(E_) edges.<sup>9</sup>

**Dummy Source and Negative Edges.** The definitions below capture a common transformation we apply to negative weights and also allow us to formalize the number of negative edges on a shortest path. Note that most of our algorithms/definitions will not refer to the input source _s<sub>in</sub>_, but instead to a dummy source that has edges of weight 0 to every vertex.

<sup>7</sup>We set \(W_G\ge 2\) so that we can write log(_W<sub>G</sub>_) in our runtime <sup>8</sup>Quoting \[Gol95\]: "Note that the basic problem solved at each iteration of the bit scaling method is a special version of the shortest paths problem where the arc lengths are integers greater or equal to -1." <sup>9</sup>One way to do this is to replace every vertex with a directed zero-weight cycle whose size is the in-degree plus out-degree of the vertex and then attach the adjacent edges to this cycle.


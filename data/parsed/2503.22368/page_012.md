## A Basic Definitions

A _subgraph_ of a graph _G_=(_V,E_) is a graph _H_=(_V<sub>H</sub>,E<sub>H</sub>_) satisfying \(V_H\subseteq V\) and \(E_H\subseteq E\), with the additional requirement that every edge in _E<sub>H</sub>_ has both endpoints in _V<sub>H</sub>_.

An important special case is the _induced subgraph_. For any subset \(S\subseteq V\) , the induced subgraph of _G_ on _S_, denoted by _G_\[_S_\], is defined by setting _V_<sub>_G_\[_S_\]</sub>=_S_ and \(E_{G[S]}=\big\{\{u,v\}\in E|u\in S,v\in S\big\}\). In essence, _G_\[_S_\] contains all vertices in _S_ and every edge of _G_ whose endpoints are both contained in _S_.

Let _G_=(_V,E_) and _H_=(_W,F_) be two graphs. An _isomorphism_ between _G_ and _H_ is a bijection \(\varphi:V\rightarrow W\) that preserves adjacency; that is, for all \(u,v\in V\) , \(\{u,v\}\in E\) if and only if \(\{\varphi(u),\varphi(v)\}\in F\). When such a bijection exists, we say that _G_ and _H_ are _isomorphic_ and write \(G\cong H\).

We also recall the definition of a _clique_ in a graph _G_. A clique is a subset of vertices \(C\subseteq V\) with the property that for every two distinct vertices \(u,v\in C\), the edge {_u,v_} is present in _E_. A clique _C_ is termed _inclusion-maximal_ if no vertex \(w\in V\backslash C\) can be added to _C_ while preserving the clique property; that is, there exists no _w_ for which \(C\cup\{w\}\) is also a clique.

Finally, a _uv-path_ in _G_ is defined as a sequence of vertices _u=v_<sub>0</sub>_,v_<sub>1</sub>_,...,v<sub>k</sub>=v_, such that for every index \(0\le i<k\), the edge {_v<sub>i</sub>,v_<sub>_i_+1</sub>} belongs to _E_.

## B Proof of Lemma 1 and Proposition 1

In the following sections, we use the definitions above to prove Lemma 1 and Proposition 1.

**Lemma 1.** _Let G_<sub>1</sub>_,...,G<sub>n</sub> be graphs. If H is a maximal common induced subgraph of G_<sub>1</sub>_,...,G<sub>n</sub>, then there exists a maximal clique K in_ \(\star_{i=1}^nG_i\) _of size_ |_V(K_)|=|_V(H_)| _and for which the projection p<sub>i</sub> onto the i-th factor satisfies_ \(p_i(K)=H_i\simeq H\).

_Proof._ Let _G_<sub>1</sub>_,...,G<sub>n</sub>_, be graphs. Put \(G:=\star_{i=1}^nG_i\). Suppose first that _H_ be a maximal common induced subgraph of _G_<sub>1</sub>_,...,G<sub>n</sub>_. By Definition, for every _i_, there is an isomorphism _f<sub>i</sub>_ from _H_ to \(H_i\subseteq G_i\). Note that \(H\simeq H_i\) for all \(i\in\{1,\dots,n\}\) implies that \(H_i\simeq H_j\) for all \(i,j\in\{1,\dots,n\}\). Now consider the map \(\varphi_i:V(H_1)\rightarrow V(H_i)\) defined by \(\varphi_i:=f_i\circ f_1^{-1}\) for all \(i\in\{1,\dots,n\}\). It is easy to verify that \(\varphi_i\) is a subgraph isomorphism between \(H_1\subseteq G_1\) and \(H_i\subseteq G_i\) for all \(i\in\{1,\dots,n\}\). Note that \(\varphi_1\) is the identity map on _V(H_<sub>1</sub>), i.e., \(\varphi_1(w)=w\) for all \(w\in V(H_1)\). Consider now the subgraph _K_ of _G_ that is induced by \(\{(u,\varphi_2(u),\dots,\varphi_n(u))|u\in V(H_1)\}\). In particular, |_V(K_)|=|_V(H_<sub>1</sub>)|=|_V(H_)|. Note that the projection _p_<sub>1</sub> satisfies \(p_i(u,\varphi_2(u),\dots,\varphi_n(u))\) for all \(u\in V(H_1)\) and thus, \(p_1(K)=H_1\simeq H\). Note that the choice of _H_<sub>1</sub> as "basis" is arbitrary, i.e., we could have started with every subgraph \(H_j\subseteq G_j\) with \(H_j\simeq H\) to establish such a map \(\varphi_i\) via \(f_i\circ f_j^{-1}\) which implies that \(p_j(K)=H_j\simeq H\).

We show now that _K_ is a clique in _G_. Assume, for contradiction, that _K_ is not complete. Hence, there are vertices \(a=(a_1,\dots,a_n),b=(b_1,\dots,b_n)\in\)


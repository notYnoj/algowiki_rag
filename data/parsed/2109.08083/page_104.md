<tbc>Finally we consider \(\delta_{H_1^*,v}:=w_{1^*}(E_{H_1^*}(v,I_{t_2}))\). By Corollary 6.16 we have that there exist constants \(\delta^\pm>0\) such that \(\delta^-\le\frac{w_{1^*}(E_{H_1^*}(v,I_{t_2}))}{w_{1^*}(E_{H_1^*}(v,I_{t_1}))}\le\delta^+\). Furthermore, \(1\ge w_{1^*}(E_{H_1^*}(v,I_{t_1}))\ge 1-t_1^{-\epsilon_1}\). Thus

\((1-t_1^{-\epsilon_1})\delta^-\le w_{1^*}(E_{H_1^*}(v,I_{t_2}))\le\delta^+,\)

and taking \(\delta_{1^*}^-=\delta^-/2\) and \(\delta_{1^*}^+=\delta^+\) completes the proof. □

We want to show that removing a particular matching from some _i_-permissible \((G,\omega)\), we may obtain a subgraph with some ‘nice’ properties. We shall end up (in Section 6.2 and in particular Subsection 6.4.2) ensuring that our nested subgraphs (_H<sub>i</sub>,w<sub>i</sub>_) are each _i_-permissible, but first we use the definition of _i_-permissibility here to show that _given_ a particular weighted graph \((G,\omega)\) is _i_-permissible, we can always define a subgraph _G<sup>o</sup>_ of _G_ with weight function \(\omega^o:=\omega|_{G^o}\) such that \((G^o,\omega^o)\) satisfies the hypotheses of Theorem 6.2. This is key, since we use Theorem 6.2 to remove a matching _M<sup>o</sup>_ from \((G^o,\omega^o)\) which we’ll show (due to the _i_-permissibility of \((G,\omega)\)) covers most vertices in _I<sub>t<sub>i</sub></sub>_\\_I_<sub>_t<sub>i</sub>_+1</sub>, and does so in a way that ensures that the subgraph \(G'\subseteq G\) with \(V(G'):=V(G)\backslash V(M^o)\) and \(E(G')=E(G[V(G')])\) has many nice properties.

Proposition 6.24. _Suppose that_ \((G,\omega)\) _is i-permissible for some i. Then_ \((G,\omega)\) _is not j-permissible for all_ \(j\neq i\).

Proof. First note that by (P1), \(G\subseteq H_{1^*}[I_{t_i}]\). Furthermore, by (P4) we have that \(V(G)\cap(I_{t_i}\backslash I_{t_{i+1}})\neq\emptyset\), since _I<sub>t<sub>i</sub></sub>_\\_I_<sub>_t<sub>i</sub>_+1</sub> is itself an _i_-valid subset. Thus, \(G\unknown\subseteq H_{1^*}[I_{t_{i+1}}]\) and so \((G,\omega)\) is not _j_-permissible for all \(j\ge i+1\). Furthermore, we see that, supposing \((G,\omega)\) is _j_-permissible for _j\<i_, again from (iv) we must have \(V(G)\cap I_{t_j}\backslash I_{t_{j+1}}\neq\emptyset\), but since \(G\subseteq H_{1^*}[I_{t_i}]\) this is clearly not possible. Hence \((G,\omega)\) is not _j_-permissible for any \(j\le i-1\) and the proposition holds. □

Given Proposition 6.24, and an _i_-permissible pair \((G,\omega)\) we may subsequently define \(G^o\subseteq G\) as follows (noting that _G<sup>o</sup>_ is well defined due to Proposition 6.24). For fixed _i_ such that \((G,\omega)\) is _i_-permissible, we define<tbc>

\(E(G^o):=\{e\in G:e\cap(I_{t_i}\backslash I_{t_{i+1}})\neq\emptyset\}\text{and}V(G^o):=\bigcup_{e\in E(G^o)}e.\)

<tbc>We let

\(\omega^o:=\omega|_{G^o}\)

be the restriction of \(\omega\) to edges in _G<sup>o</sup>_. We write

\(d_{\omega^o}(v):=d_{\omega^o,G^o}(v)\)

for every \(v\in V(G^o)\).

Proposition 6.25. _Given an i-permissible pair_ \((G,\omega)\) _for some i, for every_ \(v\in V(G[I_{t_{i+1}}])\) _we have that_<tbc>

\(\omega(E_G(v,I_{t_{i+1}}))+d_{\omega^o}(v)=d_{\omega,G}(v),\)

<tbc>_and consequently,_

\(\frac{\omega(E_G(v,I_{t_{i+1}}))}{1-d_{\omega^o}(v)}\le 1.\)


<tbc>Definition 6.10 (Depth). We say that _H<sub>i</sub>_ has _depth j_ if \(V(H_i)\subseteq K_{j-1}\) but \(V(H_i)\unknown\subseteq K_j\). We say that _v_ has _depth j_ if \(v\in K_{j-1}\backslash K_j\), and \(S\subseteq V(\mathcal{T})\) has _depth j_ if \(S\subseteq K_{j-2}\backslash K_j\) and \(S\cap K_{j-1}\neq\emptyset\).

Note that \(V(H_{1^*})\subseteq K_{-1}\) and \(V(H_{1^*})\unknown\subseteq K_0\), so _H_<sub>1<sup>∗</sup></sub> has depth 0. Furthermore, recall that for every \(j\in[c_g]\) there exists \(i\in[c_h]\) such that _I<sub>t<sub>i</sub></sub>=K<sub>j</sub>_ (recalling Set-up 3.1 and how _c_<sub>vor</sub> was defined such that \(-\frac{loglog(n)}{log(c_\mathrm{vor})}\) is an integer). As a result this will give that _H<sub>i</sub>_ and _V(H<sub>i</sub>_) have the same depth.

Definition 6.11 (Permissible sets). We say that (_v,S_) is a _closed i-permissible pair_ if (_v,S_) is a closed _i_-valid pair and there exists \(l\in[0,c_g]\) such that _v_ has depth _l_ and \(V(E_\mathcal{T}(v,S,S,S))\subseteq K_{l-2}\backslash K_{l+1}\). We also say that (_v,S_) is an _open i- permissible pair_ if (_v,S_) is an open _i_-valid pair and there exists \(l\in[0,c_g]\) such that _v_ has depth _l_ and \(V(E_\mathcal{T}(v,S,*,*))\subseteq K_{l-2}\backslash K_{l+1}\). We say that something is _permissible_ if there exists \(i\in[0,c_h]\) such that it is _i_-permissible.

Note that by nature of (_v,S_) being an _i_-valid pair, we implicitly have that \(v\in I_{t_i}\) and \(S\subseteq I_{t_i}\) and, since _v_ has depth _l_, \(v\in K_{l-1}\backslash K_l\) and in _H_<sub>1<sup>∗</sup></sub> all edges containing _v_ are in _K_<sub>_l_-2</sub>\\_K_<sub>_l_+1</sub>. Using the properties of (_H_<sub>1</sub>_,w_<sub>1</sub>) as given in Theorem 6.1, we show that Algorithm 6.9 does not abort prematurely and leads to (_H_<sub>1<sup>∗</sup></sub>_,w_<sub>1<sup>∗</sup></sub>) with properties as listed in the following theorem:

Theorem 6.12. _From running Algorithm 6.9 we obtain the weighting w_<sub>1<sup>∗</sup></sub>:=_w_<sub>(1,0)</sub>_, which is an almost-perfect fractional matching for H_<sub>1</sub> _and H_<sub>1<sup>∗</sup></sub>_, (such that E(H_<sub>1<sup>∗</sup></sub>) _does not contain any bad edges and all edges which are not bad in H_<sub>1</sub> _are contained in E(H_<sub>1<sup>∗</sup></sub>)_), with the following properties:_

(_i)_ \(d_{w_{1^*},H_{1^*}}(v)\ge 1-t_1^{-\epsilon_1}\) _for every_ \(v\in V(H_1)\),<tbc>

_(ii)_ _there exist absolute constants_ \(0<c_{1,1}^*<c_{1,2}^*\) _such that for every_ \(i\in[c_g]\) _and every edge e<sub>i</sub> of type_ \((\alpha,\beta,0)_i\) _with_ \(\alpha\neq 0\),<tbc>

<tbc>\(\frac{c_{1,1}^*}{p_\mathrm{gr}^3k_ilog(n)}\le w_{1^*}(e_i)\le\frac{c_{1,2}^*}{p_\mathrm{gr}^3k_ilog(n)},\)<tbc>

<tbc>_and edges e in H_<sub>1</sub> _with all vertices outside K_<sub>1</sub> _satisfy_<tbc>

<tbc>\(\frac{c_{1,1}^*}{p_\mathrm{gr}^3t_1}\le w_{1^*}(e)\le\frac{c_{1,2}^*}{p_\mathrm{gr}^3t_1},\)<tbc>

_(iii)_ _for every_ 1_-valid subset_ \(S\subseteq\mathcal{T}\) _we have that_ |_V(H_<sub>1<sup>∗</sup></sub>\[_S_\])|=|_V(H_<sub>1</sub>\[_S_\])|,<tbc>

_(iv)_ _for every open or closed_ 1_-permissible pair_ (_v,S_) _(given by a tuple_ (_v,S,S,S_) _or_ (_v,S,∗,∗))_, we have that_ |_E_<sub>_H_<sub>1<sup>∗</sup></sub></sub>(_v,S_)|=|_E_<sub>_H_<sub>1</sub></sub>(_v,S_)|.

Theorem 6.12 confirms that Algorithm 6.9 not only reduces the weight on all bad edges to 0, but also shows that no other edges in _H_<sub>1</sub> have their weight reduced to 0, and more specifically gives a fairly precise window for the weight of each type of edge. (Note that an edge of type (0,4,0)_<sub>i</sub>_ is an edge of type (4,0,0)<sub>_i_+1</sub>, so every type of edge really is considered by Theorem 6.12.) Furthermore, note that Theorem 6.12(iii) and (iv) are both trivial consequences of the definition of _H_<sub>1<sup>∗</sup></sub>. We leave them in the statement of the theorem as we shall have results in subsequent sections that follow a similar shape to that of Theorem 6.12, but where the conditions on the size of vertex subsets and degree-type properties are not a trivial consequence in the same way they are here. We describe the process


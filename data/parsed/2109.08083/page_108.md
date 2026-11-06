<tbc>for every \(l\in[3]\) since for every edge in _E_<sub>_G<sup>o</sup>_</sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) there is at least one tuple counted in the sum that is contained in the edge and therefore returns a 1 in the indicator function. Again by _i_-permissibility and |_S_<sub>1</sub>| it follows that,

(6.16) \(\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G^o)}{l}}q_{(G^o,v,S_1,S_2,S_3)}^{(l)}(\bar{v})\ge|E_{G^o}(v,S_1,S_2,S_3)|\ge\frac{|S_1|p_\mathrm{gr}^3}{\mathrm{log}^{l_3}(n)}\ge\frac{p_\mathrm{gr}^3t_i}{\mathrm{log}^{l_3+2}(n)},\)

for each \(l\in[3]\) and so it follows that (6.15) also holds here. Then by Proposition 6.17 and Corollary 6.27, the first statement of (K2) holds.

More generally considering the functions in Section 6.3.1.2 so that additionally \(\frac{\mathrm{max}_{e\in E_{G^o}(v,S_1,S_2,S_3)}f_v(e)}{\mathrm{min}_{e\in E_{G^o}(v,S_1,S_2,S_3)}f_v(e)}\le\mathrm{log}^{500}(n)\), we have that<tbc>

\(\mathrm{max}_{\bar{v}\in\genfrac(){pt}{2}{V(G^o)}{l}}q_{(G^o,v,S_1,S_2,S_3)}^{(l)}(\bar{v})\le\mathrm{max}_{e\in G^o}f_v(e),\)

<tbc>and, as in the previous case, \(\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G^o)}{l}}q_{(G^o,v,S_1,S_2,S_3)}^{(l)}(\bar{v})\ge f_v(E_{G^o}(v,S_1,S_2,S_3))\) for every \(l\in[3]\), since for every edge \(e\in E_{G^o}(v,S_1,S_2,S_3)\) there is at least one tuple counted in the sum on the LHS that is contained in the edge _e_ and therefore contributes at least _f<sub>v</sub>(e_) to the LHS, and the RHS contributes exactly _f<sub>v</sub>(e_) for every such edge _e_. Hence

\(\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G^o)}{l}}q_{(G^o,v,S_1,S_2,S_3)}^{(l)}(\bar{v})\ge|E_{G^o}(v,S_1,S_2,S_3)|\mathrm{min}_{e\in G^o}f_v(e).\)

By (6.16) and since \(\frac{\mathrm{max}_{e\in E_{G^o}(v,S_1,S_2,S_3)}f_v(e)}{\mathrm{min}_{e\in E_{G^o}(v,S_1,S_2,S_3)}f_v(e)}\le\mathrm{log}^{500}(n)\) we again have that (6.15) holds here. Once again combining Proposition 6.17 and Corollary 6.27 we obtain the second statement of (K2). To see the final statement of (K2), consider a fixed vertex _v_ and let \(\omega_v(e)=\omega(e)\) if \(v\in e\) and \(\omega_v(e)=0\) otherwise. Then \(\frac{\mathrm{max}_{e\in E_{G^o}(v,S_1,S_2,S_3)}\omega_v(e)}{\mathrm{min}_{e\in E_{G^o}(v,S_1,S_2,S_3)}\omega_v(e)}\le\frac{\mathrm{log}^{l_1+2}(n)}{c_1}\le\mathrm{log}^{13}(n)\) and \(\omega_v\) is a function as per the second statement of (K2). Thus

\(\omega_v(E_{G^\prime}(v,S_1,S_2,S_3))=\)<br>
\((1\pm t_i^{-\epsilon_1}\mathrm{log}^{3l_3+7}(n))\sum_{e\in E_G(v,S_1,S_2,S_3)}\omega_v(e)\prod_{u\in e\backslash\{v\}}(1-d_{\omega^o}(v)),\)

but by definition, \(\omega_v(E_{G^\prime}(v,S_1,S_2,S_3))=\omega(E_{G^\prime}(v,S_1,S_2,S_3))\) and so

\(\sum_{e\in E_G(v,S_1,S_2,S_3)}\omega_v(e)\prod_{u\in e\backslash\{v\}}(1-d_{\omega^o}(v))=\sum_{e\in E_G(v,S_1,S_2,S_3)}\omega(e)\prod_{u\in e\backslash\{v\}}(1-d_{\omega^o}(v)),\)

so the final statement of (K2) also holds. Hence, by (6.13), Proposition 6.17 and Theorem 6.2 there exists a matching _M<sup>o</sup>_ in _G<sup>o</sup>_ such that in \(G'=G[V(G)\backslash V(M^o)]\) the properties in (K1) and (K2) which refer to _i_-reachable vertices, edges and subsets contained in _I_<sub>_t<sub>i</sub>_+1</sub> all hold.

It remains to consider what happens to the other vertices, edges and sets considered in (K1) and (K3). Indeed, every subset \(S\subseteq K_{j+1}\) satisfies \(S\cap V(G^o)=\emptyset\), since sets in _K_<sub>_j_+1</sub> are not _i_-reachable, and _G<sup>o</sup>_ is defined only to include vertices in sets which are _i_-reachable. Thus removing a matching \(M^o\subseteq G^o\) removes no vertices from _V(G_\[_S_\]). Thus, by _i_-permissibility, |_V(G_\[_S_\])|=|_V(H_<sub>1∗</sub>\[_S_\])| for all such _S_. For (K3) we argue in the same way. In particular, by definition of _G<sup>o</sup>_, the matching _M<sup>o</sup>_ only uses edges containing a vertex in _I<sub>t<sub>i</sub></sub>_\\_I_<sub>_t<sub>i</sub>_+1</sub> and since \(G\subseteq H_{1*}[I_{t_i}]\),


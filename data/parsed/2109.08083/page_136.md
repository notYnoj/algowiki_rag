<tbc>that Plan 6.34 completes to reach _L_<sup>∗</sup>. In particular, we have shown that, assuming Theorem 6.1, the _vortex_ completes, allowing us to obtain a matching covering all vertices in _V(H_<sub>gr</sub>)\\_A_<sup>∗</sup> but a qualifying leave _L_<sup>∗</sup>. We discussed how a qualifying leave is absorbed by _A_<sup>∗</sup> in Section 5.2, thus we have proved Lemma 5.6. Hence in order to prove Theorem 1.2, all remains is to prove Theorem 6.1, which is done in the following section.

## 6.5. Initial steps

It remains to bridge the gap between Theorem 3.28 and Theorem 6.1. Recall that _H_ has the following properties (as per Theorem 3.28):

(i) every T -valid subset \(S\subseteq V(\mathcal{T})\) satisfies<tbc>

<tbc>\(|V(H[S])|=(1\pm\alpha_G)|S|p_\mathrm{gr},\)<tbc>

(ii) for every \(v\in V(H)\) and every open or closed T -valid tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>), we have<tbc>

<tbc>\(|E_H(v,S_1,S_2,S_3)|=(1\pm\alpha_G)|E_\mathcal{T}(v,S_1,S_2,S_3)|p_\mathrm{gr}^3,\)<tbc>

(iii) for every \(i\in[c_g]\),<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H}^+(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm\alpha_G)|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12} & \text{if}e\text{is a bad edge,} \\
O\left(k_it_1p_\mathrm{gr}^{12}\right) & \text{if}\alpha=0,\beta=1,\gamma=3, \\
0 & \text{otherwise.}
\end{array}\right.\)<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H}^-(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm\alpha_G)|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12} & \text{if}\alpha\neq 0\text{and}\gamma=0, \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{if}\alpha=0,\beta=0,\gamma=4, \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{if}\alpha=0,\beta=1,\gamma=3, \\
0 & \text{otherwise.}
\end{array}\right.\)<tbc>

<tbc>Finally, for every bad edge _e_,<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H}^2|=O\left(k_it_1p_\mathrm{gr}^{12}\right).\)<tbc>

(iv) \(|V_O^{X+Y}(H)|=|V_O^{X-Y}(H)|\), and, furthermore \(|V_O^J(H)|=(1\pm 2\alpha_G)|V_E^J(H)|\) for every \(J\in\{X,Y,X+Y,X-Y\}\). Additionally, \(|V_{O/E}^{J_1}(H[S])|=(1\pm 2\alpha_G)|V_{O/E}^{J_2}(H[S])|\) for every valid layer interval _S_, and \(J_1,J_2\in\{X,Y,X+Y,X-Y\}\).<tbc>

(v) For every \(J\in\{X,Y,X+Y,X-Y\}\) and every valid _J_-layer interval _I<sup>J</sup>_ and \(v\notin J\),<tbc>

<tbc>\(|E_H(v,I^J,O/E)|=(1\pm\alpha_G)|E_\mathcal{T}(v,I^J,O/E)|p_\mathrm{gr}^3.\)<tbc>

<tbc>As previously mentioned, the strategy is similar to that of Plan 6.34, but for some key differences. We start by assigning a weight function _w<sub>H</sub>_ to _H_ as in Theorem 3.28, such that _w<sub>H</sub>_ is an almost-perfect fractional matching for _H_ and we use Theorem 6.2 in a similar form to Theorem 6.28 on \((H^o,w_H^o)\), the graph containing all edges in _H_ with a vertex in _V(H_)\\_I_<sub>_t_<sub>0</sub></sub>, and all vertices induced by this collection of edges, to find a matching \(M_H^o\), as in Step 1 of Plan 6.34. Using Theorem 6.2 to obtain the matching \(M_H^o\) means that we may have used unequal numbers of edges of each wrap-around type. Recalling that we have certain parity requirements of _L_<sup>∗</sup> at the end of the process, we wish to correct for any unevenness at this stage. (Note that this is only necessary when _n_ is odd. Due to the nature of our process removing disjoint edges, when _n_ is even removal of a matching cannot


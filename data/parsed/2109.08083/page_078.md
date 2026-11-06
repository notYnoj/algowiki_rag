\(|\mathcal{Z}_{i,e,H_\mathrm{gr}}^-(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm 2b^{1/3}p_\mathrm{gr}^{-12})|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12} & \text{if}\alpha\neq 0\text{and}\gamma=0\text{,} \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{if}\alpha=0\text{,}\beta=0\text{,}\gamma=4\text{,} \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{if}\alpha=0\text{,}\beta=1\text{,}\gamma=3\text{,} \\
0 & \text{otherwise.}
\end{array}\right.\)

Finally, for every bad edge _e_,<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H_\mathrm{gr}}^2|=O\left(k_it_1p_\mathrm{gr}^{12}\right).\)<tbc>

(iv) \(|V_O^J(H_\mathrm{gr})|=(1\pm 4b^{1/3}p_\mathrm{gr}^{-1})|V_E^J(H_\mathrm{gr})|\) for every \(J\in\{X,Y,X+Y,X-Y\}\). Additionally, \(|V_{O/E}^{J_1}(H_\mathrm{gr}[S])|=(1\pm 4b^{1/3}p_\mathrm{gr}^{-1})|V_{O/E}^{J_2}(H_\mathrm{gr}[S])|\) for every valid layer interval _S_, and \(J_1,J_2\in\{X,Y,X+Y,X-Y\}\).<tbc>

(v) For every \(J\in\{X,Y,X+Y,X-Y\}\) and every valid _J_-layer interval _I<sup>J</sup>_ and \(v\notin J\),

\(|E_{H_\mathrm{gr}}(v,I^J,O/E)|=(1\pm 2b^{1/3}p_\mathrm{gr}^{-3})|E_\mathcal{T}(v,I^J,O/E)|p_\mathrm{gr}^3.\)

Then, having reached _H_gr, we greedily remove a matching _M_gr containing at most 2_b_<sup>1/3</sup>_n_ wrap-around edges avoiding _I_<sub>_t_<sub>0/4</sub></sub> from _H_gr, as discussed above, to obtain _H_:=_H_gr\[_V(H_gr)\\_V(M_gr)\]. We show that this graph satisfies the conditions of Theorem 3.28.

First note that the bounds listed for each property in relation to _H_gr are upper bounds for the same properties in _H_, since we only _removed_ vertices and edges. Since _S_ is T -valid if and only if _S=I<sub>t<sub>i</sub></sub>_ or _S=I<sub>t<sub>i</sub></sub>_\\_I<sub>t<sub>j</sub></sub>_ for some \(i\in[0,c_h]\) and _j\>i_. In particular, then, removing at most 8_b_<sup>1/3</sup>_n_ vertices from outside _I_<sub>_t_<sub>0/4</sub></sub> is affecting only T -valid subsets which have size \(\Theta(t_0p_\mathrm{gr})\). Then for such _S_ we have that \(|V(H_\mathrm{gr}[S])|\ge|V(H[S])|\ge(1\pm 2b^{1/3}p_\mathrm{gr}^{-1})|S|p_\mathrm{gr}-8b^{1/3}n\ge(1\pm b^{1/3}p_\mathrm{gr}^{-1}\mathrm{log}(n))|S|p_\mathrm{gr}\). Since \(\alpha_G\gg b^{1/3}p_\mathrm{gr}^{-1}\mathrm{log}(n)\), (i) holds.

Similarly for (ii), removing 8_b_<sup>1/3</sup>_n_ vertices from outside _I_<sub>_t_<sub>0/4</sub></sub> could remove at most 24_b_<sup>1/3</sup>_n_ edges containing a fixed vertex _v_ and these edges are only containing in subsets such that \(|E_{H_\mathrm{gr}}(v,S_1,S_2,S_3)|=\Theta(np_\mathrm{gr}^3)\). Thus we again find that \(|E_{H_\mathrm{gr}}(v,S_1,S_2,S_3)|\ge|E_H(v,S_1,S_2,S_3)|\ge(1\pm b^{1/3}p_\mathrm{gr}^{-3}\mathrm{log}(n))|E_\mathcal{T}(v,S_1,S_2,S_3)|p_\mathrm{gr}^3\), where again \(\alpha_G\gg b^{1/3}p_\mathrm{gr}^{-3}\mathrm{log}(n)\), so (ii) holds.

For zero-sum configurations, note that we are only interested in the changes to configurations containing a fixed bad edge or edge of type \((\alpha,\beta,0)_i\) with \(\alpha\neq 0\) and for any \(i\in[c_g]\). In these cases, the removal of 8_b_<sup>1/3</sup>_n_ vertices from outside _I_<sub>_t_<sub>0/4</sub> could remove at most _O(b_<sup>1/3</sup>_nj<sub>i</sub>_) zero-sum configurations for a bad edge _e_ and at most _O(b_<sup>1/3</sup>_nt_<sub>1</sub>) configurations for an edge of type \((\alpha,\beta,0)_i\) with \(\alpha\neq 0\) for any _i_. By Fact 3.24 each _i_-bad edge is in \(\Theta(j_it_1)\) configurations and each edge of type \((\alpha,\beta,0)_i\) with \(\alpha\neq 0\) is in \(\Theta(t_1^2)\) configurations for any _i_. Thus, as with (i) and (ii), we get that for every bad edge _e_ and for every edge of type \((\alpha,\beta,0)_i\) with \(\alpha\neq 0\) for any _i_ we have that

\(|\mathcal{Z}_{i,e,H}^+(\alpha,\beta,\gamma)|=(1\pm b^{1/3}p_\mathrm{gr}^{-12}\mathrm{log}(n))|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12},\)

as required. For (iv) note that this is similar to (i) though now a valid layer interval could have size \(\alpha_G^2n\), where 2_b_<sup>1/3</sup>_n_ vertices have been removed. Then in the worst case we have that \(|V_O^J(H_\mathrm{gr}[S])|\ge|V_O^J(H[S])|\ge|V_O^J(H_\mathrm{gr}[S])|-2b^{1/3}n\ge|V_O^J(H_\mathrm{gr}[S])|(1-b^{1/3}p_\mathrm{gr}^{-1}\alpha_G^{-2}\mathrm{log}(n))\), where \(\alpha_G\gg b^{1/3}p_\mathrm{gr}^{-1}\alpha_G^{-2}\mathrm{log}(n)\), satisfying (iv).


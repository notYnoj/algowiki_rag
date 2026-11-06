<tbc>For (iii) the details are similar. First note that we only need to consider bad edges and edges of type \((\alpha,\beta,0)_i\) where \(\alpha\neq 0\) and for every \(i\in[c_g]\), since the process only removes zero-sum configurations and by Theorem 3.28 the claims for all other edge types are already satisfied. Then, recalling the notation from Section 6.3.1.3, \(\mathrm{max}_{\bar{v}\in\genfrac(){pt}{2}{V(H^o)}{l}}f_{Z_{i,e,H}^\pm(\alpha,\beta,\gamma)}^{(l)}(\bar{v})=O(t_1)\) and \(\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H^o)}{l}}f_{Z_{i,e,H}^\pm(\alpha,\beta,\gamma)}^{(l)}(\bar{v})=\Omega(t_1j_ip_\mathrm{gr}^{12})\) for each edge _e_ under consideration. Then since \(j_ip_\mathrm{gr}^{12}\gg t_0^{2\eta}\) for all _i_ we still have that (6.15) holds. □

Corollary 6.67. _In_ \(H^c:=H[V(H)\backslash V(M_H^o)]\)_, we have that_

(_i)_ _every_ 0_-valid subset_ \(S\subseteq\mathcal{T}\) _satisfies_<tbc>

<tbc>\(|V(H^c[S])|=\Theta\left(|S|p_\mathrm{gr}\right),\)<tbc>

_(ii)_ _every open and closed_ 0_-valid tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _satisfies_<tbc>

<tbc>\(|E_{H^c}(v,S_1,S_2,S_3)|=\Theta\left(|E_\mathcal{T}(v,S_1,S_2,S_3)|p_\mathrm{gr}^3\right)\)<tbc>

_(iii)_ _for every_ \(i\in[c_g]\),<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H^c}^+(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
\Theta\left(|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12}\right) & \text{\textit{if}}e\text{\textit{is a bad edge,}} \\
O\left(k_it_1p_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0,\beta=1,\gamma=3, \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H^c}^-(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
\Theta\left(|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha\neq 0\text{\textit{and}}\gamma=0, \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0,\beta=0,\gamma=4, \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0,\beta=1,\gamma=3, \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)<tbc>

<tbc>_Finally, for every bad edge e,_<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H^c}^2|=O\left(k_it_1p_\mathrm{gr}^{12}\right).\)<tbc>

_(iv)_ _For every_ \(J\in\{X,Y,X+Y,X-Y\}\) _and every valid J-layer interval_ \(S\subseteq I_{t_0}\),<tbc>

<tbc>\(|V_{O/E}^J(H^c[S])|=\Theta\left(|V(\mathcal{T}_{O/E}^J[S])|p_\mathrm{gr}\right),\)<tbc>

_(v)_ _For every_ \(J\in\{X,YX+Y,X-Y\}\) _and every valid J-layer interval_ \(I^J\subseteq I_{t_0}\) _and_ \(v\notin J\) _with_ \(v\in V(H^c)\),<tbc>

<tbc>\(|E_{H^c}(v,I^J,O/E)|=\Theta\left(|E_\mathcal{T}(v,I^J,O/E)|p_\mathrm{gr}^3\right).\)

Proof. We again use that by Proposition 6.65, \(1\ge 1-d_{w_H^o}(u)\ge 1/4\) for every \(u\in V(H[I_{t_0}])\). Combining this with Theorem 3.28 and Proposition 6.66, and noting that we only consider subsets \(S\subseteq V(\mathcal{T})\) either contained within _I_<sub>_t_<sub>0</sub></sub>, or such that \(|S\cap I_{t_0}|=\Theta(t_0)\), the claim follows. □

We shall now modify \(M_H^o\) to balance out parities in what remains of the _X+Y_ and _X-Y_ parts, and cover the remaining vertices in _V(H<sup>c</sup>_)\\_V(H[I_<sub>_t_<sub>0</sub></sub>]).


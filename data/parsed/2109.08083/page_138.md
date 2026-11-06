_(ii)_ _every open and closed_ T _-valid tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _such that_ \(S_1,S_2,S_3\subseteq I_{t_0}\) _satisfies_<tbc>

<tbc>\(|E_{H^c}(v,S_1,S_2,S_3)|=(1\pm O(t_0^{-\epsilon}))\sum_{e\in E_H(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u)),\)<tbc>

<tbc>_and for any v-edge allowable function_ \(f_v:E(H)\rightarrow\mathbb{R}_{\ge 0}\) _for_ \((H,w_H,t_0,\eta)\) _such that f<sub>v</sub>(e_)=0 _wherever_ \(v\notin e\),<tbc>

<tbc>\(f_v(E_{H^c}(v,S_1,S_2,S_3))=(1\pm O(t_0^{-\epsilon}))\sum_{e\in E_H(v,S_1,S_2,S_3)}f_v(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u)),\)<tbc>

_(iii)_ _for every_ \(i\in[c_g]\),<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H^c}^+(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm O(t_0^{-\epsilon}))\sum_{z\in\mathcal{Z}_{i,e,H}^+(\alpha,\beta,\gamma)}\prod_{u\in z\backslash e}(1-d_{w_H^o}(u)) & \text{\textit{if}}e\text{\textit{is a bad edge}}, \\
O\left(k_it_1p_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{,}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H^c}^-(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm O(t_0^{-\epsilon}))\sum_{z\in\mathcal{Z}_{i,e,H}^-(\alpha,\beta,\gamma)}\prod_{u\in z\backslash e}(1-d_{w_H^o}(u)) & \text{\textit{if}}\alpha\neq 0\text{\textit{and}}\gamma=0\text{\textit{,}} \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=0\text{\textit{,}}\gamma=4\text{\textit{,}} \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{,}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)<tbc>

<tbc>_Finally, for every bad edge e,_<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H^c}^2|=O\left(k_it_1p_\mathrm{gr}^{12}\right).\)<tbc>

_(iv)_ _For every_ \(J\in\{X,Y,X+Y,X-Y\}\) _and every valid J-layer interval_ \(S\subseteq I_{t_0}\),<tbc>

<tbc>\(|V_{O/E}^J(H^c[S])|=(1\pm O(t_0^{-\epsilon}))\sum_{v\in V(H_{O/E}^J[S])}(1-d_{w_H^o}(v)),\)<tbc>

_(v)_ _For every_ \(J\in\{X,YX+Y,X-Y\}\) _and every valid J-layer interval_ \(I^J\subseteq I_{t_0}\) _and_ \(v\notin J\) _with_ \(v\in V(H^c)\),<tbc>

<tbc>\(|E_{H^c}(v,I^J,O/E)|=(1\pm O(t_0^{-\epsilon}))\sum_{e\in E_H(v,I^J,O/E)}\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u)),\)

_where_ \(\epsilon=10^{-8}/204800\).

Proof. The proof follows the same strategy as the proof of Theorem 6.28. In particular, we obtain _H<sup>c</sup>_ by running Theorem 6.2 on \((H^o,w_H^o)\) with \(\Delta=t_0\) and \(\eta=10^{-8}\). Comparing (i), (ii), (iv) and (v) to the proof of Theorem 6.28 (i) and (ii), the key difference is that in place of having _S_ such that \(|S|\ge\frac{t_i}{\mathrm{log}^2(n)}\), we have that |_S_| is of size \(\Omega(\mathrm{min}\{t_h,\alpha_G^2n\})=\Omega(n^{10^{-5}})\). Additionally, in place of calling Corollary 6.27, we have by Proposition 6.65 that \(1-d_{w_H^o}(v)\ge 1/4\) for every \(v\in I_{t_0}\). Then we have from Theorem 3.28 and the definition of _H<sup>o</sup>_ that \(\sum_{v\in V(H^o[S])}p_S(v)=|V(H^o[S])|\ge\frac{|S|p_\mathrm{gr}}{2}=\Omega(n^{10^{-5}-10^{-25}})\) and \(\mathrm{max}_{v\in V(H^o[S])}p_S(v)=1\). Thus since \(\eta=10^{-8}\), we see that (6.15) still holds easily in this setting. Similarly, for degree- type properties we get that \(|E_{H^o}(v,\mathcal{S})|\ge\Omega(n^{10^{-5}}p_\mathrm{gr}^3)\) and still (6.15) holds with \(\eta=10^{-8}\).


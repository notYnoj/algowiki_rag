(_ii)_ _for every_ \(v\in V(H)\) _and every open or closed_ T _-valid tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)_, we have_<tbc>

<tbc>\(|E_H(v,S_1,S_2,S_3)|=(1\pm\alpha_G)|E_\mathcal{T}(v,S_1,S_2,S_3)|p_\mathrm{gr}^3,\)<tbc>

_(iii)_ _for every_ \(i\in[c_g]\),<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H}^+(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm\alpha_G)|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12} & \text{\textit{if}}e\text{\textit{is a bad edge,}} \\
O\left(k_it_1p_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{,}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H}^-(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm\alpha_G)|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12} & \text{\textit{if}}\alpha\neq 0\text{\textit{and}}\gamma=0\text{\textit{,}} \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=0\text{\textit{,}}\gamma=4\text{\textit{,}} \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{,}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)<tbc>

<tbc>_Finally, for every bad edge e,_<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H}^2|=O\left(k_it_1p_\mathrm{gr}^{12}\right).\)<tbc>

_(iv)_ _We have that_ \(|V_O^{X+Y}(H)|=|V_O^{X-Y}(H)|\), \(|V_E^{X+Y}(H)|=|V_E^{X-Y}(H)|\) _and, furthermore_ \(|V_O^J(H)|=(1\pm 2\alpha_G)|V_E^J(H)|\) _for every_ \(J\in\{X,Y,X+Y,X-Y\}\)_. Additionally,_ \(|V_{O/E}^{J_1}(H[S])|=(1\pm 2\alpha_G)|V_{O/E}^{J_2}(H[S])|\) _for every valid layer interval S, and_ \(J_1,J_2\in\{X,Y,X+Y,X-Y\}\).<tbc>

_(v)_ _For every_ \(J\in\{X,Y,X+Y,X-Y\}\) _and every valid J-layer interval I<sup>J</sup> and_ \(v\notin J\),

<tbc>\(|E_H(v,I^J,O/E)|=(1\pm\alpha_G)|E_\mathcal{T}(v,I^J,O/E)|p_\mathrm{gr}^3.\)

Whilst we could define more general properties, or subsets for which such properties hold, these are the key subsets and properties required which allow us to run our process, and it is more intuitive to have these properties in mind throughout the process than something more general.

## 3.6. Facts about T

Our strategy will at times compare a subgraph \(H_i\subseteq\mathcal{T}\) to \(\mathcal{T}[I_{t_i}]\subseteq\mathcal{T}\) , and in particular the following details are useful for calculations in Section 6.5. More generally, the following facts should help develop a better picture of what T ‘looks like’ in terms of various degree type and wrap-around edge type properties.

Fact 3.29. _Given that_ T\[_I<sub>t<sub>k</sub></sub>_\] _contains no wrap around edges and_ \(v\in I_{t_1}\cap I_{t_{k-1}}\)_, we have that_ |_E_<sub>T</sub>(_v,I<sub>t<sub>k</sub></sub>_)| _satisfies the following:_

\(|E_\mathcal{T}(v,I_{t_k})|\pm 1=\left\{\begin{array}{ c c }
(\frac{4t_k}{3}+1) & \text{\textit{for}}v\in[-\frac{t_k}{3},\frac{t_k}{3}]\cap(X\cup Y)\text{\textit{,}} \\
(2t_k+1-2|v|) & \text{\textit{for}}v\in\pm[\frac{t_k}{3},\frac{2t_{k-1}}{3}]\cap(X\cup Y) \\
(t_k+1_{|v|}\text{\textit{is even}}) & \text{\textit{for}}v\in[-\frac{t_k}{3},\frac{t_k}{3}]\cap(X+Y\cup X-Y) \\
(\frac{4t_k}{3}+1-|v|) & \text{\textit{for}}v\in\pm[\frac{t_k}{3},t_{k-1}]\cap(X+Y\cup X-Y)\text{\textit{.}}
\end{array}\right.\)

Note that T\[_I_<sub>_t_<sub>1</sub></sub>\] contains no wrap-around edges, and hence Fact 3.29 is true for all \(k\ge 1\). When \(v\in V(\mathcal{T})\backslash I_{t_1}\), or we are considering _I_<sub>_t_<sub>0</sub></sub> there are still wrap- around edges to consider. It is helpful for the initial steps of the iterative matching process to observe some facts about |_E_<sub>T</sub>(_v,I_<sub>_t_<sub>0</sub></sub>)| for \(v\in\mathcal{T}\) , as well as |_E_<sub>T</sub>(_v,I_<sub>_t_<sub>1</sub></sub>)| for \(v\in I_{t_0}\backslash I_{t_1}\).

Fact 3.30. _The following all hold:_


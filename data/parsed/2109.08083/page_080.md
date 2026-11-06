<tbc>**The iterative matching process**

### 6.1. Overview

Recall that at this stage we have \(\alpha_G:=n^{-10-8}\) and _p_gr:=_n_<sup>-10-25</sup>, and have shown that with high probability the random greedy count leaves us with a graph _H_ as per Theorem 3.28. Until Section 6.5, we are concerned with the process starting from _H_<sub>1</sub> (two steps into the _vortex_ from _H_). Thus we start this chapter with a theorem stating the key properties of _H_<sub>1</sub>. In fact, for the iterative matching process we consider weighted subgraphs and so need to track properties concerning a weighted subgraph (_H_<sub>1</sub>_,w_<sub>1</sub>).

Recall from Section 3.1.1 that we defined \(\eta_1:=10^{-9}\) and \(\epsilon_1:=\frac{\eta_1}{204800}\) (so that \(\epsilon_1=\frac{\eta_1}{50L^2r^2}\) as in Theorem 6.2, with _r_=4 and _L_=16). We prove the following theorem in Section 6.5.

Theorem 6.1. _Given n is sufficiently large, there is a graph_ \(H_1\subseteq H\) _such that_ \(V(H_1)\subseteq I_{t_1}\) _and H_<sub>1</sub> _has an almost-perfect fractional matching w_<sub>1</sub> _with the following properties:_

(_i)_ \(d_{w_1,H_1}(v)\ge 1-t_1^{-\epsilon_1}\) _for every_ \(v\in V(H_1)\),<tbc>

(_ii)_ _there exist absolute constants_ 0_\<c_<sub>1,1</sub>_\<c_<sub>1,2</sub> _such that for every edge_ \(e\in H_1\)_, we have that_<tbc>

<tbc>\(\frac{c_{1,1}}{p_\mathrm{gr}^3t_1}\le w_1(e)\le\frac{c_{1,2}}{p_\mathrm{gr}^3t_1},\)<tbc>

_(iii)_ _there exist absolute constants_ 0_\<c_<sub>1,3</sub>_\<c_<sub>1,4</sub>_\<_1 _such that for every_ 1_-valid subset_ \(S\subseteq V(\mathcal{T})\) _we have that_<tbc>

<tbc>\(c_{1,3}|S|p_\mathrm{gr}\le|V(H_1[S])|\le c_{1,4}|S|p_\mathrm{gr},\)<tbc>

_(iv)_ _there exist absolute constants_ 0_\<c_<sub>1,5</sub>_\<c_<sub>1,6</sub>_\<_1 _such that for every open or closed_ 1_-valid tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>),<tbc>

<tbc>\(c_{1,5}|S_1|p_\mathrm{gr}^3\le|E_{H_1}(v,S_1,S_2,S_3)|\le c_{1,6}|S_1|p_\mathrm{gr}^3,\)<tbc>

_(v)_ _there exist absolute constants_ 0_\<c_<sub>1,7</sub>_\<c_<sub>1,8</sub> _such that for every_ \(i\in[c_g]\) _the number of i-legal zero-sum configurations_ \(\mathcal{Z}_{i,e,H_1}^\pm(\alpha,\beta,\gamma)\) _containing the edge_ \(e\in H_1\) _of type_ \((\alpha,\beta,\gamma)_i\) _with positive or negative sign respectively, satisfies_<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H_1}^+(\alpha,\beta,\gamma)|\le\left\{\begin{array}{ c c }
c_{1,8}|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12} & \text{\textit{if}}e\text{\textit{is a bad edge,}} \\
c_{1,8}k_it_1p_\mathrm{gr}^{12} & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{,}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)<tbc>


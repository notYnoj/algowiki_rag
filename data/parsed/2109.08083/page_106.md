(_K1)_ _for every i-reachable subset_ \(S\subseteq I_{t_{i+1}}\),<tbc>

<tbc>\(|V(G'[S])|=(1\pm c_1^{-1}t_i^{-\epsilon_1}log^{l_3+2}(n))\sum_{v\in V(G[S])}(1-d_{\omega^o}(v)),\)<tbc>

<tbc>_and for a function_ \(p_S(v):V(G)\rightarrow\mathbb{R}_{\ge 0}\) _such that_ \(p_S(v)=f_S(v)\unknown_{v\in V(G[S])}\) _and_ \(\frac{max_{v\in V(G^o[S])}p_S(v)}{min_{v\in V(G^o[S])}p_S(v)}\le log^{500}(n)\),<tbc>

<tbc>\(\sum_{v\in V(G^\prime[S])}p_S(v)=(1\pm c_1^{-1}t_i^{-\epsilon_1}log^{l_3+2}(n))\sum_{v\in V(G[S])}p_S(v)(1-d_{\omega^o}(v)).\)<tbc>

<tbc>_Furthermore, for every i-valid subset_ \(S\subseteq K_{j+1}\), \(|V(G'[S])|=|V(H_{1^*}[S])|\).<tbc>

(_K2)_ _for every open or closed i-reachable tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _with_ \(v\in V(G')\) _and_ \(S_1,S_2,S_3\subseteq I_{t_{i+1}}\)_, we have both that_<tbc>

<tbc>\(|E_{G^\prime}(v,S_1,S_2,S_3)|=(1\pm t_i^{-\epsilon_1}log^{3l_3+7}(n))\sum_{e\in E_G(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}(1-d_{\omega^o}(v)),\)<tbc>

<tbc>_and for a function_ \(f_v:E(G)\rightarrow\mathbb{R}_{\ge 0}\) _such that f<sub>v</sub>(e_)=0 _wherever_ \(v\notin e\) _and_ \(\frac{max_{e\in E_{G^o}(v,S_1,S_2,S_3)}}{min_{e\in E_{G^o}(v,S_1,S_2,S_3)}f_v(e)}\le log^{500}(n)\),<tbc>

<tbc>\(f_v(E_{G^\prime}(v,S_1,S_2,S_3))=(1\pm t_i^{-\epsilon_1}log^{3l_3+7}(n))\sum_{e\in E_G(v,S_1,S_2,S_3)}f_v(e)\prod_{u\in e\backslash\{v\}}(1-d_{\omega^o}(v)).\)<tbc>

<tbc>_In particular,_<tbc>

<tbc>\(\omega(E_{G^\prime}(v,S_1,S_2,S_3))=(1\pm t_i^{-\epsilon_1}log^{3l_3+7}(n))\sum_{e\in E_G(v,S_1,S_2,S_3)}\omega(e)\prod_{u\in e\backslash\{v\}}(1-d_{\omega^o}(v)).\)<tbc>

_(K3)_ _for every open or closed i-permissible tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _with_ \(v\in V(G')\) _such that_ \(\bigcup\{e\backslash\{v\}:e\in E_\mathcal{T}(v,S_1,S_2,S_3)\}\subseteq K_{j+1}\)_, we have that_ \(|E_{G^\prime}(v,S_1,S_2,S_3)|=|E_{H_{1^*}[S]}(v,S_1,S_2,S_3)|\).

Note that in the inequalities with log500(_n_) on the right hand side the 500 is not important, but is an explicit (not tight) upper bound that all functions we are concerned with will easily satisfy.

Proof. We obtain \(G'\) by running Theorem 6.2 on \((G^o,\omega^o)\). We first claim that the hypotheses all hold in \((G^o,\omega^o)\), taking \((\eta_1,t_i)\) in place of \((\eta,\Delta)\).1. Note that all vertices, subsets and edges in _G<sup>o</sup>_ are, by definition, _i_-reachable. Since this is the case, and \((G,\omega)\) is _i_-permissible, by (P3) we have _c_<sub>1</sub>_,l_<sub>1</sub>_\>_0 such that

\(\frac{c_1}{p_\mathrm{gr}^3t_ilog^2(n)}\le\omega^o(e)\le\frac{log^{l_1}(n)}{p_\mathrm{gr}^3t_i},\)

for every \(e\in G^o\), which implies \(\omega^o(e)\ge t_i^{-1}\) and \(\Delta_{\omega^o}^c(G^o)=max_{e\in G^o}\omega^o(e)\le t_i^{-\eta_1}\). It is also clear, since \(G^o\subseteq\mathcal{T}[I_{t_i}]\), that \(e(G^o)\le exp(t_i^{\epsilon_1^2/4})\). Recall that \(\delta_{\omega^o}(G^o)=min_{v\in V(G^o)}d_{\omega^o}(v)\). Since \((G,\omega)\) is _i_-permissible, and (_v,I<sub>t<sub>i</sub></sub>_\\_I_<sub>_t<sub>i</sub>_+1</sub>) is an open _i_-reachable pair, we have by (P5) that \(min_{v\in V(G^o)}|E_G(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\ge\)

1We consider _n_ to be sufficiently large that \(\Delta=t_i\) is sufficiently large, i.e. \(t_i\ge\Delta_0\), the value given by Theorem 6.3 given \(\eta_1\).


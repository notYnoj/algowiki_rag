<tbc>It follows that

\(\Delta^{k+\eta} q_l(\bar{e}_k)\le r^k\Delta^{l+\eta} max_{\bar{v}_k\in\genfrac(){pt}{2}{V(H)}{k}}\sum_{\bar{v}_{l-k}\in\genfrac(){pt}{2}{V(H)}{l-k}}p_l(\bar{v}_k\cup\bar{v}_{l-k})\)<br>
\(\le r^k\Delta^{l+\eta} f\Delta^{-2\eta}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\)<br>
\(\le\frac{r^k\Delta^{l-\eta}}{2r^l\Delta^{l-l\psi}(1-\frac{rl^2}{\Delta^{\eta-\psi}})}q_l(E(H))\)<br>
\(\le\frac{2r^k\Delta^{l-\eta}}{2r^l\Delta^{l-l\psi}}q_l(E(H))\)<br>
\(\le\frac{1}{r^{l-k}\Delta^{\eta(1-\frac{l}{5L^2r})}}q_l(E(H))\le q_l(E(H)),\)

using (6.7) and Proposition 6.5, for every \(k\in[l]\). Thus \(\Delta^{k+\eta} max_{\bar{e}_k}q_l(\bar{e}_k)\le q_l(E(H))\), as required. □

So _H_ is a graph satisfying the hypotheses of Theorem 6.3, and _q<sub>l</sub>_ satisfies the requirements of the theorem. It follows that there exists a distribution on matchings _M_ in _H_ such that with high probability<tbc>

\(q_l(M)=\left(1\pm\frac{\Delta^{-\epsilon}}{2}\right)\frac{q_l(E(H))}{\Delta^l}.\)

<tbc>We have, from above, that<tbc>

\(q_l(E(H))\ge\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}\left(d_H(v)-r(l-1)\Delta^\text{co}\right),\)

<tbc>and by similar arguments it is clear that<tbc>

\(q_l(E(H))\le\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}d_H(v),\)

<tbc>so, in particular, since \(\delta(H)\ge\Delta^{1-\psi}\),

\(q_l(E(H))=\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}\left(d_H(v)\left(1\pm\frac{r(l-1)\Delta^\text{co}}{\delta(H)}\right)\right)\)<br>
\(=\left(1\pm\frac{l^2r}{\Delta^{\eta-\psi}}\right)\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}d_H(v).\)

Now for any matching _M_ we have that

\(\sum_{\bar{v}\in\genfrac(){pt}{2}{V(M)}{l}}p_l(\bar{v})=\sum_{\bar{e}\in\genfrac(){pt}{2}{M}{l}}q_l(\bar{e})+\Gamma,\)

where \(\Gamma\) sums _p<sub>l</sub>_ over all of the _l_-sets of vertices in _V(M_) which contain at least two vertices from one edge \(e\in M\). This gives

\(\Gamma=\sum_{\bar{v}\in\genfrac(){pt}{2}{V(M)}{l}}p_l(\bar{v})-\sum_{\bar{e}\in\genfrac(){pt}{2}{M}{l}}q_l(\bar{e})\le\sum_{e\in M}\sum_{\bar{v}_2\subseteq e,\bar{v}_{l-2}\in\genfrac(){pt}{2}{V(M)\backslash\bar{v}_2}{l-2}}p_l(\bar{v}_2\cup\bar{v}_{l-2}),\)


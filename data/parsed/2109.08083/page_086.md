<tbc>process where parity constraints are still an issue - see Section 6.5.5.) For most of the iterative matching process the properties we are concerned with tracking are those of vertices rather than edges. As such we now derive a vertex version of Theorem 6.3. In what follows, by abuse of notation, for \(\bar{e}\in\genfrac(){pt}{2}{E(H)}{l}'\), and \(\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}\), we write \(\bar{v}\in\bar{e}\) to mean that \(\bar{v}\) is an _l_-set containing exactly one vertex from each edge in \(\bar{e}\).

Proposition 6.5. _Suppose that H is an r-graph and_ \(p_l:\genfrac(){pt}{2}{V(H)}{l}\rightarrow\mathbb{R}_{\ge 0}\) _is a weight function on l-sets of vertices such that_

(6.5) \(\mathrm{max}_{v\in V(H)}p_l(\{v\})\le f\Delta^{-2\eta}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\)

_for some fixed_ \(l\in\mathbb{N}\) _and_ \(f=f(r,l)\le\frac{1}{2r^l}\)_. Then,_

(6.6) \(\mathrm{max}_{\bar{v}_k\in\genfrac(){pt}{2}{V(H)}{k}}p_l(\bar{v}_k)\le f\Delta^{-2\eta}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\)

_for every_ \(k\in[l]\).

This leads us to a vertex version of Theorem 6.3.

Theorem 6.6. _Suppose_ \(\eta\in(0,1)\) _and_ \(r,L\in\mathbb{N}\) _with_ \(r\ge 2\)_, and let_ \(\epsilon:=\frac{\eta}{50L^2r^2}\) _and_ \(\psi:=\frac{\eta}{5L^2r}\)_. Then there exists_ \(\Delta_0\) _such that for all_ \(\Delta\ge\Delta_0\)_, the following holds. Let H be an r-uniform hypergraph with_ \(\Delta(H)\le\Delta\), \(\delta(H)\ge\Delta^{1-\psi}\) _and_ \(\Delta^\mathrm{co}(H)\le\Delta^{1-\eta}\) _as well as_ \(e(H)\le\mathrm{exp}(\Delta^{\epsilon^2})\)_. Suppose that for some_ \(l\in[L]\) _we have p<sub>l</sub> an l-set weight function on V(H_) _such that_

(6.7) \(\mathrm{max}_{v\in V(H)}p_l(\{v\})\le f\Delta^{-2\eta}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v}),\)

_where_ \(f\le\frac{1}{2r^l}\) _is fixed._

_Then there exists a distribution on matchings M in H such that with high probability_

\(p_l(M)=\left(1\pm\frac{2\Delta^{-\epsilon}}{3}\right)\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}\frac{d_H(v)}{\Delta}.\)

Proof. We start by fixing \(l\in[L]\) and defining \(q_l:\genfrac(){pt}{2}{E(H)}{l}'\rightarrow\mathbb{R}_{\ge 0}\) via

\(q_l(\bar{e})=\sum_{\bar{v}\in\bar{e}}p_l(\bar{v}).\)

Claim 6.7. _q<sub>l</sub> satisfies_ \(q_l(E(H))\ge\Delta^{k+\eta}\mathrm{max}_{\bar{e}_k\in\genfrac(){pt}{2}{E(H)}{k}}q_l(\bar{e}_k)\) _for all_ \(k\in[l]\).


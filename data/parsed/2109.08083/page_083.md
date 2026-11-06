<tbc>**6.1.3. The random matching tool.** One of the key tools used in our iterative absorption strategy is a generalisation of a result by Ehard, Glock and Joos \[18\] which enables us to find a matching with random-like properties given an _r_- uniform hypergraph with particular conditions. This generalises a result of Kahn \[29\] who proved a similar result, but with more restrictive conditions on properties that could be tracked in relation to the matching.

6.1.3.1. _Weighted version._ For our purposes, we wish to consider a weighted _r_- uniform hypergraph (_H,w_), where \(w:E(H)\rightarrow\mathbb{R}_{\ge 0}\), and \(d_w(v):=\sum_{e\unknown v}w(e)\le 1\) for every \(v\in V(H)\) (so _w_ is also a fractional matching). We write \(\Delta_w(H):=\mathrm{max}_{v\in V(H)}d_w(v)\) and letting \(d_w(v,u):=\sum_{e\supseteq\{v,u\}}w(e)\), we also write \(\Delta_w^\mathrm{co}(H):=\mathrm{max}_{\{v,u\}\in\genfrac(){pt}{2}{V(H)}{2}}d_w(v,u)\). Let \(\delta_w(H):=\mathrm{min}_{v\in V(H)}d_w(v)\).

Given a function \(p_l:\genfrac(){pt}{2}{V(H)}{l}\rightarrow\mathbb{R}_{\ge 0}\), and a set \(\bar{v}_k\in\genfrac(){pt}{2}{V(H)}{k}\), define

\(p_l(\bar{v}_k):=\sum_{\bar{v}\supseteq\bar{v}_k:\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})=\sum_{\bar{v}_{l-k}\in\genfrac(){pt}{2}{V(H)}{l-k}}p_l(\bar{v}_k\cup\bar{v}_{l-k})\)

for every \(k\le l\). Furthermore, for \(M\subseteq E(H)\), we define \(p_l(M):=\sum_{\bar{v}\in\genfrac(){pt}{2}{V(M)}{l}}p_l(\bar{v})\). Also for a function \(q:E(H)\rightarrow\mathbb{R}_{\ge 0}\) we define \(q(M)=\sum_{e\in M}q(e)\). Our key tool is the following:

Theorem 6.2. _Suppose_ \(\eta\in(0,1)\) _and_ \(r,L\in\mathbb{N}\) _with_ \(r\ge 2\)_. Let_ \(\epsilon:=\frac{\eta}{50L^2r^2}\) _and_ \(\psi:=\frac{\eta}{6L^2r}\)_. Then there exists_ \(\Delta_0\) _such that for all_ \(\Delta\ge\Delta_0\)_, the following holds. Let_ (_H,w_) _be an r-uniform weighted hypergraph with_ \(w(e)\ge\Delta^{-1}\) _for every_ \(e\in H\), \(\delta_w(H)\ge\frac{\Delta^{-\psi}}{1-\Delta^{-1}}\) _and_ \(\Delta_w^\mathrm{co}(H)\le\Delta^{-\eta}\) _as well as_ \(e(H)\le\mathrm{exp}(\Delta^{\epsilon^2/4})\).

_Suppose that for each_ \(l\in[L]\)_, we are given a set_ P_<sub>l</sub> of l-tuple weight functions on V(H_) _of size polynomial in_ \(\Delta\) _such that_

(6.1) \(\mathrm{max}_{v\in V(H)}p_l(\{v\})\le f\Delta^{-2\eta}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\)

_for all_ \(p_l\in\mathcal{P}_l\)_, where_ \(f\le\frac{1}{2r!}\).

_Suppose further that_ Q _is a set of weight functions on E(H_) _of size polynomial in_ \(\Delta\) _such that_

(6.2) \(q(E(H))\ge\frac{\Delta^{1+\eta}}{1-\Delta^{-1}}\mathrm{max}_{e\in E(H)}q(e)\)

_for all_ \(q\in\mathcal{Q}\).

_Then there exists a matching M in H such that_

\(p_l(M)=(1\pm\Delta^{-\epsilon})\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}d_w(v)\)

_for every_ \(l\in[L]\)_, and every_ \(p_l\in\mathcal{P}_l\)_, and_

\(q(M)=\big(1\pm\Delta^{-\epsilon}\big)\sum_{e\in E(H)}q(e)w(e)\)

_for all_ \(q\in\mathcal{Q}\).

We shall show in Section 6.3 that all properties we wish to keep track of (those relating to vertex subsets, degrees and zero-sum configurations) for the general iterative absorption strategy can be written as linear combinations of functions of vertices which will satisfy (6.1). Additionally, in Section 6.5, we show that a


Recalling that \(\Delta=\Theta(r^{d\frac{d-1}{d+1}})\) allows us to set \(d=2/\epsilon\) such that \(r=O(\Delta^{2\epsilon})\) implying that the number of critical pairs becomes \(\Omega(m)\Delta^{k-1-3\epsilon}\). Furthermore, the number of edges in our graph is at most<tbc>

\(m=O(Nk\ell\Delta)=O((2(r+1)r\ell)^{kd}k\ell r^{2/\epsilon})=O(r^{7k/\epsilon}).\)

<tbc>Now, we convert the shortcut \(E'\) into the union \(E''\) of \(O((\ell k)^2)\) normalized shortcuts according to Lemma 3.4, each with at most \(m^{1+\epsilon^2/k}\) edges. According to the definition of thickness and by splitting edges by Steiner vertices, we can further assume that all components of \(E''\) consist of _t_-1 layers out of which only the first and the last is adjacent to _G_. Under these assumptions, we can still assume that \(|E''|=O(m)k^3\ell^2m^{\epsilon^2/k}\) implying that the efficiency of \(|E''|\) is at least

\(\eta:=\frac{\Omega(m)\cdot\Delta^{k-1-3\epsilon}}{k^3\ell^2m^{1+\epsilon^2/k}}=\Omega(\Delta^{k-1-8\epsilon})m^{-\epsilon^2/k}\)<br>
\(=\Omega(\Delta^{k-1-9\epsilon}),\)

using that \(k=O(r),\ell=O(r^3)\), \(r=O(\Delta^{2\epsilon})\), and \(m=O(r^{7k/\epsilon})\). The diameter associated to \(E''\) is at most \(km^{\epsilon^2/k}=kO(r^{7\epsilon})<k\ell\), so, for every critical path, there is still a critical shortest path that uses at least one edge in \(E''\).

In fact, for each critical shortest path _P_, there is a component _C_ of \(E''\) such that _P_ is _C_- respecting while _C_ shortcuts two layers _L<sub>i</sub>,L<sub>j</sub>_ with \(|i-j|\ge 4rk\). Otherwise, the diameter we would achieve for the critical paths would be at least \(\frac{\ell k}{4rk}=\Omega(r^2)\), which contradicts our assumption that the achieved diameter is \(km^{\epsilon^2/k}=O(r^{1+7\epsilon})\). We therefore delete all components from \(E''\) that introduce a shortcut between layers _L<sub>i</sub>,L<sub>j</sub>_ with |_i-j|\<_4_rk_ and call the result \(E'''\). By the preceding discussion, we still know that every critical shortest path uses at least one edge in \(E'''\). Due to this fact and since \(|E'''|\le|E''|\), the efficiency of \(E'''\) does not decrease as compared to \(E''\).

We define \(\epsilon':=9\epsilon\) and delete all Steiner vertices with degree at least \(\Delta^{1+\epsilon^\prime}\) from \(E'''\) and call the resulting shortcut _E_<sup>∗</sup>. According to Lemma 3.7 the efficiency of such vertices is at most \(\Delta^{k-1-\epsilon^\prime}\), so according to Lemma 3.6 removing them does not decrease the efficiency of the shortcut. We recall that each component of _E_<sup>∗</sup> consists of _t_-1 consecutive layers _S_<sub>1</sub>_,...,S_<sub>_t_-1</sub> such that every _C_-respecting critical shortest path contains exactly one vertex in each layer _S<sub>i</sub>_. Denote by _M_ the union of all Steiner vertices in the middle layers _S_<sub>⌉_t/_2⌋</sub> across all components _C_ in _E_<sup>∗</sup>.

We claim that there exists at least one vertex in _M_ which also has efficiency at least \(\eta\). To see this, denote by _E<sub>M</sub>_ the set of edges incident to the vertices in _M_ and by P the set of _E_<sup>∗</sup>-respecting critical shortest paths. By definition of efficiency, we know that \(|\mathcal{P}|/|E^*|\ge\eta\), and since \(|E_M|\le|E^*|\), we get that \(|\mathcal{P}|/|E_M|\ge\eta\). Now, denote the efficiency of a vertex \(v\in M\) by \(\eta_v\) and assume for the sake of contradiction that \(\eta_v<\eta\) for all \(v\in M\). Then, noting that \(|\mathcal{P}|\le\sum_{v\in M}\eta_vdeg(v)\) and \(|E_M|=\sum_{v\in M}deg(v)\) allows us to infer that

\(\frac{|\mathcal{P}|}{|E_M|}\le\frac{\sum_{v\in M}\eta_vdeg(v)}{\sum_{v\in M}deg(v)}<\eta,\)

which contradicts the fact that \(\mathcal{P}/|E_M|\ge\eta\).

We have thus proved that there is some \(v\in M\) with efficiency at least \(\eta=\Omega(\Delta^{k-1-9\epsilon})\). Denote the number of _E_<sup>∗</sup>-respecting shortest paths passing through _v_ by _p(v_) and note that \(p(v)\ge\etadeg(v)\) by definition of efficiency. We show that _p(v_) is large. To this end, we note that \(p(v)\le deg(v)^2\Delta^{(1+\epsilon^\prime)(t-2)}\). The upper bound is the maximum number of pairs of vertices in _G_, one at the starting layer of _C_ and one at the final layer, both reachable from _v_ using only edges in the component _C_ of _E_<sup>∗</sup> containing _v_. This bound uses our upper bound on the degree of remaining Steiner vertices. By uniqueness of critical paths (the third property of Lemma 2.5), the number of<tbc>


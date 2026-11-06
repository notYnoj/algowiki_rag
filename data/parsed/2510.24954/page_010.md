• The outdegree of each vertex in _G_ is at most \(\Delta=\Theta\left(r^{d\cdot\frac{d-1}{d+1}}\right)\), and in fact the average degree of _G_ is \(\Theta(\Delta)\), hence \(|E|=\Theta(n\Delta)=\Theta(k\ell\Delta N)\).<tbc>

• The number of critical pairs/critical paths is \(|P|=\Theta\left(\frac{N\Delta^kr^{dk}}{(r+1)^{dk}}\right)\) by Lemma 2.5.

We are now ready to prove that graph _G_ and critical pairs _P_ imply a polynomial lower bound for reachability shortcuts. We restate Theorem 2.1 for convenience.

**Theorem 2.1** (Cf. \[Hes03, Theorem 4.1\])**.** _Let k\>_1 _be an integer and_ \(\epsilon=\Omega(1/k)\). G_<sub>k</sub> is an infinite family of n-vertex, n_<sup>1+_O_(1_/k_)</sup>_-edge directed graphs. Each graph_ \(G=(V,E)\in\mathcal{G}_k\) _has an associated set of critical vertex pairs_ \(P\subseteq V\times V\) _of size_ \(|P|=\Omega(n^{1.5-\epsilon})\)_. For any shortcut set_ \(E_+\subseteq E^*\) _of G, where G_<sup>∗</sup>=(_V,E_<sup>∗</sup>) _is the transitive closure of G, either_

• \(|E_+|\ge|P|\)_, or_<tbc>

• _There is a pair of vertices_ \((s,t)\in P\) _such that_ \(\mathrm{dist}_{G_+}(s,t)=n^{\Omega(1/k)}\) _in_ \(G_+=(V,E\cup E_+)\).

_Proof._ Let \(E_+\subseteq E^*\) be the set of shortcut edges for _G_, where |_E_<sub>+</sub>|_\<|P_|. We say that an edge \((u,v)\in E_+\) is _short_ if \((u,v)\in L_i\times L_j\) for some choice of \(i,j\in[0,k\cdot\ell]\) such that _j\<i+k_, and _long_ otherwise.

By Lemma 2.5, each long shortcut edge can only be used by one critical pair in _P_. Since |_E_<sub>+</sub>|_\<|P_|, by the pigeonhole principle there is some \((s,t)\in P\) such that the shortest _s-t_ path in _G_<sub>+</sub> uses only original edges from _E_ and _short_ edges from _E_<sub>+</sub>, hence \(\mathrm{dist}_{G_+}(s,t)\ge k\ell/(k-1)>\ell\).

Treating _k_ as constant, the quantitative claims follow by setting \(\ell=r^c=r^{O(\epsilon)}\) and \(d=\Omega(1/\epsilon)\), so that \(\Delta=\Theta(r^{d(d-1)/(d+1)})=r^{(1-\Theta(\epsilon))d}\), \(n=\Theta((2r)^{(2+c)kd}r^c)\), \(m=O(n\Delta)=r^{(2+c)kd+c+(1-\Omega(\epsilon))d}=n^{1+O(1/k)}\), \(|P|=\Omega\left(\frac{N\Delta^kr^{dk}}{(r+1)^{dk}}\right)=r^{(2+c)kd+(1-\Omega(\varepsilon))kd}=\Omega(n^{1.5-\epsilon})\).

## 2.3 Breaking Hesse’s Counterexamples using Steiner Vertices

In this section we will show how Steiner vertices break Hesse’s counterexample argument. We will achieve this by proving Theorem 2.2, restated for convenience.

**Theorem 2.2.** _Let_ \(k\ge 2\) _be an integer, and let_ \(G=(V,E)\in\mathcal{G}_k\) _be an n-vertex, n_<sup>1+_O_(1_/k_)</sup>_-edge graph with associated critical vertex pairs_ \(P\subseteq V\times V\)_. Then G admits a k-thick Steiner shortcut graph_ \(G_+=(V\cup V_+,E\cup E_+)\) _with_ \(|E_+|=|E|/n^{\Omega(1/k)}\)_, such that every_ \((s,t)\in P\) _has_ dist<sub>_G_<sub>+</sub></sub>(_s,t_)=_k._

Let \(G\in\mathcal{G}_k\) be the given graph, parameterized by \(r\in\mathbb{N}^+\). Each critical pair \((s,t)\in P\) is of the form \((((0,0),p),((\ell,0),p+\ell\vec{v}))\), for some _p_=(_p_<sub>0</sub>_,...,p_<sub>_k_-1</sub>) and critical direction \(\vec{v}=(\vec{v}_0,\dots,\vec{v}_{k-1})\). Rather than move from _s_ to _t_ by adding the _k_ critical subdirections in a "round robin" format, we can add each all at once, walking through new Steiner vertices corresponding to points

\(p\rightarrow(p_0+\ell\vec{v}_0,\dots,p_{k-1})\rightarrow(p_0+\ell\vec{v}_0,p_1+\ell\vec{v}_1,\dots,p_{k-1})\rightarrow(p_0+\ell\vec{v}_0,p_1+\ell\vec{v}_1,p_2+\ell\vec{v}_2,\dots,p_{k-1}),\)

and so on. We now give the details.

### Constructing a Steiner shortcut.

Let \(G_+=(V\cup V_+,E\cup E_+)\) be the Steiner shortcut for _G_. The vertex set _V_<sub>+</sub> is partitioned into a collection of _k_-1 disjoint layers _S_<sub>1</sub>_,...,S_<sub>_k_-1</sub>, where _S<sub>i</sub>_ is the set of tuples (_i,(p_<sub>1</sub>_,...,p_<sub>_k_-1</sub>)), each point \(p_1,\dots,p_{k-1}\in\mathbb{Z}^d\) being contained in the rectangle \((-(r+1)r\ell,(r+1)r\ell]^d\). Note that by definition, each _S<sub>i</sub>_ has the same number of vertices as each _L<sub>i,j</sub>_: |_S<sub>i</sub>_|=|_L<sub>i,j</sub>_|=_N_.


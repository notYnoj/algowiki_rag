Note that \(\delta_\mathrm{H}(y,\mathrm{Rep}^\pm(k,t))=\frac{1}{k}\sum_{i=1}^k\Delta_i\).

The tester _T_ samples a random edge \((a,b)\in E\) and rejects iff _y<sub>a,i</sub>=y<sub>b,i</sub>_, which (by construction of _g<sub>i</sub>_) is equivalent to rejecting iff \(g_i(a)\neq g_i(b)\). Therefore the rejection probability conditioned on column _i_ equals the fraction of _disagreeing_ edges of _G_ under the labeling _g<sub>i</sub>_:

\(\rho_i:=\mathbf{Pr}\left[T\mathrm{rejects}|i\right]=\frac{1}{|E|}\sum_{(u,v)\in E}\mathbf{1}\big[g_i(u)\neq g_i(v)\big].\)

We now relate \(\rho_i\) to \(\Delta_i\) using the expansion of _G_. Let \(\pi\) be the uniform distribution on \(A\cup B\), and write \(\langle f,h\rangle:=\mathbb{E}_{v\sim\pi}[f(v)h(v)]\) and \(\mathrm{Var}(f):=\langle f-\mathbb{E}[f],f-\mathbb{E}[f]\rangle\). Let _P_ be the random-walk operator on _G_ (normalized adjacency).

Apply Lemma 4.5 to \(f=g_i\in\{0,1\}^{A\cup B}\). Then \(\rho_i=\frac{1}{|E|}\sum_{(u,v)}\mathbf{1}[g_i(u)\neq g_i(v)]=\frac{1}{|E|}\sum_{(u,v)}(g_i(u)-g_i(v))^2\), so<tbc>

\(\rho_i\ge 2(1-\sigma(G))\mathrm{Var}(g_i).\)

<tbc>For a {0,1}-valued function, \(\mathrm{Var}(g_i)=\theta_i(1-\theta_i)\) where \(\theta_i\) is the fraction of 1’s; moreover \(\Delta_i=\mathrm{min}\{\theta_i,1-\theta_i\}\le\frac{1}{2}\), hence \(\theta_i(1-\theta_i)\ge\frac{1}{2}\Delta_i\). Therefore,<tbc>

\(\rho_i\ge(1-\sigma(G))\Delta_i.\)

<tbc>Averaging over the random column _i_ yields

\(\mathbf{Pr}\left[T\mathrm{rejects}y\right]=\frac{1}{k}\sum_{i=1}^k\rho_i\ge(1-\sigma(G))\frac{1}{k}\sum_{i=1}^k\Delta_i=(1-\sigma(G))\Delta\big(y,\mathrm{Rep}^\pm(k,t)\big),\)

which proves the desired soundness with \(\kappa=1-\sigma(G)\).

(4) _Degree._ Each vertex of _G_ has exactly _d_ incident edges, so a coordinate (_v,i_) appears in exactly _d_ possible queries. This _d_ is fixed once we choose _G_ and does not depend on _t_ or _n_.

Using any constant-degree bipartite expander family (e.g., Ramanujan graphs), \(\sigma(G)\le 2\sqrt{d-1}/d\), hence \(\kappa\ge 1-2\sqrt{d-1}/d\) is a positive constant.

_Proof of Theorem 1.3._ By permuting coordinates we may regard \(\mathrm{Rep}^\pm(k,t)\) as systematic, so every instance I_<sub>C</sub>(m_) produced from the code is satisfiable and encodes a bipartite Max Cut instance. The code parameters are \(|\Sigma|=2\), relative distance \(\delta=1/k\), rate _r_=1_/t_, detection probability \(\kappa=1-\sigma(G)\), and variable degree \(\theta=d\).

Let A be a \((1-\varepsilon)\)-approximation algorithm for Max Cut. Applying Theorem 3.8 yields neighboring messages \(m\sim m'\) with<tbc>

\(\mathsf{EMD}_{\delta_\mathrm{H}}\left(\mathcal{A}(\mathcal{I}_C(m)),\mathcal{A}(\mathcal{I}_C(m'))\right)\ge\frac{1}{k}\left(1-\frac{2t\varepsilon}{\kappa}\right)-\frac{2\varepsilon}{\kappa}-\frac{1}{n}.\)

<tbc>The two instances differ only on the tester constraints that query the unique message coordinate where _m_ and \(m'\) disagree; at most _d_ constraints change. By the triangle inequality, some such constraint _c_ satisfies<tbc>

\(\mathsf{EMD}_{\delta_\mathrm{H}}\left(\mathcal{A}(\mathcal{I}_C(m)),\mathcal{A}(\mathcal{I}_C(m)-c)\right)\ge\frac{1}{dk}\left(1-\frac{2t\varepsilon}{\kappa}\right)-\frac{2\varepsilon}{d\kappa}-\frac{1}{nd}.\)


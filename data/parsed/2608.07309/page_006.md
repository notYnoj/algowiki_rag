**Quantum search.**

**Theorem 2.5** (\[Gro96, BHMT00, HMdW03\])**.** _Let_ \(f:[N]\rightarrow\{0,1\}\) _be a predicate with a bounded- error coherent evaluation algorithm of cost T. There is a bounded-error quantum algorithm that finds an x satisfying f(x_)=1_, or reports that none exists, in time_ \(\widetilde{O}(\sqrt{N}T)\).

**Quantum walks.** Let _P_ be a reversible ergodic Markov chain on a finite state space, with stationary distribution \(\pi\) and spectral gap \(\delta\). Fix a marked set M and let D(_x_) denote the data stored with a state _x_. Let _T_set, _T_upd, and _T_chk denote the costs of preparing the stationary state and its data, coherently performing one transition and updating the data, and checking the vertex, respectively. The last operation maps, up to inverse-polynomial error,

\(|x\rangle|\mathcal{D}(x)\rangle\longmapsto(-1)^{[x\in\mathcal{M}]}|x\rangle|\mathcal{D}(x)\rangle,\)

and returns all ancillary registers to \(|0\rangle\).

**Theorem 2.6** (\[Sze04, MNRS11\])**.** _If_ \(\pi(\mathcal{M})\ge\mu\)_, then a state in_ M _can be found with bounded error in time_

\(\widetilde{O}\left(T_\text{set}+\frac{1}{\sqrt{\mu}}\left(\frac{1}{\sqrt{\delta}}T_\text{upd}+T_\text{chk}\right)\right).\)

**Quantum walks on Johnson graphs.** For a finite set X and \(1\le m\le|\mathcal{X}|/2\), the Johnson graph _J_(X_,m_) has the _m_-subsets of X as its vertices, with two subsets adjacent when their intersection has size _m_-1. Our algorithm uses the following lazy walk on \(J(\mathcal{X},m)\times J(\mathcal{X},m)\). At each step, the walk successively samples one of the two component subsets, a member of that subset, and an element of X from their respective uniform distributions. It replaces the sampled member by the sampled element unless the latter already belongs to the subset, in which case it stays in the same vertex. This walk is reversible and has the uniform stationary distribution. Kachigar and Tillich \[KT17\] show that its spectral gap is \(\delta=\Omega(1/m)\). Consequently, if at least a \(\mu\) fraction of its vertices are marked, Theorem 2.6 specializes to the running time

\(\widetilde{O}\left(T_\text{set}+\frac{1}{\sqrt{\mu}}\left(\sqrt{m}T_\text{upd}+T_\text{chk}\right)\right).\)

**Claw Finding.**

**Theorem 2.7** (\[Tan09\])**.** _Let_ L, R_, and_ Y _be finite sets with_ |Y|=poly(|L|,|R|)_, and let_ \(f:\mathcal{L}\rightarrow\mathcal{Y}\) _and_ \(g:\mathcal{R}\rightarrow\mathcal{Y}\)_. A_ claw _is a pair_ \((x,y)\in\mathcal{L}\times\mathcal{R}\) _satisfying f(x_)=_g(y). Suppose that_ \(|\mathcal{L}|\le|\mathcal{R}|^2\), \(|\mathcal{R}|\le|\mathcal{L}|^2\)_, and each function can be evaluated coherently in_ log<sup>_O_(1)</sup>(|L|+|R|) _time. Then there is a bounded-error quantum algorithm that finds a claw, or reports that none exists, in time_

\(\widetilde{O}\left((|\mathcal{L}|\cdot|\mathcal{R}|)^{1/3}\right).\)

## 3 The _k_-SUM Algorithm

We are now ready to prove Theorem 1.2.


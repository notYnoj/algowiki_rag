### D.3 Proof of Theorem 4.2

_Proof of Theorem 4.2._ Work on the armwise confidence event \(\mathcal{K}_\eta\) from Lemma D.1. This event has probability at least \(1-\eta\). Fix \(t\ge K\) and \(i\neq j\), and set<tbc>

\(m=N_{t,i},\ell=N_{t,j},H=H_t(\eta),N_\mathrm{eff}=\frac{m\ell}{m+\ell}.\)

<tbc>On \(\mathcal{K}_\eta\),<tbc>

\(|\widehat{\mu}_{t,i}-\mu_i|\le\sqrt{\frac{c_0H}{2m}},|\widehat{\mu}_{t,j}-\mu_j|\le\sqrt{\frac{c_0H}{2\ell}}.\)

<tbc>Let<tbc>

\(\varepsilon_\mu=\frac{1}{2}\mathrm{min}_{a\in[K]}\{\mu_a,1-\mu_a\}.\)

<tbc>First suppose that<tbc>

\(\mathrm{min}\{m,\ell\}\le\frac{2c_0}{\varepsilon_\mu^2}H.\)

<tbc>Assume without loss of generality that \(m\le\ell\). Evaluating the empirical infimum defining _V<sub>t</sub>(i,j_) at \(x=\mu_j\) gives<tbc>

\(V_t(i,j)\le md(\widehat{\mu}_{t,i},\mu_j)+\ell d(\widehat{\mu}_{t,j},\mu_j).\)

<tbc>The first term is at most \(C_\mu m\) because \(p\mapsto d(p,\mu_j)\) is bounded on \[0,1\], and the second term is at most _c_<sub>0</sub>_H_ on \(\mathcal{K}_\eta\). Thus \(V_t(i,j)\le C_\mu H\). The same evaluation at \(x=\mu_j\) gives<tbc>

\(V_t^\mu(i,j)\le md(\mu_i,\mu_j)\le C_\mu m\le C_\mu H.\)

<tbc>Hence<tbc>

\(|V_t(i,j)-V_t^\mu(i,j)|\le C_\mu H\)

<tbc>in the small-count regime.

<tbc>Now suppose that<tbc>

\(\mathrm{min}\{m,\ell\}>\frac{2c_0}{\varepsilon_\mu^2}H.\)

<tbc>Then both empirical means belong to \([\varepsilon_\mu/2,1-\varepsilon_\mu/2]\), and all true means belong to the same interval. Lemma D.2, applied with \(\varepsilon=\varepsilon_\mu/2\), gives<tbc>

\(|V_t(i,j)-V_t^\mu(i,j)|\le C_\mu N_\mathrm{eff}\left(|\widehat{\mu}_{t,i}-\mu_i|+|\widehat{\mu}_{t,j}-\mu_j|\right).\)

<tbc>Using the armwise confidence radii,<tbc>

\(|V_t(i,j)-V_t^\mu(i,j)|\le C_\mu N_\mathrm{eff}\left(\sqrt{\frac{H}{m}}+\sqrt{\frac{H}{\ell}}\right).\)

<tbc>Since \(N_\mathrm{eff}\le m\) and \(N_\mathrm{eff}\le\ell\),<tbc>

\(\frac{N_\mathrm{eff}}{\sqrt{m}}\le\sqrt{N_\mathrm{eff}},\frac{N_\mathrm{eff}}{\sqrt{\ell}}\le\sqrt{N_\mathrm{eff}}.\)

<tbc>Therefore,

\(|V_t(i,j)-V_t^\mu(i,j)|\le C_\mu\sqrt{N_\mathrm{eff}H}\)

in the large-count regime. Combining the two regimes proves the displayed bound. The event \(\mathcal{K}_\eta\) is simultaneous over all arms and all sample sizes, so the conclusion holds simultaneously over all \(t\ge K\) and all pairs \(i\neq j\).

## E Evidence Bounds in the Stabilized Regime

Let \(G_{t+1}\in\{0,1\}\) indicate whether the exploration guard is used at time _t_+1; for the unguarded rule, \(G_{t+1}\equiv 0\). We write<tbc>

\(\mathcal{J}:=[K]\backslash\{i^\star\},d_K:=|\mathcal{J}|=K-1.\)

<tbc>For \(j\in\mathcal{J}\), extend<tbc>

\(\Phi_j(n,m):=\mathrm{inf}_{x\in(0,1)}\left\{nd(\mu_{i^\star},x)+md(\mu_j,x)\right\}+\mathrm{log}m\)

<tbc>to real _m\>_0. For integers \(n\ge 1\) and \(S\ge d_K\),<tbc>

\(\Gamma_{n,S}^\mathrm{disc}(\mu)=\mathrm{max}_{m_j\in\{1,2,\dots\}:\sum_{j\in\mathcal{J}}m_j=S}\mathrm{min}_{j\in\mathcal{J}}\Phi_j(n,m_j).\)


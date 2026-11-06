Let \(\mathcal{A}_\eta\) be the event from Proposition F.1. Define<tbc>

\(\mathcal{E}_\mathrm{env}(\eta):=\mathcal{G}_\eta\cap\mathcal{A}_\eta.\)

<tbc>By Theorem 4.2 and Proposition F.1, this event has probability at least \(1-2\eta\). On \(\mathcal{E}_\mathrm{env}(\eta)\), Lemma E.4 gives, for every \(s\ge t_U\),<tbc>

\(\mathrm{min}_{j\in\mathcal{J}}Q_s(j)\ge\Gamma_{n_s,S_s}^\mathrm{disc}(\mu)-C_\mu(U)\left(t_U+G_s^\mathrm{tot}+\varepsilon_s+\mathrm{sup}_{t_U\le u\le s}u|\alpha_u-\beta|+1\right).\)

<tbc>On \(\mathcal{A}_\eta\), Proposition F.1 applied with _m=t<sub>U</sub>_ gives, uniformly over \(u\in[t_U,s]\),<tbc>

\(u|\alpha_u-\beta|\le C_\beta t_U+C_\beta\sqrt{s\widetilde{H}_s(\eta)}+G_s^\mathrm{tot}.\)

<tbc>If the guard is disabled, \(G_s^\mathrm{tot}=0\). If it is enabled, Lemma E.3 gives \(G_s^\mathrm{tot}\le\sqrt{Ks}+K\le C_K\sqrt{s\widetilde{H}_s(\eta)}\). Since

\(\varepsilon_s\le C_\mu\left(\sqrt{s\widetilde{H}_s(\eta)}+\widetilde{H}_s(\eta)\right),\)

the first displayed inequality in Proposition 5.1 follows.

For the empirical transportation costs, on \(\mathcal{G}_\eta\),<tbc>

\(|P_s(j)-Q_s(j)|\le C_\mu\left(\sqrt{sH_s(\eta)}+H_s(\eta)\right)\le C_\mu\left(\sqrt{s\widetilde{H}_s(\eta)}+\widetilde{H}_s(\eta)\right).\)

<tbc>Hence<tbc>

\(\mathrm{min}_jP_s(j)\ge\mathrm{min}_jQ_s(j)-C_\mu\left(\sqrt{s\widetilde{H}_s(\eta)}+\widetilde{H}_s(\eta)\right).\)

<tbc>After entry into the stabilized regime, _B_<sub>_s_+1</sub>=_i<sup>⋆</sup>_, so \(\widehat{\mu}_{s,i^\star}\ge\widehat{\mu}_{s,j}\) for every \(j\neq i^\star\). Therefore _W<sub>s</sub>(i<sup>⋆</sup>,j_)=_V<sub>s</sub>(i<sup>⋆</sup>,j_) for every \(j\neq i^\star\), and<tbc>

\(W_s(i^\star,j)=P_s(j)-\mathrm{log}N_{s,j}\ge P_s(j)-\mathrm{log}s.\)

<tbc>Combining this with Proposition 4.1,

\(\Gamma_{n_s,S_s}^\mathrm{disc}(\mu)\ge\frac{s}{T_{\alpha_s}^\star(\mu)}+\mathrm{log}s-C_\mu(U),\)

cancels the log_s_ term and proves the second displayed inequality.

## E.5 Challenger growth and separation

_Proof of Proposition 5.3._ Fix \(s\ge t_U\) and \(j\neq i^\star\). Proposition 5.1 gives<tbc>

\(Q_s(j)\ge\frac{s}{T_{\alpha_s}^\star(\mu)}-C_\mu(U)\left(t_U+\sqrt{s\widetilde{H}_s(\eta)}+\widetilde{H}_s(\eta)\right)-\overline{C_\mu}(U).\)

<tbc>Since \(\alpha_s\in U\), the leading term is at least \(\lambda_{\mu,U}s\). On the other hand, evaluating the population transportation cost at \(x=\mu_{i^\star}\) yields

\(Q_s(j)=V_s^\mu(i^\star,j)+\mathrm{log}N_{s,j}\le d(\mu_j,\mu_{i^\star})N_{s,j}+\mathrm{log}s.\)

Combining the two inequalities gives the claim.

**Lemma E.5** (Logarithmic separation thresholds)**.** _There exists_ \(A_\mu<\infty\) _such that for all_ \(\eta\in(0,1/2]\),<tbc>

\(n_\star(\eta)\le A_\mu\left(\mathrm{log}\frac{K}{\eta}+\mathrm{loglog}\frac{e}{\eta}+1\right).\)

<tbc>_Proof of Lemma E.5._ For each \(j\neq i^\star\), let \(\Delta_j:=\mu_{i^\star}-\mu_j>0\). The condition defining \(n_j(\eta)\) is<tbc>

\(\frac{c_0}{2n}\left(\mathrm{log}\frac{8K^2}{\eta}+\mathrm{loglog}(en)\right)\le\frac{\Delta_j^2}{16}.\)


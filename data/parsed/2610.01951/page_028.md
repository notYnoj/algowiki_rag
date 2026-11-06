For every fixed positive constant _A_, the inequality

\(n\ge A\left(log\frac{K}{\eta}+loglog\frac{e}{\eta}+1\right)\)

with _A_ sufficiently large implies the previous display uniformly over \(\eta\in(0,1/2]\). This follows from \(loglog(en)\le C_A+\frac{1}{2}log(e/\eta)\) after increasing _A_, and from the linear dominance of _n_ over the logarithmic terms. Taking the maximum over the finite set \(j\neq i^\star\) proves the claim.

_Proof of Corollary 5.4._ Let

\(L_\eta:=log\frac{K}{\eta}+loglog\frac{e}{\eta}+1.\)

By Lemma E.5, \(n_\star(\eta)\le A_\mu L_\eta\). Choose<tbc>

\(s=\left\lceil C_{\mu,\beta,U}(t_U+L_\eta)\right\rceil,\)

<tbc>with the constant to be fixed. For any \(\rho>0\), the elementary inequalities \(\sqrt{s\widetilde{H}_s(\eta)}\le\rho s+C_\rho\widetilde{H}_s(\eta)\) and \(log(es)\le\rho s+C_\rho\) imply<tbc>

\(\sqrt{s\widetilde{H}_s(\eta)}+\widetilde{H}_s(\eta)+logs\le\rho s+C_{\rho,\mu,U}L_\eta.\)

<tbc>Taking \(\rho\) small in Proposition 5.3 gives, for each \(j\neq i^\star\),

\(N_{s,j}\ge c_{\mu,U,j}s-C'_{\mu,U,j}t_U-C''_{\mu,U,j}L_\eta.\)

Choosing \(C_{\mu,\beta,U}\) sufficiently large ensures \(N_{s,j}\ge n_j(\eta)\) for all \(j\neq i^\star\). Since \(s\ge t_U\), entry into the stabilized regime gives \(N_{s,i^\star}=\alpha_ss\ge(infU)s\), and the same choice of \(C_{\mu,\beta,U}\) ensures \(N_{s,i^\star}\ge n_\star(\eta)\). Therefore \(s\ge t_\text{sep}(\eta)\), which proves the claim.

## F Leader-Fraction Control and Threshold Inversion

### F.1 Uniform leader-fraction concentration

**Proposition F.1** (Leader-fraction control, uniform in the start time)**.** _There exists a constant_ \(c_\beta>0\) _such that for every_ \(\eta\in(0,1)\) _there exists an event_ \(\mathcal{A}_\eta\) _with_ \(\mathbb{P}(\mathcal{A}_\eta)\ge 1-\eta\) _on which the following holds. For all integers_ \(m\ge 1\) _and all_ \(t\ge m\)_, if B_<sub>_u_+1</sub>=_i<sup>⋆</sup> for all_ \(u\ge m\)_, then_<tbc>

\(|(N_{t,i^\star}-N_{m,i^\star})-\beta(t-m)|\le c_\beta\sqrt{(t-m+1)log\left(\frac{etm^2}{\eta}\right)}+G_t^\text{tot}(m),\)

<tbc>_where_ \(G_t^\text{tot}(m):=\sum_{u=m}^{t-1}G_{u+1}\) _is the number of guard activations in_ {_m_+1_,...,t}. Consequently,_

\(|\alpha_t-\beta|\le\frac{(1+\beta)m}{t}+c_\beta\sqrt{\frac{1}{t}log\left(\frac{etm^2}{\eta}\right)}+\frac{G_t^\text{tot}(m)}{t}.\)

_Proof of Proposition F.1._ Fix \(\eta\in(0,1)\). For each \(m\ge 1\), set \(\eta_m:=6\eta/(\pi^2m^2)\) so that \(\sum_{m\ge 1}\eta_m\le\eta\).

Fix \(m\ge 1\) and assume _B_<sub>_u_+1</sub>=_i<sup>⋆</sup>_ for all \(u\ge m\). For the analysis, we enlarge the probability space by drawing an independent \(U_{u+1}\sim Ber(\beta)\) at every round, including guard rounds where this variable is not used by the algorithm. This does not change the law of the algorithm.

Fix \(m\ge 1\). For \(u\ge m\), define<tbc>

\(Z_{u+1}^{(m)}:=(U_{u+1}-\beta)\mathbf{1}\{G_{u+1}=0\}.\)

<tbc>Since _G_<sub>_u_+1</sub> is F_<sub>u</sub>_-measurable and _U_<sub>_u_+1</sub> is independent of F_<sub>u</sub>_ with mean \(\beta\), one has<tbc>

\(\mathbb{E}\left[Z_{u+1}^{(m)}|\mathcal{F}_u\right]=0,|Z_{u+1}^{(m)}|\le 1.\)


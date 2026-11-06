## G.2 High-probability stabilization bound for the unguarded rule

**Lemma G.1** (Separation-deficient nonleaders are cheap up to a polynomial horizon)**.** _There exist instance-dependent constants_ \(\widetilde{A}_\mu,\widetilde{B}_\mu>0\) _such that the following holds. Fix exponents_ \(a>\widetilde{A}_\mu\) _and_ \(b>\widetilde{B}_\mu+1\)_. Then there exists_ \(C_\mu^M<\infty\) _with the property that, for every_ \(\eta\in(0,1/4]\)_, if_<tbc>

\(M_\eta=\left\lceil C_\mu^M\eta^{-a}(log(e/\eta))^b\right\rceil,T_\eta=K+\left\lceil\frac{2K}{p}(M_\eta-1)+\frac{16}{p^2}log\frac{6}{\eta}\right\rceil,\)

<tbc>_where_ \(p=min\{\beta,1-\beta\}\)_, then on the event_ \(\mathcal{G}_{\eta/6}\cap\mathcal{K}_{\eta/6}\) _the following implication holds for every_ \(t\le T_\eta\)_. If_ \(j\neq B_{t+1}\) _and_<tbc>

\(N_{t,j}<\left\{\begin{array}{ c c }
n_\star(\eta/6), & j=i^\star, \\
n_j(\eta/6), & j\neq i^\star,
\end{array}\right.\)

<tbc>_then_

\(W_t(B_{t+1},j)+logN_{t,j}\le log(M_\eta-1).\)

_Consequently, whenever such a separation-deficient nonleader exists, the greedy challenger selected by the unguarded rule has count strictly smaller than_ \(M_\eta\).

_Proof of Lemma G.1._ Let \(j\neq B_{t+1}\) satisfy the displayed separation-deficiency condition. Then \(N_{t,j}\le n_\star(\eta/6)\). Since _B_<sub>_t_+1</sub> is an empirical leader, \(\widehat{\mu}_{t,B_{t+1}}\ge\widehat{\mu}_{t,j}\), and therefore _W<sub>t</sub>(B_<sub>_t_+1</sub>_,j_)=_V<sub>t</sub>(B_<sub>_t_+1</sub>_,j_). Evaluating the population symmetric GLR at \(x=\mu_{B_{t+1}}\) gives<tbc>

\(V_t^\mu(B_{t+1},j)\le D_\mu^{max}n_\star(\eta/6),\)

<tbc>where<tbc>

\(D_\mu^{max}:=max_{a\neq b}d(\mu_a,\mu_b)<\infty.\)

<tbc>On \(\mathcal{G}_{\eta/6}\), Theorem 4.2 and the crude bound \(N_{\mathrm{eff},t}(B_{t+1},j)\le N_{t,j}\le n_\star(\eta/6)\) imply<tbc>

\(W_t(B_{t+1},j)\le D_\mu^{max}n_\star(\eta/6)+C_\mu\left(\sqrt{n_\star(\eta/6)H_{T_\eta}(\eta/6)}+H_{T_\eta}(\eta/6)\right).\)

<tbc>Using Lemma E.5 and the polynomial form of \(T_\eta\), the right side plus \(logN_{t,j}\le logn_\star(\eta/6)\) is bounded by

\(\widetilde{A}_\mu log(1/\eta)+\widetilde{B}_\mu loglog(e/\eta)+O_\mu(1).\)

Choosing \(a>\widetilde{A}_\mu\), \(b>\widetilde{B}_\mu+1\), and then \(C_\mu^M\) large enough makes this upper bound at most \(log(M_\eta-1)\) and also ensures \(M_\eta\ge n_\star(\eta/6)+1\) for all \(\eta\in(0,1/4]\).

For the final claim, any arm _k_ with \(N_{t,k}\ge M_\eta\) has penalized index at least \(logM_\eta\), since transportation costs are nonnegative. A separation-deficient nonleader has index at most \(log(M_\eta-1)\), so a minimizer of the challenger index cannot have count at least \(M_\eta\).

_Proof of Proposition 6.2._ Fix \(\eta\in(0,1/4]\) and write \(\overline{\eta}:=\eta/6\). Let \(M_\eta,T_\eta\) be the quantities from Lemma G.1, and set \(p:=min\{\beta,1-\beta\}\). Define

\(X_{t+1}:=\mathbf{1}\{N_{t,I_{t+1}}<M_\eta\},D_t:=\sum_{i=1}^K(M_\eta-N_{t,i})_+,t\ge K.\)

Since each arm is pulled once initially, \(D_K=K(M_\eta-1)\) and _D_<sub>_t_+1</sub>=_D<sub>t</sub>-X_<sub>_t_+1</sub>. Let \(\tau_M:=inf\{t\ge K:D_t=0\}\). At time \(\tau_M\) all arms have at least \(M_\eta\) pulls. By Lemma G.1, \(M_\eta\ge n_\star(\overline{\eta})\), so \(t_\mathrm{sep}(\overline{\eta})\le\tau_M\).

Put

\(\mathcal{E}_\overline{\eta}:=\mathcal{G}_\overline{\eta}\cap\mathcal{K}_\overline{\eta}.\)

All martingale statements below are taken under the original probability measure. For \(s=K,\dots,T_\eta-1\), define martingale differences

\(Y_{s+1}:=X_{s+1}-\mathbb{E}[X_{s+1}|\mathcal{F}_s].\)

Then \(\mathbb{E}[Y_{s+1}|\mathcal{F}_s]=0\) and \(|Y_{s+1}|\le 1\).


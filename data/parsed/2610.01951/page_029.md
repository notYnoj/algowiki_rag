Thus

\(S_t^{(m)}:=\sum_{u=m}^{t-1}Z_{u+1}^{(m)},t\ge m,\)

is a martingale with bounded increments under the original probability measure.

For \(n\ge 1\), put _t=m+n_. Azuma-Hoeffding gives

\(\mathbb{P}_\mu\left(|S_{m+n}^{(m)}|\ge\sqrt{2nlog\left(\frac{12n^2}{\eta_m}\right)}\right)\le\frac{\eta_m}{6n^2},\)

where \(\eta_m:=6\eta/(\pi^2m^2)\). A union bound over \(n\ge 1\) gives, with probability at least \(1-\eta_m\),

\(|S_t^{(m)}|\le c_\beta\sqrt{(t-m+1)log\left(\frac{etm^2}{\eta}\right)}\forall t\ge m,\)

after increasing the numerical constant \(c_\beta\).

Now suppose that _B_<sub>_u_+1</sub>=_i<sup>⋆</sup>_ for every \(u\ge m\). On every non-guard round _u_+1 in this range, the algorithm pulls _i<sup>⋆</sup>_ if and only if _U_<sub>_u_+1</sub>=1. Hence, for every \(t\ge m\),

\((N_{t,i^\star}-N_{m,i^\star})-\beta(t-m)\)<br>
\(=\sum_{u=m}^{t-1}(U_{u+1}-\beta)\mathbf{1}\{G_{u+1}=0\}+\sum_{u=m}^{t-1}(\mathbf{1}\{I_{u+1}=i^\star\}-\beta)\mathbf{1}\{G_{u+1}=1\}.\)

The first sum is \(S_t^{(m)}\). The second sum has absolute value at most \(G_t^\mathrm{tot}(m)\), because each summand is bounded by one in absolute value and is nonzero only on guard rounds. Therefore,

\(|(N_{t,i^\star}-N_{m,i^\star})-\beta(t-m)|\le c_\beta\sqrt{(t-m+1)log\left(\frac{etm^2}{\eta}\right)}+G_t^\mathrm{tot}(m).\)

Finally, intersecting the events over all \(m\ge 1\) and using \(\sum_{m\ge 1}\eta_m\le\eta\) gives the desired event \(\mathcal{A}_\eta\).

## F.2 Entrance into a compact neighborhood of \(\beta\)

**Lemma F.2** (Entrance into a fixed compact neighborhood of \(\beta\))**.** _Fix a compact interval_ \(U=[\beta-\rho,\beta+\rho]\sqsubset(0,1)\) _with_ \(\rho>0\)_. There exists_ \(C_{\beta,U}<\infty\) _such that the following holds. On the event of Proposition F.1, if_ \(t_\mathrm{lead}\le L\) _with_ \(L\ge 1\)_, then_

\(\alpha_t\in U\forall t\ge C_{\beta,U}\left(L+K+log\frac{e(L+1)^2}{\eta}\right).\)

_When the guard is disabled, the additive K term can be dropped._

_Proof of Lemma F.2._ If the guard is enabled, Proposition F.1 yields for all \(t\ge t_\mathrm{lead}\),

\(|\alpha_t-\beta|\le\frac{(1+\beta)L}{t}+c_\beta\sqrt{\frac{1}{t}log\left(\frac{et(L+1)^2}{\eta}\right)}+\frac{G_t^\mathrm{tot}(t_\mathrm{lead})}{t}.\)

By Lemma E.3, the last term is at most \(\sqrt{K/t}+K/t\), and it is absent in the unguarded case. Let

\(A:=L+K+log\frac{e(L+1)^2}{\eta}.\)

For \(t\ge CA\), the first and guard terms are at most \(\rho/3\) once _C_ is large enough. The middle term is also at most \(\rho/3\): the map \(t\mapsto log(et(L+1)^2/\eta)/t\) is decreasing above an absolute constant, and at _t=CA_ its numerator is bounded by a constant multiple of _A_. Increasing _C_ if necessary proves the claim.


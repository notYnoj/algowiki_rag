### About the two results.

Proposition 4.1 identifies the best minimum population penalized index attainable at fixed integer pull totals. A deterministic argument for the greedy challenger-count update in Appendix E relates the actual challenger counts to this benchmark. Theorem 4.2 then controls the error incurred when the true means are replaced by adaptive empirical means. Once the true best arm is the empirical leader, the one-sided statistic used by the algorithm satisfies _W<sub>t</sub>(i<sup>⋆</sup>,j_)=_V<sub>t</sub>(i<sup>⋆</sup>,j_). The two results can therefore be combined to lower-bound the evidence against every challenger.

## 5 Sharp Guarantees in the Stabilized Regime

We first analyze the algorithm after both its leader and its best-arm sampling fraction have stabilized. Define its sampling fraction by \(\alpha_t=N_{t,i^\star}/t\). Fix a compact interval \(U\Subset(0,1)\) whose interior contains \(\beta\). We call _t<sub>U</sub>_ a _U-stabilization time_ if _B_<sub>_t_+1</sub>=_i<sup>⋆</sup>_ and \(\alpha_t\in U,\forall t\ge t_U\). Thus, after a _U_-stabilization time, the true best arm remains the empirical leader and its sampling fraction stays in _U_. Throughout this section, _stabilization_ refers to this joint condition, not only to the leader identity.

For an almost-surely finite random time _T_, an _upper-quantile bound_ is a function \(u_T:(0,1]\rightarrow[0,\infty)\) satisfying

\(\mathbb{P}_\mu\left(T\le u_T(\eta)\right)\ge 1-\eta\text{for every}\eta\in(0,1].\)

Equivalently, \(u_T(\eta)\) is a \((1-\eta)\)-confidence upper bound on _T_. We call the bound _summable_ if \(\sum_{k\ge 0}2^{-k}u_T(2^{-k})<\infty\). This dyadic summability condition is strong enough to integrate the tail bound and obtain a finite contribution to \(\mathbb{E}_\mu[T]\).

For \(t\ge t_U\) and \(j\neq i^\star\), the challenger rule compares the empirical penalized indices _P<sub>t</sub>(j_)=_V<sub>t</sub>(i<sup>⋆</sup>,j_)+log_N<sub>t,j</sub>_. Their population counterparts are \(Q_t(j)=\Phi_j(N_{t,i^\star},N_{t,j})=V_t^\mu(i^\star,j)+logN_{t,j}\). After stabilization, _B_<sub>_t_+1</sub>=_i<sup>⋆</sup>_, so \(\widehat{\mu}_{t,i^\star}\ge\widehat{\mu}_{t,j}\) for every \(j\neq i^\star\) and therefore _W<sub>t</sub>(i<sup>⋆</sup>,j_)=_V<sub>t</sub>(i<sup>⋆</sup>,j_). For later bounds, we also use the slightly looser confidence term

\(\widetilde{H}_t(\eta):=log(K/\eta)+log(et).\)

**Proposition 5.1** (Uniform lower bound on evidence against all challengers)**.** _Fix a compact interval_ \(U\Subset(0,1)\) _containing_ \(\beta\) _in its interior. There exist constants_ \(C_\mu(U),\overline{C_\mu}(U)<\infty\) _such that for every_ \(\eta\in(0,1)\) _there is an event_ \(\mathcal{E}_\text{env}(\eta)\) _with_ \(\mathbb{P}_\mu(\mathcal{E}_\text{env}(\eta))\ge 1-2\eta\) _on which the following holds simultaneously for every U-stabilization time t<sub>U</sub> and every_ \(s\ge t_U\):

\(min_{j\neq i^\star} Q_s(j)\ge\Gamma_{N_{s,i^\star},s-N_{s,i^\star}}^\text{disc}(\mu)-C_\mu(U)\left(t_U+\sqrt{s\widetilde{H}_s(\eta)}+\widetilde{H}_s(\eta)\right)-\overline{C_\mu}(U).\)

_Consequently, on the same event,_

\(min_{j\neq i^\star} W_s(i^\star,j)\ge\frac{s}{T_{\alpha_s}^\star(\mu)}-C_\mu(U)\left(t_U+\sqrt{s\widetilde{H}_s(\eta)}+\widetilde{H}_s(\eta)\right)-\overline{C_\mu}(U).\)

**Theorem 5.2** (Non-asymptotic stopping bound in the stabilized regime)**.** _Fix_ \(\beta\in(0,1)\) _and a compact interval_ \(U\Subset(0,1)\) _containing_ \(\beta\) _in its interior. Let t<sub>U</sub> be an almost-surely finite U-stabilization time. Then there exist instance-dependent constants_ \(C_{\mu,0}(U),C_{\mu,1}(U),C_{\mu,2}(U),C_{\mu,3}(U)<\infty\) _such that, for every_ \(\delta\in(0,1/2]\) _and every_ \(\eta\in(0,1/4]\)_, with probability at least_ \(1-3\eta\),

\(\tau_\delta\le(1+C_{\mu,0}(U))t_U+T_\beta^\star(\mu)log(1/\delta)+C_{\mu,1}(U)\sqrt{log(1/\delta)\left(log\frac{K}{\eta}+loglog\frac{e}{\delta}\right)}\)<br>
\(+C_{\mu,2}(U)\left(log\frac{K}{\eta}+loglog\frac{e}{\delta}\right)+C_{\mu,3}(U).\)

_Moreover, if t<sub>U</sub> admits a summable upper-quantile bound, then there exist constants_ \(C'_{\mu,1}(U),C'_{\mu,2}(U),C'_{\mu,3}(U)<\infty\) _such that, for all_ \(\delta\in(0,1/2]\),

\(\mathbb{E}_\mu[\tau_\delta]\le T_\beta^\star(\mu)log(1/\delta)+C'_{\mu,1}(U)\sqrt{log(1/\delta)loglog(e/\delta)}+C'_{\mu,2}(U)loglog(e/\delta)+C'_{\mu,3}(U).\)

Appendix F gives the proof. The lower-order terms have four sources: the time _t<sub>U</sub>_ needed to enter the stabilized regime; fluctuations of the pairwise GLR statistics and of the best-arm sampling fraction; the uniform-in-time confidence error and inversion of the stopping threshold; and bounded discretization, penalty, and early-time effects. None changes the fixed-\(\beta\) coefficient multiplying \(log(1/\delta)\).


### What remains to be controlled.

Theorem 5.2 reduces the remaining problem to controlling the _U_-stabilization time _t<sub>U</sub>_. A high-probability bound on _t<sub>U</sub>_ gives a high-probability stopping bound, while a summable upper-quantile bound gives an expected stopping-time bound.

The next proposition shows why this reduction is useful: in the stabilized regime, the penalized challenger rule cannot keep any suboptimal arm under-sampled. Each suboptimal-arm pull count grows linearly after a transient determined by _t<sub>U</sub>_ and the concentration error.

**Proposition 5.3** (Linear growth of every suboptimal-arm pull count in the stabilized regime)**.** _Fix a compact interval_ \(U\Subset(0,1)\) _containing_ \(\beta\) _in its interior and define_ \(\lambda_{\mu,U}:=inf_{\alpha\in U}T_\alpha^\star(\mu)^{-1}>0\)_. On the event of Proposition 5.1, simultaneously for all_ \(s\ge t_U\) _and all_ \(j\neq i^\star\),<tbc>

\(N_{s,j}\ge\frac{\lambda_{\mu,U}s-C_\mu(U)\left(t_U+\sqrt{s\widetilde{H}_s(\eta)}+\widetilde{H}_s(\eta)\right)-\overline{C_\mu}(U)-logs}{d(\mu_j,\mu_{i^\star})}.\)

<tbc>To translate count growth into permanent empirical separation, let _c_<sub>0</sub>_\>_0 be the universal constant from the armwise time-uniform confidence bound in Appendix D.1, and define

\(r(n,\eta)=\sqrt{\frac{c_0}{2n}\left(log\frac{8K^2}{\eta}+loglog(en)\right)},\)<br>
\(n_j(\eta)=min\left\{n\ge 1:r(n,\eta)\le\frac{\mu_{i^\star}-\mu_j}{4}\right\},n_\star(\eta)=max_{j\neq i^\star} n_j(\eta).\)

Here \(n_j(\eta)\) is the number of samples needed to estimate arms _i<sup>⋆</sup>_ and _j_ to within one quarter of their mean gap. Define the first time at which all of these count requirements hold by \(t_\mathrm{sep}(\eta)=inf\left\{t\ge K:N_{t,i^\star}\ge n_\star(\eta)\text{and}N_{t,j}\ge n_j(\eta)\forall j\neq i^\star\right\}\).

Let \(\mathcal{K}_\eta^\mathrm{sep}\) denote the simultaneous armwise event

\(|\widehat{\mu}_{t,i}-\mu_i|\le r(N_{t,i},\eta),\forall t\ge K,i\in[K].\)

The time-uniform confidence-sequence result in Appendix D.1 gives \(\mathbb{P}_\mu(\mathcal{K}_\eta^\mathrm{sep})\ge 1-\eta\).

**Corollary 5.4** (Time until all arm counts support empirical separation)**.** _Fix a compact interval_ \(U\Subset(0,1)\) _containing_ \(\beta\) _in its interior. There exists_ \(C_{\mu,\beta,U}<\infty\) _such that for every_ \(\eta\in(0,1/4]\)_, on the event of Proposition 5.1,_ \(t_\mathrm{sep}(\eta)\le C_{\mu,\beta,U}\left(t_U+log(K/\eta)+loglog(e/\eta)+1\right)\).

### Interpretation.

In the stabilized regime, the greedy penalized rule forces every suboptimal-arm pull count to grow linearly. An imbalanced configuration at time _t<sub>U</sub>_ may require a transient proportional to _t<sub>U</sub>_, but there is no additional long-run under-sampling mechanism. For the unguarded algorithm, the remaining challenge is therefore to bound the time needed to enter that regime.

## 6 Reaching the Stabilized Regime

Section 5 assumes that a _U_-stabilization time _t<sub>U</sub>_ is available. We now derive such a time. First, we control \(t_\mathrm{sep}(\eta)\), the first time at which every arm has enough samples for the simultaneous confidence bounds to separate the best arm from every suboptimal arm. We then control the best-arm sampling fraction around \(\beta\).

**Proposition 6.1** (Sufficient sampling makes the leader permanently correct)**.** _On_ \(\mathcal{K}_\eta^\mathrm{sep}\)_, the empirical leader is permanently correct after_ \(t_\mathrm{sep}(\eta)\): \(B_{t+1}=i^\star,\forall t\ge t_\mathrm{sep}(\eta)\)_. Combining this permanent- leader property with control of the best-arm sampling fraction yields a high-probability bound on the time to enter the stabilized regime._

**Proposition 6.2** (High-probability stabilization bound for the unguarded algorithm)**.** _For the unguarded_ \(\beta\)_-EB-TCI algorithm, there exist instance-dependent constants_ \(a_\mu>0\), \(b_\mu\ge 0\)_, and_ \(C_{\mu,\beta}^\mathrm{sep}<\infty\) _such that for every_ \(\eta\in(0,1/4]\), \(\mathbb{P}_\mu\left(t_\mathrm{sep}(\eta/6)\le C_{\mu,\beta}^\mathrm{sep}\eta^{-a_\mu}\left(log(e/\eta)\right)^{b_\mu}\right)\ge 1-\eta/2\)_. Consequently, for every compact interval_ \(U\Subset(0,1)\) _containing_ \(\beta\) _in its interior, there exists a U-stabilization time t<sub>U</sub> and a constant_ \(C_{\mu,\beta}^U<\infty\) _such that_ \(\mathbb{P}_\mu\left(t_U\le C_{\mu,\beta}^U\eta^{-a_\mu}\left(log(e/\eta)\right)^{b_\mu}\right)\ge 1-\eta\).


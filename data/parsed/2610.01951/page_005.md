## 4 Population Allocation Benchmark and Uniform GLR Control

### 4.1 A discrete penalized allocation benchmark

We first describe the population allocation benchmark used in the analysis. For a prescribed best-arm fraction \(\alpha\in(0,1)\) and a suboptimal arm \(j\neq i^\star\), define \(I_j^\alpha(w)=inf_{x\in(0,1)}\left\{\alpha d(\mu_{i^\star},x)+wd(\mu_j,x)\right\},w>0\). If arm _j_ receives asymptotic fraction _w_, then \(I_j^\alpha(w)\) is the per-round information rate for separating _i<sup>⋆</sup>_ from _j_. Allocating the remaining mass \(1-\alpha\) across all suboptimal arms gives the constrained characteristic time \(T_\alpha^\star(\mu)^{-1}=max_{w\in\Delta_{1-\alpha}} min_{j\neq i^\star} I_j^\alpha(w_j)\), where \(\Delta_{1-\alpha}=\left\{w\in(0,\infty)^{K-1}:\sum_{j\neq i^\star} w_j=1-\alpha\right\}\). Decom posing the full allocation simplex by the best-arm coordinate gives the global characteristic time

\(T^\star(\mu):=min_{\alpha\in(0,1)}T_\alpha^\star(\mu),T_\beta^\star(\mu)\ge T^\star(\mu).\)

Thus \(T_\beta^\star(\mu)\) quantifies the possible loss from prescribing the best-arm fraction instead of optimizing it. We keep \(\beta\) fixed throughout; we do not analyze an online estimate or adaptive choice of \(\beta\).

To connect this continuous allocation problem to integer pull counts, let _n_ denote a best-arm pull count and let _s_ denote the total pull count assigned to all other arms. For integers \(n\ge 1\) and \(s\ge K-1\), define \(\Phi_j(n,m)=inf_{x\in(0,1)}\left\{nd(\mu_{i^\star},x)+md(\mu_j,x)\right\}+logm\), and define the discrete penalized allocation benchmark

\(\Gamma_{n,s}^\mathrm{disc}(\mu)=max_{m\in\{1,2,\dots\}}^{K-1:\sum_{j\neq i^\star} m_j=s}min_{j\neq i^\star}\Phi_j(n,m_j).\)

This optimization uses the true means and integer pull counts; it is therefore a population-level benchmark, not an implementable algorithm. It describes the largest possible minimum penalized index across challengers with _n_ best-arm pulls and _s_ non-best-arm pulls, including the same logarithmic penalty used by \(\beta\)-EB-TCI.

**Proposition 4.1** (Approximation of the discrete penalized benchmark)**.** _Fix a compact interval_ \(U\Subset(0,1)\)_. There exists a constant_ \(C_\mu(U)<\infty\) _such that for every_ \(n\ge 1\) _and every_ \(s\ge K-1\)_, if t=n+s,_ \(\alpha=n/t\)_, and_ \(\alpha\in U\)_, then_

\(\left|\Gamma_{n,s}^\mathrm{disc}(\mu)-\left(\frac{t}{T_\alpha^\star(\mu)}+logt\right)\right|\le C_\mu(U).\)

To interpret the proposition, set _t=n+s_, \(\alpha=n/t\), and _w<sub>j</sub>=m<sub>j</sub>/t_. The continuous allocation problem predicts the leading value \(t/T_\alpha^\star(\mu)\), while the count penalty contributes log_t_. Proposition 4.1 shows that integer rounding and the arm-dependent terms inside log_m<sub>j</sub>_ change this value by only \(O_\mu(1)\), uniformly when \(\alpha\) stays in a compact subset of (0,1).

### 4.2 Uniform comparison of empirical and population pairwise GLR statistics

For the analysis, define the time-uniform confidence term \(H_t(\eta):=\mathrm{log}(K/\eta)+\mathrm{loglog}(et)\) and the two-arm effective sample size \(N_{\mathrm{eff},t}(i,j):=\frac{N_{t,i}N_{t,j}}{N_{t,i}+N_{t,j}}\). This effective sample size satisfies \(\frac{1}{2}\mathrm{min}\{N_{t,i},N_{t,j}\}\le N_{\mathrm{eff},t}(i,j)\le\mathrm{min}\{N_{t,i},N_{t,j}\}\). The next theorem shows that the empirical pairwise GLR stays uniformly close to its counterpart computed at the true means, at the corresponding fluctuation scale.

**Theorem 4.2** (Time-uniform pairwise Bernoulli GLR approximation)**.** _There exists an instance- dependent constant_ \(C_\mu<\infty\) _such that for every_ \(\eta\in(0,1)\) _there is an event_ \(\mathcal{G}_\eta\) _with_ \(\mathbb{P}_\mu(\mathcal{G}_\eta)\ge 1-\eta\) _and, on_ \(\mathcal{G}_\eta\)_, simultaneously for all_ \(t\ge K\) _and all pairs_ \(i\neq j\),

\(|V_t(i,j)-V_t^\mu(i,j)|\le C_\mu\left(\sqrt{N_{\mathrm{eff},t}(i,j)H_t(\eta)}+H_t(\eta)\right).\)

The population statistic \(V_t^\mu(i,j)\) grows on the scale _N_eff_,t(i,j_), while the deviation is of order \(\sqrt{N_{\mathrm{eff},t}(i,j)H_t(\eta)}+H_t(\eta)\). Therefore, if both arms are sampled increasingly often, the relative error vanishes. This quantitative statement lets us transfer the population allocation bound to the adaptive empirical indices used by the algorithm.


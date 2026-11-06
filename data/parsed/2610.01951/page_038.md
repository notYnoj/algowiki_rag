### G.5 Guarded expected bound

_Proof of Proposition 6.6._ Let \(m\ge 1\) and define epoch boundaries _t<sub>m</sub>=Km_<sup>2</sup>. By initialization, _N_<sub>_t_<sub>1</sub>_,i_</sub>=1 for all arms. Assume inductively that \(N_{t_m,i}\ge m\) for all arms. Consider any time \(t\in\{t_m,\dots,t_{m+1}-1\}\). Since \(\sqrt{t/K}<m+1\), the guard condition implies \(min_iN_{t,i}\le m\). Each time the guard triggers, it pulls a least-sampled arm. After at most _K_ such guard pulls, all arms satisfy \(N_{t,i}\ge m+1\). Because the interval length is \(t_{m+1}-t_m=K(2m+1)\ge K\), this happens no later than _t_<sub>_m_+1</sub>. The lower bound on min_<sub>i</sub>N<sub>t,i</sub>_ follows by induction. The bound on \(t_\mathrm{sep}(\eta)\) is immediate. The polylogarithmic upper-quantile bound for an _U_-stabilization time _t<sub>U</sub>_ follows by combining Lemma E.5, Proposition 6.1, Proposition F.1, and Lemma F.2.

_Proof of Theorem 6.7._ By Proposition 6.6 and Lemma F.2, the guard yields a polylogarithmic upper- quantile bound for a _U_-stabilization time _t<sub>U</sub>_. In particular, both the probability requirement and the dyadic summability condition in Theorem 5.2 hold. Applying the expectation part of Theorem 5.2 completes the proof.

### G.6 Limitation of one-step index comparisons

**Lemma G.2** (Asymptotics under a frozen wrong leader)**.** _Fix_ \(b\neq u\) _and counts_ \(m\ge 1\)_. Then the map_

\(n\mapsto\mathrm{inf}_{x\in(0,1)}\left\{nd(\mu_b,x)+md(\mu_u,x)\right\}\)

_is nondecreasing, and as_ \(n\rightarrow\infty\) _it converges to_ \(md(\mu_u,\mu_b)\).

_Proof of Lemma G.2._ Monotonicity in _n_ is immediate because the objective contains the nonnegative term \(nd(\mu_b,x)\). Evaluating at \(x=\mu_b\) gives the upper bound \(md(\mu_u,\mu_b)\). Conversely, let _x<sub>n</sub>_ be any sequence of near-minimizers. If \(d(\mu_b,x_n)\) failed to converge to zero, then the term \(nd(\mu_b,x_n)\) would diverge, contradicting the finite upper bound obtained by evaluating at \(x=\mu_b\). Hence \(x_n\rightarrow\mu_b\), and continuity gives the matching lower bound.

_Proof of Proposition 6.8._ Because \(\mu_j=\mu_b=\lambda\), choosing \(x=\lambda\) gives<tbc>

\(\Phi_j^{(b)}(n,M(\eta))=\mathrm{log}M(\eta)\)

<tbc>for every _n_. Fix any \(a<Cd(\mu_u,\lambda)\) and choose \(\varepsilon>0\) so that \(a<Cd(\mu_u,\lambda)-2\varepsilon\). By Lemma G.2, for every sufficiently small \(\eta\) there exists \(n_\eta\) such that for all \(n\ge n_\eta\),<tbc>

\(\mathrm{inf}_x\left\{nd(\lambda,x)+m_u(\eta)d(\mu_u,x)\right\}\ge m_u(\eta)d(\mu_u,\lambda)-\varepsilon\mathrm{log}(e/\eta).\)

<tbc>Since \(m_u(\eta)\ge C\mathrm{log}(e/\eta)\) for small \(\eta\),<tbc>

\(\Phi_u^{(b)}(n,m_u(\eta))\ge(Cd(\mu_u,\lambda)-\varepsilon)\mathrm{log}(e/\eta)+\mathrm{log}m_u(\eta).\)

<tbc>By assumption, for all sufficiently small \(\eta\) and all \(n\ge n_\eta\),<tbc>

\(\mathrm{log}M(\eta)=\Phi_j^{(b)}(n,M(\eta))\ge\Phi_u^{(b)}(n,m_u(\eta))\ge(Cd(\mu_u,\lambda)-\varepsilon)\mathrm{log}(e/\eta).\)

<tbc>Hence

\(M(\eta)\ge\eta^{-(Cd(\mu_u,\lambda)-\varepsilon)}.\)

Because \(a<Cd(\mu_u,\lambda)-2\varepsilon\), this implies \(M(\eta)\ge\eta^{-a}\) for all sufficiently small \(\eta\).

## H Experiment Details

This appendix gives the full protocol behind Section 7. The experiments are synthetic Bernoulli bandit simulations and use no external datasets.


<tbc>the stabilized regime when several suboptimal arms share the same mean. We do not resolve that problem here. The next proposition only explains why one direct proof route is insufficient.

Fix a provisional leader \(b\neq i^\star\). If its count is held at _n_ while a candidate challenger \(u\neq b\) has count _m_, define the corresponding population penalized index \(\Phi_u^{(b)}(n,m)=inf_{x\in(0,1)}\left\{nd(\mu_b,x)+md(\mu_u,x)\right\}+logm\).

**Proposition 6.8** (Limitation of one-step penalized-index comparisons)**.** _Fix three arms b, j, u such that_ \(\mu_b=\mu_j=\lambda<\mu_u\)_. Let C\>_0 _and define_ \(m_u(\eta)=\lceil Clog(e/\eta)\rceil\)_. Suppose_ \(M:(0,e^{-1}]\rightarrow\mathbb{N}\) _is such that for every sufficiently small_ \(\eta\) _and all sufficiently large n,_ \(\Phi_u^{(b)}(n,m_u(\eta))\le\Phi_j^{(b)}(n,M(\eta))\)_. Then for every_ \(a<Cd(\mu_u,\lambda)\), \(M(\eta)\ge\eta^{-a}\) _for all sufficiently small_ \(\eta\).

The premise compares the two population indices at a single pair of pull counts. The conclusion says that, if the higher-mean arm _u_ receives only \(O(log(1/\eta))\) pulls, then forcing its index below that of an equal-mean suboptimal arm requires the latter count to be polynomial in \(1/\eta\). Proposition 6.8 therefore limits this one-step comparison argument only. It is not an impossibility result for the algorithm and does not rule out finite-mean exploration under deterministic tie-breaking via a more global, path-dependent analysis.

## 7 Experiments

The experiments examine four questions directly connected to the analysis: (i) how observed stopping times compare with the predictor based on \(T_\beta^\star(\mu)\); (ii) how performance changes with the leader- sampling probability \(\beta\); (iii) how many pulls are introduced by the guard; and (iv) what changes when the logarithmic challenger penalty is removed. These experiments are diagnostic and are not intended as a broad comparison of best-arm algorithms. All experiments use Bernoulli rewards, the stopping threshold in (3.1), and smallest-index tie-breaking.

### Protocol.

We use three representative mean vectors: `SEP5`=\[0.70,0.50,0.40,0.30,0.20\] has well-separated arms, `CLUSTER-CLOSE5`=\[0.70,0.64,0.63,0.62,0.61\] has distinct but closely clustered suboptimal arms, and `TIE-CLOSE4`=\[0.60,0.56,0.56,0.56\] has three equal-mean suboptimal arms. The evaluation grid contains three instances, \(\beta\in\{0.3,0.5,0.7\}\), and \(\delta\in\{10^{-4},10^{-5},10^{-6},10^{-7},10^{-8}\}\). For each setting we run both the unguarded and guarded algorithms with 200 independent replications. We compare the empirical mean stopping time with the threshold-crossing predictor

\(t_\text{pred}(\mu,\beta,\delta):=min\{t\ge K:t/T_\beta^\star(\mu)>c(t,\delta)\}.\)

This predictor is the smallest time at which the leading information \(t/T_\beta^\star(\mu)\) exceeds the same threshold used by the algorithm. Appendix H gives the full grids, random-seed policy, numerical solver, uncertainty summaries, stopping caps, and additional diagnostics. The supplementary code package provides the reproduction commands.

### Predictor agreement and sensitivity to \(\beta\).

Here, predictor agreement means closeness between the empirical mean stopping time and _t_pred. Figure 1 shows the scaling at \(\beta=0.5\). The empirical means track the threshold-crossing predictor on both `SEP5` and `TIE-CLOSE4`. Across the 45 guarded settings, the mean and maximum absolute relative errors with respect to _t_pred are 1.53% and 3.86%; for the unguarded settings, they are 1.66% and 4.20%. None of the 18,000 penalized runs reaches the 700,000-round cap or recommends a wrong arm. Figure 2 also shows that the dependence on \(\beta\) is nonmonotone and instance-specific, as predicted by \(T_\beta^\star(\mu)\); the raw mean gaps alone do not determine the best choice of \(\beta\).

### Guard overhead, effect of removing the penalty, and an idealized reference.

Appendix H reports the full diagnostics. On `TIE-CLOSE4` with \(\beta=0.5\) and \(\delta=10^{-8}\), enabling the guard changes the median stopping time from 104,918 to 103,743 and the empirical 95th percentile from 134,140 to 130,792; the largest mean fraction of guarded pulls in the tested equal-mean instances is 0.0069%. Removing the penalty log_N<sub>t,j</sub>_ raises the mean stopping time from 105,593 to 188,036, with 12.8% of runs reaching the cap. The appendix also includes an idealized reference that knows the true means and tracks a globally optimal allocation. This reference is not empirical Track-and-Stop and is used only to provide scale, not to rank algorithms.


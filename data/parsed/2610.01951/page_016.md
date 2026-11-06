Hence \(q\mapsto d(p,q)\) is decreasing on (0_,p_\], increasing on \[_p,_1\], and attains its unique minimum 0 at _q=p_. This proves the two displayed formulas for \(K_\mathrm{inf}^+\) and \(K_\mathrm{inf}^-\).

For the second claim, define<tbc>

\(\Psi(x):=N_iK_\mathrm{inf}^-(\mathrm{Ber}(p_i),x)+N_jK_\mathrm{inf}^+(\mathrm{Ber}(p_j),x),p_i\ge p_j.\)

<tbc>If _x\<p<sub>j</sub>_, then<tbc>

\(\Psi(x)=N_id(p_i,x)\ge N_id(p_i,p_j)=\Psi(p_j),\)

<tbc>because \(d(p_i,\cdot)\) is decreasing on (0_,p<sub>i</sub>_\]. If _x\>p<sub>i</sub>_, then<tbc>

\(\Psi(x)=N_jd(p_j,x)\ge N_jd(p_j,p_i)=\Psi(p_i),\)

<tbc>because \(d(p_j,\cdot)\) is increasing on \[_p<sub>j</sub>,_1\]. Therefore the infimum is attained on \[_p<sub>j</sub>,p<sub>i</sub>_\], where both one-sided terms are active and

\(\Psi(x)=N_id(p_i,x)+N_jd(p_j,x).\)

This proves the identity.

_Remark_ B.2. Whenever \(\widehat{\mu}_{t,i}\ge\widehat{\mu}_{t,j}\),<tbc>

\(W_t^\mathrm{gen}(i,j)=\mathrm{inf}_{x\in(0,1)}\left\{N_{t,i}d(\widehat{\mu}_{t,i},x)+N_{t,j}d(\widehat{\mu}_{t,j},x)\right\}=V_t(i,j).\)

<tbc>Moreover, the minimizer in \(x\mapsto N_id(p_i,x)+N_jd(p_j,x)\) is the pooled mean

\(x^\star=\frac{N_ip_i+N_jp_j}{N_i+N_j}.\)

Thus, for ordered Bernoulli pairs, the one-sided transportation cost is exactly the pairwise Bernoulli GLR for testing whether the two arms can share a common mean.

## B.2 Uniform error control

**Theorem B.3** (Uniform error control for the Bernoulli EB-TCI stopping rule)**.** _With the threshold_<tbc>

\(c(t,\delta)=\mathrm{log}(1/\delta)+2\mathrm{log}(1+t/2)+2+\mathrm{log}(K-1),\)

<tbc>_Algorithm 1, with or without the optional exploration guard, satisfies_<tbc>

\(\mathbb{P}_\mu\left(\tau_\delta<\infty,\widehat{i}_{\tau_\delta}\neq i^\star\right)\le\delta.\)

<tbc>_Proof of Theorem B.3._ Bernoulli distributions are supported on \[0,1\]. The stopping rule in Algorithm 1 is exactly the bounded-reward transportation-cost stopping rule of Jourdan et al. \[9, Lemma 2\], specialized to Bernoulli arms and to the recommendation

\(\widehat{i}_t\in\mathrm{arg}\mathrm{max}_{i\in[K]}\widehat{\mu}_{t,i}.\)

That lemma states that, for any adaptive sampling rule and for the threshold displayed above, the probability that the stopping rule stops and recommends an arm different from the unique best arm is at most \(\delta\).

The optional guard only changes the predictable sampling rule. It does not change the statistic \(W_t(\widehat{i}_t,j)\), the threshold, or the recommendation rule. Therefore the same time-uniform martingale error guarantee applies to both the guarded and unguarded versions of the algorithm, and the claimed inequality follows.

Theorem B.3 supplies the error-control half of \(\delta\)-correctness. It does not imply \(\mathbb{P}_\mu(\tau_\delta<\infty)=1\) for an arbitrary sampling rule. Almost-sure termination follows under the regimes of Corollary 6.3, Theorem 6.4, Corollary 6.5, and Theorem 6.7; combining termination with the displayed error bound gives \(\delta\)-correctness in those regimes.


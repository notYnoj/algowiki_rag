## G.3 Finite-mean sufficient exploration

_Proof of Theorem 6.4._ It is enough to construct a summable upper-quantile bound for a _U_- stabilization time _t<sub>U</sub>_, since the expectation bound then follows from Theorem 5.2.

Let<tbc>

\(q_\mathrm{se}(\xi):=\mathrm{inf}\{x\ge 0:\mathbb{P}_\mu(T_\mathrm{se}\le x)\ge 1-\xi\},\xi\in(0,1],\)

<tbc>be the upper-tail quantile of _T_<sub>se</sub>. By Lemma F.5,<tbc>

\(\sum_{k\ge 0}2^{-k}q_\mathrm{se}(2^{-k})<\infty.\)

<tbc>For \(\xi\in(0,1/2]\), set<tbc>

\(R_\xi:=\mathrm{log}\frac{K}{\xi}+\mathrm{loglog}\frac{e}{\xi}+1.\)

<tbc>Lemma E.5 gives \(n_\star(\xi)\le A_\mu R_\xi\). For \(\eta\in(0,1/4]\), define<tbc>

\(L_\mathrm{se}(\eta):=q_\mathrm{se}(\eta/3)+\left[\frac{K}{c_\mathrm{se}^2}n_\star(\eta/3)^2\right]+1.\)

<tbc>On the event \(\{T_\mathrm{se}\le q_\mathrm{se}(\eta/3)\}\), every \(t\ge L_\mathrm{se}(\eta)\) satisfies \(t\ge T_\mathrm{se}\) and<tbc>

\(\mathrm{min}_iN_{t,i}\ge c_\mathrm{se}\sqrt{t/K}\ge n_\star(\eta/3).\)

<tbc>Hence \(t_\mathrm{sep}(\eta/3)\le L_\mathrm{se}(\eta)\). Intersecting this event with the armwise confidence event \(\mathcal{K}_{\eta/3}\), Proposition 6.1 implies<tbc>

\(B_{t+1}=i^\star\forall t\ge L_\mathrm{se}(\eta).\)

<tbc>Now also intersect with the event \(\mathcal{A}_{\eta/3}\) of Proposition F.1. Since the rule is unguarded, the guard term in Lemma F.2 is absent, and the lemma gives entry into the stabilized regime time satisfying

\(t_U\le u_U(\eta):=C_{\beta,U}\left(L_\mathrm{se}(\eta)+\mathrm{log}\frac{e(L_\mathrm{se}(\eta)+1)^2}{\eta/3}\right).\)

The three events used above have total probability at least \(1-\eta\). Thus _u<sub>U</sub>_ is a upper-quantile bound on (0,1/4]; extend it to (0,1] by setting \(u_U(\eta)=u_U(1/4)\) for \(\eta>1/4\).

It remains to check dyadic summability. Since \(n_\star(\eta)\le A_\mu R_\eta\),<tbc>

\(L_\mathrm{se}(\eta)\le q_\mathrm{se}(\eta/3)+C_{\mu,c_\mathrm{se},K}R_{\eta/3}^2.\)

<tbc>Along \(\eta_k=2^{-k}\), monotonicity of _q_<sub>se</sub> gives \(q_\mathrm{se}(2^{-k}/3)\le q_\mathrm{se}(2^{-k-2})\), and therefore<tbc>

\(\sum_{k\ge 0}2^{-k}q_\mathrm{se}(2^{-k}/3)<\infty.\)

<tbc>The dyadic sums of \(R_{2^{-k}/3}^2\) and log(_e/_2<sup>-_k_</sup>) are finite. Finally,<tbc>

\(\mathrm{log}\frac{e(L_\mathrm{se}(\eta)+1)^2}{\eta/3}\le C\left(L_\mathrm{se}(\eta)+\mathrm{log}(e/\eta)+1\right),\)

<tbc>using \(\mathrm{log}(1+x)\le x\). Hence

\(\sum_{k\ge 0}2^{-k}u_U(2^{-k})<\infty.\)

The expectation part of Theorem 5.2 now yields the displayed bound.

## G.4 All-distinct means instances

_Proof of Corollary 6.5._ For all-distinct Bernoulli instances, the bounded-reward theorem of Jourdan et al. \[9\], specialized to the EB leader and TCI challenger under their tie-breaking convention, proves the sufficient-exploration property used in their asymptotic \(\beta\)-optimality argument. In the Bernoulli/SPEF instantiation covered by their generic top-two analysis, this gives an almost sure finite random time _T_<sub>se</sub> with \(\mathbb{E}_\mu[T_\mathrm{se}]<\infty\) such that

\(\mathrm{min}_{i\in[K]}N_{t,i}\ge\sqrt{t/K}\forall t\ge T_\mathrm{se}.\)

Thus Theorem 6.4 applies with _c_<sub>se</sub>=1 to that tie-breaking variant. This corollary does not extend the cited sufficient-exploration result to the fixed deterministic tie-breaking convention used in Algorithm 1.


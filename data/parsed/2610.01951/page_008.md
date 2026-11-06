**Corollary 6.3** (Non-asymptotic high-probability bound for the unguarded algorithm)**.** _Fix a compact interval_ \(U\Subset(0,1)\) _containing_ \(\beta\) _in its interior. Under the standing unique-best-arm assumption, the unguarded algorithm admits instance-dependent constants_ \(A_{\mu,\beta,U},B_{\mu,\beta,U},D_{\mu,\beta,U}>0\) _such that for every_ \(\delta\in(0,1/2]\) _and_ \(\eta\in(0,1/4]\),

\(\mathbb{P}_\mu\big(\tau_\delta\le T_\beta^\star(\mu)log(1/\delta)+A_{\mu,\beta,U}\sqrt{log(1/\delta)\left(log(K/\eta)+loglog(e/\delta)\right)}\)<br>
\(+B_{\mu,\beta,U}\left(log(K/\eta)+loglog(e/\delta)\right)+D_{\mu,\beta,U}\eta^{-a_\mu}\left(log(e/\eta)\right)^{b_\mu}\big)\ge 1-4\eta.\)

The last term is polynomial in \(1/\eta\). This is sufficient for a valid non-asymptotic high-probability bound, but its tail is too heavy to integrate into the leading-order expected stopping-time result.

**Theorem 6.4** (Expected stopping time under finite-mean sufficient exploration)**.** _Consider the unguarded algorithm and fix a compact interval_ \(U\Subset(0,1)\) _containing_ \(\beta\) _in its interior. Assume_ finite-mean sufficient exploration_: there exist a constant c_<sub>se</sub>_\>_0 _and an almost-surely finite random time T_<sub>se</sub> _with_ \(\mathbb{E}_\mu[T_\mathrm{se}]<\infty\) _such that_<tbc>

\(\mathrm{min}_{i\in[K]}N_{t,i}\ge c_\mathrm{se}\sqrt{t/K}\forall t\ge T_\mathrm{se}.\)

<tbc>_Then there exists a U-stabilization time t<sub>U</sub> that admits a summable upper-quantile bound. Consequently, there are instance-dependent constants_ \(C_{\mu,1},C_{\mu,2},C_{\mu,3}<\infty\) _such that, for all_ \(\delta\in(0,1/2]\),<tbc>

\(\mathbb{E}_\mu[\tau_\delta]\le T_\beta^\star(\mu)log(1/\delta)+C_{\mu,1}\sqrt{log(1/\delta)loglog(e/\delta)}+C_{\mu,2}loglog(e/\delta)+C_{\mu,3}.\)

<tbc>**Corollary 6.5** (Expected bound for pairwise-distinct means)**.** _Assume that all arm means are pairwise distinct. Consider the unguarded Bernoulli_ \(\beta\)_-EB-TCI variant with the same empirical-best leader and transportation-cost challenger indices as Algorithm 1, but with a tie-breaking convention covered by Jourdan et al. \[9\], in particular their uniform tie-breaking convention. Then there exist instance- dependent constants_ \(C_{\mu,1},C_{\mu,2},C_{\mu,3}<\infty\) _such that, for all_ \(\delta\in(0,1/2]\),

\(\mathbb{E}_\mu[\tau_\delta]\le T_\beta^\star(\mu)log(1/\delta)+C_{\mu,1}\sqrt{log(1/\delta)loglog(e/\delta)}+C_{\mu,2}loglog(e/\delta)+C_{\mu,3}.\)

## A simple exploration guard.

When several suboptimal arms may have the same mean, a finite- mean sufficient- exploration theorem is not currently available for the unguarded deterministic- tie-breaking rule. The optional guard in Algorithm 1 removes this specific gap: whenever an arm count falls below \(\sqrt{t/K}\), it samples a least-sampled arm. This deterministic guarantee is enough to control, in expectation, the time to enter the stabilized regime for any number of arms under a unique best arm. The remaining stopping-time argument is the same as for the unguarded algorithm.

**Proposition 6.6** (Deterministic exploration rate of the guarded algorithm)**.** _Assume the exploration guard in Algorithm 1 is enabled. Then for all_ \(t\ge K\), \(\mathrm{min}_{i\in[K]}N_{t,i}\ge\left\lfloor\sqrt{t/K}\right\rfloor-1\)_. Consequently, for every_ \(\eta\in(0,1)\), \(t_\mathrm{sep}(\eta)\le K\left(n_\star(\eta)+1\right)^2\)_, and, for every compact interval_ \(U\Subset(0,1)\) _containing_ \(\beta\) _in its interior, there exists a U-stabilization time t<sub>U</sub> whose high-probability upper bound is polynomial in_ \(log(1/\eta)\).

**Remark.** On guarded rounds, the algorithm does not toss the \(\mathrm{Ber}(\beta)\) coin that normally selects between leader and challenger. Therefore the best-arm sampling fraction differs from its unguarded value by at most the guarded-pull fraction \(G_t^\mathrm{tot}/t\). Proposition F.1 in Appendix F proves the corre sponding concentration bound and shows deterministically that \(G_t^\mathrm{tot}\le\sqrt{K}t+K\).

**Theorem 6.7** (Expected stopping time of the guarded algorithm)**.** _Assume the exploration guard in Algorithm 1 is enabled and let_ \(\mu\) _be any Bernoulli instance with a unique best arm. Then there exist instance-dependent constants_ \(C_{\mu,1},C_{\mu,2},C_{\mu,3}>0\) _such that, for all_ \(\delta\in(0,1/2]\),

\(\mathbb{E}_\mu[\tau_\delta]\le T_\beta^\star(\mu)log(1/\delta)+C_{\mu,1}\sqrt{log(1/\delta)loglog(e/\delta)}+C_{\mu,2}loglog(e/\delta)+C_{\mu,3}.\)

## The expected bound for the unguarded algorithm remains unresolved.

The guard works because it gives a deterministic lower bound on every arm count. For the unguarded deterministic-tie- breaking rule, the analogous expected bound would require finite-mean control of the time to enter<tbc>


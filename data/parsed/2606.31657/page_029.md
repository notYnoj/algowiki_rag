**Corollary 6.3** (Seed-averaged cumulative influence)**.** _Under the hypotheses of Theorem 6.2, every randomized algorithm A that is one-sided_ \((1-\eta)\)_-approximate for Max E3SAT satisfies_<tbc>

\(\mathrm{SCInf}(A)=\mathbb{E}_R\big[\sum_{v=1}^n\mathrm{Inf}(f_{v,R})\big]=\Omega(nk).\)

<tbc>_Moreover, for the single-clause paths from Theorem 6.2,_<tbc>

\(\sum_{v=1}^n\sum_{i=1}^k\sum_{t=1}^L\mathbf{Pr}_{m,R}\big[A(\Psi_{t-1}^{m,i};R)_v\neq A(\Psi_t^{m,i};R)_v\big]=\Omega(nk).\)

<tbc>_Proof._ For the endpoint statement, couple the two output distributions _A(x(m_)) and \(A(x(m^{\oplus i}))\) by using the same random seed _R_ on both inputs. This is a valid coupling, so<tbc>

\(\mathrm{EMD}_{d_\mathrm{H}}\big(A(x(m)),A(x(m^{\oplus i}))\big)\le\mathbb{E}_R\big[d_\mathrm{H}\big(F_R(m),F_R(m^{\oplus i})\big)\big].\)

<tbc>Averaging over _m_ and _i_ gives<tbc>

\(\mathbb{E}_{m,i}\big[\mathrm{EMD}_{d_\mathrm{H}}\big(A(x(m)),A(x(m^{\oplus i}))\big)\big]\le\mathbb{E}_{m,i,R}\big[d_\mathrm{H}\big(F_R(m),F_R(m^{\oplus i})\big)\big].\)

<tbc>Expanding Hamming distance coordinatewise and then unfolding the definition of total influence,<tbc>

\(\mathbb{E}_{m,i,R}\big[d_\mathrm{H}\big(F_R(m),F_R(m^{\oplus i})\big)\big]=\frac{1}{k}\mathbb{E}_R\big[\sum_{v=1}^n\mathrm{Inf}(f_{v,R})\big].\)

<tbc>Applying item 1 of Theorem 6.2 yields

\(\frac{1}{k}\mathbb{E}_R\big[\sum_{v=1}^n\mathrm{Inf}(f_{v,R})\big]=\Omega(n),\)

which is equivalent to the displayed lower bound.

The path version is identical: for each _m,i,t_,

\(\mathrm{EMD}_{d_\mathrm{H}}\big(A(\Psi_{t-1}^{m,i}),A(\Psi_t^{m,i})\big)\le\mathbb{E}_R\big[d_\mathrm{H}\big(A(\Psi_{t-1}^{m,i};R),A(\Psi_t^{m,i};R)\big)\big],\)

and summing over _t_, averaging over _m_ and _i_, and expanding coordinatewise proves the second claim.

**Corollary 6.4** (Many highly influential output coordinates on average over the seed)**.** _There exist constants_ \(\alpha,\gamma>0\) _such that_<tbc>

\(\mathbb{E}_R\big[\big|\{v\in[n]:\mathrm{Inf}(f_{v,R})\ge\alpha k\}\big|\big]\ge\gamma n.\)

<tbc>_In particular, for at least one choice of the internal randomness r, at least_ \(\gamma n\) _output coordinates satisfy_

\(\mathrm{Inf}(f_{v,r})\ge\alpha k.\)

_Hence on at least one seed slice, linearly many output coordinates depend on_ \(\Omega(k)\) _message coordinates and have deterministic decision-tree depth_ \(\Omega(k)\).


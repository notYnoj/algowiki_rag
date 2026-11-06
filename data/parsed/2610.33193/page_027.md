\(\ge-\mathrm{log}(Q(0)\mathrm{ln}2)\)<br>
\(\ge\mathrm{log}\left(\frac{2^{n+t}}{c(n+t+1+\mathrm{log}e)\mathrm{ln}2}\right)\)<br>
\(=n+t-\mathrm{log}\left(c(n+t+1+\mathrm{log}e)\mathrm{ln}(2)\right)\)<br>
\(=\alpha cn+n-\mathrm{log}\left(c((\alpha c+1)n+1+\mathrm{log}e)\mathrm{ln}(2)\right)\)<br>
\(>\alpha cn-2\mathrm{log}(5\alpha cn)\text{since}\alpha,c,n\ge 1\) (3)

But if \(\phi\) were satisfiable then we must have that:

\(\mathrm{Pr}_\mathcal{D}[1]Q(1)\le\mathbb{E}_{x\sim\mathcal{D}}[Q(x)]\le c\mathrm{H}_2(\mathrm{Pr}_\mathcal{D}[1])\le c\mathrm{Pr}_\mathcal{D}[1]\mathrm{log}(e/\mathrm{Pr}_\mathcal{D}[1])\)

Which implies:

\(Q(1)\le c\mathrm{log}(e/\mathrm{Pr}_\mathcal{D}[1])\)<br>
\(=c(\mathrm{log}(e)-\mathrm{log}(\mathrm{Pr}_\mathcal{D}[1]))\)<br>
\(\le c\left(\mathrm{log}(e)-\mathrm{log}\left(\frac{1+2^t}{2^{n+t+1}}\right)\right)\)<br>
\(=c\left(n+t+1+\mathrm{log}e-\mathrm{log}(1+2^t)\right)\)<br>
\(\le c(n+1+\mathrm{log}e)\)<br>
\(<4cn.\)

As long as \(\alpha cn\ge 18\), Eq. (3) is at least \(\alpha cn/4\). For simplicity, we will fix \(\alpha=18\) to get that _Q_(1)_\>_9_cn/_2 when \(\phi\) is unsatisfiable. But, if \(\phi\) has a single satisfying assignment then _Q_(1)_\<_4_cn_. Thus finding a valid heat function _Q_ for this erasure gate such that \(\mathbb{E}_{x\sim\mathcal{D}}[Q(x)]\le c\mathbb{E}_{x\sim\mathcal{D}}[Q^*(x)]\) tells us whether \(\phi\) has a satisfying assignment.

The NP-hardness of multiplicative approximation is unfortunate, as being able to estimate the optimal heat functions for each of _T_ gates in a circuit to multiplicative error _c_ immediately gives us a thermodynamic circuit that is within a multiplicative factor _c_ of optimal. Like all NP-hard problems, it also rules out a polynomial-time _randomized_ algorithm unless \(\mathsf{NP}\subseteq\mathsf{BPP}\).

There _is_ a polynomial-time randomized algorithm for the problem of finding optimal heat functions with _additive_ error on the expected released heat. Finding heat functions for each of the _T_ gates with additive error at most \(\varepsilon\) will give us a thermodynamic circuit where the additive error (i.e. expected excess heat dissipation) across all gates is at most \(\varepsilon T\). By setting \(\varepsilon=\varepsilon'/T\) we can obtain an additive error \(\varepsilon'\) for the full circuit that doesn’t scale with _T_. The basic idea is simple: randomly sample inputs to the circuit and use them to empirically estimate the true input distribution to the gate with add-one (or Laplace) smoothing.<sup>31</sup>

**Lemma 4.8.** _Fix any_ \(\varepsilon>0\)_. Given a circuit_ C _where all gates act on a constant number of bits and one such gate g in_ C_, let_ D _be the induced marginal distribution over the inputs to gate g when_ C _receives the uniform distribution over its inputs. Let Q_<sup>∗</sup> _be a valid heat function for g that minimizes_ E<sub>_x_∼D</sub>\[_Q_<sup>∗</sup>(_x_)\]_. There is a_ \(\mathrm{poly}(n,1/\varepsilon,1/\delta)\) _time randomized algorithm that produces a valid heat function_ \(\widehat{Q}\) _such that_ \(\mathbb{E}_{x\sim\mathcal{D}}[\widehat{Q}(x)]\le\mathbb{E}_{x\sim\mathcal{D}}[Q^*(x)]+\varepsilon\) _with probability at least_ \(1-\delta\).

<sup>31</sup>The smoothing factor gives us a straightforward way to ensure that our produced heat function \(\widehat{Q}\) never sets \(\widehat{Q}(x)=\infty\) on any input.


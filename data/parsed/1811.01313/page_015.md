If we assume \((t+n(w+lgn)/b+nw/b+1)^{t+1}\le(nw/b)^{(1/30)n}\) as in the statement of the lemma, then we get<tbc>

\(k\ge\frac{n!}{4(nw/b)^{(1/30)n}}.\)

<tbc>We have now argued that there are many permutations \(\pi\), all having many arrays _A_ corresponding to \(\pi\) with some data bit strings _d_<sub>1</sub>_,...,d<sub>n</sub>_, and where the the I/O-graph of A<sup>∗</sup> on _A_ is _G_. We will use this to conclude that for at least one of those permutations, it must be the case that \(\mathrm{dist}(\pi,i,G)\) is large for many _i_. For this, observe that the number of distinct permutations \(\pi\) for which there are less than (4/5)_n_ indices \(i\in\{1,\dots,n\}\) with \(\mathrm{dist}(\pi,i,G)\ge(1/2)\mathrm{lg}_{2m/b}(nw/b)\) is bounded by:<tbc>

\(\genfrac(){pt}{2}{n}{n/5}n^{(4/5)n}(2m/b)^{(n/5)\cdot(1/2)\mathrm{lg}_{2m/b}(nw/b)}(b/w)^{n/5}.\)

<tbc>To see this, observe that any such permutation \(\pi\) can be uniquely specified by first specifying a set _I_ of _n/_5 indices _i_ with \(\mathrm{dist}(\pi,i,G)<(1/2)\mathrm{lg}_{2m/b}(nw/b)\). There are \(\genfrac(){pt}{2}{n}{n/5}\) possible choices for _I_. Then, for all indices _i_ with \(i\notin I\), there are at most _n_ choices for \(\pi(i)\). Finally, for indices \(i\in I\) we argue as follows: Every node in _G_ has degree at most 2_m/b_ by construction. Hence any node has at most \((2m/b)^\ell\) nodes within distance \(\ell\) in the undirected version of _G_. Since \(\mathrm{dist}(\pi,i,G)<(1/2)\mathrm{lg}_{2m/b}(nw/b)\) for all \(i\in I\), it must be the case that the output node containing \(C[\pi(i)]\) can be specified as one amongst (2_m/b_)<sup>(1/2)lg<sub>2_m/b_</sub>(_nw/b_)</sup> nodes. Finally, the output node containing \(C[\pi(i)]\) represents exactly _b/w_ array entries and thus another (_b/w_) factor specifies \(\pi(i)\). Assuming _nw/b_ is at least some large constant, we can upper bound the above quantity using Stirling’s approximation:

\(\genfrac(){pt}{2}{n}{n/5}n^{(4/5)n}(2m/b)^{(n/5)\cdot((1/2)\mathrm{lg}_{2m/b}(wn/b)}(b/w)^{n/5}\le(5e)^{n/5}n^{(4/5)n}(nw/b)^{n/10}(b/w)^{n/5}=(5e)^{n/5}n^n(nw/b)^{-n/10}\le\frac{n!e^n}{\sqrt{2\pi nn}^n}(5e)^{n/5}n^n(nw/b)^{-n/10}\le\frac{n!e^n(5e)^{n/5}}{(nw/b)^{n/10}}\le\frac{n!}{(nw/b)^{n/20}}.\)

In the last inequality, we assumed \(nw/b\ge(5e)^4\) (a constant). We can safely assume this, as otherwise _nw/b=n/B=O_(1) and the lower bound we claim is trivially true (an \(\Omega(1)\) lower bound). The number \(\frac{n!}{(nw/b)^{n/20}}\) is smaller than _k_ for _nw/b_ bigger than some constant, hence there must exist a permutation \(\pi\) with

\(|\Gamma_\pi|\ge\frac{2^{nw}}{4(t+n(w+lgn)/b+nw/b+1)^{t+1}}\)

and where there are at least (4/5)_n_ indices with \(\mathrm{dist}(\pi,i,G)\ge(1/2)\mathrm{lg}_{2m/b}(nw/b)\). Letting F consist of the bit strings _d_<sub>1</sub>_,...,d<sub>n</sub>_ corresponding to the arrays \(A\in\Gamma_\pi\) completes the proof.


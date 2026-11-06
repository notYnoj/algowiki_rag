matrix multiplication algorithms for computing the full product? It would also be valuable to find simpler multiplication rules or entirely different algorithms achieving such savings. Progress on these questions may also lead to stronger algorithms for 3SUM, APSP, and other fine grained algorithmic problems.

### AI methodology.

Agentin AI coordinated a large research swarm of AI agents to explore alternative proof strategies and candidate simplifications, contributing to the development of the simplified proof presented here. The authors directed the mathematical investigation, critically evaluated the proposed arguments, and developed and refined the proof and exposition through iterative work with ChatGPT and x. This process included checking calculations, simplifying the recursive analysis, separating input-preparation costs from multiplication costs, and improving the presentation. The authors take responsibility for the final manuscript.

### Acknowledgements.

We thank Virginia Vassilevska Williams for helpful comments.

### Organization.

After brief preliminaries, Section 2 proves the selected-entry bound, and Section 3 applies it to set disjointness and derives the 3SUM and APSP consequences using known reductions.

### Preliminaries.

Throughout, \[_t_\]={1_,...,t_} and logarithms have base two. We write \(\widetilde{O}(f)\) for _O(f_) up to polylogarithmic factors. All integer inputs are polynomially bounded in the relevant size parameter, so they have logarithmic bit length. Arithmetic on such integers costs only polylogarithmic time, which is absorbed by \(\widetilde{O}\).

## 2 Selected-entry matrix multiplication

Theorem 1.1 follows from the main theorem, which gives a more precise bound on the runtime of the selected-entry matrix multiplication algorithm.

**Theorem 2.1** (Combinatorial bound)**.** _Fix an integer_ \(k\ge 81\)_. Let_ \(d^{6k}\le min\{n,m\}\) _and_ \(t=\lceil log_2d\rceil\)_. Given integer matrices_ \(X\in\mathbb{Z}^{n\times d}\) _and_ \(Y\in\mathbb{Z}^{d\times m}\) _with entries of polynomial magnitude in n+m, any_ \(w\ge 1\) _distinct specified entries of XY can be computed deterministically in time_

\(\widetilde{O}\left((n+m)d^{6k}+\sum_{s=0}^t\genfrac(){pt}{2}{t}{s}6^smin\left\{w,\frac{nm}{k^s}\right\}\right).\) (2)

The following convenient corollary simplifies the runtime in terms of a single parameter \(\theta\in[0,1]\).

**Corollary 2.2** (Density tradeoff)**.** _Under the assumptions of Theorem 2.1, the same algorithm runs in time_<tbc>

\(\widetilde{O}\left((n+m)d^{6k}+(nm)^\theta w^{1-\theta} d^{log_2(1+6/k^\theta)}\right)(0\le\theta\le 1).\) (3)

<tbc>_Proof._ Using \(min\{x,y\}\le x^{1-\theta} y^\theta\) and the binomial theorem,

\(\sum_{s=0}^t\genfrac(){pt}{2}{t}{s}6^smin\left\{w,\frac{nm}{k^s}\right\}\le(nm)^\theta w^{1-\theta}\sum_{s=0}^t\genfrac(){pt}{2}{t}{s}(6/k^\theta)^s=(nm)^\theta w^{1-\theta}(1+6/k^\theta)^t.\)

Since \(t=\lceil log_2d\rceil\), the last factor is \(O(d^{log_2(1+6/k^\theta)})\).

_Proof of Theorem 1.1._ Take \(k=\lceil 81/\tau^2\rceil\) and \(\kappa=6k\). Then \(1+6/\sqrt{k}\le 1+2\tau/3<2^\tau\), so Theorem 2.2 with \(\theta=1/2\) gives the claim.

We prove Theorem 2.1 in the remainder of this section.


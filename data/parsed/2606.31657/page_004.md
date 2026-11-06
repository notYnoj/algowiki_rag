<tbc>**Theorem 1.1.** _Let_ \(\varepsilon>0\) _and C be a linear LTC over_ F_<sub>p</sub> of block length n, relative distance_ \(\delta\)_, rate r, variable degree_ \(\theta\)_, with detection probability_ \(\kappa\)_. Then, any_ \((1-\varepsilon)\)_-approximation algorithm for_ MaxCSP(_C_) _has sensitivity at least_

\(\frac{n}{2\theta}\left(\delta\left(1-\frac{p}{p-1}\frac{\varepsilon}{r\kappa}\right)-\frac{2\varepsilon}{\kappa}\right)-\frac{1}{2\theta}.\)

_even on satisfiable instances._

We emphasize that this lower bound is information-theoretic and does not rely on any complexity assumption.

We first instantiate Theorem 1.1 using the _c_<sup>3</sup>-LTC of \[12, 38\], which enjoys constant relative distance, constant rate, a constant number of queries, and constant detection probability. The associated CSP is Max E3LIN2, whose constraints are linear equations of the form _x+y+z=b_ over F<sub>2</sub>.

**Theorem 1.2.** _There exists_ \(\varepsilon>0\) _such that every_ \((1-\varepsilon)\)_-approximation algorithm for Max E3LIN2 must have sensitivity_ \(\Omega(n)\) _even when the input instances are satisfiable._

Since the assignment length is _n_, every algorithm automatically has sensitivity at most _n_, so Theorem 1.2 matches this trivial upper bound up to the hidden constant. Equivalently, for satisfiable Max E3LIN2, even slightly stable algorithms cannot achieve a \((1-\varepsilon)\)-approximation.

Previously, the best lower bound was \(\Omega(n^\delta)\) for some \(\delta>0\), and it applied only to arbitrary (not necessarily satisfiable) instances \[15\]. This non-tight exponent comes from the PCP-based reduction: it blows an _n_-variable instance up to size about \(N:=n^{1/\delta}\), so even if the \(\Omega(n)\) sensitivity lower bound survives the reduction, expressing the result in terms of the enlarged instance size _N_ leaves only an \(\Omega(N^\delta)\) lower bound.

Via standard reductions from Max E3LIN2 to Max 3SAT and Max Cut (see, e.g., \[44\]), we can show that \((1-\varepsilon)\)-approximation algorithms for Max E3SAT must have sensitivity \(\Omega(n)\) even on satisfiable instances, and that \((1-\varepsilon)\)-approximation algorithms for Max Cut on general graphs incur sensitivity \(\Omega(n)\) as well. These results again improve upon the prior sensitivity bound of \(\Omega(n^\delta)\) \[15\].

To derive a sensitivity bound specific to Max Cut on bipartite graphs, we construct an LTC whose associated CSP is precisely Max Cut and substitute it into Theorem 1.1. The result is striking because it holds even on bipartite inputs, where a perfect cut always exists:

**Theorem 1.3.** _There exists a constant_ \(\varepsilon_0>0\) _such that for every even n and every_ \(0<\varepsilon\le\varepsilon_0/\sqrt{n}\)_, any_ \((1-\varepsilon)\)_-approximation algorithm for Max Cut on bipartite graphs on n vertices must have sensitivity_ \(\Omega(1/\varepsilon)\).

Thus even on this highly structured class, where the optimum cut is trivial, any near-optimal algorithm must make \(\Omega(1/\varepsilon)\) changes after a single edge deletion. As we mentioned, it was known that any algorithm for 2-coloring a bipartite graph requires \(\Omega(n)\) sensitivity \[45\], which matches the regime \(\varepsilon<1/n\) in Theorem 1.3. Our result generalizes this by showing an \(\Omega(1/\varepsilon)\) sensitivity bound for all \(\varepsilon\) as large as \(\Theta(1/\sqrt{n})\).

## Sensitivity Lower Bounds for Other Combinatorial Problems.

Applying the standard FGLSS reduction \[14\] together with the serial repetition to Theorem 1.2, as in \[15\], yields the following lower bound for the maximum clique problem. Here, we consider the setting that the algorithm outputs a vertex set that forms a clique, and sensitivity is measured with respect to deleting a single edge.


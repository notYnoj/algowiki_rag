Our minimization result comes from a stronger sparsification theorem, resembling those of \[KPS24; KPS25; BG25\]. The goal here is, given a CSP instance _C_, to build a small, re-weighted sub- instance (denoted \(\hat{C}\)) such that on _every assignment_ \((x_1,\dots,x_n)\in D^n\), the number of unsatisfied constraints in \(\hat{C}\) is essentially the same as the number of unsatisfied constraints in _C_. Clearly, once such a sparsifier is constructed, one can (approximately) solve Min-CSP(_R_). Importantly, we show that building and maintaining such sparsifiers can still be done in space roughly equal to the non-redundancy:

**Theorem 1.2** (Informal Theorem 6.1 and Corollary 6.2 sparsification and minimization characterization)**.** _For every fixed non-trivial relation R and every_ \(\varepsilon>0\)_, there is a deterministic one-pass algorithm that can store a_ \((1\pm\varepsilon)\) _sparsifier using_ \(O_{R,\varepsilon}(\mathsf{NRD}_n(R)\mathrm{poly}(\mathrm{log}n))\) _space. Consequently, there is a deterministic one-pass_ \((1+\varepsilon)\)_-approximation algorithm for_ Min-CSP(_R_) _using_ \(O_{R,\varepsilon}(\mathsf{NRD}_n(\mathrm{core}(R))\mathrm{poly}(\mathrm{log}n))\) _space, and every finite-factor randomized approximation requires_ \(\Omega_R(\mathsf{NRD}_n(\mathrm{core}(R)))\) _space._

Finally, for Exact-CSP, the space complexity is determined by the polynomial degree of the core<sup>2</sup>.

**Theorem 1.3** (Informal Theorem 7.1 Exact-CSP characterization)**.** _Let d be the degree of the indicator function of_ core(_R). Solving_ Exact-CSP(_R_) _in one pass on simple instances requires_ \(\Omega_R(n^d)\) _randomized space and has a deterministic O<sub>R</sub>(n<sup>d</sup>_log_n)-space algorithm._

Thus all three problems first reduce to the core. After that reduction, non-redundancy characterizes satisfiability and minimization up to polylogarithmic factors, while degree characterizes Exact-CSP up to a logarithmic factor.

## The Core

The reason that core(_R_) is central to each of these results is due to the core being the _canonical fixed-point_ of _R_ under homomorphisms. More precisely, given a finite domain _D_ and a relation \(R\subseteq D^k\), a homomorphism of _R_ to itself is a map \(h:D\rightarrow D\) such that for every tuple \((t_1,\dots,t_k)\in R\), we have that \((h(t_1),\dots,h(t_k))\in R\). Given an _R_-instance of a CSP, a homomorphism _h_ always maps a satisfying assignment to a satisfying assignment. Furthermore, in the optimization setting, applying a homomorphism to an arbitrary assignment cannot decrease the number of satisfied constraints. Therefore, in any of our streaming problems, we may apply any homomorphism we desire at no cost.

If the map _h_ is not a bijection, then _h_ maps _R_ to a smaller-domain relation _h(R_). Since the domain _D_ is finite, such a shrinking can only be done a finite number of times until a fixed point is reached-this is precisely the core of the relation. As such, for any of our streaming problems, an algorithm for core(_R_) is a natural upper bound on the problem. A corresponding lower bound follows from the fact that CSP cores have canonical gadgets that can be used to fix variables. Further<tbc>

<sup>2</sup>More formally, if _C_ is the domain of the core, we write our predicate core(_R_) as a real-valued indicator function \(f:C^k\rightarrow\mathbb{R}\), compute its Fourier decomposition, and let _d_ be degree of the highest-degree monomial with a non-zero coefficient.


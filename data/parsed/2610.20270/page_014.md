### Ambient genericity.

To pass to P_<sub>n</sub>_, remove two bad families. The tie hyperplanes {_f:f(a_)=_f(b_)}, \(a\neq b\), contain every objective with a nonunique minimizer. For each (_a,d_), the objectives with \(f-f(a)\in\mathcal{E}(a,d)\backslash\mathcal{E}_\mathrm{sc}(a,d)\) have closure dimension below 2_<sup>n</sup>_ by Theorem 6.2. This proves:

**Theorem 6.3** (Generic benign degeneracy)**.** _There exists an open dense semialgebraic set_ \(\mathcal{G}_\mathrm{gen}\subseteq\mathcal{P}_n\) _(so its complement has measure zero) such that every_ \(f\in\mathcal{G}_\mathrm{gen}\) _has a unique Boolean minimizer,_ \(d_\star(f)\le n\) _is well defined, and at every order_ \(d_\star(f)\le d\le n\) _the moment relaxation has the unique optimum_ \(b_d(x_\star)b_d(x_\star)^\top\) _and an optimal certificate of rank N<sub>d</sub>_-1_. Consequently, for every such f, every such order d, and every fixed admissible parameter choice, the conclusions of Theorems 4.3, 5.1 and 5.2 hold: the three splitting methods converge eventually linearly from every initialization._

_Proof._ Theorem G.1 constructs G<sub>gen</sub>; for \(f\in\mathcal{G}_\mathrm{gen}\) and \(d\in[d_\star(f),n]\) the hypotheses of Theorem 4.3 hold and §5 applies, for every \(\sigma>0\), since the argument of §4 gives a positive modulus for each \(\sigma\).

## 7 Conclusion

We proved that the degeneracy of exact Boolean Moment-SOS relaxations, in the quotient form of §2, is benign for first-order splitting methods, answering for that formulation the open question of \[KJY25\]. Under unique rank-one exactness and one strictly complementary certificate, the abstract rigidity theorem yields a setwise error bound around the optimal set. The three splitting methods therefore converge eventually linearly from every initialization, whichever certificate they select. Generically, the hypotheses hold at every uniquely rank-one exact order.

### Limitations.

Our guarantee concerns the algorithmic residual, not objective-function growth. It is a convergence-rate statement rather than a complexity theorem, with instance-dependent constants, no bound on the entrance time, and exact algorithms with fixed scalar parameters only. The rigidity abstract theorem removes primal uniqueness; yet the Boolean theorem cannot (Theorem 4.4). The verification is tied to the Boolean quotient through the two identities of Theorem 4.1. Redundant encodings (Figure 1(a)), sparse, symmetry-reduced, or constrained hierarchies change the quotient algebra, and the propagation can fail outside it (Theorem D.3; \[KY26a\]).

### Open problems.

First, a _quantitative_ rigidity: our constants come from compactness; we conjecture that for the Boolean class they admit explicit instance-parameter bounds, the missing step from rate separation to complexity separation. Second, _beyond the Boolean quotient_: which exact relaxations satisfy the two kernel identities of Theorem 3.2? We believe residual-field rigidity is the right abstraction for exact relaxations with degenerate optimal sets, and we hope it extends beyond the Boolean cube.


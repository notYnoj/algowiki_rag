<tbc>**Assumption 19.** If halfspace \(h(\widetilde{x})\ge 0\) is chosen in Line 16 of Algorithm 1, then there exist \(\widetilde{v},\widetilde{u}\in\underline{\mathcal{E}^+}\) such that \(h(\widetilde{v})\ge 0\) and \(h(\widetilde{u})<0\).

We have two strategy (eager and lazy) to refine the segmentation of _D_.

In eager strategy, we choose a halfspace \((h(\widetilde{x})\ge 0)\in H\) that separates two distinct points \(\widetilde{v}'_i\) and \(\widetilde{v}_{i+1}\) in the implicit cycle. In doing so, we want to reduce the number of implicit cycles in _G(S(D),_E<sup>+</sup>), but adding a new halfspace may introduce new implicit cycles if there exists \((\widetilde{v},\widetilde{v}')\in\mathcal{E}_{C,C}^+\) that crosses the new border from the side of \(\widetilde{v}'_i\) to the side of \(\widetilde{v}_{i+1}\). Therefore, we choose a hyperplane that minimizes the number of new crossing examples.

In lazy strategy, we use an SMT solver to find a hyperplane \(h(\widetilde{x})\in H\) that separates \(\widetilde{v}'_i\) and \(\widetilde{v}_{i+1}\) and minimizes the number of new crossing examples.

### Termination

Assumption 18 and Assumption 19 guarantees that every leaf in _S(D_) contains at least one point in the finite set <u>E</u><sup>+</sup>. Because the number of leaves in _S(D_) strictly increases after each iteration of Phase 2 and Phase 3, we eventually get a segmentation _S(D_) where each \(L\in S(D)\) contains only one point in <u>E</u><sup>+</sup> in the worst case. Since we have excluded Case 1 at the beginning, Theorem 17 guarantees the existence of ranking function with the segmentation _S(D_). Therefore, the algorithm terminates within |<u>E</u><sup>+</sup>| times of refinement.

**Theorem 20.** _If Assumption 18 and Assumption 19 hold, then Algorithm 1 terminates. If Algorithm 1 returns a piecewise affine lexicographic function_ \(\widetilde{f}(\widetilde{x})\)_, then the function satisfies_ \(R_\widetilde{f}(\widetilde{x},\widetilde{x}')\) _for each_ \((\widetilde{x},\widetilde{x}')\in\mathcal{E}^+\) _where_ E<sup>+</sup> _is the input of the algorithm._ \(\sqcap\sqcup\)

## 5.5 Improvement by Degenerating Negative Values

There is another way to define well-founded relation from the tuple \(\widetilde{f}(\widetilde{x})=(f_k(\widetilde{x}),\dots,f_0(\widetilde{x}))\) of functions, that is, the well-founded relation \(R'_\widetilde{f}(\widetilde{x},\widetilde{x}')\) de fined inductively by \(R'_{()}(\widetilde{x},\widetilde{x}'):=\perp\) and \(R'_{(f_k,\dots,f_0)}(\widetilde{x},\widetilde{x}'):=f_k(\widetilde{x})\ge 0\wedge f_k(\widetilde{x})>f_k(\widetilde{x}')\vee\left(f_k(\widetilde{x}')<0\vee f_k(\widetilde{x})=f_k(\widetilde{x}')\right)\wedge R'_{(f_{k-1},\dots,f_0)}(\widetilde{x},\widetilde{x}')\).

In this definition, we loosen the equality \(f_i(\widetilde{x})=f_i(\widetilde{x}')\) (where _i_=1_,...,k_) of the usual lexicographic ordering (10) to \(f_i(\widetilde{x}')<0\vee f_i(\widetilde{x})=f_i(\widetilde{x}')\). This means that once \(f_i(\widetilde{x})\) becomes negative, \(f_i(\widetilde{x})\) must stay negative but the value do not have to be the same, which is useful for the synthesizer to avoid complex candidate lexicographic ranking functions and thus improves the performance.

However, if we use this well-founded relation \(R'_\widetilde{f}(\widetilde{x},\widetilde{x}')\) instead of \(R_\widetilde{f}(\widetilde{x},\widetilde{x}')\) in (10), then Theorem 17 fails because \(R'_\widetilde{f}(\widetilde{x},\widetilde{x}')\) is not necessarily subsumed by \(R'_{\widetilde{f}+\widetilde{c}}\) where \(\widetilde{c}=(c_k,\dots,c_0)\) is a nonnegative constant (see the proof of Proposition 16 and Theorem 17). As a result, there is a chance that no implicit cycle can be found in line 14 of Algorithm 1. Therefore, when we use \(R'_\widetilde{f}(\widetilde{x},\widetilde{x}')\), we modify Algorithm 1 so that if no implicit cycle can be found in line 14, then we fall back on the former definition of \(R_\widetilde{f}(\widetilde{x},\widetilde{x}')\) and restart Algorithm 1.


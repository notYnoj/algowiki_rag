## 8 Related Work

### Subset Sum Algorithms.

The classical Horowitz-Sahni meet-in-the-middle algorithm \[HS74\] remains the standard worst-case baseline for Subset-Sum, with _O_<sup>∗</sup>(2<sup>_n/_2</sup>) runtime. A space-time refinement due to Schroeppel and Shamir achieves the same time with _O_<sup>∗</sup>(2<sup>_n/_4</sup>) space \[SS81\]. Despite extensive efforts, no _deterministic_ unconditional improvement below 2<sup>_n/_2</sup> was known in general \[BFN25, Woe08\]. Our approach departs from this tradition in two ways: (i) we analyze runtime as a function of the number of _distinct_ subset sums _U_ rather than just _n_, yielding certificate- sensitive bounds; and (ii) via Controlled Aliasing under CNF with compensatory merge, we obtain a deterministic worst-case improvement.

A recent randomized algorithm by Bringmann, Fischer, and Nakos \[BFN25\] gives the first unconditional improvement over Bellman’s dynamic programming for the target-constrained decision problem, running in \(\widetilde{O}(|S(X,t)|\cdot\sqrt{n})\) time. Their technique focuses on reachable sums up to a target _t_ via algebraic/combinatorial methods. By contrast, our algorithm deterministically enumerates the full set of unique subset sums \(\Sigma(S)\), supports canonical constructive witnesses, and adapts to instance structure. The two lines are complementary: they address different problem variants and performance measures. We also note pseudo-polynomial improvements for dense/structured instances (e.g., \[KX17, Bri17\]) that are orthogonal to our certificate-size viewpoint.

### Instance Complexity and Adaptive Algorithms.

Instance Complexity was introduced by Orponen-Ko-Schöning-Watanabe \[OKSW94\] to capture the inherent difficulty of individual instances. Although potent as a conceptual tool, IC was long viewed as non-constructive (see, e.g., \[For04\]). Our results give a constructive realization: we generate the IC certificate online with runtime scaling in the certificate size _U_, and we wrap it to satisfy the partial-correctness conventions of IC (see §4.3).

### Fine-Grained Complexity.

The fine-grained framework \[Wil18\] provides tight conditional barriers (e.g., under SETH). We add a structural dimension: such lower bounds for Subset-Sum implicitly target collision-resistant instances with near-maximal _U_. Making this dependency explicit complements work on compressibility-aware reductions \[ABHS22\]; our formulation via \(\Sigma(S)\) and collision entropy is instance-level and operational.

### Collision Structure in Combinatorics.

The role of collisions in subset sums appears in additive combinatorics and cryptanalysis. Austrin-Kaski-Koivisto-Nederlof \[AKKN15\] analyze structure under anti-concentration, while Howgrave-Graham and Joux \[HGJ10\] exploit collisions via randomized meet-in-the-middle techniques to obtain sub-2<sup>_n/_2</sup> behavior in certain regimes. Classic Littlewood-Offord-type results \[TV09\] bound collision counts via anti-concentration. Our contribution is algorithmic and instance-sensitive: we prune duplicate sums in real time and link entropy collapse directly to runtime; and, distinct from prior randomized collision tricks, our Controlled Aliasing (under CNF with compensatory merge) is a deterministic, target-independent transformation that preserves correctness while provably shrinking the explored state space.

## 9 Future Directions

### Closing Algorithmic Gaps for Subset Sum.

Two natural questions remain. First, for the randomized \(O(U\cdot n)\) algorithm, can the linear factor in _n_ be removed to obtain \(\tilde{O}(U)\) time? Second, and more fundamentally, can the deterministic \(O(U\cdot n^2)\) bound be improved to match the randomized<tbc>


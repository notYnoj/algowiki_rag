In this setting, the main computational bottleneck arises in testing whether two prefixes yield the same sum and comparing their canonicality.

### A Conditional Lower Bound.

We now formalize a mild but powerful conjecture.

_Conjecture_ 1_. In the local deduplicating enumeration model, any algorithm that emits all U distinct subset sums must take_ \(\Omega(U\cdot n)\) _time in the worst case._

This conjecture posits that the \(O(U\cdot n)\) benchmark is the best we can hope for in general, even when allowing randomization. It reflects the intuition that each solution must be "seen" at _n_ bits of resolution to decide whether to include it.

_Theorem_ 3 (Conditional Optimality of Randomized IC-SubsetSum)_. If Conjecture 1 holds, then the expected_ \(O(U\cdot n)\) _runtime of the randomized_ IC-SubsetSum _algorithm is optimal in expectation within the local deduplicating model._

### Conclusion.

To our knowledge, this is the first instance-sensitive enumeration algorithm for Subset Sum whose performance is provably tied to the certificate size _U_. Our randomized variant matches the conjectured optimal runtime of \(O(U\cdot n)\) in expectation. A key open question remains whether a deterministic algorithm can also achieve this bound, or whether the additional _O(n_) overhead for comparison--leading to an \(O(U\cdot n^2)\) runtime--is inherent for any deterministic approach in this model.

## 4.3 Constructive Link to Instance Complexity

Instance complexity, introduced by Orponen-Ko-Schöning-Watanabe \[OKSW94\], measures the minimum information needed to decide a single input instance _x_ of a decision problem.

_Definition_ 2 (IC, informal (partial correctness))_. The_ instance complexity _of_ \(x\in\{0,1\}^n\) _with respect to a language L and time bound t is the bit-length of the shortest program P<sub>x</sub> such that:_

• _P<sub>x</sub>(x_)=_L(x_) _and halts within time t(n); and_<tbc>

• _for every input y of size n, P<sub>x</sub>(y_) _either halts within t(n_) _and outputs L(y), or outputs_ \(\perp\) _(i.e., is allowed to be partially correct on non-target inputs)._

They showed that for some languages in NP, the IC of a random input can be exponentially smaller than any universal algorithm. Yet because IC is defined existentially, not constructively, it was long thought to offer no algorithmic advantage.

_Proposition_ 1 (from \[OKSW94\])_. Let_ \(L\in\mathsf{NP}\)_. Then for every polynomial-time verifier V for L, the IC of a yes-instance_ \(x\in L\) _is at most the bit-length of its shortest witness._

IC-SubsetSum realizes instance complexity in a relaxed but standard partial-correctness setting. To comply with the canonical definition above, the certificate \(\Sigma(S)\) is paired with an input-checking wrapper that first verifies whether the _input set_ matches the _specific set S_ for which the certificate was generated. If the check fails, the program returns \(\perp\); otherwise, it uses \(\Sigma(S)\) to decide membership for the provided target _t_. This preserves correctness and incurs only an additive _O_(|_S_|) term in program size. Thus, while the runtime remains governed by \(U=|\Sigma(S)|\), the size of the canonical IC program is \(O(U\cdot n+|S|)\).


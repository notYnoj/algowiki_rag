<tbc>oracles have immediate implications for matchings and \(\alpha\)-factors. (Given a function \(\alpha:V\rightarrow\mathbb{Z}^+\), an \(\alpha\)_-factor_ is a subgraph of _G_ in which every vertex _v_ has degree exactly \(\alpha(v)\). This generalizes the notion of perfect matching where \(\alpha\) is identically one.)

For degree bounds \(\alpha(v)\unknown k\), this yields an \(\alpha\)-factor existence oracle with _O_((_kn_)<sup>2</sup>log_n_) space and \(O((fk^2)^\omega)\) query time. As a special case, setting \(\alpha=1\) gives a perfect matching oracle with _O(n_<sup>2</sup>log_n_) space and \(O(f^\omega)\) query time. We complement this with an \(\Omega(n^2)\) space lower bound for perfect matching oracles for \(f\unknown 2\) updates, establishing space optimality up to logarithmic factors. The standard reduction from maximum to perfect matching further gives maximum matching size within the same bounds up to polylogarithmic factors. Handling _arbitrary_ degree bounds requires a different approach: the standard expansion is prohibitively large, and unlike maximum flow, \(\alpha\)-factors admit no natural residual graph. We develop a residual-graph analogue based on closed alternating trails in the symmetric difference of two \(\alpha\)-factors, yielding an oracle with _O_((_fn_)<sup>2</sup>log_n_) space and \(O(f^{3\omega})\) query time, independent of \(max_v\alpha(v)\).

Note that all decision oracles above achieve \(\widetilde{O}_{f,k}(n^2)\) or \(\widetilde{O}_{f,k}(n^3)\) space, work for sparse matroids, and have poly(_fk_<sup>2</sup>) query time. The dependence on _k_ arises from our generic reduction, which maps _f_ updates in the original instance to \(\Theta(fk^2)\) updates in the auxiliary matrix representation on which our framework operates. This leads to a natural question: can one eliminate the dependence on _k_ and obtain query time depending only on the number _f_ of updates?

_Can the dependence on k (and on the matroid density) be removed from the query time altogether, possibly at the cost of more but still polynomial space?_

## Removing the dependence on _k_, and Subset Sensitivity.

We answer this question affirmatively. The _k_-dependence in the general model arises because every update modifies the oracle’s internal matroid representation, and the cost of each such modification grows with _k_. Our key idea is to _decouple updates from the representation_. The price of decoupling is space, which now scales with the square of the set of elements that may ever be added or deleted, which in the worst case is _O(m_<sup>2</sup>).

Additionally, we observe that if the set of edge updates is restricted to a smaller set of size \(\sigma\), then the space of our oracle has only a quadratic dependence on \(\sigma\). We therefore introduce the _subset sensitivity model_, where, a set _E<sub>Q</sub>_ of _susceptible_ elements of size \(\sigma\), possibly including elements not initially present, is specified at preprocessing time, and all updates are restricted to _E<sub>Q</sub>_. This captures applications where changes are localized, such as a known set of vulnerable links or candidate edges, and reduces the space requirement to \(O(\sigma^2)\).

Applying this primitive throughout our reductions yields subset sensitivity oracles for (_s,t_)-max<tbc>

\begin{tabular}{cccc}
**Problem** & **Space** & **Query Time** & **Ref** \\
_k_-Disjoint Arborescences & _O_((_kn_)<sup>2</sup>log_n_) & \(O((fk^2)^\omega)\) & Thm 5.3 \\
_k_-Disjoint Spanning Trees & _O_((_kn_)<sup>2</sup>log_n_) & \(O((fk^2)^\omega)\) & Thm 5.6 \\
Colorful Spanning Tree & _O(n_<sup>2</sup>log_n_) & \(O(f^\omega)\) & Thm 5.8 \\
_k_-Forest Covering & _O_((_kn_)<sup>2</sup>log_n_) & \(O((fk)^\omega)\) & Thm 5.10 \\
\end{tabular}

Man the dependence on k (and on the matroid density) be removed from the query time altogether, possibly at the cost of more but still polynomial space?

3: Sensitivity oracles (decision version) for spanning structure problems. All results have corresponding weighted versions with additional (_Wkn_)-multiplicative factors in space and query.


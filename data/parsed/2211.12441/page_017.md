## 4.2 Decomposition of the objective function

For use in this section as well as later parts of the paper, we now explain how the objective of inversion minimization on trees decomposes. We introduce the notion of root inversion along the way, and observe the effect of adjacent-rank transpositions on the decomposition.

The objective \(\mathrm{MinInv}(T,\rho)\) can be written as the sum of contributions from each of the individual nodes. A node _v_ contributes those inversions that reside in the subtree _T<sub>v</sub>_ and go through the root _v_ of _T<sub>v</sub>_. We refer to them as the root inversions in _T<sub>v</sub>_.

**Definition 26 (root inversions,** \(\mathrm{RInv}(\cdot,\cdot,\cdot)\)**,** \(\mathrm{MinRInv}(\cdot,\cdot)\)**).** _Given a tree T, a ranking_ \(\rho\) _of the leaves of T, and an ordering_ \(\sigma\) _of T, a root inversion of_ \(\sigma\) _with respect to_ \(\rho\) _is an inversion_ \((\ell_1,\ell_2)\) _of_ \(\sigma\) _with respect to_ \(\rho\) _for which the lowest common ancestor_ \(\mathrm{LCA}(\ell_1,\ell_2)\) _is the root of T. The number of root inversions of_ \(\sigma\) _with respect to_ \(\rho\) _in T is denoted by_ \(\mathrm{RInv}(T,\rho,\sigma)\)_. The minimum number of root inversions in T with respect to_ \(\rho\) _is denoted_

\(\mathrm{MinRInv}(T,\rho)\doteq\mathrm{min}_\sigma\mathrm{RInv}(T,\rho,\sigma),\) (3)

_where_ \(\sigma\) _ranges over all possible orderings of T._

The only aspect of the ordering \(\sigma\) of _T<sub>v</sub>_ that affects \(\mathrm{RInv}(T_v,\rho,\sigma)\) is the relative order of the children of _v_. For a node _v_ with _k_ children _u_<sub>1</sub>_,...,u<sub>k</sub>_, by abusing notation and using \(\sigma\) to also denote the ranking of the children induced by the ordering of the tree, we have

\(\mathrm{RInv}(T,\rho,\sigma)\doteq\sum_{1\le i<j\le k}\mathrm{XInv}_\rho(L_{\sigma(i)},L_{\sigma(j)}),\) (4)

where _L<sub>i</sub>_ is a short-hand for the leaf set _L(T<sub>u<sub>i</sub></sub>_). The contributions of the nodes can be optimized independently:

\(\mathrm{MinInv}(T,\rho)=\sum_v\mathrm{MinRInv}(T_v,\rho),\) (5)

where _v_ ranges over all nodes of _T_ with degree deg_<sub>T</sub>(v)\>_1.

When we apply an adjacent-rank transposition \(\tau\) to a ranking \(\rho\), at most one of terms in the decomposition (5) can change, and the change is at most one unit. We capture this observation for future reference as it will be helpful in several sensitivity analyses.

**Proposition 27.** _Let_ \(\rho\) _be a ranking of the leaf set X of a tree T,_ \(\tau\) _an adjacent-rank transposition, and_ \(\ell_1\) _and_ \(\ell_2\) _be the affected leaves. Then_

\(\mathrm{MinRInv}(T_v,\rho)=\mathrm{MinRInv}(T_v,\tau\rho)\)

_for all nodes v in T except possibly_ \(v=\mathrm{LCA}(\ell_1,\ell_2)\)_. Moreover, the difference is at most 1 in absolute value._

_Proof._ Since the ranks of \(\ell_1\) and \(\ell_2\) under \(\rho\) are adjacent, for any leaf \(\ell\) other than \(\ell_1\) and \(\ell_2\), the relative order of \(\ell\) under \(\rho\) is the same with respect to \(\ell_1\) as it is with respect to \(\ell_2\). This means that the adjacent-rank transposition \(\tau\) does not affect whether a pair of leaves constitutes an inversion unless that pair equals \(\{\ell_1,\ell_2\}\). As a result, the only term on the right-hand side of (5) that can be affected by the transposition \(\tau\) is the one corresponding to the node _v_, and it can change by at most one unit.


Following the identical aggregation logic as Theorem 8, summing these charges across all _r_<sub>#</sub> runs yields \(\sum_{i=1}^{r_\#}\left(r_ilg(n/r_i)+2r_i\right)=nH+2n\). Adding the global overhead of exactly _n_-1 comparisons for the mutually exclusive skip checks yields the final bound of _nH_+3_n_-1 comparisons.

To compute the move bound, we first separate the cost of reversals from the cost of merges.

**Lemma 18** (Cost of Reversals)**.** _In total, reversing decreasing subarrays makes at most_ 1.5_n moves._

_Proof._ According to the deferral logic in Algorithm 2, a subarray is physically reversed iff a recursive call identifies it as purely decreasing (_x_<sub>2</sub>=`true`). Crucially, if the reversal logic is processed, the current execution frame inevitably returns _x_<sub>2</sub>=`false` to its parent. Consequently, each individual element can be involved in at most one reversal operation across the entire execution.

Let _m_ denote the number of elements involved in a given reversal. The cost of reversing _m_ elements is at most 1.5_m_ moves, yielding an amortized bound of 1.5 moves per element per reversal. Because every element is subject to at most one reversal, we can charge a maximal cost of 1.5 moves to each of the _n_ elements, resulting in the bound of 1.5_n_ total moves.

**Lemma 19** (Optimized Moves per Run)**.** _For a non-decreasing or decreasing run of length r, the total move charge incurred is bounded by_ 1.5_r_lg(_n/r_)+4.5_r._

_Proof._ We analyze the merge moves using the amortized accounting framework established in Section 3.2, which assigns a uniform charge of 1.5 moves to every run element participating in an active merge (plus the global overhead of (_n_-1)/2 moves). The core structural savings of the algorithm rely on bypassing the merge step for pure nodes (Case 1):

• For a non-decreasing run, Case 1 nodes successfully pass the standard non-decreasing skip check, bypassing the merge step and incurring zero moves.<tbc>

• For a strictly decreasing run, Case 1 nodes successfully pass the decreasing skip check, similarly bypassing the merge step and incurring zero moves.

Because the directional orientation of the elements within the run does not change the maximal capacity or structural boundaries of the nodes across the merging tree, the worst-case move charges apply identically in both regimes:

• At the upper levels of the tree (_h\<t_+1), the total move charge incurred by the run’s elements is bounded by 1.5_r(t_+1), consistent with the derivations in Lemma 9.<tbc>

• At the lower levels of the tree (\(h\ge t+1\)), the sizes of boundary nodes (Case 2) down the tree form a convergent geometric series bounding moves at 3(_n/_2_<sup>t</sup>_).

In total, per-run charge is 1.5_r(t_+1)+3(_n/_2_<sup>t</sup>_) moves. By applying the convexity bound established in Theorem 11, this expression is bounded by 1.5_r_log(_n/r_)+4.5_r_ total moves per run.

**Theorem 20** (Optimized Move Complexity)**.** _An array of size n containing r_<sub>#</sub> _pre-existing non- decreasing or strictly decreasing runs of lengths r_<sub>1</sub>_,r_<sub>2</sub>_,...,r_<sub>_r_<sub>#</sub></sub> _is sorted in at most_ 1.5_nH_+6.5_n moves, where the run-based entropy_ \(H=\sum_{i=1}^{r_\#}(r_i/n)lg\left(n/r_i\right)\).

_Proof._ Paralleling the derivation in Theorem 11, summing the costs in Lemma 19 yields a total merge cost of 1.5_nH_+4.5_n_ moves. To obtain the final move bounds, we must reintroduce all remaining global overheads. The ceiling overhead from copying halves to the buffer in the half- buffered merge adds at most (_n_-1)/2 moves (see Section 3.2). Furthermore, the deferred physical reversal of decreasing subarrays contributes at most 1.5_n_ moves shown in Lemma 18. Thus, the final data movement complexity is then:

\(1.5nH+4.5n+1.5n+(n-1)/2\le 1.5nH+6.5n\)


**Algorithm 5** \(\alpha\)-MergeSort’s Merge Policy (see Algorithm 1 of Algorithm 1)

1: **while** \(r_2<\alpha r_1\) or \(r_3<\alpha r_2\) **do**

2: **if** _r_<sub>3</sub>_\<r_<sub>1</sub> **then**

3: \(R_2\leftarrow\) Merge(_R_<sub>3</sub>_,R_<sub>2</sub>)

4: **else**

5: \(R_1\leftarrow\) Merge(_R_<sub>2</sub>_,R_<sub>1</sub>)

**Theorem 5.** _There exist input sequences that can be sorted in O(n_) _time using standard_ \(\alpha\)_-MergeSort that take time_ \(\Omega(n\mathrm{log}n)\) _when using_ \(\alpha\)_-MergeSort implemented with the walk-back algorithm. Therefore,_ \(\alpha\)_-MergeSort is not walkable._

_Proof._ Our proof is similar to the proof for TimSort, and in fact, when \(\alpha=2\), the identical counterexample works. Similar sequences work for other values of \(\alpha\) as well where the three original runs are of sizes \(n/\alpha,n/\alpha^2,n/\alpha^3\). Without loss of generality, we assume \(\alpha=2\) for this proof and use the same counterexample as for TimSort.

We note that, similar to TimSort, only the first while loop condition (on line 1) will ever succeed, while the check in the if statement (on line 2) will always fail, and consequently only the merge on line 5, between runs _R_<sub>3</sub> and _R_<sub>2</sub>, will ever occur. Therefore the algorithm will perform identical merges to TimSort on this input. And as with TimSort, the problematic walk-back cost occurs after a stage has collapsed, and the stack has just four runs: {_n/_2_,n/_4_,n/_8,2_<sup>i</sup>_}. On the second while loop condition, where we check if _r_<sub>3</sub>_\<_2_r_<sub>2</sub>, when implementing the walk-back algorithm, we must at least fully load _R_<sub>3</sub> to confirm that the condition is false. Therefore, the walk-back cost is at least _n/_8 (and will in-fact be 3_n/_8), and our TimSort analysis holds. \(\sqcap\sqcup\)

## C Additional Walkable Mergesort Proofs

In this appendix, we provide proofs showing that additional mergesorts are walkable.

### C.1 The Original TimSort

We showed in Section B that the modern TimSort algorithm \[1,14\] is not walkable. Surprisingly, in this section we show that the original TimSort algorithm \[21\], in which the fourth condition is removed, is walkable. Refer to Algorithm 6 for the merge policy of this algorithm. In this section, we prove the following theorem.

**Theorem 6.** _Original TimSort is walkable._

As before, we begin by analyzing the walk-back cost of successful merges.

**Lemma 11.** _When we perform a merge, the walk-back cost is paid for by at most 2 times the subsequent merge cost._


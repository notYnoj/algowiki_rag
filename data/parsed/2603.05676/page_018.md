<tbc>_Proof._ Without loss of generality, let _r_<sub>2</sub>=max{_r_<sub>1</sub>_,r_<sub>2</sub>}. Then \(\ell_2\ge\ell_1\). Since _r_<sub>3</sub>_\>_2_r_<sub>2</sub>, the following holds true.

\(\ell_3\ge\lfloor log(2r_2/c)\rfloor=\lfloor log(r_2/c)+1\rfloor=\lfloor log(r_2/c)\rfloor+1>\ell_2\)

\(\sqcap\sqcup\)

The above lemma gives us the stopping condition for the walk-back algorithm applied to _c_-Adaptive ShiversSort: if we walk back \(2\times max\{r_1,r_2\}\) steps and have not found _r_<sub>3</sub>, then we know that the merge condition in line 2 of Algorithm 3 is false. See Figure 10.

**Lemma 8.** _The walk-back cost incurred by failed merges is O(m+n)._

_Proof._ As described above, we spend \(2\times max\{r_1,r_2\}\) walking back when we fail a merge condition. Since no subsequent merge occurs, we do not immediately "pay back" the cost. For simplicity, we can upper bound this cost to at most \(2\times(r_1+r_2)\). Thus, every failed merge check incurs a walk-back cost of at most twice the length of the runs labeled _R_<sub>1</sub> and _R_<sub>2</sub>.

To complete the argument, we show that each run is labeled _R_<sub>1</sub> and _R_<sub>2</sub> for at most one merge sequence each throughout the main loop. Consider any run _q_ with label _R_<sub>1</sub> or _R_<sub>2</sub> when a failed condition occurs. Assuming the run decomposition is not empty, we push a new run onto the stack and then repeat the main loop. This relabels _q_ to _R_<sub>2</sub> or _R_<sub>3</sub>, respectively. Since _R_<sub>1</sub> and _R_<sub>2</sub> are never merged in this algorithm, it is impossible to ascend from label _R_<sub>2</sub> to _R_<sub>1</sub>. It is possible to change labels from _R_<sub>3</sub> to _R_<sub>2</sub> with a merge. Nevertheless, doing so destroys the constituent runs in the merge and replaces them with a new merged run. As a result, each run is labeled _R_<sub>1</sub> and _R_<sub>2</sub> for at most one merge sequence.

The sum of all original and intermediate runs is _m+n_. Each run _q_ contributes a walk-back cost of 2|_q_| at most twice (once as _R_<sub>1</sub> and again as _R_<sub>2</sub>). Then the total walk-back cost of failed merges is at most 4(_m+n_). \(\sqcap\sqcup\)

We have shown that the walk-back cost of successful merges and failed merges during the main loop of _c_-Adaptive ShiversSort is _O(m+n_). In combination with Lemma 1, we conclude the following.

**Theorem 3.** _c-Adaptive ShiversSort is walkable._

Upon further inspection, our proof relies on two key properties of _c_-Adaptive ShiversSort. First, we only ever merge _R_<sub>3</sub> and _R_<sub>2</sub> and never examine runs below _R_<sub>3</sub>. Second, the walk-back cost of a failed merge condition is bounded by a constant multiple of our known runs. The first property allows us to easily show that the walk-back cost of successful merges is paid for by the subsequent merge. The second is a relaxed stopping condition that allows us to bound the walk-back cost of failed merges. Indeed, with slight modification, the above proof applies to _any_ almost-_k_-aware mergesort with the following two properties:

1. Only _R<sub>k</sub>_ and _R_<sub>_k_-1</sub> are ever merged during the main loop.


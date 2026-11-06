<tbc>As a result, each run contributes at most 4 times their size (2 times their size as _R_<sub>1</sub> and 2 times their size as _R_<sub>2</sub>). This can happen for every original and intermediate run, thus the total walk-back cost of failed merges is _O(m+n_). Therefore, Original TimSort is walkable.

### C.2 The 2-MergeSort

In 2019 Buss and Knop introduced several new natural stack-based mergesorts, which they call the 2-MergeSort and the \(\alpha\)-MergeSort [4]. In Section B.1, we show that \(\alpha\)-MergeSort (not to be confused with the \(\alpha\)-StackSort introduced by Auger et al. [2]) is not walkable. Here, we show that the 2-MergeSort is. The merge policy of the 2-MergeSort is described in Algorithm 7.

**Algorithm 7** 2-MergeSort’s Merge Policy (see Algorithm 1 of Algorithm 1)

1: **while** \(|S|\ge 3\) and _r_<sub>2</sub>_\<_2_r_<sub>1</sub> **do**

2: **if** _r_<sub>3</sub>_\<r_<sub>1</sub> **then**

3: \(R_2\leftarrow\) Merge(_R_<sub>3</sub>_,R_<sub>2</sub>) \(\triangleright\) _removes R_<sub>3</sub> _from S_

4: **else**

5: \(R_1\leftarrow\) Merge(_R_<sub>2</sub>_,R_<sub>1</sub>) \(\triangleright\) _removes R_<sub>2</sub> _from S_

**Theorem 7.** _2-MergeSort is walkable._

_Proof._ As always, we begin by discussing the walk-back costs when a merge occurs. By Observation 1, we always know _r_<sub>1</sub>. If a merge occurs, then the condition _r_<sub>2</sub>_\<_2_r_<sub>1</sub> is true and we incur walk-back cost _r_<sub>2</sub> to test this. If _r_<sub>3</sub>_\<r_<sub>1</sub>, we incur additional walk-back cost _r_<sub>3</sub>. Since we merge _R_<sub>3</sub> and _R_<sub>2</sub>, the merge perfectly pays for the walk-back cost of _r_<sub>2</sub>+_r_<sub>3</sub>. The case is symmetric for if \(r_3\unknown\leftarrow r_1\).

Now we discuss the cost associated when no merge occurs. This occurs when we fail the initial comparison, so \(r_2\ge 2r_1\). Therefore, we incur walk-back cost 2_r_<sub>1</sub>. We observe that this can only happen once per unique run during the main loop. Whenever a failure occurs, we push a new run, displacing _R_<sub>1</sub> to _R_<sub>2</sub>. To return to spot one of the stack, this run will have to merge, destroying it. Thus, the total walk-back cost is _O(m+n_). \(\sqcap\sqcup\)

## D In-Place Run Partitioning

In this appendix, for the sake of completeness, we describe a simple partitioning algorithm that can be used, for example, to move all short runs in an array, _A_, to the end of _A_, which also moves the long runs to be before that end region, without destroying the long runs.

We can abstract this problem by representing each element of a long run as 0’s, and each element of a short run as 1’s. Suppose _A_ is an array of _n_ elements,


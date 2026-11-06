<tbc>algorithm, maintaining a shallow stack necessitates recomputing power values as runs rise to the top of the stack. It could be that such recomputed power values do not equal their original values, causing the behavior of a shallow PowerSort to differ from standard PowerSort. Fortunately, we show that this is not the case and power values computed on-the-fly are faithful to their original values.

**Lemma 2.** _The merge step of PowerSort (line 4 of Algorithm 2) does not change the power of the second run, nor the power of any existing run._

_Proof._ See Figure 4. A successful merge combines runs _R_<sub>2</sub> and _R_<sub>3</sub> where _p_<sub>3</sub>_\>p_<sub>2</sub>. Let \(I'_2\) denote _R_<sub>2</sub>’s power interval after the merge. Since merging only extends _I_<sub>2</sub> leftward into what was _I_<sub>3</sub> and all indices in _I_<sub>3</sub> have power \(\ge p_3>p_2\), the power of _R_<sub>2</sub> remains _p_<sub>2</sub>. Similarly, _R_<sub>4</sub>’s interval extends rightward into _I_<sub>3</sub>, gaining only indices with power \(\ge p_3\ge p_4\), so its power is unchanged. Deeper runs are unaffected.

From Lemma 2, it follows that PowerSort is almost-3-aware since we can correctly recompute all power values with only knowledge of their _current_ power intervals. Given the lengths of the top-3 runs and the position of the topmost run, we can compute power intervals in constant time. By Observation 1, we always know _r_<sub>1</sub>. It costs at most _r_<sub>2</sub>+_r_<sub>3</sub> time to recover the lengths of the runs labeled _R_<sub>2</sub> and _R_<sub>3</sub> by walking back. If the merge condition is successful, then the merge cost of _R_<sub>2</sub> and _R_<sub>3</sub> equals our walk-back cost, so the total walk-back cost in this case is at most _m_. Thus, we have shown that successful merges "pay" for their own walk-back cost. It remains to bound the walk-back cost of failed

0 1
1 2
2 2
2 3
3 3
3 3
3 3
3 R3 R2 R1 = 1 p2 = 0

Fig.3: Each index in the array is associated with a **_power_** value, where the power of an index is the depth of the corresponding tree node (depicted above it). Each run is associated with the smallest power value of any index between its midpoint and the midpoint of the next run, i.e. its **_power interval I_**. The power intervals _I_<sub>3</sub> and _I_<sub>2</sub> define powers _p_<sub>3</sub> and _p_<sub>2</sub>. They are depicted under their respective runs. _R_<sub>1</sub>, being the top run, does not yet have an assigned power.


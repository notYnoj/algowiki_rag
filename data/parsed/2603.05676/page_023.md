**Algorithm 6** Original TimSort’s Merge Policy (see Algorithm 1 of Algorithm 1)

1: **while** true **do**

2: **if** |_S|\>_3 and _r_<sub>1</sub>_\>r_<sub>3</sub> **then** \(\triangleright\) _merge condition #1_

3: \(R_2\leftarrow\) Merge(_R_<sub>3</sub>_,R_<sub>2</sub>)

4: **else if** |_S|\>_2 and \(r_1\ge r_2\) **then** \(\triangleright\) _merge condition #2_

5: \(R_1\leftarrow\) Merge(_R_<sub>2</sub>_,R_<sub>1</sub>)

6: **else if** |_S|\>_3 and \(r_1+r_2\ge r_3\) **then** \(\triangleright\) _merge condition #3_

7: \(R_1\leftarrow\) Merge(_R_<sub>2</sub>_,R_<sub>1</sub>)

8: **else**

9: **break**

_Proof._ We prove this by discussing the walk-back and merge costs of each of the three conditions. By Observation 1, we always know _r_<sub>1</sub> throughout the algorithm. For simplicity, assume that we begin each iteration of a merge sequence only knowing _r_<sub>1</sub>. To test merge condition 1, we must spend _r_<sub>2</sub> time just walking from the end of _R_<sub>1</sub> to the end of _R_<sub>2</sub> as we assume we do not know _r_<sub>2</sub>. If the condition is true, we spend an additional _r_<sub>3</sub> time walking back. As such, the resulting merge of _R_<sub>2</sub> and _R_<sub>3</sub> perfectly pays for the walk-back cost.

Now we discuss condition 2. We know that we just tested and failed condition 1. Again we spent _r_<sub>2</sub> time walking to find the end of _R_<sub>3</sub>. However, because condition 1 failed, we only spent _r_<sub>1</sub> time walking before stopping. In doing so, we have recovered _r_<sub>2</sub>. Thus, condition 2 can be determined without any additional walk-back cost. We spent _r_<sub>1</sub>+_r_<sub>2</sub> time walking back and end up merging _R_<sub>1</sub> and _R_<sub>2</sub>, so the merge again perfectly pays for the walk-back cost.

Lastly, we discuss condition 3. To test and fail conditions 1 and 2 incurs _r_<sub>1</sub>+_r_<sub>2</sub> walk-back cost. An additional _r_<sub>3</sub> work is needed to confirm that \(r_1+r_2\ge r_3\). Thus, we spend _r_<sub>1</sub>+_r_<sub>2</sub>+_r_<sub>3</sub> time in total walking back. Since the condition succeeded, we know \(r_1+r_2\ge r_3\), so the walk-back cost is upper-bounded by twice the merge cost of merging _R_<sub>1</sub> and _R_<sub>2</sub>.

Now we study the walk-back cost of failed merges.

**Observation 10.** _Failing all three merge conditions in Original TimSort incurs a walk-back cost of at most_ 2(_r_<sub>1</sub>+_r_<sub>2</sub>).

_Proof._ We once again assume that we are only aware of _r_<sub>1</sub>. As discussed before, failing on condition 1 requires _r_<sub>1</sub>+_r_<sub>2</sub> time spent walking back and failing on condition 2 incurs no walk-back cost. Finally, failing on condition 3 requires an additional _r_<sub>1</sub>+_r_<sub>2</sub> time to walk back on _R_<sub>3</sub>. \(\sqcap\sqcup\)

**Observation 11.** _Each unique run can contribute to failing all merge conditions at most once as R_<sub>1</sub> _and at most once as R_<sub>2</sub>

_Proof._ If the run was _R_<sub>1</sub>, the new run added in the next iteration pushes it to _R_<sub>2</sub>. The same run cannot move back to _R_<sub>1</sub> without merging first. Likewise, if the run was _R_<sub>2</sub>, the new run pushes it to _R_<sub>3</sub>. It cannot move back to either _R_<sub>2</sub> or _R_<sub>1</sub> without merging. \(\sqcap\sqcup\)


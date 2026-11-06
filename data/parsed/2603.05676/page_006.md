<tbc>call (2) our **_stopping condition_**. It varies by algorithm. If we meet our stopping condition, we forget any information about how far we walked and retry from the beginning the next time we invoke the walk-back algorithm.

In the remainder of this section, we prove that two instance-optimal algorithms, PowerSort and _c_-Adaptive ShiversSort, are walkable. In combination with an in-place merge algorithm, this produces the first in-place instance- optimal mergesort algorithm.

Let us denote runs from the initial run decomposition R as **_original runs_**, and those obtained as the result of merges as **_intermediate runs_**. Let _m_ be the sum of the sizes of all intermediate runs; the sum of the sizes of all original runs is _n_ by definition. For any stack-based mergesort algorithm S, its runtime \(T_\mathcal{S}(n)\ge m+n\). This is because, for all intermediate runs _i_, we must have spent |_i_| time to merge the two runs that became _i_. In addition, any sorting algorithm must spend _n_ time just to read the input. If we can show that the walk-back algorithm applied to S adds no more than _O(m+n_) time over any input sequence, then we have shown that S is walkable.

**Observation 1.** _The length of the topmost run, r_<sub>1</sub>_, is always known without need of walking back during the execution of any stack-based mergesort,_ S.

\begin{tabular}{ccccc}
**Algorithm** & **Shannon-Optimal** & **Walkable** & **Jumpable** & **Shallow** \\
PowerSort \[20\] & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) \\
_c_-Adaptive ShiversSort \[17\] & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) \\
TimSort \[1,21\] & \(\checkmark\) & \<|unk|\> & \(\checkmark\) & \(\checkmark\) \\
\(\alpha\)-StackSort \[4\] & \<|unk|\> & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) \\
2-MergeSort \[4\] & \<|unk|\> & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) \\
\(\alpha\)-MergeSort (\(\varphi<\alpha<2\)) \[4,13\] & \(\checkmark\) & \<|unk|\> & \(\checkmark\) & \(\checkmark\) \\
ShiversSort \[4\] & \<|unk|\> & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) \\
\end{tabular}

r3
R2
R1
r2
r1

Fig.2: The walk-back algorithm applied to an almost-3-aware mergesort. We currently know the lengths of the runs labeled _R_<sub>1</sub> and _R_<sub>2</sub>. There may be _O_(log_n_) runs to the left of _R_<sub>2</sub> in the array (our "stack" of runs), but we do not maintain any information about them. Whenever we need to know the length of _R_<sub>3</sub>, we start walking backwards from the start of _R_<sub>2</sub>. Surprisingly, this strategy only increases runtime by a constant factor in several stack-based mergesorts.

1: A summary of our results applied to selected stack-based mergesorts.


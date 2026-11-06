<tbc>**Lemma 1.** _The collapse phase of any stack-based mergesort_ S _can be implemented in-place using the walk-back algorithm with only a constant-factor increase in runtime._

The proof follows from the fact that the cost of walking back to recover the last two runs is proportional to the cost to merge them. Because of the above lemma, we only consider the main loop of each stack-based mergesort for the remainder of this work.

### 3.2 PowerSort is Walkable

In this section, we show that PowerSort, an instance-optimal stack-based mergesort, is walkable by seeing how the walk-back cost is ‘paid for’ by the cost already spent on merges. In particular, we will analyze the walk-back cost of successful merges, determine a stopping condition, and use this stopping condition to compute the walk-back cost of failed merges.

Munro and Wild’s PowerSort \[20\] assigns every run a **_power_** value, computed jointly with the run who sits above it on the stack. These power values are used to determine whether the second and third runs on the stack should be merged. To understand how runs are assigned powers, imagine superimposing a perfect binary tree on top of the input array, where each index in the array is associated with a binary tree node.<sup>4</sup> Each index in the array is associated with a power value, where the power of an index is the depth of the corresponding tree node. The center index has a power 0, the first and third quartiles have a power 1, and so on down to \(\lfloor logn\rfloor\). Each run is associated with the smallest power value of any index between its midpoint and the midpoint of the next run, which we refer to as the runs **_power interval_** _I_. See Figure 3 for an example of how power values appear and how to compute them. Note that \[20\] define power slightly differently, and in general those power values are one greater than ours. The resulting algorithm is the same, however. We provide a simplified sketch of PowerSort’s merge policy in Algorithm 2.

One barrier to applying the walk-back algorithm is that Munro and Wild’s original algorithm does not recompute power values when merges occur. Since as many as \(\Omega(logn)\) power values may be stored at a time in the original PowerSort

**Algorithm 2** PowerSort’s Merge Policy (see Algorithm 1 of Algorithm 1)

1: **if** |_S|\>_1 **then**

2: \(p_2\leftarrow\mathsf{NodePower}(R_2,R_1)\triangleright p_3\) _already known_

3: **while** |_S|\>_2 and _p_<sub>3</sub>_\>p_<sub>2</sub> **do**

4: \(R_2\leftarrow\mathsf{Merge}(R_3,R_2)\)

5: \(p_3\leftarrow\mathsf{NodePower}(R_3,R_2)\)

6: \(p_3\leftarrow p_2\)

<sup>4</sup> We assume for simplicity that the input is of size _n_=2_<sup>a</sup>_-1 for some _a_, although the result holds for general _n_.


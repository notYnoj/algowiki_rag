**Algorithm 1** Simplified structure of the counting sort of Kolonias et al. \[5\]

**Require:** Input array _A_\[0_..n_-1\] and range size _R_

**Ensure:** Sorted array _B_\[0_..n_-1\]

1: \(H[0..R-1]\leftarrow\) histogram of _A_

2: \(P[0]\leftarrow 0\)

3: \(P[1..R]\leftarrow\) prefix sums of _H_

4: **for all** \(v\in[0,R)\) **in parallel do**

5: **for** \(p\in[P[v],P[v+1])\) **do**

6: \(B[p]\leftarrow v\)

7: **end for**

8: **end for**

9: **return** _B_

Algorithm 1 is directly related to our method in that it generates the output array as one interval per value. If the writing of output intervals is parallelized over values, however, the amount of work assigned to each value becomes imbalanced when occurrence counts vary substantially. Kolonias et al. explain that, under a uniform distribution, the average number of iterations is approximately _N/k_, whereas if 50% of the input has the same value, the computation assigned to that value must perform _N/_2 writes \[5\]. Our implementation retains the idea of output intervals for individual values, but assigns parallelism to output positions and determines the value of each output position from a local CDF loaded into shared memory. The goal is to avoid the extreme workload imbalance that can arise when one processing unit is assigned to each value.

One practical baseline in this study is CUB `DeviceRadixSort` (hereafter CUB) \[4\]. CUB allows the bit range used for sorting to be specified by `begin\_bit` and `end\_bit`. Because the normalized range size _R_ is known, we provide CUB with the relevant bit range and invoke it with `begin\_bit`= 0 and `end\_bit`= \(\lceil log_2R\rceil\). This is a more appropriate baseline for our problem than always processing all 32 bits. CUB is, however, a general-purpose implementation that provides stable sorting, a stronger functionality than the unstable integer sorting considered here. The comparison with CUB therefore evaluates how effective an implementation specialized to our more restricted problem can be relative to a practical general-purpose GPU sorter.

## 2.2 H-P Sort, RefHP, and Localizing CDFs

H-P sort is an integer-sorting algorithm based on histograms and prefix sums \[6, 7\]. Kozakai et al. position H-P sort and its extensions as counting-sort-based methods, and we likewise treat H-P sort as one implementation family of counting-sort-based integer sorting. H-P sort is not merely a direct GPU translation of ordinary counting sort; its distinctive feature is that it reconstructs output values from CDF boundary information. Let _H_<sub>1</sub> be the histogram of the input array and _P_<sub>1</sub> its prefix-sum array. Because _P_<sub>1</sub>\[_v_\] is the number of elements no greater than _v_, _P_<sub>1</sub> can be regarded as a CDF that gives the right endpoint of the output interval for each value. H-P sort constructs another histogram of _P_<sub>1</sub> and<tbc>


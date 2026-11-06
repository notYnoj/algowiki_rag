<tbc>of state _i_ are unready. We say this state and all its descendants are **_blocked_** by the sentinel in this case. Therefore, a state is **ready** if there is no sentinel on any of its ancestors (inclusive).

**Step 3** For each ready state, use its DP value to relax the tentative DP values of its descendants. Usually, we need to do so _implicitly_ to achieve efficient work. We discuss more details later.

**Step 4** Mark all ready states as finalized. Clear all the sentinels.

**Step 5** If there still exist tentative states, go to **Step 2** and repeat.

We will first prove that the algorithm is correct, i.e., it computes correct DP values for all states. Later we will show some motivating examples to help understand this algorithm in Sec. 3.

Theorem 2.1. _The Cordon Algorithm is correct._

_Proof._ This is equivalent to show that, when we find a ready state and later mark it finalized, its DP value must be finalized.

We will show this inductively. At the beginning, the ready states are those with zero in-degree in the DAG, and their true DP values are specified by the boundary cases. Clearly, their DP values cannot be relaxed by other states and they will be identified as ready in our algorithm. Their DP values are also computed by the boundary in **Step 1**. Therefore, our algorithm is correct in the first round.

Assume the algorithm is correct up to round _r_. We will show that round _r_+1 also correctly finds the ready states and their DP values. Assume to the contrary that a state _i_ identified in **Step 2** does not have its true DP value yet. This means that the best decision of _i_ has not relaxed _i_ to the finalized value. Let _j=best_\[_i_\]. Note that _j_ cannot be finalized: if so, before _j_ is marked as finalized in **Step 4**, in **Step 3** it must have relaxed _i_.

Therefore, _j_ is tentative. In this case, let _j_<sub>0</sub>=_i_, and state _j<sub>x</sub>_ be the best decision of state _j_<sub>_x_-1</sub> for \(x\ge 1\), i.e., we chase the chain of best decisions and get a list of states _i=j_<sub>0</sub>_,j_<sub>1</sub>=_best_\[_j_<sub>0</sub>\], etc. Let us find the first _x_ such that _D_\[_j<sub>x</sub>_\] is not the true DP value but _D_\[_j_<sub>_x_+1</sub>\] is the true DP value. We then prove that state _j_<sub>_x_+1</sub> must be a tentative state. If we consider _j<sub>y</sub>_ as the first finalized state on this chain, then _j_<sub>_y_-1</sub> is a tentative state, and also must already have its true DP value (because _j<sub>y</sub>_ has relaxed it in **Step 3**). Note that since state _j_<sub>_y_-1</sub> is a tentative state, all states between _j_<sub>0</sub> and _j_<sub>_y_-1</sub> must be tentative. Since _j_<sub>_y_-1</sub> has its true DP value, and _i=j_<sub>0</sub> does not have its true DP value, the first switch point _j<sub>x</sub>_ must be between _j_<sub>0</sub> and _j_<sub>_y_-1</sub>, and must also be a tentative state.

Therefore, state _j_<sub>_x_+1</sub> is a tentative state that can relax state _j<sub>x</sub>_, so it will put a sentinel on state _j<sub>x</sub>_. As a descendant of _j<sub>x</sub>_, state _i_ must be blocked by _j<sub>x</sub>_, and cannot be identified as a ready state. This leads to a contradiction. Therefore, if a state _i_ is identified as ready in our algorithm, its DP value must have been finalized. □

The Cordon Algorithm tells which states/vertices should be in the frontier in each round, but the algorithm does not show how to do so _efficiently_. Especially in **Step 3**, it is almost infeasible to use the finalized DP values to explicitly update all other states. In this case, we have to develop new parallel data structures to facilitate this step. Next, we first use LIS and LCS as two examples to illustrate our framework. We then apply it to more involved cases that use decision monotonicity in Sec. 4 and 5.

## 3 MOTIVATING EXAMPLES ON LIS/LCS

To help the audience understand the more complicated algorithms using DM in the following sections, we first provide two simple examples on Cordon Algorithm, especially on how to compute the cordon efficiently.

**_Longest Increasing Subsequence (LIS)._** We first use LIS as an example. Given an input sequence _A<sub>i</sub>_, LIS computes the maximum of _D_\[_i_\] such that:

\(D[i]=max\{1,max_{j<i,A_j<A_i}D[j]+1\}\) (2)

We use _n_ as the input size and _k_ as the output LIS length. Directly computing this recurrence takes _O(n_<sup>2</sup>) work. Sequentially, we can process all states one by one, and compute max<sub>_j\<i,A<sub>j</sub>\<A<sub>i</sub>_</sub>_D_\[_j_\] using a binary search structure, giving _O(n_log_k_) total cost \[65\]. The binary search precisely finds the best decision of each state, and only _n_ transitions are processed. Many parallel LIS solutions have also been proposed \[24, 47, 67, 68, 81\]. We will show that solving LIS using our Cordon Algorithm framework will essentially give an existing algorithm \[47\] and is a perfect parallelization of the sequential _O(n_log_k_) algorithm.

Based on Cordon Algorithm, the boundary case is to set all tentative DP values as 1. Then we will attempt to use the current tentative DP values for relaxation. In this case, for a state _i_, as long as there is any other state _j\<i_ with _A<sub>j</sub>\<A<sub>i</sub>_, _D_\[_i_\] can be relaxed to a better value 2. Therefore, all ready states are those input objects that are _prefix-min_ elements in the sequence, i.e., _A<sub>i</sub>_ is the smallest value among all _A_<sub>1_..i_</sub>. We can set these states as ready, update all other states and repeat. Note that since all unfinalized states have the same tentative DP value of 2, we _do not need to explicitly update_ the values in _D_\[_i_\], but can just maintain a global variable as the current tentative DP value. By the same idea, the ready states in the next round would be the prefix-min elements in the input after removing the finalized states. The same observation (repeatedly finding prefix-min elements) is exactly the core idea of the algorithm in \[47\]. In their algorithm, they further use a tournament tree to identify prefix-min elements efficiently and achieve efficient _O(n_log_k_) work, and _O(k_log_n_) span. Note that _k_ is exactly the perfect depth of the DP DAG, which is the longest dependency between best decisions.

Theorem 3.1. _Combining with a tournament tree, Cordon Algorithm leads to a perfect parallelization of sequential O(n_log_k_) _LIS algorithm in \[47\], where n is the input size, and k is the LIS length._

**_Longest Common Subsequence (LCS)._** LIS has a close relationship with other important problems such as LCS. Here we will revisit our cordon-based LIS algorithm from the view of LCS, which also leads to a new parallel LCS algorithm. Given two sequences _A_\[1_..n_\] and _B_\[1_..m_\] (\(m\le n\)), LCS aims to find a common subsequence _C_ of _A_ and _B_ such that _C_ has the longest length among all common subsequences. An LIS problem can be reduced to an LCS problem by first relabeling all input elements by 1_..n_ based on their total order, and then finding the LCS between this new sequence and a sequence \(B=\langle 1,2,\dots,n\rangle\). See Fig. 2(a)-(c) for an illustration. LCS has been extensively studied both sequentially \[7, 40, 51, 56, 65\] and in parallel \[6, 11, 26, 34, 76, 87, 94\]. The standard DP solution defines each state _D_\[_i,j_\] as the LCS for _A_\[1_..i_\] and _B_\[1_..j_\], and<tbc>


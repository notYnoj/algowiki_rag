### 3.1 Complexity analysis

Just like a normal _Mergesort_ routine, this new _in-place_ merging requires O(log_n_) recursion steps. Within each such recursion step, it calls the _co-ranking_ functionality once. As explained in Section 2.2, this _co-ranking_ executes O(log_n_) comparisons. Additionally, merging rotates the middle array, which--despite requiring O(_n_) time to move elements--does no element comparisons whatsoever. In total, this leads to the following recursion formula for the number of comparisons in our _in-place_ merging:

\(T(0)=1\)<br> \(T(n)=\mathcal{O}(logn)+2\cdot T(\frac{n}{2})\) (2)

The popular _master theorem_, which is typically used to solve such recurrence relations, does not cover this specific case. It can, however, be solved using the more general _Akra-Bazzi_ method [1]: Matching our equation (2) to their \(u_n=g(n)+\sum_{i=1}^ka_iu_{\lfloor\frac{n}{b_i}\rfloor}\) in (1) yields _g(n_)=O(log_n_), _k_=2, _a<sub>i</sub>_=1, _b<sub>i</sub>_=2 with _u_<sub>0</sub>=1. Determining the value of _p_ such that \(\sum_{i=1}^ka_ib_i^{-p}=1\) leads to _p_=1. Plugging this _p_-value into the _Akra-Bazzi_ equation reveals the solution \(T(n)\in\mathcal{O}(n)\). Essentially, this means that this new _in-place_ merging routine is still using only a linear number of comparisons, just like the usual non-_in-place_ variant, and as such, it remains comparison-optimal.

\(\blacktriangleright\) **Note**. The current C++ standard already defines a _std::inplace\_merge_ function within its algorithm library. Concerning complexity, it states: "_Exactly N-1 comparisons ...if enough additional memory is available,_ O(_N_log(_N_)) _comparisons otherwise._" With our new _in-place merge_ algorithm, this can now always be improved to O(_N_) comparisons.

This new _in-place Merge_ can be used directly for the general top-down _Mergesort_ approach by replacing the `Merge` call in Algorithm 3 with `Merge\_inplace`. The linear number of comparisons for the _in-place Merge_ in conjunction with the usual O(log_n_) recursion levels of _Mergesort_ leads to the better-known recurrence \(T(n)=\mathcal{O}(n)+2\cdot T(\frac{n}{2})\), which can be solved using the _master theorem_, resulting in O(_n_log_n_). As such, the traditional, non-_in- place Mergesort_ and this new _in-place Mergesort_ asymptotically utilize the same number of comparisons.

Regarding the running time, we also need to take into account the array rotations, i.e., the movement of elements. Considering this, the new _in-place Merge_ itself does a work of O(_n_log_n_). On that account, the total running time of _in-place Mergesort_ consequently becomes O(_n_log<sup>2</sup>_n_).

It should be noted that the idea of using rotations for an _in-place Merge_ is not new. Some of the algorithms mentioned in the related work make use of it. However, finding the rotation offset was previously done utilizing only a linear search, leading to O(_n_log_n_) comparisons for the _Merge_ step and consequently O(_n_log<sup>2</sup>_n_) comparisons for the resulting _Mergesort_. Replacing such a linear search with the _co-ranking_ search improves these numbers by a factor of O(log_n_) comparisons, eventually leading to our comparison-optimal solution.

Both prerequisites work with O(1) additional space and the usual recursion necessitates only an additional O(log_n_) space for the stack. For this reason, the new merging routine can be classified as _in-place_, albeit not _strictly in-place_, according to Definition 2.

## 4 Performance evaluation

We have implemented the presented _in-place Mergesort_ algorithm in plain ANSI-C. Our implementation supports arbitrary comparators using a generic comparison function, just like


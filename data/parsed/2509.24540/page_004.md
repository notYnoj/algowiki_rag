sorting algorithm. Despite these optimizations and even when keeping the restrictions on the input data, just lowering the cache size results in a much slower implementation than what we will present in this paper.

This paper proposes a _Mergesort_ that works _in place_ while keeping all the good features, namely O(_n_log_n_) comparisons with small hidden constants, and still being stable as well as comprehensible. As such, we conclude the open question from Katajainen et al. positively and demonstrate our _Mergesort_ to be practical in contrast to Chen’s and Axtmann’s observations.

## 2 Prerequisites

Our novel _in-place Mergesort_ will be presented in Section 3. This variant utilizes just two prerequisites that are introduced in this section. These already exist and can thus simply be used as "black box" functionality. For convenience, we provide pseudocodes for both of them. As such, it is not necessary for the understanding of the actual algorithm to also fully comprehend how these two components operate. Nonetheless, the more interested reader is encouraged to additionally explore their respective details as well as the cited publications given in the next subsections. Naturally, future and practical improvements or optimizations in any of these prerequisites will directly lead to a better _in-place Mergesort_.

### 2.1 Optimal array rotation

First, we need a function to rotate a given array with _n_ elements by an arbitrary offset. A rotation in this context means that elements that fall out on one side of the array are placed back into the other side of the array. Since the contemplated _Mergesort_ algorithm should work _in place_, this array rotation consequently needs to work _in place_ as well, ideally with O(1) additional memory. Moreover, this rotation should also remain time-optimal, meaning it should run in O(_n_) time, which is apparently also the lower bound.

### 2.1.1 Insufficient approaches

If we allowed a temporary array to keep a copy of all elements, such a rotation would become trivial and run in optimal time O(_n_). This temporary array would then require an additional space of O(_n_), which would clearly not be _in place_, as desired.

On the other hand, if we were to rotate all elements only by one position and repeat this _r_ times, where _r_ is the rotation offset, it could be done _in place_ but would need O(_r_) repetitions. Since this arbitrary offset can always be mapped between \(0\le r<n\) using _r_mod_n_, this would lead to O(_n_) rotations and, overall, to an inefficient O(_n_<sup>2</sup>) running time.

### 2.1.2 Time- and space-optimal rotation

Instead of moving all array elements only by one position, we could move them directly by _r_ positions. More formally, starting at position _s_, this would move all elements at positions

\(s+k\cdot r(modn)\forall k\in Z.\) (1)

**Case 1:** Whenever _r_ and _n_ are coprime, i.e., their greatest common divisor (short _gcd_) is 1, this would rotate all elements in a single cycle with a cycle length of _n_. **Example:** If a given array contains 12 elements that should be rotated by an offset of 5, then there is just a single cycle, written in cycle notation as (0 5 10 3 8 1 6 11 4 9 2 7).


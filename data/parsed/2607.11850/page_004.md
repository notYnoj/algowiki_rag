<tbc>additional bytes. Therefore, excluding recursion-stack overhead and small temporary vectors of bucket offsets, the total auxiliary memory is

\(180270\cdot sizeof(T)+12506\cdot sizeof(int).\)

For example, when sorting double values and assuming 4-byte integers, this is approximately 1.42 MiB of auxiliary memory.

Note that all of the above values were chosen using simple heuristics and may be subject to further optimization.

The memory usage of the small temporary vectors of bucket offsets is analyzed in Section 4.2.

#### 3.2.7 Floating-Point Arithmetic and Index Clamping.

For floating- point inputs, bucket indices are computed using finite-precision arithmetic. Small rounding errors may occur near bucket boundaries, especially when values lie very close to the boundary between two adjacent buckets.

The important property for correctness is that bucket regions remain ordered by value. In exact arithmetic, this follows directly from the classification formula: within a recursive call, every element is transformed using the same affine map with positive scale. Thus, if _x\<y_, then the classification value of _x_ is no larger than the classification value of _y_.

For finite floating-point inputs and non-degenerate intervals, the corresponding computation is monotone in normal use. Rounding may affect which side of a bucket boundary an element falls on, but it does not normally make bucket regions appear in the wrong order. In other words, floating-point error may slightly perturb boundary cases, but it should not cause smaller values to be placed after larger values at the bucket level.

To guard against numerical errors that could produce an index just outside the valid range, the implementation clamps each computed bucket index before using it to access bucket-related arrays. In exact arithmetic, every value in the interval [_min, max_] maps to an index between 0 and _bucket\_count_-1. The clamping step is therefore only an implementation safeguard against finite-precision arithmetic and does not change the intended bucket assignment under exact arithmetic.

## 4 Theoretical Analysis

This section analyzes the theoretical behavior of NFS Sort. We first show that the fallback mechanism guarantees a worst-case running time of O(_n_log_n_). We then analyze the auxiliary space usage and show that, because the implementation uses fixed-size helper arrays together with recursive bucket-offset vectors, the total auxiliary space is O(log_n_).

We also discuss the expected recursion depth under reasonably balanced input distributions. In such cases, the recursive bucket refinement rapidly reduces subproblem sizes, causing the algorithm to behave close to linearly in practice. Finally, we examine adversarial inputs for the algorithm.

### 4.1 Worst-Case Time Complexity

We now prove that NFS Sort has worst-case running time O(_n_log_n_).

The proof relies on the following implementation conditions, all of which are satisfied by the algorithm described above.

First, every scatter step on a subarray of size _m_ runs in O(_m_) time. This holds because the number of buckets used by the implementation is bounded by a fixed constant in the large-array cases and is at most _m_ in the small-array case.

Second, the scatter step partitions the current subarray into contiguous bucket regions ordered by their value intervals. Thus, if bucket _i_ precedes bucket _j_, with _i\<j_, then every element assigned to bucket _i_ is less than or equal to every element assigned to bucket _j_. Consequently, after scattering, no inversion crosses bucket boundaries; any remaining disorder is internal to individual buckets.

Third, recursive calls are made only on buckets larger than a fixed cleanup bound _S_. Buckets of size at most _S_ may be left for the final insertion-sort cleanup. The constant _S_ is independent of the input size _n_.

Finally, the fallback sorter has worst-case running time O(_m_log_m_) on a subarray of size _m_.

Inputs containing NaN or infinities are outside the scope of the theorem.

Lemma 4.1. _NFS Sort has worst-case running time_ O(_n_log_n_).

Proof. Consider a recursive call on a subarray of size _m_. Let _k_ be the number of buckets used by the call. All non-recursive work performed by the call, including homogeneity checks, bucket initialization, classification, prefix-sum computation, scattering, and bookkeeping, consists of a constant number of linear passes over the subarray together with O(_k_) bucket-related work. Therefore the cost of one recursive call, excluding recursive calls made on its children, is<tbc>

\(\mathcal{O}(m+k).\)

<tbc>Since the implementation ensures _k=_O(_m_), this cost is<tbc>

\(\mathcal{O}(m+k)=\mathcal{O}(m).\)

<tbc>After scattering, the subarray is partitioned into buckets of sizes<tbc>

\(m_1,m_2,\dots,m_k,\)

<tbc>with

\(\sum_{i=1}^km_i=m.\)

Buckets of size at most _S_ are not processed recursively and are left for the final cleanup phase. Buckets larger than _S_ are either processed recursively or sorted by the fallback sorter.

Let \(\alpha\) be the fixed constant used to detect insufficient progress, where \(0<\alpha<1\). A recursive child of size _m<sub>i</sub>_ is called pathological if<tbc>

\(m_i>\alpha m.\)

<tbc>Otherwise it is non-pathological, and its size satisfies

\(m_i\le\alpha m.\)

Therefore, every non-pathological recursive step reduces the subproblem size by at least a fixed constant factor.

The algorithm permits at most a fixed number _c_ of consecutive pathological recursive steps along any recursion branch. If more than _c_ consecutive pathological steps would occur, the current bucket is sorted using the fallback sorter instead of being processed recursively.


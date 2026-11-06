<tbc>It follows that along any root-to-leaf recursion path, recursive calls can be grouped into phases. Each phase consists of at most _c_ consecutive pathological calls, followed either by fallback termination or by one non-pathological call. Hence each phase has constant length, since _c_ is a fixed implementation constant.

Every phase that does not terminate by fallback contains a non- pathological call. At that point, the size of the continuing recursive subproblem is at most an \(\alpha\) fraction of the size at the beginning of the phase. Thus, after each non-terminating phase, the subproblem size decreases by a fixed constant factor. Such a decrease can occur only O(log_n_) times before the subproblem size falls below the fixed cleanup bound _S_. Since each phase has bounded length, the total number of recursive scatter levels on any root-to-leaf path is O(log_n_).

Now consider all scatter work at a fixed recursion depth. At that depth, the active subarrays are disjoint, because every scatter step partitions its parent subarray into disjoint bucket regions. Hence the sum of the sizes of all active subarrays at any fixed depth is at most _n_. Since the non-recursive cost of a call is linear in the size of its subarray, the total non-recursive work at any one depth is O(_n_).

There are only O(log_n_) recursive depths, so the total non-recursive work over all recursive calls is<tbc>

\(\mathcal{O}(nlogn).\)

<tbc>It remains to bound the total cost of fallback sorting. Suppose the fallback sorter is applied to subarrays of sizes<tbc>

\(q_1,q_2,\dots,q_r.\)

<tbc>These fallback subarrays are pairwise disjoint: each one is a bucket in the recursive partition tree, and once a bucket is fallback-sorted, recursion does not continue inside it. Therefore,<tbc>

\(\sum_{j=1}^rq_j\le n.\)

<tbc>By assumption, fallback sorting a subarray of size _q<sub>j</sub>_ costs O(_q<sub>j</sub>_log_q<sub>j</sub>_). Hence the total fallback cost is<tbc>

\(\sum_{j=1}^r\mathcal{O}(q_jlogq_j).\)

<tbc>Since \(q_j\le n\) for every _j_,<tbc>

\(\sum_{j=1}^rq_jlogq_j\le\sum_{j=1}^rq_jlogn=\left(\sum_{j=1}^rq_j\right)logn\le nlogn.\)

<tbc>Thus the total fallback cost is<tbc>

\(\mathcal{O}(nlogn).\)

<tbc>Finally, after recursive distribution and fallback sorting terminate, NFS Sort performs a global insertion-sort cleanup pass. By construction, every region that remains potentially unordered has size at most the fixed constant _S_. Furthermore, scatter steps place bucket regions in sorted value-interval order, so no inversion crosses the boundary between two final regions. Therefore all remaining inversions are internal to these final regions. For any final unordered region _B_,

\(\left(\begin{array}{ c }
|B| \\
2
\end{array}\right)\le\frac{S|B|}{2},\)

because \(|B|\le S\). Since the final regions are disjoint, the total number of remaining inversions _I_ satisfies

\(I\le\sum_B\genfrac(){pt}{2}{|B|}{2}\le\sum_B\frac{S|B|}{2}=\frac{S}{2}\sum_B|B|\le\frac{Sn}{2}=\mathcal{O}(n).\)

Insertion sort runs in O(_n+I_) time on an array with _I_ inversions [2, 5]. Since _I=_O(_n_), the final cleanup phase runs in O(_n_) time.

Combining the non-recursive work over all recursive calls, fallback work, and cleanup work gives

\(\mathcal{O}(nlogn)+\mathcal{O}(nlogn)+\mathcal{O}(n)=\mathcal{O}(nlogn).\)

Therefore, NFS Sort has worst-case running time O(_nlogn_). □

## 4.2 Space Complexity

Most of the auxiliary storage used by NFS Sort is allocated once in the top-level procedure and reused throughout the recursion. This includes the helper array, fragment buffers, temporary fragment storage, bucket-size arrays, fragment-size arrays, and offset arrays used by the scatter procedures. Since the maximum number of buckets and the fragment size are fixed implementation constants, this part of the auxiliary memory usage is constant with respect to the input size _n_.

The only additional auxiliary storage that grows with recursion comes from the temporary bucket-offset vectors created inside recursive calls. Each call to the recursive core procedure stores a vector of bucket offsets returned by the scatter step. If the call uses _k_ buckets, then this vector contains _k_+1 offsets in the usual case. During the first scatter step, two additional overflow buckets may be used to handle elements below and above the approximate initial bounds, so the first call may store _k_+3 offsets. Since the implementation uses at most 6500 buckets, the number of offsets stored by any single recursive call is bounded by a fixed constant.

Although many recursive calls may occur over the whole execution, their bucket-offset vectors are not all live at the same time. At any moment, the only live vectors are those belonging to recursive calls on the current call stack. Once a recursive call returns, its local bucket-offset vector is destroyed before control continues to other branches of the recursion tree.

Therefore, the memory used by bucket-offset vectors is proportional to the maximum recursion depth. As shown in the worst-case time analysis, the fallback mechanism prevents arbitrarily long chains of insufficiently shrinking recursive calls. Along any root-to- leaf path, after at most a fixed number of pathological steps, either the current bucket is sorted by the fallback sorter or the subproblem size decreases by a fixed constant factor. Hence the maximum recursion depth is O(log_n_).

Since each recursive level stores only a constant-size bucket- offset vector, the total live memory used by bucket-offset vectors is

\(\mathcal{O}(logn).\)

More concretely, if _K_<sub>max</sub>=6500 is the maximum number of buckets, then each non-initial recursive call stores at most _K_<sub>max</sub>+1 integer offsets, and the initial call stores at most _K_<sub>max</sub>+3 integer offsets. Thus, if the maximum recursion depth is _D_, the live storage used by bucket-offset vectors is bounded by

\((K_\mathrm{max}+3)D\cdot\text{sizeof}(\text{int}),\)


Flashsort [8] augmented with modern memory-management techniques inspired by IPS<sup>4</sup>o [1].

## 3.1 Naive NFS Sort

Appendix A gives code-style pseudocode for the naive version of NFS Sort.

We assume an array of numeric elements stored contiguously in memory. The algorithm begins by computing the minimum and maximum values of the input array, which requires _O(n_) time. These values, together with the array boundaries, are then passed to the recursive core procedure.

At each recursive step, the algorithm chooses a number of buckets based on the size of the current subarray. Our implementation uses a naive piecewise heuristic and never uses more than 6500 buckets. The algorithm then performs a _scatter step_, which distributes the elements of the subarray into buckets.

First, the global value range [_min,max_] is divided into equally sized buckets, determined by<tbc>

\(interval\text{\_}size=\frac{max-min}{bucket\text{\_}count-1}.\)

<tbc>Each element _x_ is then assigned to a bucket according to its relative position in the range [_min,max_]. Specifically, the bucket index is computed as<tbc>

\(b(x)=\left\lfloor\frac{(x-min)(bucket\text{\_}count-1)}{max-min}\right\rfloor.\)

<tbc>Equivalently, if<tbc>

\(inverse\text{\_}interval=\frac{1}{max-min},\)

<tbc>then the classification rule can be written as

\(b(x)=\lfloor(x-min)(bucket\text{\_}count-1)\cdot inverse\text{\_}interval\rfloor.\)

This mapping sends _min_ to the first bucket and _max_ to the last bucket.<sup>1</sup> Values between _min_ and _max_ are assigned proportionally, so that the bucket boundaries are evenly spaced across the full value range.

Elements are rearranged such that all elements assigned to the same bucket occupy a contiguous region of the array, while the buckets themselves appear in sorted order with respect to their value ranges. This distribution step, which we refer to as the scatter step, runs in linear time in the size of the current subarray.

Intuitively, this operation partitions the input according to value ranges, thereby decomposing the problem into smaller independent subproblems that can be processed recursively.

During the scatter step, the algorithm additionally records the number of elements assigned to each interval. The subsequent processing of a bucket depends on its size. Buckets containing at most a small threshold number of elements are left unchanged and handled later by a final cleanup phase. Larger buckets are processed recursively.

Importantly, recursion does not recompute the minimum and maximum values of a bucket. Instead, analytical bounds are propagated. Since the original value range is divided into equally sized<tbc>

<tbc>intervals, the corresponding interval boundaries directly provide valid lower and upper bounds for each recursive call. These analytically derived bounds avoid additional linear scans while preserving correctness.

The propagated bounds are interval boundaries, not necessarily the actual minimum and maximum values contained in the bucket. A bucket may contain elements that occupy only part of its assigned interval, but all of its elements lie within the bounds passed to the recursive call.

Extremely skewed distributions must nevertheless be considered. If a large fraction of the elements is assigned to a single bucket (for instance, in distributions containing a large amount of extremely small values), the recursive reduction may fail to sufficiently decrease the problem size. To address this, the algorithm employs a fallback mechanism. If a recursive branch repeatedly produces a bucket containing more than \(\alpha\) fraction of its parent subarray, the algorithm allows for only a small fixed number of such consecutive failures before falling back to a comparison-based sort on that bucket.

Assuming the fallback sorter has worst-case _O(m_log_m_) time on a bucket of size _m_, this mechanism prevents indefinitely unbalanced recursion and yields an overall worst-case bound of _O(n_log_n_), as shown in Section 4.

After the recursive phase terminates, the algorithm performs insertion sort on the entire array. At this point, all remaining unsorted regions are buckets whose sizes are bounded by a fixed threshold, and the buckets themselves are already ordered by value range. Therefore, all remaining inversions are confined within constants- size regions. For a fixed threshold, the total number of remaining inversions is _O(n_), so the final insertion-sort pass runs in _O(n_) time.

The naive version described here deliberately omits several engineering details and edge-case refinements in order to emphasize the main recursive bucketing structure. These refinements, including degenerate ranges, helper arrays, and the scatter step, are introduced in the following subsections.

## 3.2 Implementation Details and Refinements

This section describes several implementation details and refinements that improve the practical performance of the algorithm.

### 3.2.1 Data Types.

NFS Sort is implemented for arithmetic numeric types, including standard integral and floating-point types. The current implementation assumes finite inputs and does not define behaviour for special floating-point values such as NaN, +inf, or -inf.

### 3.2.2 Fast Paths.

NFS Sort includes fast paths for already sorted and reverse-sorted inputs. When the top-level sorting procedure is called, the implementation first performs quick-fail checks to determine whether the array is already in increasing or decreasing order. If the array is already sorted, the algorithm returns it immediately as-is. If the array is reverse sorted, the array is reversed and then returned.

If neither fast path applies, then the input is neither sorted nor reverse sorted. For finite numeric inputs, this also implies that the array does not consist entirely of equal elements. Hence, the<tbc>

<sup>1</sup>With this particular choice of scaling by _bucket\_count_-1, the last bucket contains only values equal to _max_, assuming exact arithmetic. This convention is intentional and simplifies the handling of the maximum element.


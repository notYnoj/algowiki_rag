<tbc>minimum and maximum values are distinct, and the algorithm can proceed.

## 3.2.3 Approximating the Minimum and Maximum.

One optimization used by NFS Sort is to approximate the minimum and maximum values before entering the recursive procedure. Instead of performing a full linear scan over the input solely to determine these values, the implementation estimates them by sampling elements from the array.

If the approximate minimum and maximum are equal, the sampled bounds are discarded and the true minimum and maximum are computed by a full scan. This prevents the initial call from receiving a degenerate value range.

The approximated bounds are then passed to the first recursive call. Since these bounds may not contain all input values, the initial scatter step uses two additional buckets: one for elements below the approximated minimum and one for elements above the approximated maximum. During this step, the algorithm also computes the true minimum and maximum. Whenever an element is placed into the underflow bucket, it is compared against the current minimum; similarly, elements placed into the overflow bucket are compared against the current maximum.

Thus, after the first scatter step, the true minimum and maximum are known. These exact bounds are then propagated to lower levels of recursion, so the overflow and underflow buckets are needed only in the initial distribution step.

## 3.2.4 Handling Homogeneous Subarrays.

At the beginning of each recursive call after the initial one, the algorithm performs a quick- fail check whether the current subarray is homogeneous, meaning that all of its elements are equal. If so, the subarray is already sorted and the recursive call returns immediately.

This case occurs naturally on inputs with few distinct values. After several distribution steps, many buckets may contain repeated copies of a single value. The homogeneity check detects such buckets early and avoids unnecessary bucket construction, scattering, and further recursion.

## 3.2.5 Scatter Step.

For large subarrays, NFS Sort uses a fragment- based scatter procedure inspired by IPS<sup>4</sup>o [1]. Instead of immediately writing each element to its final bucket region, the algorithm first classifies elements into buckets and stores them in small fixed- size buffers, called fragments. Each bucket has its own fragment buffer. When a fragment becomes full, it is flushed back into the input array as a contiguous block.

During this pass, the algorithm also counts the number of elements assigned to each bucket. These counts are then prefix- summed to compute the final bucket boundaries. Since full fragments were written sequentially during the first pass, they are not necessarily located inside their final bucket regions. A second phase therefore defragments the array by moving or swapping whole fragments into their correct bucket intervals. Any elements that do not fill a complete fragment are kept temporarily in the helper buffer and copied into the remaining gaps at the end.

This approach is similar in spirit to IPS<sup>4</sup>o [1]: both algorithms classify elements into buckets, buffer writes in small blocks, and move data in cache-friendly fragments rather than as individual elements. This is done to reduce scattered memory writes and<tbc>

<tbc>improve locality during distribution. However, the version used in NFS Sort is simpler and sequential. It uses the fragment scatter only as the distribution step inside the recursive algorithm, rather than as part of a fully in-place parallel sorting framework.

For smaller subarrays, NFS Sort uses a simpler scatter procedure. The algorithm first classifies each element into a bucket and counts the resulting bucket sizes. These counts are then converted into prefix sums, which determine the contiguous output region assigned to each bucket.

After the bucket boundaries have been computed, the algorithm performs a second linear pass over the subarray. Each element is classified again and written to its corresponding position in a helper array using the bucket offsets as write pointers. Finally, the helper array is copied back into the original subarray.

This naive scatter step performs more direct element-wise writes than the fragment-based version, but it has lower overhead and is therefore preferable on small inputs. The implementation also records whether enough sufficiently large buckets remain to justify further recursive processing; otherwise, the subarray is left for the final cleanup phase. <sup>2</sup>

## 3.2.6 Auxiliary Storage.

The auxiliary storage described in this subsection consists of the fixed work arrays allocated by the top- level procedure. The additional temporary bucket-offset vectors created during recursion are discussed separately in Section 4.2.

NFS Sort allocates a fixed set of auxiliary arrays once in the top-level procedure and reuses them throughout all recursive calls. This avoids repeated allocation inside the recursion and keeps the additional memory usage predictable.

The implementation maintains an array of bucket sizes, used by both scatter procedures to count how many elements are assigned to each bucket. For the fragment-based scatter, it also maintains an array of fragment sizes, which records how many elements are currently stored in each per-bucket fragment buffer. In addition, the fragment-based scatter uses a helper buffer containing one fixed- size fragment for each bucket, two integer arrays for bucket end offsets and current bucket write offsets, and a temporary fragment buffer used when swapping fragments.

For small subarrays, the naive scatter reuses the helper buffer as a temporary output array: elements are written into the helper array according to their bucket offsets and then copied back to the original subarray. In both scatter variants, the auxiliary arrays are temporary workspaces only; the final sorted output remains in the original input array.

With fragment size set to 90, the implementation allocates a fragment helper array of size \(2002\cdot 90\) elements and a temporary fragment of size 90. Thus, the auxiliary storage for elements of type _T_ is<tbc>

\((2002\cdot 90+90)\cdot sizeof(T)=180270\cdot sizeof(T).\)

<tbc>The implementation also allocates four integer work arrays: one array of 6500 bucket sizes and three arrays of 2002 offsets. This contributes<tbc>

\((6500+2002+2002+2002)\cdot sizeof(int)=12506\cdot sizeof(int)\)

<sup>2</sup>All buckets left for the final cleanup phase are always bounded in size by the fixed threshold _S_.


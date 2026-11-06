value order, this prefix sum equals the total number of occurrences of values from 0 through _b<sub>t</sub>_-1. The lemma follows.

**Lemma 3** (Output interval of each value)**.** _Value b<sub>t</sub>+x occupies the interval_

\([O[t]+C_t[x-1],O[t]+C_t[x])\)

_in the output array. These intervals are mutually disjoint and ordered by value, and the interval for b<sub>t</sub>+x has length c_<sub>_b<sub>t</sub>+x_</sub>.

_Proof._ By Lemma 1, the number of values within tile _t_ that are smaller than _b<sub>t</sub>+x_ is _C<sub>t</sub>_\[_x_-1\], and the number no greater than _b<sub>t</sub>+x_ is _C<sub>t</sub>_\[_x_\]. By Lemma 2, _O_\[_t_\] is the number of elements whose values are smaller than the range handled by tile _t_. Thus, in the complete output array, the number of values smaller than _b<sub>t</sub>+x_ is _O_\[_t_\]+_C<sub>t</sub>_\[_x_-1\], and the number no greater than _b<sub>t</sub>+x_ is _O_\[_t_\]+_C<sub>t</sub>_\[_x_\]. The claimed interval follows. Its length is _C<sub>t</sub>_\[_x_\]-_C<sub>t</sub>_\[_x_-1\]=_c_<sub>_b<sub>t</sub>+x_</sub>, and the monotonicity of the CDF together with the construction of tile offsets implies that the intervals for distinct values occur consecutively in value order.

**Theorem 1** (Correctness of the output array)**.** _After output generation, B contains the elements of A in nondecreasing order._

_Proof._ For each within-tile position _p_, output generation finds the smallest _x_ satisfying \(C_t[x]\ge p+1\). This operation selects the unique _x_ such that \(p\in[C_t[x-1],C_t[x])\). Therefore, exactly _c_<sub>_b<sub>t</sub>+x_</sub> output positions in the interval for value _b<sub>t</sub>+x_ given by Lemma 3 are filled with _b<sub>t</sub>+x_. The intervals for all values are mutually disjoint, and their total length is \(\sum_{v=0}^{R-1}c_v=n\), so the entire output array is filled exactly once. Because the intervals are arranged in value order, the output array is in nondecreasing order. The theorem follows.

We next summarize the computational complexity. GPU execution time depends strongly on memory bandwidth, atomic contention, occupancy, and the number of kernel launches, and therefore cannot be characterized adequately by a single parallel-time complexity as in a PRAM model. We instead describe the total work and workspace of the algorithm, and evaluate actual performance experimentally in Section 4.

Let \(m=\lceil R/T\rceil\) be the number of tiles. During histogram construction, every input element is read for every tile to test whether it belongs to that tile, yielding _O(mn_) work. The number of actual additions to shared-memory histograms over all tiles is nevertheless _O(n_), because each input element belongs to exactly one tile. Merging the shared-memory histogram of each thread block into global memory requires work proportional to the tile width and the number of blocks. The total work of the within-tile prefix sums is _O(R_) because each bin is processed a constant number of times over all tiles. Constructing tile offsets takes _O(m_) work. Output generation performs a binary search in a local CDF for every output position and therefore makes _O(n_log_T_) comparisons. The simplified total work is thus<tbc>

\(O(mn+nlogT+R).\)


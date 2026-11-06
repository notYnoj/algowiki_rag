### 2 Base-_n_ Radix Sort (BNRS)

BNRS algorithm is obtained from Radix sort \[2\] when the base is fixed to _n_ where _n_ is the size of the input. The algorithm in each round, extracts values using \(\lfloor A[i]/n^r\rfloor(modn)\), where _A_ is an array of input values with index _i_ and _r_ is the round number leading to total number of rounds to be \(\lfloor log_nk\rfloor+1\), where _k_ is the maximum element of _A_. The motive behind having _n_ as the base is based on the fundamental understanding of the Big _O_ notation which theoretically ignores the constant multiples and makes the calculation strictly relative to the input size _n_. If we maintain the base as _n_, value of _k_ for each round to bound to _n_-1, resulting to, sorting in _O(n_) time for each round and the total number of rounds is _log<sub>n</sub>k_. Thus, BNRS achieves an overall time complexity of _O(n_log_<sub>n</sub>k_). The weaknesses identified in the algorithm are the following. There is a lack in adaptive control of input in rounds as it performs unnecessary sorting on relatively sorted input amongst the same logarithmic group and the cost for computation overhead for practical performance. We will be addressing them by introducing an optimization approach by partitioning the input array into active region and sorted region with a predicate condition and subsequently reducing the size of the active region.

Now, we shall explore the novel optimization strategy that effectively reduce the input size for sorting in the consecutive rounds which is achieved by partitioning the input into two regions.

#### 2.1 Stable Partitioning Approach

**-** **Mechanism:** This approach utilizes a stable partitioning algorithm in each round. It separates elements into two groups-- ‘sorted’ and ‘active’ based on a predicate. The predicate evaluates whether an element has been fully sorted relative to the current and future rounds by the condition _A_\[_i_\]_/base_<sup>_r_-1</sup>=0. Elements satisfying this condition are moved to the front, marking distinction between the ‘sorted’ and ‘active’ region.<tbc>

**-** **Advantage:** Only the active portion of the array is processed in the subsequent passes that results in reducing the active portion, though it need not be at every round. This drastically reduces the number of elements handled in later rounds, leading to significant performance gain on skewed datasets<tbc>

**-** **Stability:** The use of a stable partition function and a stable sorting subroutine ensures that the entire algorithm maintains the relative order of equal elements (i.e., the elements having the same values).

Compared to BNRS, the stable partitioning approach reduces redundant work by limiting the process required for unsorted portion in each round, improving efficiency and performance of the algorithm. However, these improvements come at the cost of increased overhead, which is a drawback, hence we need to find break-even condition which would determine the utility of the optimization in comparison to the cost of implementation by the provision of the early termination strategies. The notations used in this paper are presented in  4, Appendix.


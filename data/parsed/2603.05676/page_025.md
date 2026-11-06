<tbc>each of which is either 0 or 1, such that there are _n-m_ 0’s and _m_ 1’s in _A_. Our goal of moving the short runs to the end of _A_ is equivalent to segregating the 0’s and 1’s in _A_, such that the _n-m_ 0’s precede the _m_ 1’s. While it is important for us that the 0’s are moved stably, i.e., that the long runs are not destroyed, it is not important for us and in general our algorithm will not preserve the stability of the 1’s, i.e., the short runs. This can be done in-place in _O(n_) time by making a single pass through _A_ while maintaining two pointers, one for the next 0 and one for the first preceding 1. See Algorithm 8.

In our setting, we do not know which elements are 0’s or 1’s _a priori_. However, since these labels are determined by the length of each run and our algorithm performs a single pass through _A_, we can scan each run as we come across them to determine whether they are a run of 0’s or 1’s. We may scan each run at most twice, once for each pointer, so this adds an additional _O(n_) time.

**Algorithm 8** In-Place Run Partitioning

1: Let _A_\[_i_\] be the first cell with _A_\[_i_\]=1

2: Let _A_\[_j_\] be the first cell with _A_\[_j_\]=0 and _j\>i_

3: Swap _A_\[_i_\] and _A_\[_j_\]

4: **while** _i\<n_ **do**

5: Let _A_\[_i_\] be the next cell with _A_\[_i_\]=1

6: Let _A_\[_j_\] be the next cell with _A_\[_j_\]=0 and _j\>i_

7: Swap _A_\[_i_\] and _A_\[_j_\]

Note that this algorithm will move 0’s forward in a way that preserves their original order in the array, _A_. Thus, we have the following:

**Theorem 8.** _Given an array, A, of n cells, m of which store 1’s and n-m of which store 0’s, we can stably partition the 0’s in-place to the first n-m cells in A in O(n_) _time._

### E Experimentally Evaluating Walk-Back Cost

We support our theoretical results with experiments by comparing the performance of several stack-based mergesorts with their in-place versions produced from the walk-back algorithm. We also compare our algorithms against the performance of the built-in C++ implementation of introsort, `std::sort`, and against QuickXsort, a recent in-place sorting algorithm.

#### E.1 Experimental setup

We ran our C++ experiments on `Ubuntu 22.04.5 LTS` (Linux kernel<br>
`5.15.0-135-generic`). The hardware comprised two Intel® Xeon® X5680 processors (@ 3.33GHz, 24MiB total L3 cache) and 94GiB of RAM. The


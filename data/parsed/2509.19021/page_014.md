## Appendix

### 7.1 Time and Space Complexities of Sorting Algorithms

The detailed time complexity some comparison and non-comparison sorting algorithms is given in  8.

### 7.2 American Flag Sorting

AFS sorting algorithm is a modified version of Radix sort and is designed to sort strings or integers by looking at one byte at a time and assigns it to a group/bucket. The traditional radix sort uses LSD approach and a second ‘work array’ of the same size of the original data to move the items back and forth. On the other hand, AFS performs Most Significant Digit (MSD) approach and

\begin{tabular}{cc}
**Notation** & **Description** \\
_n_ & Total number of elements in the input array (i.e., input size). \\
_k_ & The maximum value for an element in the array. \\
_A_ & The input array containing _n_ elements \\
_A\[i_\] & The element at index _i_ in the array _A_. \\
_B_ & An auxiliary output array for storing intermediate results. \\
_C_ & An auxiliary array used for counting frequencies. \\
_R_ & The number of rounds (passes), calculated as \(\lfloor log_n(k)\rfloor+1\). \\
_r_ & The current round or iteration, where \(0\le r<R\). \\
_p_ & The proportion of elements removed by the first predicate check. \\
div & The value of an element scaled by the base, calculated as \(\lfloor A\lceil i\rceil/base^r\rfloor\). \\
predicate & A check used to partition elements, e.g., \(\lfloor A\lceil i\rceil/div\rfloor\). \\
\(\alpha\) & Amortized cost of random-access sorting per element. \\
\(\beta\) & Amortized cost of partitioning per element. \\
_c_ & Ratio of sorting cost to partitioning cost. \\
\end{tabular}

\begin{tabular}{ccccc}
**Algorithm** & **Best Case** & **Average Case** & **Worst Case** & **Space** \\ Counting Sort & _O(n+k_) & _O(n+k_) & _O(n+k_) & _O(n+k_) \\ Radix Sort & \(O(d\cdot(n+b))\) & \(O(d\cdot(n+b))\) & \(O(d\cdot(n+b))\) & _O(n+b_) \\ Bucket Sort & _O(n+b_) & _O(n+b_) & _O(n_<sup>2</sup>) & _O(n+b_) \\ \end{tabular}

7:  of Notations Used in the Algorithm.

8: Complexity analysis of known non-comparison sorting algorithms, where _n_ is input size, _k_ is maximum value, _d_ is number of rounds/digits and _b_ is radix/base for Radix Sort and the number of buckets for Bucket Sort.


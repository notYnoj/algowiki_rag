size increases, computation time exhibits characteristic exponential growth with accelerating rates. This accelerating computational complexity presents significant challenges for larger scale problems.

## 4.2 Impact of Block/Stack Size on Speed

In this experimental section, we fixed the number of pre- placed rows at 6 and utilized a single RTX 4090 GPU to evaluate the performance of the two shared memory optimization approaches (Approach 1 and Approach 2) described in Section 3.2. The experimental results are presented in  4.

The experimental results demonstrate that when employing static shared memory allocation, optimizing stack space utilization to increase block size yields significant performance improvements. In contrast, dynamic shared memory allocation (expanded to 96KB) with block size adjusted to 256 resulted in computational performance degradation <sup>5</sup>. This phenomenon confirms the critical importance of L1 cache - which shares hardware resources with shared memory - for performance optimization. On the other hand, this also indicates that the dynamic allocation mechanism of shared memory can incur performance overhead.

## 4.3 Impact of Last-Row Optimization on Speed

Building upon optimization Approach 3 in Section 3.2, the maximum solvable queens number N can be increased by 1 for each configuration. To evaluate the performance impact of this optimization, we replicated the experimental methodology from Section 4.2. The results are presented in  5.

The data in  5 demonstrates that implementing the last-row optimization yields consistent speed improvements compared to the  4 baseline. Notably, All Configurations demonstrate a significant speedup of over 25%. Consequently, this optimization is adopted as the default approach in our study.

Special attention must be paid to implementation efficiency, as inefficient implementation can significantly diminish the potential speed improvements. Algorithm 3 presents two equivalent implementations. The initial implementation realizes the last-row optimization through a separate if-statement, resulting in two consecutive conditional checks that yield negligible speed improvement. By contrast, merging these conditionals into a single if-statement produces significant performance gains.

**Algorithm 3** Two Ways of Last-Row Optimization

**Before:**

1: **if**(valid\_pos == 0) {

2: continue;

3: }

4: **if**(\_popc(cur) == N - 1) {

5: sum++;

6: continue;

7: }

**After:**

1: **if**(valid\_pos == 0 || \_popc(cur) == N - 1) {

2: sum += \_popc(valid\_pos);

3: continue;

4: }

## 4.4 Evaluation of Inline PTX Optimization

Although only limited optimizations were applied to the inline PTX code, the achieved performance improvements surpassed expectations, as demonstrated in  6.

Compared with table 5, all configurations achieved a speed- up exceeding 7%. These results confirm the viability of assembly level optimizations, heralding PTX optimization as an emerging critical skill in GPU programming.

Although Configuration 3 exhibited the highest computational efficiency, its 6-row pre-placement constraint limited<tbc>

<sup>5</sup>Other configurations such as 64KB similarly led to performance deterioration.

\begin{tabular}{ccccccc}
**Config** & **N=17** & **N=18** & **N=19** & **N=20** & **N=21** & **N=22** \\
1 & 142 & 237 & 972 & 6536 & 52501 & 452699 \\
2 & 137 & 218 & 857 & 5447 & 43355 & 371939 \\
3 & 133 & 204 & 738 & 4669 & 36990 & 316425 \\
6 & 142 & 246 & 988 & 6631 & 53287 & 458433 \\
\end{tabular}

\begin{tabular}{ccccccc}
**Config** & **N=17** & **N=18** & **N=19** & **N=20** & **N=21** & **N=22** \\
1 & 131 & 219 & 720 & 4606 & 36765 & 316293 \\
2 & 130 & 211 & 635 & 3951 & 31217 & 267182 \\
3 & 128 & 196 & 585 & 3472 & 27247 & 233548 \\
6 & 131 & 206 & 737 & 4674 & 37121 & 318318 \\
\end{tabular}

\begin{tabular}{ccccccc}
**Config** & **N=17** & **N=18** & **N=19** & **N=20** & **N=21** & **N=22** \\
1 & 128 & 203 & 658 & 4127 & 32619 & 279885 \\
2 & 126 & 183 & 609 & 3636 & 28551 & 245090 \\
3 & 126 & 181 & 566 & 3307 & 25337 & 216740 \\
\end{tabular}

** 4.** Comparison of N-Queens Solving Times (in milliseconds) Under Different Block and Stack Size Configurations with a Single RTX 4090 GPU

** 5.** Comparison of N-Queens Solving Times (in milliseconds) Under Different Block and Stack Size Configurations with a Single RTX 4090 GPU (With Last-Row Optimization)

** 6.** Comparison of N-Queens Solving Times (in milliseconds) Using Inline PTX Optimization with a Single RTX 4090 GPU (With Last-Row Optimization)


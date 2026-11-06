We set \(B=\frac{logn}{5}\) so that the preprocessing time is _o(n_). For each frequent element we spend O(_n_<sup>2</sup>_/B_) time, so \(\mathcal{O}(n^2/B\cdot c)\) overall. For each fragment consisting of rare elements, the time is O(cnt(_v_)<sup>2</sup>log<sup>2</sup>(_n/_cnt(_v_))) for every _v_ to compute the results, and then O(_n_<sup>2</sup>_/B_) plus the number of results. Using \(\mathsf{cnt}(v)\le n/c\), where _c_ is sufficiently large, and calculating the derivative of _f(x_)=_x_log<sup>2</sup>(_n/x_) we upper bound \(\mathsf{cnt}(v)log^2(n/\mathsf{cnt}(v))\le n/c\cdot log^2c\) for every rare _v_, so the overall time is \(\mathcal{O}(n^2/B\cdot c+n/c\cdot log^2c\sum_v\mathsf{cnt}(v))=\mathcal{O}(n^2/B\cdot c+n^2/c\cdot log^2c)\).

Choosing \(c=\sqrt{logn}logogn\) we obtain an algorithm working in \(\mathcal{O}(n^2loglogn/\sqrt{logn})\) time.

## 6 Longest Common Weakly Increasing Subsequence

In this section we explain how to modify the algorithm to solve the weakly increasing version of the problem. We adapt both solutions without changing their complexity as explained below, and then combine them using the same threshold for the frequent/rare elements to arrive at \(\mathcal{O}(n^2loglogn/\sqrt{logn})\) complexity.

### 6.1 First solution

We define _dp_ as in the algorithm for LCIS. It can be calculated using the following recurrence (slightly different than for LCIS):

\(dp_{v+1}[i][j]=\left\{\begin{array}{ c c }
max\{dp_v[i][j],dp_{v+1}[i-1][j-1]+1\}, & \text{if}A[i]=B[j]=\sigma[v+1], \\
max\{dp_v[i][j],dp_{v+1}[i-1][j],dp_{v+1}[i][j-1]\}, & \text{otherwise.}
\end{array}\right.\)

The proof of Lemma 3.1 still holds, so we can store a table \(dp'\) and retrieve any value of _dp_ from \(dp'\) in constant time.

Algorithm 1 stays essentially the same so we skip a detailed explanation. The speed up is implemented by considering whole blocks of \(dp'_{v+1}\) instead of single entries. Consider a single block of \(dp'_{v+1}\) consisting of the values of \(dp'_{v+1}[i][j],dp'_{v+1}[i][j+1],\dots,dp'_{v+1}[i][j+B-1]\), and assume that they have been already partially updated by propagating the maximum. To calculate their correct values we need the following information:

1. \(dp'_{v+1}[i-1][j],dp'_{v+1}[i-1][j+1],\dots,dp'_{v+1}[i-1][j+B-1]\),<tbc>

2. \(dp'_{v+1}[i][j],dp'_{v+1}[i][j+1],\dots,dp'_{v+1}[i][j+B-1]\),<tbc>

3. _dp_<sub>_v_+1</sub>\[_i_-1\]\[_j_-1\],<tbc>

4. _dp_<sub>_v_+1</sub>\[_i_\]\[_j_-1\],<tbc>

5. for which indices _j,j_+1_,...,j+B_-1 we have \(A[i]=B[j]=\sigma[v+1]\).

Once again we can rewrite the procedure so that instead of the values _dp_<sub>_v_+1</sub>\[_i_-1\]\[_j_-1\] and _dp_<sub>_v_+1</sub>\[_i_\]\[_j_-1\] only the difference _dp_<sub>_v_+1</sub>\[_i_\]\[_j_-1\]-_dp_<sub>_v_+1</sub>\[_i_-1\]\[_j_-1\] is needed. By Lemma 3.1, the difference belongs to {0,1}, so the whole information required for calculating the correct values consists of 3_B_+1 bits. This allows us to update the whole table in O(_n_<sup>2</sup>_/B_) as for LCIS.

We set \(B=\frac{logn}{4}\) as to make required preprocessing _o(n_). Overall complexity of the algorithm becomes \(\mathcal{O}(|\sigma|n^2/logn)\).


<tbc>increasing subsequence subject to elements whose values lie in range \([\alpha,\beta]\). Longest increasing subsequence is equivalent to LCS when the inputs are two permutations of _n_ distinct characters.

Finally, we define a notation to denote the normalized solution sizes. For LCS, we denote the normalized solution size by \(||\mathsf{lcs}(A,B)||=\mathsf{lcs}(A,B)/\sqrt{|A||B|}\) for _A_ and _B_ and we use \(||\mathsf{ed}(A,B)||=\mathsf{ed}(A,B)/(2\sqrt{|A||B|})\) for edit distance. Note that, when the two strings have equal length we have \(||\mathsf{ed}(A,B)||+||\mathsf{lcs}(A,B)||=1\). Similarly, for longest increasing subsequence, we denote by \(||\mathsf{lis}(A)||=\mathsf{lis}(A)/|A|\) the normalized solution size. We usually refer to the size of the input array by _n_.

Throughout this paper, we call an algorithm \(f(\lambda)\)-approximation for LCS if it is able to distinguish the following two cases: i) \(||\mathsf{lcs}(A,B)||\ge\lambda\) or ii) \(||\mathsf{lcs}(A,B)||<\lambda f(\lambda)\). A similar definition carries over to LIS. Once an \(f(\lambda)\)-approximation algorithm is provided for either LCS or LIS, one can turn it into an algorithm that outputs a solution with size \(f(\lambda)(1-\epsilon)\lambda n\) provided that the optimal solution has a size \(\lambda n\). The algorithm is not aware of the value of \(\lambda\) but will start with \(\lambda_0=1\) and iteratively multiply \(\lambda_0\) by \(1-\epsilon\) until a solution is found.

## 1.3 Techniques Overview

Our algorithm for LCS is inspired by the recent developments for edit distance \[BEG<sup>+</sup>18, CDG<sup>+</sup>18\]. We begin by briefly explaining the previous ideas for approximating edit distance and then we show how we use these techniques to obtain a solution for LCS. Finally, in Section 1.3.2 we outline our algorithm for LIS.

### 1.3.1 Summary of Previous ED Techniques

Indeed, edit distance is hard only if the two strings are far \((||\mathsf{ed}(A,B)||=\delta\) and \(\delta=n^{-o(1)}\)) otherwise the \(O(n+(n\delta)^2)\) algorithm of Landau _et al._ \[LMS98\] computes the solution in truly subquadratic time. The algorithm of Chakraborty _et al._ \[CDG<sup>+</sup>18\] for edit distance has three main steps that we briefly discuss in the following.

#### Step 0 (window-compatible solutions):

In the first step, they construct a set of _windows_, or (contiguous) substrings, _W<sub>A</sub>_ for string _A_, and _W<sub>B</sub>_ for string _B_. Let _k_ denote the total number of windows of \(W_A\cup W_B\). For simplicity, let all the windows have the same size _d_ and \(n\simeq O(kd)^\text{9}\). The construction features two key properties: 1) provided that the edit distances of the windows between _W<sub>A</sub>_ and _W<sub>B</sub>_ are available, one can recover a \(1+\epsilon\) approximation of edit distance in time \(\widetilde{O}(n+k^2)\) via dynamic programming. 2) \(k^2\times d^2\simeq O(n^2)\). That is, if we naively compute the edit distance of every pair of windows, the overall running time would still asymptotically be the same as that of the classic algorithm.

In order to obtain a solution for edit distance, it suffices to know the distances between the windows. However, Chakraborty _et al._ \[CDG<sup>+</sup>18\] show that knowing the distances between some of the window pairs is enough to obtain an approximately optimal solution for edit distance. Step 1 provides estimates for the distances of the windows which is approximately correct except for \(O(k^{2-\Omega(1)})\) many pairs and Step 2 shows how this can be used to obtain a solution for edit distance. Discretization simplifies the problem substantially. For a fixed \(0\le\delta\le 1\), they introduce a graph \(\mathsf{G}_\delta\) where the nodes correspond to the windows and an edge between window \(w_i\in W_A\) and window \(w_j\in W_B\) means that \(||\mathsf{ed}(w_i,w_j)||\le\delta\). If we are able to construct \(\mathsf{G}_\delta\) for logarithmically different choices of \(\delta\), we can as well estimate the distances within a \(1+\epsilon\) factor for the windows. Therefore<tbc>

<sup>9</sup>The equality holds if we assume \(\delta=\Omega(1)\).


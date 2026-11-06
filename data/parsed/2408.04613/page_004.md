### Applications.

As an application of our witness recovery functionality, we consider the problem of range LIS queries. This task asks to preprocess an integer array _s_[0_..n_) so that, later, given two indices \(0\le i<j\le n\), the longest increasing subsequence (LIS) of the sub-array _s[i..j_) can be reported efficiently. Tiskin [42,45] showed that the LIS size \(\ell\) can be reported in O(log_n_) time after O(_n_log<sup>2</sup>_n_)-time preprocessing. It was unclear, though, how to efficiently report the LIS itself. The recent work of Karthik C. S. and Rahul [29] achieved \(\mathcal{O}(n^{1/2}log^3n+\ell)\)-time reporting (correct with high probability) after O(_n_<sup>3/2</sup>log<sup>3</sup>_n_)-time preprocessing. It is fairly easy to use our witness recovery algorithm to deterministically support \(\mathcal{O}(\ell log^2n)\)-time reporting after O(_n_log<sup>2</sup>_n_)-time preprocessing; see Section 5 for an overview of this result. As further shown in Appendix B, the reporting time can be improved to \(\mathcal{O}(\ell logn)\) and, with the preprocessing time increased to O(_n_log<sup>3</sup>_n_), all the way to \(\mathcal{O}(\ell)\).

\(\blacktriangleright\) **Theorem 1.3.** _For every parameter_ \(\alpha\in[0,1]\)_, there exists an algorithm that, given an integer array s_[0_..n), in time_ \(\mathcal{O}(nlog^{3-\alpha} n)\) _builds a data structure that can answer range LIS_ reporting _queries in time_ \(\mathcal{O}(\ell log^\alpha n)\)_, where_ \(\ell\) _is the length of the reported sequence._

_In particular, there is an algorithm with_ O(_n_log<sup>3</sup>_n_) _preprocessing and_ \(\mathcal{O}(\ell)\) _reporting time and an algorithm with_ O(_n_log<sup>2</sup>_n_) _preprocessing and_ \(\mathcal{O}(\ell logn)\) _reporting time._

In parallel to this work, Gorbachev and Kociumaka [23] used core-sparse Monge matrix multiplication for the _weighted edit distance_ with integer weights. Theorem 1.2 allowed for saving two logarithmic factors in the final time complexities compared to the initial preprint using Russo’s approach [38]. Weighted edit distance is known to be reducible to unweighted LCS only for a very limited class of so-called uniform weight functions [42], so this application requires the general core-sparse Monge matrix multiplication.

### Open Problem.

An interesting open problem is whether any non-trivial trade-off can be achieved for the _weighted_ version of range LIS queries, where each element of _s_ has a weight, and the task is to compute a maximum-weight increasing subsequence of _s[i..j_): either the weight alone or the whole subsequence. Surprisingly, as we show in Appendix B.1, if our bound \(\delta(A\otimes B)\le 2\cdot(\delta(A)+\delta(B))\) of Theorem 1.1 can be improved to \(\delta(A\otimes B)\le c\cdot(\delta(A)+\delta(B))+\widetilde{\mathcal{O}}(p+q+r)\) for some \(1\le c<2\), then our techniques automatically yield a solution with \(\widetilde{\mathcal{O}}(n^{1+log_2c})\) preprocessing time, \(\widetilde{\mathcal{O}}(1)\) query time, and \(\widetilde{\mathcal{O}}(\ell)\) reporting time.

## 2 Preliminaries

\(\blacktriangleright\) **Definition 2.1.** _A matrix A of size_ \(p\times q\) _is a_ Monge matrix _if it satisfies the following_ Monge property _for every_ \(i\in[0..p-1)\) _and_ \(j\in[0..q-1)\):

\(A_{i,j}+A_{i+1,j+1}\le A_{i,j+1}+A_{i+1,j}.\)

_Furthermore, A is an_ anti-Monge matrix _if the matrix −A (with negated entries) is a Monge matrix._

In some sources, the following equivalent (but seemingly stronger) condition is taken as the definition of Monge matrices.

\(\blacktriangleright\) **Observation 2.2.** _A matrix A of size_ \(p\times q\) _is a Monge matrix if and only if it satisfies the following inequality for all integers_ \(0\le a\le b<p\) _and_ \(0\le c\le d<q\):

\(A_{a,c}+A_{b,d}\le A_{a,d}+A_{b,c}.\)

**Proof.** It suffices to sum the inequality in Definition 2.1 for all \(i\in[a..b)\) and \(j\in[c..d)\).


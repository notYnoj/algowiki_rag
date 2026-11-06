have equal length.

\(\blacktriangleright\) **Theorem 2.** _Given two strings A and B of length n over an arbitrary alphabet of size k, there exist positive constants_ \(\epsilon\) _and_ \(\delta\) _such that we can compute a_ \(1/k+\epsilon\) _approximation for the longest common subsequence of A and B in_ \(O(n^{2-\delta})\) _time._

In fact, our algorithm can actually \((1/k+\epsilon)\)-approximate the LCS in near-linear time. Note that our result applies only to strings with equal input lengths. The relevance of this restriction is discussed in Section 2, which also contains the proof of Theorem 1. We present the proof of Theorem 2 in Section 3.

## Preliminaries.

We write approximation ratios as constants less than 1, so that for example a \(1/2+\epsilon\) approximation algorithm for the LCS of _A_ and _B_ is an algorithm that returns a common subsequence of _A_ and _B_ with length at least \((1/2+\epsilon)\cdot\text{LCS}(A,B)\).

When we discuss edit distance in the rest of the paper we mean the version of edit distance that does not allow symbol substitutions but only measures the number of insertions and deletions. For constant factor approximation algorithms, this version of the problem is equivalent to the original.

## 2 Reduction to Binary Alphabets & Input Length Conditions

We begin by showing how to reduce nontrivial constant factor approximations of LCS over large alphabets to better than 1/2 approximations of LCS over binary alphabets. Although we do not directly apply this reduction in our proof of Theorem 2, the reduction is elegant and motivates the approach we end up using. Moreover, the reduction works even for strings of non-equal lengths, thus showing that one merely needs to extend the Rubinstein-Song result to non-equal length strings in order to truly improve upon the trivial alphabet-size approximation algorithm. We will need the following definition.

\(\blacktriangleright\) **Definition 3** (Restrictions)**.** _Given an alphabet_ \(\Sigma\)_, we call a subset_ \(\Sigma'\subseteq\Sigma\) _a_ subalphabet. _Given a string A from alphabet_ \(\Sigma\) _the restriction of A to a subalphabet_ \(\Sigma'\) _is the maximum subsequence of A whose characters are all in_ \(\Sigma'\).

\(\blacktriangleright\) **Theorem 4.** _Fix integers s and_ \(\ell\) _with_ \(s>\ell\ge 2\)_. Suppose that there is a_ \(T(n,\ell)\) _time algorithm that achieves an_ \(1/(\ell-\epsilon)\)_-approximation of the LCS of two strings of length at most n from an alphabet of size_ \(\ell\)_. Then, there is also a_ \(O((n+T(n,\ell))\genfrac(){pt}{2}{s}{\ell})\) _time algorithm that achieves an_ \(1/(s(1-\epsilon/\ell))\)_-approximation of the LCS of two strings of length at most n from an alphabet of size s._

**Proof.** We will show how to reduce the LCS for two strings of length at most _n_ over a _s_-ary alphabet, to the LCS for two strings of length at most _n_ over an \(\ell\)-ary alphabet for any \(\ell<s\). The reduction runs in \(O(n\genfrac(){pt}{2}{s}{\ell})\) time and produces \(\genfrac(){pt}{2}{s}{\ell}\) instances of \(\ell\)-ary alphabet LCS.

Let _A_ and _B_ two strings of length at most _n_ over an alphabet \(\Sigma\) of size _s_. Let _C_ be the longest common subsequence of _A_ and _B_ (we do not know _C_). For the sake of argument, sort the alphabet symbols according to their number of occurrences in _C_.

Let _x_ be the collection of the \(\ell\) most frequent alphabet symbols in _C_. Let _C<sub>x</sub>_ be the subsequence of _C_ obtained by restricting _C_ to the subalphabet of \(\Sigma\) that contains the symbols of _x_. Since _x_ has the \(\ell\) most frequent symbols in _C_, _C<sub>x</sub>_ contains at least an \(\ell/s\) fraction of _C_.


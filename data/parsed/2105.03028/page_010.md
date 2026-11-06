## 23:10 Improved Approximation for Longest Common Subsequence over Small Alphabets

Consequently, 0(_Y_) and 1(_X_) are within \(\delta m\) of each other. Then by Lemma 13, as long as we take \(\delta\) small enough in terms of \(\rho\) we get a subquadratic \(1/2+\epsilon'\) approximation for LCS(_X,Y_). As noted earlier, this then yields the desired \(1/s+\epsilon\) approximation for LCS(_A,B_) in truly subquadratic time. In fact, because we only ever use subroutines that run in linear time or constant factor approximations to edit distance which take near-linear time, the overall algorithm takes near-linear time.

## 4 Proof of Lemma 13

This section is devoted to proving Lemma 13. We do this working through the individual arguments in the case analysis of [21] and verifying that the arguments still hold in the case where the strings have different lengths, as long as they satisfy the frequency requirements included in the hypotheses of the lemma. Throughout this section we fix the binary alphabet \(\Sigma=\{0,1\}\) and assume that all strings come from this alphabet.

We carry over the following subroutines from [21].

\(\blacktriangleright\) **Definition 15.** _Given strings A and B and a symbol_ \(\sigma\)_, the algorithm_ \(\mathrm{Match}(A,B,\sigma)\) _returns the largest subsequence of A and B consisting entirely of copies of_ \(\sigma\).

\(\blacktriangleright\) **Definition 16.** _Given strings A and B, the algorithm_ BestMatch(_A,B_) _returns the longer of the strings_

Match(_A,B,_0) _and_ Match(_A,B,_1).

_In other words, the algorithm returns the largest common unary subsequence._

Note that BestMatch is a 1/2 approximation algorithm for LCS.

\(\blacktriangleright\) **Definition 17.** _Given strings A_<sub>1</sub>_,A_<sub>2</sub>_, and B, the algorithm_ Greedy(_A_<sub>1</sub>_,A_<sub>2</sub>_,B_) _returns_

\(max_{B=B_1\sqcup B_2}\mathrm{BestMatch}(A_1,B_1)+\mathrm{BestMatch}(A_2,B_2)\)

_taken over all possible splits of B into two contiguous left and right substrings B_<sub>1</sub> _and B_<sub>2</sub>.

These algorithms can all be implemented to run in linear time by scanning through the counting how many 0s and 1s appear in each string. The final procedure we will invoke utilizes an approximation algorithm for computing the edit distance of two strings as a black-box. Although any fast enough constant factor approximation for edit distance will work, for concreteness we assume that it leverages the algorithm \(\widetilde{\mathrm{ED}}\) from [5], which runs in subquadratic time and can approximate the edit distance to a \(c=3+\epsilon'\) factor for any fixed positive constant \(\epsilon'\). Note that this algorithm can also return a common subsequence achieving the given length.

**Proof of Lemma 13.** Let \(1(X)=\alpha m\) for some \(\alpha\in[0,1]\). By assumption, we know that \(\alpha<1/2\) is bounded away from 1/2 by some constant amount. We can also assume that 0(_Y_) is within \(\delta m\) of 1(_X_) for some positive parameter \(\delta<0\) to be picked later on. We will end up setting \(\delta\) to be some sufficiently small constant depending on \(\alpha\). We will use the notation ≈ to denote quantities that are within \(\delta m\) of each other. For example 1(_X_)≈0(_Y_). This lets us avoid having to stick in \(\pm\delta m\) symbols in all the inequalities and helps make the arguments cleaner without affecting the correctness (since we just care about getting a \(1/2+\epsilon\) approximation for _some_ constant \(\epsilon>0\)).


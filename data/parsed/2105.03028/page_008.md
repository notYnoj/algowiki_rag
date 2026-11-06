## 23:8 Improved Approximation for Longest Common Subsequence over Small Alphabets

By similar reasoning, if _m=j_ and \(M\ge j\) then we have

\(|\sigma_M(B)-\sigma_m(B)|=|\sigma_M(B)-\sigma_j(B)|\le|\sigma_M(B)-\sigma_{j-1}(B)|+|\sigma_{j-1}(B)-\sigma_j(B)|\le(2\rho/s)n.\)

If instead _M,m\>j_ we know that

\(|\sigma_M(B)-\sigma_m(B)|\le|\sigma_M(B)-\sigma_{j-1}(B)|+|\sigma_{j-1}(B)-\sigma_m(B)|\le(2\rho/s)n\)

since now the subalphabets \(\{\sigma_M,\sigma_{j-1}\}\) and \(\{\sigma_m,\sigma_{j-1}\}\) both occur in Equation (3). Similar reasoning on the remaining cases of the values of _M_ and _m_ relative to _j_ to establishes the inequality

\(\sigma_M(B)-\sigma_m(B)\le(3\rho/s)n.\)

We have dropped absolute value signs because the left hand side of the above equation is positive by definition of _M_ and _m_. Since \(s\ge 3\) this contradicts the assumption that _B_ is not \(\rho\)-balanced, and the desired result follows. Note that we can find which of subalphabets from Equation (3) satisfies the conditions of the lemma in _O(n+s_) time by scanning through _B_ to get the counts of each of its characters and trying out all the restrictions. \(\blacktriangleleft\)

In our proof of Theorem 2, we will require a stronger form of the result from Section 4 of [21]. This variant of their theorem is useful because it applies to strings of different length.

\(\blacktriangleright\) **Lemma 13.** _Let X and Y be binary strings of length n and m respectively, where_ \(m\le n\)_. Suppose the frequencies_ 0(_Y_) _and_ 1(_X_) _are both at most_ \((1/2-\rho)m\) _for some positive constant_ \(\rho\)_. Then there exist positive constants_ \(\delta\) _and_ \(\epsilon\) _such that if_ 0(_Y_) _and_ 1(_X_) _are within_ \(\delta m\) _of each other, we can compute a_ \((1/2+\epsilon)\) _approximation of_ LCS(_X,Y_) _in subquadratic time._

Although the realization that this type of result holds for strings of differing length is novel, the proof of Lemma 13 itself is conceptually identical to the frequency analysis used in [21], requiring only minor changes to make the argument go through. For completeness we include the detailed casework proof of this result in Section 4.

Finally we apply a lemma that provides some frequency information about the strings.

\(\blacktriangleright\) **Lemma 14** (Lemma 3.1 from [21])**.** _For any_ \(\delta>0\) _if_

\(min\left(0(X),0(Y)\right)>(1+\delta)min\left(1(X),1(Y)\right)\)

_or_

\(min\left(1(X),1(Y)\right)>(1+\delta)min\left(0(X),0(Y)\right)\)

_then there is a unary_ \((1+\delta)/(2+\delta)\) _approximation for_ LCS(_X,Y)._

**Proof.** Observe that for any binary strings _X_ and _Y_ we have

\(LCS(X,Y)\le min\left(0(X),0(Y)\right)+min\left(1(X),1(Y)\right).\) (4)

This equation holds because the LCS is a subsequence of _X_ and _Y_ , and thus cannot contain more zeros or ones than either of the strings _X_ or _Y_ individually have.

Suppose by symmetry that min(0(_X),_0(_Y_)) is the larger of the two addends on the right. Then the we can return the all zeros string of this length. By the first inequality we get

\(min\left(0(X),0(Y)\right)>(1+\delta)\left(LCS(X,Y)-min\left(0(X),0(Y)\right)\right)\)

and then rearranging proves the claim. \(\blacktriangleleft\)


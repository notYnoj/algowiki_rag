Thus there are exactly \(2\cdot\) LCS(_X,Y_) characters paired up in the alignment and ED(_X,Y_) unmatched characters. These encompass all the characters in _X_ and _Y_ , and thus account for _n+m_ symbols.

\(\blacktriangleright\) **Definition 7** (Approximating LCS through Edit Distance)**.** _Given strings A and B of length n, the algorithm_ ApproxED(_A,B_) _approximates the edit-distance between A and B and then returns the lower bound on the LCS implied by this. More precisely, the algorithm computes an approximate edit distance_ \(\widetilde{ED}(A,B)\) _and then returns_

\(n-\frac{1}{2}\cdot\widetilde{ED}(A,B).\) (1)

As stated ApproxED can use any edit distance approximation \(\widetilde{ED}\) as a black box. For concreteness, we will take \(\widetilde{ED}\) to be the edit distance algorithm from [5] which can achieve an approximation ratio of _c_ for any constant _c\>_3 and runs in truly subquadratic time.

In [21], the authors use the ApproxED algorithm to handle the case of binary strings with large LCS. In this case, they notice that if the LCS is large then the edit distance must be small. Then constant factor approximations to edit distance will give good lower bounds on the LCS because in the calculation from Equation (1) we are subtracting off a small quantity from the maximum possible LCS value of _n_.

However, if we tried extending this algorithm to the case where the inputs _X_ and _Y_ have lengths _n_ and _m_ with _n_=100_m_ (for example) by using the identity from Lemma 6, then even when the LCS is large (say of length \((1-\epsilon)m\) for some small positive \(\epsilon\)) the edit distance will still be very large compared to the length of the smaller string (at least \((99+\epsilon)m\)). So even a 3-approximation to edit-distance would incur massive error when trying to approximate LCS by computing

\(\frac{1}{2}\cdot\left(n+m-\widetilde{ED}(X,Y)\right)\)

and the result would not give any nontrivial lower bound for the LCS. In other words, when the input strings have very different lengths it is not clear how to use approximate edit distance in general to obtain good approximations for LCS. This is essentially why the algorithm from [21] and Theorem 2 both require equal length inputs.

## 3 Extending Alphabet Size

This section proves Theorem 8 which restates Theorem 2 from the introduction slightly.

\(\blacktriangleright\) **Theorem 8.** _Given two strings A and B of length n over an arbitrary alphabet_ \(\Sigma\) _of size s, there exist a positive constant_ \(\epsilon\) _such that we can compute a_ \(1/s+\epsilon\) _approximation for the longest common subsequence_ LCS(_A,B_) _of A and B in truly subquadratic time._

Throughout the rest of this section, we assume _A_ and _B_ refer to strings satisfying the conditions of Theorem 8 and that \(s\ge 3\). We begin by establishing lemmas corresponding to easy instances of the problem. The following definition is useful for identifying these easy cases.

\(\blacktriangleright\) **Definition 9** (Balanced Strings)**.** _Given a string A of length n from an alphabet of size s and a parameter_ \(\rho>0\)_, we say a string is_ \(\rho\)-balanced _if all its character frequencies are within_ \(\rho n\) _of n/s._


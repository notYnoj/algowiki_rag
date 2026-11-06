We can now make use of Corollary 19. Count for each \(a'\in A'\) the number of _witnesses_ \((a',b',Ri)\) with \(a'+b'\in R'\). We claim that it remains to check whether there is some \(a'\) that is involved in \(|B'|\) witnesses. To see this, note that due to the disjointness of the _Ri_’s, for any \(a'\in A'\) we have that the number of \((b',Ri)\) with \(a'+b'\in Ri\) is equal to the number of \(b'\) such that there exists _Ri_ with \(a'+b'\in Ri\). Again, the desired reduction to 3-SUM follows. \(\blacktriangleleft\)

We remark that, by [11], we know that the complexity of the union of orthants in R_<sup>d</sup>_ has worst case complexity \(O(n^{\lfloor d/2\rfloor})\). Thus, the above proof does not seem directly generalizable to inequality dimensions larger than 3. We can extend Theorem 28 to _k_-quantifiers by the following theorem.

\(\blacktriangleright\) **Theorem 5.** _There is an algorithm deciding_ 3_-SUM in randomized time_ \(O(n^{2-\epsilon})\) _for an_ \(\epsilon>0\)_, if and only if for each problem P in_ \(\mathsf{FOP}_\mathbb{Z}^k\) _with_ \(k\ge 3\) _and inequality dimension at most_ 3_, there exists some_ \(\epsilon>0\) _such that we can solve P in randomized time_ \(O(n^{k-1-\epsilon})\).

The above theorem gives us immediate reductions to 3-SUM for many seemingly unrelated problems of different quantifier structures and semantics.

For instance, as a direct application of the above theorem we can conclude the equivalence of the Additive Sumset Approximation problem to 3-SUM, together with Theorem 10.

\(\blacktriangleright\) **Lemma 29** (Additive Sumset Approximation \(\le_2\) 3-SUM)**.** _If the_ 3_-SUM problem can be solved in randomized time_ \(O(n^{2-\epsilon})\) _for an_ \(\epsilon>0\) _then Additive Sumset Approximation problem can be solved in randomized time_ \(O(n^{2-\epsilon^\prime})\) _for an_ \(\epsilon'>0\).

## 7 Application: A lower bound on the computation of Pareto Sums

In the following, we explore how the 3-SUM hardness of Verification of Pareto Sum translates to a hardness result for the problem of computing Pareto Sums. Let us first justify the naming of the Verification of Pareto Sum problem, by showing it to be subquadratic equivalent to the more natural extended version of Verification of Pareto Sum. Throughout this section, we consider dimensions \(d\ge 2\).

\(\blacktriangleright\) **Definition 30** (Verification of Pareto Sum (Extended version))**.** _Given sets_ \(A,B,C\subseteq\mathbb{Z}^d\)_, do the following properties hold simultaneously:_

_(Inclusion):_ \(C\subseteq A+B\),

_(Dominance): C dominates A+B. More formally, for every_ \(a\in A,b\in B\) _there exists_ \(c\in C\) _with_ \(c\ge a+b\).

_(Minimality): There are no_ \(c,c'\in C\) _with_ \(c\neq c'\) _and_ \(c\le c'\).

We make use of the following lemma and its construction for the results in this section.

\(\blacktriangleright\) **Lemma 31.** _Given sets_ \(A,B,C\subseteq\mathbb{Z}^d\) _of size at most n, one can construct sets_ \(\tilde{A},\tilde{B},\tilde{C}\subseteq\mathbb{Z}^d\) _of size_ \(\Theta(n)\) _in time_ \(\tilde{O}(n)\) _such that (1)_ \(\tilde{A},\tilde{B},\tilde{C}\) _always satisfy the minimality and inclusion condition and (2)_ \(\tilde{A},\tilde{B},\tilde{C}\) _fulfill the dominance condition if and only if A,B,C fulfill the dominance condition._

Due to space constraints, the proof had to be deferred to the full version. Using this construction, it is not difficult to obtain the following equivalence.

\(\blacktriangleright\) **Lemma 32.** _There is an_ \(O(n^{2-\epsilon})\) _time algorithm for an_ \(\epsilon>0\) _for Verification of Pareto Sum (Extended Version) if and only if there is an_ \(O(n^{2-\epsilon^\prime})\) _time algorithm for an_ \(\epsilon'>0\) _for Verification of Pareto Sum._


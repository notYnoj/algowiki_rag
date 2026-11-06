Thus, to obtain Theorem 2, we show a fine-grained equivalence of Multiset #_k_-SUM and #_k_-SUM, for all odd \(k\ge 3\). This fine-grained equivalence, which we prove via a heavy- light approach, might be of independent interest.<sup>17</sup> Combining this equivalence with an inclusion-exclusion argument, we may thus lift Theorem 1 to a counting version for all odd \(k\ge 3\).

In the reductions below, we will make crucial use of the immediate corollary of Theorem 2 and [22] that for each \(\mathsf{FOP}_\mathbb{Z}(\exists\exists\exists)\) formula \(\phi\), there exists a subquadratic reduction from counting witnesses for \(\phi\) to 3-SUM (Corollary 3).

## On general quantifier structures

We perform a systematic study on the different quantifier structures for _k_=3. Due to simple negation arguments, we only have to perform a systematic study on the classes of problems \(\mathsf{FOP}_\mathbb{Z}(\exists\exists\exists)\), \(\mathsf{FOP}_\mathbb{Z}(\forall\exists\exists)\), \(\mathsf{FOP}_\mathbb{Z}(\forall\forall\exists)\), \(\mathsf{FOP}_\mathbb{Z}(\exists\forall\exists)\).

First, we state a simple lemma establishing syntactic complete problems for the classes above.

\(\blacktriangleright\) **Lemma 8** (Syntactic Complete problems (Informal Version))**.** _Let_ \(Q_1,Q_2\in\{\exists,\forall\}\)_. We can reduce every formula of the class_ \(\mathsf{FOP}_\mathbb{Z}(Q_1Q_2\exists)\) _to the formula_

\(Q_1\tilde{a}_1\in\tilde{A}_1Q_2\tilde{a}_2\in\tilde{A}_2\exists\tilde{a}_3\in\tilde{A}_3:\tilde{a}_1+\tilde{a}_2\le\tilde{a}_3.\)

## On the quantifier change \(\mathsf{FOP}_\mathbb{Z}(\forall\exists\exists)\rightarrow\mathsf{FOP}_\mathbb{Z}(\exists\exists\exists)\).

We rely on the subquadratic equivalence between 3-SUM and a functional version of 3-SUM called All-ints 3-SUM, which asks to determine for every \(a\in A\) whether there is a solution involving _a_. A randomized subquadratic equivalence was given in [51], which can be turned deterministic [42].

This equivalence allows us to use the bit-level trick to turn inequalities to equalities, despite it seemingly not interacting well with the quantifier structure \(\forall\exists\exists\) at first sight. This results in a proof of the following hardness result.

\(\blacktriangleright\) **Lemma 9.** _If_ 3_-SUM can be solved in time_ \(O(n^{2-\epsilon})\) _for an_ \(\epsilon>0\)_, then all problems P of_ \(\mathsf{FOP}_\mathbb{Z}(\forall\exists\exists)\) _can be solved in time_ \(O(n^{2-\epsilon P})\) _for an_ \(\epsilon P>0\).

## On the quantifier change \(\mathsf{FOP}_\mathbb{Z}(\exists\exists\exists)\rightarrow\mathsf{FOP}_\mathbb{Z}(\forall\forall\exists)\).

As a first result for the class \(\mathsf{FOP}_\mathbb{Z}(\forall\forall\exists)\), we are able to show equivalence to 3-SUM for a specific problem in this class, thus introducing a 3-SUM equivalent problem with a different quantifier structure in comparison to 3-SUM. Specifically, we consider the problem of verifying additive _t_-approximation of sumsets. We are able to precisely characterize the fine-grained complexity depending on _t_.

Formally, we show the following theorem.

\(\blacktriangleright\) **Theorem 10.** _Consider the Additive Sumset Approximation problem of deciding, given_ \(A,B,C\subseteq\mathbb{Z},t\in\mathbb{Z}\)_, whether_

\(A+B\subseteq C+\{0,\dots,t\}.\)

<sup>17</sup>We remark that it is plausible that the proof of the subquadratic equivalence of 3-SUM and #3-SUM due to Chan et al. [22] could be extended to establish subquadratic equivalence with Multiset #3-SUM as well. Note, however, that a fine-grained equivalence of #_k_-SUM and _k_-SUM is not known for any \(k\ge 4\).


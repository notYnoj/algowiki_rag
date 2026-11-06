After applying Lemma 13, it remains to reduce a conjunction of equality checks to _k_-SUM. To do so, we interpret the conjunction of equalities as a Vector _k_-SUM problem, which can be reduced to _k_-SUM in a straightforward way [5].

## 4 On counting witnesses in FOP<sub>Z</sub>

In this section, we show reductions from counting witnesses of \(\mathsf{FOP}_\mathbb{Z}(\exists^k)\) formulas to #_k_- SUM, specifically, we prove Theorem 2. To do so, we adapt the proof of Theorem 1 given in Section 3 to a counting version. As discussed in Section 2, this requires us to work with a multiset version of #_k_-SUM. Handling multisets is thus the main challenge addressed in this section. Formally, we say that a multiset is a set _A_ together with a function \(f:A\rightarrow\mathbb{N}\). For \(a\in A\), we abbreviate _na_:=_f(a_) as the multiplicity of _a_. To measure multiset sizes, we still think of each _a_ to have _na_ copies in the input, i.e. the size of _A_ is \(\sum_{a\in A}n_a\). Almost all proofs in this section are deferred to the full version of the paper.

\(\blacktriangleright\) **Definition 14** ((_U,d_)-vector Multiset #_k_-SUM)**.** _Let X_:={-_U,...,U}<sup>d</sup>. Given k multisets_ \(A_1,\dots,A_k\subseteq X\) _and_ \(t\in X\)_, we ask for the total number of k-SUM witnesses, that is_

\(\sum_{a_1+\cdots+a_k=t,a_1\in A_1,\dots,a_k\in A_k}\prod_{i=1}^kn_{a_i}.\)

Furthermore, define Multiset #_k_-SUM as (_U,_1)-vector Multiset #_k_-SUM and _M_-multiplicity #_k_-SUM as Multiset #_k_-SUM with the additional restriction that the multiplicity of each element is limited, that is for all \(a\in A_1\cup\cdots\cup A_k:na\le M\) holds. Lastly, #_k_-SUM is defined as 1-Multiplicity #_k_-SUM and (_U,d_)-vector #_k_-SUM is (_U,d_)-vector Multiset #_k_-SUM where for all \(a\in A_1\cup\cdots\cup A_k:na=1\) holds.

For the case of \(\mathsf{FOP}_\mathbb{Z}^3\) we will also introduce the #All-ints version of the above problems, which asks to determine, for each \(a_1\in A_1\), the number of witnesses involving _a_<sub>1</sub>.

The (deferred) proof of the following lemma is analogous to the proof of Abboud et al. [5] to reduce Vector _k_-SUM to _k_-SUM.

\(\blacktriangleright\) **Lemma 15** ((_U,d_)-vector Multiset #_k_-SUM \(\le_{\lceil k/2\rceil}\) Multiset #_k_-SUM)**.** _If Multiset #k- SUM can be solved in time T(n_) _then_ (_U,d)-vector Multiset #k-SUM can be solved in time O(nd_log(_U_)+_T(n_)).

Next, we give a simple approach to solve Multiset #_k_-SUM when all multiplicities are comparably small.

\(\blacktriangleright\) **Lemma 16** (_M_-multiplicity #_k_-SUM\(\le_{\lceil k/2\rceil}\) #_k_-SUM)**.** _If #k-SUM can be solved in time T(n), then M-multiplicity #k-SUM can be solved in time_ \(\tilde{O}(T(nM^{k-1}))\).

For later purposes, we will need the following version of the above lemma.

\(\blacktriangleright\) **Observation 17.** _If #All-ints_ 3_-SUM can be solved in time T(n), then we can solve #All-ints M-multiplicity_ 3_-SUM in time_ \(\tilde{O}(T(nM^2))\).

We can finally prove the main result of this section.

\(\blacktriangleright\) **Lemma 18.** _For odd_ \(k\ge 3\)_, if there exists an algorithm for the #k-SUM problem running in time_ \(O(n^{\lceil k/2\rceil-\epsilon})\) _for an_ \(\epsilon>0\)_, then there exists an algorithm for the Multiset #k-SUM problem running in time_ \(O(n^{\lceil k/2\rceil-\epsilon^\prime})\) _for an_ \(\epsilon'>0\).


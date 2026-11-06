Perhaps surprisingly in light of its generality and applicability, Theorem 1 is obtained via a very simple, deterministic reduction that combines the tricks from [5, 52]. This generality comes at the cost of polylogarithmic factors (which we do not optimize), which depend on the number of inequalities occurring in the considered formula; for the details see Section 3 and the full version of the paper.

## 1.2.2 Completeness for counting witnesses

We provide a certain extension of the above completeness result to the problem class of _counting_ witnesses to existential FOP<sub>Z</sub> formulas<sup>8</sup>. Counting witnesses is an important task particularly in database applications (usually referred to as model counting). Furthermore, we will make use of witness counting to _decide_ certain quantified formulas in subsequent results detailed below. In Section 4, we will obtain the following result.

\(\blacktriangleright\) **Theorem 2.** _Let_ \(k\ge 3\) _be odd. If there is_ \(\epsilon>0\) _such that we can count the number of witnesses for k-SUM in time_ \(O(n^{\lceil k/2\rceil-\epsilon})\)_, then for all problem P in_ \(\mathsf{FOP}_\mathbb{Z}(\exists k)\)_, there is some_ \(\epsilon'>0\) _such that we can count the number of witnesses for P in time_ \(O(n^{\lceil k/2\rceil-\epsilon^\prime})\).

Leveraging the recent breakthrough by [22] that 3-SUM is subquadratic equivalent to counting witnesses of 3-SUM, we obtain the corollary that _3-SUM is hard even for counting witnesses of_ \(\mathsf{FOP}_\mathbb{Z}(\exists^3)\).

\(\blacktriangleright\) **Corollary 3.** _For all problems P in_ \(\mathsf{FOP}_\mathbb{Z}(\exists^3)\)_, there is some_ \(\epsilon_P>0\) _such that we can count the number of witnesses for P in randomized time_ \(O(n^{2-\epsilon_P})\) _if and only if there is some_ \(\epsilon'>0\) _such that_ 3_-SUM can be solved in randomized time_ \(O(n^{2-\epsilon^\prime})\).

## 1.2.3 Completeness for general quantifier structures of FOP<sub>Z</sub>

In light of our first completeness result, one might wonder whether _k_-SUM is complete for deciding all _k_-quantifier formulas in FOP<sub>Z</sub>, regardless of the quantifier structure of the formulas. Note that for these general quantifier structures, a baseline algorithm with running time \(\tilde{O}(n^{k-1})\) can be achieved with a combination of brute-force and orthogonal range queries; see the full version for details.

However, by [7, Theorem 15] there exists a \(\mathsf{FOP}_\mathbb{Z}(\exists^{k-1}\forall)\)-formula \(\phi\) that cannot be solved in time \(O(n^{k-1-\epsilon})\)-time unless the 3-uniform hyperclique hypothesis is false (see the discussion in Section 1.3). Thus, proving that 3-SUM is complete for all 3-quantifier formulas would establish that the 3-uniform hyperclique hypothesis implies the 3-SUM hypothesis - this would be a novel tight reduction among important problems/hypotheses in fine-grained complexity theory. For \(k\ge 4\), it becomes even more intricate: the conditionally optimal running time of \(n^{k-1\pm o(1)}\) for \(\mathsf{FOP}_\mathbb{Z}(\exists^k\forall)\) formulas exceeds the conditionally optimal running time of \(n^{\lceil\frac{k}{2}\rceil\pm o(1)}\) for \(\mathsf{FOP}_\mathbb{Z}(\exists^k)\) formulas.

We are nevertheless able to obtain a completeness result for general quantifier structures: Specifically, we show that if two geometric problems over Z_<sup>d</sup>_ can be solved in time \(O(n^{2-\epsilon_d})\) where \(\epsilon_d>0\) for all _d_, then each _k_-quantifier formula in FOP<sub>Z</sub> can be decided in time \(O(n^{k-1-\epsilon})\) for some \(\epsilon>0\). These problems are (1) a variation of the Hausdorff distance that we call _Hausdorff distance under n Translations_ and (2) the Pareto Sum problem; the details are covered in Section 5.

<sup>8</sup> A witness for a \(\mathsf{FOP}_\mathbb{Z}(\exists^k)\) formula \(\exists a_1\in A_1\dots\exists a_k\in A_k:\varphi\) with \(\hat{t}_1,\dots,\hat{t}_l\in\mathbb{Z}\) is a tuple \((a_1,\dots,a_k)\in A_1\times\cdots\times A_k\) that satisfies the formula \(\varphi[(t_1,\dots,t_l)\backslash(\hat{t}_1,\dots,\hat{t}_l)]\).


to establish the highest _d_ such that 3-SUM is complete for FOP<sub>Z</sub> formulas of inequality dimension at most _d_; for a discussion see Section 8.

## Further Applications

As an immediate application of our first completeness theorem, we obtain a simple proof of a _n_<sup>4/3-_o_(1)</sup> lower bound for the 4-SUM problem based on the the 3-uniform hyperclique hypothesis; see the full version of the paper for details. Specifically, by Theorem 1, it suffices to model the 3-uniform 4-hyperclique problem as a problem in \(\mathsf{FOP}_\mathbb{Z}(\exists\exists\exists\exists)\). The resulting conditional lower bound is implicitly known in the literature, as it can alternatively be obtained by combining a 3-uniform hyperclique lower bound for 4-cycle given in [43] with a folklore reduction from 4-cycle to 4-SUM (see [39] for a deterministic reduction from 3-cycle to 3-SUM).

\(\blacktriangleright\) **Theorem 6.** _If there is some_ \(\epsilon>0\) _such that 4-SUM can be solved in time_ \(O(n^{\frac{4}{3}-\epsilon})\)_, then the 3-uniform hyperclique hypothesis fails._

Similarly, we can also give a simple proof for a known lower bound for 3-SUM.

Another application of our results is to establish class-based conditional bounds. As a case in point, consider the problem of computing the Pareto sum of \(A,B\subseteq\mathbb{Z}^d\): Clearly, this problem can be solved in time \(\tilde{O}(n^2)\) by explicitly computing the sumset _A+B_ and computing the Pareto front using any algorithm running in near-linear time in its input, e.g. [34]. We prove the following conditional optimality results already in the case when the desired output (the Pareto sum of _A,B_) has size \(\Theta(n)\).

\(\blacktriangleright\) **Theorem 7** (Pareto Sum Computation Lower Bound)**.** _The following conditional lower bounds hold for output-sensitive Pareto sum computation:_

**1.** _If there is_ \(\epsilon>0\) _such that we can compute the Pareto sum C of_ \(A,B\subseteq\mathbb{Z}^2\)_, whenever C is of size_ \(\Theta(n)\)_, in time_ \(O(n^{2-\epsilon})\)_, then the_ 3_-SUM hypothesis fails (thus, for any_ \(\mathsf{FOP}_\mathbb{Z}^k\) _formula_ \(\phi\) _of inequality dimension at most 3, there is_ \(\epsilon'>0\) _such that_ \(\phi\) _can be decided in time_ \(O(n^{k-1-\epsilon^\prime}))\).

**2.** _If for all_ \(d\ge 2\)_, there is_ \(\epsilon>0\) _such that we can compute the Pareto sum C of_ \(A,B\subseteq\mathbb{Z}^d\)_, whenever C is of size_ \(\Theta(n)\)_, in time_ \(O(n^{2-\epsilon})\)_, then there is some_ \(\epsilon'>0\) _such that we can decide all_ FOP<sub>Z</sub> _formulas with k quantifiers not ending in_ \(\exists\forall\exists\) _or_ \(\forall\exists\forall\) _in time_ \(O(n^{k-1-\epsilon^\prime})\).

Our lower bound for 2D strengthens a quadratic-time lower bound found by Funke et al. [33] based on the (min,+)-convolution hypothesis to hold already under the weaker (i.e., more believable) 3-SUM hypothesis. For higher dimensions, we furthermore strengthen the conditional lower bound via its connection to FOP<sub>Z</sub>.

We conclude with remaining open questions in Section 8.

## 1.3 Further Related Work

To our knowledge, the first investigation of the connection between classes of model-checking problems and central problems in fine-grained complexity was given by Williams [49], who shows that the _k_-clique problem is complete for the class of existentially-quantified first order graph properties, among other results. As important follow-up work, Gao et al. [36] establish OV as complete problem for model-checking any first-order property.

Subsequent results include classification results for \(\exists^k\forall\)-quantified first-order graph properties [14], fine-grained upper and lower bounds for counting witnesses of first-order properties [28], completeness theorems for multidimensional ordering properties [7] (discussed


The proof can be found in the full version. Thus, for subquadratic reductions, we can restrict ourselves to the Verification of Pareto Sum problem, which essentially only checks the dominance condition.

Let us now consider the natural problem of computing the Pareto Sum.

\(\blacktriangleright\) **Definition 33 (Pareto Sum).** _Given sets_ \(A,B\subseteq\mathbb{Z}^d\)_, compute a set_ \(C\subseteq\mathbb{Z}\)_, such that A,B,C satisfy the Inclusion, Dominance and Minimality condition._

In the following, we argue why the lower bounds to Verification of Pareto Sum translate to lower bounds to Computation of the Pareto Sum. Formally, we prove:

\(\blacktriangleright\) **Lemma 34.** _If there is an algorithm to compute the Pareto Sum C of sets_ \(A,B\subseteq\mathbb{Z}^d\) _in time_ \(O(n^{2-\epsilon})\) _for an_ \(\epsilon>0\) _even when_ \(C=\Theta(n)\)_, then one can also decide Verification of Pareto Sum of sets A,B,C in time_ \(O(n^{2-\epsilon^\prime})\) _for an_ \(\epsilon'>0\).

We conclude this section with our resulting hardness results for computing Pareto Sums.

\(\blacktriangleright\) **Theorem 7 (Pareto Sum Computation Lower Bound).** _The following conditional lower bounds hold for output-sensitive Pareto sum computation:_

**1.** _If there is_ \(\epsilon>0\) _such that we can compute the Pareto sum C of_ \(A,B\subseteq\mathbb{Z}^2\)_, whenever C is of size_ \(\Theta(n)\)_, in time_ \(O(n^{2-\epsilon})\)_, then the_ 3_-SUM hypothesis fails (thus, for any_ \(\mathsf{FOP}_\mathbb{Z}^k\) _formula_ \(\phi\) _of inequality dimension at most 3, there is_ \(\epsilon'>0\) _such that_ \(\phi\) _can be decided in time_ \(O(n^{k-1-\epsilon^\prime}))\).

**2.** _If for all_ \(d\ge 2\)_, there is_ \(\epsilon>0\) _such that we can compute the Pareto sum C of_ \(A,B\subseteq\mathbb{Z}^d\)_, whenever C is of size_ \(\Theta(n)\)_, in time_ \(O(n^{2-\epsilon})\)_, then there is some_ \(\epsilon'>0\) _such that we can decide all_ FOP<sub>Z</sub> _formulas with k quantifiers not ending in_ \(\exists\forall\exists\) _or_ \(\forall\exists\forall\) _in time_ \(O(n^{k-1-\epsilon^\prime})\).

## 8 Future Work

While we exhibit a pair of problems that is complete for the class FOP<sub>Z</sub>, one could still ask whether there is a subquadratic reduction from Hausdorff distance under _n_ Translations to Verification of Pareto Sum. As a result there would be a single complete problem (or rather the canonical multidimensional family of a single geometric problem) for FOP<sub>Z</sub>.

_Is Verification of Pareto Sum complete for the class_ FOP<sub>Z</sub>?

Interestingly, previous completeness theorems [36] were able to establish a problem of quantifier structure \(\forall\forall\exists\) (the Orthogonal Vectors problem) as complete by making use of a technique in [51] that was originally used to show subcubic equivalence between All-Pairs Negative Triangle and Negative Triangle. However, a major problem we encounter is that while the third quantifier in the Orthogonal Vectors problem ranges over a sparse (intuitively: subpolynomially sized) domain (i.e., the dimensions of the vectors), the third quantifier in Pareto Sum Verification ranges over a linearly sized domain (i.e., the set _C_).

Finally, we ask if our 3-SUM completeness result for arbitrary quantifier structures can be improved upon.

_Can we establish a d\>_3 _such that_ 3_-SUM is complete for_ FOP<sub>Z</sub> _formulas of inequality dimension at most d?_


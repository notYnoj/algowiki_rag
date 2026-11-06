\(\blacktriangleright\) **Theorem 10.** _Consider the Additive Sumset Approximation problem of deciding, given_ \(A,B,C\subseteq\mathbb{Z},t\in\mathbb{Z}\)_, whether_

\(A+B\subseteq C+\{0,\dots,t\}.\)

_This problem is_

_solvable in time_ \(O(n^{2-\delta})\) _with_ \(\delta>0\)_, whenever_ \(t=O(n^{1-\epsilon})\) _for any_ \(\epsilon>0\),

_not solvable in time_ \(O(n^{2-\epsilon})\)_, whenever_ \(t=\Omega(n)\) _assuming the Strong_ 3_-SUM hypothesis. Furthermore, subquadratic hardness holds under the standard 3-SUM Hypothesis if no restriction on t is made._

The proof is deferred to the full version of the paper.

## 5.3 Completeness results for the class \(\mathsf{FOP}_\mathbb{Z}^k\)

We turn to combining the above insights to establish (a pair of) complete problems for the class FOP<sub>Z</sub>. The proofs in this section are deferred to the full version of the paper.

\(\blacktriangleright\) **Lemma 11.** _There is a function_ \(\epsilon(d)>0\) _such that the Verification of Pareto Sum problem can be solved in time_ \(O(n^{2-\epsilon(d)})\) _if and only if all problems P in the classes_

\(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\exists\exists\exists),\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\forall\forall\forall),\)

\(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\forall\exists\exists),\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\exists\forall\forall),\)

\(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\forall\forall\exists),\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\exists\forall),\)

_where_ \(Q_1,\dots Q_{k-3}\in\{\exists,\forall\}\) _and_ \(k\ge 3\)_, can be solved in time_ \(O(n^{k-1-\epsilon_P})\) _for an_ \(\epsilon_P>0\).

\(\blacktriangleright\) **Lemma 12.** _There is a function_ \(\epsilon(d)>0\) _such that the Hausdorff Distance under n Translations problem can be solved in time_ \(O(n^{2-\epsilon(d)})\) _if and only if all problems P in the classes_

\(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\exists\forall\exists),\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\forall\exists\forall),\)

_where_ \(Q_1,\dots Q_{k-3}\in\{\exists,\forall\}\) _and_ \(k\ge 3\)_, can be solved in time_ \(O(n^{k-1-\epsilon_P})\) _for an_ \(\epsilon_P>0\).

We finally obtain our completeness theorem for the whole class \(\mathsf{FOP}_\mathbb{Z}^k\).

\(\blacktriangleright\) **Theorem 4.** _There is a function_ \(\epsilon(d)>0\) _such that both of the following problems can be solved in time_ \(O(n^{2-\epsilon(d)})\)

_Pareto Sum Verification,_

_Hausdorff distance under n Translations,_

_if and only if for each problem P in_ \(\mathsf{FOP}_\mathbb{Z}^k\) _with_ \(k\ge 3\) _there exists an_ \(\epsilon_P>0\) _such that P can be solved in time_ \(O(n^{k-1-\epsilon_P})\).

Essentially, these two problems capture the complexity of the class \(\mathsf{FOP}_\mathbb{Z}^3\) and can be seen as the most important problems in \(\mathsf{FOP}_\mathbb{Z}^k\).

## 6 The 3-SUM problem is complete for FOP<sub>Z</sub> formulas with Inequality Dimension at most 3

In this section, we show that 3-SUM problem captures an interesting subclass of FOP<sub>Z</sub> formulas with arbitrary quantifier structure, namely the formulas of sufficiently small _inequality dimension_. Let us recall the notion of inequality dimension.

\(\blacktriangleright\) **Definition 25** (Inequality Dimension of a )**.** _Let_ \(\phi=Q_1x_1\in A_1,\dots,Q_kx_k\in A_k:\psi\) _be a_ FOP<sub>Z</sub> _formula with_ \(A_i\subseteq\mathbb{Z}^{d_i}\).

_The_ inequality dimension _of_ \(\phi\) _is the smallest number s such that there exists a Boolean function_ \(\psi':\{0,1\}^s\rightarrow\{0,1\}\) _and (strict or non-strict) linear inequalities L_<sub>1</sub>_,...,L<sub>s</sub> in the_


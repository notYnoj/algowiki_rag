\(\blacktriangleright\) **Definition 20** (Verification of _d_-dimensional Pareto Sum)**.** _Given sets_ \(A,B,C\subseteq\mathbb{Z}^d\)_. Does the set C dominate A+B, that is does for all_ \(a\in A,b\in B\) _exist a_ \(c\in C\)_, with_ \(c\ge a+b\) ?

It is easy to see that Verification of _d_-dimensional Pareto Sum is in \(\mathsf{FOP}_\mathbb{Z}(\forall\exists)\).

\(\blacktriangleright\) **Definition 21** (Hausdorff Distance under _n_ Translations)**.** _Given sets_ \(A,B,C\subseteq\mathbb{Z}^d\) _with at most n elements and a_ \(\gamma\in\mathbb{N}\)_, the Hausdorff distance under n Translations problem asks whether the following holds:_

\(\delta_H^{T(A)}(B,C):=min_{\tau\in A}\delta_H\overrightarrow{H}(B,C+\{\tau\})=min_{\tau\in A}max_{b\in B}min_{c\in C}\|b-(c+\tau)\|_\infty\le\gamma.\)

We show the following result firstly, which allows us to assume without loss of generality a certain normal form.

\(\blacktriangleright\) **Lemma 22.** _A general_ \(\mathsf{FOP}_\mathbb{Z}(Q_1Q_2\exists)\) _formula, with input set_ \(A_1\subseteq\mathbb{Z}^{d_1},A_2\subseteq\mathbb{Z}^{d_2},A_3\subseteq\mathbb{Z}^{d_3}\)_, where_ |_A_<sub>1</sub>|=|_A_<sub>2</sub>|=|_A_<sub>3</sub>|=_n, can be reduced to the_ \(\mathsf{FOP}_\mathbb{Z}(Q_1Q_2\exists)\) _formula_

\(Q_1a'_1\in A'_1Q_2a'_2\in A'_2\exists a'_3\in A'_3:a'_1+a'_2\le a'_3\)

_in time O(n), where_ \(|A'_1|=|A'_2|=n\) _and_ \(|A'_3|=O(n)\).

The above lemma immediately gives us complete syntactic problems for our classes. It remains to establish connections between the different quantifier structure classes, and explore natural variants of the syntactic problems.

The syntactic complete problem for the class \(\mathsf{FOP}_\mathbb{Z}(\exists\forall\exists)\) turns out to be equivalent to Hausdorff Distance under _n_ Translations. We obtain:

\(\blacktriangleright\) **Lemma 23** (Hausdorff Distance under _n_ Translations is complete for \(\mathsf{FOP}_\mathbb{Z}(\exists\forall\exists)\))**.** _There is a function_ \(\epsilon(d)>0\) _such that Hausdorff Distance under n Translations can be solved in time_ \(O(n^{2-\epsilon(d)})\) _if and only if all problems P in_ \(\mathsf{FOP}_\mathbb{Z}(\exists\forall\exists)\) _can be solved in time_ \(O(n^{2-\epsilon_P})\) _for an_ \(\epsilon_P>0\).

Similarly, the Verification of Pareto Sum problem is complete for the class \(\mathsf{FOP}_\mathbb{Z}(\forall\exists)\).

\(\blacktriangleright\) **Lemma 24** (Verification of Pareto Sum is complete for \(\mathsf{FOP}_\mathbb{Z}(\forall\exists)\))**.** _There is a function_ \(\epsilon(d)>0\) _such that Verification of Pareto Sum can be solved in time_ \(O(n^{2-\epsilon(d)})\) _if and only if all problems P in_ \(\mathsf{FOP}_\mathbb{Z}(\forall\exists)\) _can be solved in time_ \(O(n^{2-\epsilon_P})\) _for an_ \(\epsilon_P>0\).

## 5.1 \(\mathsf{FOP}_\mathbb{Z}(\forall\exists\exists)\rightarrow\mathsf{FOP}_\mathbb{Z}(\exists\exists\exists)\)

We continue with handling the class \(\mathsf{FOP}_\mathbb{Z}(\forall\exists\exists)\). By simply making use of Corollary 19, one can easily prove that 3-SUM is hard for the class \(\mathsf{FOP}_\mathbb{Z}(\forall\exists\exists)\). We can also show a deterministic proof, as Corollary 19 makes use of the subquadratic equivalence between 3-SUM and #All-ints 3-SUM, which relies on randomization techniques.

\(\blacktriangleright\) **Lemma 9.** _If_ 3_-SUM can be solved in time_ \(O(n^{2-\epsilon})\) _for an_ \(\epsilon>0\)_, then all problems P of_ \(\mathsf{FOP}_\mathbb{Z}(\forall\exists\exists)\) _can be solved in time_ \(O(n^{2-\epsilon_P})\) _for an_ \(\epsilon_P>0\).

## 5.2 \(\mathsf{FOP}_\mathbb{Z}(\exists\exists\exists)\rightarrow\mathsf{FOP}_\mathbb{Z}(\forall\exists\exists)\)

We explore the connection between the problem Additive Sumset Approximation, which is a member of the class \(\mathsf{FOP}_\mathbb{Z}(\forall\exists\exists)\), and the 3-SUM problem. The following theorem will play a key role to enable the discovery of the relationship between 3-SUM and other quantifier structures.


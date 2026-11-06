_This problem is_

_solvable in time_ \(O(n^{2-\delta})\) _with_ \(\delta>0\)_, whenever_ \(t=O(n^{1-\epsilon})\) _for any_ \(\epsilon>0\),

_not solvable in time_ \(O(n^{2-\epsilon})\)_, whenever_ \(t=\Omega(n)\) _assuming the Strong_ 3_-SUM hypothesis. Furthermore, subquadratic hardness holds under the standard 3-SUM Hypothesis if no restriction on t is made._

The above theorem is essentially enabling a quantifier change transforming the \(\exists\exists\exists\) quantifier structure for which 3-SUM is complete into a subquadratic equivalent problem with a quantifier structure \(\forall\forall\exists\). Moreover, the 3-SUM hardness is a witness to the hardness of the class \(\mathsf{FOP}_\mathbb{Z}(\forall\forall\exists)\).

Let us remark a few interesting aspects: The algorithmic part follows from sparse convolution techniques going back to Cole and Hariharan [26], see [16] for a recent account and also [20, 17, 15]. Specifically, whenever \(t=O(n^{1-\epsilon})\), it holds that \(|C+\{0,\dots,t\}|=O(n^{2-\epsilon})\) and intuitively, we can use an output-sensitive convolution algorithm to compute _A+B_ and compare it to _C_+{0_,...,t_}.<sup>18</sup> Our result indicates that an explicit construction of _C_+{0_,...,t_} is required, since once it may get as large as \(\Omega(n^2)\), we obtain a _n_<sup>2-_o_(1)</sup>-time lower bound assuming the Strong 3-SUM Hypothesis.

The lower bound follows from describing the 3-SUM problem alternatively as \((A+B)\cap C\neq\emptyset\), which is equivalent to the negation of \((A+B)\subseteq\bar{C}\), where \(\bar{C}\) denotes the complement of _C_. Thus, we aim to cover the complement of _C_ by intervals of length _t_. While this appears impossible for 3-SUM, we employ the subquadratic equivalence of 3-SUM and its convolutional version due to Patrascu [46]. This problem will deliver us the necessary structure to represent this complement with the addition of few auxilliary points.

The reverse reduction from Additive Sumset Approximation to 3-SUM follows from Theorem 5 (as Additive Sumset Approximation has inequality dimension 2).

## On completeness results for \(\mathsf{FOP}_\mathbb{Z}^k\)

The above ingredients establish our completeness theorems by exhaustive search over remaining quantifiers. Specifically, by a combination of Theorem 10, which shows that Additive Sumset Approximation is 3-SUM hard, and a combination of Lemma 9 and Theorem 1, we get:

\(\blacktriangleright\) **Lemma 11.** _There is a function_ \(\epsilon(d)>0\) _such that the Verification of Pareto Sum problem can be solved in time_ \(O(n^{2-\epsilon(d)})\) _if and only if all problems P in the classes_

_where_ \(Q_1,\dots Q_{k-3}\in\{\exists,\forall\}\) _and_ \(k\ge 3\)_, can be solved in time_ \(O(n^{k-1-\epsilon_P})\) _for an_ \(\epsilon_P>0\).

Similarly, for quantifier structures ending in \(\exists\forall\exists\) and \(\forall\exists\forall\), we obtain the following completeness result.

\(\blacktriangleright\) **Lemma 12.** _There is a function_ \(\epsilon(d)>0\) _such that the Hausdorff Distance under n Translations problem can be solved in time_ \(O(n^{2-\epsilon(d)})\) _if and only if all problems P in the classes_

<sup>18</sup>The argument is slightly more subtle, since we need to avoid computing _A+B_ if its size exceeds \(O(n^{2-\epsilon})\).

\begin{tabular}{cc}
\(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\exists\exists\exists)\), & \(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\forall\forall\forall\forall)\), \\ \(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\forall\exists\exists)\), & \(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\exists\forall\forall)\), \\ \(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\forall\forall\exists)\), & \(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\exists\exists\forall)\), \\ \end{tabular}

\begin{tabular}{cc}
\(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\exists\forall\exists)\), & \(\mathsf{FOP}_\mathbb{Z}(Q_1\dots Q_{k-3}\forall\exists\forall)\), \\ \end{tabular}


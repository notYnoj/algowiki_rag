# Completeness Theorems for _k_-SUM and Geometric Friends: Deciding Fragments of Linear Integer Arithmetic

**Geri Gokaj** \(\includegraphics{}\) **Karlsruhe Institute of Technology, Karlsruhe, Germany**

**Marvin Künnemann** \(\includegraphics{}\) **Karlsruhe Institute of Technology, Karlsruhe, Germany**

**Abstract**

In the last three decades, the _k_-SUM hypothesis has emerged as a satisfying explanation of long- standing time barriers for a variety of algorithmic problems. Yet to this day, the literature knows of only few proven consequences of a refutation of this hypothesis. Taking a descriptive complexity viewpoint, we ask: What is the largest logically defined class of problems _captured_ by the _k_-SUM problem?

To this end, we introduce a class FOP<sub>Z</sub> of problems corresponding to deciding sentences in Presburger arithmetic/linear integer arithmetic over finite subsets of integers. We establish two large fragments for which the _k_-SUM problem is complete under fine-grained reductions:

1. The _k_-SUM problem is complete for deciding the sentences with _k_ existential quantifiers.

2. The 3-SUM problem is complete for all 3-quantifier sentences of FOP<sub>Z</sub> expressible using at most 3 linear inequalities.

Specifically, a faster-than-\(n^{[k/2]\pm o(1)}\) algorithm for _k_-SUM (or faster-than-\(n^{2\pm o(1)}\) algorithm for 3- SUM, respectively) directly translate to polynomial speedups of a general algorithm for _all_ sentences in the respective fragment.

Observing a barrier for proving completeness of 3-SUM for the entire class FOP<sub>Z</sub>, we turn to the question which other – seemingly more general – problems are complete for FOP<sub>Z</sub>. In this direction, we establish FOP<sub>Z</sub>-completeness of the _problem pair_ of Pareto Sum Verification and Hausdorff Distance under _n_ Translations under the \(L_\infty/L_1\) norm in Z_<sup>d</sup>_. In particular, our results invite to investigate Pareto Sum Verification as a high-dimensional generalization of 3-SUM.

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Computational complexity and cryptography \(\rightarrow\) Complexity theory and logic

**Keywords and phrases** fine-grained complexity theory, descriptive complexity, presburger arithmetic, completeness results, k-SUM

Funding This research is supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) - 462679611.

**Acknowledgements** The authors like to thank the reviewers for constructive feedback as well as Karl Bringmann and Nick Fischer for helpful discussions.

### 1 Introduction

Consider a basic question in complexity theory: How can we determine for which problems an essentially quadratic-time algorithm is best possible? If a given problem _A_ admits an algorithm running in _n_<sup>2+_o_(1)</sup> time, and it is known that _A_ cannot be solved in time \(O(n^{2-\epsilon})\) for any \(\epsilon>0\), then clearly the _n_<sup>2+_o_(1)</sup> algorithm has _optimal_ runtime, up to subpolynomial factors. This question can be asked more generally for any \(k\ge 1\) and time \(n^{k\pm o(1)}\). To this day, the theoretical computer science community is far from able to resolve this question unconditionally. However, a surge of results over recent years uses conditional lower bounds based on plausible hardness assumptions to shed some light on why some problems seemingly




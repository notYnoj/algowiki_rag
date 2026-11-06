## 4.3 Application to Many-to-One Matchings

Next we show a simple instantiation of our coordination mechanism for linearly separable convex programs to give a coordination complexity upper bound for many-to-one matchings. First, let’s consider the following linear program formulation of the matching problem.

\(max_x\sum_{i=1}^n\sum_{j=1}^kv_{i,j}x_{i,j}\) (2)

\(\text{subject to}\sum_{i=1}^nx_{i,j}\le b_j\text{for}j=1,\dots,k\) (3)

\(\sum_{j=1}^kx_{i,j}\le 1\text{for}j=1,\dots,k\) (4)

\(x_{i,j}\ge 0\text{for}i=1,\dots,n\text{and}j=1,\dots,k\) (5)

Observe that the matching linear program is an example of a linearly separable convex program as defined in Definition 3. Each player _i_ has valuation \(v_{i,j}\in\{0,1\}\) for each type of good _j_ and controls the decision variables \(\{x_{i,j}\}_{j=1}^k\). Each supply constraint in Equation (3) corresponds to a coupling constraint, and constraints in both Equation (4) and Equation (5) are personal constraints.

A nice property about the matching linear program is that any extreme point is integral. However, this structure no longer holds if we add a regularization term to the welfare objective, so the resulting solution \(\widehat{x}\) resulting from the coordination mechanism will be fractional. To obtain an integral solution, we can simply use independent rounding, which does not require any further coordination. In order to obtain an integral solution, each player _i_ will take their portion of the fractional solution \((\widehat{x}_{i,j})_{j=1}^k\) and will independently sample a good by selecting each good _j_ with probability \(\widehat{x}_{i,j}\). We will continue to use similar notation: let \(v(\cdot)\) denote the welfare objective in the linear program, let _x_<sup>∗</sup> be the optimal solution for the matching linear program with welfare OPT, \(\widehat{x}\) be the optimal solution for the regularized program with welfare \(\widehat{V}\), \(x'\) be the rounded solution of \(\widehat{x}\), and let F denote the feasible region defined by all the constraints of Equation (3) in the linear program. The following lemma bounds the loss of welfare due to rounding. For details of the proof, see the full version.

**Lemma 8.** _Let_ \(\beta\in(0,1)\)_. Then with probability at least_ \(1-\beta\)_, the rounded solution_ \(x'\) _satisfies_<tbc>

\(v(x')\ge\left(1-\frac{log(2/\beta)}{\sqrt{\widehat{V}}}\right)\widehat{V}\)

<tbc>_Proof._ Since \(\mathbb{E}\left[\sum_{i=1}^n\sum_{j=1}^kx'_{i,j}\right]=\widehat{V}\), by Chernoff-Hoeffding bound, we know that for any \(\delta\in(0,1)\),

\(Pr\left[\sum_{i=1}^n\sum_{j=1}^kx'_{i,j}<(1-\delta)\widehat{V}\right]<exp\left(-\delta^2\widehat{V}/2\right)\)

If we set \(\beta=exp(-\delta^2\widehat{V}/2)\), then we get \(\delta=\sqrt{2log(1/\beta)/\widehat{V}}\), which recovers the stated bound.

Now we look at approximate feasibility of \(x'\).


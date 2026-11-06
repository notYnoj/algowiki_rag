<tbc>**Lemma 9.** _Suppose that_ \(min_{x\in\mathcal{F}}\|x-\widehat{x}\|\le\varepsilon\)_. Then with probability_ \(1-\beta\), \(x'\) _satisfies_

\(\sum_{j=1}^k\left(\sum_{i=1}^nx'_{i,j}-b_j\right)_+\le\sqrt{3klog(k/\beta)\widehat{V}}+\sqrt{nk}\varepsilon\)

Observe that since this is a packing linear program, if desired, it is easy to obtain exact feasibility by simply scaling down the supply constraints: this transfers the approximation factor in the feasibility bound to the become an approximation factor in the objective.

Lastly, we are ready to establish the welfare guarantee for the rounded solution. Since the solution we obtain might slightly violate the feasibility constraints, we want to make sure we are not over-counting. If more than _b<sub>j</sub>_ parties select a particular good of type _j_, we only count the first _b<sub>j</sub>_ parties to select it when measuring our welfare guarantee.

**Theorem 4.** _There exists a coordination protocol with coordination complexity O(k_log(_nk_)) _such that the parties coordinate on a matching_ \(x'\) _with total weight:_

\(\sum_{j=1}^kmin\left\{\sum_{i=1}^nv_{i,j}x'_{i,j},b_j\right\}\ge\left(1-O\left(\frac{\sqrt{k}log(k/\beta)}{\sqrt{OPT}}\right)\right)OPT\)

_as long as_ \(OPT\ge 1\).

Observe that in the setting of many-to-one matchings, when the supply of each good is \(s_j\gg 1\), we expect that \(OPT\gg k\), and hence in this setting, the above theorem guarantees a solution with weight (1-_o_(1))OPT.

**Remark 1.** _We remark that many other combinatorial optimization tasks have fractional relaxations that can be written as linearly separable convex programs, and the same rounding technique can be applied to get low-coordination-complexity protocols for them. This class includes among others multi-commodity flow (where the coordination complexity scales with the number of edges in the underlying graph, but not with the number of parties who wish to route flow) and multi-dimensional knapsack problems (where the coordination complexity scales with the number of different types of knapsack constraints, but not with the number of parties who need to decide on their inclusion in or out of the knapsack)._

## 5 Interface with Privacy and Efficiency in Games

In this section, we explain a simple implication of our results: Problems that have low sensitivity objectives (i.e. problems such that one party’s data and action do not substantially affect the objective value) and low coordination complexity also have good algorithms for solving them subject to _joint differential privacy_. When the strategic variant of the optimization problem is a smooth game, they also have good welfare properties for no-regret players, even when agent types are dynamically changing.

### 5.1 Privacy Background

A _database_ \(D\in\mathcal{X}^n\) is an _n_-tuple of private records, each from one of _n_ agents. Two databases \(D,D'\) are _i-neighbors_ if they differ only in their _i_-th index: that is, if \(D_j=D'_j\) for all \(j\neq i\). If two databases _D_ and \(D'\) are _i_-neighbors for some _i_, we say that they are _neighboring databases_. We write \(D\sim D'\) to denote that _D_ and \(D'\) are neighboring. We will be interested in randomized algorithms that take a database as input, and output an element from some abstract range R.


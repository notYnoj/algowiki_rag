search results in a running time of \(O((\mathrm{deg}(T)!+\mathrm{deg}(T)\cdot d_\mathrm{avg}(T))\cdot n)\), which can be improved to \(O((\mathrm{deg}(T)^22^{\mathrm{deg}(T)}+\mathrm{deg}(T)\cdot d_\mathrm{avg}(T))\cdot n)\) using dynamic programming. The problem is closely related to the classical problem of minimum arc feedback set, and becomes NP-hard without any constraints on the degree. We refer to Section 10 for more details.

## Query complexity.

Rather than running time in the Turing machine model, our focus lies on query complexity in the comparison-query model. There we can only access the ranking \(\rho:X\rightarrow[n]\) via queries of the form: Is \(\rho(x_1)<\rho(x_2)\)? For any fixed tree _T_, we want to determine the minimum number of queries needed to solve the problem.

The comparison-query model represents the standard model for analyzing problems like sorting, selection, and heap construction. Sorting represents the hardest problem in the comparison-query model as it is tantamount to knowing the entire ranking \(\rho\). Its query complexity has a well-known information-theoretic lower bound of \(\mathrm{log}_2(n!)=n\mathrm{log}_2(n/e)+\frac{1}{2}\mathrm{log}_2(n)+O(1)\). Standard algorithms such as mergesort and heapsort yield an upper bound of log<sub>2</sub>(_n_!)+_O(n_), which has been improved to log<sub>2</sub>(_n_!)+_o(n_) recently \[Ser21\]. We refer to Section 2 for an overview of results and techniques for lower bounds in the model.

Information theory only yields a very weak lower bound on the query complexity of inversion minimization on trees: \(\mathrm{log}_2\genfrac(){pt}{2}{n}{2}=2\mathrm{log}_2(n)-O(1)\). The complexity of the problem critically depends on the shape of the tree _T_ and can be significantly lower than the one for sorting. For starters, the problem becomes trivial for trees of depth one as their leaves can be arranged freely in any order. More precisely, the trees _T_ for which the answer is identically zero, irrespective of the ranking \(\rho\), are exactly those such that all root-to-leaf paths have only the root in common.

Arguably, the simplest nontrivial instances of inversion minimization are for trees _T_ of the Mann-Whitney type in Figure 2 with _a_=1 and _b=n_-1. Depending on the rank _r_ of the isolated leaf, an optimal ordering of _T_ is either the left or the right part in Figure 3, where the label of each leaf is its rank under \(\rho\).

As the ordering on the left has _r_-1 inversions and the one on the right _n-r_, the answer is min(_r_-1_,n-r_). Thus, this instance of inversion minimization on trees is essentially equivalent to rank finding, which has query complexity exactly _n_-1.

## Results.

We prove that for many trees _T_, inversion minimization on _T_ is nearly as hard as sorting. First, we exhibit a common structure that guarantees high complexity, namely a subtree that contains a fairly balanced fraction of the leaves. We make use of the following notation.

**Definition 4 (leaf set,** \(\mathrm{L}(\cdot)\)**, and subtree).** _For a tree T, the leaf set of T, denoted_ L(_T), is the set of leaves of T. For a node v to T, T<sub>v</sub> denotes the subtree of T rooted at v._


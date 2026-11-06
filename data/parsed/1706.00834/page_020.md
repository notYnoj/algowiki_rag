## 5.1 Binary Search Trees

Recall again the online version of optimal binary search tree (BST) problem (Cormen et al., 2009): We are given a set of _n_ distinct keys _K_<sub>1</sub>_\<K_<sub>2</sub>_\<...\<K<sub>n</sub>_. In each trial, the algorithm predicts with a BST. Then the adversary reveals a probability vector \(p\in[0,1]^n\) with \(\sum_{i=1}^np_i=1\). For each _i_, _p<sub>i</sub>_ indicates the _search probability_ for the key _K<sub>i</sub>_. The loss is defined as the _average search cost_ in the predicted BST which is the average depth<sup>8</sup> of all the nodes in the BST:

\(\mathrm{loss}=\sum_{i=1}^n\mathrm{depth}(K_i)\cdot p_i.\)

### Convex Hull of BSTs.

Implementing CH requires a representation where not only the BST polytope has a polynomial number of facets, but also the loss must be linear over the components. Since the average search cost is linear in the depth(_K<sub>i</sub>_) variables, it would be natural to choose these _n_ variables as the components for representing a BST. Unfortunately the convex hull of all BSTs when represented this way is not known to be a polytope with a polynomial number of facets. There is an alternate characterization of the convex hull of BSTs with _n_ internal nodes called the _associahedron_ (Loday, 2005). This polytope has polynomial in _n_ many facets but the average search cost is not linear in the _n_ components associated with this polytope<sup>9</sup>. Thus CH cannot be applied to associahedron.

### The Dynamic Programming Representation.

The optimal BST problem can be solved via dynamic programming (Cormen et al., 2009). Each subproblem is denoted by a pair (_i,j_), for \(1\le i\le n+1\) and \(i-1\le j\le n\), indicating the optimal BST problem with the keys _K<sub>i</sub>,...,K<sub>j</sub>_. The base subproblems are (_i,i_-1), for \(1\le i\le n+1\) and the complete subproblem is (1_,n_). The BST dynamic programming problem uses the following min-sum recurrence:

\(\mathrm{OPT}(i,j)=\left\{\begin{array}{ c c }
0 & j=i-1 \\
\mathrm{min}_{i\le r\le j}\{\mathrm{OPT}(i,r-1)+\mathrm{OPT}(r+1,j)+\sum_{k=i}^jp_k\} & i\le j.
\end{array}\right.\)

This recurrence always recurses on 2 subproblems. Therefore for every multiedge (_v,U_) we have |_U_|=2. The associated multi-DAG has the subproblems/vertices \(V=\{(i,j)|1\le i\le n+1,i-1\le j\le n\}\), source _s_=(1_,n_) and sinks \(\mathcal{T}=\{(i,i-1)|1\le i\le n+1\}\). Also at node (_i,j_), the set \(M_{(i,j)}^{(\mathrm{out})}\) consists of (_j-i_+1) many multiedges. The _r_th multiedge leaving (_i,j_) comprised of 2 edges going from the node (_i,j_) to the nodes (_i,r_-1) and (_r_+1_,j_). Figure 4 illustrates the underlying multi-DAG and the multipath associated with a given BST.

Since the above recurrence relation correctly solves the offline optimization problem, every multipath in the DAG represents a BST, and every possible BST can be represented by a multipath of the 2-DAG. We have |_M_|=_O(n_<sup>3</sup>) multiedges which are the components of our new representation. The loss of each multiedge leaving (_i,j_) is \(\sum_{k=i}^jp_k\) and is upper bounded by 1. Most crucially, the original average search cost is linear in the losses of the multiedges and the unit-flow polytope has _O(n_<sup>3</sup>) facets.

8. Here the root starts at depth 1. 9. Concretely, the _i_th component is _a<sub>i</sub>b<sub>i</sub>_ where _a<sub>i</sub>_ and _b<sub>i</sub>_ are the number of nodes in the left and right subtrees of the _i_th internal node _K<sub>i</sub>_, respectively.


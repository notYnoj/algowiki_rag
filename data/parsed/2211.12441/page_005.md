The quantitative statement references the gamma function \(\Gamma\), which is a proxy for any convex real function that interpolates the factorial function on the positive integers. More precisely, we have that \(\Gamma(n+1)=n!\) for every integer \(n\ge 1\).

**Theorem 5 (lower bound for general trees).** _Let T be a tree with n leaves, and v a node with_ \(|\mathrm{L}(T_v)|=\ell\)_. The query complexity of inversion minimization on T is at least_ \(\mathrm{log}_2(\Gamma(\frac{\ell(n-\ell)}{n}+1))\)_. In particular, the complexity is at least_ \(\mathrm{log}_2(\Gamma(\frac{k}{(k+1)^2}\cdot n+1))\) _where k denotes the degree of T._

For trees of constant degree, Theorem 5 yields a lower bound that is as strong as the one for sorting up to a constant multiplicative factor. For the important case of binary trees (like the classification trees from the motivating example), we obtain a lower bound that is only a logarithmic additive term shy of the lower bound for sorting.

**Theorem 6 (lower bound for binary trees).** _For binary trees T with n leaves, the query complexity of inversion minimization on T is at least_ log<sub>2</sub>(_n_!)-_O_(log_n)._

The logarithmic loss can be reduced to a constant for certain restricted classes of trees. The full statement is somewhat technical. First, it assumes that the tree has no nodes of degree 1. This is without loss of generality, as we can short-cut all degree-1 nodes in the tree without affecting the minimum number of inversions. For example, trivial trees for inversion minimization have depth 1 without loss of generality. Second, the strength of the lower bound depends on the maximum size of a leaf child set, defined as follows.

**Definition 7 (leaf child set,** \(\mathrm{LC}(\cdot)\)**).** _The_ leaf child set LC(_v_) _of a vertex v in a tree T is the set_ LC(_v_) _of all the children of v that are leaves in T._

Most importantly, the result requires certain fragile parity conditions to hold. That said, there are interesting classes satisfying all requirements, and the bounds are very tight.

**Theorem 8 (lower bound for restricted classes).** _Let T be a tree without nodes of degree 1 such that the leaf child sets have size at most k, at most one of them is odd, and if there exists an odd one, say_ LC(_v_<sup>∗</sup>)_, then all ancestors of v_<sup>∗</sup> _have empty leaf child sets. The query complexity of inversion minimization on T is at least_ log<sub>2</sub>(_n_!)-_O(k_log_k). In particular, the lower bound applies to:_

\(\circ\) _perfect trees of even degree k, and_<tbc>

\(\circ\) _full binary (k_=2_) trees with at most one leaf without a sibling leaf._

Recall that a tree of degree _k_ is full if every node has degree 0 or _k_. It is perfect if it is full and all leaves have the same depth.

For the Mann-Whitney statistic, Theorem 5 provides an \(\Omega(n\mathrm{log}n)\) lower bound for balanced instances, i.e., when _a_ and _b_ are \(\Theta(n)\). For unbalanced instances there is a more efficient way to count cross inversions and thus evaluate the statistic: Sort the smaller of the two sides, and then do a binary search for each item of the larger side to find its position within the sorted smaller side so as to determine the number of cross inversions that it contributes. For \(a\le b\) the approach makes _b_log<sub>2</sub>(_a_)+_O(a_log_a_) comparisons. We establish a lower bound that shows the approach is optimal up to a constant multiplicative factor.

**Theorem 9 (lower bound for counting cross inversions).** _Counting cross inversions from a set A of size a to a set B of size_ \(b\ge a\) _with respect to a ranking_ \(\rho\) _of_ \(X\doteq A\sqcup B\) _requires_ \(\Omega((a+b)\mathrm{log}(a))\) _queries in the comparison-query model, as does inversion minimization on the tree of Figure 2._


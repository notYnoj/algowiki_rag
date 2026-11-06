Lower Bound Techniques in the Comparison-Query Model and Inversion Minimization on Trees

**Abstract**

Given a rooted tree and a ranking of its leaves, what is the minimum number of inversions of the leaves that can be attained by ordering the tree? This variation of the well-known problem of counting inversions in arrays originated in mathematical psychology. It has the evaluation of the Mann–Whitney statistic for detecting differences between distributions as a special case.

We study the complexity of the problem in the comparison-query model, the standard model for problems like sorting, selection, and heap construction. The complexity depends heavily on the shape of the tree: for trees of unit depth, the problem is trivial; for many other shapes, we establish lower bounds close to the strongest known in the model, namely the lower bound of log<sub>2</sub>(_n_!) for sorting _n_ items. For trees with _n_ leaves we show, in increasing order of closeness to the sorting lower bound:

(a) \(log_2((\alpha(1-\alpha)n)!)-O(logn)\) queries are needed whenever the tree has a subtree that contains a fraction \(\alpha\) of the leaves. This implies a lower bound of \(log_2((\frac{k}{(k+1)^2}n)!)-O(logn)\) for trees of degree _k_.

(b) log<sub>2</sub>(_n_!)-_O_(log_n_) queries are needed in case the tree is binary.

(c) log<sub>2</sub>(_n_!)-_O(klog_k_) queries are needed for certain classes of trees of degree _k_, including perfect trees with even _k_.

The lower bounds are obtained by developing two novel techniques for a generic problem II in the comparison-query model and applying them to inversion minimization on trees. Both techniques can be described in terms of the Cayley graph of the symmetric group with adjacent- rank transpositions as the generating set, or equivalently, in terms of the edge graph of the permutahedron, the polytope spanned by all permutations of the vector (1,2_,...,n_). Consider the subgraph consisting of the edges between vertices with the same value under II. We show that the size of any decision tree for II must be at least:

(i) the number of connected components of this subgraph, and

(ii) the factorial of the average degree of the complementary subgraph, divided by _n_.

Lower bounds on query complexity then follow by taking the base-2 logarithm. Technique (i) represents a discrete analog of a classical technique in algebraic complexity and allows us to establish (c) and a tight lower bound for counting cross inversions, as well as unify several of the known lower bounds in the comparison-query model. Technique (ii) represents an analog of sensitivity arguments in Boolean complexity and allows us to establish (a) and (b).

Along the way to proving (b), we derive a tight upper bound on the maximum probability of the distribution of cross inversions, which is the distribution of the Mann–Whitney statistic in the case of the null hypothesis. Up to normalization, the probabilities alternately appear in the literature as the coefficients of polynomials formed by the Gaussian binomial coefficients, also known as Gaussian polynomials.

Ivan Hu

Dieter van Melkebeek

Andrew Morgan

July 2, 2024

arXiv:2211.12441v2 [cs.DS] 1 Jul 2024


## Error probability.

Algorithm \(\mathcal{A}'\) simulates a NoisySorting(_n_) instance on _L_ with the following total order:

• If _x,y_ are in the same group, then _x\<y_ iff _x\<<sub>T</sub>y_;<tbc>

• If \(x\in A_i\), \(y\in A_j\) are in different groups, then _x\<y_ iff _i\<j_.

Therefore, with error probability _o_(1), the sequence _x_<sub>1</sub>_,...,x<sub>n</sub>_ that A outputs is sorted with respect to the above total order, which gives the valid groups.

## Number of queries.

Algorithm \(\mathcal{A}'\) makes one query when A makes a query for elements in different groups. Algorithm \(\mathcal{A}'\) makes queries between elements in the same group only when they are not known to be in the same group. Imagine an initially empty graph on vertex set _A_ where for each GroupQuery(_x,y_) that returns ∗, we add an edge between _x_ and _y_. For every such query, the number of connected components in this graph decreases by 1, and at the end the graph has at least _n/k_ connected components. Thus, the total number of queries made by \(\mathcal{A}'\) to elements in the same group is at most _n-n/k_.

Overall, the total number of queries made by Algorithm \(\mathcal{A}'\) is at most \(\mathbb{E}[U^\frac{x}{p}]+(n-n/k)\) in expectation.

Next we prove a lower bound for the Group Sorting Problem. By Lemma 26, this implies a lower bound of the number of queries made between elements in different groups of any Noisy Sorting algorithm.

**Lemma 27.** _Let k|n with k=n_<sup>_o_(1)</sup>_. Any (deterministic or randomized) algorithm for_ GroupSorting(_n,k_) _with error probability o_(1) _makes at least_ \((1-o(1))\frac{nlogn}{I(p)}\) _queries in expectation, even if the input is a uniformly random permutation._

_Proof._ Fix an algorithm A for GroupSorting(_n,k_). WLOG assume that A makes queries between elements in the same group only when they are not known to be in the same group. Therefore, the total number of queries between elements in the same group is at most _n-n/k_.

Let _X_=(_A_<sub>1</sub>_,...,A<sub>n/k</sub>_) be the true partition. Let _m_ be the (random) number of queries made. Let _Q<sup>m</sup>_ be the queries made. Let _Y<sup>m</sup>_ be the returned values of the queries. Let \(\hat{X}\) be the most probable _X_ given all query results. Note that \(\hat{X}\) is a function of (_Q<sup>m</sup>,Y<sup>m</sup>_).

When _k=n_<sup>_o_(1)</sup>, we have \(H(X)=logn!-\frac{n}{k}logk!=(1-o(1))nlogn\).

By Fano’s inequality, \(H(X|\hat{X})\le 1+o(nlogn)\), so

\(I(X;Q^m,Y^m)\ge I(X;\hat{X})=H(X)-H(X|\hat{X})\ge(1-o(1))nlogn.\) (1)


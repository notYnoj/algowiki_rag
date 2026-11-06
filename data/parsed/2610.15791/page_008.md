procedure can improve this probability with the same budget. This establishes the classical benchmark needed to assess the benefit of coherent access.

**Theorem 1.** _For integers_ \(q\ge 0\), \(n\ge q+1\) _and_ \(0\le r\le n\),

\(C_q(n,r)=1-\frac{\genfrac(){pt}{2}{n-r}{q+1}}{\genfrac(){pt}{2}{n}{q+1}}=B(n,r,q+1).\) (4)

_The following algorithm attains this value on every order and for every r at once. Choose q_+1 _distinct labels uniformly at random, compare the current winner with the next label q times, and output the final winner. Its output rank law is_

\(Pr[x_I=t]=\frac{\genfrac(){pt}{2}{n-t}{q}}{\genfrac(){pt}{2}{n}{q+1}},t\in[n].\) (5)

To prove optimality, we examine the orders consistent with the comparison answers along a branch of an arbitrary comparison tree. The following lemma describes the remaining rank uncertainty in the connected component containing the output label.

**Lemma 1.** _Fix a deterministic comparison tree and a leaf_ \(\ell\) _reached with positive probability under a uniform order. Let_ \(E_\ell\) _be the set of orders that reach_ \(\ell\)_, let a be its output label, and let C be the connected component of a in the graph whose edges are the distinct pairs compared on the path to_ \(\ell\)_. Put k_=|_C|. Conditional on_ \(E_\ell\)_, the set of ranks occupied by C is a uniform k-subset of_ \[_n_\]_, independent of the order within C, and_

\(Pr[x_a=t|E_\ell]=\sum_{j=1}^k\alpha_j\frac{\genfrac(){pt}{2}{t-1}{j-1}\genfrac(){pt}{2}{n-t}{k-j}}{\genfrac(){pt}{2}{n}{k}},\) (6)

_where_ \(\alpha_j\ge 0\) _is the fraction of linear extensions of the order recorded on C in which a has the j-th smallest rank within C, and_ \(\sum_j\alpha_j=1\).

_Proof._ Each comparison of distinct labels on the path to \(\ell\) records one strict inequality. A self-comparison imposes no constraint. An order reaches \(\ell\) exactly when it satisfies all recorded inequalities, because the tree is deterministic and every answer on the path is prescribed. So \(E_\ell\) is the set of linear extensions of the recorded partial order. Let _D_ be the complement of _C_. No recorded inequality joins _C_ and _D_, and the transitive closure adds none, since a directed path between them would be an undirected path in the comparison graph. Fix a _k_-subset _S_ of ranks and a linear extension \(\pi_C\) of the order on _C_. Place \(\pi_C\) on the ranks _S_ in increasing order. For each linear extension \(\pi_D\) of the order on _D_, place \(\pi_D\) on the complementary ranks. This gives exactly one order in \(E_\ell\) with rank set _S_ on _C_ and internal order \(\pi_C\), and every such order arises once. The count is the number _e<sub>D</sub>_ of linear extensions of the order on _D_, which does not depend on _S_ or \(\pi_C\). The joint law of rank set and internal order is therefore uniform, which proves independence. If _a_ has the _j_-th smallest rank within _C_ under \(\pi_C\), then _x<sub>a</sub>=t_ exactly when _S_ contains _t_, _j_-1 ranks below _t_ and _k-j_ ranks above it, which gives (6).

_Proof of Theorem 1. Attainment._ The output rank is the minimum of a uniform (_q_+1)-subset of ranks. It misses the top _r_ exactly when all _q_+1 ranks exceed _r_, which has probability \(\genfrac(){pt}{2}{n-r}{q+1}/\genfrac(){pt}{2}{n}{q+1}\). The output rank equals _t_ exactly when the subset contains _t_ and _q_ ranks above<tbc>


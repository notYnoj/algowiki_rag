strong: that a uniformly random pivot in _any_ instance \(V'\) has a good chance of not being in many vertex separators, even when \(|V'|\) is much smaller than _n_, or even \(\sqrt{m}\). To achieve this, we query the Max-Flow between pairs of high degree nodes in every instance, but with a very high degree threshold compared to \(|V'|\), which is \(\hat{t}\ge|V'|/\mathsf{polylog}(n)\). By analyzing the recursion tree _T_, and that instances \(V'\) in any single depth of _T_ are disjoint, we conclude that there cannot be more than \(\tilde{O}(m)\) such queries in a single depth of _T_.

The second challenge is in the correctness proof for any node pair _u,v_. Similar to \[AKT20a\], we would like to reason about the pivot choice _p_ in the instance separating _u_ and _v_. However, vertex separators in our case introduce a worrisome dependency, as it could be for some instances that the only nodes separating _u_ and _v_ as pivots are _u_, _v_, and nodes within their separator _C<sub>u,v</sub>_. In this case, a careful analysis is needed to prove that such node pairs are likely to be pushed together (i.e. not being separated) to a later stage. We do this by using a more global argument that is independent of the particular instance separating _u_ and _v_, described below.

On one hand, while \(|V'|\) is large compared to |_C<sub>u,v</sub>_|, there is a decent probability to pick pivots outside of _C<sub>u,v</sub>_. On the other hand, if \(|V'|\) becomes small enough while _u_ and _v_ are still together, then they would be queried as a pair of high degree nodes in \(V'\). This motivates the following analysis (see Figure 2). Consider the path _P_ from the root of _T_ to \(V'_u\), the highest recursion node in _T_ where \(|V'_u|\) is smaller than a threshold set to \(\tilde{O}(d_G(u))\), where we assume without loss of generality that \(d(u)\le d(v)\). We show that with constant probability, all pivot choices in instances along _P_ do not belong to _C<sub>u,v</sub>_. Assuming that this event occurs, we have two cases. If _v_ has survived all the way down to \(V'_u\), then _v_ and _u_’s high degrees compared to \(|V'_u|\) would cause the algorithm to query them directly as a pair at this stage. Otherwise, they got separated earlier _along P_, and consequently, the pivot chosen at the moment of separation does not belong to _C<sub>u,v</sub>_.

Altogether, property (\*) in \[AKT20a\] is modified to fit our setting as follows:

(\*\*) For every pair \(s'\in S_{i,p},t'\in S_{j,p}\) for \(i\neq j\) such that \(\mathsf{Max}-\mathsf{Flow}(p,s')\le\mathsf{Max}-\mathsf{Flow}(p,t')\), with constant probability at least one of the following holds.

1. \(t'\in C_{p,i}\).<tbc>

T
P
Vu
|V'| < (dg(u))

Figure 2: If \(v\in V_u\) then both _u,v_ are queried directly as a high degree pair. Otherwise, with constant probability _v_ must have been separated from _u_ in a higher recursion node along _P_, in which case \(v\notin C_{u,v}\) at that moment of separation.


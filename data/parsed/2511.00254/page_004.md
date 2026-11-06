The third key question requires slightly more motivation. If (_G,H_) is not an uncrossable layout, it only means the structure of (_G,H_) alone is insufficient to guarantee uncrossed solutions. However for specific capacities _u_ and demands _d_ we may still be able to find an uncrossed flow and round it. Thus it would be nice to have algorithms to determine whether (in the congestion setting) we can find a feasible fractional flow that is uncrossed, or (in the maximization setting) find the largest feasible flow that is uncrossed.

**Question 3.** Suppose we are given an _arbitrary_ planar multiflow instance. Can we solve the fractional multiflow problem if we constrain the feasible space to only allow uncrossed solutions? Specifically:

i. (Congestion Setting) Given (_G,H,u,d_), can we determine whether there exists a feasible fractional multiflow that is uncrossed?<tbc>

ii. (Maximization Setting) Given (_G,H,u_), can we compute a feasible fractional uncrossed multiflow whose value is (approximately) maximum amongst feasible uncrossed solutions (_maximum uncrossed multiflow_)?

These questions concern _fractional_ multiflows and may feel like linear optimization problems. However the requirement of uncrossed flow paths makes these computationally much more challenging. Interestingly, the positive result of Theorem 1.2 can be combined with results of \[8, 9\] to establish strong almost-polynomial inapproximability for maximum uncrossed fractional multiflow (for both edge and node capacities).

**Theorem 1.6.** _For planar G, maximum uncrossed fractional multiflow is not approximable to within a factor of_ \(2^{\Omega(log^{1-\epsilon} n)}\) _for any_ \(\epsilon>0\) _assuming that_ \(NP\unknown\subseteq DTIME(n^{polylog}n)\)_. Moreover, there is no_ \(n^O\big(\frac{1}{(loglogn)^2}\big)\)_- approximation polynomial-time algorithm assuming that for some constant_ \(\delta>0\), \(NP\unknown\subseteq DTIME(2^{n^\delta})\)_. These results hold even when G is maximum degree_ 3 _(or even G is a wall graph) and the capacities are unit._

For the congestion setting, we prove that the problem posed by Question 3 is NP-complete.

**Theorem 1.7.** _It is NP-complete to determine whether planar congestion instance_ (_G,H,u,d_) _has a feasible fractional uncrossed multiflow, even with unit-valued capacities and demands._

We remark that since this problem is not a linear program anymore, it is not even obvious that the problem is in NP, however we establish this in Section C.1. On the positive side, we show that finding uncrossed edge-disjoint paths can be (polytime) reduced to a node-disjoint paths instance. Hence we may find uncrossed solutions if _E(H_) is incident with a bounded number of faces using a result of Schrijver \[30\].

**Theorem 1.8.** _For instances where G is planar, the edges of H are incident with a bounded number of faces, and the capacities and demands are unit-valued, there is a polynomial time algorithm to find a feasible integral uncrossed multiflow for_ (_G,H,u,d_) _or declare that none exists._

## 1.1 Organization of the Paper

Section 2 lays the groundwork for the theory of uncrossed flows, including detailed definitions. Section 3 discusses pairwise-planar instances, proves they admit uncrossed flows, and shows a constant integral flow- multicut gap. Section 4 covers our maximization results, both rounding (Theorem 1.2) and inapproximability (Theorem 1.6). The rounding result for congestion (Theorem 1.3) appears in Section 5. The NP-completeness result (Theorem 1.7) is deferred to the appendix (Section C). Section 6 contains the algorithm to solve integral congestion instances when demands are incident with a bounded number of faces (Theorem 1.8).

## 1.2 Related Work

Uncrossed flows have played a role in previous routing algorithms in planar graphs, such as Schrijver’s Homotopy Method \[29\] for node-disjoint paths. Most relevant are recent algorithms for maximum disjoint paths in fully-planar instances (_G+H_ planar). In \[18, 15\], constant-factor approximation algorithms are given for maximum edge-disjoint path, then extended to the node-disjoint setting in \[28, 27\]. These algorithms<tbc>


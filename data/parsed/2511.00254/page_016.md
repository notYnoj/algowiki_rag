### 4.2 Inapproximability of Maximum Uncrossed Fractional Multiflow

Next we prove Theorem 1.6 on the inapproximability of maximum uncrossed (fractional) multiflow. We make use of a strong inapproximability result given by Chuzhoy, Kim, and Nimavat for maximum edge-disjoint paths (MEDP) and maximum node-disjoint paths (MNDP) in planar graphs; i.e. maximum integer multiflow for unit capacities. One minor technicality is that in their formulation, a feasible solution is only allowed to route one unit of flow for each demand. We thus call these problems _capped MEDP_ and _capped MNDP_ respectively.

**Theorem 4.6** (Theorems 1.1 and 1.2, \[9\])**.** _For every constant_ \(\epsilon>0\) _, there is no_ \(2^{\Omega(log^{1-\epsilon} n)}\)_-approximation polynomial-time algorithm for capped MEDP or capped MNDP, assuming that_ \(NP\unknown\subseteq DTIME(n^{polylogn})\)_. Moreover, there is no_ \(n^{O\left(\frac{1}{(loglogn)^2}\right)}\)_-approximation polynomial-time algorithm for capped MEDP or capped MNDP, assuming that for some constant_ \(\delta>0\), \(NP\unknown\subseteq DTIME(2^{n^\delta})\)_. These results hold even when the input graph is a maximum degree_ 3 _planar graph, or even if G is a wall graph._

We now prove Theorem 1.6 which relies on this result. We focus on the edge-capacitated version (the node-capacitated version is similar).

_Proof of Theorem 1.6._ We prove that result by giving a polytime reduction from capped MEDP in wall graphs to maximum uncrossed multiflow in wall graphs, that preserves the approximation ratio up to a constant factor. For an instance (_G,H_) of the capped MEDP problem where _G_ is a wall graph (which is planar and has maximum degree 3), define the following quantities.

• Let _D<sub>E</sub>(G,H_) denote the maximum number of demands in _H_ which can be routed on edge-disjoint paths in _G_ (i.e. the optimal value for capped MEDP).<tbc>

• Let _U<sub>E</sub>(G,H_) denote the maximum value of a (fractional) uncrossed multiflow for \((G,H,u=\vec{1})\).

Observe that any capped MEDP solution for (_G,H_) is a feasible (integral) uncrossed multiflow for \((G,H,u=\vec{1})\). To see this, consider a collection of edge-disjoint paths that form a capped MEDP solution. Recall from Section 2.2 that two edge-disjoint paths cross only if they cross at a node (rather than a longer common subpath). Since _G_ has maximum degree 3, a node crossing is not possible. Thus we have \(D_E(G,H)\le U_E(G,H)\).

Suppose we have a \(\beta\)-approximation algorithm for maximum uncrossed (fractional) multiflow in wall graphs. We obtain an approximation algorithm for capped MEDP as follows. We run our \(\beta\)-approximation algorithm for maximum uncrossed multiflow on \((G,H,u=\vec{1})\) to obtain flow _f_ whose value is at least \(U_E(G,H)/\beta\). We apply the polytime algorithm from Theorem 4.3 to compute a feasible uncrossed integral multiflow \(f'\) whose value is \(1/\gamma\) that of _f_. It may still not be a valid capped MEDP solution, since it may route more than one flow path for the same commodity. However, since _G_ has maximum degree 3, it routes on at most 3 paths for each commodity, so by selecting exactly one path for each commodity we obtain a capped MEDP solution whose value is at least \(\frac{1}{3}\) that of \(f'\). Thus this algorithm outputs a capped MEDP solution whose value is at least \(\frac{U_E(G,H)}{3\gamma\beta}\ge\frac{D_E(G,H)}{3\gamma\beta}\) , and is thus a \(3\gamma\beta\)-approximation algorithm.

## 5 Congestion Setting: Rounding

In this section, we focus on planar congestion instances (_G,H,u,d_) where the demands must be fully routed. We show Theorem 1.3, which states that we can convert (fractional) strongly uncrossed multiflows into integral flows that violate the capacities by a factor of at most 2, and if we accept an additional additive error of less than \(d_{max}=max_{h\in E(H)}d(h)\) the flow can be made unsplittable. Section 5.1 presents the relevant properties of strongly uncrossed flows, and Section 5.2 gives the proof of Theorem 1.3.


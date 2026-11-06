<tbc>edge is upper-bounded by 1. Most crucially, the total profit over chosen intervals in the scheduling is linear in the gains of the edges and the unit-flow polytope has _O(n_) facets.

### Regret Bounds.

Similar to rod cutting, this is also the online longest-path problem with one sink node. Like the rod cutting problem, we modify the graph by adding O(_n_<sup>2</sup>) vertices and edges (with gain zero) to make all paths have the same length of _D=n_ and change the gains into losses. Call this new DAG \(\bar{\mathcal{G}}\). Again we have \(L_\bar{\mathcal{G}}(\unknown)=n-G_\mathcal{G}(\unknown)\) for all paths \(\unknown\). According to our initial assumption logN=O(_n_). Thus using Theorem 10 we obtain:

\(G^*-\mathbb{E}[G_\mathrm{EH}]=(nT-L^*)-(nT-\mathbb{E}[L_\mathrm{EH}])\)<br>
\(=\mathbb{E}[L_\mathrm{EH}]-L^*=\mathcal{O}(n\sqrt{L^*}).\)

Notice that the number of multiedges/edges in \(\bar{\mathcal{G}}\) is |_M_|=|_E_|=_O(n_<sup>2</sup>) and each path consists of _D=n_ edges. Therefore using Theorem 14 we obtain:

\(G^*-\mathbb{E}[G_\mathrm{CH}]=(nT-L^*)-(nT-\mathbb{E}[L_\mathrm{CH}])\)<br>
\(=\mathbb{E}[L_\mathrm{CH}]-L^*=\mathcal{O}(n^\frac{1}{2}(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*}).\)

**6. Conclusions and Future Work**

We developed a general framework for combinatorial online learning problmes whose offline optimization problems can be efficiently solved via "min-sum" dynamic programming algorithms.  2 gives the performance of EH and CH in our dynamic programming<tbc>

11. The loss of a fully parenthesized matrix-chain multiplication is the number of scalar multiplications in the execution of all matrix products. This number cannot be expressed as a linear loss over the dimensions of the matrices. We are thus unaware of a way to apply FPL to this problem using the dimensions of the matrices as the components.

\begin{tabular}{cccc}
Problem & FPL & EH & CH \\
Optimal Binary & \(\mathcal{O}(n(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\) & \(\mathcal{O}(n\sqrt{L^*})\) & \(\mathcal{O}(n^\frac{1}{2}(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\) \\
Search Trees & & & \*\*Best\* \\
Matrix-Chain & -- & \(\mathcal{O}(n(d_\mathrm{max})^\frac{3}{2}\sqrt{L^*})\) & \(\mathcal{O}(n^\frac{1}{2}(\mathrm{log}n)^\frac{1}{2}(d_\mathrm{max})^\frac{3}{2}\sqrt{L^*})\) \\
Multiplications <sup>11</sup> & & & \*\*Best\* \\
Knapsack & \(\mathcal{O}(n(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\) & \(\mathcal{O}(n\sqrt{L^*})\) & \(\mathcal{O}(n^\frac{1}{2}(\mathrm{log}nC)^\frac{1}{2}\sqrt{L^*})\) \\
 & & & \*\*Best\* \\
_k_-sets & \(\mathcal{O}(k^\frac{1}{2}n^\frac{1}{2}(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\) & \(\mathcal{O}(k^\frac{1}{2}(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\) & \(\mathcal{O}(n^\frac{1}{2}(\mathrm{log}k(n-k))^\frac{1}{2}\sqrt{L^*})\) \\
 & & \*\*Best\* & \\
Rod Cutting & \(\mathcal{O}(n(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\) & \(\mathcal{O}(n\sqrt{L^*})\) & \(\mathcal{O}(n^\frac{1}{2}(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\) \\
 & & & \*\*Best\* \\
Weighted Interval & \(\mathcal{O}(n(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\) & \(\mathcal{O}(n\sqrt{L^*})\) & \(\mathcal{O}(n^\frac{1}{2}(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\) \\
Scheduling & & & \*\*Best\* \\
\end{tabular}

2: Performance of various algorithms over different problems in the full information setting. _C_ is the capacity in the Knapsack problem, and _d_<sub>max</sub> is the upper-bound on the dimension in matrix-chain multiplication problem.


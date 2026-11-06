## 5.2 Active subset heuristics

Following Theorem 5.1, the main principle of the heuristics we propose is to select a subset of paths \(Q^k\subset P^k\) for each \(k\in K\), and to replace the constraints (3) by the constraints \(\sum_{a\in p}\frac{1}{c_a-y_a}\le d^k\) for each \(p\in Q^k\), and to set \(x_p^k\) to 0 for all paths in _P<sup>k</sup>_\\_Q<sup>k</sup>_. All that remains is to solve a convex problem:

\(\mathrm{DCMCF}_\mathrm{subset}\mathrm{max}\gamma\)<br>
\((1),(2),(4),(5)\)<br>
\(\sum_{a\in p}\frac{1}{c_a-y_a}\le d^k\forall k\in K,p\in Q^k.\)

DCMCF<sub>subset</sub> is a simple convex optimization problem. The difficulty, of course, is guessing the right subset of paths to select.

### 5.2.1 All paths heuristic

Remember that we assumed that \(\sum_{a\in p}\frac{1}{c_a}<d^k\) for each path \(p\in P^k\). One can then simply solve DCMCF<sub>subset</sub> with _Q<sup>k</sup>=P<sup>k</sup>_ for every commodity \(k\in K\) to obtain a feasible solution of the problem with a strictly positive objective value, that will be called H_<sub>all paths</sub>_.

### 5.2.2 Greedy heuristic

The H_<sub>all paths</sub>_ heuristic can be improved in a greedy fashion: the DCMCF<sub>subset</sub> problem is first solved with _Q<sup>k</sup>=P<sup>k</sup>_ for every \(k\in K\), then the path with the smallest \(x_p^k\) value is removed. This process is repeated as long as the objective function of the problem increases. This heuristic, called H_<sub>greedy</sub>_ is presented in Algorithm 1, where \(\mathrm{OPT}(\mathrm{DCMCF}_{\{Q^k\}_{k\in K}})\) is the optimal value of the DCMCF<sub>subset</sub> problem on the subsets _Q<sup>k</sup>_ of _P<sup>k</sup>_ for \(k\in K\).

### 5.2.3 Heuristic based on the DCMCF<sub>env</sub> Relaxation

It also makes sense to use the convex relaxation solution of Section 3 to select the subsets _Q<sup>k</sup>_. For example, for a given scalar \(S\in\mathrm{IR}^+\), we can select all paths for which \(x_p^k\ge\frac{\gamma}{|P^k|}\) in the convex relaxation’s optimal solution: \(Q_S^k=\{p\in P^k:x_p^k\ge\frac{\gamma}{S|P^k|}\}\). Let us denote this heuristic by H_<sub>threshold</sub>_. If<tbc>


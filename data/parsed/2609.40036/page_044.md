## B.1 Disagreement probabilities and the LP objective

Fix an error vector **e** and its syndrome **s**=_H_**e**. Let **x**<sup>**e**</sup> be the corresponding integral feasible marginal vector, with entries \(x_{f,a}^\mathbf{e}=\mathbf{1}\{a=e_f\}\). For any other feasible marginal vector **x**, define the disagreement probabilities by

\(z_f:=1-x_{f,e_f}=\sum_{a\in\unknown_q\backslash\{e_f\}}x_{f,a},\) (205)

and put

\(T:=\{f:e_f\neq 0\},\omega_f:=1-2\mathbf{1}\{f\in T\}.\) (206)

Thus _T_ is the set of erroneous edges, and \(\omega_f\) is +1 on an uncorrupted edge and -1 on a corrupted edge. The vector **z** is nonnegative, and \(\mathbf{z}\neq 0\) whenever \(\mathbf{x}\neq\mathbf{x}^\mathbf{e}\).

Fix a vertex _v_ and sample a local assignment **b** from a distribution \(\lambda_{v,\mathbf{b}}\) witnessing feasibility of **x**. Both **b** and the restriction of **e** to \(\partial v\) satisfy the check at _v_, so

\(\sum_{f\in\partial v}h_{vf}(b_f-e_f)=0.\) (207)

These two assignments cannot differ on exactly one edge _f_ in the check support: that would give _h<sub>vf</sub>(b<sub>f</sub>-e<sub>f</sub>_)=0 with both factors nonzero in F_<sub>q</sub>_. Therefore, if \(b_f\neq e_f\), there must be another edge \(f'\in\partial v\backslash\{f\}\) on which \(b_{f^\prime}\neq e_{f^\prime}\). By local consistency, the probabilities of these disagreements are _z<sub>f</sub>_ and \(z_{f^\prime}\). A union bound gives

\(z_f\le\sum_{f^\prime\in\partial v\backslash\{f\}}z_{f^\prime}\) (208)

for every \(v\in V\) and \(f\in\partial v\). This is the only algebraic property of the checks used in the recovery argument. It uses nonzero entries within each check support, but no relation between the entries at the two endpoints of an edge. It also uses only one local assignment distribution at a time; no joint distribution on complete syndrome-consistent words is assumed.

On an uncorrupted edge, the objective difference is 1-_x_<sub>_f,_0</sub>=_z<sub>f</sub>_. On a corrupted edge, it is \(-x_{f,0}\ge-z_f\), because \(e_f\neq 0\) and \(x_{f,0}\le 1-x_{f,e_f}\). Summing these contributions gives

\(\mathcal{L}(\mathbf{x})-|\mathbf{e}|\ge\sum_f\omega_fz_f.\) (209)

In particular, \(\mathbf{x}\neq\mathbf{x}^\mathbf{e}\) and \(\mathcal{L}(\mathbf{x})\le|\mathbf{e}|\) imply that **z** is nonzero, satisfies (208), and obeys \(\sum_f\omega_fz_f\le 0\). Equivalently,

\(\sum_{f:e_f\neq 0}z_f\ge\sum_{f:e_f=0}z_f.\) (210)

The comparison applies to all feasible marginal vectors, including fractional solutions and equal-cost ties.

## B.2 From disagreement probabilities to walks

A nonbacktracking walk traverses adjacent edges without immediately reversing the previous edge. We now use (208) to construct a random walk that has probability proportional to _z<sub>f</sub>_ of traversing edge _f_ at each step. This converts the objective comparison into a statement about the error locations along walks.


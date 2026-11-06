<tbc>_where_ \(\mathbf{d}^\unknown\) _denotes the vector_ **d** _ordered by nonincreasing values, i.e.,_ \(d_1^\unknown\ge d_2^\unknown\ge\dots\ge d_N^\unknown\).

The weights of the GGI aggregation function may be defined in a variety of manner. For instance, the weights initially proposed for the Gini social-evaluation function are:

\(\lambda_i=(2(N-i)+1)/N^2\forall i\in\{1,\dots,N\}\) (4)

**Example 6** _Coming back to Example 1, if the weights_ \(\unknown\) _are defined by Equation 4 and the disutility function is defined by d(i_)=_i, the GGI values of the different stable marriages are (the lower the better):_

_We thus observe that using a GGI aggregation function makes it possible to obtain_ **x**<sup>4</sup> _as an optimal stable marriage._

The GGI is also known in multicriteria decision making under the name of _ordered weighted average_ \[Yager, 1988\]. This aggregation function, to minimize, is well-known to satisfy the Pigou-Dalton transfer principle if \(\lambda_1>\lambda_2>\dots>\lambda_N\):

**Definition 2** _An aggregation function F satisfies the_ transfer principle _if for any_ \(\mathbf{d}\in(\mathbb{R}^+)^N\) _and_ \(\varepsilon\in(0,d_j-d_i)\) _where d<sub>j</sub>\>d<sub>i</sub>:_

\(F(d_1,\dots,d_i+\varepsilon,\dots,d_j-\varepsilon,\dots,d_N)<F(d_1,\dots,d_N).\)

This condition states that the overall welfare should be improved by any transfer of disutility from a "less happy" agent _j_ to a happier agent _i_ given that this transfer reduces the gap between the disutilities of agent _i_ and _j_. We can now define the GGI Stable Marriage problem.

## 3 Complexity of the GGISM Problem

The GGISM problem extends both the egalitarian and the utilitarian approaches to the stable marriage problem. Indeed, if the weights of the GGI operator are \(\unknown=(1,\dots,1)\), one obtains the sum operation. If the weights are \(\unknown=(1,0,\dots,0)\), one obtains the max operation. While both variants are polynomially solvable problems, the following result states that the GGISM problem is NP-hard:

**Theorem 2** _The GGISM problem is NP-hard._

\begin{tabular}{ccc}
_matching_ **x** & _ordered vectors_ \(\mathbf{d}^\unknown(\mathbf{x})\) & \(\mathtt{GGI}_\unknown(\mathbf{d}(\mathbf{x}))\) \\
**x**<sup>1</sup> & (10,7,7,7,7,4,3,3,2,1,1,1,1,1,1,1,1,1,1,1) & _4.4525_ \\
**x**<sup>2</sup> & (10,7,7,5,5,4,4,4,3,3,2,1,1,1,1,1,1,1,1,1,1,1) & _4.4725_ \\
**x**<sup>3</sup> & (10,7,7,5,5,4,4,4,3,3,2,1,1,1,1,1,1,1,1,1,1) & _4.4725_ \\
**x**<sup>4</sup> & (10,5,5,5,5,4,4,4,4,4,3,2,1,1,1,1,1,1,1,1,1,1) & _4.3925_ \\
**x**<sup>5</sup> & (9,5,5,5,5,5,5,5,4,4,4,4,3,3,2,2,1,1,1,1,1,1,1) & _4.74_ \\
\end{tabular}

GGI Stable Marriage (GGISM)
INSTANCE: Two disjoint sets of size n, the men and the women; for each person, a preference list containing all the members of the opposite sex; a vector of weight parameters and a disutility function d.
SOLUTION: A stable marriage x.
MEASURE: (d(x)) (to minimize).


2. _Z<sub>kij</sub>_ participates in three inequalities: the ones that correspond to _r<sub>ij</sub>_, _q<sub>ikj</sub>_ and _q<sub>jki</sub>_ (with negative sign in _q_). It is not part of the primal objective, therefore: \(r_{ij}-q_{ikj}-q_{jki}\ge 0\).

It is more natural to work with non-negative variables, so let us re-define \(R\equiv-r\) and \(Q\equiv-q\). In this case, we flip signs in the inequalities. We also need to flip the sign in the objective function, but instead we flip from minimization to maximization. The final formulation is as follows.

**Definition 4.1** (STT Dual LP)**.**

1. Variables _R_ over pairs, _Q_ over colinear triplets: \(\forall i,j:R_{ij}\), and \(\forall k\in(i\unknown\rightarrow j):Q_{ikj},Q_{jki}\).<tbc>

2. Objective function: maximize \(\sum_{i,j\in U}R_{ij}\).<tbc>

3. Constraints:<tbc>

(a) (Bounds) \(\forall i,j\in U:\forall k\in(i\unknown\rightarrow j):0\le R_{ij},Q_{ikj},Q_{jki}\).<tbc>

(b) (Capping) \(\forall i,j\in U:\forall k\in(i\unknown\rightarrow j):R_{ij}\le Q_{ikj}+Q_{jki}\).<tbc>

(c) (Frequency) \(\forall i,j\in U:R_{ij}+\sum_{a:i\in(j\unknown\rightarrow a)}Q_{jia}\le f_j\).

## 4.2 The Dual LP: Interpretations and Insights

We list a few observations:

1. The solution \(R=\vec{0}\), \(Q=\vec{0}\) is feasible.<tbc>

2. In the frequency constraints, \(\{a:i\in(j\unknown\rightarrow a)\}\) is the set of all nodes that are "behind" _i_ from the perspective of _j_. Another way to view it: if we root the tree (topology) _U_ in node _j_, then this is exactly the subtree of _i_, excluding _i_.<tbc>

3. If _i_ and _j_ are neighbors, then _R<sub>ij</sub>_ has no capping inequality. However, it is still bounded by frequency inequalities. If _i_ is a leaf, these are \(R_{ij}\le f_j\) and \(R_{ij}\le f_i-\sum_{a\in U\backslash\{i,j\}}Q_{ija}\).<tbc>

4. We may assume that every capping inequality holds as equality. Indeed, if _R<sub>ij</sub>\<Q<sub>ikj</sub>+Q<sub>jki</sub>_ we can decrease the right hand side until we get an equality. This can only help us increase the objective function, if we happen to get a loose frequency inequality in which we can further increase some _R<sub>ij</sub>_. Given this tightness, we also get that \(Q_{ik^\prime j}+Q_{ik^\prime j}=Q_{ikj}+Q_{ikj}(=R_{ij})\) for every pair \(k,k'\in(i\unknown\rightarrow j)\). To explain this freedom to tweak these constraints, recall that the primal constraints \(Z\ge 0\) were unnecessary. When we omit them in the primal LP, the corresponding dual constraints that we get are equalities.<tbc>

5. Unlike the primal LP which "usually" has a unique solution, the dual LP "usually" has multiple solutions. As a simple example, consider a topology with 3 nodes, with frequencies _f_=\[3,1,2\]. The primal optimum value is 4 due to the unique optimal BST with depths _D_=\[0,2,1\]. The dual solution is _R_<sub>12</sub>=_R_<sub>23</sub>=1, _R_<sub>13</sub>=2 with freedom to set _Q_ such that \(Q_{123}\in[0,2]\), \(Q_{321}\in[0,1]\) and \(Q_{123}+Q_{321}\ge 2\). In larger topologies, there may be degrees of freedom on the _R_ variables as well. That is, the sum over all _R<sub>ij</sub>_’s is fixed (the value of the dual LP), but there will be freedom of how to distribute the sum between the specific variables. Sometimes, the dual LP has a unique solution. Tweaking the current example to _f_=\[2,1,2\], the unique solution has the same _R_, with a unique _Q_: _Q_<sub>123</sub>=_Q_<sub>321</sub>=1.<tbc>


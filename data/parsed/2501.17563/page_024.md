<tbc>_U<sub>i</sub>_ in _P<sub>i</sub>_ and \(P'_i\) are the same. Furthermore, the proof shows how to extend a direction _h<sub>i</sub>_ for which _P<sub>i</sub>_ is uniquely optimal, to a direction \(h'_i\) for which \(P'_i\) is optimal. The extension adds 0’s in coordinates of \(h'_i\) that do not correspond to coordinates of _h<sub>i</sub>_. So if _P_<sub>1</sub> is a vertex of the LP of _U_<sub>1</sub> and _h_<sub>1</sub> is a direction in which _P_<sub>1</sub> it is the unique optimum, then \(P_2=\pi(P_1)\) is a vertex of _U_<sub>2</sub> and \(h_2=\pi(h_1)\) is a direction in which _P_<sub>2</sub> is uniquely optimal. It follows that \(P'_1\) and \(P'_2\) are both vertices of _U_, \(P'_1\) is optimal in the direction \(h'_1\), and \(P'_2\) is optimal in the direction \(h'_2\). Note that \(h'_1\) and \(h'_2\) are directions with the same coordinate-values, permuted. These values are the same as of _h_<sub>1</sub>, and _h_<sub>2</sub>, padded with zeros. In many cases, this permutation does not correspond to an automorphism of _U_. As an example, name the edges of the topology _U_<sub>(8,4)</sub> as {(1,2),(2,3),(3,4),(4,5),(5,6),(3,7),(7,8)}. We can shrink it to _U_<sub>(7,3)</sub> by deleting one of the nodes in {4,5,6}, and as a result we get multiple similar but not automorphically symmetric primary directions. A concrete example of such directions is: (3,2,0,0,2,3,3,10), (3,2,0,2,0,3,3,10) and (3,2,0,2,3,0,3,10) (all extend (3,2,0,2,3,3,10) from Theorem 2.2). Such directions may find vertices that are not automorphically symmetric, and thus lead to a different behavior under rounding (e.g. with Definition 1.6).

## 4 The Dual LP

In this section we study the dual formulation of the LP given in Definition 1.2. Section 4.1 develops the formulation slowly with verbose explanations. For the final formulation and some interpretations, skip to Definition 4.1 and Section 4.2.

### 4.1 Developing the Dual LP

First, we rewrite the primal LP:

1. Remove _D_, and also change the problem to a maximization problem. As a consequence, the objective function becomes: maximize \(\sum_{j\in U}\left(-f_j\right)\cdot D_j=\sum_{j\in U}\left(-f_j\right)\cdot\left(\sum_{i\in U}X_{ij}\right)\).<tbc>

2. Rewrite the LCA inequalities as follows (for relevant values of _i,j,k_):<br>
(1) \(0\le X_{ki}-Z_{kij}\); (2) \(0\le X_{kj}-Z_{kij}\).

Next, we define the variables of the dual. We have a variables _r<sub>ij</sub>_ for each ancestry inequality over a pair of _i_ and _j_. There is no difference in the order of indices, so \(r_{ji}\equiv r_{ij}\) and we only use one of them (similar to how \(Z_{kij}\equiv Z_{kji}\)). For the LCA inequalities we define the variables _q<sub>ikj</sub>_ whose indices are ordered, and represent a directed "path" from _i_, through _k_, to _j_. For a triplet _i,k,j_, _q<sub>ikj</sub>_ corresponds to the first LCA inequality, and _q<sub>jki</sub>_ corresponds to the second inequality. Since all the inequalities are such that the sum of the variables is greater or equal to the free coefficient, both _r_ and _q_ are non-positive coordinate-wise (we flip this later).

The dual objective function is to minimize \(\sum_{i,j}r_{ij}\) since the free coefficient is 1 only in (ancestry) inequalities that correspond to _r_, and 0 otherwise. We derive the dual inequalities based on the primal variables _X_ and _Z_ as follows:

1. _X<sub>ij</sub>_ participates in the ancestry inequality that corresponds to _r<sub>ij</sub>_, and also in the LCA inequalities of the form _X<sub>ij</sub>-Z<sub>iaj</sub>_ where \(i\in(j\unknown a)\), which corresponds to _q<sub>jia</sub>_, and not to be confused with _q<sub>aij</sub>_ which corresponds to \(X_{ia}-Z_{ija}\ge 0\). Lastly, _X<sub>ij</sub>_ has a coefficient of -_f<sub>j</sub>_ in the objective function, therefore we get the inequality: \(r_{ij}+\sum_{a:i\in(j\unknown a)}q_{jia}\ge(-f_j)\).<tbc>


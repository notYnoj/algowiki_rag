<tbc>collisions of vertices, that is, if there exists (_X,Z,D_)-vertices, \(P\neq P'\), such that \(P_D=P'_D\). Because the LP without _Z_ variables is arguably nicer and "more true" (recall Section 5.2), let us wonder about collisions of vertices of the (_X,D_)-polytope of the LP when projected to _D_-space.

For STTs the answer is negative: given a depths-vector _D_ induced by an STT, there is exactly one (_X,D_)-vertex in its pre-image. Indeed, the depths-vector _D_ uniquely implies the value of all the _X_ variables, because there is a unique index _r_ (the root) such that _D<sub>r</sub>_=0, so it must be that \(\forall i\neq r:X_{ir}=0,X_{ri}=1\). Then we recurse in each connected component, now looking for a vertex of depth one in each connected component etc.

In contrast, general vertices may collide. When we solved the LP without the _Z_ variables, in all the primary directions that discover non-STT vertices, we found a few collisions. Recall that the objectives that we used had non-zero coefficients only for the _D_-variables, so to truly study the collisions one should use general objectives. Furthermore, note that refinements of the LP such as those discussed in Section 5.1 may affect these collisions.

## 6 Open Questions

In this section we summarize the main open questions regarding the LP approach towards solving Problem 1. Of course, solving the problem with any tool/approach, is still open. Moreover, we assumed that all queries are successful, that is, there are no searches of non-existing nodes. If the optimum can be found for this case, it may also be interesting to consider an extension with search failures in a way analogous to BSTs, where the misses occur over an edge (between neighbors) or "beyond" a leaf, with their own frequencies.

### Optimality Questions and Alternative Approaches

1. Can we extend the LP, or formulate an alternative which could be shown to have no integrality gap? Can the dual formulation (Section 4) be useful?<tbc>

2. Can more general tools help? For example Quadratic Programming (QP) or Semi-Definite Programming (SDP)?<tbc>

3. Is it useful to view the optimization problem in bilinear terms of minimizing the expression \(\mathbf{1}^T\cdot X\cdot f\) where **1**_<sup>T</sup>_ is an all-ones row vector, _f_ are the frequencies, and _X_ is the matrix of the _X<sub>ij</sub>_ variables subjected to the LP constraints?<tbc>

4. The paper \[7\] gives a general way to transform dynamic programming (DP) formulations to linear programs (LP), thus one may take Knuth’s DP for BSTs \[10\], or the _k_-cut trees DP of \[5\], and try to generalize it to all STTs. For the details of the latter DP, see Chapter 5 in the thesis of Berendsohn \[4\].<tbc>

5. Can we prove that the LP approach with root rounding is optimal for a sub-class of topologies other than stars (Theorem 3.9)? The most interesting and promising candidates are probably (a) the class of paths, and (b) the class of graphs with edge-diameter of 3 ("almost stars") for which we do not know if the LP itself is integer.<sup>13</sup>

<sup>13</sup>The LP is known to be non-integer for edge-diameter 4 and above by studying the path over 5 nodes. This is discussed in more details in Section 5.2. Moreover the _D_-space projection of the LP is non-integer for edge-diameter 5 and above by Theorem 2.2.


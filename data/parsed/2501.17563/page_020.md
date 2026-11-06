To conclude this section, we analyze all the vertices of the polytopes for topologies with _n_=2 and _n_=3 nodes, each of these sizes has a single, path, topology. In both cases, there are only integer vertices. When _n_=2, there are no _Z_ variables, the LP is defined as \(X_{12}+X_{21}\ge 1\) for \(X_{12},X_{21}\ge 0\). Overall there are two vertices, one per STT. When _n_=3 the LP becomes more interesting. The following inequalities define the polytope, and  4 lists all 9 vertices: 5 of them correspond to STTs, and 4 more are constructed as detailed in the proof of Theorem 3.7, two of each class.

\(X_{12}+X_{21}\ge 1,X_{23}+X_{32}\ge 1,X_{13}+X_{31}+Z_{213}\ge 1,Z_{213}\le X_{21},Z_{213}\le X_{23}\)

## 3.3 Star Topologies Have Integer Vertices

In this subsection we prove analytically that if the tree topology is a star, then all the vertices of the LP are integer. Section 3.2 explicitly shows this claim for _n_=2,3. Consequently, as a result of Property 2, we get a polynomial-time algorithm to find the optimal static STT (for stars).

**Theorem 3.9.** The LP polytope for a star topology has only integer vertices.

**Corollary 3.10.** An optimal static STT for any star topology is computable in polynomial time.

(The corollary can be proven directly, using a simple enumeration: since the star is very symmetric, there are at most _n_ effective STTs to consider: we always query leaves in decreasing order of weight, and the _n_ STTs vary according to the depth at which we query the central node.)

_Proof of Theorem 3.9._ The LP for a star over _n_ nodes is given in Equation (4), where we denote the center by 1 (recall that _Z_<sub>1_ij_</sub> and _Z_<sub>1_ji_</sub> are the same).

\(\forall i>1:X_{1i}+X_{i1}\ge 1;\forall i,j\neq 1:X_{ij}+X_{ji}+Z_{1ij}\ge 1;\forall i,j\neq 1:Z_{1ij}\le X_{1i};X,Z\ge 0\) (4)

We show that each vertex corresponds to an assignment satisfying the following three conditions:

1. For every \(i,j\neq 1\), \(Z_{1ij}\in\{0,1\}\).<tbc>

2. For each _i_: Let \(z_i\equiv max_{j\neq 1,i}\{Z_{1ij}\}\). We set \(X_{1i}\in\{z_i,1\}\) and _X_<sub>_i_1</sub>=1-_X_<sub>1_i_</sub>.<tbc>

3. For each \(i,j\neq 1\): Choose \(X_{ji}\in\{0,1-Z_{1ij}\}\) and set _X<sub>ij</sub>_=1-_Z_<sub>1_ij_</sub>-_X<sub>ji</sub>_. Explicitly: if _Z_<sub>1_ij_</sub>=1 then _X<sub>ij</sub>=X<sub>ji</sub>_=0, otherwise (_Z_<sub>1_ij_</sub>=0) \(X_{ij}\in\{0,1\}\) and _X<sub>ji</sub>_=1-_X<sub>ij</sub>_.<tbc>

\begin{tabular}{cccccccc}
_X_<sub>12</sub> & _X_<sub>21</sub> & _X_<sub>23</sub> & _X_<sub>32</sub> & _X_<sub>13</sub> & _X_<sub>31</sub> & _Z_<sub>213</sub> & Comments \\
0 & 1 & 0 & 1 & 0 & 1 & 0 & STT: root 3, leaf 1 \\
0 & 1 & 0 & 1 & 1 & 0 & 0 & non-STT: cyclic ancestry \\
0 & 1 & 1 & 0 & 0 & 0 & 1 & STT: root 2 \\
0 & 1 & 1 & 0 & 0 & 1 & 0 & non-STT: LCA abuse \\
0 & 1 & 1 & 0 & 1 & 0 & 0 & non-STT: LCA abuse \\
1 & 0 & 0 & 1 & 0 & 1 & 0 & STT: root 3, leaf 2 \\
1 & 0 & 0 & 1 & 1 & 0 & 0 & STT: root 1, leaf 2 \\
1 & 0 & 1 & 0 & 1 & 0 & 0 & STT: root 1, leaf 3 \\
1 & 0 & 1 & 0 & 0 & 1 & 0 & non-STT: cyclic ancestry \\
\end{tabular}

4: All the vertices of the LP of the topology over _n_=3 nodes. The vertices with comment of "non-STT: LCA abuse" become non-vertices when we eliminate _Z_<sub>213</sub> as detailed in Section 5.2.


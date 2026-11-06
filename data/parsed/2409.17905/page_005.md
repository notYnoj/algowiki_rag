similar to the potential function arguments used to prove amortized upper bounds on the performance of dynamic algorithms.

Actually, for the sake of symmetry, we prefer to think in terms of oriented triangles. An _oriented triangle_ is a triple {_i,j,k_} of polygon vertices (not necessarily adjacent), together with one of two possible orientations, _ijk=jki=kij_ or _ikj=kji=jik_, such that changing the orientation multiplies by -1: in other words, _w(ijk_)=-_w(ikj_) for all _i,j,k_.

Let _w(T_) be the weight of a triangulation _T_ drawn inside the polygon with all triangles oriented counterclockwise. We draw the initial triangulation _T<sub>i</sub>_ inside the polygon, orienting all triangles counterclockwise. We redraw the final triangulation _T<sub>f</sub>_ so that all of its edges are outside the polygon, orienting all triangles counterclockwise. We obtain a triangulated planar graph _T_ with all triangles oriented counterclockwise and with total weight _w(T_)=_w(T<sub>i</sub>_)-_w(T<sub>f</sub>_). A flip of triangles of _T<sub>i</sub>_ or of _T<sub>f</sub>_ can be seen as a flip in T which preserves the counterclockwise orientation. The central part of the proof consists in showing that any flip of any edge changes the weight of the triangulation by at most 1.

In particular, transforming _T<sub>i</sub>_ into _T<sub>f</sub>_ by doing flips of edges inside the polygon yields a graph with two copies of each triangle of _T<sub>f</sub>_, one inside and one outside the polygon, with opposite orientations, and thus the total weight is 0.

Given a polygon with (_n_+2) vertices, the lower bound will be proved by exhibiting: firstly, a weight function on oriented triangles which satisfies the following _tetrahedral constraints_: for any quadruple {_i,j,k,l_} of polygon vertices,

\(\cdot|w(ijk)+w(jlk)+w(jlk)+w(kli)+w(ilj)|\le 1,\) (1)

(which guarantees that any flip changes the weight by at most 1); secondly, a triangulated planar graph which has a hamiltonian cycle (i.e. which can be viewed as the union of two polygon triangulations, one on each side of the hamiltonian cycle) and has weight 2_n_-6 if all triangles are oriented counterclockwise.

Geometrically, we can consider this planar triangulation as a triangulation of the sphere with all triangles oriented outwards. Each flip corresponds to a tetrahedron. In [2], the idea is to exhibit a sphere triangulation which cannot be extended to a triangulation of the ball with fewer than 2_n_-6 tetrahedra. Since the hyperbolic volume of any tetrahedron is at most a constant _V_<sub>0</sub>, the proof focuses on constructing a sphere triangulation forming a polyhedron of<tbc>


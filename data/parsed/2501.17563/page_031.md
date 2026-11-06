seen that adding these constraints does not remove all non-integer vertices, but one can wonder whether it helps. It turns out to be a double-edged sword.

At a first glance, it has benefits. The small topologies with non-integer vertices that we found have 74 such vertices in total after sieving symmetric copies (revisit  1). For each specific topology, more than half satisfy these constraints, so no topology becomes "truly nicer". Testing singular vertices is sort of cheating, because we need to see how the polytope changes as a whole. When considering the path over 5 nodes, we get promising results. Consider the version without _Z_ variables, as discussed in details in Section 5.2. When we add path-monotonicity constraints, we still have non-integer vertices overall, but instead of having 165 as such (158 half-integer and 7 third-integer), the new polytope only has 4 non-integer vertices, all half-integer. This is not quite fully-integer, but it looks like a promising simplification.

Alas, some topologies are badly affected. Consider topology _U_<sub>(5,1)</sub> (5 nodes, "T"-shaped) which was found to have an integer polytope for the original LP. If we add path-monotonicity constraints, its (_X,Z,D_)-polytope now has half-integer and third-integer vertices. So, to conclude this discussion: while path-monotonicity seem like a clean and simple addition to the LP, it is not clear whether it helps or complicates things.

## 5.4 Multiple Vertices with the Same Depths

Throughout the paper, we sometime discuss vertices in (_X,Z,D_)-space, and sometimes in _D_-space. In particular, the normals method uses _D_-space to solve and find "(_X,Z,D_)-vertices", which we then project back to _D_-space. It is natural to ask whether the projection to _D_-space results in<tbc>

\begin{tabular}{cccccccc}
 & \multicolumn{3}{c}{(_X,Z,D_)-Direction} & \multicolumn{2}{c}{(_X,D_)-Direction} & \multicolumn{2}{c}{_D_-Direction} \\
Path length (_n_) & LP & _Z_-elim. & LP & _Z_-elim. & LP & _Z_-elim. \\
6 & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1\] & \[1\] \\
7 & \[1, 2, 3, 4\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1\] & \[1\] & \[1\] \\
8 & \[1, 2, 3, 4, 5\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1\] & \[1\] \\
9 & \[1, 2, 3, 4, 5\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1\] & \[1\] \\
10 & \[1, 2, 3, 4, 5, 6\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1\] & \[1\] \\
11 & \[1, 2, 3, 4, 7\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1\] & \[1\] \\
12 & \[1, 2, 3, 4, 5, 6, 7, 8, 9, 111, 12, 14\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1\] & \[1\] \\
13 & \[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 16, 20\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1\] & \[1\] \\
14 & \[1, 2, 3, 4, 5, 6, 8, 9, 10,11, 12, 13,18, 20, 23, 43\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1, 2\] & \[1\] & \[1\] \\
15 & \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 22, 23, 28, 40, 47, 80\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1\] & \[1\] \\
16 & \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 20, 22, 23, 24, 26, 28, 34, 36, 39, 46, 58, 67, 87, 92, 111, 134, 174, 257, 261, 522, 999\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1, 2, 3\] & \[1\] & \[1\] \\
\end{tabular}

5: A summary of denominators of vertex coordinates found when solving the LP for path topologies, of different lengths, in six variations. The vertices were found by sampling directions, which is not exhaustive as can be seen since for _n_=5 we know of third-integer vertices in (_X,Z,D_)-space, but here for _n_=6 we have not found such vertices. We chose the objective (weights) in either: (1) a general direction with arbitrary weights for (_X,Z,D_), (2) (_X,D_)-direction with weights 0 for all _Z_, and (3) depths-only direction with non-zero weights only for _D_. In each of these three methods, we solve the LP as in Definition 1.2 (LP column), and its variant where we eliminate _Z_ as in Section 5.2 (_Z_-elim. column). It is clear that an arbitrary direction reveals fractions with increasing denominators, yet they seem to be artifacts of the presence of the _Z_, and are either non-existent or very rare when eliminating _Z_ or when considering (_X,D_) or _D_ directions. Furthermore, all the vertices found in _D_-directions are integer. Among the last five columns, 2 and 3 denominators never appear together, i.e., every vertex is either integer, half-integer or third-integer. However, this fact is an artifact of sampling the rare mixed cases, which exist by Theorem 3.14 (e.g., combine two paths of length _n_=5 with an extra node to get a path of _n_=11).


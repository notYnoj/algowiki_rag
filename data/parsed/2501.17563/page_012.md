**Definition 2.5** (Partially Integer Vertex)**.** We say that an (_X,Z,D_)-vertex is _partially integer_ if its _D_ coordinates are all integer, but at least one _X_ coordinate is non-integer.

**Remark 2.6** (New vertices are half-integer)**.** Partially integer vertices exists, an example is given in Figure 2.7. Therefore, the normals method may technically find partially integer vertices which do not correspond to STTs. Indeed, while Property 2 says that STT-vertices dominate other integer points, it is with respect to fully integral points in (_X,Z,D_)-space.

However, interestingly every new _D_-space vertex that we were able to find has non-integer depths. Partially integer vertices that we found are always projected to non-vertices in _D_-space. Moreover, all depths are half-integer, that is, have coordinates that are 0 or \(\frac{1}{2}\), modulo 1 (some coordinates may be integer, but not all of them). Is all of this an artifact of small sizes (\(n\le 8\)), like the fact that all the polytopes are integer for \(n\le 4\), or is it an inherent property?

**Example 2.7.** The smallest example for a partially integer vertex (Definition 2.5) is for _n_=6, see _P_<sub>1</sub> in Equation (3). We find _P_<sub>1</sub> when solving the LP for the path topology, in some general (_X,Z,D_)-direction.<sup>6</sup> The depths-vector of _P_<sub>1</sub> is dominated by the STT (BST) [2,1,2,0,1,2]. In other cases (not shown) the depths are dominated by a convex combinations of more than one STT. For \(n\le 5\), only the path topology has non-integer vertices, and each has a non-integer _D_ coordinate (and is projected to a non-vertex in _D_-space).

<sup>6</sup>The order of LP variables is defined in the code, in the function named "\_construct\_dictionaries\_PRIMAL" of the _SearchTreeUtilities_ class. The direction according to their order is [0, 5, 5, 1, 2, 3, 1, 4, 1, 1, 3, 3, 1, 4, 2, 2, 3, 5, 3, 1, 1, 3, 5, 4, 2, 2, 6, 0, 2, 1, 5, 3, 3, 1, 5, 4, 4, 5, 3, 2, 1, 6, 3, 5, 2, 3, 4, 5, 3, 2, 2, 1, 0, 3, 5, 2].

U (2,0)
U (6,0)
U (7,0)
9
U (7,3)
U (8,0)
65
U (8,4)
18
U (8,11)
U (3,0)
U (39)
U (6,1)
U (7,1)
U (7,4)
U (8,1)
2
U (8,5)
U (8,12)
U (4,0)
U (6,2)
U (7,2)
U (7,5)
U (8,2)
2
U (8,6)
U (8,13)
U (4,1)
U (6,3)
U (7,6)
U (8,3)
U (8,7)
U (8,14)
U (5,0)
U (7,8)
U (8,19)
U (8,8)
U (8,15)
U (6,4)
U (7,7)
U (8,20)
U (8,9)
U (8,16)
U (8,21)
U (8,10)
U (8,17)
U (8,22)
U (8,18)

Figure 6: All tree topologies with \(2\le n\le 8\) nodes, 47 in total. Each tree is named _U_<sub>(_n,i_)</sub> where _n_ is its number of nodes and _i_ is a running index, over non-increasing diameter. For example, _U_<sub>(_n,_0)</sub> is always the path over _n_ nodes and the last among _U_<sub>(_n,i_)</sub> is the star with _n_ nodes. The number of trees for each _n_ is also known as OEIS sequence A000055 (see: https://oeis.org/A000055). Rectangles group by size _n_, and dashed lines divide by diameter within each group. Color scheme: Green trees are stars, analytically proven to have only integer vertices in (_X,Z,D_)-space. Blue trees were also verified to have only integer vertices in (_X,Z,D_)-space, with computer assistance. Black trees only have integer vertices in _D_-space, but have non-integer vertices in (_X,Z,D_)-space, this is further discussed in Section 5.2. Gray trees may be either blue or black, it was infeasible to verify. Red and purple mark trees with non-integer vertices in _D_-space, i.e., counter-example vertices. The red trees are the unique such tree for _n_=7 and its extensions to _n_=8 (Definition 3.11), while purple trees are additional topologies that cannot be extended from the red tree with 7 nodes. The number of non-integer vertices is written in a gray box near each tree, and in parenthesis is the number of false facets (or, primary directions) by which we found these vertices.


## 4 Defining the weight function

The definition of the weight of a triangle (_ijk_) will essentially depend on the position of its three vertices in _T_.

### 4.1 Defining orientations of triangles

Before defining the actual value of the weight of triangles, we will first choose an orientation for each triangle {_i,j,k_} such that the weight of the triangle will be non-negative for the chosen orientation. (Knowing the sign of _w(ijk_), even if we do not know its exact value, will often be sufficient for checking the tetrahedral constraints 1).

In graph _T_, consider non-crossing shortest paths _p<sub>ij</sub>,p<sub>jk</sub>,p<sub>ki</sub>_ from _i_ to _j_, _j_ to _k_ and _k_ to _i_ respectively. Their concatenation forms a cycle separating _T_ into two connected components. The one with the least area (i.e. with the fewest triangles) is called the _interior_. We define the _triangular region_ (_ijk_) to be the union of all the interiors of such cycles. Informally, (_ijk_) is the "fattest" region formed by geodesics between the vertices. The boundary of this triangular region usually defines a cyclic order on the vertices (except if a vertex is in the interior of the triangular region, or if the triangular region is flat, or if the triangle is so big that the triangular region contains the whole graph _T_). We choose the orientation to be _ijk_ if the vertices occur in that order in the counterclockwise direction around the boundary. Also note (we will use this later) that inclusion of triangular regions induces a natural partial order on triangles. Unless otherwise specified, from now on the "weight of triangle {_i,j,k_}" will refer to the triangle with this chosen orientation.

### 4.2 Defining the weights of triangles

We partition triangles in classes, depending on how many edges they have which are in the graph _T_.

Firstly, triangles of _T_: the triangles which are not adjacent to one of the degree 4 or degree 5 vertices have weight 1. The triangles adjacent to a vertex of degree 4 have weight 3/4. For the triangles adjacent to a vertex of degree 5, their weight, 3/4 or 1, is defined as in figure 8.

Secondly, triangles having exactly two edges of _T_: If the area of their triangular region is 0, they have weight 0. Otherwise the weight is defined as<tbc>


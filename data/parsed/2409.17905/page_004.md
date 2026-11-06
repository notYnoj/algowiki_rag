<tbc>planar dual of this graph is a triangulation of an (_n_+2)-gon with one distinguished polygon edge. This defines a bijection between rooted binary trees with _n_ internal nodes and triangulations of an (_n_+2)-gon with a distinguished polygon edge. A rotation on a binary tree corresponds to a _flip_ in the triangulation, obtained by replacing an edge by the other diagonal of the quadrilateral formed by the two triangles adjacent to this edge. (See figure 2). We define the _flip distance_ between two triangulations _T_<sub>1</sub> and _T_<sub>2</sub> as the minimum number of flips required to transform _T_<sub>1</sub> into _T_<sub>2</sub>. We will prove that the maximum flip distance between triangulations of an (_n_+2)-gon is 2_n_-6.

## 2.2 Amortized analysis : defining a weight function

The proof idea is to define a weight function on triangles, such that the weight of a triangulation is the sum of the weights of its triangles; such that any flip, by destroying two triangles and creating two new triangles, changes the total weight by at most 1; and such that there are two particular triangulations whose weights differ by exactly 2_n_-6. The lower bound follows. This is<tbc>

root
C
root
C
A
B
A
B

Figure 2: Binary trees and triangulations


<tbc>in figure 9: in most cases, they are obtained by using two adjacent triangles of weight 1 in the flip, and are then given weight 1/2. Other cases involve the degree 4 and degree 5 vertices, and are listed in figure 9.

Thirdly, triangles having exactly one edge of _T_: this is the crucial part of the construction. Each such triangle is associated to its isolated vertex _s_ (the vertex which is not an extremity of the edge of _T_). We will define the weight of all triangles associated to _s_ simultaneously by solving a flow problem (one flow problem for each _s_) defined as follows.

We flip every edge opposite to _s_ in the six (or five or four in special cases) triangles of _T_ containing _s_. (The degree of _s_ doubles in the process). We consider the planar dual of the graph _T_ with these six flips, _T(s_). Add a vertex _s_<sub>0</sub> to _T(s_), the source for the flow problem, linked to all the vertices dual to the triangles obtained by doing a flip. Define the value of the source as the sum of the weights of these triangles. The sink for the flow problem is a new vertex _t_<sub>0</sub> linked to all the vertices dual to triangles of weight 3/4, and each edge linked to the sink has capacity 1/4.

We now want to give an orientation to the edges of _T(s_). Let _e_ be an edge of _T(s_) and _ab_ its dual edge of _T_. If triangle {_a,b,s_} is oriented, then we direct _e outwards_ from the triangular region (_abs_).

The next step is to define capacities. We choose two constants _c_ large enough and \(c'>10c\). All oriented edges within distance _c_ of the source or of the sink are given capacity 1/2. All oriented edges within distance \(c'\) of the source or of the sink are given capacity 1/4. Forget the orientation of all the other edges of the graph, and give them capacity 1/4. See figure 10.

3/4
3/4
3/4
1
3/4
3/4
3/4

Figure 8: Defining weights near the special vertices


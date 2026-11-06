<tbc>the two points labeled _v_. The triangular lattice _L_ is a double cover of \(L'\) (except for the edge of _L_ going through _c_): to compute the distance between two points _x_ and _y_ of \(L'\), we take \(y'\), the image of _y_ by the symmetry of center _c_ in _L_, and compute \(d_{L^\prime}(x,y)=min(d_L(x,y),d_L(x,y'))\). See figure 6 for an example, where the distance is \(d_{L^\prime}(x,y)=min(d_L(x,y),d_L(x,y'))=min(6,4)=4\).

We now turn to our problem of constructing a convenient picture of _T_. The same idea can be used, using _L_ as an infinite cover. We obtain the graph depicted in figure 7. Let _c_ denote the center of any one of the black lozenges (formed by two adjacent triangles of _L_). Two vertices of _L_ which are images of each other by the symmetry of center _c_ represent the same vertex of _T_. A fundamental region consists of four big triangular regions, which we label 0,1,2,3. Graph _T_ can be recovered by taking such a fundamental region (dotted in the figure) and suitably identifying the sides (identified vertices are joined by arrows in figure 7).

To compute the distance between vertices _x_ and _y_ in _T_, we consider all the vertices _y<sub>i</sub>_ of _L_ which represent _y_. Then _d<sub>T</sub>(x,y_)=min{_d<sub>L</sub>(x,y<sub>i</sub>_)}. In practice, for a given _x_ in _T_, we take the set of all the representatives of _x_ in _L_, and compute its Voronoi diagram (where distances are computed in _L_). Then for any _y_, _d<sub>T</sub>(x,y_)=_d<sub>L</sub>(x_<sub>0</sub>_,y_<sub>0</sub>), where _x_<sub>0</sub> is an arbitrary (fixed) representative of _x_ and _y_<sub>0</sub> is the representative of _y_ in the Voronoi cell of _x_<sub>0</sub>.<tbc>

y'
V
C
V
u
X
y

Figure 6: Computing distances in \(L'\) using the lattice _L_


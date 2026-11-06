for proving lower bounds on other problems involving structures which evolve through local transformations.

This work stems from the last section of [2] (in the journal version only), which briefly sketched connections between the original proof and linear programming.

More explicitly, each flip of two triangles can be associated to an _oriented tetrahedron_, i.e. a quadruple {_i,j,k,l_}, vertices of the triangles involved, together with a sign giving the direction of the transformation. There are \(N=2\genfrac(){pt}{2}{n+2}{4}\) oriented tetrahedra. The distance between two triangulations _T<sub>i</sub>_ and _T<sub>f</sub>_ is the length of the shortest path transforming _T<sub>i</sub>_ in _T<sub>f</sub>_. To each such path, we associate a vector (_x_<sub>1</sub>_,...,x<sub>N</sub>_), where _x<sub>j</sub>_ is the number of times that the flip corresponding to tetrahedron _j_ occured on the path. The length of the path is _x_<sub>1</sub>+_...+x<sub>n</sub>_, and all _x<sub>j</sub>_’s are non-negative integers. The constraint is that the path must lead from _T<sub>i</sub>_ to _T<sub>f</sub>_. Amazingly, this can be worded as a linear constraint, using the linearity of the boundary operator for simplices: let \(\partial\) be the map<tbc>

\(\{\{i,j,k,l\},+\}\mapsto(ijl)+(jkl)+(kil)+(kji),\)

<tbc>where the image is a formal sum of oriented triangles and we adopt the convention (_ijk_)=-(_kji_). Then the set of formal sums of triangles is an \(\genfrac(){pt}{2}{n}{3}\)-dimensional vector space. One can check that \(\partial\) can be extended to a linear operator:<tbc>

\(\partial:(x_1,\dots,x_N)\mapsto\sum_{1\le j\le N}x_j\partial(\text{tetrahedron}j).\)

<tbc>The constraint that the path must go from _T<sub>i</sub>_ to _T<sub>f</sub>_ then gives:<tbc>

\(\partial((x_1,\dots,x_N))=T_f-T_i,\)

<tbc>where _T<sub>f</sub>_ (resp. _T<sub>i</sub>_) is the formal sum of triangles of the triangulation _T<sub>f</sub>_ (resp. _T<sub>i</sub>_), with counterclockwise orientation. If we solve the following linear program:

\(m^*=min(x_1+\dots+x_N)\)<br>
\(s.t.\left\{\begin{array}{ c }
\forall j,x_j\ge 0 \\
\partial(x_1,\dots,x_N)=T_f-T_i,
\end{array}\right.\)


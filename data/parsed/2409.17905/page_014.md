To show that there exists a flow absorbing all the value coming out of the source, we use the max-flow min-cut theorem (in the straightforward direction), along with the following lemma.

**Lemma 1.** _Any cut in_ \(T(s)\cup\{s_0\}\cup\{t_0\}\) _separating the source s_<sub>0</sub> _from the sink t_<sub>0</sub> _has capacity at least equal to the value of the source._

This is proved by examining orientations, using the representation of _T_ described above (the proof will be in the full version).

Coming back to the problem of defining weights on triangles, if _w_ is the flow through an edge _e_, we give weight _w_ to the triangle _sab_ associated to _s_ and containing the edge _ab_ dual of _e_, oriented so that the flow goes out of the triangle and oriented counterclockwise.

An example is given in figure 11 for a "typical" source (not in the neighborhood of the sink).

Fourthly, we need to define the weight of triangles with no edge of _T_: We will define their weights inductively in order of increasing area of their triangular region. Area 0 triangles are given weight 0. Let (_ijk_) be a triangle of non-zero area. We look at all vertices _l_ in the triangular region (_ijk_) such that (_ijl),(jkl_) and (_kil_) all have area strictly smaller than the area of (_ijk_), and define a function _f(l_):<tbc>

\(f(l)=w(ijl)+w(jkl)+w(kil)-1.\)

T
1/4
S
1/2
1/4
1/2
1/4

Figure 10: Defining capacities


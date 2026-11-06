so that the degree 4 vertices are far from one another in _T_ as we will see later. The weight function on oriented triangles will be defined using graph _T_ and will require computing distances on this graph _T_. Thus we need to understand distances on _T_.

## 3.2 Visualizing distances on _T_

As a warmup, let us start from the planar regular triangular lattice _L_, and show how to use it to represent a triangulated graph \(L'\) where every vertex has degree 6, except for one degree 5 vertex and one adjacent degree 4 vertex, in such a way that distances can easily be computed.

Pick a vertex _u_ from _L_; its 6 edges extend to infinite half-lines which partition the plane into 6 sectors. Removing one sector and identifying the two half-lines bounding it into one half-line _V_ decreases the degree of _u_ by 1. Let _v_ be the neighbor of _u_ on _V_ . Removing the two sectors of _v_ on either side of _V_ and identifying their remaining boundaries decreases _v_’s degree by 2. We obtain the following picture for \(L'\), where the arrows join vertices which are identified (figure 5). Let _c_ denote the center of the segment in _L_ joining<tbc>



Figure 4: The sphere triangulation in the neighborhood of a degree 4 vertex


we will have a lower bound _m_<sup>∗</sup> on the distance between _T<sub>i</sub>_ and _T<sub>f</sub>_. The dual linear program is:

\(M^*=max\left(T_f-T_i\right)\cdot(w_1,\dots,w_{\genfrac(){pt}{2}{n}{3}})\)<br>
\(s.t.\partial^Tw\le(1,1,\dots,1).\)

Since \(M^*\le m^*\), the value of _M_<sup>∗</sup> is also a lower bound.

The constraints of the dual program can be interpreted as follows: for every tetrahedron, the sum of the weights of the four triangles bounding it is at most 1. Thus this _w_ is precisely our weight function on triangles, and our whole proof can be viewed as constructing a feasible solution to the dual program.

In the hyperbolic geometry approach, the authors choose an embedding of the sphere triangulation in space, with one vertex _v_<sub>0</sub> at infinity. We can say that they define a weight function on triangles:

\(w((i,j,k))=Vol(\{i,j,k,v_0\})/V_0,\)

where the volumes are computed in hyperbolic space. If we consider the dual program, in that case the constraints are trivially satisfied, and the cost function is the volume of the sphere triangulation (up to a factor 1_/V_<sub>0</sub>).

It can be hoped that this linear programming interpretation would help providing "natural" amortized analyses for other problems.

## References

[1] Daniel D. Sleator and R. E. Tarjan. _Self-adjusting binary search trees_, J.ACM 32, 1985, 652-686.<br>
[2] D. D. Sleater, R. E. Tarjan and W. P. Thurston. _Rotation distance, triangulations, and hyperbolic geometry_, Journal of the AMS, 1, 3, 1988, 647-681. (Preliminary version in S 1986).


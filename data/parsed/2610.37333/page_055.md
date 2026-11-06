(a)
Brusselator 2D, N = 128
(b)
Brusselator 2D, scaling
(c)
Brusselator 3D, N = 64
103
103
wall time (s)
102
102
wall time (s)
103
101
101
100
100
102
10-1
10-1
10-6
10-5
10-4
104
105
10-7
10-6
10-5
10-4
error
degrees of freedom
error
(d)
Brusselator 3D, scaling
(e)
Brusselator closure, state
(f)
Cahn-Hilliard closure, state
103
103
103
102
wall time (s)
102
102
101
101
101
100
100
100
104
105
104
105
104
105
degrees of freedom
degrees of freedom
degrees of freedom
(g)
Brusselator closure, width
(h)
Cahn-Hilliard closure, width
103
103
diff-soup JIDA
wall time (s)
102
diff-soup JBDF
102
diff-soup JNDF
reverse mode (e to h) forward mode (e to h)
101
101
100
100
102
103
104
105
106
102
103
104
105
106
network weights
network weights

Figure A.15: Work-precision and scaling diagrams for the two-dimensional (a, b) and three-dimensional (c, d) Brusselator and gradient scaling diagrams for the Brusselator (e, g) and Cahn-Hilliard (f, h) closures for the `diff-soup` solvers `JIDA` (navy), `JBDF` (blue), and `JNDF` (light blue), with the marker denoting the solver and the line style the differentiation mode as described in the legend. All benchmarks are run according to the procedure described in Section 7.1. Notably, data points are omitted where the solve did not converge or exceeded the wall cap. (a, c) The work-precision diagrams show the three solvers sharing one performance-accuracy frontier. (b, d) The scaling diagrams show the three solvers exhibiting the same asymptotic scaling within a small factor of one another. (e, f, g, h) The gradient diagrams show the three solvers within a small factor of one another in both differentiation modes, with the mass-matrix solvers `JBDF` and `JNDF` marginally faster on the Brusselator closure and `JIDA` the fastest on the Cahn-Hilliard closure.


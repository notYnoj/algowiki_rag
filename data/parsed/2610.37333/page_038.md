Traditionally, Newton-Krylov methods are used to scale CPU based codes to large problems, since they require only Jacobian-vector products rather<tbc>

(a)
Brusselator, N = 128
(b)
Brusselator, rtol = atol = 10-6
103
103
102
102
wall time (s)
wall time (s)
101
101
100
100
10-1
10-1
10-7
10-6
10-5
10-4
10-3
104
105
error
degrees of freedom
(c)
Cahn-Hilliard + elasticity, N = 64
(d)
Cahn-Hilliard + elasticity, rtol = atol = 10-6
103
103
102
102
wall time (s)
wall time (s)
101
101
100
100
10-1
10-1
10-8
10-7
10-6
10-5
10-4
10-3
104
105
error
degrees of freedom
diff-soup JIDA (device-resident)
SUNDIALS ILU (hybrid)
PETSc multigrid (hybrid)
SUNDIALS GMRES (hybrid)
PETSc ILU (hybrid)

Figure 9: Work-precision and scaling diagrams for the Brusselator (a, b) and the Cahn- Hilliard problem (c, d) for device-resident `diff-soup` (solid blue) and the hybrid GPU execution of SUNDIALS (dash-dot red) and PETSc (dash-dot green), with the marker denoting the particular solver as described in the legend. All benchmarks are run according to the procedure described in Section 7.1. Notably, data points are omitted where the solve did not converge or exceeded the wall cap. (a) The work-precision diagram for the Brusselator problem shows `diff-soup` outperforming both hybrid solvers, with the unpreconditioned Newton-Krylov solver of SUNDIALS following within a small factor and the multigrid-preconditioned PETSc solver trailing by over an order of magnitude. (b) The Brusselator scaling diagram shows `diff-soup` extending its lead over the hybrid SUNDIALS solver as the problem grows, with the PETSc solver trailing by more than an order of magnitude at scale. (c) The Cahn-Hilliard work-precision diagram shows `diff-soup` outperforming both hybrid solvers by one to three orders of magnitude, with the closest being the preconditioned Newton-Krylov solver of SUNDIALS. (d) The Cahn- Hilliard scaling diagram shows only `diff-soup` reaching the largest sizes, with both hybrid solvers growing far more steeply before they stop.


As demonstrated in Figure 8, the selected benchmarks show the `diff-soup` GPU solver far outperforms the other solvers, especially above<tbc>

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
104 degrees of freedom
105
error
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
104 degrees of freedom
105
error
diff-soup JIDA (GPU, cuDSS)
SUNDIALS GMRES
PETSc KLU
Julia SciML FBDF
diff-soup JIDA (CPU, KLU)
SUNDIALS ILU
PETSc ILU
Julia SciML QNDF
SUNDIALS KLU
SUNDIALS SuperLU_MT
PETSc multigrid
MATLAB ode15s

Figure 8: Work-precision and scaling diagrams for the Brusselator (a, b) and the Cahn- Hilliard problem (c, d) for `diff-soup` on GPU (solid blue) and CPU (dashed blue), SUNDIALS (dashed red), PETSc (dashed green), Julia `DifferentialEquations.jl` (dashed purple), and MATLAB (dashed gray), with the marker denoting the particular solver as described in the legend. All benchmarks are run according to the procedure described in Section 7.1. Notably, data points are omitted where the solve did not converge or exceeded the wall cap. (a) The work-precision diagram for the Brusselator problem shows the `diff-soup` GPU solver outperforming all solvers, with the Newton-Krylov solvers of SUNDIALS trailing by a small factor and the other libraries by an order of magnitude or more. (b) The Brusselator scaling diagram shows the `diff-soup` GPU solver exhibiting a transition from fixed overhead to power-law scaling, whereas the CPU based solvers all exhibit a sharper power-law growth. (c) The Cahn-Hilliard work-precision diagram shows a similar order of magnitude improvement of the `diff-soup` GPU solver over the other libraries, with the closest solvers being the sparse direct `SuperLU\_MT` in SUNDIALS and `ode15s` in MATLAB. (d) The Cahn-Hilliard scaling diagram shows the `diff-soup` GPU solver exhibiting a two order of magnitude improvement over the other libraries at scale, with the CPU based solvers again growing more steeply.


## Appendix B. One-dimensional Brusselator comparison

## References

(a)
Brusselator 1D, N = 256
(b)
Brusselator 1D, rtol = atol = 10-6
103
103
102
102
wall time (s)
101
wall time (s)
101
100
100
10-1
10-1
10-2
10-2
10-3
10-7
10-6
10-5
10-4
10-3
103
error
degrees of freedom
diff-soup JIDA
SUNDIALS ILU
PETSc ILU
Julia SciML QNDF
SUNDIALS KLU
SUNDIALS SuperLU_MT
PETSc multigrid
MATLAB ode15s
SUNDIALS GMRES
PETSc KLU
Julia SciML FBDF

Figure B.16: Work-precision (a) and scaling (b) diagrams for the one-dimensional Brusselator for `diff-soup` (solid blue), SUNDIALS (dashed red), PETSc (dashed green), Julia `DifferentialEquations.jl` (dashed purple), and MATLAB (dashed gray), with the marker denoting the particular solver as described in the legend. All benchmarks are run according to the procedure described in Section 7.1. Notably, data points are omitted where the solve did not converge or exceeded the wall cap. Generally, we find that for a one-dimensional problem below the crossover of Figure 5d the fixed overhead of the GPU dominates and the CPU based solvers lead. (a) The work-precision diagram shows the CPU based solvers outperforming `diff-soup`, the fastest of them by over an order of magnitude, with only the multigrid-preconditioned PETSc solver trailing it. (b) The scaling diagram shows `diff-soup` exhibiting a fixed overhead across the ladder, whereas the CPU based solvers exhibit power-law growth.


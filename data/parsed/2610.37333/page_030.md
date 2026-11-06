We note that the eigenvalues of the discrete Laplacian span \(\lambda_1\approx\pi^2\) to \(\lambda_N\approx 4/\Delta x^2\), which causes the stiffness, typically characterized by the ratio of the largest to smallest eigenvalues, to grow as _O(N_<sup>2</sup>) [95]. Furthermore, explicit solvers for the heat equation face a CFL limit on the largest stable time step, \(\Delta t<2/\lambda_N\approx\Delta x^2/2\) for the explicit Euler method, due to the coupling of the temporal and spatial discretizations, so the step count grows as _O(N_<sup>2</sup>) regardless of the accuracy requested. As such, it is common to employ implicit time integrators to achieve unconditional stability with respect to the time step. However, implicit time integrators require a linear solve at every step, which creates a computational burden of _O(N_<sup>3</sup>) per step if dense linear solvers are used. By contrast, `diff-soup` uses the adaptive VSVO time integrators described in Section 2.1 with the sparse numerical methods of Section 2.2, which scale quasilinearly in _N_.

0.25
0.2
0.20
0.15
0.1
0.10
0.05
0.00
0
0.0
0.2
0.4
0.6
0.8
1.0
X

Figure 4: Solution of the heat equation of Eq. (16) at the eleven output times of the benchmark, evenly spaced over \(t\in[0,0.2]\) and colored by time.


## 6. Conclusion

The fast iterative moment (FIM) method developed in \[23\] provides an efficient framework for accelerating steady- state solutions of near-continuum gas flows by alternating between the high-order moment system and the consistent hydrodynamic equations. In this work, the FIM solver is extended to the Shakhov model and further improved through second-order finite volume spatial discretization, an IMEX scheme with implicit treatment of the collision term, and a Newton-multigrid hydrodynamic solver equipped with a new regularization strategy. A local Fourier analysis of a linearized one-dimensional BGK model is performed to investigate the convergence behavior of the original FIM method. The analysis reveals the need for more hydrodynamic iterations at smaller Knudsen numbers and their slower convergence on refined grids, motivating the replacement of the time-integration-based hydrodynamic solver by a Newton-multigrid method. The resulting solver also forms an integrated multilevel method, in which the FIM iteration and Newton-multigrid correction provide acceleration in the velocity and spatial spaces, respectively.

Numerical experiments for planar Couette flow, lid-driven cavity flow, and heat transfer in a bottom-heated cavity demonstrate that the improved FIM solver achieves significantly enhanced efficiency and robustness, particularly at small Knudsen numbers. Generally, one Newton-multigrid step in each alternating iteration is sufficient to maintain fast convergence, thereby substantially reducing the need for case-dependent parameter tuning. The numerical results also show that the proposed solver offers a greater efficiency advantage with second-order spatial discretization than with first-order discretization at small Knudsen numbers. Overall, the proposed method provides a practical and efficient framework for steady-state computation of high-order moment systems in near-continuum gas flows.

## Appendix A. Expression of the moment system (9)

The expression of the moment system (9) is

\(\sum_{j=1}^D\big[\big(\theta\frac{\partial f_{\alpha-e_j}}{\partial x_j}+u_j\frac{\partial f_\alpha}{\partial x_j}+(1-\delta_{|\alpha|,M})(\alpha_j+1)\frac{\partial f_{\alpha+e_j}}{\partial x_j}\big)\)<br>
\(+\sum_{d=1}^3\frac{\partial u_d}{\partial x_j}\big(\theta f_{\alpha-e_d-e_j}+u_jf_{\alpha-e_d}+(1-\delta_{|\alpha|,M})(\alpha_j+1)f_{\alpha-e_d+e_j}\big)\) (A.1)

\(+\frac{1}{2}\frac{\partial\theta}{\partial x_j}\sum_{d=1}^3\big(\theta f_{\alpha-2e_d-e_j}+u_jf_{\alpha-2e_d}+(1-\delta_{|\alpha|,M})(\alpha_j+1)f_{\alpha-2e_d+e_j}\big)\big]=\bar{v}\big(f_\alpha^\text{E}-f_\alpha\big)=\mathcal{Q}_\alpha,|\alpha|\le M,\)

where \(\mathcal{Q}_\alpha\) denotes the \(\alpha\)th Hermite expansion coefficient of the collision term Q(_f_), and \(f_\alpha\) is taken as zero if any component of \(\alpha\) is negative. For the Shakhov model,

\(f_\alpha^\text{E}=\left\{\begin{array}{ c c }
\rho, & \text{if}\alpha=0, \\
\frac{1-Pr}{5}q_j, & \text{if}\alpha=2e_i+e_j,i,j=1,2,3, \\
0, & \text{otherwise.}
\end{array}\right.\) (A.2)

100
FIM-3, Kn = 0.1, M = 10, 72 = 1
FIM-3, Kn = 0.1, M = 10, 72 = 2
FIM-3, Kn = 0.1, M = 10, 72 = 5
FIM-3, Kn = 0.1, M = 10, 72 = 10
FIM-3, Kn = 0.1, M = 10, 72 = 15
FIM-4, Kn = 0.1, M = 10
10-4
10-6
10-8
0
500
1000
1500
2000
2500
Wall-clock time(s)

100
FIM-3, Kn = 0.01, M = 8, 72 = 1
FIM-3, Kn = 0.01, M = 8, 72 = 10
FIM-3, Kn = 0.01, M = 8, 72 = 20
FIM-3, Kn = 0.01, M = 6, 72 = 60
FIM-3, Kn = 0.01, M = 8, 72 = 40
FIM-3, Kn = 0.01, M = 6, 72 = 80
FIM-3, Kn = 0.01, M = 8, 72 = 60
FIM-4, Kn = 0.01, M = 8
10-4
10-6
10-8
0
1000
2000
3000
4000
5000
Wall-clock time(s)

100
FIM-3, Kn = 0.001, M = 6, 72 = 1
FIM-3, Kn = 0.001, M = 6, 72 = 20
FIM-3, Kn = 0.001, M = 6, 72 = 60
FIM-3, Kn = 0.001, M = 6, 72 = 80
FIM-3, Kn = 0.001, M = 6, 72 = 100
FIM-4, Kn = 0.01, M = 6
10-4
10-6
10-8
0
1000
2000
3000
4000
5000
Wall-clock time(s)

(a) _Kn_=0.1

(b) _Kn_=0.01

(c) _Kn_=0.001

Figure 12: Convergence histories for the heat transfer with _N<sub>x</sub>=N<sub>y</sub>_=64 and second-order spatial discretization.


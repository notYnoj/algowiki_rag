sum fixed, without affecting the leading-order convergence factor. This reduces the computational cost because the hydrodynamic stage is much less expensive than the moment stage.

However, this does not explain the observation in \[23\] that a larger \(\gamma_2\) is required when the Knudsen number is smaller. To understand this, we consider the first-order term \(\Lambda_0^{(1)}(k)\) for \(\gamma_1=1\). Since \(\Lambda_0^{(0)}(k)\ge 0\), we have

\(|\Lambda_0(\varepsilon,k)|^2=|\Lambda_0^{(0)}(k)|^2+2\varepsilon\Lambda_0^{(0)}(k)\mathrm{Re}\Lambda_0^{(1)}(k)+O(\varepsilon^2),\)

and therefore, it suffices to study the real part of \(\Lambda_0^{(1)}(k)\). Expanding (C.46) for small nonzero \(|k\Delta x|\) with \(\gamma_2(k\Delta x)^2\checkmark 1\), we obtain

\(\mathrm{Re}\Lambda_0^{(1)}(k)=-\frac{2\nu}{C_{M+1}(2-\nu)^2}\left[(4-\nu)+2\gamma_2(2-\nu)\right]k^2\Delta x+O((k\Delta x)^4).\) (42)

Since the leading-order term of \(\mathrm{Re}\Lambda_0^{(1)}(k)\) is negative for \(0<\nu<1\) and \(\Lambda_0^{(0)}(k)\) is positive, the amplification factor \(|\Lambda_0(\varepsilon,k)|\) increases towards \(|\Lambda_0^{(0)}(k)|\) as \(\varepsilon\) decreases. As a result, for a smaller Knudsen number, one needs to increase \(\gamma_2\) to reduce \(|\Lambda_0^{(0)}(k)|\) and make \(\mathrm{Re}\Lambda_0^{(1)}(k)\) more negative in order to maintain the same convergence factor. This explains the observation in \[23\].

### 3.3. Motivation for an improved hydrodynamic solver

The preceding analysis identifies the remaining bottleneck of the FIM method: the hydrodynamic stage aims to solve the system (28) with SGS iterations, but the number of iterations still depends strongly on both the Knudsen number and the grid resolution. To overcome these limitations, we seek a more efficient solver for the hydrodynamic stage that can achieve the effect of a large \(\gamma_2\) in only a few iterations. Since the actual hydrodynamic system (10) is nonlinear, we will apply Newton’s method to achieve fast convergence. The linear system arising in each Newton iteration is then solved using a multigrid method to efficiently reduce errors over a broad range of spatial frequencies and mitigate the deterioration of convergence under grid refinement.

## 4. Improved FIM method

Based on the considerations above, we now develop the improved FIM method for the full nonlinear high-order moment system (17). Before introducing the Newton-multigrid iteration for the hydrodynamic equations, we first present an IMEX scheme to address the stiffness of the Shakhov collision term in the moment stage.

### 4.1. IMEX scheme for the Shakhov model

Since the collision term is not taken into account in determining the relaxation parameter \(\omega\) by (19), the Richardson iteration (18) may become unstable as the collision term becomes increasingly stiff with decreasing _Kn_. To alleviate this stiffness, we follow the IMEX framework in \[23\] to treat the Shakhov collision term implicitly and the convection term explicitly, which yields

\(f_i^{n+1}-\omega\mathcal{Q}\left(f_i^{n+1}\right)=f_i^n-\omega\mathcal{A}_i\left(\mathbf{f}^n\right),\) (43)

where A_<sub>i</sub>_(**_f_**_<sup>n</sup>_) denotes the remaining part of -R_<sub>i</sub>_(**_f_**_<sup>n</sup>_), namely, the contribution from the spatial discretization of the convection term. Using the truncated expansions (12) and (13), the above equation can be written as

\(\sum_{|\alpha|\le M}\left(f_{i,\alpha}^{n+1}-\omega\mathcal{Q}_{i,\alpha}^{n+1}\right)\mathcal{H}_\alpha^{[u_i^{n+1},\varrho_i^{n+1}]}(\mathbf{v})=\sum_{|\alpha|\le M}g_{i,\alpha}\mathcal{H}_\alpha^{[u_i^n,\varrho_i^n]}(\mathbf{v}).\) (44)

Here, \(g_{i,\alpha}\) denotes the coefficient obtained from the right-hand side of (43), while the Hermite expansion coefficients \(\mathcal{Q}_{i,\alpha}^{n+1}\) of the Shakhov collision term are given according to Appendix A by

\(\mathcal{Q}_{i,\alpha}^{n+1}=\left\{\begin{array}{ c c }
0, & \text{if}|\alpha|=0,1, \\
\bar{\nu}_i^{n+1}\left(\frac{1-\mathrm{Pr}}{5}q_{i,j}^{n+1}-f_{i,\alpha}^{n+1}\right), & \text{if}\alpha=2e_k+e_j,k,j=1,2,3, \\
-\bar{\nu}_i^{n+1}f_{i,\alpha}^{n+1}, & \text{otherwise.}
\end{array}\right.\) (45)


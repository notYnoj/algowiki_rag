Multiplying both sides of (44) by \(\left(1,\nu,|\nu|^2\right)^\mathsf{T}\) and integrating over the velocity space, we obtain

\(f_{i,0}^{n+1}=g_{i,0},u_i^{n+1}=u_i^n+\frac{1}{g_{i,0}}\left(g_{i,e_1},g_{i,e_2},g_{i,e_3}\right)^\mathsf{T},\theta_i^{n+1}=\theta_i^n+\frac{2}{3}\sum_{d=1}^3\frac{g_{i,2e_d}}{g_{i,0}}-\frac{\left|u_i^{n+1}-u_i^n\right|^2}{3}.\) (46)

The right-hand side of (44) is then projected onto the same function space \(\mathcal{F}_M^{[u_i^{n+1},\theta_i^{n+1}]}\) as the left-hand side, yielding

\(\sum_{|\alpha|\le M}\left(f_{i,\alpha}^{n+1}-\omega\mathcal{Q}_{i,\alpha}^{n+1}\right)\mathcal{H}_\alpha^{[u_i^{n+1},\theta_i^{n+1}]}(\nu)=\sum_{|\alpha|\le M}\tilde{g}_{i,\alpha}\mathcal{H}_\alpha^{[u_i^{n+1},\theta_i^{n+1}]}(\nu),\) (47)

with \(\tilde{g}_{i,\alpha}\) denoting the coefficients after projection. Substituting (45) into (47) and matching the coefficients gives

\(f_{i,\alpha}^{n+1}=\left\{\begin{array}{ c c }
\tilde{g}_{i,\alpha}, & \text{if}|\alpha|=0,1, \\
\frac{1}{1+\omega\bar{\nu}_i^{n+1}}\left(\tilde{g}_{i,\alpha}+\omega\bar{\nu}_i^{n+1}\frac{1-\mathrm{Pr}}{5}q_{i,j}^{n+1}\right), & \text{if}\alpha=2e_k+e_j,k,j=1,2,3, \\
\frac{1}{1+\omega\bar{\nu}_i^{n+1}}\tilde{g}_{i,\alpha}, & \text{otherwise,}
\end{array}\right.\) (48)

where the updated heat flux is obtained from (7) as

\(q_{i,j}^{n+1}=\frac{2\tilde{g}_{i,3e_j}+\sum_{d=1}^3\tilde{g}_{i,2e_d+e_j}}{1+\omega\bar{\nu}_i^{n+1}\mathrm{Pr}}.\)

One step of the above IMEX scheme is summarized in **Algorithm 2**. The implicit treatment of the Shakhov collision term improves the numerical stability of the moment iteration, whereas the computational cost per iteration remains essentially the same as that of the Richardson iteration (18).

**Algorithm 2** One step of the IMEX iteration for (17) with the Shakhov model

**Input:** Grid, **_f_**_<sup>n</sup>_

**Output:** The new approximation _f_<sup>_n_+1</sup> denoted by **_f_**<sup>_n_+1</sup>=IMEX (**_f_**_<sup>n</sup>_)

1: Determine the relaxation parameter \(\omega\) from **_f_**_<sup>n</sup>_ by (19);

2: On each grid cell, calculate the right-hand side of (43) and denote it by _g<sub>i</sub>_;

3: Compute \(u_i^{n+1}\) and \(\theta_i^{n+1}\) from _g<sub>i</sub>_ by (46);

4: Project _g<sub>i</sub>_ onto \(\mathcal{F}_M^{[u_i^{n+1},\theta_i^{n+1}]}\) to obtain \(\tilde{g}_i\);

5: Obtain the new approximation \(f_i^{n+1}\) from \(\tilde{g}_i\) by (48);

The IMEX scheme (43) can be naturally reformulated as an IMEX-SGS iteration, with cellwise update given by

\(f_i^{n+1}-\omega_i\mathcal{Q}\left(f_i^{n+1}\right)=f_i^n-\omega_i\mathcal{A}_i\left(f^*\right),\) (49)

where the local relaxation parameter \(\omega_i\) replaces the global one, and **_f_**<sup>∗</sup> is initialized as **_f_**_<sup>n</sup>_. The _i_th component of **_f_**<sup>∗</sup> is immediately replaced by \(f_i^{n+1}\) once the updated value becomes available during the sweeping process.

## 4.2. Newton-multigrid iteration for hydrodynamic equations

To further enhance the efficiency and robustness of the FIM method, the time-integration-based schemes for the hydrodynamic equations, namely (24) and its SGS version, Hydro-SGS (25), are replaced by a Newton-multigrid method. Following \[31-33\], the Newton iteration leads to the linearization

\(\sum_{j\in\mathcal{I}(i)}\frac{\partial\mathcal{R}_i^\mathrm{hydro}\left(U^m\right)}{\partial U_j}\delta U_j^m=-\mathcal{R}_i^\mathrm{hydro}\left(U^m\right),\) (50)


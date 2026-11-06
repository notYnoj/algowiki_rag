**Algorithm 1** One step of the FIM alternating iteration \[23\]

**Input:** Grid, **_f_**_<sup>n</sup>_

**Output:** The new approximation **_f_**<sup>_n_+1</sup> denoted by **_f_**<sup>_n_+1</sup>=FIM\(\big(\)**_f_**_<sup>n</sup>_\(\big)\)

1: Perform \(\gamma_1\) moment iterations for (9) to obtain a new approximation \(\tilde{f}\) from **_f_**_<sup>n</sup>_;

2: Compute \(\tilde{\rho}\), \(\tilde{u}\) and \(\tilde{\theta}\) on all grid cells from \(\tilde{f}\);

3: Prepare hydrodynamic initial guess **_U_**<sup>0</sup> with \(U_i^0=\left[\tilde{\rho}_i,\tilde{\rho}_i\tilde{u}_i,\frac{1}{2}\tilde{\rho}_i\left(3\tilde{\theta}_i+|\tilde{u}_i|^2\right)\right]^\mathrm{T}\) and set _m_=0;

4: Calculate **_U_**<sup>_m_+1</sup> from **_U_**_<sup>m</sup>_ by performing one hydrodynamic iteration for (10) with compatible constitutive relations \(\sigma\), **_q_** and boundary conditions. If \((m+1)\ge\gamma_2\) or \(\|U^{m+1}-U^m\|_1\le tol\), then break; otherwise, let _m_:=_m_+1, and repeat the current step;

5: Extract \(\rho^{m+1}\), **_u_**<sup>_m_+1</sup> and \(\theta^{m+1}\) from **_U_**<sup>_m_+1</sup>;

6: Construct **_f_**<sup>_n_+1</sup> from \(\tilde{f}\) by replacing \(\tilde{\rho}\), \(\tilde{u}\) and \(\tilde{\theta}\) with \(\rho^{m+1}\), **_u_**<sup>_m_+1</sup> and \(\theta^{m+1}\), respectively.

<tbc>where \(\tilde{\sigma}_i\) and \(\tilde{q}_i\) are evaluated from the intermediate moment solution \(\tilde{f}\). The slopes vanish for the first-order discretization, while for the second-order discretization they are given by

\(\tilde{s}_i=\frac{\tilde{\sigma}_{i+1}-\tilde{\sigma}_{i-1}}{2\Delta x},\tilde{s}_i=\frac{\tilde{q}_{i+1}-\tilde{q}_{i-1}}{2\Delta x},\) (23)

where \(\tilde{\sigma}_{i\pm 1}\) and \(\tilde{q}_{i\pm 1}\) are also evaluated from \(\tilde{f}\) on the neighboring cells. The spatial discretization of the hydrodynamic equations is required to be consistent with that of the moment system, including the reconstruction procedure, numerical fluxes, and characteristic wave speeds used in the HLL flux.

In \[23\], the boundary conditions for the hydrodynamic equations are obtained indirectly from the distribution- function boundary treatment of the moment system. In the present method, the ghost-cell values for the hydrodynamic equations are instead obtained directly from the explicit expressions given in Appendix B, thereby simplifying the boundary treatment.

The discrete system (21) can be solved using the Richardson iteration given by

\(U_i^{m+1}=U_i^m+\omega\mathcal{R}_i^\mathrm{hydro}\left(U^m\right),\) (24)

where the relaxation parameter \(\omega\) is again determined by the CFL condition given in (19) and (20). Here, the superscript _m_ corresponds to the iterations for solving the hydrodynamic equations. To improve convergence, the SGS method can be incorporated into (24), yielding

\(U_i^{m+1}=U_i^m+\omega_i\mathcal{R}_i^\mathrm{hydro}\left(U^*\right),\) (25)

where **_U_**<sup>∗</sup> is a vector initialized with **_U_**_<sup>m</sup>_ and updated cell by cell as the new approximation \(U_i^{m+1}\) becomes available during the sweep. For convenience, this SGS iteration is referred to as the Hydro-SGS iteration hereafter.

Numerical experiments in \[23\] indicate that \(\gamma_1\) is often set to 1 or 2 in practice, while \(\gamma_2\) needs to be chosen appropriately to balance the per-iteration cost and the overall convergence rate. When _Kn_ becomes small, \(\gamma_2\) usually needs to be increased to tens or even hundreds to ensure that the hydrodynamic information is sufficiently captured. Replacing the Richardson iteration (24) with Hydro-SGS can improve the convergence of the hydrodynamic solver, but a relatively large \(\gamma_2\) is still required.

## 3. Convergence analysis of the FIM method

One hydrodynamic iteration (24) or (25) is usually faster than one moment iteration due to the smaller number of unknowns. However, a large \(\gamma_2\), which is often required at small _Kn_ \[23\], increases the computational cost of the hydrodynamic stage in each alternating iteration and may reduce the overall efficiency of the FIM method. In order to better understand this behavior and motivate further improvements, we analyze the convergence of the FIM method in the near-continuum regime based on a linearized one-dimensional BGK model. This simplified model retains the essential coupling between the primary macroscopic quantities and nonequilibrium moments while allowing an explicit local Fourier analysis. This section summarizes the main results, while the detailed derivations are provided in Appendix C.


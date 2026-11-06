where \(\mathbf{z}=(x,\tau)\), \(N_{p,n}^{(s)}\) is the number of PDE collocation points on slab _n_ at stage _s_, \(\mathbf{z}_{j,n}^{(s)}\) denotes the corresponding collocation location, and \(\alpha_{j,n}^{(s)}\) is its kernel coefficient. Thus, the PDE collocation locations also serve as kernel represententer sites.

For a fixed slab and stage, let \(\unknown\) collect the unknown coefficients, with the slab and stage indices suppressed for simplicity. Analytical differentiation of the embedded trial solution gives the affine relations

\(\mathbf{u}=\mathbf{u}_\mathrm{in}+D_u\unknown,\)<br>
\(\mathbf{u}_x=\mathbf{u}_{\mathrm{in},x}+D_{u_x}\unknown,\)<br>
\(\mathbf{u}_{xx}=\mathbf{u}_{\mathrm{in},xx}+D_{u_{xx}}\unknown,\)<br>
\(\mathbf{u}_t=D_{u_t}\unknown,\) (34)

where the vectors on the left contain the solution and its derivatives at the PDE collocation points. The vectors **u**<sub>in</sub>, **u**<sub>in_,x_</sub>, and **u**<sub>in_,xx_</sub> contain the incoming profile and its spatial derivatives at those points.

The matrices _D<sub>u</sub>_, _D<sub>u<sub>x</sub></sub>_, _D<sub>u<sub>xx</sub></sub>_, and _D<sub>u<sub>t</sub></sub>_ represent the corresponding contributions of the kernel correction, including derivatives of the analytical embedding factor. The incoming profile has no local-time dependence and therefore contributes nothing to the time derivative.

The discrete nonlinear residual is

\(\mathbf{r}(\unknown)=\mathbf{u}_t+\mathbf{u}\odot\mathbf{u}_x-\nu\mathbf{u}_{xx},\) (35)

where \(\odot\) denotes componentwise multiplication. Differentiating this residual with respect to the kernel coefficients yields

\(J(\unknown)=D_{u_t}+\mathrm{diag}(\mathbf{u}_x)D_u+\mathrm{diag}(\mathbf{u})D_{u_x}-\nu D_{u_{xx}},\) (36)

where \(\mathrm{diag}(\cdot)\) denotes the diagonal matrix formed from a vector.

The nonlinear coefficients are obtained by minimizing the residual in eq. 35 using the analytical Jacobian in eq. 36. Linearized initialization, multiscale kernel refinement, and residual-guided collocation are used in the numerical implementation, with the specific settings described in the benchmark setup.

## 2.5 Residual-adaptive collocation

The continuum-feature kernel formulation permits either fixed or adaptive PDE collocation. A fixed deterministic point distribution is sufficient when it adequately resolves the solution. For problems with localized under-resolution, residual-adaptive collocation can concentrate additional PDE constraints in regions where the current approximation exhibits larger governing-equation residuals.

This refinement mechanism is not required by CFKS itself. It provides an additional resolution strategy that can be combined with linear or nonlinear kernel formulations.

To describe both cases, define the PDE residual operator

\(\mathcal{R}[u]=\left\{\begin{array}{ c c }
\mathcal{L}u-f, & \text{for a linear PDE}, \\
\mathcal{N}[u]-f, & \text{for a nonlinear PDE},
\end{array}\right.\) (37)

where L and N are the prescribed linear and nonlinear differential operators, respectively, and _f_ is the corresponding source function.

Let P<sup>(0)</sup> denote an initial deterministic PDE collocation set, and let _u_<sup>(0)</sup> be the CFKS approximation obtained from this set. We refer to _u_<sup>(0)</sup> as the predictor solution.

The computational region is partitioned into _N<sub>B</sub>_ blocks, denoted by \(\{\Omega_b\}_{b=1}^{N_B}\), where _b_ is the block index. For each block, define an independent residual probe set \(\mathcal{Q}_b\subset\Omega_b\). The probe points are distinct from the PDE collocation locations used to construct the predictor.

At a probe point **q**, the predictor residual is

\(r^{(0)}(\mathbf{q})=\mathcal{R}[u^{(0)}](\mathbf{q}),\) (38)

where _r_<sup>(0)</sup> measures the discrepancy between the governing differential equation and the predictor approximation.

The residual magnitude within each block is characterized by its root-mean-square and maximum values,

\(R_b^\mathrm{rms}=\left(\frac{1}{|\mathcal{Q}_b|}\sum_{\mathbf{q}\in\mathcal{Q}_b}|r^{(0)}(\mathbf{q})|^2\right)^{1/2},R_b^\mathrm{max}=\mathrm{max}_{\mathbf{q}\in\mathcal{Q}_b}|r^{(0)}(\mathbf{q})|.\) (39)


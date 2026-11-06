counterparts are evaluated analytically and used directly in the numerical discretization. For linear problems, this construction leads to symmetric operator-kernel collocation systems, with boundary and initial conditions enforced through constraint-compatible null-space parameterization. For nonlinear problems, the continuum-feature representation is retained, while the unknown coefficients are determined through linearized initialization and nonlinear least-squares residual minimization using analytical kernel derivatives and Jacobians.

The numerical investigations support the proposed formulation from both the feature-representation and differential- equation perspectives. Finite-feature convergence experiments demonstrate that empirical Gaussian-RBF value and operator Gram matrices approach their analytically derived continuum counterparts as the number of sampled features increases. The corresponding finite-feature solutions also approach the deterministic CFKS solution, confirming the computational connection between finite Gaussian-RBF models and the continuum-feature formulation. The linear benchmarks demonstrate the applicability of the analytical operator kernels to oscillatory and multiscale ODEs, second- and fourth-order elliptic problems on irregular domains, singularly perturbed boundary layers, and time-dependent transport equations. Residual-guided collocation enrichment further improves the resolution of localized solution structures without changing the underlying mean kernel in the linear adaptive examples. The transport experiments additionally demonstrate that this strategy can track multiple moving localized features within a spatially global kernel formulation.

The viscous Burgers experiment extends the numerical assessment to a nonlinear differential operator. At the investigated viscosity of \(\nu=0.01\), the continuum-feature mean kernel, analytical constraint embedding, and nonlinear residual minimization provide an accurate approximation of the developing internal transition. The two-stage predictor–corrector procedure combines residual-guided collocation enrichment with narrower prescribed global and local Gaussian kernel widths, producing substantial improvements over the coarse predictor. These results demonstrate the feasibility of extending CFKS to nonlinear PDEs without introducing finite Gaussian-RBF feature realizations. However, because both the collocation distribution and kernel scales are modified between stages, the individual contributions of these refinement mechanisms cannot be isolated from the present experiment. Further assessment across different nonlinear operators and parameter regimes is therefore needed.

The principal significance of CFKS lies in using the continuum-feature limit as a direct computational representation rather than solely as an asymptotic interpretation of a finite feature model. Analytical marginalization removes finite-feature sampling variability while preserving the connection to the underlying Gaussian-RBF representation. Nevertheless, the method retains prescribed Gaussian widths, bounded center distributions, collocation configurations, and regularization parameters, whose selection influences accuracy and conditioning. Moreover, CFKS inherits the dense matrix assembly and linear-algebra costs of global kernel methods, while nonlinear problems require additional iterative computations. The time-dependent experiments also highlight the computational expense associated with residual evaluation and slab-to-slab solution transfer. Future research will address scalable low-rank and iterative kernel formulations, efficient residual evaluation, conditioning-aware parameter selection, and localized or domain- decomposed extensions. Broader nonlinear benchmarks and systematic investigations of collocation and kernel-scale refinement will further clarify the accuracy, robustness, and computational limits of CFKS.

## A From finite features to the CFKS representer form

We briefly show how the CFKS representer form follows from the finite RBF feature model. Consider<tbc>

\(u_M(\mathbf{z})=\frac{1}{\sqrt{M}}\sum_{m=1}^M\beta_m\phi_{\theta_m}(\mathbf{z}),\) (52)

<tbc>and let \(\{\ell_i\}_{i=1}^N\) denote the selected PDE, boundary, and initial functionals. Define the finite feature matrix<tbc>

\(Z_{im}=\frac{1}{\sqrt{M}}\ell_i[\phi_{\theta_m}],\) (53)

<tbc>and the feature vector<tbc>

\(\varphi_M(\mathbf{z})=\frac{1}{\sqrt{M}}\left[\phi_{\theta_1}(\mathbf{z})\cdots\phi_{\theta_M}(\mathbf{z})\right]^\top.\) (54)

<tbc>Then<tbc>

\(u_M(\mathbf{z})=\varphi_M(\mathbf{z})^\top\beta.\) (55)

<tbc>For a minimum-norm feature-space solution satisfying the discrete constraints, the coefficient vector lies in the range of \(Z^\top\) and may therefore be written as<tbc>

\(\beta=Z^\top\alpha,\) (56)


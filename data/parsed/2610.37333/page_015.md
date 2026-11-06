to the Schur complement _S_ of _A_,

\(S\delta_g=-G_g+CA^{-1}G_l,S=D-CA^{-1}B,\) (8)

after which the local increment is recovered as \(\delta_l=-A^{-1}G_l-(A^{-1}B)\delta_g\). In practice, we factorize _A_ only when the setup gate refreshes _W<sub>n</sub>_ and cache the _n<sub>g</sub>_ sparse solves forming _A_<sup>-1</sup>_B_ alongside the factors, so each Newton iterate costs one sparse solve, one small dense solve, and the back-substitution. Since \(n_g\checkmark n_a+n_d\), the Schur system adds negligible cost, and the dense rows and columns never enter the sparse factorization, preserving the local sparsity and the fill-reducing ordering of _A_ [36].

## 2.3. Differentiable Simulation and PDE-constrained Optimization

Recent progress in scientific machine learning has concentrated on differentiable simulation for PDE-constrained applications in learning, inference, design, control, and uncertainty quantification [15, 78, 79, 24, 25]. The PDE- constrained optimization problem takes the form

\(min_\theta\mathcal{L}\big(y(t,\theta),\theta\big),\)<br>
\(\text{s.t.}M(y,t)\cdot y'=f(y,\theta,z(t),t),\) (9)

where L is a scalar cost function and \(\theta\in\mathbb{R}^{n_\theta}\) collects the parameters of interest. Conventional first-order optimization requires the total derivative of the cost with respect to the parameters,

\(\frac{d}{d\theta}\mathcal{L}\big(y(t,\theta),\theta\big)=\frac{\partial\mathcal{L}}{\partial y}\frac{\partial y}{\partial\theta}+\frac{\partial\mathcal{L}}{\partial\theta},\) (10)

where the central quantity is the sensitivity matrix \(\partial y/\partial\theta\in\mathbb{R}^{n\times n_\theta}\), the derivative of the solution with respect to the parameters.

To compute the sensitivity matrix, one must differentiate Eq. (2) with respect to the parameters using either the continuous or discrete sensitivity paradigm. Optimize-then-discretize derives continuous auxiliary equations for the sensitivities and integrates them numerically alongside the state, as in the CVODES and IDAS integrators of SUNDIALS [80, 31] Discretize- then-optimize differentiates the discrete computational graph of the solver program and can be implemented in three ways: hand-derived discrete adjoints, as in PETSc’s `TSAjoint` [33, 81] and FATODE [82]; symbolic derivation of the adjoint from the recorded variational forms of a finite element<tbc>


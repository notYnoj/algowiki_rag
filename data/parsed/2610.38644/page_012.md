### Predictor-corrector slab marching

Sequential slab marching can also be combined with residual-adaptive collocation. In this case, a predictor solution is first computed using an initial deterministic collocation distribution.

Let \(u_n^{(0)}(\mathbf{x},\tau)\) denote the predictor approximation on slab _n_, where the superscript (0) identifies the predictor stage. The predictor satisfies the sequential transfer condition

\(u_n^{(0)}(\mathbf{x},0)=\left\{\begin{array}{ c c }
u_\mathrm{init}(\mathbf{x}), & n=0, \\
u_{n-1}^{(0)}(\mathbf{x},\Delta t_{n-1}), & n>0.
\end{array}\right.\) (48)

The predictor is advanced through the entire temporal interval, with each slab initialized from the preceding predictor slab.

After completing the predictor march, the PDE residual is evaluated at independent probe locations, as described in Section 2.5. The resulting residual indicators identify regions requiring additional collocation resolution.

Let \(\gamma_{b,n}\) denote the refinement level assigned to block _b_ on slab _n_, where _b_ is the spatial-block index. These refinement assignments determine the collocation distribution used for the subsequent corrector computation.

The corrector solution, denoted by \(u_n^{(1)}(\mathbf{x},\tau)\), is then computed through a second sequential march, with

\(u_n^{(1)}(\mathbf{x},0)=\left\{\begin{array}{ c c }
u_\mathrm{init}(\mathbf{x}), & n=0, \\
u_{n-1}^{(1)}(\mathbf{x},\Delta t_{n-1}), & n>0.
\end{array}\right.\) (49)

where the superscript (1) identifies the corrector stage.

The predictor and corrector marches are performed independently, each beginning from the prescribed initial condition. The predictor residual information determines the refined collocation distributions, but the predictor solution is not imposed as the initial profile of the corrector.

Instead, continuity between successive corrector slabs is maintained through the terminal profile of the preceding corrector slab, subject to the selected numerical transfer procedure.

The corrector may retain the prescribed mean kernel used by the predictor or employ different prescribed kernel parameters. In the latter case, residual-guided collocation refinement and kernel-scale refinement are combined within the same sequential solution strategy.

### General characteristics

Sequential space-time-slab marching is compatible with both linear and nonlinear CFKS formulations. The governing PDE is discretized independently within each slab, while the incoming solution profile supplies the initial data required for temporal advancement.

For linear problems, the local coefficients can be determined through the corresponding kernel collocation or constraint- compatible linear least-squares formulation. For nonlinear problems, the same slab decomposition can be combined with linearized initialization and nonlinear residual minimization.

The continuum-feature mean kernel and its analytical differential operators remain applicable within every slab. Temporal decomposition changes the organization of the discrete PDE solve without reintroducing finite Gaussian RBF feature realizations.

Residual-guided predictor-corrector marching is an additional refinement strategy rather than a requirement of the sequential formulation.

## 3 Test Conditions

We consider a set of ODE and PDE benchmarks spanning oscillatory and multiscale one-dimensional problems, irregular two-dimensional geometries, a fourth-order equation, a singularly perturbed boundary layer, time-dependent transport, and a nonlinear viscous conservation law. The governing equations, computational domains, physical conditions, and reference solutions are summarized in  1. For the Poisson and biharmonic problems, the five-petal domain is centered at (0.5,0.5) and its boundary is defined by \(r(\theta)=0.33+0.10\mathrm{cos}(5\theta)\) for \(0\le\theta<2\pi\).


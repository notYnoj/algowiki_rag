## 4.6 Viscous Burgers equation

We next consider the nonlinear viscous Burgers equation to examine the applicability of CFKS beyond linear differential operators. The problem is solved directly at viscosity \(\nu=0.01\) over \([-1,1]\times[0,1]\), with initial condition \(u(x,0)=-sin(\pi x)\) and homogeneous Dirichlet conditions at both spatial boundaries. The numerical solution is compared with a Cole-Hopf reference solution. At this viscosity, nonlinear steepening produces a sharp internal transition near _x_=0, providing a demanding test of the continuum-feature representation, analytical kernel derivatives, and nonlinear residual minimization. The calculation employs a two-stage predictor-corrector strategy combining prescribed multiscale kernel refinement with residual-guided collocation enrichment. Unlike the linear transport experiments, both the collocation distribution and the Gaussian kernel widths are modified between the two stages.

The temporal interval is divided into 40 uniform space-time slabs, each of duration \(\Delta t=0.025\), while the spatial interval is partitioned into 20 equal blocks for residual assessment and collocation refinement. On each slab, the analytical trial-function embedding in (32) preserves the incoming solution profile and homogeneous boundary conditions. After completing a slab, the terminal solution is evaluated on a uniform spatial transfer grid containing 1201 points, with the prescribed boundary values imposed at the endpoints. A cubic-spline interpolant of this terminal profile supplies the incoming solution and its spatial derivatives for the following slab. The predictor and corrector are marched separately through the complete temporal interval, each starting from the prescribed initial condition. The predictor residual information determines the corrector collocation distribution, but the predictor solution is not imposed as the incoming profile of the corrector.

The nonlinear approximation uses the normalized global-local continuum-feature mean kernel defined in (29), with prescribed mixing weight \(\eta=0.30\). The global Gaussian center distribution covers the spatial interval \[-1.3,1.3\], whereas the local component uses the narrower interval \[-0.3,0.3\] to provide additional resolution around the developing internal transition. The corresponding local-time center intervals are \([-0.04,\Delta t+0.04]\) for the global component and \([-0.035,\Delta t+0.035]\) for the local component. Each kernel component is normalized by its diagonal value at the spatial origin and the midpoint of the local time slab. For the Stage-1 predictor, the prescribed spatial and temporal Gaussian widths are (0.20,0.04) for the global kernel and (0.06,0.06) for the local kernel. In Stage 2, these widths are reduced to (0.10,0.02) and (0.015,0.015), respectively. The prescribed kernel parameters remain fixed across the slabs within each stage but differ between the predictor and corrector computations.

The nonlinear coefficient solution on each slab begins with a frozen-advection linearization based on the incoming solution profile, followed by a Picard update. The linearized coefficient systems are solved using singular-value- decomposition (SVD) regularization, with relative ridge factors of 10<sup>-8</sup> and 10<sup>-9</sup> for the frozen-advection and Picard steps, respectively. The resulting coefficients initialize nonlinear least-squares minimization of the full Burgers residual, using the analytical Jacobian derived in (36). The nonlinear solver employs a trust-region reflective algorithm with an<tbc>

Predictor, t = 0.0
Predictor, t = 0.5
Predictor, t = 1.0
Independent residual
1.00
1.00
1.00
1.0
1.0
Predictor
Exact
0.75
0.75
0.8
0.8
0.75
0.75
0.6
0.6
0.50
0.50
0.50
0.4
0.4
0.25
0.25
0.25
0.2
0.2
0.00
0.00
0.00
0.0
0.0
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
x
x
x
Corrector, t = 0.0
Corrector, t = 0.5
Corrector, t = 1.0
Collocation enrichment
1.00
1.00
1.00
1.0
Corrector
0.8
0.75
Exact
0.75
0.75
high
0.6
0.50
0.50
0.50
0.4
mid
0.25
0.25
0.2
low
0.00
0.00
0.00
0.0
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
x
x
x

Figure 5: CFKS results for the advection-diffusion problem. Top row: predictor solutions at representative times and the independently evaluated PDE residual. Bottom row: adaptive corrector solutions and the corresponding space-time collocation enrichment. The enriched region follows the translating and diffusing Gaussian pulse.


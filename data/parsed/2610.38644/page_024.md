<tbc>The adaptive corrector uses an average of 413.0 PDE collocation points per slab, with a range of 384-432. Thus, the residual-based enrichment is not tied to a single localized feature; it can identify and track multiple simultaneously propagating structures while leaving the underlying CFKS kernel and physical constraints unchanged.

## 4.10 Overall observations

The numerical experiments demonstrate the applicability of CFKS across differential problems involving oscillatory solutions, multiscale structures, irregular geometries, higher-order operators, localized boundary layers, time-dependent transport, and nonlinear dynamics. The finite-feature convergence study provides direct numerical evidence that empirical Gaussian-RBF value and operator Gram matrices approach their analytically defined continuum counterparts as the number of sampled features increases. This establishes the connection between finite Gaussian-RBF representations and the deterministic continuum-feature formulation used throughout the paper. The ODE, Poisson, and biharmonic benchmarks further demonstrate that the resulting mean kernel and its analytical derivatives can be employed for differential operators of different orders without introducing separate finite feature realizations. The successful treatment of the irregular five-petal domain also illustrates that the prescribed kernel center-support region need not coincide with the physical computational domain, since the domain geometry and physical conditions enter through the corresponding constraint functionals.

The singularly perturbed and time-dependent transport experiments demonstrate the role of residual-adaptive collocation as an additional resolution strategy within the continuum-feature framework. Independent PDE residual evaluations identify localized regions where the predictor approximation is insufficiently resolved, and the corrector redistributes collocation points accordingly. The singularly perturbed problem shows that concentrating additional constraints near a narrow boundary layer can be more effective than uniform refinement with the same point budget. Similarly, the advection and advection–diffusion experiments demonstrate that residual-guided enrichment can follow moving localized structures, while the two-pulse advection benchmark confirms that multiple separated regions of under-resolution can be identified simultaneously. In these linear examples, the prescribed continuum-feature mean kernel remains unchanged between the predictor and corrector stages; refinement modifies the discrete collocation representation rather than the underlying Gaussian feature distribution.

The viscous Burgers experiment extends the numerical assessment to a nonlinear differential operator. In this setting, the continuum-feature mean kernel defines a deterministic trial representation, while the unknown coefficients are determined through nonlinear least-squares residual minimization. Linearized initialization and analytical kernel derivatives provide the starting approximation, nonlinear residual, and corresponding Jacobian. At the investigated viscosity \(\nu=0.01\), the two-stage procedure substantially improves the resolution of the developing internal transition.<tbc>

Predictor, t= 0.0
Predictor, t= 0.5
Predictor, t= 1.0
Independent residual
1.00
Predictor
1.00
1.00
1.0
1.0
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
-1
0
1
-1
0
1
-1
0
1
-1
0
1
x
x
x
Corrector, t= 0.0
Corrector, t= 0.5
Corrector, t= 1.0
Collocation enrichment
1.00
1.00
1.00
1.0
Corrector
0.75
Exact
0.75
0.8
high
0.75
0.75
0.75
0.6
0.50
0.50
0.50
0.4
mid
0.25
0.25
0.25
0.2
low
0.00
0.00
0.00
0.0
-1
0
1
-1
0
1
-1
0
1
-1
0
1
x
x
x

Figure 10: Periodic advection of two separated Gaussian pulses. Top row: predictor solution at _t_=0,0.5, and 1.0, followed by the independently evaluated residual over the space–time domain. Bottom row: adaptive-corrector solution at the same times and the resulting collocation-enrichment pattern. The residual traces both propagating pulses and directs increased collocation density along their corresponding space–time trajectories.


<tbc>The advection-diffusion problem considers a translating Gaussian pulse on \[0,1\], with advection coefficient _a_=0.5 and diffusion coefficient \(\nu=10^{-3}\). In contrast to pure advection, the exact solution broadens and decreases in amplitude as diffusion acts on the moving pulse. The coarse predictor reproduces the overall translation and spreading but increasingly underestimates the pulse amplitude, yielding a final RMSE of \(4.36\times 10^{-2}\) and a maximum absolute error of \(1.51\times 10^{-1}\). As shown in Fig. 5, the independent residual again identifies the moving region of strongest local variation, while the enriched collocation band broadens consistently with the diffusive spreading of the solution. The adaptive corrector reduces the final RMSE to \(9.42\times 10^{-4}\) and the maximum absolute error to \(3.46\times 10^{-3}\). The corrector employs an average of 326.2 PDE points per slab, with the number varying between 304 and 344 according to the residual-guided refinement pattern.

For the advection-diffusion predictor, kernel assembly, spectral factorization, and coefficient solution require approximately 0.061, 0.047, and 0.048 s, respectively, resulting in a core CFKS time of 0.156 s. Residual probing requires 31.98 s, while slab prediction and transfer require 20.13 s. The adaptive corrector has a core CFKS time of 3.10 s, of which 2.69 s is spent on cached spectral factorizations for 52 distinct refinement patterns. The total Stage-2 elapsed time is 30.80 s. Together with the pure advection results, these measurements show that the numerical cost of the slab-based computations is influenced strongly by residual diagnostics, prediction-grid evaluation, and solution transfer, rather than solely by assembly and solution of the operator-kernel systems.

Taken together, the two transport experiments demonstrate that residual-adaptive CFKS can concentrate collocation resolution along moving localized structures while preserving the underlying continuum-feature representation. In the pure advection case, the enrichment follows the narrow trajectory of the periodically transported pulse, whereas in the advection-diffusion case it adapts to a translating and broadening profile. The accuracy improvements are obtained by changing the locations and number of discrete PDE constraints rather than introducing additional finite Gaussian-RBF features or sampling new feature centers. This distinction is important because the adaptive procedure operates on the discretization of the governing equations while the analytically prescribed mean kernel remains unchanged. The results also indicate that improving the efficiency of residual probing and slab-to-slab transfer is a relevant direction for reducing the overall computational cost of time-dependent CFKS implementations.

Closely related sharp-gradient transport benchmarks were previously used to motivate the distributed physics-informed extreme learning machine (PIELM) formulation \[21\], in which spatial domain decomposition was introduced to improve the resolution of localized solution structures. In contrast, the present CFKS computations retain a spatially global continuum-feature kernel representation within each time slab, without introducing artificial spatial interface conditions. Localized structures are instead resolved by redistributing PDE collocation points according to independently evaluated residual information. The resulting calculations illustrate how deterministic population-kernel representations can be combined with adaptive collocation without requiring spatial domain decomposition.

Predictor, t=0.0
Predictor, t=0.5
Predictor, t=1.0
Independent residual
1.00
1.00
1.00
1.00
1.0
Predictor
Exact
0.8
0.75
0.75
0.75
0.8
0.6
0.50
0.50
0.6
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
Corrector, t=0.0
Corrector, t=0.5
Corrector, t=1.0
Collocation enrichment
1.00
1.00
1.00
1.00
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

Figure 4: CFKS results for the linear advection problem. Top row: predictor solutions at representative times and the independently evaluated PDE residual. Bottom row: adaptive corrector solutions and the resulting space-time collocation enrichment. The enriched collocation region follows the trajectory of the advecting Gaussian pulse.


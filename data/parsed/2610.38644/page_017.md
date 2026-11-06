## 4.5 Advection and advection-diffusion

We first consider two time-dependent transport problems to examine the performance of sequential space-time-slab marching and residual-adaptive collocation. The governing equations, computational domains, and reference solutions are summarized in  1. Both experiments employ a deterministic coarse predictor followed by a residual-guided corrector, with the continuum-feature mean kernel retained between the two stages. Independent residual evaluations are used to identify regions of under-resolution and redistribute the PDE collocation points accordingly. Figures 4 and 5 illustrate the resulting predictor and corrector solutions, residual distributions, and space-time collocation patterns.

For the linear advection problem, a narrow Gaussian pulse propagates periodically across the spatial domain \[-1,1\] with unit advection speed. The coarse predictor captures the overall motion of the pulse but accumulates visible phase and amplitude errors during propagation. At the final time _t_=1, the predictor has a root-mean-square error (RMSE) of \(6.53\times 10^{-2}\) and a maximum absolute error of \(3.73\times 10^{-1}\). The independently evaluated residual identifies a narrow moving region of under-resolution, producing a high-attention space-time band aligned with the pulse trajectory, as shown in Fig. 4. Residual-guided collocation enrichment follows this band and reduces the final RMSE to \(2.87\times 10^{-3}\) and the maximum absolute error to \(2.13\times 10^{-2}\). The corrector uses an average of 307.0 PDE collocation points per slab, with a minimum of 288 and a maximum of 320 points. The improved agreement with the exact solution demonstrates that localized enrichment can resolve the transported feature without changing the prescribed continuum-feature kernel.

The computational timings distinguish the cost of the kernel solution from the additional operations required for residual diagnostics and sequential transfer. For the advection predictor, kernel assembly, spectral factorization, and coefficient solution over all slabs require approximately 0.085, 0.119, and 0.054 s, respectively, giving a core CFKS time of 0.259 s. Residual probing and slab prediction/transfer require approximately 19.48 and 12.70 s, respectively, and therefore dominate the predictor-stage computational cost. For the adaptive corrector, the core CFKS time increases to 4.64 s, including 0.103 s for full operator-kernel assembly and 4.30 s for cached spectral factorizations associated with 52 distinct refinement patterns. The total Stage-2 elapsed time, including prediction and transfer, is 20.16 s. These measurements indicate that the cost of independent residual evaluation and dense solution transfer can substantially exceed that of the underlying population-kernel coefficient solve.

Predictor: full domain
Predictor: boundary-layer zoom
Independent residual
1.0
1.0
1.0
Predictor
Exact
0.8
0.8
0.8
0.6
0.6
0.6
u
u
0.4
0.4
0.4
attention
0.2
0.2
0.2
0.0
0.0
0.0
0.0
0.2
0.4
0.6
0.8
1.0
0.985
0.990
0.995
1.000
0.0
0.2
0.4
0.6
0.8
1.0
x
x
x
Corrector: full domain
Corrector: boundary-layer zoom
Collocation enrichment
1.0
1.0
Corrector
high
Exact
0.8
0.8
0.6
0.6
mid
u
u
0.4
0.4
level
0.2
0.2
low
0.0
0.0
0.0
0.2
0.4
0.6
0.8
1.0
0.985
0.990
0.995
1.000
0.0
0.2
0.4
0.6
0.8
1.0
x
x
x

Figure 3: CFKS solution of the singularly perturbed problem. Top row: coarse predictor over the full domain, boundary- layer zoom, and independent residual indicator. Bottom row: adaptive corrector over the full domain, boundary-layer zoom, and residual-guided collocation enrichment. The adaptive refinement is concentrated near the boundary layer at _x_=1.


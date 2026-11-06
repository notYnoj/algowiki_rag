<tbc>iterative least-squares linear solver, a maximum of 20 function evaluations, and convergence tolerances of 10<sup>-8</sup> for the objective function, coefficient changes, and gradient norm. This initialization and optimization procedure is used in both stages, so the distinction between the predictor and corrector lies principally in their prescribed kernel scales and collocation distributions.

For the Stage-1 predictor, each of the 20 spatial blocks contains 10 PDE collocation points, giving 200 points per time slab. After completing the predictor march, the nonlinear PDE residual is evaluated on independent probe grids within each block. Each probe grid contains 11 spatial locations and 7 local-time locations, giving 77 residual evaluation points per block. The spatial probe locations extend from 5% to 95% of the block width, while the temporal locations range from \(0.08\Delta t\) to \(0.96\Delta t\). Residual root-mean-square and maximum magnitudes are evaluated separately for each block, and the normalized indicator in (40) is computed using \(\omega=0.7\) and \(\varepsilon=10^{-14}\). The normalization is performed independently within each time slab, allowing the refinement decisions to respond to the spatial distribution of residuals at different stages of the evolution.

The refinement thresholds are prescribed as _s_<sub>mid</sub>=0.10 and _s_<sub>high</sub>=0.35, defining low-, medium-, and high-attention regions. To avoid abrupt changes in collocation density, medium- and high-attention assignments are extended to their immediate neighboring spatial blocks without wrapping around the physical boundaries. High-attention assignments take precedence wherever the expanded regions overlap. The corresponding collocation budgets are _N_<sub>low</sub>=10, _N_<sub>mid</sub>=20, and _N_<sub>high</sub>=30 PDE points per block, with deterministic collocation locations generated using a two- dimensional Halton sequence with bases 2 and 3. Within each block, the selected number of Halton points is mapped to the corresponding spatial and local-time interval. Since the kernel representer sites coincide with the PDE collocation locations, residual-guided enrichment changes both the number of PDE constraints and the dimension of the nonlinear coefficient system. The resulting Stage-2 corrector uses between 350 and 600 PDE points per slab, with an average of 402.75 points.

Figure 6 illustrates the two-stage solution process and its associated collocation refinement. The coarse predictor initially follows the Cole-Hopf reference solution but develops oscillatory errors as the nonlinear internal transition becomes sharper. These discrepancies are especially pronounced near the central gradient at later times, where the independently evaluated PDE residual also identifies increased under-resolution. The Stage-2 corrector allocates additional collocation points around the developing transition while using the narrower prescribed multiscale kernel widths. The corrected solution exhibits substantially improved agreement with the reference, indicating that the combined refinement strategy can resolve localized nonlinear structures more accurately than the coarse predictor.

Predictor, t = 0.25
Predictor, t = 0.5
Predictor, t = 1
Independent residual
1.0
1.0
1.0
1.0
Cole-Hopf
CFKS
0.5
0.5
0.5
0.5
100
0.0
0.0
0.0
0.0
10-1
10-1
block RMS
-0.5
-0.5
-0.5
-0.5
10-2
-1.0
-1.0
-1.0
-1.0
-1
0
1
-1
0
1
-1
0
1
0.0
0.5
1.0
x
x
x
t
Corrector, t = 0.25
Corrector, t = 0.5
Corrector, t = 1
Collocation enrichment
1.0
1.0
1.0
1.0
30
0.5
0.5
0.5
0.5
0.5
0.0
0.0
0.0
20
-0.5
-0.5
-0.5
-0.5
10
-1.0
-1.0
-1.0
-1.0
-1
0
1
-1
0
1
-1
0
1
0.0
0.5
1.0
x
x
x
t

Figure 6: Two-stage multiscale CFKS solution of viscous Burgers’ equation at \(\nu=0.01\). Top row: coarse predictor solutions at _t_=0.25, 0.5, and 1, together with the independently evaluated nonlinear PDE residual. Bottom row: adaptive corrector solutions at the corresponding times and the residual-guided collocation distribution. Dashed curves denote the Cole-Hopf reference solution. The corrector combines increased collocation resolution near the developing internal transition with narrower prescribed multiscale kernel widths.


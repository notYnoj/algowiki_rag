We observe that the dependence on the CG tolerance \(\varepsilon_\mathrm{cg}\) is similar as in the previous example, with \(\varepsilon_\mathrm{cg}=10^{-1}\) already requiring just about half times more the number of iterations than with "exact" solves (\(\varepsilon_\mathrm{cg}=10^{-12}\)). FGAL and FMR behave similarly with FGAL showing a slightly more oscillatory convergence behavior than before. This example also shows stagnation once the residual norm is reduced by a factor of approximately 10<sup>-10</sup> for FGAL and 10<sup>-11</sup> for FMR. Note that here as in all the other plots we always report the norms of "computed" residuals, i.e. residuals which were explicitly computed from the current iterate in each iteration. We attribute the observed stagnation to the relatively high condition number \(\kappa\) of the matrix which makes us expect that the reported residual norms, which rely on explicitly computed residuals, will not go beyond roughly \(\kappa\cdot\varepsilon_\mathrm{mach}\), with \(\varepsilon_\mathrm{mach}\approx 10^{-16}\) being the machine roundoff unit. The reported residual _bounds_ are based on updated quantities, which is why they continue to decrease beyond the point where the computed residuals stagnate.

Interestingly, the numerical computations in \[9\] used only an _incomplete_ Cholesky factorization to solve the systems with _H_--the incomplete Cholesky drop tolerance in Matlab’s `ichol` was set to the relatively small value of 10<sup>-9</sup>. Thus, the experiments reported in \[9\] perform approximate solves only, while the algorithms used there are not flexible. This might be the reason why the experiments in \[9\], as the authors say, could not use larger values than 10<sup>-3</sup> for \(\tau/2\).

The remaining two examples are linear systems that arise when using the implicit midpoint Euler rule when integrating a DOE resulting from a port Hamiltonian<tbc>

cg tolerance = 0.1
cg tolerance = 0.01
100
FGAL
100
FGAL FMR FMR
a posteriori bound
a posteriori bound
10-5
10-5
10-10
10-10
10-15
10-15
0
20
40
60
80
100
120
0
20
40
60
80
100
cg tolerance = 0.001
cg tolerance = 1e-12
100
FGAL
100
FGAL FMR FMR FMR
a posteriori bound
a posteriori bound
10-5
10-5
10-10
10-10
10-15
10-15
0
20
40
60
80
100
0
10
20
30
40
50
60

Fig. 1. _Convergence plots for the convection-diffusion equation, Example 1, four choices for_ \(\varepsilon_\mathrm{cg}\)


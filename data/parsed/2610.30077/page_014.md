<tbc>In the dense-solve runs shown in Figure 3, the discrete energy identity (12) holds to round-off (∼10<sup>-</sup>14-10<sup>-</sup>17) at every step, regardless of whether the initial data is smoothly resolved or deliberately under-resolved and noisy. Since no GMRES tolerance floor is present, mass likewise stays at round-off. In the under-resolved case, the clamp safeguard of Section 3 is active at no more than 9% of the spatial grid points. The coarser, GMRES-tolerance-limited mass conservation reported in Section 7.1 is specific to the larger, iteratively-solved production runs, not a general limitation of the scheme.

## Temporal and spatial convergence.

We check the scheme’s temporal order _p<sub>t</sub>_ (the exponent such that the error shrinks like \(\Delta t^{p_t}\)) in two independent ways. The first is the method of manufactured solutions (MMS) [25, 26], the standard technique for measuring a scheme’s convergence order when no closed-form solution of the original equations is available: we pick an arbitrary smooth function of (_x,t_), substitute it into (1), and add whatever extra forcing term is needed to make that function an exact solution of the resulting, slightly modified system (the explicit function and forcing term used here are given in Appendix B). Because the exact solution is then known in closed form, we can measure the true numerical error directly at each \(\Delta t\) and check how fast it shrinks as \(\Delta t\rightarrow 0\). Doing this with the reference configuration’s own \(b,c,A,\kappa\) forms, but with \(\gamma=0.30\) in place of 10<sup>-3</sup> and _N_=40 (both chosen large enough that the spatial grid is not the bottleneck at any \(\Delta t\) tested), gives _p<sub>t</sub>_≈2.00 for the backward-Euler startup and, for the Richardson startup, an order climbing from 1.68 to 1.95 as \(\Delta t\rightarrow 10^{-4}\), approaching 2 (Figure 4). The second check is directly at the physical \(\gamma=10^{-3}\) (_N_=160, tiny perturbation IC), where no manufactured solution is used; instead we estimate the order by self-convergence, comparing the numerical solutions obtained at successively halved \(\Delta t\) against one another rather than against a known exact solution, which gives _p<sub>t</sub>_=1.98,2.00. For the spatial discretisation, the Fourier-Galerkin method is expected to converge spectrally on smooth data, meaning the error should fall off faster than any fixed power of 1_/N_ as _N_ increases: starting from a smooth but sharply peaked (Lorentzian-shaped) initial condition and measuring the error relative to a highly resolved reference run at _N_=160, the error drops by a factor of 10<sup>7</sup> as _N_ increases from 16 to 96, confirming this spectral rate.

## Agreement with an independent discretisation.

The two checks above test the scheme’s time-stepping order against itself or against a forcing term built with the same code; a bug shared<tbc>

Discrete energy identity (*), every step (reference coefficients, dense solve)
10-13
resolved smooth IC (max clamp frac 0.00) under-resolved noisy IC (max clamp frac 0.09)
10-14
relative (*) residual
10-15
10-16
10-17
5
10
15
20
25
30
35
40
step n

Figure 3: Relative (⋆) residual (12), every step, dense solve: resolved smooth IC and under- resolved noisy IC (clamp active), reference coefficients. Both scatter at machine round-off with no drift.


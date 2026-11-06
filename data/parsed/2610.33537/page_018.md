<tbc>0.01 and 0.001, respectively, are considered below. Driven by the motion of the top lid, the gas would finally reach a steady state.

## 5.2.1. Solution validation and spatial DOF comparison

Numerical solutions computed by the second-order FIM solver on the \(64\times 64\) grid are presented in Figure 6, including temperature contours and heat-flux streamlines at _Kn_=0.1, as well as velocity streamlines and normalized velocity profiles along the centerlines at both _Kn_=0.01 and 0.001. Again, the DUGKS solutions obtained by the dugksFoam solver [38] are used as references, with a \(60\times 60\) physical grid employed for all Knudsen numbers and \(81\times 81\) discrete velocity points for _Kn_=0.1 and \(28\times 28\) discrete velocity points for _Kn_=0.01 and 0.001. It can be seen that our results agree well with DUGKS results, validating the applicability of the moment system with moderate orders in the near-continuum flow regime.

The same flow configuration was also investigated in [23], where it was shown that the first-order FIM solver generally requires much finer grids to obtain solutions comparable with the reference results, especially in the near- continuum flow regime. At _Kn_=0.001, even with a grid of \(512\times 512\) cells, the first-order discretization still shows noticeable discrepancies in the size, location, and shape of the primary and secondary vortices compared with the second-order results, as shown in Figure 6c and 7a. To further examine the spatial convergence behavior, the velocity profiles along four representative slices are compared in Figure 7b and 7c. The second-order FIM solver on the \(64\times 64\) grid already agrees well with the DUGKS reference solution, whereas the first-order solver still exhibits visible deviations even on the 2048\(\times\)2048 grid. These results demonstrate the substantially improved spatial resolution of the second-order discretization, which significantly reduces the required spatial DOF without sacrificing solution accuracy and thereby further improves the efficiency of the FIM method in the near-continuum flow regime.

## 5.2.2. Performance of FIM solvers

The first-order IMEX-SGS iteration, FIM-3, and FIM-4 are tested on the \(64\times 64\) grid for all three Knudsen numbers, with the results summarized in  5. Similar to the Couette-flow results, FIM-3 can be accelerated by increasing \(\gamma_2\), and the values of \(\gamma_2\) listed in  5 are selected empirically for the corresponding Knudsen numbers. However, the convergence histories in Figure 8 show that further increasing \(\gamma_2\) provides only limited additional acceleration. In contrast, FIM-4 achieves fast convergence with one Newton-multigrid step in each alternating iteration, i.e., \(\gamma_2=1\), and thus requires no case-dependent parameter tuning. Compared with the tuned FIM-3, FIM-4 is slightly slower at _Kn_=0.1, but becomes substantially more efficient as the Knudsen number decreases. At _Kn_=0.01, the wall-clock time is reduced by factors of approximately 4, while a speedup of about 2 is maintained at _Kn_=0.001. These results demonstrate that one Newton-multigrid step provides an effective hydrodynamic correction for the multi-dimensional FIM framework, achieving high efficiency and robust performance without empirical tuning of \(\gamma_2\).

The results of the second-order solvers for the lid-driven cavity flow are summarized in  6 and the convergence histories are shown in Figure 9. Possibly due to the wider stencil of the second-order discretization, all solvers<tbc>

100
M = 10, Residual-based
M = 10, Kn-based
M = 9, Residual-based
10-2
M = 9, Kn-based
10-4
Residual
10-6
10-8
0
100
200
300
400
500
Wall-clock time(s)

Figure 5: Convergence histories of FIM-4 using different regularizations for the Couette flow at _Kn_=0.1 with _N<sub>x</sub>_=256 and second-order discretization.


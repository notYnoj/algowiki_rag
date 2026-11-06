_Remark_ 1. As shown in the numerical experiments, one step of the Newton-multigrid iteration is generally sufficient to provide an effective correction to the primary macroscopic quantities within the FIM framework. Accordingly, \(\gamma_2=1\) is adopted as the default choice in **Algorithm 1**, which avoids case-dependent tuning of \(\gamma_2\) and contributes to reducing the overall computational time while maintaining fast convergence across all considered Knudsen numbers.

_Remark_ 2. The Newton-multigrid method presented in **Algorithm 3** provides efficient spatial acceleration for the hydrodynamic equations. Incorporated into the alternating iteration framework, it yields an integrated multilevel solver that combines both velocity and spatial coarse-level corrections through the outer FIM iteration and the inner Newton-multigrid iteration, respectively, providing an alternative to the integrated multilevel construction in \[23\].

### 4.3. FIM solvers

Incorporating the improvement strategies introduced above, we summarize a family of FIM solvers in  1, in which different numerical schemes are adopted for the moment system and the hydrodynamic equations. When the Prandtl number is set to Pr = 1 and the first-order discretization is adopted, the FIM-1, FIM-2 and FIM-3 in  1 actually correspond to the FIM solvers investigated in \[23\], among which FIM-3 was shown to achieve the highest efficiency. Therefore, in the present study for the Shakhov model, we mainly focus on FIM-3 and FIM-4 with both first- and second-order discretization, and evaluate their performance through a series of numerical experiments.

## 5. Numerical experiments

In this section, three numerical examples, i.e., the planar Couette flow, the lid-driven cavity flow and the heat transfer in a bottom-heated cavity, are carried out to assess the accuracy, efficiency, and robustness of the proposed first- and second-order FIM solvers. Throughout the experiments, argon gas is considered and the dimensionless collision frequency \(\bar{\nu}\) is given by

\(\bar{\nu}=\sqrt{\frac{\pi}{2}}\frac{1}{Kn}\rho\theta^{1-w},\)

where the viscosity index is _w_=0.81. Three Knudsen numbers in the near-continuum flow regime, namely, _Kn_=0.1, 0.01, and 0.001, are considered. Following \[23\], moment systems of orders _M_=10 and 9 are employed for _Kn_=0.1, _M_=8 and 7 for _Kn_=0.01, and _M_=6 and 5 for _Kn_=0.001, which have been shown to provide sufficiently accurate approximations for the corresponding Knudsen numbers. The steady-state tolerance is set to 10<sup>-8</sup> using the stopping criterion in \[23\], and \(\gamma_1=1\) is adopted for the FIM solvers. The CFL number for choosing \(\omega_i\) in (20) is 0.8, and the Prandtl number is Pr = 2/3. Since the Maxwell boundary condition used here does not determine a unique steady state, the mass-conservation correction in \[20, 21\] is also applied.

All numerical experiments are conducted using a C++ program on Intel Xeon Gold 6248 CPUs at 2.5 GHz. The two-dimensional computations are performed in parallel using four CPU threads.

### 5.1. The planar Couette flow

The first example is the planar Couette flow, which is a frequently used one-dimensional benchmark test \[20, 36, 37\]. For convenience, the same dimensionless settings as in \[18, 20\] are adopted in our tests. The gas lies between two infinite parallel plates with a distance _L_=1. These two plates are maintained at the dimensionless temperature \(\theta^W=1\) and move tangentially with a relative speed _u<sup>W</sup>_=1.2577. The computation starts at the global Maxwellian with \(\rho^0=1\), **_u_**<sup>0</sup>=0, and \(\theta^0=1\). The gas is driven by the motion of the plates and eventually reaches a steady state.

\begin{tabular}{ccc}
\multirow{2}{*}{FIM solver} & \multicolumn{2}{c}{Schemes} \\
 & High-order moment system & Hydrodynamic equations \\
FIM-1 & Richardson iteration (18) & Richardson iteration (24) \\
FIM-2 & IMEX (43) & Richardson iteration (24) \\
FIM-3 & IMEX-SGS (49) & Hydro-SGS (25) \\
FIM-4 & IMEX-SGS (49) & Newton-multigrid method (51) and (54) \\
\end{tabular}

1: FIM solver setup.


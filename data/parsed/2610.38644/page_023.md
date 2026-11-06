## 4.9 Advection with two separated Gaussian pulses

To further test the spatial selectivity of the residual-adaptive procedure, we consider the same periodic advection equation as in Sec. 3, but replace the single Gaussian initial condition with two separated pulses,

\(u(x,0)=\mathrm{exp}\big[-\left(25(x+0.4)\right)^2\big]+\mathrm{exp}\big[-\left(25(x-0.4)\right)^2\big].\) (51)

The two pulses therefore have identical width and are initially centered at _x_=-0.4 and _x_=0.4. The exact periodic solution is obtained by translating the complete initial profile with unit advection speed.

Figure 10 shows that the predictor captures the transport of both pulses but develops localized oscillatory errors near the moving sharp features. The independent residual identifies two distinct space-time trajectories associated with the advecting pulses, and the corrector consequently concentrates additional collocation points along both paths. The final-time predictor error is \(\mathrm{RMSE}=9.16\times 10^{-2}\) with a maximum error of \(3.74\times 10^{-1}\). After residual-guided enrichment, these errors decrease to \(\mathrm{RMSE}=3.31\times 10^{-3}\) and a maximum error of \(1.84\times 10^{-2}\), respectively.

10-1
100
10-2
CFKS VS exact
Relative Gram error
Solution RMSE
10-3
10-4
10-5
10-1
102
103
102
103
Number of finite features M
Number of finite features M

1018
Solution RMSE
10-3
Residual RMS
1017
Baseline
1016
10-4
1015
K(Ared)
Regularized effective condition
1014
Condition number
10-5
Baseline
1013
10-6
1012
1011
10-15
10-13
10-11
10-9
10-7
10-5
0.050
0.075
0.100
0.125
0.150
0.175
0.200
Relative ridge parameter 2rel
Gaussian width σ

Figure 8: Finite-feature convergence toward CFKS. Left: relative errors of the empirical value and operator Gram matrices as the number of sampled Gaussian RBF features _M_ increases; shaded bands denote realization-to-realization variability and the dashed line indicates the _M_<sup>-1/2</sup> reference rate. Right: RMS difference between the finite-feature and CFKS solutions, together with the finite-feature error relative to the exact solution. The dashed horizontal line denotes the CFKS error relative to the exact solution.

Figure 9: Conditioning and regularization study for the first-order oscillatory ODE benchmark. Left: dependence of the CFKS solution RMSE and PDE-residual RMS on the relative Tikhonov parameter \(\lambda_\mathrm{rel}\) at fixed \(\sigma=0.10\). Right: raw reduced-system condition number and regularized effective condition number as the Gaussian width \(\sigma\) is varied. Dashed vertical lines indicate the baseline parameters used in the numerical experiments.


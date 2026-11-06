## 4.8 Conditioning and regularization

Figure 9 examines the sensitivity of CFKS to the two principal numerical parameters using the first-order oscillatory ODE benchmark. The regularization sweep shows the expected trade-off between stabilization and approximation accuracy: insufficient regularization leaves the solve sensitive to small singular values, whereas excessive regularization increases both the solution and residual errors. The baseline value \(\lambda_\mathrm{rel}=10^{-11}\) lies within the stable low-error region.

The lower panel shows that the Gaussian width \(\sigma\) has a strong effect on the conditioning of the reduced operator system. Increasing \(\sigma\) changes the overlap among neighboring population-kernel basis functions and can substantially increase the raw condition number. Tikhonov regularization reduces this effective conditioning burden while preserving the solution accuracy over a useful range of kernel widths. These results motivate the moderate width and weak regularization used throughout the remaining experiments.

t= 0.25
t= 0.5
1.0
Cole-Hopf
CFKS
0.5
0.0
-0.5
-1.0
X
X
t= 0.75
t= 1
1.0
0.5
0.0
-0.5
-1.0
-1.0
-0.5
0.0
0.5
1.0
-1.0
-0.5
0.0
0.5
1.0
X
X

Figure 7: Corrected multiscale CFKS solution of viscous Burgers’ equation at \(\nu=0.01\) compared with the Cole-Hopf reference solution at _t_=0.25, 0.5, 0.75, and 1. The corrected solution closely follows the reference while resolving the developing internal transition near _x_=0.


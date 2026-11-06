<tbc>The quantitative errors at four representative times are summarized in  4. At _t_=0.25, the predictor RMSE is \(9.02\times 10^{-4}\), which decreases to \(2.21\times 10^{-4}\) after correction. As the internal transition develops, the difference between the two stages becomes considerably more pronounced. At _t_=0.5, the predictor RMSE of \(4.65\times 10^{-2}\) is reduced to \(3.44\times 10^{-4}\), while at _t_=0.75 the corresponding values are \(5.97\times 10^{-2}\) and \(4.70\times 10^{-4}\). At the final time _t_=1, the predictor has an RMSE of \(4.83\times 10^{-2}\) and a maximum absolute error of \(3.01\times 10^{-1}\), whereas the corrector reduces these values to \(4.55\times 10^{-4}\) and \(1.81\times 10^{-3}\), respectively. The final-time RMSE is therefore reduced by approximately a factor of 106.

Figure 7 provides a further comparison between the corrected CFKS solution and the Cole-Hopf reference at _t_=0.25, 0.5, 0.75, and 1. The corrected approximation remains in close agreement with the reference throughout the simulation, including the increasingly steep internal transition near _x_=0. Both the amplitude and position of this localized structure are reproduced without spatial domain decomposition or viscosity continuation. The improvement should, however, be interpreted as the combined effect of residual-guided collocation enrichment and refinement of the prescribed Gaussian kernel widths, since these two changes are introduced simultaneously in the corrector.

Overall, the Burgers experiment demonstrates that the continuum-feature mean-kernel representation can be extended to nonlinear PDEs through linearized initialization and nonlinear least-squares residual minimization. Analytical kernel derivatives provide the nonlinear PDE residual and its Jacobian, while the global-local multiscale representation supplies additional flexibility for resolving localized solution structures. The two-stage procedure improves accuracy by combining residual-guided collocation enrichment with prescribed kernel-scale refinement. The computation is performed directly at the target viscosity without introducing finite Gaussian-RBF center sampling, viscosity continuation, or spatial domain decomposition.

## 4.7 Finite-feature to continuum convergence

To verify the finite-feature interpretation of CFKS, we use the first-order oscillatory ODE benchmark defined in Sec. 3,

\(u'(x)=cos(15x),x\in[-2\pi,2\pi],u(0)=0,\) (50)

with exact solution \(u_\mathrm{ex}(x)=\frac{1}{15}sin(15x)\). This case provides a convenient controlled setting in which the finite Gaussian-RBF feature representation and the corresponding CFKS population limit can be compared directly.

Figure 8 verifies numerically that the finite Gaussian-RBF feature representation approaches the CFKS population limit as the number of sampled features _M_ increases. The top panel shows the relative Frobenius errors of the empirical value Gram matrix, \(\|K_M-K_\rho\|_F/\|K_\rho\|_F\), and of the operator-applied Gram matrix, \(\|G_M-G_\rho\|_F/\|G_\rho\|_F\). Both decrease systematically with _M_ and closely follow the reference _M_<sup>-1/2</sup> slope expected for Monte Carlo sampling of the center population. The mean value-kernel error decreases from 1.52 at _M_=25 to \(1.04\times 10^{-1}\) at _M_=5000, while the operator-Gram error decreases from 1.74 to \(1.18\times 10^{-1}\) over the same range. The shrinking realization-to-realization spread further confirms convergence toward a deterministic population kernel.

The bottom panel shows the corresponding effect at the solution level. For small feature counts, the finite-feature approximation remains far from the CFKS solution, with RMS differences of approximately \(6\times 10^{-2}\) for \(M\le 200\). A marked transition occurs once the feature space becomes sufficiently rich: at _M_=500 the mean finite-feature-to-CFKS RMSE falls to \(5.98\times 10^{-5}\), and subsequently decreases to \(4.45\times 10^{-6}\) at _M_=5000. The CFKS solution itself has an RMSE of \(1.54\times 10^{-5}\) relative to the exact solution. At large _M_, the finite-feature solutions therefore converge toward the deterministic CFKS reference, while their realization-dependent variability also decreases.

These results provide direct numerical evidence for the interpretation of CFKS as the population limit of the underlying finite Gaussian-RBF feature model. The continuum formulation removes the finite-feature sampling error and the associated realization variability, while retaining the operator Gram structure obtained from the original RBF representation.<tbc>

\begin{tabular}{ccccc}
 & \multicolumn{2}{c}{Predictor} & \multicolumn{2}{c}{Corrector} \\
_t_ & RMSE & \(L^\infty\) & RMSE & \(L^\infty\) \\
0.25 & \(9.02\times 10^{-4}\) & \(4.69\times 10^{-3}\) & \(2.21\times 10^{-4}\) & \(9.64\times 10^{-4}\) \\
0.50 & \(4.65\times 10^{-2}\) & \(3.32\times 10^{-1}\) & \(3.44\times 10^{-4}\) & \(2.32\times 10^{-3}\) \\
0.75 & \(5.97\times 10^{-2}\) & \(4.16\times 10^{-1}\) & \(4.70\times 10^{-4}\) & \(2.65\times 10^{-3}\) \\
1.00 & \(4.83\times 10^{-2}\) & \(3.01\times 10^{-1}\) & \(4.55\times 10^{-4}\) & \(1.81\times 10^{-3}\) \\
\end{tabular}

4: Predictor and corrector errors for viscous Burgers’ equation at \(\nu=0.01\), evaluated against the Cole-Hopf reference solution.


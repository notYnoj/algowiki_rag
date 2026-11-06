<tbc>(say \(n\in\{100,200,500,1000,1500,2000\}\)) with the others fixed. For each value of the parameter in this range, and for three different GMMs in GMM_<sub>d</sub>(K_) with _d_=3 (shown in Appendix A.3), we sample the data from \(X\sim\mu_0^{\otimes n}60\) times, then run the EM algorithm for _T_ iterations. We run the experiments on three different GMMs taken with random parameters (adding a small term 10<sup>-14</sup>_I<sub>d</sub>_ to the covariances to avoid vanishing eigenvalues). Note that GMM#1 is better conditioned than GMM#2, and GMM#3 is the worst-conditioned. We observe the mean squared error of the fixed point property \(F(\theta_T,X)\approx\theta_T\) by evaluating \(\frac{1}{p}\|\theta_T-F(\theta_T,X)\|_2^2\) with _p_:=_K+Kd+Kd_<sup>2</sup>, measuring the quality of convergence of the EM algorithm. To study the local contractivity of _F_, we compute the spectral norm \(\|\partial_\theta F(\theta_T,X)\|_\mathrm{op}\): if this is close to 0, then locally the iterated function _F<sub>X</sub>_ has a tame behaviour and the OS method is expected to work well, while if it is close to or larger than 1, the local landscape is difficult and the OS method is expected to fail. Finally, we compare the OS and AI gradients (from Eqs. (10) and (11)) to the reference AD gradient by computing the relative MSEs \(\frac{1}{p}\|J_\mathrm{OS}-J_\mathrm{AD}\|_2^2/(\frac{1}{p}\|J_\mathrm{AD}\|_2^2)\) and \(\frac{1}{p}\|J_\mathrm{AI}-J_\mathrm{AD}\|_2^2/(\frac{1}{p}\|J_\mathrm{AD}\|_2^2)\), where _J_<sub>AD</sub> is the AD gradient, which serves as a baseline (see Appendix A.4 for a discussion on this choice). Concerning the impact of the number of components _K_, we defer to Appendix A.9.2, since the findings are less conclusive.

## Impact of the number of samples _n_.

We begin by fixing _d_=3, _K_=3 and _T_=30 and varying \(n\in\{100,200,500,1000,1500,2000\}\). The results are shown in row 1 of Fig. 6, and we observe that EM appears to converge to a fixed point for all _n_, albeit with a large variance in the MSE depending on the sampled GMMs. The spectral norm of the Jacobian is often close to 0.6 and has no clear trend with _n_, hence we expect the OS method to be a very coarse approximation of the true gradient. The quality of the OS gradient is relatively poor, and substantially worse than the AI gradient, whose median MSE is much smaller, but suffers from very high variance (in log space). Comparing GMMs shows that a precise EM convergence leads to high precision for the AI gradient.

## Impact of the number of EM iterations _T_.

Finally, we fix _n_=200_,d_=3 and _K_=3, and vary \(T\in\{1,2,5,10,15,20,30,40\}\) in row 3 of Fig. 6. Reassuringly, increasing the number of iterations _T_ leads to improved convergence of the EM algorithm to better-conditioned points. The convergence speed seems heavily dependent on the GMM, with an additional variance caused by the dataset sampling. In the favourable settings for larger _T_, the AI approximation substantially outperforms the OS approximation. Since the spectral norm of the Jacobian stabilises to values of the order of 0.5, the OS method plateaus at coarse MSEs, even for larger _T_.

GMM#1 median
GMM#1 quantiles
GMM#2 median
GMM#2 quantiles
GMM#3 median
GMM#3 quantiles
Fixed Point MSE
Max Eigenvalue of aF/a0
relative MSE: OS vs AD
relative MSE: AI vs AD
10-6
100
100
10-3
10-10
10-1
10-8
10-14
10-2
10-13
10-18
10-18
Varying n
10-22
10-1
10-3
10-23
10-26
10-4
10-28
500
1000
1500
2000
500
1000
1500
2000
500
1000
1500
2000
500
1000
1500
2000
n
n
n
n
n
n
10-1
100
10-3
10-6
100
10-1
10-9
10-11
10-2
10-15
Varying T
10-16
10-21
10-1
10-3
10-21
10-26
10-27
10-4
0
10
20
30
40
0
10
20
30
40
0
10
20
30
40
0
10
20
30
40
T
T
T
T

Figure 6: Varying the number of samples _n_ and the number of iterations _T_, we study the convergence of EM, the local contractivity of _F_, and the MSEs of the OS and AI gradients against the AD gradient.


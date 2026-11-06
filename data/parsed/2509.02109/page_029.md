<tbc>_T_=30. Note that the FD approximation is extremely intensive numerically, prohibiting its use in practice and even for extensive testing. First, we observe variability between data samples, indicating sensitivity of the methods to the algorithm initialisation (and in turn, convergence). Fortunately, the AD method is close to the AD method at numerical precision in all three cases. Given this observation, the AD method appears to be an adequate baseline.

## A.5 Numerical Comparison of Warm and Cold Initialisation

We compare warm and cold initialisation in a flow between two fixed random GMMs with _K_=3 components in dimension _d_=20 ( 2). For each of two samples of _n_=200 points from the same source GMM, we run 300 outer SGD updates with learning rate 0.05. Both methods differentiate through exactly \(T\in\{1,2,5,10\}\) EM steps. Their only difference is that, after the first outer iteration, the warm run is initialised with the preceding EM fit whereas the cold run retains the same seeded initialisation at every iteration. The GMM weights are fixed and all other settings are identical. For both samples, the warm and cold runs give the same recorded objective and fitted parameters at _T_=10, and the warm run with _T_=1 gives almost the same objective as the ones with larger _T_.

\begin{tabular}{ccccc}
Sample & _T_ & MW\(_2^2\) (warm) & MW\(_2^2\) (cold) & Difference \\
#1 & 1 & 676.5595 & 662.2502 & 14.3093 \\
#1 & 2 & 674.8875 & 670.1658 & 4.7217 \\
#1 & 5 & 674.6132 & 674.6144 & 0.0012 \\
#1 & 10 & 674.6132 & 674.6132 & 0 \\
#2 & 1 & 680.5627 & 622.3420 & 58.2207 \\
#2 & 2 & 680.4759 & 629.5430 & 50.9329 \\
#2 & 5 & 680.4014 & 643.9372 & 36.4642 \\
#2 & 10 & 680.4597 & 680.4597 & 0 \\
\end{tabular}

Relative MSE of AD and FD
10-13
10-14
GMM#1
GMM#2
10-15
GMM#3
10-16
10-17
10-7
10-6
10-5
EFD

Figure 15: Relative MSE of the full automatic differentiation gradient (AD) against the finite differences approximation (FD) for three different GMMs and varying the FD step size \(\varepsilon_\mathrm{FD}\).

2: Comparison between warm-start and cold-start runs.


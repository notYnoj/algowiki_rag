<tbc>scaling factor, Taylor degree, and random seed.

3 reports the median end-to-end times. Dynamic TiGMRES is faster than fully refreshed TiGMRES in all six problems, and IR-TiGMRES is fastest in every problem. Relative to fully refreshed TiGMRES, their arithmetic mean speedups across the six problems are 1.34 and 4.39, respectively. The smallest speedups occur for `railtrack2\_rep`, where the LU factorization dominates the runtime.

4 shows the largest residual for each method, evaluated from the eigenpairs returned by the last timed run. The values range from \(5.41\times 10^{-14}\) to \(1.14\times 10^{-10}\). IR-TiGMRES has the smallest residual in almost every problem.

**7. Conclusions.** In this work, we present Toeplitz infGMRES, which avoids computing full Arnoldi vectors occurring in infGMRES. To address the numerical cancellation in this method, we develop Dynamic TiGMRES, which constructs full Arnoldi vector whenever the cancellation is detected. Numerical experiments show that Dynamic TiGMRES is efficient and accurate.

We further develop a structured representation of the Arnoldi basis in infGMRES. And we apply this structure to the case when _A(s_) has a split form with a small fixed _d_, leading to IR-TiGMRES. Numerical experiments demonstrate computational advantages of IR-TiGMRES in every problem.

The structured representation also yields a residual lower bound for infGMRES. We prove that the linearized residual of infGMRES cannot converge to zero when

\begin{tabular}{ccccccccccc}
Problem & _n_ & _k_ & _N_ & _p_ & _w_ & _t_<sub>FR</sub> & _t_<sub>D</sub> & _t_<sub>IR</sub> & _S_<sub>D</sub> & _S_<sub>IR</sub> \\
`spring` & 3000 & 32 & 1000 & 70 & 1.0E-1 & 13.072 & 10.761 & 2.907 & 1.21\(\times\) & 4.50\(\times\) \\
`acoustic\_wave\_2d` & 9900 & 10 & 500 & 70 & 1.0E1 & 11.261 & 6.745 & 1.566 & 1.67\(\times\) & 7.19\(\times\) \\
`butterfly` & 5041 & 9 & 504 & 50 & 5.0E-1 & 1.975 & 1.610 & 0.695 & 1.23\(\times\) & 2.84\(\times\) \\
`loaded\_string` & 20000 & 10 & 128 & 50 & 4.0E3 & 9.692 & 6.968 & 1.800 & 1.39\(\times\) & 5.38\(\times\) \\
`railtrack2\_rep` & 35955 & 2 & 128 & 32 & 1.0E1 & 9.651 & 9.399 & 8.798 & 1.03\(\times\) & 1.10\(\times\) \\
`gun` & 9956 & 21 & 1000 & 75 & 2.0E5 & 33.208 & 21.716 & 6.263 & 1.53\(\times\) & 5.30\(\times\) \\
\end{tabular}

\begin{tabular}{cccc}
Problem & \(\rho_\mathrm{max}^\mathrm{FR}\) & \(\rho_\mathrm{max}^\mathrm{D}\) & \(\rho_\mathrm{max}^\mathrm{IR}\) \\
`spring` & \(5.41\times 10^{-14}\) & \(5.45\times 10^{-14}\) & \(5.54\times 10^{-14}\) \\
`acoustic\_wave\_2d` & \(5.05\times 10^{-12}\) & \(5.23\times 10^{-12}\) & \(4.89\times 10^{-12}\) \\
`butterfly` & \(6.66\times 10^{-11}\) & \(1.14\times 10^{-10}\) & \(5.72\times 10^{-11}\) \\
`loaded\_string` & \(1.35\times 10^{-13}\) & \(1.12\times 10^{-13}\) & \(9.58\times 10^{-14}\) \\
`railtrack2\_rep` & \(2.06\times 10^{-13}\) & \(2.07\times 10^{-13}\) & \(1.91\times 10^{-13}\) \\
`gun` & \(2.76\times 10^{-12}\) & \(1.28\times 10^{-12}\) & \(1.54\times 10^{-13}\) \\
\end{tabular}

3: Problem sizes, scaling factors, runtimes, and speedup factors for the six NLEVP problems. Here _n_ is the matrix dimension, _k_ is the requested number of eigenvalues, _N_ is the number of contour nodes, and _p_ is the Taylor degree. The scaling factor _w_ is used in \(\widehat{T}(s)=T(s_0+ws)\). The times _t_<sub>FR</sub>, _t_<sub>D</sub>, and _t_<sub>IR</sub> are medians in seconds for fully refreshed TiGMRES, Dynamic TiGMRES , and IR-TiGMRES. The speedup factors are _S_<sub>D</sub>=_t_<sub>FR</sub>_/t_<sub>D</sub> and _S_<sub>IR</sub>=_t_<sub>FR</sub>_/t_<sub>IR</sub>.

4: Largest eigenpair residuals for the six NLEVP problems. The columns \(\rho_\mathrm{max}^\mathrm{FR}\), \(\rho_\mathrm{max}^\mathrm{D}\), and \(\rho_\mathrm{max}^\mathrm{IR}\) give the largest residual (6.1) for each method.


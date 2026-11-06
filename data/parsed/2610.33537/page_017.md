<tbc>328 to 175, with the wall-clock time decreasing to about 11s. Nevertheless, fixing \(\gamma_2=1\) generally provides good convergence without requiring case-dependent parameter tuning.

The convergence histories of FIM-3 and FIM-4 in terms of wall-clock time are shown in Figure 4. FIM-3 generally exhibits stable residual decay, except for the case with \(\gamma_2=80\) at _Kn_=0.001 and _M_=6, whereas FIM-4 maintains stable convergence in all cases shown. Similar to the first-order results, FIM-4 achieves the best overall performance, indicating that one Newton-multigrid step is sufficient to provide an effective hydrodynamic correction even with the second-order spatial discretization.

## 5.1.4. Effect of the new regularization strategy

To investigate the effectiveness of the proposed regularization strategy defined in (53), FIM-4 using the proposed _Kn_-based regularization is compared with that using the original residual-based regularization for the Couette flow with _N<sub>x</sub>_=256. Since the two regularization strategies exhibit nearly identical performance at _Kn_=0.01 and 0.001, only the results at _Kn_=0.1 are reported in  4.

As shown in  4, the proposed _Kn_-based regularization has little influence on the first-order discretization, indicating that the original residual-based regularization is already sufficient. For the second-order discretization at _Kn_=0.1, it reduces the iteration number from 2949 to 1148 for _M_=10 and from 2601 to 1038 for _M_=9, corresponding to a reduction of more than 60%. The convergence histories in Figure 5 further show that the proposed _Kn_-based regularization effectively suppresses the oscillations observed with the residual-based regularization strategy and achieves faster convergence. These results suggest that the _Kn_-dependent term provides additional stabilization for the Newton system under second-order discretization. Therefore, the proposed _Kn_-based regularization is adopted in all FIM-4 computations unless otherwise stated.

## 5.2. Lid-driven cavity flow

The lid-driven cavity flow is one of the most frequently used benchmark tests in the multi-dimensional case. Our setting is the same as in \[21, 39, 40\]. The flow domain is a square cavity with side length _L_=1m. The top boundary (the lid) of the cavity moves to the right at a constant speed _u<sup>W</sup>_=50m/s, while the other walls are fixed. All the solid walls are maintained at a uniform reference temperature of _T_ref=273K. Initially, the argon gas with a molecular mass of \(m_*=6.63\times 10^{-26}\mathrm{kg}\) is uniformly distributed and assumed to be in a Maxwellian equilibrium state with constant density \(\rho^0\), zero mean velocity **_u_**<sup>0</sup>=**0**, and temperature _T_<sup>0</sup>=_T_ref. Three initial densities, namely \(\rho^0=8.58\times 10^{-7}\mathrm{kg}/\mathrm{m}^3\), \(8.58\times 10^{-6}\mathrm{kg}/\mathrm{m}^3\) and \(8.58\times 10^{-5}\mathrm{kg}/\mathrm{m}^3\), corresponding to Knudsen numbers _Kn_=0.1,<tbc>

\begin{tabular}{ccccc}
\multirow{2}{*}{_M_} & \multicolumn{2}{c}{First-order} & \multicolumn{2}{c}{Second-order} \\
 & Residual-based & _Kn_-based & Residual-based & _Kn_-based \\
10 & 653 & 632 & 2949 & 1148 \\
9 & 647 & 629 & 2601 & 1038 \\
\end{tabular}

100
FIM-3, Ka = 0.1, M = 10, 72 = 1
FIM-3, Ka = 0.1, M = 10, 72 = 5
FIM-3, Ka = 0.1, M = 10, 72 = 10
FIM-3, Ka = 0.1, M = 10, 72 = 10
FIM-3, Ka = 0.1, M = 10, 72 = 15
FIM-3, Ka = 0.1, M = 10, 72 = 20
FIM-4, Ka = 0.1, M = 10
FIM-4, Ka = 0.1, M = 10
10-4
10-6
10-8
0
100
200
300
400
500
600
700
800
900
Wall-clock time(s)
Wall-clock time(s)

100
FIM-3, Ka = 0.01, M = 8, 72 = 1
FIM-3, Ka = 0.01, M = 8, 72 = 10
FIM-3, Ka = 0.01, M = 6, 72 = 10
FIM-3, Ka = 0.01, M = 8, 72 = 20
FIM-3, Ka = 0.01, M = 8, 72 = 30
FIM-3, Ka = 0.01, M = 8, 72 = 40
FIM-4, Ka = 0.01, M = 8
FIM-4, Ka = 0.01, M = 6
10-4
10-6
10-8
0
50
100
150
200
250
300
350
400
Wall-clock time(s)
Wall-clock time(s)

100
FIM-3, Ka = 0.001, M = 6, 72 = 1
FIM-3, Ka = 0.001, M = 6, 72 = 10
FIM-3, Ka = 0.001, M = 6, 72 = 30
FIM-3, Ka = 0.001, M = 6, 72 = 50
FIM-3, Ka = 0.001, M = 6, 72 = 50
FIM-3, Ka = 0.001, M = 6, 72 = 80
FIM-4, Ka = 0.001, M = 6
10-4
10-6
10-8
0
100
200
300
400
500
Wall-clock time(s)
Wall-clock time(s)

(a) _Kn_=0.1

(b) _Kn_=0.01

(c) _Kn_=0.001

Figure 4: Convergence histories for the Couette flow with _N<sub>x</sub>_=256 and second-order spatial discretization.

4: Comparison of iteration numbers required by FIM-4 using different regularizations for the Couette flow at _Kn_=0.1 with _N<sub>x</sub>_=256.


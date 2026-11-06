<tbc>more than 30% without noticeably affecting the convergence behavior.

Additionally, a rebound in the number of iterations is again observed for FIM-4 with fixed \(\gamma_2\) at _Kn_=0.001, which can be effectively suppressed by increasing the value of \(\gamma_2\). A supplemental test for _M_=5 shows that increasing \(\gamma_2\) from 1 to 5 reduces the number of iterations from 416 to 95, while the wall-clock time decreases only slightly, from 455.75 s to about 439 s.

\begin{tabular}{ccccccccc}
\multirow{2}{*}{_Kn_} & \multirow{2}{*}{_M_} & \multicolumn{2}{c}{IMEX-SGS} & \multicolumn{2}{c}{FIM-3<sup>†</sup>} & \multicolumn{2}{c}{FIM-4} & \multirow{2}{*}{Speedup <sup>‡</sup>} \\
 & & Steps & Time (s) & Steps & Time (s) & Steps & Time (s) & \\
0.1 & 10 & 2076 & 4173.95 & 274 & 795.75 & 276 & 909.58 & 0.87 \\
 & 9 & 2054 & 3267.26 & 263 & 574.18 & 262 & 670.63 & 0.85 \\
0.01 & 8 & 2604 & 3114.57 & 74 & 321.13 & 42 & 81.08 & 3.96 \\
 & 7 & 2482 & 2287.67 & 70 & 251.10 & 40 & 56.18 & 4.47 \\
0.001 & 6 & 2731 & 1676.43 & 39 & 100.15 & 47 & 50.62 & 1.98 \\
 & 5 & 2610 & 1224.42 & 38 & 80.12 & 46 & 40.73 & 1.97 \\
\end{tabular}

\begin{tabular}{ccccccccc}
\multirow{2}{*}{_Kn_} & \multirow{2}{*}{_M_} & \multicolumn{2}{c}{IMEX-SGS} & \multicolumn{2}{c}{FIM-3<sup>†</sup>} & \multicolumn{2}{c}{FIM-4} & \multirow{2}{*}{Speedup <sup>‡</sup>} \\
 & & Steps & Time (s) & Steps & Time (s) & Steps & Time (s) & \\
0.1 & 10 & 3336 & 4435.14 & 524 & 1293.78 & 504 & 1775.9 & 0.73 \\
 & 9 & 3129 & 3217.69 & 499 & 844.08 & 471 & 1250.1 & 0.67 \\
0.01 & 8 & 8100 & 6186.40 & 258 & 731.21 & 82 & 173.15 & 4.22 \\
 & 7 & 7418 & 4062.74 & 237 & 564.20 & 77 & 122.43 & 4.61 \\
0.001 & 6 & 41117 & 16244.3 & 734 & 1710.64 & 458 & 580.82 & 2.95 \\
 & 5 & 36324 & 9956.71 & 502 & 1478.64 & 416 & 455.75 & 3.24 \\
\end{tabular}

100
FIM-3, Kn = 0.1, M = 10, 72 = 1
FIM-3, Kn = 0.1, M = 10, 72 = 5
FIM-3, Kn = 0.1, M = 10, 72 = 10
10-2
FIM-3, Kn = 0.1, M = 10, 72 = 15
FIM-3, Kn = 0.1, M = 10, 72 = 20
FIM-4, Kn = 0.1, M = 10
10-4
10-6
10-8
0
500
1000
1500
2000
Wall-clock time(s)
Wall-clock time(s)

100
FIM-3, Kn = 0.01, M = 6, 72 = 1
FIM-3, Kn = 0.01, M = 6, 72 = 10
FIM-3, Kn = 0.01, M = 6, 72 = 20
FIM-3, Kn = 0.01, M = 6, 72 = 40
FIM-3, Kn = 0.01, M = 6, 72 = 40
FIM-3, Kn = 0.01, M = 6, 72 = 80
FIM-4, Kn = 0.01, M = 8
10-4
10-6
10-8
0
200
400
600
800
1000
1200
1400
1600
Wall-clock time(s)

100
FIM-3, Kn = 0.001, M = 6, 72 = 1
FIM-3, Kn = 0.001, M = 6, 72 = 10
FIM-3, Kn = 0.001, M = 6, 72 = 60
FIM-3, Kn = 0.001, M = 6, 72 = 80
FIM-3, Kn = 0.001, M = 6, 72 = 80
FIM-4, Kn = 0.001, M = 6
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

5: Performance results of the IMEX-SGS, FIM-3 and FIM-4 for the lid-driven cavity flow at various _Kn_ with _N<sub>x</sub>=N<sub>y</sub>_=64 and first-order discretization.

<sup>†</sup> The parameter \(\gamma_2\) in FIM-3 is set to 10, 40, and 80 for _Kn_=0.1, 0.01, and 0.001, respectively. <sup>‡</sup> The speedup is the acceleration ratio of FIM-4 relative to FIM-3.

(a) _Kn_=0.1

(b) _Kn_=0.01

(c) _Kn_=0.001

Figure 8: Convergence histories for the lid-driven cavity flow with _N<sub>x</sub>=N<sub>y</sub>_=64 and first-order spatial discretization.

6: Performance results of the IMEX-SGS, FIM-3 and FIM-4 for the lid-driven cavity flow at various _Kn_ with _N<sub>x</sub>=N<sub>y</sub>_=64 and second-order discretization.

<sup>†</sup> The parameter \(\gamma_2\) in FIM-3 is set to 10, 40, and 80 for _Kn_=0.1, 0.01, and 0.001, respectively. <sup>‡</sup> The speedup is the acceleration ratio of FIM-4 relative to FIM-3.


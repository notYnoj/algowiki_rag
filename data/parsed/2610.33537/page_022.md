wall-clock times on the \(64\times 64\) grid are listed in  7 and  8 for the first- and second-order discretization, respectively, with the corresponding convergence histories shown in Figure 11 and Figure 12. As in the lid-driven cavity flow, FIM-3 relies on empirical tuning of \(\gamma_2\), whereas FIM-4 employs one Newton-multigrid step in each alternating iteration without case-dependent tuning. Compared with the tuned FIM-3, FIM-4 is moderately less efficient at _Kn=_0.1 but becomes significantly faster at smaller Knudsen numbers, particularly for the second-order discretization. Moreover, its efficiency could potentially be further improved by adopting a Jacobian simplification strategy similar to that proposed in \[41\].

\begin{tabular}{ccccccccc}
\multirow{2}{*}{_Kn_} & \multirow{2}{*}{_M_} & \multicolumn{2}{c}{IMEX-SGS} & \multicolumn{2}{c}{FIM-3<sup>†</sup>} & \multicolumn{2}{c}{FIM-4} & \multirow{2}{*}{Speedup <sup>‡</sup>} \\
 & & Steps & Time (s) & Steps & Time (s) & Steps & Time (s) & \\
0.1 & 10 & 2264 & 4707.65 & 350 & 1037.54 & 363 & 1251.78 & 0.83 \\
 & 9 & 2208 & 3564.67 & 341 & 741.98 & 362 & 962.90 & 0.77 \\
0.01 & 8 & 3170 & 3897.69 & 88 & 241.27 & 62 & 126.31 & 1.91 \\
 & 7 & 3008 & 2847.76 & 84 & 181.50 & 59 & 90.20 & 2.01 \\
0.001 & 6 & 3672 & 2444.45 & 52 & 117.56 & 65 & 72.77 & 1.62 \\
 & 5 & 3549 & 1804.98 & 51 & 88.75 & 64 & 55.11 & 1.61 \\
\end{tabular}

\begin{tabular}{ccccccccc}
\multirow{2}{*}{_Kn_} & \multirow{2}{*}{_M_} & \multicolumn{2}{c}{IMEX-SGS} & \multicolumn{2}{c}{FIM-3<sup>†</sup>} & \multicolumn{2}{c}{FIM-4} & \multirow{2}{*}{Speedup <sup>‡</sup>} \\
 & & Steps & Time (s) & Steps & Time (s) & Steps & Time (s) & \\
0.1 & 10 & 3952 & 4948.82 & 669 & 1602.53 & 685 & 2518.59 & 0.64 \\
 & 9 & 3368 & 3463.51 & 631 & 1148.13 & 613 & 1641.27 & 0.70 \\
0.01 & 8 & 10725 & 8313.79 & 299 & 842.87 & 126 & 280.90 & 3.00 \\
 & 7 & 9814 & 5490.72 & 274 & 599.04 & 116 & 191.66 & 3.13 \\
0.001 & 6 & 69502 & 28705.4 & 966 & 3438.18 & 765 & 1052.61 & 3.27 \\
 & 5 & 61445 & 17354.4 & 861 & 2672.26 & 691 & 782.22 & 3.42 \\
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

100
FIM-3, Kn = 0.01, M = 8, 72 = 1
FIM-3, Kn = 0.01, M = 8, 72 = 10
FIM-3, Kn = 0.01, M = 8, 72 = 20
FIM-3, Kn = 0.01, M = 8, 72 = 40
FIM-3, Kn = 0.01, M = 8, 72 = 80
FIM-4, Kn = 0.01, M = 8
10-4
10-6
10-8
0
500
1000
1500
2000
Wall-clock time(s)

100
FIM-3, Kn = 0.001, M = 6, 72 = 1
FIM-3, Kn = 0.001, M = 6, 72 = 10
FIM-3, Kn = 0.001, M = 6, 72 = 60
FIM-3, Kn = 0.001, M = 6, 72 = 80
FIM-3, Kn = 0.001, M = 6, 72 = 100
FIM-4, Kn = 0.001, M = 6
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
Wall-clock time(s)

7: Performance results of the IMEX-SGS, FIM-3 and FIM-4 for the heat transfer in a bottom-heated cavity at various _Kn_ with _N<sub>x</sub>=N<sub>y</sub>=_64 and first-order discretization.

<sup>†</sup> The parameter \(\gamma_2\) in FIM-3 is set to 10, 40, and 80 for _Kn=_0.1, 0.01, and 0.001, respectively.

<sup>‡</sup> The speedup is the acceleration ratio of FIM-4 relative to FIM-3.

(a) _Kn=_0.1

(b) _Kn=_0.01

(c) _Kn=_0.001

Figure 11: Convergence histories for the heat transfer with _N<sub>x</sub>=N<sub>y</sub>=_64 and first-order spatial discretization.

8: Performance results of the IMEX-SGS, FIM-3 and FIM-4 for the heat transfer in a bottom-heated cavity at various _Kn_ with _N<sub>x</sub>=N<sub>y</sub>=_64 and second-order discretization.

<sup>†</sup> The parameter \(\gamma_2\) in FIM-3 is set to 10, 40, and 80 for _Kn=_0.1, 0.01, and 0.001, respectively.

<sup>‡</sup> The speedup is the acceleration ratio of FIM-4 relative to FIM-3.


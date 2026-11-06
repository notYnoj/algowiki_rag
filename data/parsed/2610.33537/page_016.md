<tbc>empirically for the corresponding cases. An excessively large \(\gamma_2\) may even lead to loss of convergence, as shown in Figure 4c for \(\gamma_2=80\) at _Kn_=0.001 and _M_=6. Although convergence can sometimes be recovered by reducing the CFL number and retuning \(\gamma_2\), such case-dependent adjustments limit the robustness and practical applicability of FIM-3. In contrast, FIM-4 employs one Newton-multigrid step in each alternating iteration (\(\gamma_2=1\)) and avoids the parameter tuning required by FIM-3. Even when compared with the carefully tuned FIM-3, FIM-4 achieves substantial speedups, ranging from approximately 1.4 at _Kn_=0.1 to more than 17 at _Kn_=0.001. The advantage of the Newton-multigrid strategy becomes more pronounced for the second-order discretization than in the first-order case, demonstrating its effectiveness for high-resolution computations.

In addition, the total number of iterations of FIM-4 exhibits a slight rebound at _Kn_=0.001 in  3. A supplemental test at _Kn_=0.001 and _M_=5 shows that increasing \(\gamma_2\) from 1 to 2 reduces the iteration number from<tbc>

\begin{tabular}{ccccccccccc}
\multirow{2}{*}{**_Kn_**} & \multirow{2}{*}{**_M_**} & \multicolumn{2}{c}{IMEX-SGS} & \multicolumn{2}{c}{FIM-3} & \multicolumn{2}{c}{FIM-3<sup>†</sup>} & \multicolumn{2}{c}{FIM-4} & \multirow{2}{*}{Speedup <sup>‡</sup>} \\
 & & Steps & Time (s) & Steps & Time (s) & Steps & Time (s) & Steps & Time (s) & \\
0.1 & 10 & 7327 & 1165.12 & 3633 & 537.74 & 664 & 162.38 & 632 & 107.46 & 5.0 / 1.5 \\
 & 9 & 6923 & 839.29 & 3451 & 392.83 & 643 & 118.45 & 629 & 83.91 & 4.7 / 1.4 \\
0.01 & 8 & 20038 & 1875.70 & 10161 & 983.36 & 95 & 28.27 & 87 & 9.13 & 107 / 3.1 \\
 & 7 & 18796 & 1266.87 & 9557 & 666.95 & 88 & 16.11 & 81 & 6.42 & 103 / 2.5 \\
0.001 & 6 & 36192 & 1667.87 & 18364 & 875.84 & 52 & 15.63 & 77 & 4.51 & 194 / 3.4 \\
 & 5 & 34729 & 1081.79 & 17679 & 579.94 & 51 & 13.72 & 78 & 3.42 & 169 / 4.0 \\
\end{tabular}

\begin{tabular}{ccccccccccc}
\multirow{2}{*}{**_Kn_**} & \multirow{2}{*}{**_M_**} & \multicolumn{2}{c}{IMEX-SGS} & \multicolumn{2}{c}{FIM-3} & \multicolumn{2}{c}{FIM-3<sup>†</sup>} & \multicolumn{2}{c}{FIM-4} & \multirow{2}{*}{Speedup <sup>‡</sup>} \\
 & & Steps & Time (s) & Steps & Time (s) & Steps & Time (s) & Steps & Time (s) & \\
0.1 & 10 & 9347 & 1591.86 & 4662 & 794.52 & 1668 & 307.02 & 1148 & 218.26 & 3.6 / 1.4 \\
 & 9 & 8773 & 1121.80 & 4445 & 576.34 & 1399 & 198.28 & 1038 & 153.13 & 3.7 / 1.3 \\
0.01 & 8 & 38003 & 3799.43 & 19318 & 1970.32 & 1367 & 168.86 & 179 & 21.91 & 90 / 7.7 \\
 & 7 & 34630 & 2415.83 & 17663 & 1258.12 & 1282 & 119.51 & 161 & 14.81 & 85 / 8.0 \\
0.001 & 6 & 2.4e5 & 11759.7 & 1.2e5 & 6174.50 & 5037 & 428.34 & 364 & 25.08 & 246 / 17.1 \\
 & 5 & 2.1e5 & 6830.1 & 1.0e5 & 3573.08 & 4455 & 300.04 & 328 & 17.14 & 208 / 17.5 \\
\end{tabular}

100
FIM-3, Ka = 0.1, M = 10, 72 = 1
FIM-3, Ka = 0.1, M = 10, 72 = 5
FIM-3, Ka = 0.1, M = 10, 72 = 10
10-2
FIM-3, Ka = 0.1, M = 10, 72 = 20
FIM-3, Ka = 0.1, M = 10, 72 = 40
FIM-3, Ka = 0.1, M = 10, 72 = 80
FIM-3, Ka = 0.1, M = 10, 72 = 80
10-4
FIM-4, Ka = 0.1, M = 10
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
Wall-clock time(s)
Wall-clock time(s)

100
FIM-3, Ka = 0.01, M = 6, 72 = 1
FIM-3, Ka = 0.01, M = 6, 72 = 50
FIM-3, Ka = 0.01, M = 6, 72 = 100
10-2
FIM-3, Ka = 0.01, M = 6, 72 = 200
FIM-3, Ka = 0.01, M = 6, 72 = 300
FIM-3, Ka = 0.01, M = 6, 72 = 400
FIM-3, Ka = 0.01, M = 6, 72 = 800
10-4
FIM-3, Ka = 0.01, M = 6, 72 = 800
10-6
10-8
0
10
20
30
40
50
60
70
80
Wall-clock time(s)


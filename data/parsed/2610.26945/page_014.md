<tbc>on the B60 the INT8 GEMM accounts for 75-80% of the time at _N_=8192 and 88-90% at _N_=24576, running at 186TOP/s, while the split and CRT kernels run at the memory bandwidth. The performance model of Section 9.2 reproduces the measured times to within 10% on average.

## 8.5 ZGEMM performance and accuracy

12 compares the 3M emulation with native oneMKL ZGEMM (0.76TFLOP/s, counting 8_mnk_ flops). Since the emulation spends 3_s_ INT8 GEMMs on four times the flops of a real product, the emulated complex rate is \(\frac{4}{3}\) of the real one: 24.4, 16.8 and 12.8TFLOP/s at _N_=8192 for _s_=8, 12 and 16, and up to 27.4TFLOP/s at _N_=16384 (_s_=8). At _s_=16 this is 13.7-17.8 times native ZGEMM for \(N\ge 4096\), and the board energy efficiency is 70 versus 9.4GFLOP/s/W. The accuracy behaves as for DGEMM ( 13): the results are correctly rounded from _s_=16 on for U\[-1,1\] and from _s_=24 for \(\phi=2\) (99.9% at _s_=20). In the cancellation case the normwise error drops from \(3\times 10^{-6}\) for native ZGEMM to \(9\times 10^{-16}\) at _s_=20. As expected, the exact 3M form loses no accuracy relative to the real case.

\begin{tabular}{cccccccccc}
_N_ & _s_ & scale & split & GEMM & TOP/s & CRT & GEMM % & tiles \\
2048 & 8 & 0.25 & 0.41 & 0.90 & 153 & 0.47 & 44 & 1x1 \\
2048 & 12 & 0.25 & 0.51 & 1.34 & 153 & 0.63 & 49 & 1x1 \\
2048 & 16 & 0.25 & 0.60 & 1.76 & 156 & 0.78 & 52 & 1x1 \\
2048 & 20 & 0.25 & 0.89 & 2.20 & 156 & 0.90 & 52 & 1x1 \\
2048 & 24 & 0.27 & 1.02 & 2.66 & 155 & 1.05 & 53 & 1x1 \\
8192 & 8 & 2.64 & 6.29 & 47.31 & 186 & 7.21 & 75 & 1x1 \\
8192 & 12 & 2.64 & 7.86 & 70.97 & 186 & 9.52 & 78 & 1x1 \\
8192 & 16 & 2.68 & 9.40 & 94.63 & 186 & 11.92 & 80 & 1x1 \\
8192 & 20 & 2.66 & 13.71 & 118.09 & 186 & 13.77 & 80 & 1x1 \\
8192 & 24 & 2.70 & 15.83 & 141.78 & 186 & 16.23 & 80 & 1x1 \\
24576 & 8 & 22.75 & 86.64 & 1332.98 & 178 & 65.33 & 88 & 3x2 \\
24576 & 12 & 22.73 & 108.26 & 1954.12 & 182 & 87.03 & 90 & 6x2 \\
24576 & 16 & 22.82 & 215.98 & 2836.96 & 167 & 108.34 & 89 & 3x4 \\
24576 & 20 & 22.82 & 248.67 & 3229.24 & 184 & 125.77 & 89 & 6x3 \\
\end{tabular}

175
scaling split
150
INT8 GEMM
CRT
125
100
time (ms)
75
50
25
0
4
6
8
10
12
14
16
18
20
22
24
S

11: Phase breakdown (ms).

Figure 4: Phase breakdown versus _s_ at _N_=8192.


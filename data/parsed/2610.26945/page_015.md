## 8.6 Energy

During the emulation the board draws 120-193W, compared with 80W during native DGEMM, but the run time is an order of magnitude shorter. At _N_=8192 the emulation delivers 96 (_s_=8) and 50 (_s_=16) GFLOP/s per watt, against 9.5 for native DGEMM; for \(N\ge 4096\) it thus needs 4.4-12 times less energy per product ( 14). Per operation, an INT8 multiply-add pair costs 1.0pJ on this device and an FP64 pair 100pJ ( 1).

## 8.7 Comparison with Ozaki scheme I on the same INT8 engine

To quantify the benefit of scheme II on this hardware, we implemented the INT8 Ozaki scheme I \[14, 15\] with the same scaling, the same INT8 GEMM and 7-bit balanced slices (_L_ slices, _L(L_+1)/2 products, diagonal sums accumulated in double-double). At comparable accuracy, scheme I needs 36-45 INT8 GEMMs where scheme II needs 15-16, and it is 2.3-2.9 times slower ( 15, Figure 5). Because of its truncation it is also less accurate than scheme II at an equal number of GEMMs. We found no regime in which scheme I is preferable on the B60 and therefore include it only as a point of comparison.

\begin{tabular}{ccccccc}
_N_ & _s_=8 & _s_=12 & _s_=16 & _s_=20 & ZGEMM GPU & speed-up (_s_=16) \\
1024 & 6.72 & 5.21 & 4.19 & 3.49 & 0.75 & 5.6 \\
2048 & 13.06 & 9.54 & 7.45 & 6.06 & 0.75 & 9.9 \\
4096 & 19.28 & 13.47 & 10.33 & 8.42 & 0.75 & 13.7 \\
6144 & 21.81 & 15.13 & 11.56 & 9.33 & 0.76 & 15.2 \\
8192 & 24.41 & 16.75 & 12.76 & 10.26 & 0.76 & 16.7 \\
12288 & 22.96 & 15.47 & 11.52 & - & 0.76 & 15.1 \\
16384 & 27.36 & 18.00 & 13.60 & - & 0.76 & 17.8 \\
\end{tabular}

\begin{tabular}{ccccccc}
Data & Method & _t_ & max ulp & CR % & max \(\frac{|e|}{|A||B|}\) & \(\frac{\|e\|_F}{\|C\|_F}\) \\
U\[-1,1) & ZGEMM GPU & 53 & \(5.2\cdot 10^6\) & 1.87 & \(2.4\cdot 10^{-16}\) & \(3.0\cdot 10^{-15}\) \\
U\[-1,1) & ZGEMM CPU & 53 & \(6.5\cdot 10^5\) & 10.01 & \(2.3\cdot 10^{-17}\) & \(4.9\cdot 10^{-16}\) \\
U\[-1,1) & Oz-II 3M _s_=12 & 39 & \(1.8\cdot 10^9\) & 0.00 & \(4.6\cdot 10^{-14}\) & \(1.3\cdot 10^{-12}\) \\
U\[-1,1) & Oz-II 3M _s_=14 & 47 & \(3.7\cdot 10^6\) & 0.99 & \(1.7\cdot 10^{-16}\) & \(5.0\cdot 10^{-15}\) \\
U\[-1,1) & Oz-II 3M _s_=16 & 55 & 0.50 & 100.00 & \(3.1\cdot 10^{-18}\) & \(4.7\cdot 10^{-17}\) \\
U\[-1,1) & Oz-II 3M _s_=20 & 70 & 0.50 & 100.00 & \(3.1\cdot 10^{-18}\) & \(4.7\cdot 10^{-17}\) \\
U\[-1,1) & Oz-II 3M _s_=24 & 85 & 0.50 & 100.00 & \(3.1\cdot 10^{-18}\) & \(4.7\cdot 10^{-17}\) \\
\(\phi\)=2 & ZGEMM GPU & 53 & \(2.5\cdot 10^6\) & 2.05 & \(9.4\cdot 10^{-15}\) & \(2.9\cdot 10^{-15}\) \\
\(\phi\)=2 & ZGEMM CPU & 53 & \(8.0\cdot 10^5\) & 11.45 & \(1.7\cdot 10^{-15}\) & \(4.8\cdot 10^{-16}\) \\
\(\phi\)=2 & Oz-II 3M _s_=12 & 39 & \(3.1\cdot 10^{11}\) & 0.00 & \(1.3\cdot 10^{-9}\) & \(8.4\cdot 10^{-11}\) \\
\(\phi\)=2 & Oz-II 3M _s_=14 & 47 & \(1.4\cdot 10^9\) & 0.02 & \(4.3\cdot 10^{-12}\) & \(3.3\cdot 10^{-13}\) \\
\(\phi\)=2 & Oz-II 3M _s_=16 & 55 & \(3.3\cdot 10^6\) & 3.76 & \(1.2\cdot 10^{-14}\) & \(1.3\cdot 10^{-15}\) \\
\(\phi\)=2 & Oz-II 3M _s_=20 & 70 & 32.98 & 99.91 & \(9.1\cdot 10^{-17}\) & \(4.6\cdot 10^{-17}\) \\
\(\phi\)=2 & Oz-II 3M _s_=24 & 85 & 0.50 & 100.00 & \(9.1\cdot 10^{-17}\) & \(4.6\cdot 10^{-17}\) \\
cancel & ZGEMM GPU & 53 & \(1.6\cdot 10^{17}\) & 0.00 & \(1.9\cdot 10^{-16}\) & \(3.2\cdot 10^{-6}\) \\
cancel & ZGEMM CPU & 53 & \(1.9\cdot 10^{16}\) & 0.00 & \(1.8\cdot 10^{-17}\) & \(7.3\cdot 10^{-7}\) \\
cancel & Oz-II 3M _s_=12 & 39 & \(1.1\cdot 10^{19}\) & 0.00 & \(3.2\cdot 10^{-14}\) & \(1.4\cdot 10^{-3}\) \\
cancel & Oz-II 3M _s_=14 & 47 & \(1.1\cdot 10^{17}\) & 0.00 & \(1.3\cdot 10^{-16}\) & \(5.4\cdot 10^{-6}\) \\
cancel & Oz-II 3M _s_=16 & 55 & \(7.7\cdot 10^{13}\) & 0.00 & \(1.5\cdot 10^{-19}\) & \(6.0\cdot 10^{-9}\) \\
cancel & Oz-II 3M _s_=20 & 70 & \(2.2\cdot 10^5\) & 99.22 & \(1.0\cdot 10^{-25}\) & \(8.6\cdot 10^{-16}\) \\
cancel & Oz-II 3M _s_=24 & 85 & 14.45 & 100.00 & \(1.7\cdot 10^{-27}\) & \(4.7\cdot 10^{-17}\) \\
\end{tabular}

12: Emulated ZGEMM (3M) versus native ZGEMM; rates in TFLOP/s (8_mnk_).

13: ZGEMM accuracy (\(512\times 512\), _k_=4096).


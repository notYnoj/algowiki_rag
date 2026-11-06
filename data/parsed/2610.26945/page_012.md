## 8.4 DGEMM performance

9 and Figure 3 report the emulated rate for square problems. For \(N\ge 2048\) the emulation outperforms native DGEMM for every _s_. At _N_=8192 it reaches 17.3, 12.1 and 9.3 TFLOP/s for _s_=8, 12 and 16, which is 22.8, 15.9 and 12.2 times the native DGEMM rate (0.76 TFLOP/s). Problems up to _N_=24576 are tiled automatically (24576<sup>3</sup> requires ≈9GB of workspace in addition to the 14.5GB occupied by _A_, _B_ and _C_) at an efficiency loss of 0-10%. For \(N\le 256\), kernel-launch overheads (≈0.15ms) dominate, and native DGEMM is faster. Non-square shapes ( 10) behave as the operation count predicts: a small inner dimension (_k_=256) leaves the memory-bound phases exposed (2.4 TFLOP/s at _s_=8), whereas a large one approaches the GEMM bound (19.6 TFLOP/s for _k_=32768). Transposed operands cost at most 7%.

### Phase breakdown.

11 and Figure 4 split the run time into scaling, splitting, INT8 GEMM and CRT. Unlike on the CPUs studied in \[20\], where the residue conversion dominates,<tbc>

\begin{tabular}{cccccc}
Data & _k_ & (a) ≈DGEMM & (b) 99.9% CR & (c) 100% CR & DGEMM GPU CR % \\
U\[-1,1) & 256 & 14 & 15 & 15 & 10.6 \\
U\[-1,1) & 4096 & 14 & 16 & 16 & 2.6 \\
U\[-1,1) & 65536 & 14 & 16 & 16 & 0.6 \\
\(\phi\)=0.5 & 256 & 15 & 18 & 19 & 10.5 \\
\(\phi\)=0.5 & 4096 & 15 & 19 & 20 & 2.6 \\
\(\phi\)=0.5 & 65536 & 15 & 19 & 22 & 0.7 \\
\(\phi\)=1 & 256 & 15 & 18 & 20 & 11.0 \\
\(\phi\)=1 & 4096 & 15 & 19 & 21 & 2.7 \\
\(\phi\)=1 & 65536 & 16 & 20 & 22 & 0.7 \\
\(\phi\)=2 & 256 & 17 & 19 & 21 & 12.2 \\
\(\phi\)=2 & 4096 & 17 & 20 & 22 & 2.9 \\
\(\phi\)=2 & 65536 & 17 & 21 & 23 & 0.7 \\
\(\phi\)=4 & 256 & 21 & 22 & 24 & 13.7 \\
\(\phi\)=4 & 4096 & 21 & 23 & - & 3.3 \\
\(\phi\)=4 & 65536 & 21 & 24 & - & 0.8 \\
sincos & 256 & 14 & 18 & 19 & 7.7 \\
sincos & 4096 & 14 & 19 & 20 & 1.7 \\
sincos & 65536 & 13 & 20 & 21 & 0.4 \\
\end{tabular}

\begin{tabular}{ccccccc}
Data & Method & _t_ & max ulp & CR % & max \(\frac{|e|}{|A||B|}\) & \(\frac{\|e\|_F}{\|C\|_F}\) \\
spike & DGEMM GPU & 53 & 86.57 & 3.57 & \(1.8\cdot 10^{-14}\) & \(2.2\cdot 10^{-15}\) \\
spike & DGEMM CPU & 53 & 16.76 & 15.54 & \(3.1\cdot 10^{-15}\) & \(5.0\cdot 10^{-16}\) \\
spike & Oz-II _s_=12 & 40 & \(2.2\cdot 10^{10}\) & 0.00 & \(3.9\cdot 10^{-6}\) & \(2.2\cdot 10^{-11}\) \\
spike & Oz-II _s_=16 & 55 & \(6.7\cdot 10^5\) & 8.05 & \(1.3\cdot 10^{-10}\) & \(6.8\cdot 10^{-16}\) \\
spike & Oz-II _s_=20 & 70 & 7.46 & 99.93 & \(9.1\cdot 10^{-16}\) & \(4.7\cdot 10^{-17}\) \\
spike & Oz-II _s_=24 & 85 & 0.50 & 100.00 & \(1.1\cdot 10^{-16}\) & \(4.7\cdot 10^{-17}\) \\
spike & Oz-I 36 GEMMs & 54 & \(5.8\cdot 10^6\) & 1.30 & \(1.0\cdot 10^{-9}\) & \(4.1\cdot 10^{-15}\) \\
spike & Oz-I 45 GEMMs & 61 & 59480.00 & 66.32 & \(1.1\cdot 10^{-11}\) & \(6.0\cdot 10^{-17}\) \\
cancel & DGEMM GPU & 53 & \(5.6\cdot 10^{15}\) & 0.00 & \(3.2\cdot 10^{-16}\) & \(2.3\cdot 10^{-6}\) \\
cancel & DGEMM CPU & 53 & \(8.5\cdot 10^{14}\) & 0.00 & \(5.2\cdot 10^{-17}\) & \(7.2\cdot 10^{-7}\) \\
cancel & Oz-II _s_=12 & 40 & \(7.2\cdot 10^{17}\) & 0.00 & \(4.1\cdot 10^{-14}\) & \(6.9\cdot 10^{-4}\) \\
cancel & Oz-II _s_=16 & 55 & \(2.1\cdot 10^{13}\) & 0.00 & \(3.6\cdot 10^{-19}\) & \(6.0\cdot 10^{-9}\) \\
cancel & Oz-II _s_=20 & 70 & \(9.8\cdot 10^5\) & 99.42 & \(4.2\cdot 10^{-25}\) & \(9.4\cdot 10^{-16}\) \\
cancel & Oz-II _s_=24 & 85 & 0.50 & 100.00 & \(5.5\cdot 10^{-27}\) & \(4.7\cdot 10^{-17}\) \\
cancel & Oz-I 36 GEMMs & 54 & \(3.2\cdot 10^{14}\) & 0.00 & \(1.2\cdot 10^{-17}\) & \(1.5\cdot 10^{-7}\) \\
cancel & Oz-I 45 GEMMs & 61 & \(1.1\cdot 10^{12}\) & 0.00 & \(8.2\cdot 10^{-20}\) & \(1.2\cdot 10^{-9}\) \\
\end{tabular}

7: Smallest _s_ that reaches (a) the componentwise accuracy of native GPU DGEMM, (b) 99.9% and (c) 100% correctly rounded entries.

8: Worst-case inputs (\(512\times 512\), _k_=4096).


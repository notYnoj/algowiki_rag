<tbc>_R_<sub>8</sub> faster than \(\beta_\mathrm{mem}\) therefore shift the balance towards the memory-bound phases, which our split and CRT kernels already run at full bandwidth. For the D270 (Crescent Island), only the FP8 rate (1.3PFLOP/s) and a memory bandwidth of ≈1.5TB/s have been reported \[34\]. A quantitative projection requires the INT8 GEMM rate, which has not yet been published; we therefore defer it.

Our design does not depend on INT8 specifically. Should future Intel GPUs favour FP8 over INT8 in their matrix engines, as NVIDIA’s Blackwell Ultra already does \[9\], the FP8 variant of Ozaki scheme II \[18\] can be mapped onto the same device-resident pipeline, with only the moduli and the residue format changed.

### 9.3 Limitations

• Exponents are shared per row and column, so elements more than _t_-53 binades below the row maximum lose bits (Section 8.3); a larger _s_ mitigates this.<tbc>

• The number of moduli is limited to \(s\le 24\) (log<sub>2</sub>_M\<_192); _k\>_131071 is handled by splitting _k_.<tbc>

• An Inf or NaN in a row of op(_A_) or a column of op(_B_) produces NaN in the entire corresponding row or column of _C_, and subnormal results may be double-rounded.<tbc>

• The workspace grows as _s(mk+kn_+4_mn_) bytes (\(\times 3\) for ZGEMM). Large problems are tiled, at the cost of re-splitting parts of _A_.<tbc>

• Small problems (\(N\lesssim 256\)) are dominated by launch overhead.

## 10 Conclusions

Ozaki scheme II turns the INT8 matrix engines of an affordable Intel Arc Pro B60 into a DGEMM/ZGEMM engine that is an order of magnitude faster and about five times more energy- efficient than the native FP64 path. With enough moduli it is also more accurate: it rounds<tbc>

\begin{tabular}{ccccc}
_N_ & _s_ & measured (ms) & model (ms) & deviation \\
1024 & 8 & 0.58 & 0.46 & -21% \\
1024 & 16 & 0.87 & 0.68 & -22% \\
1024 & 24 & 1.21 & 0.90 & -26% \\
2048 & 8 & 2.03 & 1.81 & -11% \\
2048 & 16 & 3.38 & 3.05 & -10% \\
2048 & 24 & 4.98 & 4.30 & -14% \\
3072 & 8 & 5.21 & 4.73 & -9% \\
3072 & 16 & 9.21 & 8.37 & -9% \\
3072 & 24 & 13.58 & 12.01 & -12% \\
4096 & 8 & 10.39 & 9.78 & -6% \\
4096 & 16 & 18.89 & 17.73 & -6% \\
4096 & 24 & 27.82 & 25.69 & -8% \\
6144 & 8 & 30.23 & 28.50 & -6% \\
6144 & 16 & 55.72 & 53.07 & -5% \\
6144 & 24 & 82.74 & 77.64 & -6% \\
8192 & 8 & 63.54 & 62.42 & -2% \\
8192 & 16 & 118.73 & 117.95 & -1% \\
8192 & 24 & 176.58 & 173.48 & -2% \\
12288 & 8 & 222.23 & 193.62 & -13% \\
12288 & 16 & 432.89 & 371.91 & -14% \\
16384 & 8 & 432.86 & 438.95 & +1% \\
\end{tabular}

17: Performance model versus measurement (single tile).


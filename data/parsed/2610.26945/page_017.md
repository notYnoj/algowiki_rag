### 8.8 Effect of the pipeline-level decisions

16 disables the pipeline-level decisions of Section 6 one at a time. Issuing the _s_ INT8 products as one batched call saves 6-9% at _N_=2048 and _N_=24576. The preference for power-of-two tiles matters when tiling is active: at _N_=24576 and _s_=16, tiles with a nonpower-of-two row count cost 6%. The padding of the leading dimension changes these timings by at most 1%, because the tilings chosen here rarely produce the critical leading dimensions; its effect on the INT8 GEMM itself is shown in  4. At _N_=8192, where the problem fits into a single tile with favourable dimensions, none of the decisions changes the run time.

## 9 Discussion

### 9.1 Using the library as a BLAS replacement

The interface mirrors `dgemm` and `zgemm` of the oneMKL SYCL API with a single extra argument, the number of moduli. We recommend the following policy. By default we take _s_=`moduli\_for\_bits`(_k,_53), i.e. _s_=15-16 for \(k\le 2^{16}\); this is as accurate as DGEMM for well-scaled data and correctly rounded for U\[-1,1). Inputs with wide exponent ranges, or computations in which cancellation is expected, call for _s_=20-24, while _s_=8-12 suffices where an accuracy between FP32 and FP64 is acceptable. Because all accumulation is performed in exact integer arithmetic, the results are deterministic and independent of the tiling. Existing applications currently have to call the library explicitly; a layer that transparently redirects their oneMKL calls is left for future work.

### 9.2 Performance model and outlook to Xe3/Xe3P

The measured run time is well described by

\(T\approx\frac{2mnksg}{R_8}+\frac{g\big[(16+s)(mk+kn)+(4s+8)mn\big]}{\beta_\text{mem}}+n_\text{launch}\tau,\) (9)

where _g_=1 for DGEMM and _g_=3 for ZGEMM, _R_<sub>8</sub> is the INT8 GEMM rate, \(\beta_\text{mem}\) the memory bandwidth and \(\tau\approx 15\mu\)s the launch overhead. The three terms correspond to the three kinds of work in the pipeline. The first is the time of the _s_ INT8 products of 2_mnk_ operations each. The second is the memory traffic of the remaining kernels, in bytes: the scaling and split kernels read every element of _A_ and _B_ twice as FP64 (16 bytes) and write _s_ residue bytes, and the CRT kernel reads _s_ INT32 products (4_s_ bytes) and writes one FP64 result (8 bytes) per entry of _C_. The third counts the kernel launches. With the B60 values of  1, the model matches the measurements to within 10% on average and to within 1-8% for \(4096\le N\le 8192\) ( 17). It underestimates the time for small problems, where the INT8 GEMM runs below its asymptotic rate, and for _N_=12288, where oneMKL is slower for this shape. The fraction of time spent in INT8 GEMM is approximately \(\big(1+R_8[2(16+s)+(4s+8)]/(2sN\beta_\text{mem})\big)^{-1}\). Devices that raise<tbc>

\begin{tabular}{ccccccc}
 & & \multicolumn{2}{c}{full pipeline} & \multicolumn{3}{c}{slowdown without} \\
_N_ & _s_ & \multicolumn{2}{c}{(ms)} & batched GEMM & lda padding & 2_<sup>j</sup>_ tiles \\
2048 & 8 & \multicolumn{2}{c}{2.0} & +6% & 0 & 0 \\
2048 & 16 & \multicolumn{2}{c}{3.4} & +9% & 0 & 0 \\
8192 & 8 & \multicolumn{2}{c}{63.6} & 0 & 0 & 0 \\
8192 & 16 & \multicolumn{2}{c}{118.7} & 0 & 0 & 0 \\
24576 & 8 & \multicolumn{2}{c}{1492.3} & +9% & +1% & 0 \\
24576 & 16 & \multicolumn{2}{c}{3200.3} & +7% & 0 & +6% \\
\end{tabular}

16: Ablation of the pipeline-level decisions: run time of the full pipeline and slowdown when one decision is disabled.


Emulating DGEMM and ZGEMM with INT8 Matrix Engines on Intel Arc GPUs: Ozaki Scheme II on the Xe2 Architecture

**Abstract**

Double-precision matrix multiplication, real (DGEMM) and complex (ZGEMM), dominates the run time of dense linear algebra and electronic-structure codes. On affordable GPUs, however, FP64 throughput is a small and shrinking fraction of the throughput of the low-precision matrix engines. Ozaki scheme II closes this gap by reducing a floating-point matrix product to a handful of exact INT8 products followed by a Chinese-remainder reconstruction; the number of products sets the accuracy. We present what is, to our knowledge, the first implementation of Ozaki scheme II for Intel GPUs. Written in SYCL on top of oneMKL, it runs entirely on the device and exposes the full BLAS `dgemm/zgemm` interface, including transposition, conjugation, \(\alpha\), \(\beta\) and arbitrary problem sizes through memory- aware tiling. Making the scheme fast on the Xe2 (Battlemage) architecture required keeping FP64 arithmetic out of all memory-bound kernels, a branch-free residue computation, an FP32 evaluation of the CRT quotient with a proven safety margin, 16-bit limb arithmetic in the reconstruction, and work-arounds for performance cliffs of the vendor INT8 GEMM. On an Intel Arc Pro B60 (24GB) the emulated DGEMM reaches 17.3, 12.1 and 9.3 TFLOP/s with _s_=8, 12 and 16 moduli at _N_=8192, and up to 21.1 TFLOP/s overall, i.e. 12-28\(\times\) the native FP64 DGEMM of the same board; 75-90% of the run time is spent in INT8 GEMM at ≈95% of its attainable rate. The emulated ZGEMM, which uses the 3M form exactly in integer arithmetic, reaches up to 27.4 TFLOP/s and is 13.7-17.8\(\times\) faster than native ZGEMM for \(N\ge 4096\) at _s_=16. With \(s\ge 16\) the results are correctly rounded for well-scaled inputs and, using an extended-width residue path (_s_=20-24), also for inputs with wide exponent ranges, whereas native DGEMM on GPU or CPU rounds only 2-13% of the entries correctly. We further report worst-case accuracy, phase breakdowns, energy, an ablation of the pipeline-level decisions, a comparison with Ozaki scheme I on the same hardware, and a validated performance model for projecting the method to Intel’s announced Xe3P-based products.

## 1 Introduction

High-precision matrix multiplication. The general matrix product \(C ←\alpha\mathrm{op}(A)\mathrm{op}(B)+\beta C\) (GEMM, a level-3 BLAS routine [1]) is the kernel onto which dense linear algebra is mapped: blocked LU, Cholesky and QR factorizations, eigenvalue and singular-value solvers, and the High-Performance LINPACK benchmark all perform the overwhelming majority of their floating- point operations in GEMM [2]. Computational chemistry and materials science are a prominent example: self-consistent-field methods such as Hartree–Fock and Kohn–Sham density functional

<sup>∗</sup>Corresponding author: `rostislavs.rostovskis@cfi.lu.lv`

Rostislavs Rostovskis<sup>∗</sup><sup>1</sup> and Aleksandrs Platonenko<sup>1</sup>

<sup>1</sup>Institute of Solid State Physics, University of Latvia, Riga, Latvia

October 21, 2026

arXiv:2610.26945v1 [cs.MS] 18 Oct 2026


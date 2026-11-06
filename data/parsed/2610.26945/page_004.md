### 2.4 Related implementations

GEMMul8 \[27\] implements Ozaki scheme II for NVIDIA and AMD GPUs, and ozIMMU \[28\] implements the INT8 variant of Ozaki scheme I. Kouya \[20\] implements Ozaki scheme II for multiple precision on Intel AMX and Arm SVE2. Uchino et al. \[19\] extend Ozaki scheme II to CGEMM and ZGEMM with a Karatsuba (3M) formulation, also released in GEMMul8, and report speed-ups on NVIDIA and AMD GPUs. Among vendor libraries, cuBLAS has offered opt-in fixed-point emulation of FP64 matrix products (DGEMM and ZGEMM) on INT8 Tensor Cores since CUDA 13.0 Update 2 \[10, 11\], whereas the oneMKL 2026 release notes list no comparable feature \[29\]. We are not aware of any implementation for Intel GPUs.

## 3 Target platform: Intel Arc Pro B60 (Xe2)

The B60 has 20 Xe2 cores with 160 XMX matrix engines and 24 GB of GDDR6 on a 192-bit bus with a nominal bandwidth of 456 GB/s. Intel specifies 197TOP/s of dense INT8, 12.28 TFLOP/s of FP32 and a total board power of 120-200W, depending on the partner design \[21\]; the maximum GPU clock of our board is 2.4GHz.  1 lists the measured throughput of the operations relevant here. Three properties of the device shape the implementation:

(i) INT8 GEMM in oneMKL reaches 184-186TOP/s, about 250 times the native DGEMM rate of 0.76 TFLOP/s.<tbc>

(ii) FP64 vector arithmetic runs at 1/16 of the FP32 rate, and the conversion from FP64 to INT64 is not native. Kernels that are meant to run at memory speed must therefore avoid FP64 altogether.<tbc>

(iii) The memory bandwidth is ≈400GB/s for incompressible data, but the hardware compresses regular data (constant buffers are read at 1.1TB/s). All memory-bound measurements therefore use random data.

These numbers also settle the choice of backend. Following the per-bit argument of \[20, §3.3\], one INT8 product contributes ≈7.85 bits to log<sub>2</sub>_M_ at 186TOP/s, whereas one DGEMM in an FP64-based Ozaki-II backend contributes ≈21.5 bits (_k_=4096) at 0.76 TFLOP/s. Per bit of accuracy, the INT8 path is thus ≈90 times cheaper on this device, and we do not consider an FP64 backend.

\begin{tabular}{cccc}
Operation & Size & Rate & pJ/op \\
Memory copy (random data) & 4GiB & 397.20 GB/s & - \\
Memory copy (constant data) & 4GiB & 1088.00 GB/s & - \\
DGEMM, oneMKL, GPU & 4096 & 0.75 TFLOP/s & 98.0 \\
SGEMM, oneMKL, GPU & 4096 & 12.00 TFLOP/s & 10.1 \\
INT8 GEMM, oneMKL, GPU & 4096 & 170.90 TOP/s & 1.0 \\
DGEMM, oneMKL, GPU & 8192 & 0.76 TFLOP/s & 99.7 \\
SGEMM, oneMKL, GPU & 8192 & 11.89 TFLOP/s & 9.2 \\
INT8 GEMM, oneMKL, GPU & 8192 & 184.30 TOP/s & 1.0 \\
INT8 GEMM, batch of 16, GPU & 8192 & 185.50 TOP/s & 1.0 \\
\end{tabular}

1: Measured throughput on the test system (oneMKL 2026.1, random data). Energy per operation is taken from the board energy counter.


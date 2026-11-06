**Algorithm 4** Emulated ZGEMM, 3M form

1: \(t\leftarrow\) Eq. (4) with 2_k_; _D<sub>i</sub>,E<sub>j</sub>_ from max(|Re|,|Im|)

2: \((A_r^{(t)},A_i^{(t)},A_\Sigma^{(t)})\leftarrow\text{SplitC}(A,D)\); same for \(B\triangleright A_\Sigma^{(t)}=\text{sym}(A_r^{(t)}+A_i^{(t)})\)

3: \(P_0^{(t)}\leftarrow A_r^{(t)}B_r^{(t)}\), \(P_1^{(t)}\leftarrow A_i^{(t)}B_i^{(t)}\), \(P_2^{(t)}\leftarrow A_\Sigma^{(t)}B_\Sigma^{(t)}\triangleright 3\) batched calls

4: \(\text{Re}\leftarrow\text{CRT}((P_0-P_1)\text{mod}m_t)\), \(\text{Im}\leftarrow\text{CRT}((P_2-P_0-P_1)\text{mod}m_t)\)

5: \(C\leftarrow\alpha(\text{Re}+i\text{Im})2^{-D_i-E_j}+\beta C\)

## 6 Implementation decisions specific to Intel Arc (Xe2)

### Kernel code generation.

The split and CRT kernels are templates over _s_. All loops over moduli are unrolled, and the modulus tables (at most 1KB) are passed as kernel arguments instead of being read from memory. Both kernels use sub-groups of 32 work-items; the complex split uses 16 because of register pressure. With integer-only residue generation, 16-bit limbs and a \[0,2_m_) representative, both kernels are memory-bound: at _N_=8192 the split kernel streams 270-340GB/s and the CRT kernel 373-416GB/s, i.e. close to the measured memory bandwidth ( 3).

### Using the vendor INT8 GEMM.

The INT8 products are computed by the batched GEMM of oneMKL (`gemm\_batch`), which reaches 184-193TOP/s on the B60. A hand-written `joint\_matrix` kernel is possible, but offers no advantage: the INT8 GEMM is currently a core operation of the vendor’s inference stack and is tuned by the vendor for each generation of XMX engines. Relying on it lets the emulation inherit these improvements without changes to our code, and confines our own kernels to the memory-bound split and CRT phases. We do, however, adapt the calling pattern to three behaviours of the routine that we measured: (i) with `transb=trans` its throughput drops from 175 to 33TOP/s, so we first transpose a transposed op(_B_) through shared local memory into a temporary tile and always store the residue planes of _B_ in `N` layout; (ii) a leading dimension of the _A_ planes that is a multiple of \(12288=3\cdot 4096\) reduces the throughput to 120-145TOP/s, which a padding of 64 bytes eliminates ( 4); (iii) tiles whose row count is not a power of two run 5-17% slower, so the tiler prefers _m<sub>b</sub>_=2_<sup>j</sup>_ (Figure 1).

### Memory-aware tiling.

A tile of size \(m_b\times n_b\) requires a workspace of _s(m<sub>b</sub>k+kn<sub>b</sub>_+4_m<sub>b</sub>n<sub>b</sub>_) bytes (\(\times 3\) for ZGEMM). When this exceeds the memory budget, _C_ is tiled. Candidate tile sizes are scored with a simple cost model, consisting of the GEMM time with a shape-efficiency factor plus the split and CRT traffic, and the cheapest feasible tiling is selected. The budget is derived from the driver’s free-memory query. We observed, however, that the Linux `xe` driver<tbc>

\begin{tabular}{cccc}
kernel & _s_ & ms & GB/s \\
split & 8 & 3.18 & 337 \\
split & 16 & 4.73 & 340 \\
split & 24 & 7.94 & 270 \\
CRT & 8 & 7.20 & 373 \\
CRT & 16 & 11.90 & 406 \\
CRT & 24 & 16.78 & 416 \\
\end{tabular}

\begin{tabular}{ccccc}
_m_ & _n_ & lda=_m_ & lda & padded \\
4096 & 4096 & 183 & 4160 & 182 \\
4096 & 16384 & 185 & 4160 & 185 \\
8192 & 4096 & 184 & 8256 & 184 \\
8192 & 16384 & 185 & 8256 & 185 \\
12288 & 4096 & 129 & 12352 & 175 \\
12288 & 16384 & 122 & 12352 & 181 \\
16384 & 4096 & 184 & 16448 & 185 \\
16384 & 16384 & 185 & 16448 & 186 \\
\end{tabular}

3: Split and CRT kernels (_N_=8192): time (ms) and effective bandwidth (GB/s).

4: oneMKL INT8 GEMM throughput (TOP/s), _k_=8192, with the natural leading dimension (lda=_m_) and with a padded one.


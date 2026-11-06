• A ZGEMM in the exact 3M (Karatsuba) form of \[19\], integrated into the same device- resident pipeline: the split kernel emits the residues of _A<sub>r</sub>+A<sub>i</sub>_ directly, and the CRT kernel combines the three products before reconstruction, so that a complex product costs 3_s_ INT8 GEMMs and inherits the accuracy of the real case (Section 5).<tbc>

• An extended-width residue path (scaling width _t_ up to 100 bits) that delivers correctly rounded DGEMM and ZGEMM for inputs with wide exponent ranges.<tbc>

• A systematic evaluation covering verification (unit tests of the kernels and element-wise checks of the error bound), accuracy against a double-double reference for typical and worst-case inputs, performance with a breakdown into phases, energy efficiency, an ablation study, a comparison with Ozaki scheme I on the same INT8 engine, and a validated performance model (Sections 7-9).

## 2 Background

### 2.1 Notation

We write \(\mathrm{op}(A)\in\mathbb{R}^{m\times k}\) and \(\mathrm{op}(B)\in\mathbb{R}^{k\times n}\), stored in column-major order, and _u_=2<sup>-53</sup>. For an integer _x_ and a modulus _m_, sym_<sub>m</sub>(x_) denotes the representative of _x_mod_m_ in a fixed window of _m_ consecutive integers that contains 0; for \(m\le 256\) it fits in a signed byte. rint denotes rounding to nearest with ties to even.

### 2.2 Ozaki scheme I

Ozaki scheme I \[12\] writes each scaled row of _A_ and column of _B_ as a sum of _L_ low-precision slices, \(A\approx\sum_iA_i\) and \(B\approx\sum_jB_j\), chosen so that a low-precision engine computes every product _A<sub>i</sub>B<sub>j</sub>_ without rounding. The approximation \(AB\approx\sum_{i+j\le L+1}A_iB_j\) then requires _L(L_+1)/2 products. The INT8 variants \[14, 15\] use slices of about 7 bits.

### 2.3 Ozaki scheme II

Ozaki scheme II \[17\] consists of four steps. We follow the formulation of the original paper, with the modifications described in Section 4.

_1. Integration with shared exponents._ Each row _i_ of _A_ and each column _j_ of _B_ is scaled by a power of two such that

\(\hat{a}_{ip}=\mathrm{rint}(a_{ip}2^{D_i}),\hat{b}_{pj}=\mathrm{rint}(b_{pj}2^{E_j}),|\hat{a}_{ip}|,|\hat{b}_{pj}|\le 2^t.\) (1)

Then \(\hat{c}_{ij}=\sum_p\hat{a}_{ip}\hat{b}_{pj}\in\mathbb{Z}\) and \(c_{ij}\approx 2^{-D_i-E_j}\hat{c}_{ij}\). Errors arise only from the rounding in Eq. (1) and from the final rounding of \(\hat{c}_{ij}2^{-D_i-E_j}\).

_2. Residues._ For pairwise coprime moduli \(m_1,\dots,m_s\le 256\) with \(M=\prod_tm_t\), the residue matrices \(A^{(t)}=\mathrm{sym}_{m_t}(\hat{A})\) and \(B^{(t)}=\mathrm{sym}_{m_t}(\hat{B})\) have entries in \[-128,128\] and are stored as INT8.

_3. Exact INT8 products._ Each product _C_<sup>(_t_)</sup>=_A_<sup>(_t_)</sup>_B_<sup>(_t_)</sup> is computed with INT32 accumulation and is exact as long as \(k\cdot 128^2<2^{31}\), i.e. \(k\le 131071\).

_4. CRT reconstruction._ By the Chinese remainder theorem (see, e.g., \[26, §4.3.2\]), with _M<sub>t</sub>=M/m<sub>t</sub>_ and \(y_t=M_t^{-1}\mathrm{mod}m_t\),

\(\hat{c}_{ij}\equiv\sum_{t=1}^sC_{ij}^{(t)}M_ty_t(\mathrm{mod}M),\) (2)

and \(\hat{c}_{ij}\) is the unique representative with \(|\hat{c}_{ij}|<M/2\), provided that \(|\hat{c}_{ij}|<M/2\) is known a priori. The method needs _s_ INT8 products, and each modulus contributes log<sub>2</sub>_m<sub>t</sub>_≈7.9 bits to log<sub>2</sub>_M_.


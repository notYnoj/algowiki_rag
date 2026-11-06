**Algorithm 3** CRT kernel (one work-item per entry (_i,j_))

1: \(\tilde{z}\leftarrow 0\); \(acc_\ell\leftarrow 0\) for \(\ell=0..2N_L-1\)

2: **for** _t_=1_..s_ **do** \(\triangleright\) unrolled

3: \(r\leftarrow\text{Barrett}(C_{ij}^{(t)}+2^{31})+K'_t\triangleright r\in[0,2m_t)\), \(K'_t=(-2^{31})\mathrm{mod}m_t\)

4: \(\tilde{z}\leftarrow\text{fma}_{32}(r,y_t/m_t,\tilde{z})\)

5: \(acc_\ell\leftarrow acc_\ell+r\cdot W_{t,\ell}\) for all \(\ell\triangleright 16\)-bit limbs of _W<sub>t</sub>=M<sub>t</sub>y<sub>t</sub>_

6: **end for**

7: \(q\leftarrow\text{rint}(\tilde{z})\); \(acc_\ell\leftarrow acc_\ell-qM_\ell\); propagate carries \(\triangleright\hat{c}=Z-qM\) exactly

8: \(c\leftarrow\text{RoundToDouble}(\hat{c})\cdot 2^{-D_i-E_j}\triangleright\) normalize, sticky bit, RNE

9: \(C_{ij}\leftarrow\alpha c+\beta C_{ij}\)

Once _q_ is known, \(\hat{c}_{ij}=Z-qM\) is an integer with \(|\hat{c}_{ij}|\le M/4<2^{32N_L-1}\), where \(N_L=\lfloor\mathrm{log}_2M/32\rfloor+1\), and we compute it exactly in two’s complement modulo 2<sup>32_N<sub>L</sub>_</sup>. Neither long division nor correction steps are needed, in contrast with the FP64 quotient estimate and subsequent integer correction of \[17, 20\]. We accumulate _Z_ in 16-bit limbs held in 32-bit registers. Every term satisfies \(r_t\cdot W_{t,\ell}<2^9\cdot 2^{16}\), and 24 such terms stay below 2<sup>30</sup>, so carries need to be propagated only once at the end; moreover, all multiplications are \(16\times 16\)-bit, which Xe2 executes natively, unlike \(32\times 32\rightarrow 64\)-bit products. Finally, the 32_N<sub>L</sub>_-bit integer is normalized, its top 64 bits are OR-ed with a sticky bit of the remaining bits and converted with round-to- nearest-even, and the result is multiplied by the exact power of two 2<sup>-_D<sub>i</sub>-E<sub>j</sub>_</sup>. The output is therefore the correctly rounded value of \(2^{-D_i-E_j}\hat{c}_{ij}\) unless it is subnormal.

### 4.5 Error bound and the precision knob

Combining the rounding in Eq. (1) with the final rounding gives, for every entry,

\(|\tilde{c}_{ij}-c_{ij}|\le\frac{1}{2}2^{-D_i}\sum_p|b_{pj}|+\frac{1}{2}2^{-E_j}\sum_p|a_{ip}|+\frac{1}{4}k2^{-D_i-E_j}+u|\tilde{c}_{ij}|,\) (7)

which our tests verify element by element (Section 8.1). Since 2<sup>-_D<sub>i</sub>_</sup>≈2<sup>-_t_</sup>max_<sub>p</sub>|a<sub>ip</sub>_|, the first three terms are of order 2<sup>-_t_</sup>(|_A_||_B_|)_<sub>ij</sub>_. The number of moduli _s_ thus determines _t_ and, through it, the accuracy. The helper `moduli\_for\_bits`(_k,b_) returns the smallest _s_ for which \(t\ge b\).

## 5 Complex matrix multiplication (ZGEMM)

For _A=A<sub>r</sub>+iA<sub>i</sub>_ and _B=B<sub>r</sub>+iB<sub>i</sub>_ we use one shared exponent per row of op(_A_), taken over both real and imaginary parts, and one per column of op(_B_). The integrated parts then satisfy \(|\mathrm{Re}\hat{C}|,|\mathrm{Im}\hat{C}|\le 2k2^{2t}\), so _t_ is chosen with 2_k_ in place of _k_ in Eq. (4). As in \[19\], we use the 3M (Karatsuba) form

\(P_0=\hat{A}_r\hat{B}_r,P_1=\hat{A}_i\hat{B}_i,P_2=(\hat{A}_r+\hat{A}_i)(\hat{B}_r+\hat{B}_i),\mathrm{Re}\hat{C}=P_0-P_1,\mathrm{Im}\hat{C}=P_2-P_0-P_1,\) (8)

evaluated entirely in residues. The split kernel emits three groups of _s_ planes, \(\mathrm{sym}(\hat{a}_r)\), \(\mathrm{sym}(\hat{a}_i)\) and \(\mathrm{sym}(\mathrm{sym}(\hat{a}_r)+\mathrm{sym}(\hat{a}_i))\), and implements conjugation by negating the imaginary residue. Three strided-batch INT8 GEMMs follow, and the CRT kernel forms (_P_<sub>0</sub>-_P_<sub>1</sub>) mod_m<sub>t</sub>_ and (_P_<sub>2</sub>-_P_<sub>0</sub>-_P_<sub>1</sub>) mod_m<sub>t</sub>_ before two independent reconstructions. Because every product is exact, the 3M form incurs no accuracy penalty here, unlike its floating-point counterpart \[31\], and it saves a quarter of the INT8 GEMMs (3_s_ instead of 4_s_). Algorithm 4 summarizes the procedure.


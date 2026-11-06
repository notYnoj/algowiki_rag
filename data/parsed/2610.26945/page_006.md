**Algorithm 2** Split kernel (one work-item, four rows _r..r_+3 of column _c_)

1: **for** _e_=0..3 **do**

2: \(u\leftarrow\text{ScaledOffsetInt}(X_{r+e,c},D_{r+e})\triangleright\) integer shifts with RNE, \(u=\hat{x}+2^{62}\)

3: \((u_0,u_1,u_2)\leftarrow 2\)1-bit limbs of _u_

4: **end for**

5: **for** _t_=1.._s_ **do** \(\triangleright\) unrolled; _s_ is a template parameter

6: **for** _e_=0..3 **do**

7: \(v\leftarrow u_0+u_1c_{t,1}+u_2c_{t,2}+K_t\triangleright c_{t,\ell}=2^{21\ell}\text{mod}m_t\)

8: \(q\leftarrow\text{\texttt{mul\_hi}}(v,\mu_t)\); \(\rho\leftarrow v-qm_t\); \(\rho\leftarrow\text{min}(\rho,\rho-m_t)\triangleright\) unsigned

9: \(byte_e\leftarrow(\rho-h_t)\&\text{\texttt{OxFF}}\)

10: **end for**

11: store (_byte_<sub>0</sub>.._byte_<sub>3</sub>) as one 32-bit word into plane _t_

12: **end for**

<tbc>\(e_a-1075+D\ge 0\), and otherwise a right shift with round-to-nearest-even. To avoid branching on the sign, we work with the non-negative offset value \(u=\hat{a}+2^{62}\) (or \(\hat{a}+2^{104}\) when _t\>_62), split into 21-bit limbs \(u=\sum_\ell u_\ell^{21\ell}\). For each modulus we form

\(v=\sum_\ell u_\ell\left(2^{21\ell}\text{mod}m\right)+K_m<2^{32},K_m=(h_m-2^{62})\text{mod}m,h_m=\lfloor(m-1)/2\rfloor,\) (5)

so that \((v\text{mod}m)-h_m\equiv\hat{a}\) (mod _m_) lies in the window \([-h_m,m-1-h_m]\subset[-127,128]\). The value 128, which occurs only for _m_=256, wraps to -128 in INT8; this is congruent and preserves the product bound 128<sup>2</sup>. The reduction _v_ mod _m_ uses Barrett’s method \[30\] with a single `mul\_hi` and one conditional subtraction (\(\mu_m=\lfloor 2^{32}/m\rfloor\), valid because _v\<_2<sup>32</sup>). Algorithm 2 shows the kernel. Each work-item converts four consecutive elements of one column and writes one 32-bit word per modulus, so the kernel reads _A_ once and writes _s_ bytes per element.

## 4.3 INT8 products

The _s_ products are issued as a single strided-batch call (`oneapi::mkl::blas::gemm\_batch`, `int8`\(\times\)`int8`\(\rightarrow\)`int32`). For _k\>_131071 we split the _k_ dimension into chunks and sum their residues in the reconstruction.

## 4.4 CRT reconstruction with an FP32 quotient

Let \(r_t\in[0,2m_t)\) be any representative of \(C_{ij}^{(t)}\) mod _m<sub>t</sub>_ and _W<sub>t</sub>=M<sub>t</sub>y<sub>t</sub>_. Then \(Z=\sum_tr_tW_t\equiv\hat{c}_{ij}\) (mod _M_) and, exactly,

\(\frac{Z}{M}=\sum_{t=1}^s\frac{r_ty_t}{m_t},\) (6)

an identity also used in \[20, §4.4\]. Writing \(Z=\hat{c}_{ij}+qM\) with \(q\in\mathbb{Z}\), the bound of Eq. (4) gives \(|Z/M-q|\le 1/4\). The integer _q_ can therefore be recovered from a crude approximation of _Z/M_.

**Lemma 1.** _Let_ \(\tilde{z}\) _be_ \(\sum_tr_t\text{fl}_{32}(y_t/m_t)\) _accumulated with s FP32 fused multiply-ads. For_ \(s\le 24\) _and_ \(m_t\le 256\), \(|\tilde{z}-Z/M|<2^{-6}\)_; hence_ \(q=\text{rint}(\tilde{z})\).

_Proof sketch._ All partial sums are below \(2\cdot 256\cdot 24<2^{14}\), so each FMA contributes a rounding error of at most 2<sup>-11</sup>, and each representation error satisfies \(|r_t(\text{fl}_{32}(y_t/m_t)-y_t/m_t)|\le 2^92^{-24}\). The total is below 24(2<sup>-11</sup>+2<sup>-15</sup>)_\<_2<sup>-6</sup>, well inside the margin of 1/4.


3. Approximately _H_<sup>-1</sup>-normalize the vector resulting from the approximate _H_<sup>-1</sup> orthogonalization.

Algorithm 3.2 gives the details for one iteration of the resulting right preconditioned flexible Lanczos process.

**Algorithm 3.2** _m_ steps of right preconditioned flexible Lanczos for \(i\sigma H+B\) with approximate solves for _H_. \(\langle\cdot,\cdot\rangle\) denotes the standard inner product

1: choose initial vector _w_, compute \(\widehat{w}\approx H^{-1}w,\beta_0=\langle w,\widehat{w}\rangle\)

2: put \(v_1=w/\beta_0,z_1=\widehat{w}/\beta_0,v_0=0\)

3: **for** _k_=1_,...,m_ **do**

4: \(w=(i\sigma H+S)z_k\) {we have _z<sub>k</sub>≈H_<sup>-1</sup>_v<sub>k</sub>_ from the previous iteration}

5: \(\alpha_k=\langle w,z_k\rangle\)

6: \(\gamma_k=\langle w,z_{k-1}\rangle\)

7: \(w=w-\alpha_kv_k-\gamma_kv_{k-1}\)

8: \(\widehat{w}\approx H^{-1}w\)

9: \(\beta_k=\langle w,\widehat{w}\rangle^{1/2}\)

10: \(v_{k+1}=w/\beta_k\)

11: \(z_{k+1}=\widehat{w}/\beta_k\) {now _z_<sub>_k_+1</sub>≈_H_<sup>-1</sup>_v_<sub>_k_+1</sub>}

12: **end for**

In the non-flexible Algorithm 3.1 we used \(\langle w,\widetilde{v}_{k-1}\rangle=\langle H^{-1}v_k,v_k\rangle^{1/2}=\beta_{k-1}\), and we avoided to compute \(\langle w,\widetilde{v}_{m-1}\rangle\) explicitly. In the flexible context the above equality does not hold any more, since \(\langle w,\widetilde{v}_{m-1}\rangle\) is computed with the approximation _z_<sub>_m_-1</sub> for _H_<sup>-1</sup>_v_<sub>_m_-1</sub>, whereas \(\beta_m\) is computed with the approximation \(\widehat{w}\) for _H_<sup>-1</sup>_w_.

With the flexible Lanczos process we have the recurrence relation<tbc>

(3.4) \((i\sigma H+B)Z_m=V_{m+1}T_{m+1,m},\)

<tbc>were _T_<sub>_m_+1_,m_</sub> is again tridiagonal,

(3.5) \(T_{m+1,m}=\left[\begin{array}{ c c c c c c c }
\alpha_1 & \gamma_2 &  &  &  &  &  \\
\beta_1 & \alpha_2 & \gamma_3 &  &  &  &  \\
 & \beta_2 & \ddots & \ddots &  &  &  \\
 &  & \ddots & \ddots & \gamma_{m-1} &  \\
 &  &  & \beta_{m-1} & \alpha_m &  \\
 &  &  &  &  & \beta_m
\end{array}\right].\)

When used to solve the linear system (3.1), the initial vector _w_ in Algorithm 3.2 is the residual \(ib-(i\sigma H+B)x_0\), i.e., the first Lanczos vector _v_<sub>1</sub> is<tbc>

(3.6) \(v_1=\frac{1}{\beta_0}r_0\text{with}r_0=ib-(iH+B)x_0,\widehat{w}\approx H^{-1}r_0,\beta_0=\langle r_0,\widehat{w}\rangle^{1/2}.\)

<tbc>We emphasize that _V<sub>m</sub>_ is now only approximately _H_<sup>-1</sup>-orthonormal and _Z<sub>m</sub>_ is only approximately equal to _H_<sup>-1</sup>_V<sub>m</sub>_. We define the flexible GAL and MR iterates in analogy to (2.3) and (2.4) as \(x_m=x_0+Z_m\zeta_m\) with

(3.7) FGAL: \(T_m\zeta_m=\beta_0e_1,\)

(3.8) FMR: \(\zeta_m=\mathrm{argmin}\{\|\beta_0e_1-T_{m+1,m}\zeta_m\|_2\},\)


where the _margin_ \(\mu(\mathbf{q}):=\gamma(\overline{e_\mathbf{q}}M_n+\overline{n_\mathbf{q}}M_e+M_l)\) uses the database maxima _M<sub>n</sub>_, _M<sub>e</sub>_, and _M<sub>l</sub>_ of <o>_n_</o><sub>**x**</sub>, <o>_e_</o><sub>**x**</sub>, and |_l_<sub>**x**</sub>|.

The proof of Proposition 3 uses every coordinate of the retina vectors, which we now define. We assume that the data are scaled once so that every lifted coordinate and every _a_(**x**)/2 lies in the normal range of half precision. This assumption loses no generality, because a common scale multiplies all distances by the same factor and therefore leaves the neighbors unchanged.

The coordinates that carry the error terms are themselves stored in half precision and must still bound norms and errors from above. We therefore write fl(_v_) for the rounding of _v_ to the nearest half-precision number and up(_v_):=fl((1+2<sup>-10</sup>)_v_) for rounding up. Since rounding to nearest changes a value in the normal range by at most the relative 2<sup>-11</sup>, \(\mathrm{up}(v)\ge(1+2^{-10})(1-2^{-11})v>v\) for every _v\>_0. Although the norms inside up are computed in fp32, their relative error stays far below this margin. With these two operators, CertEx computes for each database vector **x**

\(\nu_\mathbf{x}:=(1+2^{-10})\mathrm{max}(\|\ell(\mathbf{x})\|,\|\tilde{\ell}(\mathbf{x})\|),\)<br>
\(\overline{n_\mathbf{x}}:=\mathrm{up}(\|\ell(\mathbf{x})\|),\)<br>
\(\overline{e_\mathbf{x}}:=\mathrm{up}(\delta(\mathbf{x})+\gamma\nu_\mathbf{x}),\)<br>
\(h_\mathbf{x}:=\mathrm{fl}(a(\mathbf{x})/2),\)<br>
\(l_\mathbf{x}:=\mathrm{fl}(a(\mathbf{x})/2-h_\mathbf{x}).\)

Here, the auxiliary value \(\nu_\mathbf{x}\) bounds both \(\|\ell(\mathbf{x})\|\) and \(\|\tilde{\ell}(\mathbf{x})\|\) from above. By the property of up, \(\overline{n_\mathbf{x}}\ge\|\ell(\mathbf{x})\|\) bounds the norm, and \(\overline{e_\mathbf{x}}\ge\delta(\mathbf{x})+\gamma\nu_\mathbf{x}\) bounds the rounding error \(\delta(\mathbf{x})\) together with the term \(\gamma\nu_\mathbf{x}\). This term absorbs the accumulation error of the products of the first _m_+1 coordinates (Step 3 of the proof below). Finally, the pair _h_<sub>**x**</sub>_,l_<sub>**x**</sub> stores _a_(**x**)/2 as a high and a low half-precision part. Correspondingly, for a query **q**, CertEx computes \(\overline{e_\mathbf{q}}:=\mathrm{up}(\delta(\mathbf{q}))\) and \(\overline{n_\mathbf{q}}:=\mathrm{up}(\|\tilde{\ell}(\mathbf{q})\|)\). The coefficient \(1-\varepsilon\) of \(\hat{\mathbf{q}}\) uses the smallest multiple \(\varepsilon\) of 2<sup>-11</sup> that exceeds \(\gamma\), so that \(1-\varepsilon\) is exact in half precision.

**Proposition 3** (No false dismissal)**.** _If_ \(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|\le U\)_, the computed product satisfies Eq._ (12)_, so that CertEx keeps_ **x**.

_Proof._ We bound the exact product _P_ from below, then the accumulation error, and combine the two bounds in four steps.

Step 1 bounds _P_ from below. The coordinates satisfy \(\overline{e_\mathbf{q}}\ge\delta(\mathbf{q})\), \(\overline{n_\mathbf{x}}\ge\|\ell(\mathbf{x})\|\), \(\overline{n_\mathbf{q}}\ge\|\tilde{\ell}(\mathbf{q})\|\), and \(\overline{e_\mathbf{x}}\ge\delta(\mathbf{x})+\gamma\nu_\mathbf{x}\), so that

\(\overline{e_\mathbf{q}}\overline{n_\mathbf{x}}+\overline{n_\mathbf{q}}\overline{e_\mathbf{x}}\ge\delta(\mathbf{q})\|\ell(\mathbf{x})\|+\|\tilde{\ell}(\mathbf{q})\|\delta(\mathbf{x})+\gamma\overline{n_\mathbf{q}}\nu_\mathbf{x}.\)

Adding \(\langle\tilde{\ell}(\mathbf{q}),\tilde{\ell}(\mathbf{x})\rangle\) to both sides and applying Eq. (10) bounds the first three terms of Eq. (11) from below by \(\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle+\gamma\overline{n_\mathbf{q}}\nu_\mathbf{x}\). The last two terms of Eq. (11) equal<tbc>

\(-(h_\mathbf{x}+l_\mathbf{x})+\varepsilon h_\mathbf{x}\)

<tbc>, which is at least \(-a(\mathbf{x})/2-\sigma_\mathbf{x}+\varepsilon h_\mathbf{x}\), where \(\sigma_\mathbf{x}:=|a(\mathbf{x})/2-h_\mathbf{x}-l_\mathbf{x}|\) is the error of the split. Hence

\(P\ge\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle-\frac{a(\mathbf{x})}{2}+\gamma\overline{n_\mathbf{q}}\nu_\mathbf{x}+\varepsilon h_\mathbf{x}-\sigma_\mathbf{x}.\) (13)

Step 2 bounds the split error. Rounding to nearest gives \(|a(\mathbf{x})/2-h_\mathbf{x}|\le 2^{-11}a(\mathbf{x})/2\) and then \(\sigma_\mathbf{x}\le 2^{-11}|a(\mathbf{x})/2-h_\mathbf{x}|\le 2^{-22}a(\mathbf{x})/2\). Since \(h_\mathbf{x}\ge(1-2^{-11})a(\mathbf{x})/2\), this gives \(\sigma_\mathbf{x}\le 2^{-21}h_\mathbf{x}\). The padded length _L_ is a multiple of 64, so that \(\gamma=16Lu\) with _u_=2<sup>-24</sup> is a multiple of 2<sup>-14</sup>, and so is \(\varepsilon\). Their difference is positive and therefore at least 2<sup>-14</sup>, which gives

\((\varepsilon-\gamma)h_\mathbf{x}\ge\sigma_\mathbf{x}.\) (14)

Step 3 bounds the accumulation error. Since the tensor cores multiply exactly and accumulate in fp32,

\(|\widehat{P}-P|\le\gamma\sum_i|\hat{q}_i\hat{x}_i|,\)

where \(\hat{q}_i\) and \(\hat{x}_i\) denote the _i_-th coordinates of \(\hat{\mathbf{q}}\) and \(\hat{\mathbf{x}}\). The Cauchy-Schwarz inequality bounds the sum over the first _m_+1 coordinates by \(\|\tilde{\ell}(\mathbf{q})\|\|\tilde{\ell}(\mathbf{x})\|\le\overline{n_\mathbf{q}}\nu_\mathbf{x}\). The remaining four products are <o>_e_</o><sub>**q**</sub><o>_n_</o><sub>**x**</sub>, \(\overline{n_\mathbf{q}}\overline{e_\mathbf{x}}\), \((1-\varepsilon)h_\mathbf{x}\le h_\mathbf{x}\), and |_l_<sub>**x**</sub>|. Replacing <o>_n_</o><sub>**x**</sub>, <o>_e_</o><sub>**x**</sub>, and |_l_<sub>**x**</sub>| by their database maxima gives

\(|\widehat{P}-P|\le\gamma\overline{n_\mathbf{q}}\nu_\mathbf{x}+\gamma h_\mathbf{x}+\mu(\mathbf{q}).\) (15)

Step 4 combines the bounds. Subtracting Eq. (15) from Eq. (13) and applying Eq. (14),

\(\widehat{P}\ge\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle-\frac{a(\mathbf{x})}{2}+(\varepsilon-\gamma)h_\mathbf{x}-\sigma_\mathbf{x}-\mu(\mathbf{q})\)<br>
\(\ge\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle-\frac{a(\mathbf{x})}{2}-\mu(\mathbf{q}).\)

By the premise and Eq. (9), \(\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle-a(\mathbf{x})/2\ge(a(\mathbf{q})-U^2)/2\). Hence \(\widehat{P}\ge\theta(\mathbf{q})\).

In the implementation, CertEx sets \(\gamma:=16Lu\), where _u_=2<sup>-24</sup> is the unit roundoff of fp32. This constant exceeds the worst-case constant that Blanchard et al. \[10\] derive for the accumulation of tensor cores, and it also covers an accumulator that truncates instead of rounding. In addition, CertEx inflates _U_<sup>2</sup> by the relative factor 1+10<sup>-4</sup>. The threshold \(\theta(\mathbf{q})\) is evaluated in fp64 and rounded down to fp32, so that neither rounding shrinks the kept set. Finally, the retina pass reads the database retina vectors once per batch of queries and writes out only the pairs that satisfy Eq. (12). The same certificate extends to the 8-bit integer tensor cores, whose retina halves the device memory per vector at the same width while every answer stays exact (Section 4.6).


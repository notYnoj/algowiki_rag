applying the same construction \(\lceil r/m\rceil\) times, obtaining an exact construction for _m_ independent matrix multiplications of dimension _n_<sup>2</sup> with rank at most \(r\lceil r/m\rceil\). Iterating this recursion gives a concrete sequence of algorithms, with additional recursive levels used as the input dimension increases, and can yield a better effective exponent \(\omega\). Inefficiency from the use of the ceiling may be addressed by first taking a sufficiently high tensor power of the construction. We now state the asymptotic sum theorem in slightly simplified form.

**Theorem 1.** _(Schönhage’s Asymptotic Sum Theorem \[30\]) Let_ \(\mathcal{M}=\oplus_{i=1}^m\langle n,n,n\rangle\) _be a direct sum of m matrix multiplication tensors. If the border rank is bounded by_ \(\underline{R}(\mathcal{M})\le r\)_, then the exponent of matrix multiplication_ \(\omega\) _satisfies_

\(mn^\omega\le r.\)

_Proof._ We provide an algorithmic proof for the simplified case where the direct sum consists of _m_ identical terms \(\langle n,n,n\rangle\) and the rank bound _r_ is divisible by _m_ in Appendix A. For the general proof involving multinomial coefficients and arbitrary dimensions, we refer the reader to \[30\] or the survey by Bläser \[10\].

## 4.3 The Coppersmith-Winograd Tensor

We first recall the tensor constructions of Coppersmith and Winograd \[15\].

**Definition 5** (Little CW tensor)**.** _For_ \(x,y,z\in\mathbb{C}^{n+1}\)_, the little CW tensor is defined by the trilinear form,_<tbc>

\(\phi_\mathrm{CW}(x,y,z)=\sum_{i=1}^n\big(x_iy_iz_0+x_iy_0z_i+x_0y_iz_i\big).\) (16)

<tbc>For \(n\ge 2\), the little CW tensor has border rank exactly _n_+2 \[14, Section 1.2\]. The upper bound, valid for all \(n\ge 1\), is shown by

\(\phi_\mathrm{CW}(x,y,z)=\mathrm{lim}_{\lambda\rightarrow 0}\big[\lambda^{-2}\sum_{i=1}^n(x_0+\lambda x_i)(y_0+\lambda y_i)(z_0+\lambda z_i)\) (17)

\(-\lambda^{-3}(x_0+\lambda^2\sum_{i=1}^nx_i)(y_0+\lambda^2\sum_{j=1}^ny_j)(z_0+\lambda^2\sum_{k=1}^nz_k)\) (18)

\(-(\lambda^{-2}n-\lambda^{-3})x_0y_0z_0\big].\) (19)

For _n_=1, the little CW tensor instead has border rank two.

**Definition 6** (Big CW tensor)**.** _For_ \(x,y,z\in\mathbb{C}^{n+2}\)_, the big CW tensor is defined by the trilinear form,_

\(\phi_\mathrm{BCW}(x,y,z)=\sum_{i=1}^n\big(x_iy_iz_0+x_iy_0z_i+x_0y_iz_i\big)+x_0y_0z_{n+1}+x_0y_{n+1}z_0+x_{n+1}y_0z_0.\) (20)

The big CW tensor has border rank exactly _n_+2: its flattening in any variable space has matrix rank _n_+2, giving the lower bound, and the following degeneration gives the upper bound

\(\phi_\mathrm{BCW}(x,y,z)=\mathrm{lim}_{\lambda\rightarrow 0}\big[\lambda^{-2}\sum_{i=1}^n(x_0+\lambda x_i)(y_0+\lambda y_i)(z_0+\lambda z_i)\) (21)

\(-\lambda^{-3}(x_0+\lambda^2\sum_{i=1}^nx_i)(y_0+\lambda^2\sum_{j=1}^ny_j)(z_0+\lambda^2\sum_{k=1}^nz_k)\) (22)

\(-(1/\sigma_{\lambda,n})(x_0-\sigma_{\lambda,n}x_{n+1})(y_0-\sigma_{\lambda,n}y_{n+1})(z_0-\sigma_{\lambda,n}z_{n+1})\big],\) (23)

\(\sigma_{\lambda,n}=\frac{\lambda^3}{n\lambda-1}.\) (24)


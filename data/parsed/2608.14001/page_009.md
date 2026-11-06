<tbc>_Theorem 6:_ Let \(\mathbf{T}\in\mathbb{C}^{\ell\times m}\) be as in (14). Consider \(z_p=e^{i\theta_p}\) for \(p\in\{1,\dots,m\}\) with \(\{\theta_p\}_{p=1}^m\in\mathbb{R}\) distinct. Let \(\{\tau_k\}_{k=1}^\ell>0\) be a set of distinct powers. Then, provided<tbc>

\(\mathrm{max}_{p\in\{1,\dots,m\}}\sum_{q=1,p\neq q}^m\left|\mathbb{E}[e^{-i\gamma_{pq}\tau}]\right|\le\varepsilon<1\) (39)

<tbc>the scaled condition number has the upper bound:

\(\tilde{\kappa}_m\left(\sqrt{\frac{m}{\ell}}\mathbf{T}\right):=\kappa_m\left(\sqrt{\frac{m}{\ell}}\mathbf{T}\right)^{1/\genfrac(){pt}{2}{m}{2}}\le\left(\frac{1+\varepsilon}{1-\varepsilon}\right)^\frac{1}{m(m-1)}\) (40)

_Proof:_ Provided (39) is satisfied, then from (37) \(\lambda_\mathrm{max}(\mathbf{S})\le m(1+\varepsilon)\) and from (36) \(\lambda_\mathrm{min}\ge m(1-\varepsilon)\). Since \(\kappa(\mathbf{S})=\left(\frac{\lambda_\mathrm{max}(\mathbf{S})}{\lambda_\mathrm{min}(\mathbf{S})}\right)^{1/2}\) , by normalizing with the power \(1/\genfrac(){pt}{2}{m}{2}\), the result follows.

The conclusions of Theorem 5 rest on the assumption that \(\mathrm{max}_{p\in\{1,\dots,m\}}R_{p,\infty}=0\). To show this is reasonable, we compute \(R_{p,\infty}\) for different time-sampling schemes: (1) the uniform distribution, to simulate time-delays that are on average uniformly-spaced and which we would expect to behave like the deterministic evenly-spaced sampling scheme; (2) the exponential distribution, to stimulate delays across different orders of magnitude, potentially like in multi-scale modeling; and (3) the normal distribution.

### 1) Uniform Distribution:

Suppose the delays \(\{\tau_k\}_{k=1}^\ell\) are i.i.d. uniform random variables, \(\tau\sim\mathcal{U}[0,\ell]\) with \(\Omega:=[0,\ell]\).

\(\mathbb{E}[e^{-i\gamma_{pq}\tau}]=\int_\Omega e^{-i\gamma_{pq}\tau} f(\tau)\mathrm{d}\tau=\frac{1}{\ell}\int_0^\ell e^{-i\gamma_{pq}\tau}\mathrm{d}\tau\)<br>
\(=\frac{1}{\ell}\frac{i}{\gamma_{pq}}e^{-i\gamma_{pq}\ell/2}\left(e^{-i\gamma_{pq}\ell/2}-e^{i\gamma_{pq}\ell/2}\right)\)<br>
\(=\frac{2}{\ell\gamma_{pq}}e^{-i\gamma_{pq}\ell/2}\mathrm{sin}\left(\frac{\gamma_{pq}\ell}{2}\right)\) (41)

Taking the modulus of the expected value nullifies the exponential oscillatory behavior, leaving:

\(|\mathbb{E}[e^{-i\gamma_{pq}\tau}]|=\left|\mathrm{sin}\left(\frac{\gamma_{pq}\ell}{2}\right)\cdot\left(\frac{\gamma_{pq}\ell}{2}\right)^{-1}\right|=\left|\mathrm{sinc}\left(\frac{\gamma_{pq}\ell}{2}\right)\right|\) (42)

As \(\ell\rightarrow\infty\), \(|\mathbb{E}[e^{-i\gamma_{pq}\tau}]|\rightarrow 0\) (42) based on the behavior of the \(\mathrm{sinc}(\cdot)\) function. Then, \(R_{p,\infty}\), as a finite linear combination of functions that converge to zero as \(\ell\rightarrow\infty\) also converges to zero, the conclusions of Theorem 5 hold.

### 2) Exponential Distribution:

Suppose now that the delays \(\{\tau_k\}_{k=1}^\ell\) are i.i.d. exponential random variables, \(\tau\sim\mathrm{Exp}(\lambda)\), where the PDF is \(f(\tau;\lambda)=\lambda e^{-\lambda\tau}\), valid for \(\tau\ge 0\) and with rate parameter \(\lambda>0\). To fit \(1-\varepsilon\) of the distribution in the interval \([0,\ell]\), pick \(\lambda=\frac{-\mathrm{ln}(\varepsilon)}{\ell}\) . Then,<tbc>

\(\mathbb{E}[e^{-i\gamma_{pq}\tau}]=\int_0^\infty e^{-i\gamma_{pq}\tau}\lambda e^{-\lambda\tau}\mathrm{d}\tau=\frac{\lambda}{\lambda+i\gamma_{pq}}\) (43)

<tbc>Taking the modulus of the above, we have:

\(|\mathbb{E}[e^{-i\gamma_{pq}\tau}]|=|\lambda|/\sqrt{\lambda^2+\gamma_{pq}^2}\) (44)

Substituting \(\lambda=\frac{-\mathrm{ln}(\varepsilon)}{\ell}\) and taking the limit as \(\ell\rightarrow\infty\),

\(\mathrm{lim}_{\ell\rightarrow\infty}|\lambda|/\sqrt{\lambda^2+\gamma_{pq}^2}=\mathrm{lim}_{\ell\rightarrow\infty}\frac{-\mathrm{ln}(\varepsilon)}{\sqrt{\mathrm{ln}(\varepsilon)^2+\ell^2\gamma_{pq}^2}}=0\) (45)

and thus \(R_{p,\infty}\rightarrow 0\) and the conclusions of Theorem 5 apply.

### 3) Normal Distribution:

If the delays \(\{\tau_k\}_{k=1}^\ell\) are i.i.d. normally-distributed random variables, \(\tau\sim\mathcal{N}(\mu,\sigma^2)\), we can pick \(\mu=\ell/2\) and \(\sigma^2=\alpha\ell^2\) for some \(\alpha>0\) such that a high percentage of the distribution is contained within \([0,\ell]\). Of course, unlike a truncated normal distribution, this would allow, albeit with low probability, negative sampling times, which would not be realistic. However, for the purpose of analysis, it is sufficiently reasonable. Then,

\(\mathbb{E}[e^{-i\gamma_{pq}\tau}]=\int_{-\infty}^\infty e^{-i\gamma_{pq}\tau}\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{exp}\left(-\frac{(\tau-\mu)^2}{2\sigma^2}\right)\mathrm{d}\tau\)<br>
\(=\frac{1}{\sqrt{2\pi\sigma^2}}\int_{-\infty}^\infty e^{-i\gamma_{pq}\tau-\frac{(\tau-\mu)^2}{2\sigma^2}}\mathrm{d}\tau\)<br>
\(=\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{exp}(-i\mu\gamma_{pq}-\frac{1}{2}\sigma^2\gamma_{pq}^2)\) (46)

Taking the modulus of (46) cancels oscillations, and by (34):

\(R_{p,\infty}=m\sum_{q=1,p\neq q}^m\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{exp}(-\frac{1}{2}\sigma^2\gamma_{pq}^2)\) (47)

When \(\ell\rightarrow\infty\), \(\sigma^2\rightarrow\infty\) too and the distribution escapes to infinity so that the CDF for any finite value is zero, in which case \(R_{p,\infty}\rightarrow 0\) for all \(p\in\{1,\dots,m\}\), thereby leading to the conclusions of Theorem 5.

### 4) Numerical Simulations:

To empirically test the propositions in Conjecture 1, we generated random conjugate pairs of frequencies \(\{\pm\theta_j\}_{j=1}^d\) for \(d\in\{1,\dots,50\}\) drawn uniformly from \([0,\pi]\). For each choice of _d_, we performed 50 iterations to generate a representative average and variance for the results. To find the rank, scaled determinant, and condition number of \(\sqrt{m/\ell}\mathbf{T}\), we computed the singular values of the matrix using the SVD. The rank is the number of nonzero singular values; the condition number is the ratio of the largest to the smallest singular value; and the scaled determinant is the product of the singular values normalized by \(1/\genfrac(){pt}{2}{m}{2}\).

Figure 2 illustrates the rank of **T**; Figure 3 depicts the normalized determinant; and Figure 4 shows the normalized condition number for different numbers of points _m_ in the regime where \(\ell\rightarrow\infty\). For each property, the plot compares the result for the generalized Vandermonde matrix for the 3 chosen PDFs (uniform, exponential, and normal) with that of the normal Vandermonde matrix, which is the baseline. Empirically, **T** is always full rank, and the normalized condition number and rank of the generalized Vandermonde matrices converge to 1 as \(m\rightarrow\infty\). The normalized determinant upper bound of _m_<sup>1/(_m_-1)</sup> is an overestimate for when \(\ell\checkmark+\infty\). Thus, empirical results seem to suggest that generalized Vandermonde matrices tend to behave similarly to regular Vandermonde matrices with consecutive integer powers.


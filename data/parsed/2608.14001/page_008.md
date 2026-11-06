<tbc>Combining (28) and (29):<tbc>

\(\tilde{d}_m(\mathbf{T})\le\left(\frac{m}{\ell}\times\frac{1}{m}\sum_{p=1}^m\sigma_p(\mathbf{T})^2\right)^{1/(m-1)}\)

<tbc>Since \(\sum_{p=1}^m\sigma_p(\mathbf{T})^2=\mathrm{tr}(\mathbf{T}^H\mathbf{T})\),<tbc>

\(\tilde{d}_m(\mathbf{T})\le\left(\frac{1}{\ell}\mathrm{tr}(\mathbf{T}^H\mathbf{T})\right)^{1/(m-1)}\)

<tbc>With \(\mathrm{tr}(\mathbf{T}^H\mathbf{T})=m\ell\) from (27),<tbc>

\(\tilde{d}_m(\mathbf{T})\le m^{1/(m-1)}\)

<tbc>As \(m\rightarrow\infty\), \(m^{1/(m-1)}\rightarrow 1\), meaning the pseudo-transfinite diameter is bounded above by 1 in the limit, and the rate of convergence is at least related to _m_<sup>1/(_m_-1)</sup>, which is \(O\left(\frac{\mathrm{ln}(m)}{m}\right)\). While the bound on the convergence rate is sub linear in terms of _m_-the number of frequencies or dimensions present in the system, importantly the result does converge and it does so independently of the number of lags \(\ell\) used. The only inequality in the proof was in (29), so any improvement on the bound would require a tighter inequality. \(\blacksquare\)

_Remark 1:_ If **T** was normalized not by \(\sqrt{m/\ell}\) but instead by \(1/\sqrt{\ell}\), the above bound would be 1 for all _m\>_1. This would provide a uniform upper bound and would match the Fourier Vandermonde matrices considered by \[26\], but may not scale the "energy" to be comparable to a regular square Vandermonde matrix.

Let the delays \(\{\tau_k\}_{k=1}^\ell\) be independent and identically- distributed (i.i.d.) random variables, and suppose, for consistency with the evenly-sampled setting, that the interval of interest for the particular distribution of each \(\tau_k\) for \(k\in\{1,\dots,\ell\}\) is mostly contained in \([0,\ell]\). To analyze the behavior of _R<sub>p</sub>_ (23) as \(\ell\rightarrow\infty\), we first define an empirical measure:<tbc>

\(\mu_\ell(\tau):=\frac{1}{\ell}\sum_{k=1}^\ell\delta_{\tau_k}(\tau)\) (30)

<tbc>where \(\delta\) here is the delta function. In this case:<tbc>

\(\frac{1}{\ell}\sum_{k=1}^\ell e^{-i(\theta_p-\theta_q)\tau_k}=\int e^{-i(\theta_p-\theta_q)\tau}\mathrm{d}\mu_\ell(\tau)\)

<tbc>For a random variable \(\tau\), define the function \(g(\tau):=e^{-i(\theta_p-\theta_q)\tau}\). The Strong Law of Large Numbers \[33\] states that for every bounded measurable function _g_,<tbc>

\(\int g(\tau)\mathrm{d}\mu_\ell(\tau)=\frac{1}{\ell}\sum_{k=1}^\ell g(\tau_k)\longrightarrow^{a.s.}\int g(\tau)\mathrm{d}\mu(\tau)\) (31)

<tbc>meaning the empirical measures \(\mu_\ell\) converge almost surely in the weak sense to the measure \(\mu\), defined on the domain \(\Omega\). Since \(g(\tau)=e^{-i(\theta_p-\theta_q)\tau}\) is a bounded measurable function,<tbc>

\(\int e^{-i(\theta_p-\theta_q)\tau}\mathrm{d}\mu_\ell(\tau)\longrightarrow^{a.s.}\int e^{-i(\theta_p-\theta_q)\tau}\mathrm{d}\mu(\tau)\) (32)

<tbc>For convenience, define \(\gamma_{pq}:=\theta_p-\theta_q\). Then, considering the Gerschgorin radii of \(\mathbf{S}=\frac{m}{\ell}\mathbf{T}^H\mathbf{T}\) from (23) and using (32):

\(R_{p,\infty}:=\mathrm{lim}_{\ell\rightarrow\infty} R_p=\mathrm{lim}_{\ell\rightarrow\infty} m\sum_{q=1,p\neq q}^m\left|\frac{1}{\ell}\sum_{k=1}^\ell e^{-i\gamma_{pq}\tau_k}\right|=m\sum_{q=1,p\neq q}^m\left|\mathrm{lim}_{\ell\rightarrow\infty}\frac{1}{\ell}\sum_{k=1}^\ell e^{-i\gamma_{pq}\tau_k}\right|=m\sum_{q=1,p\neq q}^m\left|\int_\Omega e^{-i\gamma_{pq}\tau}\mathrm{d}\mu(\tau)\right|\) (33)

If the random variable \(\tau\) is distributed according to the probability density function (PDF) \(f(\tau)\) on a set \(\Omega\), then

\(R_{p,\infty}=m\sum_{q=1,p\neq q}^m\left|\int_\Omega e^{-i\gamma_{pq}\tau} f(\tau)\mathrm{d}\tau\right|=m\sum_{q=1,p\neq q}^m\left|\mathbb{E}[e^{-i\gamma_{pq}\tau}]\right|\) (34)

By Gerschgorin’s circle theorem (Theorem 1), it follows that all the eigenvalues of **S** are contained in the interval:

\(\lambda(\mathbf{S})\in\left[\mathrm{min}_{p\in\{1,\dots,m\}}\{s_{pp}-R_{p,\infty}\},\mathrm{max}_{p\in\{1,\dots,m\}}\{s_{pp}+R_{p,\infty}\}\right]\) (35)

With \(\mathrm{min}_{p\in\{1,\dots,m\}}\{s_{pp}\}=m\), \(\mathrm{max}_{p\in\{1,\dots,m\}}\{s_{pp}\}=m\),

\(\lambda_\mathrm{min}(\mathbf{S})\ge m\left(1-\mathrm{max}_{p\in\{1,\dots,m\}}\sum_{q=1,p\neq q}^m\left|\mathbb{E}[e^{-i\gamma_{pq}\tau}]\right|\right)\) (36)

\(\lambda_\mathrm{max}(\mathbf{S})\le m\left(1+\mathrm{max}_{p\in\{1,\dots,m\}}\sum_{q=1,p\neq q}^m\left|\mathbb{E}[e^{-i\gamma_{pq}\tau}]\right|\right)\) (37)

_Theorem 5:_ Let \(\mathbf{T}\in\mathbb{C}^{\ell\times m}\) be a generalized Vandermonde matrix as in (14). Suppose that \(\mathrm{max}_{p\in\{1,\dots,m\}}R_{p,\infty}=0\) with \(R_{p,\infty}\) as in (34). Then,

1) \(\mathrm{lim}_{\ell\rightarrow\infty}\mathrm{rank}(\mathbf{T})=m\);<tbc>

2) \(\mathrm{lim}_{\ell\rightarrow\infty}\tilde{d}_m(\mathbf{T})=m^{1/(m-1)}\);<tbc>

3) \(\mathrm{lim}_{\ell\rightarrow\infty}\kappa\left(\sqrt{\frac{m}{\ell}}\mathbf{T}\right)=1\).

<tbc>_Proof:_ If \(\mathrm{max}_{p\in\{1,\dots,m\}}R_{p,\infty}=0\), then by (36), \(\lambda_\mathrm{min}(\mathbf{S})\ge m\), and by (37), \(\lambda_\mathrm{max}(\mathbf{S})\le m\). So, all _m_ eigenvalues of **S** converge to _m_. Since \(0<m<+\infty\), all _m_ eigenvalues are nonzero, so rank(**S**)=_m_, and, since rank(**T**)=rank(**T**_<sup>H</sup>_**T**)=rank(**S**), rank(**T**)=_m_. Next, the determinant is the product of the eigenvalues, so det(**S**)=_m<sup>m</sup>_, and, using (4),<tbc>

\(\tilde{d}_m(\mathbf{T})=\left(\mathrm{det}(\mathbf{S})^{1/2}\right)^{1/\genfrac(){pt}{2}{m}{2}}=m^{1/(m-1)}\)

<tbc>Thus, in the asymptotic regime as \(\ell\rightarrow\infty\), the upper bound on the determinant derived from Theorem 4 is sharp. Finally,

\(\mathrm{lim}_{\ell\rightarrow\infty}\kappa\left(\sqrt{\frac{m}{\ell}}\mathbf{T}\right)=\frac{\sigma_\mathrm{max}\left(\sqrt{\frac{m}{\ell}}\mathbf{T}\right)}{\sigma_\mathrm{min}\left(\sqrt{\frac{m}{\ell}}\mathbf{T}\right)}=\left(\frac{\lambda_\mathrm{max}(\mathbf{S})}{\lambda_\mathrm{min}(\mathbf{S})}\right)^{1/2}=1\) (38)


• Backward sweep: in decreasing order of _j_, solve for \(\mathbf{U}_j^{(n,\ell+1)}\) from<tbc>

\(\mathbf{U}_j^{(n,\ell+1)}=(1-\nu)\mathbf{U}_j^{(n,\ell+1/2)}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{U}_{j-1}^{(n,\ell+1/2)}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{U}_{j+1}^{(n,\ell+1)}-\frac{\nu}{2C_{M+1}}\mathbf{b}\left(u_{j+1,3}^{(n,\gamma_1)}-u_{j-1,3}^{(n,\gamma_1)}\right).\) \(\text{(34)}\)

3. The solution after the (_n_+1)th FIM iteration is then given by

\(\mathbf{u}_j^{(n+1)}=\left((\mathbf{U}_j^{(n,\gamma_2)})^\mathsf{T},u_{j,3}^{(n,\gamma_1)},u_{j,4}^{(n,\gamma_1)},\dots,u_{j,M}^{(n,\gamma_1)}\right)^\mathsf{T}.\) \(\text{(35)}\)

The results of the Fourier analysis of this numerical method are presented in the next subsection.

## 3.2. Results of the Fourier analysis and low-frequency behavior

Define the error after _n_ FIM iterations by<tbc>

\(\delta\mathbf{u}_j^{(n)}=\mathbf{u}_j^{(n)}-\mathbf{u}_j,\) (36)

<tbc>where **_u_**_<sub>j</sub>_ is the exact solution of the discrete system (30). We neglect boundary effects associated with the sweeps and assume that the solution is periodic in space with period \(2\pi\). Consider a Fourier mode of the form<tbc>

\(\delta\mathbf{u}_j^{(n)}=\widehat{\mathbf{e}}^{(n)}(k)e^{\mathrm{i}jk\Delta x},\widehat{\mathbf{e}}^{(n)}(k)\in\mathbb{C}^{M+1}.\) (37)

<tbc>Since the numerical scheme is linear, we define its Fourier error-propagation matrix \(\mathbf{T}(\varepsilon,k)\) by

\(\widehat{\mathbf{e}}^{(n+1)}(k)=\mathbf{T}(\varepsilon,k)\widehat{\mathbf{e}}^{(n)}(k),\mathbf{T}(\varepsilon,k)\in\mathbb{C}^{(M+1)\times(M+1)}.\) (38)

The maximum magnitude of the amplification factors is given by the spectral radius of \(\mathbf{T}(\varepsilon,k)\).

As shown in Appendix C.3, at most three eigenvalues of \(\mathbf{T}(\varepsilon,k)\) have _O_(1) leading terms in the near-continuum limit \(\varepsilon\rightarrow 0\). They are indexed by \(\mu\in\{-\sqrt{3},0,\sqrt{3}\}\), the eigenvalues of **A**_<sub>h</sub>_, and can be expanded as

\(\Lambda_\mu(\varepsilon,k)=\Lambda_\mu^{(0)}(k)+\varepsilon\Lambda_\mu^{(1)}(k)+O(\varepsilon^2).\) (39)

The remaining _M_-2 eigenvalues have magnitudes of \(O(\varepsilon)\) and are therefore negligible in the near-continuum limit. For the three branches in (39), define

\(\mathcal{G}_\mu^{(0)}(k)=\frac{\left[1-\nu+\frac{\nu}{2}\left(1-\frac{\mu}{C_{M+1}}\right)e^{\mathrm{i}k\Delta x}\right]\left[1-\nu+\frac{\nu}{2}\left(1+\frac{\mu}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x}\right]}{\left[1-\frac{\nu}{2}\left(1+\frac{\mu}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x}\right]\left[1-\frac{\nu}{2}\left(1-\frac{\mu}{C_{M+1}}\right)e^{\mathrm{i}k\Delta x}\right]}.\) (40)

Their leading amplification factors are

\(\Lambda_\mu^{(0)}(k)=\left[\mathcal{G}_\mu^{(0)}(k)\right]^{\gamma_1+\gamma_2},\mu\in\{-\sqrt{3},0,\sqrt{3}\}.\) (41)

When \(\gamma_1=1\), the first-order term \(\Lambda_\mu^{(1)}(k)\) has also been derived. Due to its complexity, we refer readers to Appendix C.5 (equation (C.46)) for its expression.

It can be shown that \(|\mathcal{G}_\mu^{(0)}(k)|\) attains its maximum value of 1 at _k_=0 for all \(\mu\in\{-\sqrt{3},0,\sqrt{3}\}\) (see Proposition 1). Meanwhile, when \(|k\Delta x|<2\pi/5\), we have \(|\mathcal{G}_0^{(0)}(k)|\ge|\mathcal{G}_{\pm\sqrt{3}}^{(0)}(k)|\) (see Proposition 2). Therefore, we will mainly focus on the case \(\mu=0\) and small nonzero values of \(|k\Delta x|\). In this case, we have<tbc>

\(\Lambda_0^{(0)}(k)=\mathrm{exp}\left(-\frac{2\nu}{2-\nu}(\gamma_1+\gamma_2)k^2\Delta x^2\right)+O\left((k\Delta x)^4\right).\)

<tbc>This result is consistent with the well-known smoothing property of the SGS method, indicating that the number of sweeps required to reduce a fixed low-frequency error mode by a constant factor should scale as \(\Delta x^{-2}\) for fixed \(\nu\). It also shows the benefit of the FIM method: when \(\varepsilon\) is small, one can increase \(\gamma_2\) while reducing \(\gamma_1\), keeping their<tbc>


## E First-order covariance of L-comoment ratios

We consider the sample versions of the standardized coefficients \(\tau_m^{[XY]}\) and \(\tau_m^{[YX]}\) of Section 2,

\(\widehat{\tau}_m^{[XY]}=\frac{\widehat{\lambda}_m^{[XY]}}{\widehat{\lambda}_2(X)},\widehat{\tau}_m^{[YX]}=\frac{\widehat{\lambda}_m^{[YX]}}{\widehat{\lambda}_2(Y)},m=2,3.\) (E.1)

The denominators are the marginal sample L-scales of the measured variables. The covariance of these nonlinear ratios is not obtained exactly by linear transformation of the underlying moment covariance. Following Elamir and Seheult (2004), who distinguished exact covariances of sample L-moments from Taylor-approximated standard errors of their ratios, we use the delta method (Oehlert, 1992; van der Vaart, 1998).

**Corollary E.1** (Joint first-order ratio covariance)**.** _Assume the margins are continuous and nondegenerate and_ \(\mathbb{E}(X^2+Y^2)<\infty\)_. Let_<tbc>

\(\widehat{\mathbf{m}}_n=\left(\widehat{\lambda}_2^{[XY]},\widehat{\lambda}_2^{[YX]},\widehat{\lambda}_3^{[XY]},\widehat{\lambda}_3^{[YX]},\widehat{\lambda}_2(X),\widehat{\lambda}_2(Y)\right)^\mathsf{T}\)

<tbc>_be the vector of the four sample L-comoments and the two marginal sample L-scales, and let_ \(\mathbf{m}=\mathbb{E}(\widehat{\mathbf{m}}_n)=(m_1,\dots,m_6)^\mathsf{T}\)_. Denote their exact finite-sample covariance by C<sub>M,n</sub>, and its leading Hoeffding term by_ \(\Omega_M\)_, so that_ \(C_{M,n}=\Omega_M/n+O(n^{-2})\)_. Define the map_ \(g:\mathbb{R}^4\times(0,\infty)^2\rightarrow\mathbb{R}^4\) _by_<tbc>

\(g(m_1,\dots,m_6)=\left(\frac{m_1}{m_5},\frac{m_2}{m_6},\frac{m_3}{m_5},\frac{m_4}{m_6}\right)^\mathsf{T},\)

<tbc>_so that_ \(g(\widehat{\mathbf{m}}_n)=(\widehat{\tau}_2^{[XY]},\widehat{\tau}_2^{[YX]},\widehat{\tau}_3^{[XY]},\widehat{\tau}_3^{[YX]})^\mathsf{T}\) _by_ (E.1)_. Its Jacobian at **m** is_<tbc>

\(J=Dg(\mathbf{m})=\left(\begin{array}{ c c c c c c c }
1/m_5 & 0 & 0 & 0 & -m_1/m_5^2 & 0 \\
0 & 1/m_6 & 0 & 0 & 0 & -m_2/m_6^2 \\
0 & 0 & 1/m_5 & 0 & -m_3/m_5^2 & 0 \\
0 & 0 & 0 & 1/m_6 & 0 & -m_4/m_6^2
\end{array}\right).\)

<tbc>_Then_<tbc>

\(\sqrt{n}\{g(\widehat{\mathbf{m}}_n)-g(\mathbf{m})\}\rightarrow^dN_4(0,J\Omega_MJ^\mathsf{T}).\) (E.2)

<tbc>_In particular, if_ \(\widehat{J}_n=Dg(\widehat{\mathbf{m}}_n)\) _and_ \(\widehat{\Omega}_{M,n}\) _is the projection-based covariance estimator for this enlarged moment vector, then_<tbc>

\(\widehat{V}_{\tau,n}=n^{-1}\widehat{J}_n\widehat{\Omega}_{M,n}\widehat{J}_n^\mathsf{T},n\widehat{V}_{\tau,n}\rightarrow^pJ\Omega_MJ^\mathsf{T}.\) (E.3)

<tbc>_For arbitrary ratios R=A/B and S=C/D, write r_=E(_A)/_E(_B), s_=E(_C)/_E(_D), b_=E(_B)\>_0_, and d_=E(_D)\>_0_. A first-order Taylor approximation to their covariance, when defined, is_<tbc>

\(\mathrm{Cov}(R,S)\approx\frac{\mathrm{Cov}(A,C)-s\mathrm{Cov}(A,D)-r\mathrm{Cov}(B,C)+rs\mathrm{Cov}(B,D)}{bd},\) (E.4)


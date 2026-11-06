**Proof:** We follow the proof of Theorem 6.1, showing that there exists \(h_\xi\) such that \(U_m=T_m(h_\xi)\) for all \(m\in\mathbb{N}\). We prove that the series<tbc>

\(h_\xi(\theta):=\sum_{k=0}^\infty\gamma_ke^{-\rho k\Delta t}e^{\mathrm{i}k\theta},\)

<tbc>with \(\gamma_k\) defined by (6.5), belongs to the Wiener class. Considering \(\psi_\xi(t):=t^{1-\xi}\) and using (6.4), we have

\(\gamma_k=(k+1)^{1-\xi}-2k^{1-\xi}+(k-1)^{1-\xi}\)<br>
\(=\left(\frac{m}{T}\right)^{1-\xi}\left[t_{k+1}^{1-\xi}-2t_k^{1-\xi}+t_{k-1}^{1-\xi}\right]\)<br>
\(=\left(\frac{m}{T}\right)^{1-\xi}\left[\psi_\xi(t_{k+1})-2\psi_\xi(t_k)+\psi_\xi(t_{k-1})\right]\)<br>
\(=\left(\frac{m}{T}\right)^{1-\xi}\left[\frac{\psi_\xi(t_{k+1})-2\psi_\xi(t_k)+\psi_\xi(t_{k-1})}{\Delta t^2}\right]\Delta t^2\)<br>
\(=\left(\frac{T}{m}\right)^{1+\xi}\left[\psi''_\xi(t_k)+O(\Delta t^2)\right]\text{as}k\rightarrow\infty,\)

using \(\Delta t=\frac{T}{m}\) and a standard central finite difference scheme. From<tbc>

\(\psi''_\xi(x)=\xi(\xi-1)\frac{1}{t^{1+\xi}},\)

<tbc>we have

\(\gamma_k=\left(\frac{T}{m}\right)^{1+\xi}\xi(\xi-1)\frac{1}{t_k^{1+\xi}}+\Delta t^{1+\xi} O(\Delta t^2)\)<br>
\(=\left(\frac{T}{m}\right)^{1+\xi}\frac{\xi(\xi-1)}{k^{1+\xi}}\left(\frac{m}{T}\right)^{1+\xi}+O(\Delta t^{3+\xi})\)<br>
\(=\frac{\xi(\xi-1)}{k^{1+\xi}}+O(\Delta t^{3+\xi}).\)

Since \(\xi\in(0,1)\) and \(\rho>0\), the series<tbc>

\(\sum_{k=0}^\infty\left|\gamma_ke^{-\rho k\Delta t}\right|\)

<tbc>is convergent, and \(h_\xi\) belongs to the Wiener class by definition. Since \(h_\xi\) belongs to the Wiener class, it is a continuous and hence Lebesgue integrable function, so that \(U_m=T_m(h_\xi)\). As a consequence of Axiom GLT 2 and of Axiom GLT 1 we conclude

\(\{U_m\}_m\sim_{\mathrm{GLT},\sigma} h_\xi(\theta),\)

while the eigenvalue distribution is obvious from the triangular structure.

**Remark 6.3** _As it is evident from the final part of the proofs of Theorem 6.1 and Theorem 6.2, the fact that the involved generating functions belong to the Wiener class is not a goal, but it is instrumental in applying the GLT axioms for deducing in a fast way the distribution in the sense of the singular values._


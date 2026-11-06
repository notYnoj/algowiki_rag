listed in ascending order. The square root branch is taken on the right half-plane, ensuring \(\nu_j^k>0\) for \(j\ge 1\), with further behavior outlined as \(\mathrm{lim}_{j\rightarrow\infty}\left(\sqrt{\nu_j^k}-\pi j\right)=0\), \(\nu_j^k>0\) if \(d\mu_k^2<1\), \(\nu_0^k<0\) if \(d\mu_k^2>1\), and \(\nu_0^k=0\) if \(d\mu_k^2=1\). In the latter case, the eigenfunction takes the form<tbc>

\(X_{0,k}(x,y)=2x\mathrm{sin}(\mu_ky).\)

<tbc>It is verified that the system _Y<sub>j,k</sub>(x,y),j_=1,2_,...;k_=1,2_,..._, defined as<tbc>

\(Y_{j,k}(x,y)=\frac{2}{\chi_{j,k}}\left[\mathrm{sin}\left(\sqrt{\nu_j^k}x\right)-\frac{\mathrm{sin}\left(\sqrt{\nu_j^k}\right)}{\mathrm{sin}\left(\sqrt{\nu_0^k}\right)}\mathrm{sin}\left(\sqrt{\nu_0^k}x\right)\right]\mathrm{sin}(\mu_ky),\)

<tbc>is bi-orthogonal in \(L^2((0,1)\times(0,1))\) to the system _X<sub>j,k</sub>(x,y),j,k_=1,2_,..._. The denominator \(\chi_{j,k}\) for _Y<sub>j,k</sub>(x,y_) is given by

\(\chi_{j,k}=1+\frac{d\mathrm{sin}^2\left(\sqrt{\nu_j^k}\right)}{\sqrt{\nu_j^k}}\left(\sqrt{\nu_j^k}-\frac{\mu_k^2}{\sqrt{\nu_j^k}}\right)\)<br>
\(=d\mathrm{sin}^2\left(\sqrt{\nu_j^k}\right)+\int_0^1\mathrm{sin}^2\left(\sqrt{\nu_j^k}x\right)dx.\) (5.18)

After performing the integral and using Eq. (5.17), we get

\(\sqrt{\nu_j^k}=\pi j+\frac{\pi k}{d\gamma_{j,k}}+\sigma_j^k,\) (5.19)

where \(\gamma_{j,k}=(\pi j)^2+\mu_k^2\), and \(|\sigma_k^j|\le A\gamma_{j,k}^{-\frac{3}{2}}\), for a constant _A\>_0.<br>
The following theorem applies to the basis property of the eigenfunctions.

**Theorem 5.1** _\[71\] The system of functions_ {_X<sub>j,k</sub>(x,y_)}_, with j_=1,2_,...;k_=1,2_,..., form a Riesz basis in_ \(L^2((0,1)\times(0,1))\).

**Lemma 5.1** _Consider_ \(\phi(x,y)\in C^4([0,1]\times[0,1])\) _that meets the following conditions_<tbc>

\(\begin{array}{ c c c c c }
\phi(x,0)=0, & \phi(0,y)=0, & \phi(1,y)=0 & \phi_y(x,1)=0, & \phi_x(0,y)=0, \\
\phi_x(1,y)=0, & \phi_{xx}(x,0)=0, & \phi_{xx}(0,y)=0, & \phi_{xx}(1,y)=0, \\
\phi_{xyx}(1,y)=0, & \int_0^1\phi(x,y)\mathrm{sin}\left(\sqrt{\nu_0^j}x\right)dx=0, & y\in[0,1], & j=1,2,\cdots
\end{array}\right.\) (5.20)

<tbc>_then the following inequalities_

\(\sum_{j=1}^\infty\sum_{k=1}^\infty\lambda_{j,k}|\phi_{j,k}|\le C\|\phi^{(iv)}\|_{C^4([0,1]\times[0,1])},\) (5.21)

\(|\phi_{j,k}|\le\frac{1}{\nu_k^j\mu_j^2}\|\phi_{xyxy}\|_{C^4([0,1]\times[0,1])}\) (5.22)

_hold, where_<tbc>

\(\phi_{j,k}:=\frac{2}{\chi_{j,k}}\int_0^1\int_0^1\phi(x,y)Y_{j,k}(x,y)dydx.\)


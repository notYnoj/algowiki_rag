\(_G\mathcal{D}_t^{(\varrho)}E(t)=4\pi^2j(2k-1)_G\mathcal{D}_t^{(\varrho)}t\genfrac(){pt}{2}{R-1-}{\sum_{\xi=2}^n\beta_\xi\big),\mathcal{T}(t)=0,\)<br>
\(\mathcal{G}(t,\tau)=4\pi^2j(2k-1)\big(C_1(t)+\lambda_{j,k}C_2(t)\big)\mathbf{V}_{j,k}(t-\tau).\)

Thus, the expression for _w(t_) becomes

\(w(t)=t\genfrac(){pt}{2}{R-1-}{\sum_{\xi=1}^n\beta_\xi\big)\)<br>
\(.\)

Consider another source term like _f(x,y,t_)=0, then the solution corresponding to _f(x,y,t_) is _u(x,y,t_)=0.

The error in \(L^2(0,T;L^2((0,1)\times(0,1)))\) between the two solutions is

\(\|\hat{u}-u\|_{L^2(0,T;L^2((0,1)\times(0,1)))}=\int_0^T\|\hat{u}-u\|_{L^2((0,1)\times(0,1))}dt\)<br>
\(\le\lambda_{j,k}\int_0^Tt\genfrac(){pt}{2}{R-1-}{\sum_{\xi=2}^n\beta_\xi\big)dt\)<br>
\(=\frac{\lambda_{j,k}}{R-\sum_{\xi=2}^n\beta_\xi}T\genfrac(){pt}{2}{R-}{\sum_{\xi=2}^n\beta_\xi\big).\)

Taking the limit as \((j,k)\rightarrow\infty\), we find

\(lim_{j,k\rightarrow\infty}\|\hat{u}-u\|_{L^2(0,T;L^2((0,1)\times(0,1)))}=\frac{T}{R-\sum_{\xi=2}^n\beta_\xi}lim_{j,k\rightarrow\infty}\lambda_{j,k}=+\infty.\) (5.67)

Therefore, based on Eq. (5.67), we guarantee that second-ISP is ill-posed.

## 5.5 Examples

This section provides examples illustrating first-ISP and second-ISP.

**Example 01:** For the specific case of first-ISP, consider the initial data<tbc>

\(\psi(x,y)=2\chi_{j,k}xsin\left(\sqrt{\nu_j^k}x\right)sin(\mu_ky),\)

<tbc>where \(\chi_{j,k}\) is given by equation (5.18). The final data is defined as<tbc>

\(g(x,y)=\frac{2T^{\beta_1}sin\left(\sqrt{\nu_j^k}x\right)sin(\mu_ky)}{\Gamma(\beta_1+2)}.\)


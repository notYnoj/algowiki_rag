## 5.4.3 Ill-posedness of second-ISP

In this subsection, we discuss the ill-posedness of second-ISP.

The following example illustrates the ill-posed nature of second-ISP. Let us consider

\(\hat{f}(x,y,t)=\lambda_{j,k}\varrho(t)\big(C_1(t)+\lambda_{j,k}C_2(t)\big)X_{j,k}(x,y),\)

where

\(C_1(t)=\sum_{r=1}^n\frac{\Gamma(1-\beta_r)\Gamma\big(R-\sum_{\xi=2}^n\beta_\xi\big)t^{\beta_1}}{\Gamma\big(R-\beta_r-\sum_{\xi=2}^n\beta_\xi\big)},R\ge 2,\)

and

\(C_2(t)=\sum_{r=1}^n\frac{\Gamma(1-\beta_r)}{P_r}t^{\beta_1+\beta_r}.\)

The initial condition given in Eq. (5.8) is taken to be zero, and let the additional condition be represented as follows

\(\int_0^1\int_0^1\hat{u}(x,y,t)dxdy=4\pi^2j(2k-1)\cdot t\big(_{R-1-}\sum_{\xi=2}^n\beta_\xi\big).\)

We know \(\lambda_{j,k}=\nu_j^k+\mu_k^2\), where \(\mu_j^2=\pi/2(2j-1)\) and \(\nu_k^j\) is given in (5.19).

For the given data, the solution (5.55) can be written as

\(\hat{u}(x,y,t)=\sum_{j=1}^\infty\sum_{k=1}^\infty w(t)\hat{f}_{j,k}(t)*\mathbf{V}_{j,k}(t)X_{j,k}(x,y),\)

where \(\hat{f}_{j,k}(t)=\langle\hat{f}(x,y,t),Y_{j,k}(x,y)\rangle\).

By applying Lemma 1.3 and Proposition 1.1, we derive the solution \(\hat{u}(x,y,t)\) in the form

\(\hat{u}(x,y,t)=\lambda_{j,k}t\big(_{R-1-}\sum_{\xi=2}^n\beta_\xi\big)X_{j,k}(x,y)).\)

Additionally, _w(t_) given in Eq. (5.57) can be written as

\(w(t)=\frac{_G\mathcal{D}_t^{(\varrho)}E(t)-\mathcal{T}(t)-\int_0^t\mathcal{G}(t,\tau)w(\tau)d\tau}{\int_0^1\int_0^1\hat{f}(x,y,t)dxdy},\)

where

\(\int_0^1\int_0^1\hat{f}(x,y,t)dxdy=4\pi^2j(2k-1)\big(C_1(t)+\lambda_{j,k}C_2(t)\big),\)


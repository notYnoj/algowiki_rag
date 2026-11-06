## 5.3.2 Ill-posedness of first-ISP

In this subsection, we see the ill-posedness of first-ISP. Reviewing some relevant results will be the first step before moving forward.

**Lemma 5.2** _\[60\] Given that_ \(\lambda_{j,k}>0\)_, the following holds:_

\(\frac{d}{dt}\mathbf{W}_{j,k}(t)=-\lambda_{j,k}\mathbf{V}_{j,k}(t).\) (5.35)

_Moreover, for T\>_0_, we have the following bound:_

\(\mathbf{Z}_{j,k}(t)=\int_0^T\mathbf{V}_{j,k}(\zeta)d\zeta\le\frac{1}{\lambda_{j,k}}.\) (5.36)

Consider the following example as a way to demonstrate the ill-posedness of first-ISP. The final and initial data are set as follows

\(\tilde{g}(x,y)=\frac{1}{\sqrt{\lambda_{j,k}}}Y_{j,k}(x,y),\text{and}\tilde{\psi}(x,y)=0,\)

where \(j,k\in\mathbb{N}\). With these choices, the source term becomes

\(\tilde{f}(x,y)=\frac{1}{\sqrt{\lambda_{j,k}}\mathbf{Z}_{j,k}(T)}X_{j,k}(x,y).\) (5.37)

Now, by taking an alternative final data and the initial data

\(g(x,y)=0,\text{and}\psi(x,y)=0,\)

then, the source term becomes _f(x,y_)=0. We then calculate the _L_<sup>2</sup>-norm between the two final data \(\tilde{g}\) and _g_

\(\|\tilde{g}-g\|_{L^2((0,1)\times(0,1))}=\left\|\frac{1}{\sqrt{\lambda_{j,k}}}X_{j,k}(x,y)\right\|_{L^2((0,1)\times(0,1))}.\)

Due to (5.19), the equality

\(\|\tilde{g}-g\|_{L^2((0,1)\times(0,1))}=\frac{1}{\sqrt{\lambda_{j,k}}}\)

is obtained, leading to the limit relation

\(lim_{j,k\rightarrow+\infty}\|\tilde{g}-g\|_{L^2((0,1)\times(0,1))}=lim_{j,k\rightarrow+\infty}\frac{1}{\sqrt{\lambda_{j,k}}}=0.\) (5.38)

To compute the error in the _L_<sup>2</sup>-norm between the two source terms \(\tilde{f}\) and _f_, we have

\(\|\tilde{f}-f\|_{L^2((0,1)\times(0,1))}=\left\|\frac{X_{j,k}(x,y)}{\sqrt{\lambda_{j,k}}\mathbf{Z}_{j,k}(T)}\right\|_{L^2((0,1)\times(0,1))}=\frac{1}{\sqrt{\lambda_{j,k}}\mathbf{Z}_{j,k}(T)}.\)

Using the estimate from Lemma 5.2, we arrive at

\(\|\tilde{f}-f\|_{L^2((0,1)\times(0,1))}\ge\sqrt{\lambda_{j,k}}.\)

This leads to

\(lim_{j,k\rightarrow+\infty}\|\tilde{f}-f\|_{L^2((0,1)\times(0,1))}>lim_{j,k\rightarrow+\infty}\sqrt{\lambda_{j,k}}=+\infty.\) (5.39)

From Eqs. (5.38) and (5.39), we conclude that first-ISP is ill-posed.


**Proof:** To construct the _w(t_), we employ an additional condition given by (5.14), which yields<tbc>

\(\int_0^1\int_0^1_G\mathcal{D}_t^{(\varrho)}u(x,y,t)dxdy=_G\mathcal{D}_t^{(\varrho)}\mathcal{E}(t).\)

<tbc>According to Eq. (5.5), this results in<tbc>

\(\int_0^1\int_0^1\big(u_{xx}(x,y,t)+u_{yy}(x,y,t)+w(t)f(x,y,t)\big)dxdy=_G\mathcal{D}_t^{(\varrho)}\mathcal{E}(t),\)

<tbc>From this, the following expression for _w(t_) is obtained

\(w(t)=\frac{_G\mathcal{D}_t^{(\varrho)}\mathcal{E}(t)-\mathcal{T}(t)-\int_0^t\mathcal{G}(t,\tau)w(\tau)d\tau}{\int_0^1\int_0^1f(x,y,t)dxdy}.\) (5.57)

Setting

\(\mathcal{T}(t)=-2\sum_{j=1}^\infty\sum_{k=1}^\infty\psi_{j,k}\mathbf{W}_{j,k}(t)\left(1-cos\left(\sqrt{\nu_j^k}\right)\right)\left(\frac{\sqrt{\nu_j^k}}{\mu_k}+\frac{2\mu_k}{\sqrt{\nu_j^k}}\right),\) (5.58)

\(\int_0^1\int_0^1f(x,y,t)dxdy=-2\sum_{j=1}^\infty\sum_{k=1}^\infty f_{j,k}(t)\left(1-cos\left(\sqrt{\nu_j^k}\right)\right)\left(\frac{\sqrt{\nu_j^k}}{\mu_k}+\frac{2\mu_k}{\sqrt{\nu_j^k}}\right),\) (5.59)

\(\mathcal{G}(t,\tau)=-2\sum_{j=1}^\infty\sum_{k=1}^\infty f_{j,k}(\tau)\mathbf{V}_{j,k}(t-\tau)\left(1-cos\left(\sqrt{\nu_j^k}\right)\right)\left(\frac{\sqrt{\nu_j^k}}{\mu_k}+\frac{2\mu_k}{\sqrt{\nu_j^k}}\right).\) (5.60)

Based on Lemma 4.1 (refer to \[13\], Eq. (42) on page 10) and Lemma 5.3, there are positive constants _Q_<sub>1</sub>_\>_0 and _Q_<sub>2</sub>_\>_0 such that<tbc>

\(\|\mathcal{T}(t)\|_{C([0,T])}\le Q_1,\text{and}\|\mathcal{G}(t,\tau)\|_{C([0,T]\times[0,T])}\le Q_2.\) (5.61)

<tbc>In order to define the mapping \(\mathcal{I}:C([0,T])\rightarrow C([0,T])\), let’s write it as follows

\(\mathcal{I}(w(t)):=\frac{_G\mathcal{D}_t^{(\varrho)}\mathcal{E}(t)-\mathcal{T}(t)-\int_0^t\mathcal{G}(t,\tau)w(\tau)d\tau}{\int_0^1\int_0^1f(x,y,t)dxdy}.\) (5.62)

As a result of the uniform convergence of

\(\|\mathcal{T}(t)\|_{C([0,T])}\text{and}\|\mathcal{G}(t,\zeta)\|_{C([0,T]\times[0,T])},\)

the mapping I(_w(t_)) is well-defined.

Now, we demonstrate that the mapping I(_w(t_)) is a contraction. Consider

\(|\mathcal{I}(w_1(t))-\mathcal{I}(w_2(t))|=\left(\int_0^1\int_0^1f(x,y,t)dxdy\right)^{-1}\int_0^t|\mathcal{G}(t,\tau)||w_1(\tau)-w_2(\tau)|d\tau.\)


be a smooth function (for the sake of simplicity, just assume differentiability up to the correct order, as above), and let _Z_<sub>1</sub>_,...,Z<sub>m</sub>_ be i.i.d. standard normal random variables. Now, for \(k\ge 1\), let<tbc>

\(\theta_k=\sum_{1\le i_1,\dots,i_k\le m}\left(\mathbb{E}\left(\frac{\partial^kG}{\partial x_{i_1}\dots x_{i_k}}(Z_1,\dots,Z_m)\right)\right)^2,\)

<tbc>and let<tbc>

\(\eta_k=\sum_{1\le i_1,\dots,i_k\le m}\left(\mathbb{E}\left(\frac{\partial^kG}{\partial x_{i_1}\dots x_{i_k}}(Z_1,\dots,Z_m)\right)^2\right).\)

<tbc>Let further \((X_{i,j})_{i\in\{1,\dots,m\},j\in\{1,\dots,n\}}\) be independent Rademacher random variables and let<tbc>

\(S(X_{1,1},\dots,X_{m,n}):=G\left(\frac{X_{1,1}+\cdots+X_{1,n}}{\sqrt{n}},\dots,\frac{X_{m,1}+\cdots+X_{m,n}}{\sqrt{n}}\right).\)

<tbc>Then for all \(k\ge 1\),<tbc>

\(J_k(n)-\rightarrow_{n\rightarrow+\infty}\eta_k\text{and}K_k(n)-\rightarrow_{n\rightarrow+\infty}\theta_k.\)

<tbc>Moreover, for all \(k\ge 1\),

\(\frac{\theta_{k+1}}{(k+1)!}\le(-1)^k\left(\mathrm{Var}G(Z_1,\dots,Z_m)-\eta_1+\frac{\eta_2}{2}-\cdots+(-1)^k\frac{\eta_k}{k!}\right)\le\frac{\eta_{k+1}}{(k+1)!}.\)<br>
\(\frac{\theta_{k+1}}{(k+1)!}\le\mathrm{Var}G(Z_1,\dots,Z_m)-\theta_1-\frac{\theta_2}{2}-\cdots-\frac{\theta_k}{k!}\le\frac{\eta_{k+1}}{(k+1)!}.\)

**Remark 3.4.** _It is well known that if Z_<sub>1</sub>_,Z_<sub>2</sub>_,...,Z<sub>m</sub> are iid standard normal random variables, and if_ \(\|Z\|_2^2:=\sum_{k=1}^mZ_k^2\)_, then_ \((Z_1/\|Z\|_2,\dots,Z_m/\|Z\|_2)\) _is uniformly distributed on the m_-1_-dimensional unit sphere. Therefore, the above multivariate Gaussian case allows to recover and extend various variance bounds and covariance representations on the high-dimensional sphere._

## 3.2 The infinitely divisible case

Let _Y_ be an infinitely divisible real-valued random variable, and \(G:\mathbb{R}\rightarrow\mathbb{R}\) be a smooth function such that its derivatives of all order are well defined and \(\mathbb{E}\left(G^{(k)}(Y)\right)^2<+\infty\) for all \(k\ge 0\). We are interested in the decomposition of the variance of _G(Y_).

We let \((Y_t)_{t\ge 1}\) be the corresponding Lévy process (i.e. _Y_<sub>1</sub> has the same distribution as _Y_ ), we denote by \((b,\sigma,\nu)\) its generator (from the Lévy-Khintchine representation), and let \((Y'_t)_{t\ge 0},(Y''_t)_{t\ge 0}\) be independent copies of \((Y_t)_{t\ge 0}\). For \(1\le\ell,m\), let

\(X_{\ell,m}=Y_{\ell/m}-Y_{(\ell-1)/m},\)<br>
\(X'_{\ell,m}=Y'_{\ell/m}-Y'_{(\ell-1)/m},\)

and let

\(S_n=G(X_{1,n}+\cdots+X_{n,n}).\)

We now study, for any fixed \(\alpha\in(0,1)\), the limit when _m_ goes to infinity of \(nB_{\lfloor\alpha n\rfloor}\) (the _B<sub>k</sub>_’s of _S<sub>n</sub>_) where _n_=2_<sup>m</sup>_+1, which allows us to recover in another way the representation of the variance from \[16\].

**Theorem 3.5.** _Let_ \(\alpha\in(0,1)\)_. Then with the notations above,_

\(2^mB_{\lfloor\alpha(2^m)\rfloor+1}-\rightarrow_{m\rightarrow\infty}\mathbb{E}\left(\sigma G'(Y_\alpha+Y''_{1-\alpha})G'(Y'_\alpha+Y''_{1-\alpha})+\int_\mathbb{R}\Delta_uG(Y_\alpha+Y''_{1-\alpha})\Delta_uG(Y'_\alpha+Y''_{1-\alpha})\mathrm{d}\nu\right),\)

_where_ \(\Delta_uG(x)=G(x+u)-G(x)\).


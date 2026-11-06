<tbc>Here, we used \(\lambda_i^\theta(t)\ge\underline{\mu}\) (Lemma 3.7) and \(\|U^\theta\|_2\le 1\). The constant _c_<sub>1_,k_</sub> depends on _k_ because the initial guess _z_<sub>0</sub> depends on _k_. Since \(k\in\{1,\dots,n-1\}\), define \(c_1:=max_{1\le j\le n-1}c_{1,j}\). Then

(3.30) \(T_\mathrm{c}^\theta(t)\le c_1q_k^{2\ell} t^2.\)

We next bound \(T_\mathrm{n}^\theta(t)\). Differentiating \(p_\ell^{(t)}\) and using \(\xi_j(t)\ge\underline{\mu}\) gives, for \(\lambda\in[\underline{\mu},\overline{\mu_k}]\),

(3.31) \(\left|\partial_\lambda p_\ell^{(t)}(\lambda)\right|=\left|-\sum_{j=1}^\ell\frac{1}{\xi_j(t)}\prod_{h=1h\neq j}^\ell(1-\frac{\lambda}{\xi_h(t)})\right|\le\frac{\ell}{\underline{\mu}}q_k^{\ell-1}.\)

Write \(f_{\ell,t}^\theta(\lambda)=g^\theta(\lambda)p_\ell^{(t)}(\lambda)^2\) with \(g^\theta(\lambda)=\lambda^{-1}(1-\lambda/\theta)^2\). For \(\lambda\in[\underline{\mu},\overline{\mu_k}]\),

\(|g^\theta(\lambda)|=\frac{1}{\lambda}(1-\frac{\lambda}{\theta})^2\le\frac{1}{\underline{\mu}}(1+\frac{\lambda_1+t^*\|E\|_2}{\lambda_n})^2=:c_2,|\partial_\lambda g^\theta(\lambda)|=\left|-\frac{1}{\lambda^2}+\frac{1}{\theta^2}\right|\le\frac{1}{\underline{\mu}^2}+\frac{1}{\lambda_n^2}=:c'_2.\)

Combining these estimates with (3.29) and (3.31) yields _c_<sub>2</sub>_,c_<sub>3</sub>_,c_<sub>4</sub>_\>_0, independent of \(\ell\) and of \(\theta\in\Theta_\delta\), such that the following bounds hold for every \(\lambda\in[\underline{\mu},\overline{\mu_k}]\):

(3.32) \(|f_{\ell,t}^\theta(\lambda)|\le c_2q_k^{2\ell},|\partial_\lambda f_{\ell,t}^\theta(\lambda)|\le c_3q_k^{2\ell}+c_4\ell q_k^{2\ell-1}.\)

For each _i=k_+1_,...,n_

\(\widetilde{\beta}_i^\theta(t)^2f_{\ell,t}^\theta(\lambda_i^\theta(t))=\widetilde{\zeta}_i(t)^2f_{\ell,t}^\theta(\widehat{\lambda}_i(t))+\left(\widetilde{\beta}_i^\theta(t)^2-\widetilde{\zeta}_i(t)^2\right)f_{\ell,t}^\theta(\lambda_i^\theta(t))+\widetilde{\zeta}_i(t)^2\left(f_{\ell,t}^\theta(\lambda_i^\theta(t))-f_{\ell,t}^\theta(\widehat{\lambda}_i(t))\right).\text{(3.33)}\)

Lemmas 3.5 and 3.6 provide constants \(c_{\beta,k,i},c_{\lambda,k,i}\ge 0\) (independent of \(\theta\)) such that

\(\left|\widetilde{\beta}_i^\theta(t)^2-\widetilde{\zeta}_i(t)^2\right|\le c_{\beta,k,i}t^2,\left|\lambda_i^\theta(t)-\widehat{\lambda}_i(t)\right|\le c_{\lambda,k,i}t^2,i=k+1,\dots,n.\)

Setting \(c_\beta:=max_{1\le j\le n-1,j+1\le l\le n}c_{\beta,j,l}\) and \(c_\lambda:=max_{1\le j\le n-1,j+1\le l\le n}c_{\lambda,j,l}\), yields

(3.34) \(\left|\widetilde{\beta}_i^\theta(t)^2-\widetilde{\zeta}_i(t)^2\right|\le c_\beta t^2,\left|\lambda_i^\theta(t)-\widehat{\lambda}_i(t)\right|\le c_\lambda t^2,i=k+1,\dots,n.\)

Using (3.32), the sum of the second terms in (3.33) satisfies

(3.35) \(\sum_{i=k+1}^n\left|\widetilde{\beta}_i^\theta(t)^2-\widetilde{\zeta}_i(t)^2\right|\left|f_{\ell,t}^\theta(\lambda_i^\theta(t))\right|\le nc_\beta c_2q_k^{2\ell} t^2.\)

Set \(c_\zeta:=max_{1\le j\le n-1}max_{0\le s\le t^*}\sum_{i=j+1}^n\widetilde{\zeta}_i(s)^2\). (3.32) and the mean value theorem yield

\(\sum_{i=k+1}^n\widetilde{\zeta}_i(t)^2\left|f_{\ell,t}^\theta(\lambda_i^\theta(t))-f_{\ell,t}^\theta(\widehat{\lambda}_i(t))\right|\le c_\zeta max_{k+1\le i\le n}\left|f_{\ell,t}^\theta(\lambda_i^\theta(t))-f_{\ell,t}^\theta(\widehat{\lambda}_i(t))\right|\le c_\zeta sup_{\lambda\in[\underline{\mu},\overline{\mu_k}]}\left|\partial_\lambda f_{\ell,t}^\theta(\lambda)\right|max_{k+1\le i\le n}\left|\lambda_i^\theta(t)-\widehat{\lambda}_i(t)\right|\le c_\zeta c_\lambda\left(c_3q_k^{2\ell}+c_4\ell q_k^{2\ell-1}\right)t^2.\text{(3.36)}\)

Summing (3.33) over _i=k_+1_,...,n_, and combining (3.35)-(3.36), gives

\(T_\mathrm{n}^\theta(t)\le\sum_{i=k+1}^n\widetilde{\zeta}_i(t)^2f_{\ell,t}^\theta(\widehat{\lambda}_i(t))+\left(c_5q_k^{2\ell}+c_6\ell q_k^{2\ell-1}\right)t^2,\)


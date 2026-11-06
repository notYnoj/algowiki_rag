<tbc>The posterior density is \((b_i^{a_i}/\Gamma(a_i))\theta^{-a_i-1}e^{-b_i/\theta}\) on \(\theta>0\). Then

\(\mu_i(t)=\frac{b_i}{a_i-1},v_i(t)=\frac{b_i^2}{(a_i-1)^2(a_i-2)},F_{i,t}(q)=\Gamma(a_i,b_i/q)(q>0),\)

and _q_<sup>∗</sup>(_t_) solves

\(\sum_{i=1}^I\gamma(a_i,b_i/q)=k.\)

We next compute the expected post-round-_t_ posterior variance. Let \(W:=\kappa_i\sum_{\ell=1}^{\Delta_i}Y_{i,\ell}^\mathrm{new}\). Each gamma observation contributes likelihood proportional to \(\theta^{-\kappa_i}e^{-\kappa_iy/\theta}\), so

\(\theta_i|\mathcal{H}_t,W\sim\mathrm{InvGamma}(a_i+\kappa_i\Delta_i,b_i+W),\mathbb{V}(\theta_i|\mathcal{H}_t,W)=\frac{(b_i+W)^2}{(a_i+\kappa_i\Delta_i-1)^2(a_i+\kappa_i\Delta_i-2)}.\)

Conditional on \(\theta_i\), \(W\sim\mathrm{Gamma}(\kappa_i\Delta_i,\theta_i)\) (shape \(\kappa_i\Delta_i\), scale \(\theta_i\)), so \(\mathbb{E}_t[W]=\kappa_i\Delta_ib_i/(a_i-1)\) and \(\mathbb{E}_t[W^2]=\kappa_i\Delta_i(\kappa_i\Delta_i+1)b_i^2/[(a_i-1)(a_i-2)]\), giving

\(\mathbb{E}_t[(b_i+W)^2]=\frac{b_i^2(a_i+\kappa_i\Delta_i-1)(a_i+\kappa_i\Delta_i-2)}{(a_i-1)(a_i-2)}\)

and therefore

\(\bar{v}_i(t,\Delta_i)=\frac{b_i^2}{(a_i-1)(a_i-2)(a_i+\kappa_i\Delta_i-1)}=v_i(t)\frac{a_i-1}{a_i+\kappa_i\Delta_i-1},\)<br> \(c_i(t,\Delta_i)^2=\frac{a_i-1}{a_i+\kappa_i\Delta_i-1}=\frac{1}{1+(\kappa_i/(a_i-1))\Delta_i}.\)

This has the form (10), so GBB is exact.

Finally, for _z\>_0,

\(\mathbb{E}_t[(z-\theta_i)^+]=z\Gamma(a_i,b_i/z)-\frac{b_i}{a_i-1}\Gamma(a_i-1,b_i/z).\)

Combined with \(c_i(t,\Delta_i)\) and (7), this gives the closed form for \(\ell_{i,t}(\Delta_i)\).

**B.5. Lognormal observations with known log-variance**

Suppose \(Y_{i,n}|\theta_i\sim\mathrm{Lognormal}(\mathrm{log}\theta_i-\sigma_i^2/2\), \(\sigma_i^2)\) with \(\sigma_i^2\) known, parameterized so \(\mathbb{E}[Y_{i,n}|\theta_i]=\theta_i\). Let \(\eta_i:=\mathrm{log}\theta_i\) and \(X_{i,n}:=\mathrm{log}Y_{i,n}+\sigma_i^2/2\), so \(X_{i,n}=\eta_i+\varepsilon_{i,n}\) with \(\varepsilon_{i,n}\sim N(0,\sigma_i^2)\). With prior \(\eta_i\sim N(m_i(0),s_i^2(0))\), the transformed problem in \(\eta_i\) is Gaussian-Gaussian conjugate:

\(\eta_i|\mathcal{H}_t\sim N(m_i(t),s_i^2(t)),s_i^2(t)=\left(\frac{1}{s_i^2(0)}+\frac{N_i(t)}{\sigma_i^2}\right)^{-1},m_i(t)=s_i^2(t)\left(\frac{m_i(0)}{s_i^2(0)}+\frac{1}{\sigma_i^2}\sum_{n=1}^{N_i(t)}X_{i,n}\right).\)

Hence \(\theta_i=e^{\eta_i}\) has lognormal posterior with

\(\mu_i(t)=\mathrm{exp}\left(m_i+\frac{s_i^2}{2}\right),v_i(t)=(e^{s_i^2}-1)e^{2m_i+s_i^2},F_{i,t}(q)=\Phi\left(\frac{\mathrm{log}q-m_i}{s_i}\right)(q>0),\)

and _q_<sup>∗</sup>(_t_) solves

\(\sum_{i=1}^I\left[1-\Phi\left(\frac{\mathrm{log}q-m_i}{s_i}\right)\right]=k.\)


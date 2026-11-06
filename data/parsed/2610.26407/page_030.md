This has the form (10), so GBB is exact.

Finally, for 0_\<z\<r_,

\(\mathbb{E}_t[(z-\theta_i)^+]=zI_{z/r}(a_i,b_i)-r\frac{a_i}{n_i}I_{z/r}(a_i+1,b_i),\)

extending to \(z\le 0\) and \(z\ge r\) with values 0 and \(z-\mu_i(t)\) respectively. Combined with \(c_i(t,\Delta_i)\) and (7), this yields the closed form for \(\ell_{i,t}(\Delta_i)\).

**B.3. Poisson with gamma posterior**

Suppose \(Y_{i,n}|\theta_i\sim\mathrm{Pois}(\theta_i)\) with prior \(\theta_i\sim\mathrm{Gamma}(a_i(0),b_i(0))\), where _b<sub>i</sub>_(0) is the rate. After _N<sub>i</sub>(t_) observations,

\(\theta_i|\mathcal{H}_t\sim\mathrm{Gamma}(a_i(t),b_i(t)),a_i(t):=a_i(0)+\sum_{n=1}^{N_i(t)}Y_{i,n},b_i(t):=b_i(0)+N_i(t).\)

The posterior density is \((b_i^{a_i}/\Gamma(a_i))\theta^{a_i-1}e^{-b_i\theta}\) on \(\theta>0\). Then

\(\mu_i(t)=\frac{a_i}{b_i},v_i(t)=\frac{a_i}{b_i^2},F_{i,t}(q)=\gamma(a_i,b_iq)(q>0),\)

and _q_<sup>∗</sup>(_t_) solves

\(\sum_{i=1}^I\Gamma(a_i,b_iq)=k.\)

We next compute the expected post-round-_t_ posterior variance. The future total \(X:=\sum_{\ell=1}^{\Delta_i}Y_{i,\ell}^\mathrm{new}\) satisfies \(X|\theta_i\sim\mathrm{Pois}(\Delta_i\theta_i)\), so

\(\theta_i|\mathcal{H}_t,X\sim\mathrm{Gamma}(a_i+X,b_i+\Delta_i),\mathbb{V}(\theta_i|\mathcal{H}_t,X)=\frac{a_i+X}{(b_i+\Delta_i)^2}.\)

Using \(\mathbb{E}_t[X]=\Delta_ia_i/b_i\),

\(\bar{v}_i(t,\Delta_i)=\frac{a_i}{b_i(b_i+\Delta_i)}=v_i(t)\frac{b_i}{b_i+\Delta_i},c_i(t,\Delta_i)^2=\frac{b_i}{b_i+\Delta_i}=\frac{1}{1+\Delta_i/b_i}.\)

This has the form (10), so GBB is exact.

Finally, for _z\>_0,

\(\mathbb{E}_t[(z-\theta_i)^+]=z\gamma(a_i,b_iz)-\frac{a_i}{b_i}\gamma(a_i+1,b_iz).\)

Combined with \(c_i(t,\Delta_i)\) and (7), this gives the closed form for \(\ell_{i,t}(\Delta_i)\).

**B.4. Gamma observations with known shape and inverse-gamma posterior**

Suppose \(Y_{i,n}|\theta_i\sim\mathrm{Gamma}(\kappa_i,\theta_i/\kappa_i)\) (shape \(\kappa_i\), scale \(\theta_i/\kappa_i\)) with \(\kappa_i>0\) known (the case \(\kappa_i=1\) is the exponential model \(Y_{i,n}|\theta_i\sim\mathrm{Exp}(1/\theta_i)\)). The conjugate prior is \(\theta_i\sim\mathrm{InvGamma}(a_i(0),b_i(0))\) with _a<sub>i</sub>_(0)_\>_2 and _b<sub>i</sub>_(0)_\>_0, ensuring _v<sub>i</sub>(t_) is finite at every round. After _N<sub>i</sub>(t_) observations,

\(\theta_i|\mathcal{H}_t\sim\mathrm{InvGamma}(a_i(t),b_i(t)),a_i(t):=a_i(0)+\kappa_iN_i(t),b_i(t):=b_i(0)+\kappa_i\sum_{n=1}^{N_i(t)}Y_{i,n}.\)


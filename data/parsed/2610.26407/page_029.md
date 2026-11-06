## B.1. Gaussian observations with known variance

Suppose \(Y_{i,n}|\theta_i\sim N(\theta_i,\sigma_i^2)\) with \(\sigma_i^2\) known, and prior \(\theta_i\sim N(m_i(0),s_i^2(0))\). At the start of round _t_,<tbc>

\(\theta_i|\mathcal{H}_t\sim N(m_i(t),s_i^2(t)),s_i^2(t)=\left(\frac{1}{s_i^2(0)}+\frac{N_i(t)}{\sigma_i^2}\right)^{-1},m_i(t)=s_i^2(t)\left(\frac{m_i(0)}{s_i^2(0)}+\frac{1}{\sigma_i^2}\sum_{n=1}^{N_i(t)}Y_{i,n}\right).\)

<tbc>Then \(\mu_i(t)=m_i\), \(v_i(t)=s_i^2\), \(F_{i,t}(q)=\Phi\left(\frac{q-m_i}{s_i}\right)\) and _q_<sup>∗</sup>(_t_) solves<tbc>

\(\sum_{i=1}^I\left[1-\Phi\left(\frac{q-m_i}{s_i}\right)\right]=k.\)

<tbc>We next compute the expected post-round-_t_ posterior variance. After \(\Delta_i\) further observations, the posterior variance of \(\theta_i\) is deterministic: it depends on \(\Delta_i\) but not on the realized values. This deterministic update is a special property of the Gaussian-Gaussian pair that does not hold for the other families. Hence

\(\bar{v}_i(t,\Delta_i)=\left(\frac{1}{s_i^2}+\frac{\Delta_i}{\sigma_i^2}\right)^{-1},c_i(t,\Delta_i)^2=\frac{1}{1+s_i^2\Delta_i/\sigma_i^2}.\)

This has the form (10), so GBB is exact.

Finally, for any \(z\in\mathbb{R}\),

\(\mathbb{E}_t[(z-\theta_i)^+]=(z-m_i)\Phi\left(\frac{z-m_i}{s_i}\right)+s_i\phi\left(\frac{z-m_i}{s_i}\right).\)

Combined with \(c_i(t,\Delta_i)\) and (7), this yields the closed form for \(\ell_{i,t}(\Delta_i)\).

## B.2. Binomial with beta posterior

Suppose _Y<sub>i,n</sub>|p<sub>i</sub>_∼Bin(_r,p<sub>i</sub>_) with \(r\in\mathbb{Z}_+\) known, mean parameter \(\theta_i=rp_i\), and prior _p<sub>i</sub>_∼Beta(_a<sub>i</sub>_(0)_,b<sub>i</sub>_(0)). Let \(S_i(t):=\sum_{n=1}^{N_i(t)}Y_{i,n}\). At the start of round _t_,<tbc>

\(p_i|\mathcal{H}_t\sim\text{Beta}(a_i(t),b_i(t)),a_i(t):=a_i(0)+S_i(t),b_i(t):=b_i(0)+rN_i(t)-S_i(t).\)

<tbc>Set _n<sub>i</sub>_:=_a<sub>i</sub>+b<sub>i</sub>_. Then<tbc>

\(\mu_i(t)=r\frac{a_i}{n_i},v_i(t)=r^2\frac{a_ib_i}{n_i^2(n_i+1)},F_{i,t}(q)=I_{q/r}(a_i,b_i)(0<q<r),\)

<tbc>and _q_<sup>∗</sup>(_t_) solves<tbc>

\(\sum_{i=1}^I\left[1-I_{q/r}(a_i,b_i)\right]=k.\)

<tbc>We next compute the expected post-round-_t_ posterior variance. Allocating \(\Delta_i\) further binomial observations is equivalent to \(r\Delta_i\) further Bernoulli trials. Conditional on the future number of successes _X_,<tbc>

\(p_i|\mathcal{H}_t,X\sim\text{Beta}(a_i+X,b_i+r\Delta_i-X),\)

<tbc>so taking expectation of \(\mathbb{V}(\theta_i|\mathcal{H}_t,X)\) over _X_ gives

\(\bar{v}_i(t,\Delta_i)=r^2\frac{a_ib_i}{n_i(n_i+1)(n_i+r\Delta_i)}=v_i(t)\frac{n_i}{n_i+r\Delta_i},c_i(t,\Delta_i)^2=\frac{n_i}{n_i+r\Delta_i}=\frac{1}{1+(r/n_i)\Delta_i}.\)


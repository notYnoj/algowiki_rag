<tbc>PROPOSITION 3. _Fix round t and write_ \(\mu_i:=\mu_i(t)\)_. For_ (ii)-(iv)_, write a<sub>i</sub>_:=_a<sub>i</sub>(t_) _and b<sub>i</sub>_:=_b<sub>i</sub>(t)._

(i) **_Gaussian, known variance_** \(\sigma_i^2\)**.** _Posterior_ \(N(m_i,s_i^2)\), \(\mu_i=m_i\):<tbc>

<tbc>\(c_i(t,\Delta_i)^2=\frac{1}{1+(s_i^2/\sigma_i^2)\Delta_i}\mathbb{E}_t[(z-\theta_i)^+]=(z-m_i)\Phi\big(\frac{z-m_i}{s_i}\big)+s_i\phi\big(\frac{z-m_i}{s_i}\big)\)<tbc>

<tbc>_where_ \(\phi\) _is the standard normal density._<tbc>

(ii) **_Binomial/Bernoulli._** _Observations are binomial with success probability p<sub>i</sub> and number of trials_ \(r\in\mathbb{Z}_+\)_. Posterior p<sub>i</sub>_∼Beta(_a<sub>i</sub>,b<sub>i</sub>),_ \(\mu_i=ra_i/n_i\) _where n<sub>i</sub>=a<sub>i</sub>+b<sub>i</sub>:_<tbc>

<tbc>\(c_i(t,\Delta_i)^2=\frac{1}{1+(r/n_i)\Delta_i}\mathbb{E}_t[(z-\theta_i)^+]=\left\{\begin{array}{ c c }
0, & z\le 0, \\
zI_{z/r}(a_i,b_i)-\mu_iI_{z/r}(a_i+1,b_i), & 0<z<r, \\
z-\mu_i, & z\ge r
\end{array}\right.\)<tbc>

<tbc>_where I<sub>z</sub>(a,b_) _is the regularized incomplete beta function._<tbc>

(iii) **_Poisson._** _Posterior_ Gamma(_a<sub>i</sub>,b<sub>i</sub>_) _with shape a<sub>i</sub> and rate b<sub>i</sub>,_ \(\mu_i=a_i/b_i\):<tbc>

<tbc>\(c_i(t,\Delta_i)^2=\frac{1}{1+\Delta_i/b_i}\mathbb{E}_t[(z-\theta_i)^+]=\left\{\begin{array}{ c c }
0, & z\le 0, \\
z\gamma(a_i,b_iz)-\mu_i\gamma(a_i+1,b_iz), & z>0
\end{array}\right.\)<tbc>

<tbc>_where_ \(\gamma(a,x)\) _is the lower regularized incomplete gamma function._<tbc>

(iv) **_Gamma, known shape_** \(\kappa_i\)**.** _Posterior_ InvGamma(_a<sub>i</sub>,b<sub>i</sub>),_ \(\mu_i=b_i/(a_i-1)\):<tbc>

<tbc>\(c_i(t,\Delta_i)^2=\frac{1}{1+(\kappa_i/(a_i-1))\Delta_i}\mathbb{E}_t[(z-\theta_i)^+]=\left\{\begin{array}{ c c }
0, & z\le 0, \\
z\Gamma(a_i,b_i/z)-\mu_i\Gamma(a_i-1,b_i/z), & z>0
\end{array}\right.\)<tbc>

<tbc>_where_ \(\Gamma(a,x)\) _is the upper regularized incomplete gamma function._<tbc>

(v) **_Lognormal._** _Posterior lognormal with log-mean m<sub>i</sub>, log-variance_ \(s_i^2\), \(\mu_i=e^{m_i+s_i^2/2}\)_, and_ \(s_i^2(\Delta_i):=(1/s_i^2+\Delta_i/\sigma_i^2)^{-1}\):<tbc>

<tbc>\(c_i(t,\Delta_i)^2=\frac{1-e^{-s_i^2(\Delta_i)}}{1-e^{-s_i^2}}\mathbb{E}_t[(z-\theta_i)^+]=\left\{\begin{array}{ c c }
0, & z\le 0, \\
z\Phi\big(\frac{logz-m_i}{s_i}\big)-\mu_i\Phi\big(\frac{logz-m_i-s_i^2}{s_i}\big), & z>0
\end{array}\right..\)<tbc>

<tbc>_For_ (i)-(iv), \(c_i(t,\Delta_i)^2\) _has the form_ (10)_, so GBB solves_ (8) _exactly by Proposition 2(ii). For_ (v), \(c_i(t,\Delta_i)^2\) _does not have this form in general._

## 4. Theoretical guarantees

The guarantees in §3 concern the optimization of the surrogate objective (8), not the performance of TEAk in reducing EOC. In this section, we give asymptotic performance guarantees for TEAk. We begin by showing that TEAk is consistent (EOC(H_<sub>t</sub>_) converges to zero) and then make additional distributional assumptions to obtain a much stronger result. In particular, with threshold _q_<sup>†</sup>(_t_), we show that the asymptotic exponential rate at which EOC(H_<sub>t</sub>_) converges to zero, referred to as the posterior convergence rate, is at least half of the best rate achievable by any sequential sampling rule.


_M(c_)=_cD(c_) by the Einstein relation. We parameterize both functions with orthogonal polynomials,

\(\mu_h(c)=\mathrm{ln}\frac{c}{1-c}+\sum_{k=1}^{12}a_kP_k(c),D(c)=\mathrm{exp}\big(\sum_{k=0}^9b_kP_k(c)\big),\) (22)

where _P<sub>k</sub>_ is the shifted Legendre polynomial of degree _k_ normalized in _L_<sup>2</sup>([0,1]) , the logarithmic term retains the ideal entropy of mixing, the exponential keeps the diffusivity positive, and \(\theta=(a,b)\) collects the coefficients. Following Zhao et al. [79], we assume the coefficients are distributed as

\(a_k,b_k\sim\mathcal{N}\big(0,\frac{s^2}{1+k(k+1)}\big),\) (23)

where the variance decays with the polynomial degree, so that the prior damps oscillations that the data cannot resolve, and the scale _s_ is set by empirical Bayes (Section 7.2). We then solve for the maximum a posteriori (MAP) estimate

\(\theta^*=\mathrm{argmin}_\theta\frac{1}{2\sigma^2}\sum_{i=1}^N\big\|c(t_i;\theta)-\hat{c}(t_i)\big\|^2-\mathrm{ln}p(\theta),\) (24)

where \(\hat{c}(t_i)\) is the measured frame at time _t<sub>i</sub>_, \(\sigma\) is the standard deviation of the measurement noise, and \(p(\theta)\) is the prior of Eq. (23). We use multiple shooting, so that each prediction \(c(t_i;\theta)\) is integrated from the previous measured frame \(\hat{c}(t_{i-1})\) rather than from the start of the movie, which keeps each solve short and greatly accelerates the optimization [93]. As in Cohen et al. [25], we treat each measured frame as an exact initial state for its window, so the likelihood of Eq. (24) accounts for the noise in the predicted frame but not in the initial one. We solve Eq. (24) with the Newton trust region algorithm and then sample the posterior with the No-U-Turn sampler (NUTS) [99] implemented in `blackjax` [53].


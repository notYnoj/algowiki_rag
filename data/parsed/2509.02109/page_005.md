<tbc>for the parameters:

\(w_k^{(t+1)}=\frac{1}{n}\sum_{i=1}^n\gamma_{ik}(\theta_t),m_k^{(t+1)}=\frac{\sum_{i=1}^n\gamma_{ik}(\theta_t)x_i}{\sum_{j=1}^n\gamma_{jk}(\theta_t)},\Sigma_k^{(t+1)}=\frac{\sum_{i=1}^n\gamma_{ik}(\theta_t)(x_i-m_k^{(t+1)})(x_i-m_k^{(t+1)})^\top}{\sum_{j=1}^n\gamma_{jk}(\theta_t)}.\) (4)

It is a standard result (see \[Moo96\]) that the log-likelihood \(\ell_\theta(X)=\sum_{i=1}^nlog\left(\sum_{k=1}^Kw_kg_{m_k,\Sigma_k}(x_i)\right)\) increases with respect to \(\theta=(w,(m_k),(\Sigma_k))\) with each EM iteration. In practice, we shall see that it is sometimes preferable to tweak the standard EM algorithm by not updating the weights _w_ and keeping the weights _w_<sub>0</sub> of the initialisation \(\theta_0\) (we refer to this as fixing the weights). We summarise the two algorithms in Algorithms 1 and 2, with the difference highlighted in red.


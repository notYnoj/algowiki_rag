<tbc>mean and scaling by their standard deviation. Put together, these conditions say that we replace the random future posterior with a deterministic, "shrunken" copy of the current prior, as it has the same mean as the prior, keeps the same shape, and changes only through a contraction around its mean by the expected amount of uncertainty that the proposed samples will remove. Figure 1 gives an example.

Formally, we replace each \(\theta_i\) in (4) by the random variable \(\widetilde{\theta}_i(\Delta_i)\) that satisfies

(i) \(\frac{\widetilde{\theta}_i(\Delta_i)-\mathbb{E}_t[\widetilde{\theta}_i(\Delta_i)]}{\sqrt{\mathbb{V}_t(\widetilde{\theta}_i(\Delta_i))}}=^d\frac{\theta_i-\mu_i(t)}{\sqrt{v_i(t)}},\)<tbc>

(ii) \(\mathbb{E}_t[\widetilde{\theta}_i(\Delta_i)]=\mathbb{E}[\mu_i(t+1)|\Delta,\mathcal{H}_t]=\mu_i(t),\)<tbc>

(iii) \(\mathbb{V}_t(\widetilde{\theta}_i(\Delta_i))=\mathbb{E}[\mathbb{V}(\theta_i|\mathcal{H}_{t+1})|\Delta,\mathcal{H}_t]=:\bar{v}_i(t,\Delta_i).\)

<tbc>For a given H_<sub>t</sub>_, this distribution is unique and is given by

\(\widetilde{\theta}_i(\Delta_i)=\mu_i(t)+c_i(t,\Delta_i)(\theta_i-\mu_i(t)),c_i(t,\Delta_i):=\sqrt{\frac{\bar{v}_i(t,\Delta_i)}{v_i(t)}}.\) (5)

We then define the surrogate loss induced by the allocation \(\Delta\) as

\(\mathcal{L}_t(\Delta):=\mathbb{E}_t\left[\sum_{i\in S_k(\mu(t))}(q(t)-\widetilde{\theta}_i(\Delta_i))^++\sum_{i\notin S_k(\mu(t))}(\widetilde{\theta}_i(\Delta_i)-q(t))^+\right]\)<br>
\(=\sum_{i=1}^I\mathbb{E}_t[(q(t)-\widetilde{\theta}_i(\Delta_i))^+]+\sum_{i\notin S_k(\mu(t))}(\mu_i(t)-q(t)),\) (6)

where the second equality follows from (_x-q_)<sup>+</sup>=(_x-q_)+(_q-x_)<sup>+</sup>. The second sum is constant with respect to \(\Delta\). For the first sum we have<tbc>

\(\ell_{i,t}(\Delta_i):=\mathbb{E}_t[(q(t)-\widetilde{\theta}_i(\Delta_i))^+]=c_i(t,\Delta_i)\mathbb{E}_t[(z_i(t,\Delta_i)-\theta_i)^+],\) (7)

Gaussian (batch Bt = 10) Beta (batch Bt = 10) 1.2 A
B
C A
B
C A = 5
A = 4
A = 1
A = 6
A = 4
A = 0
4.0 1.0 0.8 2.0 q* (t) q* (t) 0.6 value 0.0 value 0.4 -2.0 0.2 0.0 current prior post-allocation (current) loss contribution (post-allocation)

**Figure 1** Structure of the surrogate loss \(\mathcal{L}_t(\cdot)\) and allocation for _I_=3, _k_=1 using _q(t_)=_q_<sup>∗</sup>(_t_). For each item \(i\in\{A,B,C\}\), the left distribution is its current prior for \(\theta_i\), and the right is the posterior moment-matched distribution \(\widetilde{\theta}_i(\Delta_i)\). The allocation shown minimizes (8) with _B<sub>t</sub>_=10. The shaded area is the item’s contribution to the loss.


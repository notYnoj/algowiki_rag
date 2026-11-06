Here, the first equality holds because \(\mathcal{E}^\sigma=\mathcal{F}^\tau\) for each \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\text{coup}\), meaning each solution in \(\Omega^{\mathcal{F}\wedge\tau}\) is generated with equal probability \(\frac{1}{|\Omega^{\mathcal{F}\wedge\tau}|}=\frac{1}{|\Omega^{\mathcal{E}\wedge\sigma}|}\) as established in Lemma 5.13. The last equality follows from the identity \(\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma)=\frac{|\Omega^{\mathcal{E}\wedge\sigma}|}{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}\), because \(\mathcal{E}\wedge\sigma\Longrightarrow\mathcal{C}\backslash\{c_0\}\) for each \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})\), which holds by induction.

Therefore, we can construct a distribution \(\nu\) over \[_q_\]_<sup>V</sup>_ such that the measure of each \(y\in\Omega^\mathcal{C}\) is<tbc>

(17) \(\nu(y)=\frac{1}{|\Omega^\mathcal{C}|}\cdot\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\text{coup}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y,\)

<tbc>and meanwhile the total variation distance between \(\nu\) and the distribution \(\mu^\text{out}\) of \(\sigma^\text{out}\) is bounded as:

(18) \(d_\text{TV}\left(\nu,\mu^\text{out}\right)\le\left|\frac{1}{|\Omega^\mathcal{C}|}-r_-\cdot\frac{1}{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}\right|\sum_{y\in\Omega^\mathcal{C}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\text{coup}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y.\)

Given that \(\left(1-\frac{\varepsilon}{4}\right)r_-\cdot\frac{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}{|\Omega^\mathcal{C}|}\le\left(1+\frac{\varepsilon}{4}\right)r_+\) and \(r_-\ge\frac{4+\varepsilon}{4+2\varepsilon}r_+\) are ensured by the process, we obtain<tbc>

(19) \(\left(1-\frac{\varepsilon}{2}\right)\cdot\frac{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}{|\Omega^\mathcal{C}|}\le r_-\le\left(1+\frac{\varepsilon}{2}\right)\cdot\frac{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}{|\Omega^\mathcal{C}|}.\)

<tbc>Combining (18) and (19), we have<tbc>

(20) \(d_\text{TV}(\nu,\mu^\text{out})\le\frac{\varepsilon}{2}\cdot\frac{1}{|\Omega^\mathcal{C}|}\sum_{y\in\Omega^\mathcal{C}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\text{coup}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\le\frac{\varepsilon}{2}.\)

<tbc>Now, consider the total variation distance between \(\nu\) and \(\mu_\mathcal{C}\), the uniform distribution over \(\Omega^\mathcal{C}\). By (17) and (11), for each \(y\in\Omega^\mathcal{C}\) we have \(\nu(y)\le\frac{1}{|\Omega^\mathcal{C}|}=\mu_\mathcal{C}(y)\). Thus, we have

\(d_\text{TV}(\mu_\mathcal{C},\nu)=\sum_{y\in\Omega^\mathcal{C}}(\mu_\mathcal{C}(y-\nu(y))\)<br>
\(=\sum_{y\in\Omega^\mathcal{C}}\left(\frac{1}{|\Omega^\mathcal{C}|}-\frac{1}{|\Omega^\mathcal{C}|}\cdot\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\text{coup}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\right)\)<br>
\(=\frac{1}{|\Omega^\mathcal{C}|}\sum_{y\in\Omega^\mathcal{C}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\text{coup}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\)<br>
\(\text{(by (11))}\)<br>
\(\text{(by Claim 5.11)}\le\frac{\varepsilon}{2}.\)

Combining with (20) and by triangle inequality, we conclude

\(d_\text{TV}(\mu_\mathcal{C},\mu^\text{out})\le d_\text{TV}(\mu_\mathcal{C},\nu)+d_\text{TV}(\nu,\mu^\text{out})=\varepsilon.\) □

## References


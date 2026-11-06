<tbc>Lemma 3 says that \(\Gamma(w;\theta^0)\) is determined by the pair of items satisfying \(i\le k<j\) whose relative ranking is hardest to learn under the sampling design **_w_**. Maximizing over **_w_** gives

\(\Gamma^*(\theta^0):=max_{w\in\Delta_I}\Gamma(w;\theta^0).\) (13)

The next proposition establishes that \(\Gamma^*(\theta^0)\) is the optimal exponential decay rate of posterior EOC and that it is attained by any sampling rule whose empirical proportions converge to a maximizer of (13).

PROPOSITION 5 **(Optimal exponential rate of posterior EOC).**

(i) _The maximum in_ (13) _is attained, and_ \(0<\Gamma^*(\theta^0)<\infty\).<tbc>

(ii) _Every sampling rule satisfies_<tbc>

<tbc>\(limsup_{t\rightarrow\infty}-\frac{logEOC(\mathcal{H}_t)}{\sum_iN_i(t)}\le\Gamma^*(\theta^0).\)<tbc>

<tbc>(iii) _If the sampling proportions converge to a maximizer of_ (13)_, then_

\(lim_{t\rightarrow\infty}-\frac{logEOC(\mathcal{H}_t)}{\sum_iN_i(t)}=\Gamma^*(\theta^0).\)

We next show that, with threshold _q_<sup>†</sup>(_t_), TEAk’s posterior convergence rate is at least \(\Gamma^*(\theta^0)/2\).

## 4.3. The rate of TEAk

To determine the rate TEAk achieves, it is sufficient to characterize the sample proportions produced asymptotically. First, we do this assuming the threshold _q(t_) converges to some point \(q\in(\theta_{k+1}^0,\theta_k^0)\). For such a _q_, define the proportions

\(w_i(q):=\frac{1/d_i(\theta_i^0,q)}{\sum_{j=1}^I1/d_j(\theta_j^0,q)},i=1,\dots,I.\) (14)

THEOREM 1 **(Allocation and rate for a convergent threshold)**. _Assume_ \(q(t)\rightarrow q_0\in(\theta_{k+1}^0,\theta_k^0)\)_. Then_

(i) \(\widehat{w}_i(t)\rightarrow w_i(q_0)\) _for every i,_<tbc>

(ii) \(-\frac{logEOC(\mathcal{H}_t)}{\sum_iN_i(t)}\rightarrow\Gamma(w(q_0);\theta^0)\),<tbc>

(iii) \(\Gamma(w(q_0);\theta^0)\ge\left(\sum_{i=1}^I1/d_i(\theta_i^0,q_0)\right)^{-1}\).

Part (i) says that the asymptotic sampling proportions of TEAk are described by (14). To prove this, we show that<tbc>

\(-\frac{logD_{i,t}(d)}{N_i(t)}\longrightarrow d_i(\theta_i^0,q_0)\text{for every}i\text{and}d=0,\dots,B-1.\)

<tbc>Thus, \(d_i(\theta_i^0,q_0)\) gives the exponential decay rate of the marginal decrease in the surrogate per sample of item _i_. Since TEAk allocates samples to the items with the largest marginal decreases (the argument under DPBB is a bit more technical but also holds), it asymptotically samples the items with the smallest \(N_i(t)d_i(\theta_i^0,q_0)\), which leads to balancing \(N_i(t)d_i(\theta_i^0,q_0)\) across all items. Therefore, the sampling proportions converge to _w<sub>i</sub>(q_<sub>0</sub>), which makes \(w_i(q_0)d_i(\theta_i^0,q_0)\) equal across items. Part (ii) says that TEAk’s posterior convergence<tbc>


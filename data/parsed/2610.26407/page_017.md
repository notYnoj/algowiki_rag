and (_k_+1)th items, whereas **_w_**<sup>∗</sup> puts 78%. The middle panel shows an approximation<sup>1</sup> of -logEOC(H_<sub>t</sub>)/t_ along each replication as a fraction of \(\Gamma^*(\theta^0)\). For TEAk, it decreases towards \(\Gamma(w(q^\dagger);\theta^0)\) in line with Theorem 1(ii), and for the oracle allocation it approaches \(\Gamma^*(\theta^0)\). The right panel shows the convergence \(q^\dagger(t)\rightarrow q^\dagger\) on each replication.

## 5. Numerical experiments

In this section, we evaluate TEAk’s performance numerically by comparing it to the most competitive algorithms in the literature. For this comparison, we use a batch size of 1, as most benchmarks are designed for the fully sequential problem. §5.3 then turns to the batched setting and compares the performance of TEAk across batch sizes. Throughout, TEAk and TEAk-_q_<sup>†</sup>(_t_) denote Algorithm 3 with the threshold _q_<sup>∗</sup>(_t_) and _q_<sup>†</sup>(_t_) respectively. Across all settings, the two are nearly identical in both performance and allocation.

### 5.1. Setup

We consider \(I\in\{20,50,100\}\), with a sampling budget of up to \(1,000\cdot I\) for each setting. For _I_=20 we consider \(k\in\{1,3,5,10\}\), and for \(I\in\{50,100\}\) we consider \(k\in\{1,5,10,20\}\). On each (_I,k_) pair, we consider four likelihood families: Gaussian, exponential, Bernoulli, and lognormal. For each of the four families, we consider three generative distributions for their true means \(\theta\), given in  1. These ranges, although somewhat arbitrary, are targeted so that the difficulty of the identification problem is approximately the same across the likelihood families. The results are generally the same across these three generative distributions of the true means, so we report the results in the middle column in this section, giving the rest in Appendix D. We run 10,000 replications of each simulation, drawing the true means afresh in each.

<sup>1</sup> The posterior EOC(H_<sub>t</sub>_) has no closed form, so we plot the upper bound \(U_t:=\sum_{i\in S_k(\mu(t))}\sum_{j\notin S_k(\mu(t))}\mathbb{E}_t[(\theta_j-\theta_i)^+]\) in its place, and each term has an explicit expression under Gaussian posteriors. Since \(U_t/(k(I-k))\le\text{EOC}(\mathcal{H}_t)\le U_t\), the plotted value differs from -logEOC(H_<sub>t</sub>)/t_ by at most log(_k(I-k_))_/t_.

TEAk -
- =
0.57T *
0.4 1.2 -2.150 -2.175 1.0 -2.200 0.3 0.8 -2.225 sampling proportion at t = 20, 000 0.6 threshold q (t) -2.250 0.2 -logEOC(H0)/(tT*) -2.275 0.4 0.1 -2.300 0.2 -2.325 0.0 0.0 1
3 5
7 9
11 13 15 17 19 2500 5000 7500 10000 12500 15000 17500 20000 0
2500 5000 7500 10000 12500 15000 17500 20000 item, ordered by true mean cumulative samples t cumulative samples t

**Figure 3** Left: TEAk’s sampling proportions at _t_=20,000, averaged over replications, as well as **_w_**(_q_<sup>†</sup>) and **_w_**<sup>∗</sup>. Middle: \(-log\text{EOC}(\mathcal{H}_t)/(t\Gamma^*(\theta^0))\) for TEAk, the oracle allocation, and equal allocation on each of the 50 replications (median in bold). Right: the threshold _q_<sup>†</sup>(_t_) on each of the 50 replications (median in bold).


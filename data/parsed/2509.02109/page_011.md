<tbc>parametrise a discrete measure \(\mu\in\mathcal{P}(\mathbb{R})\) with a support size of 3 as follows:<tbc>

\(\forall\alpha\in[-\frac{1}{6},\frac{1}{6}]^2,\forall\eta\in(-\frac{1}{2},\frac{1}{2})^3,\mu_{\alpha,\eta}:=(\frac{1}{6}+\alpha_1)\delta_{\eta_1}+(\frac{1}{6}+\alpha_2)\delta_{\eta_2}+(\frac{2}{3}-\alpha_1-\alpha_2)\delta_{1+\eta_3},\)

<tbc>and we fix a target measure \(\nu:=\frac{1}{3}(\delta_0+\delta_{1-\varepsilon}+\delta_{1+\varepsilon})\) for a fixed \(\varepsilon\in(0,\frac{1}{2})\). The energy to minimise is then:

\(\mathcal{E}_3:=\left\{\begin{array}{ c c }
[-\frac{1}{6},\frac{1}{6}]^2\times(-\frac{1}{2},\frac{1}{2})^3 & \longrightarrow\mathbb{R} \\
(\alpha,\eta) & \longmapsto\text{W}_2^2(\mu_{\alpha,\eta},\nu)
\end{array}\right..\) (19)

Obviously, the energy \((\alpha,\eta)\longmapsto\text{W}_2^2(\mu_{\alpha,\eta},\nu)\) has a global minimum with value 0 at all \((\alpha,\eta)\) such that \(\mu_{\alpha,\eta}=\nu\). However, on the region with \((\alpha,\eta)\in[-\frac{1}{6},\frac{1}{6}]^2\times(-\frac{1}{2},\frac{1}{2})^3\), we show in Appendix A.7.1 that the energy E<sub>3</sub> has a minimum at \(\alpha=0_{\mathbb{R}^2}\) and \(\eta=0_{\mathbb{R}^3}\), with value E<sub>3</sub>(0<sub>R<sup>2</sup></sub>,0<sub>R<sup>3</sup></sub>)_\>_0. Note that for the case _n_=2 we can show that there is a unique local minimum, see Appendix A.7.2.

### Essential Stationary Points for the \(\text{EM}-\text{MW}_2^2\) Loss.

We have seen in the previous paragraph that optimising \(\mu\longmapsto\text{W}_2^2(\mu,\nu)\) with respect to the weights and support of \(\mu\) can lead to local minima, which are not global minima. An additional difficulty arises when optimising the energy

\(\mathcal{E}_{\text{EM}-\text{MW}_2^2}:=X\longmapsto\text{MW}_2^2(\mu(F(\theta,X)),\nu),\) (20)

with one iteration _F_ of the EM algorithm, due to the update on the weights. The issue is that at some problematic points _X_ to which the algorithm often converges in practice, the gradient \(\partial_X\mathcal{E}_{\text{EM}-\text{MW}_2^2}(X)\) becomes extremely small, in particular when the covariances are highly localised. This leads in practice to undesirable convergence to an essential local minimum, as illustrated by an example in Section 4.3. We provide a theoretical explanation in a simple case in Appendix A.7.3. To avoid these numerical issues, we propose fixing the weights of the GMMs in the EM steps by using Algorithm 2.

Our theoretical observations suggest that considering GMMs with uniform weights and using fixed- weights EM (Algorithm 2) is a more stable alternative to standard EM (Algorithm 1). In practice, we believe it is also preferable to keep the same number of components _K_ between the compared GMMs for additional stability. Note that an identifiability issue remains with GMMs: if the means and covariances of two modes coincide, then the GMM can also be written by fusing both components and adding their weights. At this stage, it remains unclear whether this phenomenon has an impact on the optimisation behaviour (note that we never observed it in our experiments).

## 3.4 Unbalanced GMM-OT

Starting from the discrete formulation of the MW<sub>2</sub> distance, we relax the constraints on the transport plan \(\pi\), penalising the marginal conditions instead of enforcing them in the optimisation problem. The resulting optimisation problem defines an unbalanced GMM-OT distance on the set<tbc>

101
low medium high n-1/2
100
MW2(u, u)
10-1
10-2
103
104
sample size n

100
MW2(u, v)/MW2(u, v)
low medium high n-1/2
10-1
10-2
103
104
sample size n

(a) One-sample: \(\text{MW}_2^2(\hat{\mu}_n,\mu)\)

(b) Two-sample: relative error

Figure 2: Sample complexity of \(\text{MW}_2^2\) for three specific GMMs of "low" to "high" mode separation. Curves show the median across 40 repetitions, with shaded interquartile ranges.


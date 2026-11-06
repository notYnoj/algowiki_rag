<tbc>_Proof_ Fix _i_ and let \(\widetilde{\pi}_i^{(n)}\) be the posterior density of \(\eta_i(\theta_i)\). By Russo (2020, Lemmas EC.5, EC.7, and EC.8), with the latter two applied over E_<sub>i</sub>_,

\(sup_{x\in\mathcal{J}}\left|\frac{1}{n}log\widetilde{\pi}_i^{(n)}(\eta_i(x))+d_i(\theta_i^0,x)\right|\longrightarrow 0.\)

Since \(\widetilde{\pi}_{i,0}\) is bounded above and bounded away from zero, the same limit holds after dividing \(\widetilde{\pi}_i^{(n)}\) by \(\widetilde{\pi}_{i,0}\). The posterior-to-prior density ratio is unchanged by the transformation \(\eta_i\), proving (18).

We next establish convergence of the posterior mean and variance. By Russo (2020, Proposition 4), the posterior concentrates at \(\theta_i^0\). Since J is bounded, this gives \(\mu_{i,n}\rightarrow\theta_i^0\) and \(v_{i,n}\rightarrow 0\). His proof of that proposition in Section EC.6.2 also shows that, for every sufficiently small \(\delta>0\), there is a constant \(c_{i,\delta}>0\) such that, for all sufficiently large _n_,<tbc>

\(\Pi_i^{(n)}(|\theta_i-\theta_i^0|\ge\delta)\le e^{-nc_{i,\delta}}.\) (20)

<tbc>We next show that \(-n^{-1}logv_{i,n}\rightarrow 0\). Fix \(\varepsilon>0\) and choose \(\delta>0\) so that \(V:=(\theta_i^0-2\delta,\theta_i^0-\delta)\subset\mathcal{J}\) and \(d_i(\theta_i^0,x)\le\varepsilon\) for every \(x\in V\) . Since \(\mu_{i,n}\rightarrow\theta_i^0\), eventually \(\mu_{i,n}\ge\theta_i^0-\delta/2\), giving<tbc>

\(v_{i,n}\ge\int_V(x-\mu_{i,n})^2\Pi_i^{(n)}(dx)\ge\frac{\delta^2}{4}\Pi_i^{(n)}(V).\)

<tbc>Taking logarithms and applying Lemma 2,

\(limsup_{n\rightarrow\infty}-\frac{1}{n}logv_{i,n}\le inf_{x\in V}d_i(\theta_i^0,x)\le\varepsilon.\)

Letting \(\varepsilon\downarrow 0\) and using that the variance is bounded gives \(-n^{-1}logv_{i,n}\rightarrow 0\).

It remains to prove (19). The claim is trivial for _m_=0. Fix \(m\ge 1\). The law of total variance gives \(\bar{v}_i(t,m)/v_i(t)\le 1\). We will show that \(liminf_{t\rightarrow\infty}\bar{v}_i(t,m)/v_i(t)\ge 1\).

Let _Y_<sub>1</sub>_,...,Y<sub>m</sub>_ denote the new observations of item _i_. The expectation \(\mathbb{E}_{\theta_i^0}\) is over these additional observations only. By Bayes’ formula and minimization of expected squared error,

\(\bar{v}_i(t,m)=\mathbb{E}_t\left[\frac{min_{a\in\mathbb{R}}\int_\mathcal{J}(x-a)^2\prod_{r=1}^mp_i(Y_r|x)\Pi_{i,t}(dx)}{\int_\mathcal{J}\prod_{r=1}^mp_i(Y_r|z)\Pi_{i,t}(dz)}\right]\)<br>
\(=\mathbb{E}_{\theta_i^0}\left[\frac{\int_\mathcal{J}\prod_{r=1}^mp_i(Y_r|z)\Pi_{i,t}(dz)}{\prod_{r=1}^mp_i(Y_r|\theta_i^0)}\times\frac{min_{a\in\mathbb{R}}\int_\mathcal{J}(x-a)^2\prod_{r=1}^mp_i(Y_r|x)\Pi_{i,t}(dx)}{\int_\mathcal{J}\prod_{r=1}^mp_i(Y_r|z)\Pi_{i,t}(dz)}\right]\)<br>
\(=\mathbb{E}_{\theta_i^0}\left[min_{a\in\mathbb{R}}\int_\mathcal{J}(x-a)^2\prod_{r=1}^m\frac{p_i(Y_r|x)}{p_i(Y_r|\theta_i^0)}\Pi_{i,t}(dx)\right].\)


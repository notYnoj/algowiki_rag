observation is that this biased edge sampler is by very definition an _importance sampler_ for sampling a uniformly random edge at its original weight, the variance of which is sensitive to outlier heavy edges; our importance sampling approach with Rand_<sub>G</sub>_ does not have this issue, enjoying a manner of variance reduction by virtue of yielding Bernoulli variables that concentrate well for Chernoff bounds.

**Proposition 5** (Chernoff-Hoeffding bound, \[20\])**.** Let _X_<sub>1</sub>_,...,X<sub>m</sub>∼X_ be i.i.d. Bernoulli random variables. Let \(Y=\sum_{i=1}^mX_i\). Then,

\(Pr\left[|Y-\mathbb{E}[Y]|\ge t\mathbb{E}[Y]\right]\le 2exp(-t^2\mathbb{E}[Y]/3)\text{for}t\in(0,1)\) (1a)

\(Pr\left[Y-\mathbb{E}[Y]\ge t\mathbb{E}[Y]\right]\le exp(-t\mathbb{E}[Y]/3)\text{for}t\ge 1\) (1b)

Theorem 3.1 also gives a tighter analysis on the sample complexity required to sparsify heavy subgraph problems, improving the bound of \(O(n(4+\delta)log\ell/\gamma\varepsilon^2)\) samples in Proposition 4 to \(O(n(1+\delta+log\ell+\gamma^{-1})/\varepsilon^2)\) samples. We now state the result.

**Theorem 3.1.** Let P be a \((\gamma,\ell)\)-heavy subgraph problem on the (hyper)graph _H_=(_V,E,w_) with objective _f_. Let oracle \(\mathcal{O}\in E\) be a random variable s.t. O=_e_ w.p. _w(e)/w(H_) for all \(e\in E\), and let \(\unknown_\mathcal{O}\) be the indicator function s.t. \(\unknown_\mathcal{O}(e)=1\) if _e_=O and 0 otherwise. For any \(\delta>0\), \(\varepsilon\in[0,1]\), let weight function \(\hat{w}\) be the sum of \(\unknown_\mathcal{O}\) for \(O(n(1+\delta+log\ell+\gamma^{-1})/\varepsilon^2)\) independent samples of O. Define the heavy subgraph problem \(\hat{\mathcal{P}}\) identically to P, but on the hypergraph \(\hat{H}=(V,E,\hat{w})\) with objective _g_ s.t. \(g(\mathcal{S})=f_k\cdot\hat{w}(\mathcal{S})\) for all \(\mathcal{S}\in\mathbb{S}_k\). Denoting by S<sup>∗</sup> and \(\hat{\mathcal{S}}^*\) the optimal solutions to P and \(\hat{\mathcal{P}}\), respectively, then we have

\(f(\hat{\mathcal{S}}^*)\ge f(\mathcal{S}^*)/(1+\varepsilon)\text{w.p. at least}1-e^{-\delta}.\)

_Proof._ Let S, the set of solutions to P and thus \(\hat{\mathcal{P}}\), be partitioned into sets \(\mathbb{S}_1,\dots,\mathbb{S}_\ell\) with local linearity constants \(f_1,\dots,f_\ell\). Without loss of generality, assume that _H_ has average edge weight 1 such that _w(H_)=_m_=|_E_|. Let \(C=240n(1+\delta+log\ell+\gamma^{-1})/\varepsilon^2\) be the number of samples of O taken, and define scaling factor _p=C/m_. Lastly, we denote _f_(S<sup>∗</sup>) by OPT.

Now, let S be an arbitrary solution from S_<sub>k</sub>_. Using local linearity, we first show that the objective value of S in \(\hat{H}\), after scaling, is an unbiased estimator for its objective value in _H_.

\(\mathbb{E}[g(\mathcal{S})]=\mathbb{E}[f_k\cdot\hat{w}(\mathcal{S})]=f_k\sum_{e\in\mathcal{S}}\mathbb{E}[\hat{w}(e)]=f_k\sum_{e\in\mathcal{S}}C\cdot\mathbb{E}[\unknown_\mathcal{O}(e)]=Cf_k\sum_{e\in\mathcal{S}}Pr[\mathcal{O}=e]=Cf_k\sum_{e\in\mathcal{S}_H}w(e)/m=pf_k\cdot w(\mathcal{S})=p\cdot f(\mathcal{S}).\text{(2)}\)

Since \(\hat{w}(\mathcal{S})\) is the sum of \(\unknown_\mathcal{O}(e)\)’s which are individually Bernoulli, then we are able to show that the objective _g_(S) concentrates well.

**Lemma 3.2.** Fix \(k\in[\ell]\), and let \(\epsilon_k=2exp\left(-p\varepsilon^2OPT/240f_k\right)\). Then for any \(\mathcal{S}\in\mathbb{S}_k\),

\(Pr\left[\left|g(\mathcal{S})-pf(\mathcal{S})\right|\ge\varepsilon pf(\mathcal{S})/4\right]\le\epsilon_k\text{if}f(\mathcal{S})>OPT/5\)<br>
\(Pr\left[g(\mathcal{S})\ge 3pOPT/5\right]\le\epsilon_k\text{if}f(\mathcal{S})\le OPT/5\)

_Proof._ Take S such that _f_(S)_\>_OPT/5. Local linearity yields \(|g(\mathcal{S})-pf(\mathcal{S})|=|f_k\hat{w}(\mathcal{S})-pf_kw(\mathcal{S})|\), and so noting that _w_(S)=_f_(S)_/f<sub>k</sub>_, we have

\(Pr\left[\left|g(\mathcal{S})-pf(\mathcal{S})\right|\ge\frac{\varepsilon pf(\mathcal{S})}{4}\right]=Pr\left[\left|\hat{w}(\mathcal{S})-pw(\mathcal{S})\right|\ge\frac{\varepsilon}{4}\frac{pf(\mathcal{S})}{f_k}\right]\le 2exp\left(-\frac{\varepsilon^2}{16}\frac{pf(\mathcal{S})}{3f_k}\right)\le\epsilon_k,\)

where the first inequality uses the Chernoff bound eq. (1a) along with eq. (2), and the second follows by our lower bound on _f_(S). Otherwise, if \(f(\mathcal{S})\le OPT/5\), then the inequality \(g(\mathcal{S})\ge\)<tbc>


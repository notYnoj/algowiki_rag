<tbc>_Remark_ II.2. Compared with the existing tightest bound \(\Omega(Klog(1/\delta)/log((1-p)/p))\) in Feige et al. (1994), the rate is greatly improved as \(p\rightarrow 0\) or \(p\rightarrow 1/2\).

On the other hand, the best known upper bound from Feige et al. (1994), which is \(\mathcal{O}(\frac{Klog(1/\delta)}{1-H(p)})\). We include its algorithm and analysis in Appendix I. Theorem II.1 shows that when \(\delta\) is bounded away from 0, one needs at least \(C\cdot K/(1-H(p))\) samples, matching the upper bound. Similarly, when _p_ is bounded away from 0, the term _D_KL(_p_∥1-_p_) is also within a constant factor of 1-_H(p_), thus the upper and lower bounds match. The only regime where the upper and lower bounds do not match is the case when both _p_ and \(\delta\) go to 0. We conjecture that a better upper bound is needed in this case.

## B. Non-adaptive Sampling

In the case of non-adaptive sampling, we show that O(_K_) queries are not enough. And one needs \(\Omega(Klog(K))\) queries.

**Theorem II.3.** _In the non-adaptive sampling setting, where the sampling procedure is restricted to taking independent samples from a sequence of distributions_ \(p_1,\cdots,p_T\)_, we have_

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\mathsf{OR}(\theta))\)<br>
\(\ge\frac{1}{2}\cdot\left(1-\sqrt{\frac{1}{2K}\big(\left(1+\frac{(1-2p)^2}{K(1-p)p}\right)^T-1\big)\big)}\right).\)

_This shows that the query complexity is at least_ \(\Omega(max(K,Klog(K)p/(1-H(p))))\).

We provide the proof below. Different from the case of adaptive sampling, for non-adaptive sampling we target for a rate of \(\Omega(Klog(K))\). And a standard Le Cam’s two point method is not sufficient to give the extra logarithmic factor. Thus we provide a new proof based on a point versus mixture extension of Le Cam’s method.

_Proof of Theorem II.3._ Consider the instance 0 which has all 0 as its elements. For instance 1, we define it as a distribution _q_ over _K_ instances 1_<sub>k</sub>_, \(k\in[K]\) which puts probability _p<sub>k</sub>_ on the _k_-th element. We will determine the value of _p<sub>k</sub>_ later. Here instance 1_<sub>k</sub>_ refers to the case when _k_-th element is 1, and the rest elements are 0. Now from Le Cam’s two point lemma, we have

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\mathsf{OR}(\theta))\)<br>
\(\ge\frac{1}{2}(1-\mathsf{TV}(\mathbb{P}_1,\mathbb{P}_0))\)<br>
\(=\frac{1}{2}(1-\mathsf{TV}(\mathbb{E}_{j\sim q}[\mathbb{P}_{1_j}],\mathbb{P}_0))\)<br>
\(\ge\frac{1}{2}\left(1-\sqrt{\frac{1}{2}}\chi^2(\mathbb{E}_{j\sim q}[\mathbb{P}_{1_j}],\mathbb{P}_0)}\right).\)

Here the last inequality is based on the inequality \(\mathsf{TV}\le\sqrt{\frac{1}{2}}\chi^2\). Let \(\pi_m^t\) be the probability of querying the _m_-th


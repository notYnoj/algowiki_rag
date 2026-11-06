## A. Adaptive Sampling

We have the following minimax lower bound.

**Theorem II.1.** _In the adaptive setting, we have_

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\mathsf{OR}(\theta))\ge\frac{1}{4}\cdot exp\left(-\frac{T\cdot D_\mathsf{KL}(p\|1-p)}{K}\right).\)

_Thus, the number of queries required to recover the true value with probability at least_ \(1-\delta\) _is lower bounded by_ \(\Omega(K/(1-H(p))+Klog(1/\delta)/D_\mathsf{KL}(p\|1-p))\).

We provide the proof here, which is based on Le Cam’s two point method (see e.g. (LeCam, 1973; Yu, 1997)).

_Proof of Theorem II.1._ Our lower bound proof is mainly based on Le Cam’s two point method, which is also re-stated in Lemma A.1 in Appendix A for reader’s convenience. Let \(\theta_0\) be the length-_K_ all-zero sequence, and let \(\theta_j\in\{0,1\}^K\) be such that \(\theta_{jj}=1\) and \(\theta_{ji}=0\) for \(i\neq j\). Here \(\theta_{ji}\) refers to the _i_-th element in the binary vector \(\theta_j\). We can first verify that for any \(\hat{\mu}\), one has<tbc>

\(\mathbb{1}(\hat{\mu}\neq\mathsf{OR}(\theta_0))+\mathbb{1}(\hat{\mu}\neq\mathsf{OR}(\theta_j))\ge 1.\)

<tbc>By applying Le Cam’s two point lemma on \(\theta_0\) and \(\theta_j\), we know that<tbc>

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\mathsf{OR}(\theta))\ge\frac{1}{2}(1-\mathsf{TV}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_j})).\)

<tbc>Here \(\mathbb{P}_{\theta_j}\) is the joint distribution of query-observation pairs in _T_ rounds when the ground truth is \(\theta_j\). By taking maximum over _j_ on the right-hand side, we have

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\mathsf{OR}(\theta))\)<br>
\(\ge sup_{1\le j\le K}\frac{1}{2}(1-\mathsf{TV}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_j}))\)<br>
\(\ge sup_{1\le j\le K}\frac{1}{4}exp(-D_\mathsf{KL}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_j})).\)

Here the last inequality is due to Bretagnolle-Huber inequality (Bretagnolle and Huber, 1979) (Lemma A.4 in Appendix A). Now we aim at computing \(D_\mathsf{KL}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_j})\). Let _T<sub>j</sub>_ be the random variable that denotes the number of times the _j_-th element is queried among all _T_ rounds. From divergence decomposition lemma (Auer et al., 1995) (Lemma A.3 in Appendix A), we have<tbc>

\(D_\mathsf{KL}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_j})=\mathbb{E}_{\theta_0}[T_j]\cdot D_\mathsf{KL}(p\|1-p).\)

<tbc>Here \(\mathbb{E}_{\theta_0}[T_j]\) denotes the expected number of times the _j_-th element is queried when the ground truth is \(\theta_0\). Thus we have

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\mathsf{OR}(\theta))\)<br>
\(\ge sup_{1\le j\le K}\frac{1}{4}exp(-\mathbb{E}_{\theta_0}[T_j]\cdot D_\mathsf{KL}(p\|1-p)).\)

Now since \(\sum_j\mathbb{E}_{\theta_0}[T_j]=T\), there must exists some _j_ such that \(\mathbb{E}_{\theta_0}[T_j]\le T/K\). This gives

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\mathsf{OR}(\theta))\ge\frac{1}{4}\cdot exp\left(-\frac{T\cdot D_\mathsf{KL}(p\|1-p)}{K}\right).\)

On the other hand, _K_ is naturally a lower bound for query complexity since one has to query each element at least once. Thus we arrive at a lower bound of \(\Omega(K+Klog(1/\delta)/D_\mathsf{KL}(p\|1-p))\). Note that this is equivalent to \(\Omega(K/(1-H(p))+Klog(1/\delta)/D_\mathsf{KL}(p\|1-p))\) up to a constant factor when \(\delta<0.49\). The reason is that when _p_ is bounded away from 0, (1-_H(p_))_/D_<sub>KL</sub>(_p_∥1-_p_) is always some constant. When _p_ is close to 0, 1-_H(p_) is within constant factor of 1.


<tbc>_Remark_ II.4. Compared with the bound \(\Omega(\frac{Klog(K)}{log((1-p)/p)})\) in (Reischuk and Schmeltz, 1991; Gács and Gál, 1994), our lower bound is tighter when \(p\rightarrow 1/2\), but looser when \(p\rightarrow 0\). Thus the tightest lower bound is a maximum of _K_ and the two lower bounds. The corresponding repetition-based upper bound \(\mathcal{O}(\frac{Klog(K/\delta)}{1-H(p)})\) can be derived by a union-bound based argument. Compared with the upper bound \(\mathcal{O}(\frac{Klog(K/\delta)}{1-H(p)})\), the lower bound is tight with respect to all parameters when both _p_ and \(\delta\) are bounded away from 0.

## III. COMPUTING THE MAX FUNCTION

Let \(\theta\in[0,1]^K\) be a sequence of length _K_ representing the true values of each element. \(\text{MAX}(\theta)\) be the index of the maximum value in the sequence. We also let \(\hat{\mu}\) be any algorithm that (possibly randomly) queries any noisy comparison between two elements in _T_ rounds, and output a (possibly random) decision from 0,1.

### A. Adaptive Sampling

We have the following minimax lower bound for the adaptive setting. The proof is deferred to Appendix B.

**Theorem III.1.** _In the adaptive setting, we have_

\(inf_\hat{\mu}sup_{\theta\in[0,1]^K}\mathbb{P}(\hat{\mu}\neq\text{MAX}(\theta))\ge\frac{1}{2}\cdot exp\left(-\frac{T\cdot D_\text{KL}(p\|1-p)}{K}\right).\)

_Thus, the number of queries required to recover the true value with probability at least_ \(1-\delta\) _is lower bounded by_ \(\Omega(K/(1-H(p))+Klog(1/\delta)/D_\text{KL}(p\|1-p))\).

The comparison with the existing lower bound (Feige et al., 1994) for computing MAX is similar as that for OR in Remark II.2, and is thus omitted here.

### B. Non-adaptive Sampling

In the case of non-adaptive sampling, we show that O(_K_) samples are not enough. Instead, one needs at least \(\Omega(K^2)\) samples. We have the following result. The proof is deferred to Appendix C.

**Theorem III.2.** _In the non-adaptive setting, where the sampling procedure is restricted to taking independent samples from a sequence of distributions_ \(p_1,\cdots,p_T\)_, we have_

\(inf_\hat{\mu}sup_{\theta\in[0,1]^K}\mathbb{P}(\hat{\mu}\neq\text{MAX}(\theta))\ge\frac{1}{4}\cdot exp\left(-\frac{T\cdot D_\text{KL}(p\|1-p)}{K^2}\right).\)

_Thus the queries required to recover the true value with probability at least_ \(1-\delta\) _is lower bounded by_ \(\Omega(K^2/(1-H(p))+K^2log(1/\delta)/D_\text{KL}(p\|1-p))\).

_Remark_ III.3. Compared with the repetition-based upper bound O(_K_<sup>2</sup>log(_K_)), the lower bound has a log(_K_) gap. The tight dependence on _K_ remains open.

## IV. COMPUTING THE SEARCH FUNCTION

### A. Adaptive Sampling

Recall that for any sorted sequence \(X_1,\cdots,X_K\), the SEARCH function for _X_ is defined as \(\text{SEARCH}(X;X_1,\cdots,X_K)=i\), where _i_ satisfies _X<sub>i</sub>\<X\<X_<sub>_i_+1</sub>. We start with adaptive setting. The proof is deferred to Appendix D.

**Theorem IV.1.** _In the adaptive setting, we have_

\(inf_\hat{\mu}sup_X\mathbb{P}(\hat{\mu}\neq\text{SEARCH}(X))\)<br>
\(\ge\frac{1}{4}\cdot max\left(exp\left(-T\cdot D_\text{KL}(p\|1-p)\right),1-\frac{T\cdot(1-H(p))}{log(K)}\right).\)

_Thus the queries required to recover the true value with probability at least_ \(1-\delta\) _is lower bounded by_ \(\Omega(log(K)/(1-H(p))+log(1/\delta)/D_\text{KL}(p\|1-p))\).

_Remark_ IV.2. The same lower bound is also proven in two different manners in the concurrent work (Wang et al., 2023; Gu and Xu, 2023). And a matching upper bound that is tight with respect to all parameters when _p_ is bounded away from 0 and 1/2 is provided in Gu and Xu (2023).


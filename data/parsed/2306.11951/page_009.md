### B. Non-adaptive Sampling

For non-adaptive sampling, we show \(\Omega(K)\) queries are needed. The proof is deferred to Appendix E.

**Theorem IV.3.** _In the non-adaptive setting where the sampling procedure is restricted to taking independent samples from a sequence of distributions_ \(p_1,\cdots,p_T\)_, we have_

\(inf_\hat{\mu}sup_X\mathbb{P}(\hat{\mu}\neq\mathsf{SEARCH}(X))\ge\frac{1}{4}\cdot exp\left(-\frac{T\cdot D_\mathsf{KL}(p\|1-p)}{K}\right).\)

_Thus, the queries required to recover the true value with probability at least_ \(1-\delta\) _is lower bounded by_ \(\Omega(K/(1-H(p))+Klog(1/\delta)/D_\mathsf{KL}(p\|1-p))\).

_Remark_ IV.4. We show in Appendix H the upper bound \(\mathcal{O}(Klog(1/\delta)/(1-H(p)))\) for computing SEARCH. Our lower bound matches with all parameters when either _p_ or \(\delta\) is bounded away from 0.

## V. COMPUTING THE SORT FUNCTION

### A. Adaptive Sampling

Let \(\theta\in[0,1]^K\) be any sequence of _K_ elements with distinct values in \[0,1\], \(\mathsf{SORT}(\theta)\) be the result of the SORT function applied on the noiseless sequence. We also let \(\hat{\mu}\) be any algorithm that queries any noisy comparison between two elements in _T_ rounds, and output a (possibly random) decision. We have the following result for computing the SORT function. The proof is deferred to Appendix F.

**Theorem V.1.** _In the adaptive setting, we have_

\(inf_\hat{\mu}sup_{\theta\in[0,1]^K}\mathbb{P}(\hat{\mu}\neq\mathsf{SORT}(\theta))\)<br>
\(\ge\frac{1}{4}max\left(exp\left(-\frac{T\cdot D_\mathsf{KL}(p\|1-p)}{K}\right),1-\frac{T\cdot(1-H(p))}{Klog(K)}\right).\)

_Thus, the queries required to recover the true value with probability at least_ \(1-\delta\) _is lower bounded by_ \(\Omega(Klog(K)/(1-H(p))+Klog(K/\delta)/D_\mathsf{KL}(p\|1-p)))\).

_Remark_ V.2. Compared with the upper bound \(\mathcal{O}(Klog(K/\delta)/(1-H(p)))\), the bound is tight with all parameters when either _p_ or \(\delta\) is bounded away from 0.

### B. Non-adaptive Sampling

Here we provide the following minimax lower bound for non-adaptive learning. The proof is deferred to Appendix G.

**Theorem V.3.** _In the non-adaptive setting where the sampling procedure is restricted to taking independent samples from a sequence of distributions_ \(p_1,\cdots,p_T\),

\(inf_\hat{\mu}sup_{\theta\in[0,1]^K}\mathbb{P}(\hat{\mu}\neq\mathsf{SORT}(\theta))\ge\frac{1}{2}\cdot\left(1-\frac{T\cdot D_\mathsf{KL}(p\|1-p)}{K^2log(K)}\right).\)

_Thus, the queries required to recover the true value with probability at least_ \(1-\delta\) _is lower bounded by_ \(\Omega(max(K^2,K^2log(K)/D_\mathsf{KL}(p\|1-p)))\).

_Remark_ V.4. Compared with the repetition-based upper bound \(\mathcal{O}(K^2log(K/\delta)/(1-H(p)))\), the lower bound is tight with all parameters when _p_ and \(\delta\) are bounded away from 0.

## VI. MATCHING BOUNDS FOR VARIABLE LENGTH

In this section, we provide matching upper and lower bounds for the variable-length setting. All the bounds here are the same as the lower bound for the fixed-length setting, the proof of which can be directly adapted from the fixed-length results.

**Theorem VI.1.** _In the adaptive setting, the number of queries in expectation to achieve at most_ \(\delta\) _error probability is_

1) \(\Theta(\frac{K}{1-H(p)}+\frac{Klog(1/\delta)}{D_\mathsf{KL}(p\|1-p)})\) _for computing_ OR;


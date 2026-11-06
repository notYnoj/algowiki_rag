<tbc>compared to non-adaptive querying. When the observation of each query goes through a binary symmetric channel BSC(_p_), we ask two questions:

\(\bullet\) How many queries (samples) do we need in the worst case to recover the true OR function value of any given sequences \(X_1,\cdots,X_K\) with probability at least \(1-\delta\)?<tbc>

\(\bullet\) Can adaptive sampling do better than non-adaptive sampling when noise is present?

TABLE I: Summary of query complexity bounds of OR, MAX, SEARCH and SORT. Here, we assume \(\delta<0.49\).

In Feige et al. (1994), an adaptive tournament algorithm is proposed that achieves worst-case query complexity O(_K_log(1/\(\delta\))/(1-_H(p_))), and a corresponding lower bound \(\Omega(Klog(1/\delta)/log((1-p)/p))\) for adaptive sampling is provided. A simple calculation tells us that their ratio log((1-_p)/p)/_(1-_H(p_)) goes to infinity as \(p\rightarrow 0\) or \(p\rightarrow 1/2\), which indicates that there is still a gap between the upper and the lower bounds when the noise probability _p_ is near the point 0 or 1/2. This calls for tighter upper or lower bound for these cases. In our paper, we improve the lower bound to \(\Omega(K/(1-H(p))+Klog(1/\delta)/D_\text{KL}(p\|1-p))\), which matches the existing upper bound up to a constant factor when either _p_ or \(\delta\) is bounded away from 0.

One may wonder how many samples are needed when each query is not allowed to depend on previous outcomes. We provide a lower bound \(\Omega(max(K,Klog(K)p/(1-H(p))),Klog(K)/log((1-p)/p))\) for this non-adaptive setting. On the other hand, a repetition-based upper bound \(\mathcal{O}(Klog(K/\delta)/(1-H(p)))\) matches the lower bound up to a constant factor when both _p_ and \(\delta\) are bounded from 0.

Similarly, we ask the same questions for computing MAX, SEARCH, and SORT. We defer the definitions and discussions of the problems to Section I-B. Here we summarize the best upper and lower bounds for the problems considered in this paper in  I, either from previous art or from this paper.

Our lower bounds take the form of \(f(K)/(1-H(p))+g(K,\delta)/D_\text{KL}(p\|1-p)\). Here the first term does not depend on \(\delta\) for \(\delta<0.49\), representing the number of queries one must pay regardless of the target error probability \(\delta\). The second term grows logarithmically with \(1/\delta\), representing the price to pay for smaller target<tbc>

\begin{tabular}{ccc}
\multirow{2}{*}{**Problem**} & \multicolumn{2}{c}{**Fixed Length, Adaptive Sampling**} \\
 & Upper Bound & Lower Bound \\
OR & \(\mathcal{O}(\frac{Klog(1/\delta)}{1-H(p)})\) (Feige et al., 1994) & \(\Omega(\frac{K}{1-H(p)}+\frac{Klog(1/\delta)}{D_\text{KL}(p\|1-p)})\) (Thm II.1) \\
MAX & \(\mathcal{O}(\frac{Klog(1/\delta)}{1-H(p)})\) (Feige et al., 1994) & \(\Omega(\frac{K}{1-H(p)}+\frac{Klog(1/\delta)}{D_\text{KL}(p\|1-p)})\) (Thm III.1) \\
SEARCH & \(\mathcal{O}(\frac{log(K/\delta)}{1-H(p)})\) (Feige et al., 1994) & \(\Omega(\frac{log(K)}{1-H(p)}+\frac{log(1/\delta)}{D_\text{KL}(p\|1-p)})\) (Thm IV.1) \\
SORT & \(\mathcal{O}(\frac{Klog(K/\delta)}{1-H(p)})\) (Feige et al., 1994) & \(\Omega(\frac{Klog(K)}{1-H(p)}+\frac{Klog(K/\delta)}{D_\text{KL}(p\|1-p)})\) (Thm V.1) \\
\multirow{2}{*}{**Problem**} & \multicolumn{2}{c}{**Fixed Length, Non-adaptive Sampling**} \\
 & Upper Bound (Appendix H) & Lower Bound \\
OR & \(\mathcal{O}(\frac{Klog(K/\delta)}{1-H(p)})\) & \(\Omega(max(K,\frac{Klog(K)p}{1-H(p)},\frac{Klog(K)}{log((1-p)/p)}))\) (Thm II.3) \\
MAX & \(\mathcal{O}(\frac{K^2log(K/\delta)}{1-H(p)})\) & \(\Omega(\frac{K^2}{1-H(p)}+\frac{K^2log(1/\delta)}{D_\text{KL}(p\|1-p)})\) (Thm III.2) \\
SEARCH & \(\mathcal{O}(\frac{Klog(1/\delta)}{1-H(p)})\) & \(\Omega(\frac{K}{1-H(p)}+\frac{Klog(1/\delta)}{D_\text{KL}(p\|1-p)})\) (Thm IV.3) \\
SORT & \(\mathcal{O}(\frac{K^2log(K/\delta)}{1-H(p)})\) & \(\Omega(K^2+\frac{K^2log(K)}{D_\text{KL}(p\|1-p)})\) (Thm V.3) \\
\multirow{2}{*}{**Problem**} & \multicolumn{2}{c}{**Variable Length, Adaptive Sampling**} \\
 & \multicolumn{2}{c}{Matching Bound (Thm VI.1)} \\
OR & \(\Theta(\frac{K}{1-H(p)}+\frac{Klog(1/\delta)}{D_\text{KL}(p\|1-p)})\) \\
MAX & \(\Theta(\frac{K}{1-H(p)}+\frac{Klog(1/\delta)}{D_\text{KL}(p\|1-p)})\) \\
SEARCH & \(\Theta(\frac{log(K)}{1-H(p)}+\frac{log(1/\delta)}{D_\text{KL}(p\|1-p)})\) \\
SORT & \(\Theta(\frac{Klog(K)}{1-H(p)}+\frac{Klog(K/\delta)}{D_\text{KL}(p\|1-p)})\) \\
\end{tabular}


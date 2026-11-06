## Appendix

This appendix provides additional proofs, full algorithm pseudo-codes, and experimental details referenced in the main text. Unless stated otherwise, notation matches the main text.

### Contents

## A The MedianEst routine

### A.1 Bounding the mean via the median

In Section 2, we assumed that for each arm _k_, the learner is provided with an anchor point _c<sub>k</sub>_ satisfying \(|\mu_k-c_k|\le\sigma\). We can rigorously satisfy this assumption by estimating the median of the reward distribution.

Let _c_ be the true median of a random variable _X_ with mean \(\mu\) and variance bounded by \(\sigma^2\). By Cantelli’s inequality (the one-sided Chebyshev inequality), for any _a\>_0, we have:<tbc>

\(Pr(X-\mu\ge a)\le\frac{\sigma^2}{\sigma^2+a^2}.\)

<tbc>If the median is greater than the mean (\(c>\mu\)), we can substitute \(a=c-\mu\) to obtain:<tbc>

\(Pr(X\ge c)\le\frac{\sigma^2}{\sigma^2+(c-\mu)^2}.\)

<tbc>By the definition of the median, \(Pr(X\ge c)\ge\frac{1}{2}\). Combining these yields:

\(\frac{1}{2}\le\frac{\sigma^2}{\sigma^2+(c-\mu)^2}\Longrightarrow\sigma^2+(c-\mu)^2\le 2\sigma^2\Longrightarrow(c-\mu)^2\le\sigma^2.\)

Taking the square root gives \(|c-\mu|\le\sigma\). A symmetric argument using \(Pr(X\le c)\) applies when \(c<\mu\). Therefore, finding a point close to the true median naturally provides a valid anchor point _c<sub>k</sub>_ that is guaranteed to be at most \(O(\sigma)\) away from the true mean.

### A.2 Noisy binary search

Our goal is to find a threshold _x_<sub>_i_∗</sub> where the probability _p_<sub>_i_∗</sub> crosses \(\tau=1/2\). This exactly matches the MONOTONICNBS(\(\tau,\varepsilon'\)) framework \[9\], where the algorithm must find an \(\varepsilon'\)-good interval despite coins (thresholds) near the target being indistinguishable from it. As established by \[9\], for the median target \(\tau=1/2\), tolerance \(\varepsilon'\in(0,1/4)\), and failure probability \(\gamma\in(0,1/2)\), the MEDIANEST algorithm successfully identifies a valid index \(\hat{i}\) such that the interval \([Pr(X\le x_i),Pr(X\le x_{\hat{i}+1})]\) intersects the target window \((1/2-\varepsilon',1/2+\varepsilon')\) with probability at least \(1-\gamma\).

To achieve this, the total number of 1-bit queries used by the algorithm is bounded by the sample complexity:

\(M(n,\varepsilon',\gamma)=O\left(\frac{1}{(\varepsilon')^2}\left(logn+log^{2/3}nlog^{1/3}\frac{1}{\gamma}+log\frac{1}{\gamma}\right)\right).\)

\begin{tabular}{cc}
**Item** & **Page** \\
Appendix A: The MedianEst routine & 13 \\
Appendix B: Proofs for Section 2 (A 1-bit mean estimator) & 17 \\
Appendix C: Proofs for Section 3 (1-bit BAI algorithm and upper bound) & 24 \\
Appendix D: Proofs for Section 4 (Lower bound) & 38 \\
Appendix E: Detailed algorithms & 43 \\
Appendix F: Numerical experiment details & 44 \\
\end{tabular}


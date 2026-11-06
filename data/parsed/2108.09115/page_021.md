The recursion continues until each interval has less than log<sup>2</sup>(_n_) windows, after which all windows are covered.

We now summarize the approximation factor and the complexity of the query algorithm.

_Lemma_ 13 (Time Complexity)_. Let_ \(A,B\in\Sigma^n\)_. Then running time of the query phase is bounded by:_ \(\tilde{O}_\epsilon(n^{3/2+\epsilon})\).

_Proof._ Fix \(\tau\). By the complexity analysis of Step C, the total number of queries required to cover dense windows over all the recursion steps is \(\tilde{O}(t_\tau^{4/3})\).

On the \(\ell\)-th level of recursion, the number of intervals is \(t_\tau^{1/3+(\ell+1)\epsilon}\). For every interval, we pick at most log<sup>2</sup>_n_ sparse windows, and query all relevant windows. The number of relevant windows is \(\tilde{O}(t_\tau^{1-\ell\epsilon})\). Therefore, on the \(\ell\)-th level of recursion, the number of queries spent on sparse windows is \(t_\tau^{4/3+\epsilon}\). Since the number of levels of recursion is at most \(\frac{1}{\epsilon}+1\), the total number of queries spent on sparse windows is \(O(\frac{t_\tau^{4/3+\epsilon}}{\epsilon})\).

Computing \(\tau d\)-thresholded edit distance between pairs of windows requires time \(\tilde{O}(\tau^2d^2)\) (using our algorithm from Section 3). Therefore, the time complexity for a given \(\tau\) over all dense and sparse windows is \(\tilde{O}(\frac{t_\tau^{4/3+\epsilon}\tau^2d^2}{\epsilon})=\tilde{O}(\frac{n^{3/2+\epsilon}}{\epsilon^{7/4}})\).

Since, the number of choices of \(\tau\) is \(O(\frac{logn}{\epsilon})\) and the time to run the DP from Section 5.3 is \(O(\frac{1}{\epsilon}n^{3/2}logn)\) , the overall total time complexity is \(\tilde{O}(\frac{n^{3/2+\epsilon}}{\epsilon^{15/4}})\).

_Lemma_ 14 (Approximation)_. Let_ \(A,B\in\Sigma^n\)_. Let_ \(\mathcal{E}:\mathcal{A}\times\mathcal{B}\rightarrow\mathbb{R}^+\) _be the cost function produced during the query phase. Then with probability at least_ \(1-\frac{1}{n}\)_, we have:_

\(\mathrm{ED}(\mathcal{E})\le(7+\epsilon)\mathrm{ED}(A,B).\)

_Proof._ Note that if we can construct \(\mathcal{E}:\mathcal{A}\times\mathcal{B}\rightarrow\{0,\dots,d\}\) such that \(\mathrm{ED}(a,b)\le\mathcal{E}(a,b)\le 7\mathrm{ED}(a,b)\), then using the DP algorithm from Section 5.3 and employing Lemma 10, we get a 7+_o_(1) approximation for ED(_A,B_). Moreover, by Lemma 11, it is only required to compute all the edges of E with the above accuracy which an optimum low-skew monotone mapping \(\mu\) would use. Fix such a mapping \(\mu\).

We prove that for the first level of the recursion, for each interval \(I\in I_A\) it is either the case that there exists a sparse window _a_ such that: \(\mu(a)\in\mathcal{N}^{\mathcal{B}_\tau,\tau}(a)\), or that the covered dense windows provide a good approximation for the edges used by \(\mu\). Indeed, fix \(I\in I_A\), the proof proceeds by case analysis.

**Case 1:** Suppose that there exists \(\tau\) such that at least \(\epsilon\)-fraction of \(a\in I_\mathcal{A}\), are such that \(\mu(a)\in\mathcal{N}^{\mathcal{B}_\tau,\tau}(a)\) and _a_ is \(\tau\)-sparse.

In this case, with high probability the algorithm will eventually pick a window \(a\in I_\mathcal{A}\) such that \(\mu(a)\in\mathcal{N}^{\mathcal{B}_\tau,\tau}(a)\) and _a_ is \(\tau\)-sparse. Consider the set \(\widehat{I_{\mathcal{B}^\tau}}\) recorded by the algorithm. Since \(\mu\) is a low-skew mapping, one of the intervals \(I_\mathcal{B}\in\widehat{I_{\mathcal{B}^\tau}}\) is such that all the edges \((a,\mu(a))\) where \(a\in I_\mathcal{A}\), are such that \(\mu(a)\in I_\mathcal{B}\), and hence declared relevant. Therefore, in further iterations of the algorithm these edges will be assigned with the required approximation guarantee.

**Case 2:** Suppose that for all \(\tau\) at most \(\epsilon\)-fraction of \(a\in I_\mathcal{A}\), are such that \(\mu(a)\in\mathcal{N}^{\mathcal{B}_\tau,\tau}(a)\) and _a_ is \(\tau\)-sparse.

In this case we may fail to detect all the edges \((a,\mu(a))\), where \(\mu(a)\in\mathcal{N}^{\mathcal{B}_\tau,\tau}(a)\) and _a_ is \(\tau\)- sparse. Nevertheless, in that case, even if we map _all_ these edges to \(\perp\), we only lose a \((1+\epsilon)\) factor in the edit distance. As for the rest of the windows \(a\in I_\mathcal{A}\), we claim that with high probability for at least \(1-\epsilon\) of the windows _a_ we have: \(\mathcal{E}(a,\mu(a))\le 7\mathrm{ED}(a,\mu(a))\).


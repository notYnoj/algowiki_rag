### 2.3 Confidence sequence for the tail-integral estimator

Let _Z_<sub>1</sub>_,Z_<sub>2</sub>_,..._ be i.i.d. copies of the above estimator, each built from an independent reward sample and independent internal randomization. Define

\(\bar{Z}_n:=\frac{1}{n}\sum_{i=1}^nZ_i,\hat{\mu}_n:=c+\bar{Z}_n.\)

Since \(\bar{Z}_n\) estimates the clipped-variable mean and _c_ restores the shift, \(\hat{\mu}_n\) is our 1-bit estimate of \(\mu\).

**Theorem 5** (Confidence sequence for the tail-integral estimator)**.** _For every_ \(L\ge\sigma\) _and_ \(\gamma\in(0,1)\)_, with probability at least_ \(1-\gamma,|\hat{\mu}_n-\mu|\le\beta(n,\gamma,L)\) _for all_ \(n\ge 1\)_, where_

\(\beta(n,\gamma,L)=\frac{\sigma^2}{2L}+2\sqrt{\frac{3\alpha_L\sigma^2x_n(\gamma)}{n}}+\frac{\alpha_LLx_n(\gamma)}{n},\)

_with_ \(\alpha_L=1+\mathrm{log}(L/\sigma)\) _and_ \(x_n(\gamma):=\mathrm{log}\big(\pi^2(1+\lfloor\mathrm{log}_2n\rfloor)^2/(3\gamma)\big)\).

The first term in \(\beta(n,\gamma,L)\) is the clipping bias, the second is the main stochastic fluctuation term, and the third is the Bernstein range correction. The only price paid for time-uniformity is the stitched penalty \(x_n(\gamma)\), which is of order \(\mathrm{log}(1/\gamma)+\mathrm{loglog}(e+n)\). The proof of Theorem 5 is in Appendix B.4, and the sample-complexity inversion below is proved in Appendix B.5.

**Corollary 6** (Sample complexity of the tail-integral estimator)**.** _Fix a target accuracy_ \(\beta\in(0,\sigma)\) _and an error probability_ \(\gamma\in(0,1/3)\)_. By setting the clipping level_ \(L=\frac{2\sigma^2}{\beta}\)_, the tail-integral estimator_ \(\hat{\mu}_n\) _satisfies_ \(|\hat{\mu}_n-\mu|\le\beta\) _with probability at least_ \(1-\gamma\) _for sample sizes n satisfying:_

\(n=O\left(\frac{\sigma^2}{\beta^2}\mathrm{log}\frac{\sigma}{\beta}\left[\mathrm{log}\frac{1}{\gamma}+\mathrm{loglog}\left(e+\frac{\sigma}{\beta}\right)\right]\right).\)

**Remark 7** (Comparison with \[21\])**.** _In the finite-variance regime, \[21\] achieve the optimal rate_ \(O\left(\frac{\sigma^2}{\beta^2}\mathrm{log}\frac{\sigma}{\beta}\mathrm{log}\frac{1}{\gamma}\right)\)_. Our estimator matches this rate up to the lower-order_ loglog _factor needed for time-uniform validity. Structurally, their estimator partitions the domain into geometric regions and assigns fixed regional budgets, whereas ours samples a single randomized threshold from g<sub>L</sub> and yields an anytime confidence sequence. This avoids fixed regional allocations and makes the estimator compatible with adaptive bandit sampling and stopping rules._

## 3 1-bit BAI algorithm and upper bound

We now convert the time-uniform 1-bit mean confidence sequence from Section 2 into fixed- confidence BAI algorithms. Our algorithms follow the candidate-challenger interval logic of \[7\]. At each time, we construct arm-wise confidence intervals, select a candidate arm _h_, identify its strongest challenger \(\ell\), and stop once the candidate is certified to be \(\varepsilon\)-optimal. If the stopping condition is not met, the algorithm samples the more uncertain arm among \(\{h,\ell\}\), namely the one with the larger confidence radius.

The main new difficulty, compared with the unquantized setting, is the choice of the clipping level _L_. A larger clipping level reduces the bias of the 1-bit mean estimator but increases both its variance factor and its range term. Thus, the clipping level must be matched to the statistical resolution at which arms are being compared.

We present two approaches. The first is a fixed-clipping algorithm, which chooses a single clipping level tuned to the target accuracy \(\varepsilon\). This algorithm is simple and fully anytime, but it pays an additional mixed term in the sample complexity; see Theorem 8. The second is a phased adaptive- clipping algorithm, which gradually decreases the statistical resolution and chooses the clipping level accordingly. This removes the mixed term and yields the main gap-adaptive upper bound of the paper; see Theorem 10. Both algorithms are \((\varepsilon,\delta)\)-PAC, and their sample complexities are compared in Subsection 3.3.

Consider the non-trivial case \(0<\varepsilon\le\sigma\); the case \(\varepsilon>\sigma\) is trivial up to constants and can be handled by the initial phase alone. Define \(\widetilde{\Delta}_k:=\mathrm{max}\{\Delta_k,\varepsilon\}\), and \(\overline{\Delta_k}:=\mathrm{min}\{\widetilde{\Delta}_k,\sigma\}\).


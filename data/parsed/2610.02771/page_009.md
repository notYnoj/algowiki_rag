## 4 Lower bound

We now establish an information-theoretic lower bound for fixed-confidence best-arm identification under 1-bit set queries. The construction is closely related in spirit to the multiscale hard instances that arise in finite-variance 1-bit mean estimation \[21\]: in both settings, one-bit queries cannot avoid a logarithmic loss under only a second-moment assumption. Here, we formulate this obstruction directly in the BAI setting by embedding opposite perturbations of a multiscale one-dimensional distribution into a _K_-arm instance and combining it with a change-of-measure argument for adaptive stopping. The construction uses a symmetric distribution _P_<sub>0</sub> of mean zero and perturbed distributions _P_<sub>-</sub> and _P_<sub>+</sub> of means \(-\Delta\) and \(+\Delta\).

The base instance (_P_<sub>0</sub>_,P_<sub>-</sub>_,...,P_<sub>-</sub>) has _K_-1 equal suboptimal gaps \(\Delta\). For each \(i\ge 2\), changing only arm _i_ to _P_<sub>+</sub> changes the best arm to _i_. A change of measure forces sufficient queries to each such arm under the same base instance, and summing gives the factor _K_-1.

**Theorem 12** (_K_-arm worst-case lower bound for 1-bit BAI)**.** _Fix_ \(K\ge 2\), \(\sigma>0\), \(\delta\in(0,1/4)\)_, and_ \(\Delta\in(0,\sigma/4]\)_. There exists a K-arm instance_ \(\nu^{(0)}\) _with variance at most_ \(\sigma^2\) _for every arm and all suboptimal gaps equal to_ \(\Delta\)_, such that every 1-bit algorithm that is_ \(\delta\)_-correct for exact BAI over the stated instance class satisfies_

\(\mathbb{E}_{\nu^{(0)}}[\tau]\ge c(K-1)\frac{\sigma^2}{\Delta^2}\mathrm{log}\frac{\sigma}{\Delta}\mathrm{log}\frac{1}{\delta}\)

_for an absolute constant c\>_0_. The same bound holds for algorithms that are_ \((\varepsilon,\delta)\)_-PAC over this class when_ \(0<\varepsilon<\Delta/2\).

All base and alternative distributions admit the same anchor _c<sub>k</sub>_=0, so the bound persists when valid anchors are supplied. The construction, uniform one-query KL bound, and adaptive change- of-measure proof appear in Appendices D.1-D.3. On the equal-gap base instance, \(H_\mathrm{gap}=K(1+\mathrm{log}(\sigma/\Delta))\sigma^2/\Delta^2\). When \(\delta\le 1/K\), \(\mathrm{log}(1/\delta)\) and \(\mathrm{log}(K/\delta)\) are equivalent up to constants. Hence the expected lower bound matches the leading _K_, gap, and confidence dependence of the high- probability phased upper bound, up to lower-order iterated logarithms. This worst-case comparison does not characterize the optimal expected complexity on every instance.

## 5 Numerical experiments

### 5.1 1-bit mean estimation

We compare our tail-integral estimator proposed in Section 2 against the baseline of \[21\] in the finite-variance regime. The experiment has two goals: first, to compare the empirical mean absolute error (MAE) of the two estimators; second, to verify the qualitative behavior predicted by Theorem 5, namely that the error is governed by a decaying stochastic term together with a deterministic bias term induced by clipping/truncation.

Detailed calibration and setup are given in Appendix F.1; Appendix F.2 compares variances of the signed estimates. Figure 1 illustrates the MAE relative to the number of 1-bit queries. While both estimators show the expected _O(n_<sup>-1/2</sup>) decay in the Gaussian case, our estimator consistently<tbc>

Normal
Student-t (df=5)
Exponential
100
10-1
10-2
10-3
102
104
106
102
104
106
102
104
106
Samples n
Samples n
Samples n
Our MAE
O(1/vn)
True bias (Ours)
Lau-Scarlett MAE
Theoretic bias upper bound
True bias (Lau-Scarlett)

Figure 1: Mean absolute error \(\mathbb{E}|\hat{\mu}_n-\mu|\) over the number of 1-bit queries _n_ for our estimator and the estimator of \[21\] (mean \(\pm\sigma\) over runs). For readability, bias lines below 10<sup>-3</sup> are not shown.


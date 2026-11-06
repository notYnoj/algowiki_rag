**Case 2, Example 1.**<tbc>

\(\widetilde{G}(\kappa,\xi)(x,\theta)=0_{2\times 2}.\)

<tbc>**Case 2, Example 2.**<tbc>

\(\widetilde{G}(\kappa,\xi)(x,\theta)=\sqrt{\left(2+\mathrm{cos}\theta\right)\left(3+\mathrm{cos}\theta\right)h(x)k(x)}\otimes J.\)

<tbc>**Numerical verification of the Conjecture**<tbc>

<tbc>Let

\(G_n:=G(A_n,B_n)\in\mathbb{C}^{d_n\times d_n},d_n=\mathrm{size}(G_n).\)

We test whether the empirical eigenvalue distribution of {_G<sub>n</sub>}<sub>n</sub>_ converges to the distribution induced by the candidate symbol \(\widetilde{G}(\kappa,\xi)(x,\theta)\) defined in Section 9.2.4. The comparison follows the standard rearrangement strategy.

**1. Sampling the symbol.** Evaluate \(\widetilde{G}(\kappa,\xi)\) on a tensor grid \(\{x_j\}_{j=1}^{M_x}\subset[0,1]\), \(\{\theta_i\}_{i=1}^{M_\theta}\subset[-\pi,\pi]\) with a total number of \(M_x\times M_\theta\simeq 2000\) samples. For each point \((x_j,\theta_i)\) compute the _r_ eigenvalues of the function; then merge and sort in non-decreasing order all the computed values. This yields the empirical quantile function of the eigenvalues.<tbc>

**2. Eigenvalue computation.** Matrices _A<sub>n</sub>,B<sub>n</sub>_ are generated for \(n\in\{40,80,160,320\}\), and eigenvalues are ordered in non-decreasing order, to obtain the quantile spectral distribution function of {_G<sub>n</sub>}<sub>n</sub>_.<br>
We also record \(\lambda_\mathrm{min}(G_n)\), \(\lambda_\mathrm{max}(G_n)\) and the condition number cond<sub>2</sub>(_G<sub>n</sub>_) for later stability analysis.

**3. Quantile plot matching.** For each _n_ we plot the sorted eigenvalues \(\left(\lambda_i(G_n)\right)\) against the corresponding rearranged eigenvalues of the sample values of \(\widetilde{G}\). A superposition of the two plots for growing values of _n_ gives an experimental indication of the asymptotic convergence of the empirical spectral distribution of {_G<sub>n</sub>}<sub>n</sub>_ to that of the symbol.<tbc>

**4. Support analysis.** To estimate the measure of the zero set \(\{(x,\theta):\widetilde{G}=0\}\), we count the fraction of eigenvalues below the threshold 0.1 compared to the matrix size; the value is an estimate of the complement of the predicted measure of the support as _n_ grows.

All tests for this section are run on an Intel Core Ultra 7 155H CPU (22 threads, 30.9 GiB RAM) under Ubuntu 24.10, Linux 6.11.0-29, with Python 3.12.7, NumPy 1.26.4 and SciPy 1.13.1 linked against OpenBLAS.

**Remark 9.2 (Measure-theoretic meaning of the rearrangement test)** _As anticipated implicitly, the comparison of sorted eigenvalues versus the sorted eigenvalues of the sampled symbol has a precise measure-theoretic foundation based on the quantile approximation theory \[22\]. For completeness, we report the construction in \[22\] for the unilevel setting d_=1_; the multilevel case is analogous. Let r denote the size of_<tbc>


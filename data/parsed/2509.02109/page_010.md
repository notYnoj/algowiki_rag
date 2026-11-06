<tbc>We complement the stability bounds of Proposition 3.1 and Proposition 3.2 with an empirical study. We fix _K_=3, _d_=2, vary the sample size _n_ between 10<sup>3</sup> and \(2\cdot 10^4\), and for each _n_ run 40 repetitions of EM with 200 iterations (with _k-means++_ initialisation), noting the resulting estimates \(\hat{\mu}_n\) and \(\hat{\nu}_n\). Three regimes of component separation (low, medium, high) are considered, controlled by a scale parameter \(\sigma\) applied to the covariances. The mixtures \(\mu\), \(\nu\) are fixed, and we provide a visualisation in Appendix A.3. For each _n_, we report the median error and interquartile range across repetitions. Fig. 2a shows \(\mathrm{MW}_2^2(\hat{\mu}_n,\mu)\). With medium and high component separation, the error decreases regularly with _n_, while with low separation it remains flat, indicating that EM does not improve the estimation significantly in this regime. Fig. 2b shows the relative error \(|\mathrm{MW}_2^2(\hat{\mu}_n,\hat{\nu}_n)-\mathrm{MW}_2^2(\mu,\nu)|/\mathrm{MW}_2^2(\mu,\nu)\). Medium and high separation again yield decay with _n_, while low separation plateaus. The results above translate parameter error rates of EM into rates for \(\mathrm{MW}_2^2\), but do not specify a universal value. In well-separated special cases, EM is known to achieve a rate of O(_n_<sup>-1/2</sup>) (see \[KC20\] for spherical covariances). When separation is weak, EM appears not to converge reliably, hence the \(\mathrm{MW}_2^2\) error does not decrease.

## 3.3 Minimisation of \(\mathrm{EM}-\mathrm{MW}_2^2\): Local Optima and Weight Fixing

In practice, the minimisation of the energy \(X\longmapsto\mathrm{MW}_2^2(F_X^T(\theta_0),\nu)\) for some initialisation \(\theta_0\in\Theta\) and a target GMM \(\nu\) comes with numerous challenges. The first hurdle is the "outer" minimisation of the \(\mathrm{MW}_2^2\) cost. To illustrate this difficulty, we begin with a study of the simpler energy \(\mu\longmapsto\mathrm{W}_2^2(\mu,\nu)\) for a fixed (discrete) measure \(\nu\in\mathcal{P}_2(\mathbb{R}^d)\) with respect to the weights and support of the discrete measure \(\mu=\sum_{i=1}^na_i\delta_{x_i}\). This setting corresponds to the optimisation of \(\mathrm{MW}_2^2\) with known covariances, and thus highlights practical bottlenecks for the minimisation of the complete energy at stake, \(\mathrm{EM}-\mathrm{MW}_2^2\). The objective of this section is to provide a theoretical rationale for fixing the mixture weights in practical applications, which is to say using Algorithm 2 instead of standard EM (Algorithm 1).

### Local Minima of the Discrete 2-Wasserstein Distance.

We focus on a particular instance of the minimisation of \(\mu\longmapsto\mathrm{W}_2^2(\mu,\nu)\), and show the existence of a strict local minimum. We<tbc>

\begin{tabular}{cc}
\(\mu\). & Assume "convergence rates" on the parameter estimations for \(k\in\unknown 1,K\unknown\): \\
\(\mathbb{E}\left[\|w-\hat{w}\|_1\right]\le\rho_w\), \(\mathbb{E}\left[\mathrm{W}_2^2(\mathcal{N}(\hat{m}_k,\hat{\Sigma}_k),\mathcal{N}(m_k,\Sigma_k))\right]\le\rho_\mathcal{N}\), \\
\end{tabular}

\begin{tabular}{cc}
\(\mathbb{E}\left[\mathrm{MW}_2^2(\hat{\mu},\mu)\right]\le\rho_\mathcal{N}+\frac{\rho_w}{2}\mathrm{max}_{k,\ell}\mathbb{E}\left[\mathrm{W}_2^2(\mathcal{N}(\hat{m}_k,\hat{\Sigma}_k),\mathcal{N}(m_\ell,\Sigma_\ell))\right].\) & (17) \\
\end{tabular}

\begin{tabular}{cc}
\(\text{\textbf{Proposition 3.2.} For}i\in\{0,1\}\), consider GMM parameters \((\hat{w}_i,\hat{m}_i,\hat{\Sigma}_i)\in\triangle_{K_i}\times\mathbb{R}^{K_i\times d}\times S_d^{++}(\mathbb{R})^{K_i}\) of a GMM \(\hat{\mu}_i\) as estimators of \((w_i,m_i,\Sigma_i)\in\triangle_{K_i}\times\mathbb{R}^{K_i\times d}\times S_d^{++}(\mathbb{R})^{K_i}\) which are parameters of a target GMM \(\mu_i\). Assume that the means and covariances are bounded, namely that there exists _R<sub>m</sub>\>_0, \(R_\Sigma>0\) such that: \\
\(\forall i\in\{0,1\},\forall k\in\unknown 1,K_i\unknown,\|m_k^{(i)}\|_2\le R_m,\|\hat{m}_k^{(i)}\|_2\le R_m,\sqrt{\mathrm{Tr}\Sigma_k^{(i)}}\le R_\Sigma,\sqrt{\mathrm{Tr}\hat{\Sigma}_k^{(i)}}\le R_\Sigma.\) \\
\end{tabular}

\begin{tabular}{cc}
\(\text{Further assume "convergence rates" on the parameter estimations}k\in\unknown 1,K_i\unknown\): & \\
\(\forall i\in\{0,1\},\mathbb{E}\left[\|w_i-\hat{w}_i\|_1\right]\le\rho_w\), \(\mathbb{E}\left[\|m_k^{(i)}-\hat{m}_k^{(i)}\|_2\right]\le\rho_m\), \(\mathbb{E}\left[d_\mathrm{BW}\left(\Sigma_k^{(i)},\hat{\Sigma}_k^{(i)}\right)\right]\le\rho_\Sigma\), \\
\end{tabular}

\begin{tabular}{cc}
\(\mathbb{E}\left[\left|\mathrm{MW}_2^2(\hat{\mu}_0,\hat{\mu}_1)-\mathrm{MW}_2^2(\mu_0,\mu_1)\right|\right]\le 8R_m\rho_m+8R_\Sigma\rho_\Sigma+8(R_m^2+R_\Sigma^2)\rho_w.\) & (18) \\
\end{tabular}


## F.2 Variance comparison with Lau-Scarlett

The bands in Figure 1 describe absolute errors and do not directly measure the variance of the signed estimates. To compare dispersion, we use the signed _n_-sample estimates from the same _R_=1000 independent repetitions and the same calibration \(\mu=1\), \(\sigma=1\), _c_=0, _L=t_=5. For either estimator, compute

\(\widehat{\mathrm{Var}}(\hat{\mu}_n)=\frac{1}{R-1}\sum_{r=1}^R\left(\hat{\mu}_n^{(r)}-\bar{\mu}_n\right)^2,\bar{\mu}_n=\frac{1}{R}\sum_{r=1}^R\hat{\mu}_n^{(r)}.\)

2 reports its square root. These values are the Monte Carlo results reported in the rebuttal.

Across these twelve configurations, the baseline’s standard deviation is 1.924-2.090 times ours, corresponding to approximately 3.70-4.37 times the empirical variance. Under this calibration our estimator therefore has smaller dispersion as well as smaller clipping bias. This comparison concerns the implemented fixed-budget estimators on these distributions; it establishes neither a universal variance ordering nor a sample-complexity rate separation. Variance is computed about each estimator’s empirical mean and is distinct from mean squared error, which also includes bias.

## F.3 1-bit best-arm identification

### Experiment Setting

The empirical performance of the proposed 1-bit best-arm identification algorithms was evaluated against the full-feedback UGAPE baseline across three distinct environments. For all experiments, we evaluate a _K_=5 armed bandit setting with a target accuracy of \(\epsilon=0.05\) and a maximum query cap of _N_=20000. To thoroughly analyze the sample complexity and safety of each approach, the confidence parameter \(\delta\) is varied over 10 logarithmically spaced values from 0.01 to 0.5. The results are averaged over 5000 independent Monte Carlo runs for each configuration.

### BAI Environments and Distributions

The experiments utilize three distinct reward environments, all bounded by a global variance proxy of \(\sigma=0.5\):

• **Bernoulli**: The reward distributions are Bernoulli with means \(\mu=[0.5,0.4,0.4,0.4,0.4]\). This represents a uniform gap setting where \(\Delta_k=0.1\) for all suboptimal arms. The arm-wise anchors are _c<sub>k</sub>_=0.5 for all arms and satisfy the localization condition.<tbc>

• **Normal**: The rewards follow a Gaussian distribution with linearly decaying means \(\mu=[0.5,0.4,0.3,0.2,0.1]\). The arm standard deviations are set to \(\sigma_k=0.5\), and the anchors are uniformly set to _c<sub>k</sub>_=0.<tbc>

• **Student-t**: The rewards are drawn from a heavy-tailed Student-t distribution with degrees of freedom _df_=3. The distributions are scaled by a factor of \(\sigma\sqrt{(df-2)/df}\) so that the true variance is precisely \(\sigma^2\). The arm means are \(\mu=[0.5,0.4,0.3,0.2,0.1]\) and the anchors are _c<sub>k</sub>_=0.<tbc>

\begin{tabular}{ccccc}
Distribution & _n_ & Std. (ours) & Std. (Lau-Scarlett) & Ratio (LS/ours) \\
Normal & 10<sup>4</sup> & 0.02515 & 0.04917 & 1.955 \\
 & 10<sup>5</sup> & 0.007806 & 0.01624 & 2.081 \\
 & 10<sup>6</sup> & 0.002472 & 0.005166 & 2.090 \\
 & 10<sup>7</sup> & 0.0007860 & 0.001537 & 1.956 \\
Student-_t_(5) & 10<sup>4</sup> & 0.02532 & 0.04995 & 1.973 \\
 & 10<sup>5</sup> & 0.007799 & 0.01585 & 2.033 \\
 & 10<sup>6</sup> & 0.002452 & 0.005002 & 2.040 \\
 & 10<sup>7</sup> & 0.0007863 & 0.001557 & 1.980 \\
Exponential & 10<sup>4</sup> & 0.02469 & 0.04917 & 1.992 \\
 & 10<sup>5</sup> & 0.007285 & 0.01506 & 2.067 \\
 & 10<sup>6</sup> & 0.002413 & 0.004916 & 2.037 \\
 & 10<sup>7</sup> & 0.0007716 & 0.001485 & 1.924 \\
\end{tabular}

2: Empirical standard deviations of signed estimates over 1000 repetitions, under the common calibration. Ratios above one indicate greater dispersion for the Lau-Scarlett baseline.


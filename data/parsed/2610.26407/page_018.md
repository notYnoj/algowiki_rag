<tbc>_Fair comparison._ We use three measures to ensure each method is on equal footing. First, within a replication, all methods have the same true means and the outcomes come from the same stream, so the _n_th observation of an item _i_ is identical across methods. Second, to ensure fairness across Bayesian and frequentist methods, the Bayesian methods all use the same uninformative (Jeffreys) prior for each distribution family: the flat prior for the Gaussian mean, \(\propto 1/\theta\) for the exponential mean, Beta(1/2,1/2) for Bernoulli, and the flat prior on \(log\theta\) for the lognormal mean (Jeffreys 1946). Third, since some benchmark methods require a warm-up, each algorithm receives a warm-up of _n_<sub>0</sub>=3 samples per item.

_Benchmarks._ We compare against the following benchmarks, all of which aim to maximize PCS unless otherwise specified.

- _Gaussian-Specific from the Ranking and Selection Literature:_ For _k_=1 AOAP from Peng et al. (2018) and for _k\>_1 AOAm from Zhang et al. (2023) and EMIp from Liu et al. (2024). For the top-_k_ EOC setting, EOC-m from Gao and Chen (2015).<tbc>

- _General k_=1: Top two Thompson sampling (TTTS) of Russo (2020) with \(\beta=1/2\) and its variant that does not rely on a tuning parameter, TTTS-IDS from Qin and You (2026). BOLD (Chen and Ryzhov 2023).<tbc>

- _General k\>_1 _from the Best Arm(s) Identification Literature:_ The top-_k_ Thompson sampling approaches TS-PPS-IDS and TS-KKT(.5)-IDS from You et al. (2023), Qin and You (2026), KL-LUCB from Kaufmann and Kalyanakrishnan (2013), and gap-e from Bubeck et al. (2013).<tbc>

**-** _Uniform:_ Equal allocation across all items.

_Metrics._ Since most benchmarks aim to maximize PCS, we report both EOC and PCS, estimated from the 10,000 replications. Consistent with previous literature and the discussion in the introduction, the two are closely aligned. Since none of the methods other than gap-e depend on the total budget, we have their EOC and PCS for every fixed budget up to 1,000\(\cdot I\).

## 5.2. Results

To keep the paper focused, we report PCS at the largest budget (1,000\(\cdot I\)), and for EOC, we report performance curves across budgets for the Gaussian setting. The PCS and EOC performance curves for all settings are in Appendix D.

\begin{tabular}{cccc}
Likelihood \(Y_{i,n}|\theta_i\) & \multicolumn{3}{c}{Distribution of true means \(\theta_i\)} \\
\(N(\theta_i,1)\) & Unif(-2,2) & Unif(-1,1) & Unif(-0.5,0.5) \\
\(Exp(1/\theta_i)\) & Unif(1,9) & Unif(1,5) & Unif(1,3) \\
\(Bern(\theta_i)\) & Unif(0.05,0.95) & Unif(0.2,0.8) & Unif(0.35,0.65) \\
\(Lognormal(log\theta_i-1/2,1)\) & Unif(1,9) & Unif(1,5) & Unif(1,3) \\
\end{tabular}

** 1** The four likelihood families and the three distributions used to generate the true means.


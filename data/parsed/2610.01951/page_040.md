<tbc>hits this cap. The only cap hits occur in the unpenalized ablation, where the cap-hit rate is explicitly reported.

For a scalar statistic _Z_ over _R_ independent runs, the empirical standard error of the mean is

\(\widehat{\mathrm{s}}\mathrm{e}(\overline{Z})=\left(\frac{1}{R(R-1)}\sum_{r=1}^R(Z^{(r)}-\overline{Z})^2\right)^{1/2}.\)

Bootstrap percentile 95% confidence intervals use 1000 resamples with an independent bootstrap seed 314159. The finite-confidence scaling figure uses bootstrap percentile bands for the empirical mean; the \(\beta\)-sensitivity figure uses \(\pm 1.96\) empirical standard errors.

### Metrics

The main predictor-agreement metric is the absolute relative error<tbc>

\(\mathrm{ARE}(\mu,\beta,\delta)=\left|\frac{\overline{\tau_\delta}}{t_\mathrm{pred}(\mu,\beta,\delta)}-1\right|,\)

<tbc>where \(\overline{\tau_\delta}\) is the Monte Carlo mean stopping time. We also record the median, 10th, 90th, and 95th percentiles of \(\tau_\delta\), the empirical error rate, the cap-hit rate, and final allocation diagnostics. For the guard, let

\(G_\mathrm{tot}=\sum_{t=K}^{\tau_\delta-1}\mathbf{1}\{\mathrm{min}_iN_{t,i}<\sqrt{t/K}\}.\)

We report both \(G_\mathrm{tot}/\tau_\delta\) and the theory-facing normalization \(G_\mathrm{tot}/\sqrt{K\tau_\delta}\).

### Aggregate results

2 reports predictor agreement over the full \(3\times 3\times 5\) grid.  3 summarizes the stress, guard, and penalty-ablation diagnostics.  4 gives the equal-close guard- overhead family.

### \(\beta\)-sensitivity numerical table

5 gives the numerical values underlying the right-hand panel of Figure 2. The empirical mean tracks the nonmonotone dependence of \(T_\beta^\star(\mu)\) on the leader sampling probability.

## H.2 Idealized population-allocation reference

To provide a finite-sample scale check without turning the paper into a broad benchmarking study, we run an idealized population-allocation reference. It computes the Bernoulli characteristic-time allocation \(w^\star(\mu)=\mathrm{argmax}_w\mathrm{min}_{j\neq i^\star} I_j(w)\) from the true means, then deterministically C-tracks that allocation and uses the same GLR statistic and threshold \(c(t,\delta)\) as the EB-TCI runs. This construction is motivated by the allocation principle underlying Track-and-Stop \[4\], but it is not an empirical Track-and-Stop implementation: the reference is given population information unavailable to a learning algorithm and never recomputes an empirical optimal allocation.

\begin{tabular}{ccccc}
Variant & Settings & Median ARE & Mean ARE & Max ARE \\
Guarded penalized & 45 & 1.39% & 1.53% & 3.86% \\
Unguarded penalized & 45 & 1.60% & 1.66% & 4.20% \\
\end{tabular}

\begin{tabular}{ccccc}
Variant & Reps & Mean & Median & 95th percentile \\
Unguarded penalized & 600 & 105,593 & 104,918 & 134,140 \\
Guarded penalized & 600 & 104,022 & 103,743 & 130,792 \\
Unpenalized ablation & 500 & 188,036 & 108,036 & 700,000 \\
\end{tabular}

2: Absolute relative error between empirical mean stopping time and _t_<sub>pred</sub> over the complete evaluation grid. No penalized evaluation setting hits the simulation cap or yields a Monte Carlo misidentification.

3: Stress-test stopping-time summaries on TIE-CLOSE4 with \(\beta=0.5\) and \(\delta=10^{-8}\). The unpenalized ablation hits the 700,000-round cap in 12.8% of runs.


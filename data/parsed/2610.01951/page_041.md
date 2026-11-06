6 compares this reference with the closest guarded EB-TCI point from the \(\beta\)-sweep. We use \(\beta=0.4\) because it is the closest grid value to the optimal best-arm fractions \(\alpha^\star=0.357\) on CLUSTER-CLOSE5 and \(\alpha^\star=0.367\) on TIE-CLOSE4. Because the methods use different best-arm fractions and the reference knows \(\mu\), the table is a diagnostic comparison of finite-sample scales, not evidence for an algorithm ranking.

## H.3 Supplementary figures

Figure 3 reports the guard diagnostics that are summarized in the main text. The left panel compares stopping-time survival curves on the hard stress instance. The right panel reports the normalized guard overhead across the equal-close family.

Figure 4 contains the remaining diagnostics. The penalty ablation shows the effect of removing log_N<sub>t,j</sub>_ from the challenger index. The allocation panel compares final empirical sampling fractions with the optimal population weights \(w^\beta\).

\begin{tabular}{cccccc}
Instance & _K_ & Reps & Mean \(\tau_\delta\) & Mean \(G_\mathrm{tot}/\tau_\delta\) & 95th perc. \(G_\mathrm{tot}/\sqrt{K\tau_\delta}\) \\
EQUAL-CLOSE4 & 4 & 200 & 92,922 & 0.0058% & 1.80% \\
EQUAL-CLOSE8 & 8 & 200 & 196,872 & 0.0065% & 1.80% \\
EQUAL-CLOSE12 & 12 & 100 & 301,114 & 0.0069% & 1.89% \\
EQUAL-CLOSE16 & 16 & 50 & 417,489 & 0.0062% & 1.41% \\
\end{tabular}

\begin{tabular}{ccccc}
Instance & \(\beta\) & Mean \(\tau_\delta\) & _t_<sub>pred</sub> & Relative error \\
CLUSTER-CLOSE5 & 0.2 & 34,151 & 33,901 & 0.74% \\
CLUSTER-CLOSE5 & 0.3 & 28,757 & 29,267 & -1.74% \\
CLUSTER-CLOSE5 & 0.4 & 29,141 & 29,001 & 0.48% \\
CLUSTER-CLOSE5 & 0.5 & 31,390 & 31,334 & 0.18% \\
CLUSTER-CLOSE5 & 0.6 & 36,063 & 36,505 & -1.21% \\
CLUSTER-CLOSE5 & 0.7 & 45,304 & 46,458 & -2.48% \\
CLUSTER-CLOSE5 & 0.8 & 65,735 & 67,856 & -3.13% \\
TIE-CLOSE4 & 0.2 & 102,704 & 102,907 & -0.20% \\
TIE-CLOSE4 & 0.3 & 88,998 & 88,819 & 0.20% \\
TIE-CLOSE4 & 0.4 & 85,348 & 87,269 & -2.20% \\
TIE-CLOSE4 & 0.5 & 92,510 & 93,342 & -0.89% \\
TIE-CLOSE4 & 0.6 & 105,470 & 107,680 & -2.05% \\
TIE-CLOSE4 & 0.7 & 134,493 & 135,786 & -0.95% \\
TIE-CLOSE4 & 0.8 & 191,672 & 196,628 & -2.52% \\
\end{tabular}

4: Guard overhead on the equal-close family with \(\beta=0.5\) and \(\delta=10^{-6}\). The mean guard- round fraction is shown as a percentage.

5: \(\beta\)-sensitivity with \(\delta=10^{-6}\), the guarded penalized rule, and 200 replications per point.


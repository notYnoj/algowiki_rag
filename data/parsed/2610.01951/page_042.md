\begin{tabular}{ccccccc}
Instance & Method & \(\beta\) or \(\alpha^\star\) & Reps & Mean \(\tau_\delta\) & SE & 95th perc. \\
CLUSTER-CLOSE5 & Guarded EB-TCI & 0.400 & 200 & 29,141 & 401 & 38,530 \\
CLUSTER-CLOSE5 & Idealized allocation tracking & 0.357 & 200 & 34,808 & 411 & 43,978 \\
TIE-CLOSE4 & Guarded EB-TCI & 0.400 & 200 & 85,348 & 1,107 & 111,139 \\
TIE-CLOSE4 & Idealized allocation tracking & 0.367 & 200 & 102,085 & 1,373 & 132,011 \\
\end{tabular}

Exploration guard diagnostics
Stopping-time tail, tie-close4, 6 = 10-8
Normalized guard overhead, 6 = 10-6
100
unguarded guarded
4.0
3.5
10-1
3.0
Empirical survival probability
2.5
100 x Gtot/V KTs
2.0
10-2
1.5
1.0
0.5
50000
100000
150000
200000
4
8
12
16
Stopping time
Number of arms K

Penalty ablation on tie-close4, β = 0.5, 6 = 10-8
100
penalized, unguarded penalized, guarded unpenalized ablation
cap
10-1
Empirical survival probability
10-2
100000 200000 300000 400000 500000 600000 700000 Stopping time

Post-stabilization allocation diagnostics, β = 0.5, 6 = 10-8
Mean final fractions versus oracle weights
Run-level allocation error
0.5
sep5
0.20
cluster-close5
0.4
tie-close4
0.15
Empirical final fraction
0.3
0.10
0.2
0.1
0.05
0.0
0.0
0.0
0.1
0.2
0.3
0.4
0.5
sep5
cluster
tie
Oracle weight w
8

6: Idealized population-allocation reference at \(\delta=10^{-6}\). The population-benchmark rows use the population-optimal Bernoulli allocation and the same GLR threshold as the EB-TCI experiments. No run in this table hits the cap or yields a Monte Carlo misidentification.

Figure 3: Exploration guard diagnostics. Left: empirical survival curves on TIE-CLOSE4 with \(\beta=0.5\) and \(\delta=10^{-8}\), using 600 replications per penalized variant. Right: normalized guard overhead on the equal-close family with \(K\in\{4,8,12,16\}\) and \(\delta=10^{-6}\).

(a) Penalty ablation on the equal-close stress instance.

(b) Final allocation diagnostics.

Figure 4: Additional diagnostics. Left: the unpenalized challenger removes log_N<sub>t,j</sub>_ but leaves the stopping rule and all other details unchanged. Right: final sampling fractions for the guarded rule with \(\beta=0.5\) and \(\delta=10^{-8}\), compared with the optimal population weights.


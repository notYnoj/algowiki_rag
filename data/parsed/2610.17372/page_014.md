## 7.6 Performance: Runtime and Memory Scaling

We evaluate computational performance by measuring end- to-end runtime and peak memory usage as a function of constellation size _n_ and number of snapshots _M_. Runtime is dominated by repeated tuple updates in Procedure 3<tbc>

<tbc>and run-detection operations in Procedure 1, while peak memory is driven by storing connectivity strings \(CS_{pq}^{(R)}\) and intermediate candidate tuples prior to compression by Procedure 4. Each configuration was executed 5 times; we report mean \(\pm\) standard deviation of wall-clock runtime. Peak memory is reported as peak resident set size (RSS) on the host (and peak GPU memory allocation when GPU kernels are enabled).

At mega-constellation scale, we construct temporal con nectivity primitives \(CS_{pq}^{(R)}\) globally, but compute shortest- time routes only for sampled source-destination pairs (or sampled sources) using the same hop-admissibility rules. Full APSP materialization is evaluated up to _n_=16384 on our platform due to path-matrix memory requirements.

Worst-case vs. observed scaling: Theorem 2 gives a worst- case bound of _O(M_<sup>2</sup>_n_<sup>3</sup>). Empirically, runtime can be substantially lower because Procedure 3 prunes candidates:<tbc>

\begin{tabular}{ccccccc}
**Interval** & **Degree** & **Persistent** & **New** & **Dropped** & **Jaccard** _J_ & **Turnover (%)** \\
1 & 6 & - & - & - & - & - \\
2 & 5 & 3 & 2 & 3 & 0.375 & 62.5 \\
3 & 7 & 4 & 3 & 1 & 0.500 & 50.0 \\
4 & 5 & 3 & 2 & 4 & 0.333 & 66.7 \\
**Mean** & 5.75 & 3.33 & 2.33 & 2.67 & 0.403 & 59.7 \\
**Std** & 0.96 & 0.58 & 0.58 & 1.53 & 0.084 & 8.7 \\
**Max** & 7 & 4 & 3 & 4 & 0.500 & 66.7 \\
\end{tabular}

\begin{tabular}{ccccc}
_R_ (km) & Mean %Found & Mean %Missing & Mean _J<sub>E</sub>_ & Peak %Missing \\
659 & 18.7 & 19.1 & 0.68 & 32.4 \\
1319 & 11.3 & 11.0 & 0.79 & 21.5 \\
1500 & 8.6 & 8.4 & 0.84 & 17.2 \\
1700 & 6.1 & 6.0 & 0.88 & 12.9 \\
\end{tabular}

\begin{tabular}{cc}
**Metric** & **Definition / Interpretation** \\
\(\pi_1\) & Duty cycle: \(\pi_1=\frac{1}{M}\sum_tCS[t]\). Higher values imply greater availability. \\
\(\bar{\ell}\) & Mean run length of ones (contact persistence). Higher values imply fewer reconnection events. \\
\(\ell_{95}\) & 95th percentile run length; captures long feasibility windows relevant when _t<sub>qr</sub>\>_1. \\
_g_<sub>95</sub> & 95th percentile gap length (consecutive zeros); large gaps imply substantial waiting under misalignment. \\
\end{tabular}

Temporal Edge Density Over One Orbital Period
4
3
Average degree (per snapshot)
2
1
R=659 km
R=1500 km
R=1319 km
R=1700 km
0
0
20
40
60
80
100
Time into orbit (minutes)

TABLE 4

Interval-wise neighborhood dynamics for the focus node (from Fig. 4).

TABLE 5

Global link churn over one orbit.

Fig. 7. Temporal edge density over one orbital period. Snapshot-wise average degree for \(R\in\{659,1319,1500,1700\}\) km over a full orbital window \(T=M\tau\). Larger _R_ increases baseline connectivity and contact persistence; smaller _R_ yields sharper periodic peaks and deeper troughs due to tighter geometric feasibility.

TABLE 6

Connectivity-string run-length metrics (computed from Fig. 6).


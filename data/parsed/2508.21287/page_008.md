<tbc>respectively. While variability is observed across seeds, the minimum speedup remains above the VF2 baseline in nearly all cases. The few low-minimum cases (e.g., heavy-hex with 20-node patterns) arise when the pattern size is sufficiently small that GPU launch overhead dominates the runtime.

We additionally compare \(\Delta\)_-Motif_ against GSI where results are available. On smaller instances, such as the 1600-node square grid with 20-node patterns, the two methods show comparable average performance, measured by the mean speedup \(T_\mathrm{GSI}/T_{\Delta\text{-}Motif}\), with maximum speedups of up to \(17\times\). As problem difficulty increases, the performance gap widens. For the 3600-node square grid with 20-node patterns, \(\Delta\)_-Motif_ is on average \(2\times\) faster than GSI, with maximum speedups reaching \(63\times\). For larger patterns, GSI fails to complete within a reasonable time window, while \(\Delta\)_-Motif_ continues to scale effectively.

Overall, the results show that \(\Delta\)_-Motif_ consistently outperforms VF2 and increasingly outperforms GSI as problem size and complexity grow, with the largest benefits realized on large data graphs and medium-to-large pattern sizes that maximize GPU utilization. We also note that pattern graph decomposition accounts for less than 1% of the total runtime in all cases, with end-to-end execution completing in just a few seconds.

## B. Performance Impact of Motif Selection

The experiments in Fig. 3 assess how different motif selection strategies influence runtime, speedup, and decomposition behavior on two data graphs. Each experiment uses 60- node random pattern graphs and compares VF2 with \(\Delta\)_-Motif_ executed on CPU, on GPU, and on GPU with data preparation time excluded (marked as GPU<sup>∗</sup>).<sup>1</sup>. Bars show mean values over 50 random seeds, with error bars representing the minimum and maximum values. The three subplot columns present total runtime, speedups over VF2, and the average number of iterations for pattern decomposition using the chosen motif set.

Across both heavy-hex and square grid topologies, the GPU version of \(\Delta\)_-Motif_ achieves the lowest execution times,<tbc>

<tbc>often providing speedups of one to two orders of magnitude compared to VF2. Excluding the one-time data preparation step yields even greater gains, highlighting the benefit of caching in repeated-query scenarios. The CPU version also outperforms VF2 in most cases, although the margins are smaller.

The choice of motif strongly affects performance. The baseline motif _M_<sub>2</sub> (Sec. IV-B), functionally similar to a<tbc>

<sup>1</sup>We focus on 60-node patterns rather than 100-node ones, since CPU execution times for the latter were too long.

\begin{tabular}{cccccccccccccccc}
\multirow{2}{*}{**Data Graph**} & \multicolumn{12}{c}{**Pattern Graph Size**} \\
 & \multirow{2}{*}{**Size**} & \multicolumn{3}{c}{**20**} & \multicolumn{3}{c}{**40**} & \multicolumn{3}{c}{**60**} & \multicolumn{3}{c}{**80**} & \multicolumn{3}{c}{**100**} \\
 & & **min** & **mean** & **max** & **min** & **mean** & **max** & **min** & **mean** & **max** & **min** & **mean** & **max** & **min** & **mean** & **max** \\
Heavy & 1990 & 0.64 & 2.96 & 7.84 & 1.61 & 12.78 & 151.11 & 1.85 & 14.05 & 210.91 & 1.83 & 15.62 & 179.33 & 2.48 & 13.03 & 160.35 \\
Hex & 4485 & 2.76 & 10.09 & 22.58 & 5.70 & 35.76 & 238.03 & 6.84 & 42.43 & 294.80 & 9.95 & 49.53 & 269.72 & 9.18 & 42.36 & 415.20 \\
Square & 1600 & 0.91 & 3.29 & 46.98 & 1.49 & 6.24 & 78.85 & 2.21 & 11.58 & 313.95 & 2.44 & 12.65 & 135.46 & 1.57 & 15.20 & 99.58 \\
Grid & 3600 & 2.75 & 7.79 & 127.64 & 5.17 & 17.50 & 146.19 & 7.25 & 30.11 & **594.92** & 8.32 & 36.50 & 306.00 & 8.15 & 53.43 & 269.03 \\
\end{tabular}


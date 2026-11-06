<tbc>seconds, unless otherwise noted. Furthermore, for timed out runs of MSTUMP we report, in parentheses, an estimate of the running time, which is made possible by the very regular behavior of MSTUMP with respect to the input size. For EDM and RP the running time is more unpredictable, therefore we refrain from providing estimates for timed out runs.

As can be seen, our algorithm is faster on all settings, completing the execution orders of magnitude faster than the baselines on the larger datasets. To substantiate this observation,  4 reports the number of distance computations carried out by each approach: MOMENTI usage of LSH allows to effectively prune most distance computations, whereas MSTUMP computes a quadratic number of distances.

The EMD algorithm appears to be the slowest, its major drawback being the set up of the parameters for a successful discovery. On the other hand, RP scales better to larger datasets but its parameter tuning heuristic repeatedly discards the collision matrix when a sparsification target is not met, this is especially costly on high dimensional datasets. We stress that the Matrix Profile computed by MSTUMP allows the discovery of motifs of any dimensionality, while in this test MOMENTI only finds the top motif for a fixed dimensionality. In the next section we will investigate how MOMENTI behaves when finding motifs for all dimensionalities at the same time.

Finally,  5 reports the memory usage, in gigabytes, of the different algorithms. We observe that MOMENTI requires the least memory to execute.

_Quality of the motifs._ To better understand what pairs are returned by the different algorithms we measured the Mean Absolute Relative Error (MARE) of the distances of the discovered motifs with respect to the exact ones. We found that RP can reach MARE values as high as 40%, while EMD stays below 20%. In contrast, our method consistently maintains MARE under 3%, underlining how beneficial LSH, that mainly explores close pairs, is in this context. Further details on the quality of our results will be given in Section 7.5.

## 7.2 Finding the top motifs with different dimensionalities

In this second experiment the aim is to find the motifs for all dimensionalities \(2\le d\le D\) in the same execution. MSTUMP does this natively, whereas our algorithm MOMENTI can be adapted to do so as described in Section 6.3. EMD and RP can only achieve<tbc>

<tbc>this through multiple executions and are thus excluded from this experiment. In  6 we report the results for this experiment.

\begin{tabular}{ccccc}
dataset & MOMENTI & MSTUMP & EMD & RP \\
potentials & 64 & \(2.4\cdot 10^7\) & \(1.0\cdot 10^2\) & \(2.7\cdot 10^3\) \\
evaporator & \(4.7\cdot 10^2\) & \(1.4\cdot 10^8\) & 5 & \(4.4\cdot 10^4\) \\
RUTH & \(1.2\cdot 10^2\) & \(3.3\cdot 10^9\) & \(5.4\cdot 10^3\) & \(2.3\cdot 10^5\) \\
weather & \(9.8\cdot 10^4\) & \(3.9\cdot 10^{10}\) & - & \(2.1\cdot 10^6\) \\
whales & \(3.1\cdot 10^8\) & \((3.2\cdot 10^{12})\) & - & - \\
quake & \(1.1\cdot 10^6\) & \((6.6\cdot 10^{14})\) & - & - \\
el\_load & \(4.4\cdot 10^2\) & \((2.4\cdot 10^{14})\) & - & - \\
LTMM & \(4.4\cdot 10^2\) & \((1.9\cdot 10^{15})\) & - & - \\
\end{tabular}

\begin{tabular}{ccccc}
 & \multicolumn{4}{c}{Space (GB)} \\
dataset & MOMENTI & MSTUMP & EMD & RP \\
potentials & 0.016 & 0.028 & 0.79 & 0.07 \\
evaporator & 0.020 & 0.030 & 0.81 & 0.1 \\
RUTH & 0.025 & 0.084 & 1.19 & 0.5 \\
weather & 0.027 & 0.106 & - & 0.8 \\
whales & 0.24 & 3.2 & - & - \\
quake & 2.13 & 23.0 & - & - \\
el\_load & 1.50 & 7.4 & - & - \\
LTMM & 3.00 & 15.7 & - & - \\
\end{tabular}

\begin{tabular}{ccc}
dataset & MOMENTI & MSTUMP \\
potentials & 0.75 & 3.65 \\
evaporator & 0.89 & 4.45 \\
RUTH & 12.46 & 84.04 \\
weather & 47.85 & 1035.73 \\
whales & 2.5 h & (2.7 days) \\
quake & 5.8 h & (7.2 days) \\
el\_load & 3.1 h & (8.4 days) \\
LTMM & 16 h & (11.8 days) \\
\end{tabular}

106
LTMM (Mstump)
EL_LOAD (Mstump)
QUAKE (Mstump)
WHALES (Mstump)
105
LTMM
104
EL_LOAD
QUAKE
103
WEATHER (Mstump)
Time (s)
WHALES
102
RUTH (Mstump)
WEATHER
101
EVAPORATOR (Mstump)
POTENTIALS (Mstump)
RUTH
100
POTENTIALS
EVAPORATOR
100
101
102
103
Distance

** 4: Number of cumulative distance computations to find the top** _d_**-dimensional motif.**

** 5: Memory required to find the top** _d_**-dimensional motif.**

** 6: Time required for the top motifs for all dimensionalities. Mean over 9 runs. Values in parentheses are estimates.**

**Figure 2: Solid lines mark the time required by MOMENTI to find the top motif of each dimensionality for all datasets; dashed lines mark the time required by the MSTUMP baseline for the same task.**


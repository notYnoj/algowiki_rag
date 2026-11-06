<tbc>tecture by first modelling it with the help of a temporal graph. Next, we have used this model for computing all- pairs shortest time paths in the network. These paths can be used for shortest time communication among nodes in the network to realize a time-critical distributed computing platform using this network which forms the backbone for internode message communication. Future research works in this direction include the computation of other types of optimum paths, e.g., earliest arrival time paths and latest departure time paths based on the proposed model.

## REFERENCES

\begin{tabular}{cc}
**Statistic** & **Definition / Reporting Guidance** \\
Med\[T\], P95\[T\] & Median and 95th percentile of shortest communication time (seconds/minutes). \\
Med\[_H_\] & Median hop count of shortest-time paths; report with IQR. \\
Med\[_f<sub>w</sub>_\] & Median waiting fraction \(f_w=\frac{T_\text{wait}}{T_\text{wait}+T_\text{trav}}\) . \\
Pr(_f<sub>w</sub>\>_0.5) & Fraction of sampled routes where waiting exceeds traversal time. \\
\end{tabular}

Hop-count distribution
Waiting vs. traversing decomposition
1.0
0.16
median=5
0.14
0.8
mean=0.69
0.12
0.10
0.6
Probability density
0.08
Fraction of end-to-end duration
0.4
mean=0.31
0.06
0.04
0.2
0.02
0.00
0.0
1
2
3
4
5
6
7
8
9
10
11
Traversing fraction
Waiting fraction
Hop count of fastest (shortest-duration) path

Fig. 8. Hop count and waiting-time decomposition (sampled, \(n\approx 2\times 10^4\)). Left: hop-count distribution of sampled shortest-time paths. Right: fraction of end-to-end time spent waiting versus traversing, computed by subtracting hop traversal time from total temporal-path duration.

TABLE 10

Shortest-time path summary metrics (mappings paths in Fig. 8).


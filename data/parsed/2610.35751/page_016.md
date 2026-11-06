## C SENSITIVITY ANALYSIS OF THE PARETO ANGLE THRESHOLD \(\theta_{th}\)

To understand why HM is more sensitive to the Pareto angle threshold \(\theta_{th}\), we analyze the Pareto angle dispersion of its neighbors and the local neighborhood consistency between its two attribute spaces.

**Pareto Angle Dispersion**. We analyze the distribution of dual- attribute distances between each node _u_ and its neighbors, as shown in Figure 33. Specifically, for each node _u_, we collect the distance pairs \((\delta_x(u,v),\delta_y(u,v))\) for all its neighbors _v_ and aggregate them across all nodes to characterize the overall neighbor distribution of each dataset. HM exhibits a wider Pareto-angle interval containing 95% of the neighbor pairs, spanning \(55.5^\circ\), compared with \(31.0^\circ\) for OI and \(43.0^\circ\) for CM. To further quantify the dispersion of neighbors, we compute the average difference in Pareto angles among the neighbors of each node and average it across all nodes. Under the same maximum neighbor count _R_, HM exhibits a substantially larger mean angular difference of \(16.07^\circ\), compared with \(8.73^\circ\) for OI and \(10.38^\circ\) for CM. These results indicate that the neighbors of individual nodes in HM tend to be more widely spread in the Pareto angular space. Consequently, a small threshold may exclude more potentially useful pruning comparisons in HM, affecting neighbor selection quality and search performance.

**Local Neighborhood Consistency**. To understand the data properties underlying the differences in Pareto-angle distributions, we measure local neighborhood consistency directly from the attribute vectors, independently of the graph index. We uniformly sample 10,000 objects from each dataset and compute their exact nearest- neighbor rankings over the entire dataset, excluding the source object itself. For each sampled object, we identify its 100 nearest neighbors in attribute space _x_ and calculate their average distance- rank percentile in attribute space _y_. We then average these values across all sampled objects. As shown in  4, HM has a mean percentile of 49.99%, close to the expected percentile of approximately 50% for uniformly random candidates. In contrast, OI and CM have lower mean percentiles of 38.98% and 32.90%, respectively, indicating stronger local neighborhood consistency between the two attribute spaces. HM’s weaker consistency, together with its greater Pareto angular dispersion, helps explain why it is more sensitive to the threshold.

\begin{tabular}{cc}
Dataset & Mean distance-rank percentile \\
OpenImage & 38.98% \\
Howto100M & 49.99% \\
CC3M & 32.90% \\
\end{tabular}

Neighbors (%)
1
0.05
10-2
0.5
10-4
31.0
0
0
0.5
1
10-6
δ x

Neighbors (%)
1
0.05
10-2
0.5
10-4
35.5
0
0
0.5
1
10-6
δ x

Neighbors (%)
1
0.05
10-2
0.5
10-4
43.0
0
0
0.5
1
10-6
δ x

**(a) OpenImage**

**(b) Howto100M**

**(c) CC3M**

**Figure 33: Distribution of dual-attribute distances between nodes and their neighbors. The blue dashed rays delimit the shortest continuous Pareto-angle interval containing 95% of the neighbor pairs. The angular width of each interval is annotated.**

** 4: Average distance-rank percentile in attribute space _y_ of the 100 nearest neighbors selected in attribute space _x_. For each dataset, 10,000 source points are uniformly sampled. Nearest-neighbor selection and distance ranking are performed over the entire dataset, excluding the source point itself. Lower values indicate stronger local neighborhood consistency, while uniformly random candidates yield an expected percentile of approximately 50%.**


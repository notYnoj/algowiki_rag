## E.3 External Exact-Statevector Baselines

s 8 and 9 contextualize the local stochastic methods by reporting every available external exact-statevector parameter-setting baseline for MaxCut QAOA. Because these methods feature unequal instance coverage and unmatched initialization, tuning, and stopping conditions, they are included strictly as descriptive, contextual baselines rather than a controlled ranking.

\begin{tabular}{cccccccc}
Depth & Method & Feasible (%) & Avg. |_IS_| (support) & Max. |_IS_| (support) & Calls & Calls/SPSA & Time/SPSA \\
1 & SPSA & 49.8 & 2.83 (35/36) & 5.00 (35/36) & 4,123 & 1.00 & 1.00 \\
 & non-recursive CRVG & 50.8 & 2.52 (34/36) & 5.00 (34/36) & 3,536 & 0.86 & 0.86 \\
 & recursive CRVG & 50.0 & 2.58 (33/36) & 5.00 (33/36) & 3,000 & 0.73 & 0.73 \\
3 & SPSA & 68.0 & 2.26 (36/36) & 5.00 (36/36) & 4,500 & 1.00 & 1.00 \\
 & non-recursive CRVG & 73.2 & 3.07 (36/36) & 5.50 (36/36) & 3,552 & 0.79 & 0.81 \\
 & recursive CRVG & 69.9 & 2.95 (36/36) & 5.00 (36/36) & 2,992 & 0.66 & 0.68 \\
5 & SPSA & 73.6 & 2.06 (36/36) & 4.50 (36/36) & 4,500 & 1.00 & 1.00 \\
 & non-recursive CRVG & 56.6 & 2.98 (35/36) & 5.00 (35/36) & 3,538 & 0.79 & 0.80 \\
 & recursive CRVG & 39.3 & 2.58 (35/36) & 4.00 (35/36) & 2,958 & 0.66 & 0.67 \\
7 & SPSA & 68.6 & 2.29 (36/36) & 5.00 (36/36) & 4,500 & 1.00 & 1.00 \\
 & non-recursive CRVG & 52.3 & 2.79 (34/36) & 4.50 (34/36) & 3,570 & 0.79 & 0.80 \\
 & recursive CRVG & 11.5 & 2.40 (34/36) & 4.00 (34/36) & 2,952 & 0.66 & 0.66 \\
\end{tabular}

\begin{tabular}{cccccc}
Depth & External method & Coverage & Baseline ratio \[IQR\] & Matched local & Local - baseline \\
1 & Fixed angle & 15/36 & 0.787 \[0.773, 0.817\] & 0.806 & +0.020 \\
 & Fixed angle + opt. & 19/36 & 0.788 \[0.775, 0.831\] & 0.806 & +0.014 \\
 & Recursive transfer + opt. & 2/36<sup>†</sup> & 0.740 \[0.723, 0.757\] & 0.753 & +0.014 \\
 & TQA & 27/36 & 0.773 \[0.753, 0.788\] & 0.798 & +0.025 \\
 & TQA + opt. & 21/36 & 0.774 \[0.745, 0.784\] & 0.790 & +0.015 \\
3 & Fixed angle & 27/36 & 0.892 \[0.873, 0.899\] & 0.884 & -0.002 \\
 & Fixed angle + opt. & 29/36 & 0.900 \[0.889, 0.914\] & 0.884 & -0.011 \\
 & Fourier & 27/36 & 0.860 \[0.808, 0.904\] & 0.890 & +0.046 \\
 & Interpolation & 32/36 & 0.891 \[0.866, 0.905\] & 0.885 & -0.004 \\
 & Recursive transfer + angle opt. & 2/36<sup>†</sup> & 0.863 \[0.850, 0.876\] & 0.847 & -0.016 \\
 & Recursive transfer + opt. & 2/36<sup>†</sup> & 0.844 \[0.829, 0.859\] & 0.847 & +0.003 \\
 & TQA & 31/36 & 0.822 \[0.786, 0.835\] & 0.884 & +0.069 \\
 & TQA + opt. & 25/36 & 0.874 \[0.862, 0.892\] & 0.884 & -0.003 \\
 & Transfer strategy & 32/36 & 0.881 \[0.858, 0.890\] & 0.884 & +0.011 \\
\end{tabular}

7: MIS QAOA endpoint feasibility, feasible-set sizes, and resources. Entries are descriptive medians across instances; size entries show median (valid support) because size is undefined when no feasible shot was observed. Call and time ratios are paired within instance against SPSA before taking the median; values below one favor the listed method. Calls are sampled-objective calls with 256 shots each, and wall time is host-specific.

8: External exact-statevector QAOA parameter-setting baselines on their available instance support. Baseline entries report median \[interquartile range\]. For every row, the local median and paired difference are recomputed using only the instances available for that baseline; positive differences favor the best local finite-shot optimizer. Different rows have different support and do not constitute a common controlled ranking.

<sup>†</sup>Sparse support (_n\<_5); interpret the median descriptively only.


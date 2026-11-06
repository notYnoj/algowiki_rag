## E Additional Experimental Details

This appendix provides granular tabular data supporting the empirical observations discussed in Section 5. It includes exact numerical endpoints for selected trajectories, exhaustive resource exposure summaries, and broader contextual comparisons against external exact-statevector baselines.

### E.1 Trajectory Numerical Endpoints

5 details the final logged parameters, sampled energies, and variance measurements for the selected 10- and 15-node MaxCut trajectories featured in Figures 1 and 2. Note that unequal logged endpoints preclude a strict matched-budget interpretation.

### E.2 Exhaustive Resource Summaries

s 6 and 7 provide the exact median approximations, sampled-objective call counts, and relative time ratios for the MaxCut QAOA and MIS QAOA depth studies, respectively. Calls are reconstructed from the optimizer control flow, with each invoking one 256-shot Aer sampler job.

\begin{tabular}{ccccccc}
Ansatz / nodes & Method & Best energy & Final energy & Variance & Entropy & Logged evals \\
EfficientSU2 / 10 & SPSA & -5.09 & -5.03 & 5.19 & 4.34 & 4,982 \\
 & non-recursive CRVG & -7.93 & -7.93 & 0.26 & 0.24 & 5,776 \\
 & recursive CRVG & -1.97 & -0.60 & 16.68 & 7.06 & 4,638 \\
EfficientSU2 / 15 & SPSA & -7.09 & -6.94 & 21.62 & 6.34 & 4,982 \\
 & non-recursive CRVG & -9.34 & -9.34 & 7.39 & 4.28 & 5,951 \\
 & recursive CRVG & -0.93 & 0.23 & 17.18 & 7.93 & 4,826 \\
QAOA / 10 & SPSA & -2.55 & -2.11 & 12.11 & 7.17 & 4,982 \\
 & non-recursive CRVG & -5.87 & -5.73 & 8.13 & 6.40 & 5,934 \\
 & recursive CRVG & -5.73 & -5.55 & 6.98 & 6.58 & 4,981 \\
QAOA / 15 & SPSA & -9.11 & -8.91 & 15.46 & 7.77 & 2,762 \\
 & non-recursive CRVG & -9.16 & -8.25 & 20.94 & 7.77 & 5,934 \\
 & recursive CRVG & -10.29 & -9.95 & 15.25 & 7.56 & 4,805 \\
\end{tabular}

\begin{tabular}{cccccccc}
Depth & Method & Best ratio & Calls & Time (s) & Calls/SPSA & Time/SPSA & Early stops \\
1 & SPSA & 0.793 & 3,247 & 19.3 & 1.00 & 1.00 & 36/36 \\
 & non-recursive CRVG & 0.793 & 3,536 & 20.5 & 1.09 & 1.06 & 36/36 \\
 & recursive CRVG & 0.791 & 3,000 & 17.5 & 0.90 & 0.87 & 36/36 \\
3 & SPSA & 0.883 & 4,500 & 43.8 & 1.00 & 1.00 & 36/36 \\
 & non-recursive CRVG & 0.881 & 3,552 & 37.0 & 0.79 & 0.80 & 36/36 \\
 & recursive CRVG & 0.879 & 2,992 & 31.4 & 0.66 & 0.68 & 36/36 \\
5 & SPSA & 0.873 & 4,500 & 73.6 & 1.00 & 1.00 & 36/36 \\
 & non-recursive CRVG & 0.850 & 3,538 & 59.1 & 0.79 & 0.80 & 36/36 \\
 & recursive CRVG & 0.856 & 2,958 & 49.1 & 0.66 & 0.66 & 36/36 \\
7 & SPSA & 0.843 & 4,500 & 88.3 & 1.00 & 1.00 & 36/36 \\
 & non-recursive CRVG & 0.863 & 3,570 & 73.0 & 0.79 & 0.79 & 36/36 \\
 & recursive CRVG & 0.763 & 2,952 & 60.5 & 0.66 & 0.66 & 36/36 \\
\end{tabular}

5: Single-seed MaxCut trajectory summaries on 30%-density Erdős-Rényi graphs. "Variance" is the variance of sampled output energies, not gradient-estimator variance. Metrics use the final stored parameters except best energy, which is the trajectory minimum. Unequal logged endpoints preclude a strict matched-budget interpretation.

6: Endpoint resource statistics for the paired local QAOA runs. "Calls" are calls to the sampled objective, reconstructed from the optimizer control flow; each invokes one 256-shot Aer sampler job. They are not the number of stored history points. Ratios are computed within each instance before taking the median; values below one favor the listed method. Wall time is specific to the archived Aer implementation and execution host.


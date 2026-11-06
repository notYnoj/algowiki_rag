<tbc>Solving for _p_, we obtain the **Skew Crossover**:

\(p>\frac{R-2}{c(R-1)+(R-3)}\)

## 5.5 Case 2: Uniform Log Distribution

We analyze performance on a uniform input distribution within log groups, where the active set shrinks by a constant fraction 1_/R_ in each round. We assume the active set size at round _r_ is \(n_r=n(1-\frac{r-1}{R})\).

**Cost Derivation:**

- **Stage 1:** Full Sort. \(\text{Cost}=\alpha\cdot n\).<tbc>

**- **Stage 2 (Iterative Sum):** Rounds 2 to _R_-1 involve both partitioning and sorting on the decaying active set _n<sub>r</sub>_.<tbc>

<tbc>\(\text{Cost}_{\text{Stage}2}=(\alpha+\beta)\sum_{r=2}^{R-1}n\left(1-\frac{r-1}{R}\right)\)<tbc>

<tbc>Using the discrete sum identity for the range _r_=2_...R_-1:<tbc>

<tbc>\(\text{Cost}_{\text{Stage}2}=(\alpha+\beta)n\left[(R-2)-\frac{(R-2)(R-1)}{2R}\right]\)<tbc>

**- **Stage 3:** Sort remaining elements _n/R_. \(\text{Cost}=\alpha(n/R)\).

**Total Cost Equation:** Summing Stage 1 with the combined costs of Stage 2 and 3, we get, \(T_\text{SP-LSD}^\text{uniform}=\alpha n+(\alpha+\beta)n\left[(R-2)-\frac{(R-2)(R-1)}{2R}\right]+\alpha(n/R)\).

\begin{tabular}{ccccccc}
**R (Rounds)** & \multicolumn{6}{c}{**Cost Ratio** \((c=\alpha/\beta)\)} \\
 & \multicolumn{6}{c}{**c=1c=2c=3c=4c=5**} \\
3 & 0.500 & 0.250 & 0.167 & 0.125 & 0.100 & \\
4 & 0.500 & 0.286 & 0.200 & 0.154 & 0.125 & \\
8 & 0.500 & 0.316 & 0.231 & 0.182 & 0.150 & \\
16 & 0.500 & 0.326 & 0.241 & 0.192 & 0.159 & \\
32 & 0.500 & 0.330 & 0.246 & 0.197 & 0.163 & \\
\end{tabular}

2: Minimum Pruning Fraction (_p_) Required for SP-LSD Viability across varying Rounds (_R_) and Cost Ratios (_c_). Calculated using the Pruning Crossover inequality \(p>\frac{R-2}{c(R-1)+R-3}\).


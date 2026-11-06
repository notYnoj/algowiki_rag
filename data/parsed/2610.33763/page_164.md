## Case 2 - Example 1.

The minimum eigenvalue appear to decay to 0 at a quadratic rate, while the largest eigenvalue converges to zero linearly, as determined by the momentary symbol. As a consequence, the growth of cond<sub>2</sub>(_G<sub>n</sub>_) is moderate.

## Case 2 - Example 2.

Here \(\widetilde{G}_\mathrm{max}\simeq 1.22\). \(\lambda_\mathrm{max}(G_n)\) converges to this value and is included in the range of \(\widetilde{G}\), whereas \(\lambda_\mathrm{min}(G_n)\) decays linearly. This better conditioning compared to **Example 2** of the first case is reasonable, since the positive perturbations we introduced to the Toeplitz matrices of this example (Equation 9.12 decay in norm more slowly than the ones in **Case 1 - Example 1**).

## Zero-related statistics.

For each block size _n_, we report the fraction of eigenvalues whose modulus does not exceed the fixed cutoff 0.1; see s 9.7-9.10. Each table lists the empirical proportion (\(Prop.\le 0.1\)), the theoretical measure of the zero set of the rearranged symbol (_Target_), and the absolute difference (_Error_).

## Case 1 - Example 1.

The conjectured symbol is the zero function, so the target measure is 1. The empirical value increases monotonically with _n_, remaining within a small error. Because the number of outliers is at most _o(n_), we expect that the proportion will converge to 1 as \(n\rightarrow\infty\).

\begin{tabular}{ccccccc}
_n_ & \(\widetilde{G}_\mathrm{min}\) & \(\widetilde{G}_\mathrm{max}\) & Min. eig. & Max. eig. & \multicolumn{2}{c}{cond<sub>2</sub>(_G<sub>n</sub>_)} \\
40 & 0.0000 & \(2.99393066\) & \(1.5625\times 10^{-5}\) & \(2.99257415\) & \(1.915\times 10^5\) \\
80 & 0.0000 & \(2.99393066\) & \(1.9531\times 10^{-6}\) & \(2.99393280\) & \(1.533\times 10^6\) \\
160 & 0.0000 & \(2.99393066\) & \(2.4414\times 10^{-7}\) & \(2.99393094\) & \(1.226\times 10^7\) \\
320 & 0.0000 & \(2.99393066\) & \(3.0518\times 10^{-8}\) & \(2.99393070\) & \(9.811\times 10^7\) \\
\end{tabular}

\begin{tabular}{ccccccc}
_n_ & \(\widetilde{G}_\mathrm{min}\) & \(\widetilde{G}_\mathrm{max}\) & Min. eig. & Max. eig. & cond<sub>2</sub>(_G<sub>n</sub>_) \\
40 & 0.00 & 0.00 & \(1.2615\times 10^{-3}\) & \(0.51134401\) & \(4.0536\times 10^2\) \\
80 & 0.00 & 0.00 & \(3.2103\times 10^{-4}\) & \(0.25691974\) & \(8.0029\times 10^2\) \\
160 & 0.00 & 0.00 & \(8.0993\times 10^{-5}\) & \(0.12877171\) & \(1.5899\times 10^3\) \\
320 & 0.00 & 0.00 & \(2.0342\times 10^{-5}\) & \(0.06447364\) & \(3.1695\times 10^3\) \\
\end{tabular}

\begin{tabular}{ccccccc}
_n_ & \(\widetilde{G}_\mathrm{min}\) & \(\widetilde{G}_\mathrm{max}\) & Min. eig. & Max. eig. & cond<sub>2</sub>(_G<sub>n</sub>_) \\
40 & 0.00 & \(1.22418242\) & \(3.24\times 10^{-3}\) & \(1.13658304\) & \(3.50\times 10^2\) \\
80 & 0.00 & \(1.22418242\) & \(1.46\times 10^{-3}\) & \(1.17911634\) & \(8.10\times 10^2\) \\
160 & 0.00 & \(1.22418242\) & \(5.65\times 10^{-4}\) & \(1.20156562\) & \(2.13\times 10^3\) \\
320 & 0.00 & \(1.22418242\) & \(8.19\times 10^{-5}\) & \(1.21306699\) & \(1.48\times 10^4\) \\
\end{tabular}

9.4: Extremal eigenvalues and condition numbers for **Case 1 - Example 2** (symbol positive on an overlap set).

9.5: Extremal eigenvalues and condition numbers for **Case 2 - Example 1** (candidate symbol \(\widetilde{G}\equiv 0\)).

9.6: Extremal eigenvalues and condition numbers for **Case 2 - Example 2** (symbol positive on an overlap set).


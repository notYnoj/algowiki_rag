## Extremal eigenvalues.

For each block size _n_ we report

\(\lambda_\mathrm{min}(G_n),\lambda_\mathrm{max}(G_n),\mathrm{cond}_2(G_n)=\frac{\lambda_\mathrm{max}(G_n)}{\lambda_\mathrm{min}(G_n)},\)

together with the essential infimum and supremum of the conjectured symbol, \(\widetilde{G}_\mathrm{min}\) and \(\widetilde{G}_\mathrm{max}\). In this way, we can observe how rapidly the minimum eigenvalue decays and, in most cases, how the maximum eigenvalues converge to the essential supremum of the spectral symbol. This provides a clear measure of the conditioning behaviour as _n_ grows.

## Case 1 - Example 2.

Here \(\widetilde{G}_\mathrm{max}=2.9939\) is strictly positive. In this example, we observe a fast convergence of \(\lambda_\mathrm{max}(G_n)\) and an exponential decay of \(\lambda_\mathrm{min}(G_n)\), which clearly causes the condition number cond<sub>2</sub>(_G<sub>n</sub>_) to escalate, reaching O(10<sup>8</sup>) at _n_=320.

\begin{tabular}{ccccccc}
_n_ & \(\widetilde{G}_\mathrm{min}\) & \(\widetilde{G}_\mathrm{max}\) & Min. eig. & Max. eig. & \multicolumn{3}{c}{cond<sub>2</sub>(_G<sub>n</sub>_)} \\
40 & 0.0000 & 0.0000 & \(8.7142\times 10^{-3}\) & \(3.91278029\) & \(4.490\times 10^2\) & \\
80 & 0.0000 & 0.0000 & \(3.6849\times 10^{-3}\) & \(4.03656685\) & \(1.095\times 10^3\) & \\
160 & 0.0000 & 0.0000 & \(1.4929\times 10^{-3}\) & \(4.13399129\) & \(2.769\times 10^3\) & \\
320 & 0.0000 & 0.0000 & \(5.8335\times 10^{-4}\) & \(4.21189805\) & \(7.220\times 10^3\) & \\
\end{tabular}

Rearranged G(x, θ) vs Geom-Mean (n = 40)
Rearranged G(x, θ) vs Geom-Mean (n = 80)
1.2
G(x, θ) (theoretical)
Geom-mean eigs
1.2
G(x, θ) (theoretical)
Geom-mean eigs
1.0
1.0
0.8
0.8
Eigenvalue
Eigenvalue
0.6
0.6
0.4
0.4
0.2
0.2
0.0
0.0
Rearranged G(x, θ) vs Geom-Mean (n = 160)
Rearranged G(x, θ) vs Geom-Mean (n = 320)
1.2
G(x, θ) (theoretical)
Geom-mean eigs
Geom-mean eigs
1.2
G(x, θ) (theoretical)
Geom-mean eigs
1.0
1.0
0.8
0.8
Eigenvalue
Eigenvalue
0.6
0.6
0.4
0.4
0.2
0.2
0.0
0.0
0.0
0.2
0.4 Index scaled to [0, 1]
0.6
0.8
1.0
0.0
0.2
0.4 Index scaled to [0, 1]
0.6
0.8
1.0

Figure 9.6: **Case 2, Example 2.** Sorted eigenvalues of _G(A<sub>n</sub>,B<sub>n</sub>_) (colored markers) versus the rearranged eigenvalue distribution from \(G(\kappa,\xi)\) (solid red line), for _n_=40,80,160,320.

9.3: Extremal eigenvalues and condition numbers for **Case 1 - Example 1** (symbol zero almost everywhere).


<tbc>Overall, the proposed P<sub>VBP</sub> preconditioner consistently outperforms the other methods, yielding the lowest iteration counts and the least computational time for all tested grid resolutions.

## 6 Conclusions

In this paper, we have proposed a variant of the block preconditioner (VBP) based on a matrix splitting of the coefficient matrix. The convergence of the corresponding stationary iterative method was analyzed, and the spectral properties of the preconditioned matrix were investigated in detail. Numerical experiments confirm that the proposed preconditioner outperforms the other preconditioners considered in this study in terms of computational efficiency and robustness.

\begin{tabular}{ccccc}
Method & \(\alpha\) & \(32\times 32\) & \(64\times 64\) & \(128\times 128\) \\
P<sub>BS</sub> & \(\alpha_\mathrm{BS}\) & 1.5565e+01 & 1.5962e+01 & 1.6673e+01 \\
P<sub>VHSS</sub> & \(\alpha_\mathrm{VHSS}\) & 5.4021 & 2.7430 & 1.3822 \\
P<sub>MBP</sub> & \(\alpha_\mathrm{MBP}\) & 1.4582 & 1.1.4579 & 1.4578 \\
P<sub>VBP</sub> & \(\alpha_\mathrm{VBP}\) & 1.7071e-05 & 1.9189e-05 & 1.9770e-5 \\
\end{tabular}

\begin{tabular}{ccccccccc}
\multirow{2}{*}{Grids} & \multicolumn{3}{c}{\(32\times 32\)} & \multicolumn{3}{c}{\(64\times 64\)} & \multicolumn{3}{c}{\(128\times 128\)} \\
 & IT & CPU & RES & IT & CPU & RES & IT & CPU & RES \\
P<sub>BS</sub> & 24 & 0.14 & 7.6e-07 & 45 & 1.22 & 5.5e-07 & 85 & 20.22 & 7.6e-07 \\
P<sub>VHSS</sub> & 14 & 0.07 & 1.6e-07 & 18 & 0.71 & 2.6e-07 & 24 & 5.45 & 2.8e-07 \\
P<sub>MBP</sub> & 6 & 0.03 & 5.4e-07 & 7 & 0.21 & 4.2e-07 & 7 & 1.22 & 5.4e-07 \\
P<sub>VBP</sub> & 5 & 0.02 & 3.1e-07 & 5 & 0.18 & 3.4e-08 & 4 & 0.82 & 6.4e-07 \\
\end{tabular}

6: Comparison of quasi-optimal parameter \(\alpha\) values obtained by different preconditioning methods for Example 2 across various grid sizes with \(\tau=10\) and \(\omega=20\) .

7: Comparison of FGMRES performance using different preconditioning strategies with quasi-optimal parameter \(\alpha\) for Example 2 with \(\tau=10\) and \(\omega=10\).


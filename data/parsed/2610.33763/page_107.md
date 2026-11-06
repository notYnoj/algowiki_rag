We recall that \(cI_\mathbf{n}+\hat{a}B_\mathbf{n}\) which is of Toeplitz lower triangular form and we have specialized techniques for lower triangular Toeplitz matrices of cost \(O(\nu(\mathbf{n})log[\nu(\mathbf{n})])\) and this remains true for the circulant or \(\omega\)-circulant counterpart; see \[18, 31\] and references therein.

\begin{tabular}{ccccccccccccc}
 & \multicolumn{4}{c}{\(\xi=0.2\)} & \multicolumn{4}{c}{\(\xi=0.5\)} & \multicolumn{4}{c}{\(\xi=0.8\)} \\
 & \multicolumn{4}{c}{\(\eta_1=0.2,\eta_2=0.8\)} & \multicolumn{4}{c}{\(\eta_1=0.5,\eta_2=0.5\)} & \multicolumn{4}{c}{\(\eta_1=0.8,\eta_2=0.2\)} \\
 & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} \\
_n_<sub>1</sub>=_n_<sub>2</sub> & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) \\
2<sup>4</sup> & 31 & 22 & 0.00 & 0.00 & 27 & 22 & 0.02 & 0.01 & 31 & 22 & 0.01 & 0.01 \\
2<sup>5</sup> & 61 & 25 & 0.06 & 0.07 & 38 & 25 & 0.04 & 0.09 & 59 & 25 & 0.05 & 0.08 \\
2<sup>6</sup> & 116 & 26 & 1.67 & 1.28 & 56 & 26 & 0.56 & 1.17 & 113 & 26 & 1.27 & 1.17 \\
2<sup>7</sup> & 214 & 27 & 46.36 & 21.34 & 83 & 27 & 20.54 & 21.03 & 207 & 27 & 35.68 & 18.57 \\
\end{tabular}

\begin{tabular}{ccccccccccccc}
 & \multicolumn{4}{c}{\(\xi=0.2\)} & \multicolumn{4}{c}{\(\xi=0.5\)} & \multicolumn{4}{c}{\(\xi=0.8\)} \\
 & \multicolumn{4}{c}{\(\eta_1=0.2,\eta_2=0.8\)} & \multicolumn{4}{c}{\(\eta_1=0.5,\eta_2=0.5\)} & \multicolumn{4}{c}{\(\eta_1=0.8,\eta_2=0.2\)} \\
 & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} \\
_n_<sub>1</sub>=_n_<sub>2</sub> & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) & - & \(\widetilde{P}_{\nu(\mathbf{n})}\) \\
2<sup>4</sup> & 29 & 15 & 0.00 & 0.00 & 24 & 14 & 0.00 & 0.00 & 28 & 14 & 0.00 & 0.00 \\
2<sup>5</sup> & 50 & 15 & 0.02 & 0.02 & 32 & 15 & 0.01 & 0.03 & 49 & 15 & 0.02 & 0.02 \\
2<sup>6</sup> & 88 & 16 & 0.59 & 0.41 & 44 & 16 & 0.30 & 0.41 & 86 & 15 & 0.59 & 0.37 \\
2<sup>7</sup> & 156 & 19 & 14.98 & 7.02 & 61 & 16 & 6.87 & 7.18 & 153 & 16 & 18.62 & 7.41 \\
\end{tabular}

7.2: Iteration counts and CPU times of the GMRES method for solving the linear system with coefficient matrix \(\widetilde{M}_{\nu(\mathbf{n})}\) and \(c=\gamma_0\), without preconditioner and with preconditioner \(\widetilde{P}_{\nu(\mathbf{n})}\), for different fractional orders and for _a(x,y_)=_e_<sup>_x+y_</sup>, with _m_=3.

7.3: Iteration counts and CPU times of the GMRES method for solving the linear system with coefficient matrix \(\widetilde{M}_{\nu(\mathbf{n})}\) and \(c=\gamma_0\), without preconditioner and with preconditioner \(\widetilde{P}_{\nu(\mathbf{n})}\), for different fractional orders and for _a(x,y_)=1+_x+y_, with _m_=3.


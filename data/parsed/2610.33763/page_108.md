Finally, we introduce an alternative Strang-like preconditioner \(S_\widetilde{\mathbf{N}}\) for the linear system (7.16).

A Strang-like preconditioner for our block structure is defined by replacing each lower triangular Toeplitz matrix in the various blocks with its natural circulant approximation and by replacing coefficient _a(x,y_) with its integral average \(\hat{a}\) so that _D_**<sub>n</sub>**(_a_) is replaced by \(\hat{a}I_\mathbf{n}\) and _G_**<sub>n</sub>** reduces to<tbc>

\(G_\mathbf{n}=\hat{a}B_\mathbf{n},B_\mathbf{n}=(B_\mathbf{n}^x+B_\mathbf{n}^y),\)

<tbc>that is

\(S_\widetilde{\mathbf{N}}:=\left[\frac{S(U_m)\otimes I_\mathbf{n}+I_m\otimes\hat{a}S(B_\mathbf{n})}{\mathbf{e}_m^T\otimes I_\mathbf{n}}\right|\text{O}_{\mathbf{n}m\times\mathbf{n}}\frac{\lambda}{\alpha_m}D_\mathbf{n}(a)S(B_\mathbf{n})}\right].\) (7.23)

Since circulant matrices are diagonalizable by the Fourier matrices, we write

\(S(U_m)=F_m\Lambda_m^{(1)}F_m^*,S(B_\mathbf{n})=F_\mathbf{n}\Lambda_\mathbf{n}^{(2)}F_\mathbf{n}^*,\)

where \(\Lambda_m^{(1)}\) and \(\Lambda_\mathbf{n}^{(2)}\) are the diagonal matrices containing the eigenvalues and can be computed starting from the coefficients of _U<sub>m</sub>_, _B_**<sub>n</sub>** via the FFT.

\begin{tabular}{cccccccccccc}
 & \multicolumn{4}{c}{\(\xi=0.2\)} & \multicolumn{4}{c}{\(\xi=0.5\)} & \multicolumn{4}{c}{\(\xi=0.8\)} \\
 & \multicolumn{4}{c}{\(\eta_1=0.2\), \(\eta_2=0.8\)} & \multicolumn{4}{c}{\(\eta_1=0.5\), \(\eta_2=0.5\)} & \multicolumn{4}{c}{\(\eta_1=0.8\), \(\eta_2=0.2\)} \\
 & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} \\
_n_<sub>1</sub>=_n_<sub>2</sub> & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) \\
2<sup>4</sup> & 31 & 25 & 0.00 & 0.01 & 27 & 21 & 0.02 & 0.02 & 31 & 24 & 0.01 & 0.01 \\
2<sup>5</sup> & 61 & 27 & 0.06 & 0.03 & 38 & 24 & 0.04 & 0.03 & 59 & 26 & 0.05 & 0.03 \\
2<sup>6</sup> & 116 & 29 & 1.67 & 0.42 & 56 & 25 & 0.56 & 0.37 & 113 & 27 & 1.27 & 0.32 \\
2<sup>7</sup> & 214 & 29 & 46.36 & 6.64 & 83 & 25 & 20.56 & 4.78 & 207 & 27 & 35.68 & 4.69 \\
\end{tabular}

\begin{tabular}{cccccccccccc}
 & \multicolumn{4}{c}{\(\xi=0.2\)} & \multicolumn{4}{c}{\(\xi=0.5\)} & \multicolumn{4}{c}{\(\xi=0.8\)} \\
 & \multicolumn{4}{c}{\(\eta_1=0.2\), \(\eta_2=0.8\)} & \multicolumn{4}{c}{\(\eta_1=0.5\), \(\eta_2=0.5\)} & \multicolumn{4}{c}{\(\eta_1=0.8\), \(\eta_2=0.2\)} \\
 & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} \\
_n_<sub>1</sub>=_n_<sub>2</sub> & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) & - & \(\widetilde{S}_{\nu(\mathbf{n})}\) \\
2<sup>4</sup> & 29 & 17 & 0.00 & 0.00 & 24 & 13 & 0.00 & 0.00 & 28 & 16 & 0.00 & 0.00 \\
2<sup>5</sup> & 50 & 18 & 0.02 & 0.01 & 32 & 14 & 0.01 & 0.01 & 49 & 17 & 0.02 & 0.01 \\
2<sup>6</sup> & 88 & 18 & 0.59 & 0.14 & 44 & 14 & 0.30 & 0.10 & 86 & 17 & 0.59 & 0.12 \\
2<sup>7</sup> & 156 & 18 & 14.98 & 1.73 & 61 & 15 & 6.87 & 1.68 & 153 & 17 & 18.62 & 2.49 \\
\end{tabular}

7.4: Iteration counts and CPU times of the GMRES method for solving the linear system with coefficient matrix \(\widetilde{M}_{\nu(\mathbf{n})}\) and \(c=\gamma_0\), without preconditioner and with preconditioner \(\widetilde{S}_{\nu(\mathbf{n})}\), for different fractional orders and for _a(x,y_)=_e_<sup>_x+y_</sup>, with _m_=3.

7.5: Iteration counts and CPU times of the GMRES method for solving the linear system with coefficient matrix \(\widetilde{M}_{\nu(\mathbf{n})}\) and \(c=\gamma_0\), without preconditioner and with preconditioner \(\widetilde{S}_{\nu(\mathbf{n})}\), for different fractional orders and for _a(x,y_)=1+_x+y_, with _m_=3.


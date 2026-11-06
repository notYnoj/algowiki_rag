are the following

• When performing one matrix-vector multiplication with matrix \(A_\widetilde{\mathbf{N}}\), we per form \(\frac{m^2}{2}+O(m)\) products of a constant times a vector of size \(\nu(\mathbf{n})\), \(\frac{m^2}{2}+O(m)\) additions between vectors of size \(\nu(\mathbf{n})\), and _m_+1 products of the matrix _D_**<sub>n</sub>**(_a)B_**<sub>n</sub>** times a vector: hence the corresponding arithmetic cost is equal to \(m^2\nu(\mathbf{n})+Cm\nu(\mathbf{n})log[\nu(\mathbf{n})]+o(m^2\nu(\mathbf{n}))=m^2\nu(\mathbf{n})+o(m^2\nu(\mathbf{n}))\) arithmetic operations, if we make the natural assumption that \(log[\nu(\mathbf{n})]=o(m)\) and taking into account that _C_ is a constant;<tbc>

• When solving one linear system with coefficient matrix \(P_\widetilde{\mathbf{N}}\), we perform \(\frac{m^2}{2}+O(m)\) products of a constant times a vector of size \(\nu(\mathbf{n})\), \(\frac{m^2}{2}+O(m)\) additions between vectors of size \(\nu(\mathbf{n})\), and _m_+1 solutions of linear systems with coefficient matrix \(M_{\nu(\mathbf{n})}:=cI+D_\mathbf{n}(a)B_\mathbf{n}\) times a vector: hence the corresponding arithmetic cost is equal to \(m^2\nu(\mathbf{n})+C'm\nu(\mathbf{n})log[\nu(\mathbf{n})]+o(m^2\nu(\mathbf{n}))=m^2\nu(\mathbf{n})+o(m^2\nu(\mathbf{n}))\) arithmetic operations, if we make the natural assumption that \(log[\nu(\mathbf{n})]=o(m)\) and \(C'\) depends linearly on the number of iterations we need preconditioning with \(\widetilde{P}_{\nu(\mathbf{n})}:=cI+\hat{a}B_\mathbf{n}\) or with \(\widetilde{S}_{\nu(\mathbf{n})}:=cI+\hat{a}S(B_\mathbf{n})\). As it can be seen from  7.2,  7.3,  7.4,  7.5, the number of iterations for both preconditioned GMRES is bounded by a constant independent of the matrix size \(\nu(\mathbf{n})\) so that also \(C'\) can be assumed to be constant.<tbc>

\begin{tabular}{ccccccccccccc}
 & & \multicolumn{4}{c}{\(\xi=0.2\)} & \multicolumn{4}{c}{\(\xi=0.5\)} & \multicolumn{4}{c}{\(\xi=0.8\)} \\
 & & \multicolumn{2}{c}{\(\eta_1=0.2\),} & \multicolumn{2}{c}{\(\eta_2=0.8\)} & \multicolumn{2}{c}{\(\eta_1=0.5\),} & \multicolumn{2}{c}{\(\eta_2=0.5\)} & \multicolumn{2}{c}{\(\eta_1=0.8\),} & \multicolumn{2}{c}{\(\eta_2=0.2\)} \\
 & & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} \\
_n_<sub>1</sub>=_n_<sub>2</sub> & _m_ & - & \(P_\widetilde{\mathbf{N}}\) & - & \(P_\widetilde{\mathbf{N}}\) & - & \(P_\widetilde{\mathbf{N}}\) & - & \(P_\widetilde{\mathbf{N}}\) & - & \(P_\widetilde{\mathbf{N}}\) & - & \(P_\widetilde{\mathbf{N}}\) \\
2<sup>2</sup> & 2<sup>2</sup> & 32 & 8 & 0.02 & 0.01 & 29 & 8 & 0.01 & 0.01 & 30 & 8 & 0.00 & 0.00 \\
2<sup>2</sup> & 2<sup>3</sup> & 34 & 8 & 0.01 & 0.00 & 33 & 8 & 0.01 & 0.01 & 35 & 8 & 0.00 & 0.00 \\
2<sup>2</sup> & 2<sup>4</sup> & 34 & 8 & 0.01 & 0.00 & 38 & 8 & 0.01 & 0.00 & 47 & 8 & 0.01 & 0.01 \\
2<sup>2</sup> & 2<sup>5</sup> & 34 & 8 & 0.01 & 0.00 & 42 & 8 & 0.01 & 0.01 & 60 & 8 & 0.01 & 0.01 \\
2<sup>3</sup> & 2<sup>2</sup> & 59 & 17 & 0.01 & 0.00 & 48 & 15 & 0.01 & 0.00 & 49 & 16 & 0.00 & 0.00 \\
2<sup>3</sup> & 2<sup>3</sup> & 57 & 16 & 0.01 & 0.01 & 50 & 16 & 0.01 & 0.01 & 55 & 16 & 0.01 & 0.00 \\
2<sup>3</sup> & 2<sup>4</sup> & 61 & 16 & 0.01 & 0.01 & 54 & 16 & 0.01 & 0.01 & 66 & 15 & 0.02 & 0.01 \\
2<sup>3</sup> & 2<sup>5</sup> & 58 & 17 & 0.03 & 0.01 & 59 & 16 & 0.02 & 0.02 & 82 & 16 & 0.03 & 0.01 \\
2<sup>4</sup> & 2<sup>2</sup> & 98 & 27 & 0.04 & 0.02 & 75 & 28 & 0.04 & 0.02 & 78 & 27 & 0.03 & 0.01 \\
2<sup>4</sup> & 2<sup>3</sup> & 99 & 27 & 0.06 & 0.03 & 74 & 28 & 0.04 & 0.02 & 83 & 27 & 0.04 & 0.03 \\
2<sup>4</sup> & 2<sup>4</sup> & 97 & 28 & 0.12 & 0.04 & 79 & 28 & 0.09 & 0.04 & 92 & 27 & 0.11 & 0.04 \\
2<sup>4</sup> & 2<sup>5</sup> & 98 & 27 & 0.22 & 0.08 & 84 & 28 & 0.16 & 0.07 & 113 & 27 & 0.27 & 0.08 \\
2<sup>5</sup> & 2<sup>2</sup> & 189 & 39 & 1.71 & 0.69 & 115 & 43 & 0.96 & 0.83 & 146 & 38 & 1.18 & 0.63 \\
2<sup>5</sup> & 2<sup>3</sup> & 189 & 40 & 2.00 & 0.82 & 114 & 42 & 1.02 & 0.83 & 138 & 38 & 1.58 & 1.63 \\
2<sup>5</sup> & 2<sup>4</sup> & 185 & 39 & 2.87 & 1.16 & 115 & 41 & 1.40 & 1.13 & 144 & 37 & 2.04 & 2.11 \\
2<sup>5</sup> & 2<sup>5</sup> & 186 & 39 & 3.14 & 1.10 & 116 & 40 & 2.13 & 1.15 & 149 & 36 & 3.10 & 3.09 \\
\end{tabular}

7.1: Iteration counts and CPU times required by the GMRES method for solving the linear system, with and without preconditioning, for different values of the fractional orders.


## GMRES performance in the two-dimensional setting

Finally, we report the results of a few numerical tests performed in the the two- dimensional setting, both in the constant-coefficient case and in the variable-coefficient setting, where the diffusion function _a(x,y_) is chosen as the most natural bivariate extension of the ones previously considered. Though, discretization parameters are a bit small, due to the global dimension of the all-at-once systems, no relevant difference is observed in the convergence properties, which we already reported and commented in the one-dimensional setting; see  8.8,  8.9, and  8.10 for the numerics in the two-dimensional space case.<br>
It is worth stressing that we do not report numerical experiments when \(\alpha_1\neq\alpha_2\) since the results in practice are of the same quality as in the case \(\alpha_1=\alpha_2\) (and even slightly better indeed): the reason of such behavior is contained in Theorem 8.2, Theorem 8.4, Theorem 8.8, where it is evident that \(\alpha_1\neq\alpha_2\) implies a simplification in the spectral behavior, because the matrix sequence associated with the smaller parameter is spectrally negligible, when the matrix-sizes increase.

\begin{tabular}{ccccccccccccc}
\multicolumn{4}{c}{} & \multicolumn{3}{c}{\(\alpha_1=\alpha_2=1.3\)} & \multicolumn{3}{c}{\(\alpha_1=\alpha_2=1.5\)} & \multicolumn{3}{c}{\(\alpha_1=\alpha_2=1.8\)} \\
_N_<sub>1</sub> & _N_<sub>2</sub> & _M_ & _A_ & \(\widetilde{P}^{-1}A\) & \(\widehat{P}^{-1}A\) & _A_ & \(\widetilde{P}^{-1}A\) & \(\widehat{P}^{-1}A\) & _A_ & \(\widetilde{P}^{-1}A\) & \(\widehat{P}^{-1}A\) \\
2<sup>2</sup> & 2<sup>2</sup> & 2<sup>2</sup> & 16 & 10 & 10 & 19 & 11 & 11 & 21 & 12 & 12 \\
2<sup>2</sup> & 2<sup>2</sup> & 2<sup>3</sup> & 22 & 11 & 11 & 25 & 12 & 12 & 27 & 13 & 14 \\
2<sup>2</sup> & 2<sup>2</sup> & 2<sup>4</sup> & 32 & 11 & 12 & 35 & 13 & 13 & 40 & 15 & 16 \\
2<sup>2</sup> & 2<sup>2</sup> & 2<sup>5</sup> & 65 & 11 & 12 & 66 & 13 & 14 & 68 & 16 & 16 \\
2<sup>3</sup> & 2<sup>3</sup> & 2<sup>2</sup> & 27 & 13 & 13 & 31 & 14 & 15 & 37 & 15 & 15 \\
2<sup>3</sup> & 2<sup>3</sup> & 2<sup>3</sup> & 33 & 13 & 13 & 37 & 15 & 15 & 45 & 17 & 17 \\
2<sup>3</sup> & 2<sup>3</sup> & 2<sup>4</sup> & 45 & 14 & 14 & 51 & 16 & 16 & 63 & 18 & 18 \\
2<sup>3</sup> & 2<sup>3</sup> & 2<sup>5</sup> & 77 & 14 & 14 & 81 & 16 & 17 & 97 & 20 & 20 \\
2<sup>4</sup> & 2<sup>4</sup> & 2<sup>2</sup> & 49 & 15 & 15 & 55 & 17 & 17 & 67 & 18 & 17 \\
2<sup>4</sup> & 2<sup>4</sup> & 2<sup>3</sup> & 56 & 16 & 16 & 62 & 19 & 19 & 79 & 21 & 21 \\
2<sup>4</sup> & 2<sup>4</sup> & 2<sup>4</sup> & 69 & 16 & 16 & 79 & 19 & 19 & 106 & 23 & 23 \\
2<sup>4</sup> & 2<sup>4</sup> & 2<sup>5</sup> & 103 & 16 & 16 & 116 & 20 & 20 & 155 & 25 & 25 \\
2<sup>5</sup> & 2<sup>5</sup> & 2<sup>2</sup> & 91 & 18 & 18 & 102 & 20 & 20 & 124 & 20 & 20 \\
2<sup>5</sup> & 2<sup>5</sup> & 2<sup>3</sup> & 101 & 18 & 18 & 112 & 22 & 22 & 145 & 24 & 24 \\
2<sup>5</sup> & 2<sup>5</sup> & 2<sup>4</sup> & 118 & 18 & 18 & 139 & 23 & 23 & 189 & 29 & 29 \\
2<sup>5</sup> & 2<sup>5</sup> & 2<sup>5</sup> & 160 & 19 & 18 & 187 & 24 & 24 & 268 & 31 & 31 \\
\end{tabular}

8.8: Iterations required for solving the unpreconditioned _A_ and preconditioned linear system with \(\widetilde{P}=\widetilde{P}_{\alpha,\mathbf{n},M}\) and \(\widehat{P}=\widehat{P}_{\alpha,\mathbf{n},M}\) with the GMRES method - _a(x_<sub>1</sub>_,x_<sub>2</sub>)=1, \(\theta=0.5\).


## 7. Conclusion

In this paper, we investigated all-at-once linear systems arising from variable-coefficient fractional evolution equations with weakly singular temporal kernels and Riemann-Liouville space fractional derivatives. The temporal discretization was carried out using the L1 scheme, while the spatial fractional operator was approximated through finite difference techniques, leading to large structured (_d_+1)-level Toeplitz-like systems, where one level corresponds to the temporal discretization and the remaining _d_ levels arise from the spatial discretization. In this work, we focused on the case _d_=1, resulting in a two-level block structured system. Using the GLT framework, we analyzed the asymptotic spectral distribution of the resulting matrix sequences and derived the associated GLT symbols for both the spatial and temporal discretization operators.

Motivated by the structure of the coefficient matrix, we proposed a block lower triangular preconditioner obtained by simplifying the upper triangular part of the spatial operator while preserving the main spectral properties of the original system. The theoretical analysis showed that the preconditioned matrix sequence are well clustered in the sense of the singular values

The numerical experiments confirmed the effectiveness of the proposed preconditioning strategy for both constant and variable diffusion coefficients. In all tested cases, the preconditioners significantly reduced the condition numbers of the discretized systems and improved the convergence behavior of the<tbc>

\begin{tabular}{cccccccccccc}
 & & \multicolumn{10}{c}{\(\alpha=1.9\)} \\
 & & \multicolumn{4}{c}{\(\beta=0.1\)} & \multicolumn{3}{c}{\(\beta=0.5\)} & \multicolumn{3}{c}{\(\beta=0.9\)} \\
_N_ & _M_ & - & \(P_{\alpha,\beta,NM}\) & \(P_{\omega,\alpha,\beta,MN}\) & - & \(P_{\alpha,\beta,NM}\) & \(P_{\omega,\alpha,\beta,MN}\) & - & \(P_{\alpha,\beta,NM}\) & \(P_{\omega,\alpha,\beta,MN}\) \\
2<sup>4</sup> & 2<sup>4</sup> & 38.00 & 19.00 & 18.00 & 59.00 & 21.00 & 21.00 & 85.00 & 19.00 & 20.00 \\
2<sup>5</sup> & 2<sup>4</sup> & 74.00 & 20.00 & 19.00 & 105.00 & 21.00 & 21.00 & 151.00 & 20.00 & 21.00 \\
2<sup>6</sup> & 2<sup>4</sup> & 132.00 & 20.00 & 20.00 & 193.00 & 21.00 & 21.00 & 272.00 & 21.00 & 21.00 \\
2<sup>7</sup> & 2<sup>4</sup> & 253.00 & 19.00 & 19.00 & 340.00 & 21.00 & 21.00 & 488.00 & 21.00 & 21.00 \\
2<sup>8</sup> & 2<sup>4</sup> & 471.00 & 20.00 & 19.00 & 500.00 & 20.00 & 20.00 & 500.00 & 20.00 & 21.00 \\
2<sup>4</sup> & 2<sup>5</sup> & 38.00 & 20.00 & 19.00 & 61.00 & 25.00 & 25.00 & 106.00 & 21.00 & 22.00 \\
2<sup>5</sup> & 2<sup>5</sup> & 74.00 & 21.00 & 20.00 & 111.00 & 28.00 & 27.00 & 186.00 & 24.00 & 25.00 \\
2<sup>6</sup> & 2<sup>5</sup> & 132.00 & 22.00 & 22.00 & 196.00 & 30.00 & 29.00 & 330.00 & 26.00 & 27.00 \\
2<sup>7</sup> & 2<sup>5</sup> & 252.00 & 21.00 & 20.00 & 347.00 & 31.00 & 30.00 & 500.00 & 28.00 & 29.00 \\
2<sup>8</sup> & 2<sup>5</sup> & 465.00 & 22.00 & 21.00 & 500.00 & 30.00 & 29.00 & 500.00 & 29.00 & 31.00 \\
2<sup>4</sup> & 2<sup>6</sup> & 38.00 & 21.00 & 20.00 & 64.00 & 27.00 & 26.00 & 135.00 & 23.00 & 23.00 \\
2<sup>5</sup> & 2<sup>6</sup> & 74.00 & 22.00 & 21.00 & 112.00 & 31.00 & 30.00 & 231.00 & 26.00 & 26.00 \\
2<sup>6</sup> & 2<sup>6</sup> & 133.00 & 24.00 & 23.00 & 201.00 & 34.00 & 33.00 & 407.00 & 29.00 & 30.00 \\
2<sup>7</sup> & 2<sup>6</sup> & 252.00 & 23.00 & 22.00 & 348.00 & 36.00 & 34.00 & 500.00 & 32.00 & 34.00 \\
2<sup>8</sup> & 2<sup>6</sup> & 461.00 & 23.00 & 22.00 & 500.00 & 35.00 & 34.00 & 500.00 & 34.00 & 36.00 \\
2<sup>4</sup> & 2<sup>7</sup> & 38.00 & 22.00 & 21.00 & 65.00 & 29.00 & 28.00 & 178.00 & 23.00 & 24.00 \\
2<sup>5</sup> & 2<sup>7</sup> & 74.00 & 23.00 & 22.00 & 115.00 & 33.00 & 31.00 & 294.00 & 27.00 & 28.00 \\
2<sup>6</sup> & 2<sup>7</sup> & 133.00 & 25.00 & 24.00 & 205.00 & 37.00 & 35.00 & 500.00 & 31.00 & 32.00 \\
2<sup>7</sup> & 2<sup>7</sup> & 252.00 & 24.00 & 23.00 & 350.00 & 39.00 & 36.00 & 500.00 & 35.00 & 37.00 \\
2<sup>8</sup> & 2<sup>7</sup> & 459.00 & 24.00 & 23.00 & 500.00 & 39.00 & 38.00 & 500.00 & 36.00 & 40.00 \\
2<sup>4</sup> & 2<sup>8</sup> & 38.00 & 23.00 & 21.00 & 67.00 & 31.00 & 29.00 & 244.00 & 23.00 & 24.00 \\
2<sup>5</sup> & 2<sup>8</sup> & 74.00 & 24.00 & 23.00 & 117.00 & 34.00 & 33.00 & 384.00 & 27.00 & 29.00 \\
2<sup>6</sup> & 2<sup>8</sup> & 133.00 & 26.00 & 25.00 & 207.00 & 38.00 & 36.00 & 500.00 & 31.00 & 34.00 \\
2<sup>7</sup> & 2<sup>8</sup> & 252.00 & 24.00 & 24.00 & 358.00 & 40.00 & 39.00 & 500.00 & 35.00 & 39.00 \\
2<sup>8</sup> & 2<sup>8</sup> & 458.00 & 25.00 & 24.00 & 500.00 & 42.00 & 41.00 & 500.00 & 37.00 & 43.00 \\
\end{tabular}

12: Number of GMRES iterations without preconditioner, with \(P_{\alpha,\beta,NM}\) circulant preconditioner, and \(P_{\omega,\alpha,\beta,MN}\omega-\)circulant preconditioner - case _a(x_)=_x_<sup>2</sup>+1.


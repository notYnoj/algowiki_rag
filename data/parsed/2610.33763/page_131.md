## 8.4.1 Eigenvalue distribution

We first assess the performance of the preconditioners \(\widetilde{P}_{\alpha,N,M}\) and \(\widehat{P}_{\alpha,N,M}\) by examining their influence on the eigenvalue distribution and condition number of the coefficient matrix. Figure 8.5 presents the eigenvalue plots in the complex plane for different values of the fractional order \(\alpha\), with the problem size fixed at _N=M_=2<sup>6</sup>. The eigenvalues of the unpreconditioned matrix are widely scattered along the positive real axis, indicating poor spectral clustering and, consequently, a high level of ill-conditioning. The behaviour is worsening as the fractional diffusion parameter increases as expected.<br>
As shown in  8.1, the unpreconditioned matrix exhibits rapidly growing 2-norm condition numbers, even for moderate values of _N_ and _M_. Though the condition numbers of the preconditioned matrix remain bounded and stable, it’s not so lower. Indeed, a more refined spectral analysis highlights that the condition number alone does not provide an exhaustive description of the eigenvalues distribution properties. In Figures 8.6-8.7 are reported the eigenvalues of preconditioned matrices \(P_{\alpha,N,M}^{-1}A_{\alpha,N,M}\) and \(\widehat{P}_{\alpha,N,M}^{-1}A_{\alpha,N,M}\) for different values of the fractional order \(\alpha\), with the problem size fixed at _N=M_=2<sup>6</sup>. It evident as we can observe a pronounced clustered distributions around the unity. The same behaviour is observed in the non constant coefficient case: the related matrix sequences not cluster at 1 but at the range of the nice function reported in Theorem 8.6.

\begin{tabular}{ccccccccccc}
 & \multicolumn{4}{c}{\(\alpha=1.3\)} & \multicolumn{4}{c}{\(\alpha=1.5\)} & \multicolumn{3}{c}{\(\alpha=1.8\)} \\
_N_ & _M_ & _A_ & \(\widetilde{P}^{-1}A\) & \(\widehat{P}^{-1}A\) & _A_ & \(\widetilde{P}^{-1}A\) & \(\widehat{P}^{-1}A\) & _A_ & \(\widetilde{P}^{-1}A\) & \(\widehat{P}^{-1}A\) \\
2<sup>4</sup> & 2<sup>4</sup> & 2.013e+02 & 1.727e+01 & 1.953e+01 & 1.634e+02 & 2.662e+01 & 3.238e+01 & 1.483e+02 & 6.765e+01 & 8.167e+01 \\
2<sup>4</sup> & 2<sup>5</sup> & 7.475e+02 & 1.728e+01 & 1.955e+01 & 5.604e+02 & 2.664e+01 & 3.241e+01 & 3.957e+02 & 6.770e+01 & 8.173e+01 \\
2<sup>4</sup> & 2<sup>6</sup> & 2.937e+03 & 1.729e+01 & 1.955e+01 & 2.160e+03 & 2.664e+01 & 3.241e+01 & 1.417e+03 & 6.771e+01 & 8.174e+01 \\
2<sup>4</sup> & 2<sup>7</sup> & 1.170e+04 & 1.729e+01 & 1.955e+01 & 8.562e+03 & 2.665e+01 & 3.241e+01 & 5.520e+03 & 6.772e+01 & 8.175e+01 \\
2<sup>5</sup> & 2<sup>4</sup> & 2.352e+02 & 3.878e+01 & 4.367e+01 & 2.273e+02 & 6.930e+01 & 8.360e+01 & 3.173e+02 & 2.190e+02 & 2.604e+02 \\
2<sup>5</sup> & 2<sup>5</sup> & 7.854e+02 & 3.882e+01 & 4.372e+01 & 6.177e+02 & 6.937e+01 & 8.367e+01 & 5.477e+02 & 2.191e+02 & 2.606e+02 \\
2<sup>5</sup> & 2<sup>6</sup> & 3.007e+03 & 3.883e+01 & 4.373e+01 & 2.226e+03 & 6.938e+01 & 8.369e+01 & 1.548e+03 & 2.192e+02 & 2.607e+02 \\
2<sup>5</sup> & 2<sup>7</sup> & 1.190e+04 & 3.883e+01 & 4.373e+01 & 8.684e+03 & 6.939e+01 & 8.370e+01 & 5.650e+03 & 2.192e+02 & 2.607e+02 \\
2<sup>6</sup> & 2<sup>4</sup> & 3.221e+02 & 9.102e+01 & 1.023e+02 & 4.187e+02 & 1.878e+02 & 2.256e+02 & 9.089e+02 & 7.328e+02 & 8.655e+02 \\
2<sup>6</sup> & 2<sup>5</sup> & 8.632e+02 & 9.113e+01 & 1.024e+02 & 7.886e+02 & 1.880e+02 & 2.258e+02 & 1.123e+03 & 7.334e+02 & 8.661e+02 \\
2<sup>6</sup> & 2<sup>6</sup> & 3.096e+03 & 9.115e+01 & 1.024e+02 & 2.379e+03 & 1.880e+02 & 2.258e+02 & 2.057e+03 & 7.335e+02 & 8.663e+02 \\
2<sup>6</sup> & 2<sup>7</sup> & 1.206e+04 & 9.116e+01 & 1.024e+02 & 8.859e+03 & 1.880e+02 & 2.258e+02 & 6.088e+03 & 7.336e+02 & 8.664e+02 \\
2<sup>7</sup> & 2<sup>4</sup> & 5.478e+02 & 2.189e+02 & 2.457e+02 & 9.705e+02 & 5.199e+02 & 6.231e+02 & 2.959e+03 & 2.495e+03 & 2.936e+03 \\
2<sup>7</sup> & 2<sup>5</sup> & 1.064e+03 & 2.191e+02 & 2.460e+02 & 1.317e+03 & 5.204e+02 & 6.237e+02 & 3.166e+03 & 2.497e+03 & 2.938e+03 \\
2<sup>7</sup> & 2<sup>6</sup> & 3.276e+03 & 2.192e+02 & 2.461e+02 & 2.836e+03 & 5.205e+02 & 6.238e+02 & 4.029e+03 & 2.497e+03 & 2.939e+03 \\
2<sup>7</sup> & 2<sup>7</sup> & 1.227e+04 & 2.192e+02 & 2.461e+02 & 9.270e+03 & 5.205e+02 & 6.239e+02 & 7.811e+03 & 2.497e+03 & 2.939e+03 \\
\end{tabular}

8.1: Spectral condition numbers of unpreconditioned _A_ and preconditioned matrices \(\widetilde{P}^{-1}A=\widetilde{P}_{\alpha,N,M}^{-1}A_{\alpha,N,M}\) and \(\widehat{P}^{-1}A=\widehat{P}_{\alpha,N,M}^{-1}A_{\alpha,N,M}\) - case _a(x_)=1.


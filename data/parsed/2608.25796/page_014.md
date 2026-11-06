## 6. Numerical Results

In the present section we perform extensive numerical experiments concerning the Krylov precondition related to **Technique 1** and **Technique 2**. More precisely,  1- 6 concern the number of the preconditioned GMRES in **Technique 1** and  7- 12 concern the number of the preconditioned GMRES in **Technique 2** for the global linear systems.

In all the considered cases, irrespectively of the chosen parameters \(\alpha\), \(\beta\), _a(x_), we can appreciated that the number of iterations stabilizes to a given constant independent of the matrix size. These constants are mild and are a bit more pronounced when \(\beta\) is close to 2. The optimality of the preconditioning preconditioned GMRES is a confirmation that the total arithmetic cost is optimal with **Technique 2**, since it grows in order as a bivariate FFT.

\begin{tabular}{ccccccccccc}
 & & \multicolumn{8}{c}{\(\alpha=1.1\)} \\
 & & \multicolumn{3}{c}{\(\beta=0.1\)} & \multicolumn{3}{c}{\(\beta=0.5\)} & \multicolumn{3}{c}{\(\beta=0.9\)} \\
_N_ & _M_ & - & \(P_{\alpha,N}\) & \(P_{\omega,\alpha,N}\) & - & \(P_{\alpha,N}\) & \(P_{\omega,\alpha,N}\) & - & \(P_{\alpha,N}\) & \(P_{\omega,\alpha,N}\) \\
2<sup>4</sup> & 2<sup>4</sup> & 16.00 & 4.00 & 4.00 & 16.00 & 4.00 & 4.00 & 16.00 & 4.00 & 4.00 \\
2<sup>5</sup> & 2<sup>4</sup> & 32.00 & 4.00 & 4.00 & 32.00 & 5.00 & 4.00 & 32.00 & 4.00 & 4.00 \\
2<sup>6</sup> & 2<sup>4</sup> & 64.00 & 4.00 & 4.00 & 64.00 & 5.00 & 4.00 & 64.00 & 4.06 & 4.00 \\
2<sup>7</sup> & 2<sup>4</sup> & 128.00 & 5.00 & 4.00 & 128.00 & 5.00 & 4.00 & 128.00 & 5.00 & 4.00 \\
2<sup>8</sup> & 2<sup>4</sup> & 256.00 & 5.00 & 4.00 & 256.00 & 5.00 & 4.00 & 256.00 & 5.00 & 4.00 \\
2<sup>4</sup> & 2<sup>5</sup> & 16.00 & 4.00 & 4.00 & 16.00 & 4.00 & 4.00 & 16.00 & 4.00 & 4.00 \\
2<sup>5</sup> & 2<sup>5</sup> & 32.00 & 4.00 & 4.00 & 32.00 & 4.09 & 4.00 & 32.00 & 4.00 & 4.00 \\
2<sup>6</sup> & 2<sup>5</sup> & 64.00 & 4.00 & 4.00 & 64.00 & 5.00 & 4.00 & 62.12 & 4.00 & 4.00 \\
2<sup>7</sup> & 2<sup>5</sup> & 128.00 & 5.00 & 4.00 & 128.00 & 5.00 & 4.00 & 117.22 & 4.09 & 4.00 \\
2<sup>8</sup> & 2<sup>5</sup> & 256.00 & 5.00 & 4.00 & 256.00 & 5.00 & 4.00 & 225.31 & 5.00 & 4.00 \\
2<sup>4</sup> & 2<sup>6</sup> & 16.00 & 4.00 & 4.00 & 16.00 & 4.00 & 4.00 & 14.00 & 4.00 & 4.00 \\
2<sup>5</sup> & 2<sup>6</sup> & 32.00 & 4.00 & 4.00 & 32.00 & 4.02 & 4.00 & 22.03 & 4.00 & 4.00 \\
2<sup>6</sup> & 2<sup>6</sup> & 64.00 & 5.00 & 4.00 & 64.00 & 5.00 & 4.00 & 38.05 & 4.00 & 4.00 \\
2<sup>7</sup> & 2<sup>6</sup> & 128.00 & 5.00 & 4.00 & 128.00 & 5.00 & 4.00 & 70.03 & 4.00 & 4.00 \\
2<sup>8</sup> & 2<sup>6</sup> & 256.00 & 5.00 & 4.00 & 256.00 & 5.00 & 4.00 & 132.06 & 4.03 & 4.00 \\
2<sup>4</sup> & 2<sup>7</sup> & 16.00 & 4.00 & 4.00 & 16.00 & 4.00 & 4.00 & 10.00 & 4.00 & 4.00 \\
2<sup>5</sup> & 2<sup>7</sup> & 32.00 & 4.00 & 4.00 & 32.00 & 4.00 & 4.00 & 15.00 & 4.00 & 4.00 \\
2<sup>6</sup> & 2<sup>7</sup> & 64.00 & 5.00 & 4.00 & 64.00 & 4.01 & 4.00 & 24.01 & 4.00 & 4.00 \\
2<sup>7</sup> & 2<sup>7</sup> & 128.00 & 5.00 & 4.00 & 128.00 & 5.00 & 4.00 & 42.01 & 4.00 & 4.00 \\
2<sup>8</sup> & 2<sup>7</sup> & 256.00 & 5.00 & 4.00 & 256.00 & 5.00 & 4.00 & 77.03 & 4.00 & 4.00 \\
2<sup>4</sup> & 2<sup>8</sup> & 16.00 & 4.00 & 4.00 & 16.00 & 4.00 & 4.00 & 8.00 & 4.00 & 3.00 \\
2<sup>5</sup> & 2<sup>8</sup> & 32.00 & 4.00 & 4.00 & 32.00 & 4.00 & 4.00 & 11.00 & 4.00 & 4.00 \\
2<sup>6</sup> & 2<sup>8</sup> & 64.00 & 5.00 & 4.00 & 64.00 & 4.00 & 4.00 & 16.00 & 4.00 & 4.00 \\
2<sup>7</sup> & 2<sup>8</sup> & 128.00 & 5.00 & 4.00 & 128.00 & 5.00 & 4.00 & 26.00 & 4.00 & 4.00 \\
2<sup>8</sup> & 2<sup>8</sup> & 256.00 & 5.00 & 4.00 & 256.00 & 5.00 & 4.00 & 46.00 & 4.00 & 4.00 \\
\end{tabular}

1: Averaged number of GMRES iterations in forward block solution without preconditioner, with \(P_{\alpha,N}\) circulant preconditioner, and \(P_{\omega,\alpha,N}\omega-\)circulant preconditioner - case _a(x_)=1.


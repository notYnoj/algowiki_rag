where the matrices _H<sub>M</sub>_ and \(H_{\theta,M}\) are defined as follows<tbc>

\(H_M=\left[\begin{array}{ c c c c }
1 &  &  &  \\
-1 & 1 &  &  \\
 & \ddots & \ddots &  \\
 &  & -1 & 1
\end{array}\right]\in\mathbb{R}^{M\times M},H_{\theta,M}=-\left[\begin{array}{ c c c c }
\theta &  &  &  \\
1-\theta & \theta &  &  \\
 & \ddots & \ddots &  \\
 &  & 1-\theta & \theta
\end{array}\right]\in\mathbb{R}^{M\times M}.\)

<tbc>To calculate the solution of (8.12) in a parallel pattern form, we exchange the order of the Kronecker product in \(\bar{A}\). This leads to an equivalent system<tbc>

\(\widetilde{A}\widetilde{\mathbf{u}}=\widetilde{\mathbf{f}},\) (8.14)

<tbc>where<tbc>

\(\widetilde{A}=G_{\alpha,N}\otimes H_{\theta,M}+I_N\otimes H_M,\)

<tbc>and \(\widetilde{\mathbf{f}}\) is obtained by reshaping \(\bar{\mathbf{f}}\in\mathbb{R}^{NM}\) into an \(N\times M\) matrix and then stacking its rows into a single column \(MN\times 1\) vector. Equivalently, \(\widetilde{\mathbf{f}}\) is formed by stacking the columns of the transpose of the reshaped matrix.<br>
By pre-multiplying both sides of (8.14) with \((I_N\otimes H_{\theta,M})^{-1}\), we obtain an equivalent formulation<tbc>

\(A_{\alpha,N,M}\mathbf{u}=\mathbf{f},\) (8.15)

<tbc>where<tbc>

\(A_{\alpha,N,M}=G_{\alpha,N}\otimes I_M+I_N\otimes H_{\theta,M}^{-1}H_M=G_{\alpha,N}\otimes I_M+I_N\otimes Q_{\theta,M},\)

<tbc>with the matrix \(Q_{\theta,M}=H_{\theta,M}^{-1}H_M\) defined as

\(Q_{\theta,M}=-\left[\begin{array}{ c c c c c }
\frac{1}{\theta} &  &  &  &  \\
\frac{-1}{\theta^2} &  & \frac{1}{\theta} &  &  \\
\frac{-(\theta-1)}{\theta^3} &  & \frac{-1}{\theta^2} &  & \frac{1}{\theta} &  \\
\vdots & \ddots & \ddots & \ddots &  \\
\vdots & \ddots & \frac{-(\theta-1)}{\theta^3} &  & \frac{-1}{\theta^2} & \frac{1}{\theta}
\end{array}\right]\in\mathbb{R}^{M\times M}.\) (8.16)

The transformed right-hand side is given by \(\mathbf{f}=(I_N\otimes H_{\theta,M})^{-1}\widetilde{\mathbf{f}}=(I_N\otimes H_{\theta,M}^{-1})\widetilde{\mathbf{f}}\).

## Two-dimensional

Let _N_<sub>1</sub>, _N_<sub>2</sub> and _M_ be positive integers representing the number of interior spatial and temporal steps, respectively. The spatial and temporal meshes are defined as

\(x_i=L_1+i\Delta x,\Delta x=\frac{(R_1-L_1)}{(N_1+1)},0\le i\le N_1+1,\)<br>
\(y_j=L_2+j\Delta y,\Delta y=\frac{(R_2-L_2)}{(N_2+1)},0\le j\le N_2+1,\)<br>
\(t_m=m\Delta t,\Delta t=\frac{T}{M},0\le m\le M.\)


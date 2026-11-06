<tbc>Substituting the block form (41) into (44), we obtain

\(\Psi\left(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\right)=\left[\prod_{i=1}^n\left(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}-\lambda_iI\right)\right]\left(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}-I\right)\)<br>
\(=\left[\prod_{i=1}^n\left[\begin{array}{ c c }
\Theta_1-\lambda_iI & \Theta_2 \\
0 & (1-\lambda_i)I
\end{array}\right]\right]\left[\begin{array}{ c c }
\Theta_1-I & \Theta_2 \\
0 & 0
\end{array}\right]\) (45)

\(=\left[\prod_{i=1}^n(\Theta_1-\lambda_iI)(\Theta_1-I)\prod_{i=1}^n(\Theta_1-\lambda_iI)\Theta_2 \\
0 & 0
\end{array}\right]\) (46)

According to the Cayley-Hamilton theorem, the matrix \(\Theta_1\) satisfies its own characteristic equation, meaning \(\prod_{i=1}^n(\Theta_1-\lambda_iI)=0\). Substituting this into (46), we obtain

\(\Psi\left(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\right)=\left[\begin{array}{ c c }
0 & 0 \\
0 & 0
\end{array}\right].\) (47)

Therefore, the degree of the minimal polynomial of the preconditioned matrix \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\) is at most _n_+1.

**Remark 2.** _The theoretical results in Theorem 5 determine the convergence behavior of a Krylov subspace method, such as GMRES \[28\]. Theorem 5 shows that with the VBP preconditioner_ P<sub>VBP</sub>_, termination (in exact arithmetic) of the GMRES method will occur in at most n_+1 _steps for any choice of the right hand side_ **d**.

## 4 Parameter selection

The overall efficiency of the P<sub>VBP</sub> is highly sensitive to the selection of the two parameters \(\alpha\) and \(\gamma\). Therefore, to achieve optimal performance, it is crucial to establish an effective method for estimating these values within the VBP framework.

As indicated by (8), the deviation between the preconditioner P<sub>VBP</sub> and the matrix A highlights the need for proper parameter tuning. Ideally, these parameters should be chosen to minimize this distance, ensuring that the preconditioner closely approximates the original coefficient matrix. Although several strategies for parameter selection have been explored in the literature (see, e.g., \[4, 10, 14, 20\]), this study adopts the algebraic estimation technique proposed by Huang \[20\] to determine the practical values of \(\alpha\) and \(\gamma\). Based on Eq. (48), we have R as follows

\(\mathscr{R}_\mathrm{VBP}=\left[\begin{array}{ c c }
\alpha I-\gamma W^2 & W-\gamma WT \\
0 & 0
\end{array}\right].\) (48)

To determine the quasi-optimal parameters, we aim to minimize the overall distance between the preconditioner and the original matrix. Therefore, we introduce an objective function


<tbc>We now check that our critical point is a local minimum. For \(\alpha\in[-\frac{1}{6},\frac{1}{6}]^2\), \(\eta\in(-\frac{1}{2},\frac{1}{2})^3\) verifying \(\alpha_1+\alpha_2\ge 0\), we compute the Hessian of E<sub>3</sub>:

\(H^+(\alpha,\eta)=\left(\begin{array}{ c c c c }
0 & 0 & 2\eta_1 & 2\varepsilon-2 & -2\eta_3-2\varepsilon \\
0 & 0 & 0 & 2\eta_2+2\varepsilon-2 & -2\eta_3-2\varepsilon \\
2\eta_1 & 0 & 2\alpha_1+\frac{1}{3} & 0 & 0 \\
2\varepsilon-2 & 2\eta_2+2\varepsilon-2 & 0 & 2\alpha_2+\frac{1}{3} & 0 \\
-2\eta_3-2\varepsilon & -2\eta_3-2\varepsilon & 0 & 0 & -2\alpha_1-2\alpha_2+\frac{4}{3}
\end{array}\right).\) (72)

Using numerical solvers, we obtain that at \((\alpha,\eta)=(0_{\mathbb{R}^2},0_{\mathbb{R}^3})\), the Hessian verifies the following property:

\(H^+(0_{\mathbb{R}^2},0_{\mathbb{R}^3})v=0,v:=(1,-1,0,0,0),\forall w\in v^\perp,w^\top H^+(0_{\mathbb{R}^2},0_{\mathbb{R}^3})w>0.\) (73)

Adding the vector _tv_ to \((\alpha,\eta)\) for |_t_| small enough corresponds to adding _t_ to \(\alpha_1\) and subtracting _t_ from \(\alpha_2\), and we notice that at \((\alpha,\eta)=(0_{\mathbb{R}^2},0_{\mathbb{R}^3})\), since \(\eta_1=\eta_2\), this operation does not change the cost: E<sub>3</sub>((_t,-t),_0<sub>R<sup>3</sup></sub>)=E<sub>3</sub>(0<sub>R<sup>2</sup></sub>,0<sub>R<sup>3</sup></sub>). We conclude that (0<sub>R<sup>2</sup></sub>,0<sub>R<sup>3</sup></sub>) is a local minimum for the problem \(\mathcal{E}_3^+\) defined in Eq. (69).

## Case \(\alpha_1+\alpha_2\le 0\).

For any \((\alpha,\eta)\in[-\frac{1}{6},\frac{1}{6}]^2\times(-\frac{1}{2},\frac{1}{2})^3\) such that \(\alpha_1+\alpha_2\le 0\) and \(\eta_1\le\eta_2\), the optimal plan between \(\mu_{\alpha,\eta}\) and \(\nu\) and the associated energy E<sub>3</sub> are given by:

\(\pi^-(\alpha,\eta)=\left(\begin{array}{ c c c c }
\frac{1}{6}+\alpha_1 & 0 & 0 \\
\frac{1}{6}+\alpha_2 & 0 & 0 \\
-\alpha_1-\alpha_2 & \frac{1}{3} & \frac{1}{3}
\end{array}\right),\)<br>
\(\mathcal{E}_3(\alpha,\eta)=\left(\frac{1}{6}+\alpha_1\right)\eta_1^2+\left(\frac{1}{6}+\alpha_2\right)\eta_2^2-\left(\alpha_1+\alpha_2\right)\left(1+\eta_3\right)^2+\frac{1}{3}\left(\eta_3+\varepsilon\right)^2+\frac{1}{3}(\eta_3-\varepsilon)^2.\)

We deduce the expression of the Lagrangian of the problem \(\mathcal{E}_3^-\) defined in Eq. (69):

\(\mathcal{L}^-(\alpha,\eta,\lambda_1,\lambda_2)=\mathcal{E}_3(\alpha,\eta)+\lambda_1(\alpha_1+\alpha_2)+\lambda_2(\eta_1-\eta_2).\) (74)

The KKT stationarity condition writes then:

\(0=\frac{\partial\mathcal{L}^-}{\partial\alpha_1}=\eta_1^2-\left(1+\eta_3\right)^2+\lambda_1;\)<br>
\(0=\frac{\partial\mathcal{L}^-}{\partial\alpha_2}=\eta_2^2-\left(1+\eta_3\right)^2+\lambda_1;\)<br>
\(0=\frac{\partial\mathcal{L}^-}{\partial\eta_1}=2\left(\frac{1}{6}+\alpha_1\right)\eta_1+\lambda_2;\)<br>
\(0=\frac{\partial\mathcal{L}^-}{\partial\eta_2}=2\left(\frac{1}{6}-\alpha_1\right)\eta_2-\lambda_2;\)<br>
\(0=\frac{\partial\mathcal{L}^-}{\partial\eta_3}=-2\left(\alpha_1+\alpha_2\right)\left(1+\eta_3\right)+\frac{4}{3}\eta_3.\)

Again the primal / dual feasibility conditions read:<tbc>

\(\alpha_1+\alpha_2\le 0,\eta_1\le\eta_2,\lambda_1\ge 0,\lambda_2\ge 0,\)

<tbc>and the complementary slackness conditions:

\(\lambda_1(\alpha_1+\alpha_2)=0,\lambda_2(\eta_1-\eta_2)=0.\)

Likewise, the point \((\alpha,\eta,\lambda_1,\lambda_2)=(0_{\mathbb{R}^2},0_{\mathbb{R}^3},1,0)\) is a solution of the KKT system.


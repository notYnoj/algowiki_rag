results in \[24, 34, 35\] that its eigenvalues can be determined from the so-called generating function of T . According to these results, YT is symmetric indefinite when _n_ is large enough, which accounts for the use of MINRES instead of a HPD Krylov subspace method like the conjugate gradient method in this work. For complete surveys on generating functions as well as other properties of block multilevel Toeplitz matrices, we refer readers to \[5, 6, 18, 19, 38\] and the references therein.

Proposed in \[32\], the following block \(\alpha\)-circulant preconditioner can be constructed as an approximation to T :

\(\mathcal{C}_\alpha=\left[\begin{array}{ c c c c c c c c }
L &  &  &  & \alpha L &  & -2\alpha I_m \\
-2I_m & L &  &  &  & \alpha L &  \\
L &  & -2I_m & L &  &  &  \\
 & \ddots & \ddots & \ddots &  &  &  \\
 &  &  & L &  & -2I_m & L
\end{array}\right].\) (1.5)

Clearly, \(\mathcal{C}_\alpha\) is not symmetric and, thus, not HPD. However, Krylov subspace solvers (e.g., MINRES) for symmetric linear systems typically require an HPD preconditioner for maintaining the short-recurrence property. Therefore, \(\mathcal{C}_\alpha\) is not a suitable preconditioner for the symmetric linear system (1.3).

To address this issue of positive definiteness, we first note that \(\mathcal{C}_\alpha\) is diagonalizable for \(\alpha\in(0,1)\). To see this, we can rewrite \(\mathcal{C}_\alpha\) as<tbc>

\(\mathcal{C}_\alpha=B_1^{(\alpha)}\otimes L+B_2^{(\alpha)}\otimes(-2I_m),\) (1.6)

<tbc>where<tbc>

\(B_1^{(\alpha)}=\left[\begin{array}{ c c c c c c c c }
1 &  &  & \alpha & 0 &  & \alpha \\
0 & 1 &  &  & \alpha &  & 1 & 0 \\
1 & 0 & 1 &  &  &  & \\
 & \ddots & \ddots & \ddots &  &  &  \\
 &  &  & 1 & 0 & 1
\end{array}\right],B_2^{(\alpha)}=\left[\begin{array}{ c c c c c c c c }
0 &  &  &  &  & \alpha &  \\
1 & 0 &  &  &  &  &  \\
1 & 0 &  &  &  &  &  \\
 & \ddots & \ddots &  &  &  &  \\
 &  &  &  &  & 1 & 0
\end{array}\right]\in\mathbb{R}^{n\times n}\)

<tbc>According to \[1\], \(B_1^{(\alpha)}\) and \(B_2^{(\alpha)}\) are diagonalizable as follows

\(B_j^{(\alpha)}=D_\alpha^{-1}\mathbb{F}\Lambda_{\alpha,j}\mathbb{F}^*D_\alpha,j=1,2,\)<br>
\(D_\alpha=\mathrm{diag}(\alpha^\frac{i-1}{n})_{i=1}^n,\mathbb{F}=\frac{1}{\sqrt{n}}[\theta_n^{(i-1)(j-1)}]_{i,j=1}^n,\theta_n=\mathrm{exp}\left(\frac{2\pi\mathbf{i}}{n}\right),\mathbf{i}=\sqrt{-1},\)<br>
\(\Lambda_{\alpha,j}=\mathrm{diag}(\lambda_{j,k}^{(\alpha)})_{k=1}^n,j=1,2,\lambda_{1,k}^{(\alpha)}=1+\alpha^\frac{2}{n}\theta_n^{2(k-1)},\lambda_{2,k}^{(\alpha)}=-2\alpha^\frac{1}{n}\theta_n^{k-1}.\)


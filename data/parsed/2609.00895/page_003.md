Choosing the sign of each eigenfunction so that the leading coefficient is positive, the _L_<sub>2</sub>- normalization determines<tbc>

\(K_0=\frac{1}{\sqrt{2}},\)

<tbc>since (3) yields

\(\|v_n\|_{L_2}^2=\int_{-1}^1\left(v_{n,1}^2(x)+v_{n,2}^2(x)\right)dx=2K_0^2+O\left(\frac{1}{n}\right)=1.\)

Moreover, the eigenvalues satisfy \[16\]

\(\lambda_n=\frac{\pi n}{2}-\frac{\widetilde{\theta}}{2}+O\left(\frac{1}{n}\right),n\rightarrow\pm\infty,\) (5)

where

\(\widetilde{\theta}:=\beta-\alpha+\frac{1}{2}\int_{-1}^1(p(\tau)+r(\tau))d\tau.\)

## 1.1 Reduced boundary values

The eigenfunctions satisfy the boundary conditions (2) exactly. Hence, their endpoint values belong to the corresponding one-dimensional boundary subspaces:

\(v_n(1)=\kappa_n^{(+)}\left(\begin{array}{ c }
cos\beta \\
-sin\beta
\end{array}\right),v_n(-1)=\kappa_n^{(-)}\left(\begin{array}{ c }
cos\alpha \\
-sin\alpha
\end{array}\right),\) (6)

for some real scalars \(\kappa_n^{(\pm)}\).

We set

\(\mathcal{A}f:=Jf'-Qf,J=\left(\begin{array}{ c c }
0 & 1 \\
-1 & 0
\end{array}\right),Q(x)=\text{diag}(p(x),r(x)),\)

and define

\(\mathcal{B}f:=-Jf=\left(\begin{array}{ c }
-f_2 \\
f_1
\end{array}\right),f_k:=\mathcal{B}\mathcal{A}^kf=-J\mathcal{A}^kf,k\ge 0.\) (7)

Thus,

\(\mathcal{A}^kf=\left(\begin{array}{ c c }
(\mathcal{A}^kf)_1 &  \\
(\mathcal{A}^kf)_2
\end{array}\right),f_k=\left(\begin{array}{ c }
-(\mathcal{A}^kf)_2 \\
(\mathcal{A}^kf)_1
\end{array}\right).\)

For the remainder of this subsection, let \(q\ge 1\) and assume in addition that

\(f\in C^q([-1,1];\mathbb{R}^2),p,r\in C^q[-1,1],\)

so that A_<sup>k</sup>f_ is continuous for _k_=0_,...,q_. For _k_=0_,...,q_, we define the _reduced boundary values_

\(g_k^\pm:=f_{k,1}(\pm 1)cos\gamma_\pm-f_{k,2}(\pm 1)sin\gamma_\pm,\gamma_+=\beta,\gamma_-=\alpha.\) (8)

Equivalently,<tbc>

\(g_k^\pm=-(\mathcal{A}^kf)_2(\pm 1)cos\gamma_\pm-(\mathcal{A}^kf)_1(\pm 1)sin\gamma_\pm.\)

<tbc>By (6), the boundary terms involving the eigenfunctions reduce to

\(v_n^T(\pm 1)f_k(\pm 1)=\kappa_n^{(\pm)}\left(cos\gamma_\pm-sin\gamma_\pm\right)\left(\begin{array}{ c }
f_{k,1}(\pm 1) \\
f_{k,2}(\pm 1)
\end{array}\right)\)<br>
\(=\kappa_n^{(\pm)}g_k^\pm.\)


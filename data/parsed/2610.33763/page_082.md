_As a consequence,_<tbc>

\(A_N^{(1)}:=P_N^{(1)}A_N=\left[\begin{array}{ c c }
Q_N & -\alpha_m\tilde{\mathbf{q}}\otimes I_n \\
\alpha^{(1)} & \beta^{(1)}
\end{array}\right]\)

<tbc>_with_

\(\alpha^{(1)}:=\big[\mathrm{O}_n|-Q_{m,m}^{-1}Q_{m,m-1}|-Q_{m,m}^{-1}Q_{m,m-2}|\cdots|-Q_{m,m}^{-1}Q_{m,1}\big],\)<br>
\(\beta^{(1)}:=\frac{\lambda}{\beta_n}G_n+\alpha_mq^{(m)}Q_{m,m}^{-1}.\)

_Iterating the block Gaussian steps, at each step k_=2_,...,m we define_<tbc>

\(P_N^{(k)}:=\left[\begin{array}{ c c c }
I_n &  &  \\
 & \ddots &  \\
 & I_n &  \\
\mathbf{p}_1^{(k)} & \cdots & \mathbf{p}_m^{(k)} & I_n
\end{array}\right],\mathbf{p}_j^{(k)}:=\left\{\begin{array}{ c c }
\mathrm{O}_n & \text{\textit{if}}j\neq k \\
-\alpha_k^{(k-1)}Q_{m+1-k,m+1-k}^{-1} & \text{\textit{if}}j=k,
\end{array}\right.\)

<tbc>_so that_<tbc>

\(A_N^{(k)}:=P_N^{(k)}A_N^{(k-1)}=\left[\begin{array}{ c c }
Q_N & \tilde{\mathbf{q}} \\
\alpha_1^{(k)} & \cdots \\
\alpha_m^{(k)} & \beta^{(k)}
\end{array}\right],\)

<tbc>_where_

\(\alpha_j^{(k)}:=\left\{\begin{array}{ c c }
\mathrm{O}_n & \text{\textit{for}}j=1,\dots,k \\
\mathbf{p}_k^{(k)}Q_{m+1-k,m+1-j}+\alpha_j^{(k-1)} & \text{\textit{for}}j=k+1,\dots m,
\end{array}\right.\)<br>
\(\beta^{(k)}:=-\alpha_mq^{(m+1-k)}\mathbf{p}_k^{(k)}+\beta^{(k-1)}.\)

_In conclusion, for k=m we find_<tbc>

\(A_N^{(m)}=\left[\begin{array}{ c c }
Q_N & -\alpha_m\tilde{\mathbf{q}}\otimes I_n \\
\mathrm{O}_{n\times mn} & \beta^{(m)}
\end{array}\right].\)

<tbc>_We are left to analyze the spectrum of_ \(\beta^{(m)}\)_, which by expanding the recursive definition takes the form_

\(\beta^{(m)}=-\sum_{k=1}^m\alpha_mq^{(m+1-k)}\mathbf{p}_k^{(k)}+\frac{\lambda}{\beta_n}G_n.\)

_It is evident that_ \(\beta^{(m)}\) _is a sum of products and inverses of lower triangular matrices, so that it is lower triangular as well. Its non singular character holds if and only if the matrix A<sub>N</sub> is invertible, and the check can be done on the diagonal entries of_ \(\beta^{(m)}\)_. This criterion is easy to check and computationally inexpensive, since it only involves element-wise operations, and in fact it has been checked to hold true in our numerical experiments in Section 6.4._


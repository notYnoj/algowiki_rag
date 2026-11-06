<tbc>Since \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\) and L<sub>VBP</sub> share the same eigenvectors, and by Theorem 1, it follows that \(x\neq 0\). Without loss of generality, we may assume \(\|x\|_2=1\). Premultiplying (31) by _x_<sup>∗</sup> yields the quadratic equation

\(\zeta=\frac{c+b}{c+\alpha},\) (32)

where _c_ and _b_ are as defined in (13).

Thus, \(\zeta\) in (32) is an eigenvalue of \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\), and the corresponding eigenvector is

\(\mathbf{u}=\left[\begin{array}{ c }
x \\
-T^{-1}Wx
\end{array}\right],x\neq 0.\)

In what follows, we prove that the set of eigenvectors corresponding to \(\zeta=1\) and \(\zeta\neq 1\) are linearly independent. First, we determine the number of eigenvectors

• For \(\zeta=1\), since \(y\in\mathbb{R}^n\) is arbitrary, there are exactly _n_ linearly independent vectors, which can be written as<tbc>

<tbc>\(\mathbf{u}_j^{(1)}=\left[\begin{array}{ c }
Ke_j \\
e_j
\end{array}\right],j=1,\dots,n,\)<tbc>

<tbc>where \(\{e_j\}_{j=1}^n\) is the standard basis of R_<sup>n</sup>_.<tbc>

• For \(\zeta\neq 1\), assume there exist _r_ linearly independent vectors<tbc>

<tbc>\(\mathbf{u}_j^{(2)}=\left[\begin{array}{ c }
x_j \\
-T^{-1}Wx_j
\end{array}\right],j=1,\dots,r,\)<tbc>

<tbc>where \(0\le r\le n\) and \(\{x_j\}_{j=1}^r\) is a linearly independent set in R_<sup>n</sup>_.<tbc>

<tbc>Now suppose the following linear combination equals zero<tbc>

\(\sum_{j=1}^nc_j^{(1)}\mathbf{u}_j^{(1)}+\sum_{j=1}^rc_j^{(2)}\mathbf{u}_j^{(2)}=\mathbf{0}.\) (33)

<tbc>Substituting the vector forms, we obtain<tbc>

\(\sum_{j=1}^nc_j^{(1)}\left[\begin{array}{ c }
Ke_j \\
e_j
\end{array}\right]+\sum_{j=1}^rc_j^{(2)}\left[\begin{array}{ c }
x_j \\
-T^{-1}Wx_j
\end{array}\right]=\left[\begin{array}{ c }
0 \\
0
\end{array}\right].\) (34)

<tbc>Since each \(\mathbf{u}_j^{(1)}\) is an eigenvector corresponding to the eigenvalue 1, we have

\(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\mathbf{u}_j^{(1)}=1\cdot\mathbf{u}_j^{(1)}.\)


<tbc>For \((\nu_1,\nu_2)=(1,0)\) the optimality of the transfer operators already follows from \[2, Theorem 4.6\] by using the structure of the matrix _B_ defined by the HPD block diagonal matrix _D_ as in (4.6) and the _B_-normality of _M_<sup>-1</sup>_A_ together with Theorem 3.10.

**4.1. Some remarks.** To emphasize the differences of the two error operators \(E_+^{\nu_1,\nu_2}\) and \(E^{\nu_1,\nu_2}\) and their respective assumptions for convergence, we consider some theoretical examples. These examples shall improve the understanding of the required assumptions and the different structures of the error operators.<br>
In the Theorems 4.8 and 4.10 we considered certain _B_-norms with matrices _B_ that are constructed with block diagonal HPD matrices _D_ of the form (4.6). In the underlying theory from \[16, Theorems 3.3, 3.5\] only diagonal HPD matrices _D_ were allowed. The following example shows a case where \[16, Theorem 3.3\] does not guarantee convergence, but Theorem 4.8 does.

_Example_ 4.11. We consider _n_=3 and _n<sub>c</sub>_=1. Let<tbc>

\(A=\left[\begin{array}{ c c c c }
\frac{7}{8} & -\frac{5}{8} & \frac{5}{8} & \frac{7}{8} \\
-\frac{5}{8} & \frac{7}{8} & \frac{5}{8} & \frac{7}{8} \\
0 & 0 & \frac{3}{2}
\end{array}\right]=\left[\begin{array}{ c c c c }
1 & 0 & 1 \\
1 & 1 & 0 \\
0 & 1 & 1
\end{array}\right]\left[\begin{array}{ c c c }
\frac{1}{4} & \frac{3}{2} & \frac{3}{2}
\end{array}\right]\left[\begin{array}{ c c c c }
1 & 0 & 1 \\
1 & 1 & 0 \\
0 & 1 & 1
\end{array}\right]^{-1},M^{-1}=I_3,\)

<tbc>then _M_<sup>-1</sup>_A=A_ is diagonalizable with eigenvalues \(\lambda_1=\frac{1}{4}\) and \(\lambda_2=\lambda_3=\frac{3}{2}\). The (generalized) right eigenvalues _V<sub>r</sub>_ are given by<tbc>

\(V_r=\left[\begin{array}{ c c c }
1 & 0 & 1 \\
1 & 1 & 0 \\
0 & 1 & 1
\end{array}\right].\)

<tbc>The (generalized) left eigenvectors are the (generalized) right eigenvectors of _A<sup>H</sup>=A<sup>T</sup>_ which are given by<tbc>

\(V_l=\left[\begin{array}{ c c c c }
-1 & -1 & 0 \\
-1 & 1 & 0 \\
1 & 0 & 1
\end{array}\right].\)

<tbc>Let _B_ be given by<tbc>

\(B=\left[\begin{array}{ c c c c }
\frac{5}{8} & -\frac{3}{8} & -\frac{1}{8} \\
-\frac{3}{8} & \frac{5}{8} & -\frac{1}{8} \\
-\frac{1}{8} & -\frac{1}{8} & \frac{7}{24}
\end{array}\right].\)

<tbc>Then _B_ can be written as \(B=V_r^{-H}D^{-1}V_r^{-1}=(V_rDV_r^H)^{-1}\) for<tbc>

\(D=\left[\begin{array}{ c c c c }
2 & 0 & 0 \\
0 & 2 & 1 \\
0 & 1 & 2
\end{array}\right]\)

<tbc>which is an HPD block diagonal matrix with block sizes corresponding to those of the eigenvalue matrix of _A_, that is a \(2\times 2\) block corresponding to the double eigenvalue \(\frac{3}{2}\) and a \(1\times 1\) block corresponding to the eigenvalue \(\frac{1}{4}\). By construction, the matrix _M_<sup>-1</sup>_A_ is _B_-normal (a calculation shows that it even is _B_-orthogonal). We define

\(P_\#=\left[\begin{array}{ c }
1 \\
1 \\
0
\end{array}\right]\text{and}R_\#=\left[\begin{array}{ c }
-1 \\
-1 \\
1
\end{array}\right]\)


<tbc>with \(\|E_+^{1,1}\|_B=1-\mu_2=\frac{1}{4}\) by Theorem 4.1. However, since _M_<sup>-1</sup>_A_ is not _B_-normal, theory does not guarantee the convergence of _E_<sup>1,1</sup>. However, it also holds

\(E^{1,1}=\left[\begin{array}{ c c c }
\frac{1}{4} & 0 & 0 \\
0 & \frac{-\sqrt{3}+3}{24} & \frac{\sqrt{3}-2}{4} \\
0 & \frac{\sqrt{3}}{24} & \frac{-\sqrt{3}+1}{8}
\end{array}\right]\text{with}\|E^{1,1}\|_B=\frac{1}{4}.\)

It is interesting that both of the operators have the same norm.

The example demonstrated that the _B_-normality of _M_<sup>-1</sup>_A_ is not necessary for the convergence of \(E^{\nu_1,\nu_2}\), however the following example shows that the operator requires at least some additional assumption for convergence.

_Example_ 4.13. We consider _n_=3 and _n<sub>c</sub>_=1 and \((\nu_1,\nu_2)=(1,1)\). Let<tbc>

\(A=\left[\begin{array}{ c c c }
\frac{1}{4} & 0 & \frac{1}{12} \\
0 & \frac{1}{2} & 0 \\
0 & 0 & \frac{1}{4}
\end{array}\right]=\left[\begin{array}{ c c c }
1 & 0 & 1 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]\left[\begin{array}{ c c c }
\frac{1}{4} & 0 & 0 \\
0 & \frac{1}{2} & 0 \\
0 & 0 & \frac{1}{3}
\end{array}\right]\left[\begin{array}{ c c c }
1 & 0 & 1 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]^{-1}=V_r\Lambda V_r^{-1}\)

<tbc>and _M=I_<sub>3</sub>. Further let<tbc>

\(B=\left[\begin{array}{ c c c }
4 & 0 & 0 \\
0 & 2 & 1 \\
0 & 1 & 1
\end{array}\right].\)

<tbc>Then _B_ is HPD and _M_<sup>-1</sup>_A=A_ is diagonalizable. However, _M_<sup>-1</sup>_A_ is not _B_-normal because _B_ does not have the required structure as in Theorem 2.9 (5). We have<tbc>

\(\widehat{M}^{-1}B=\left[\begin{array}{ c c c }
\frac{55}{144} & \frac{1}{36} & \frac{5}{72} \\
-\frac{1}{6} & \frac{5}{6} & \frac{1}{12} \\
\frac{4}{9} & -\frac{2}{9} & \frac{4}{9}
\end{array}\right]\)

<tbc>which has eigenvalues in the interval (0,1\]. By Theorem 3.5 the smoothing assumption is then satisfied. Choosing \(\hat{P}\) and \(\hat{R}\) as in Theorem 4.1, the theorem also implies the convergence of \(E_+^{1,1}\), that is \(\|E_+^{1,1}(\hat{P},\hat{R})\|_B<1\). But the error operator _E_<sup>1,1</sup> does not convergence. The left eigenvectors of _M_<sup>-1</sup>_A_ are given by<tbc>

\(V_l=\left[\begin{array}{ c c c }
1 & 0 & 0 \\
0 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right].\)

<tbc>We set \(P_\#=\left[\begin{array}{ c }
1 \\
0
\end{array}\right]\) and \(R_\#=\left[\begin{array}{ c }
1 \\
0 \\
-1
\end{array}\right]\) and obtain<tbc>

\(E^{1,1}(P_\#,R_\#)=\left[\begin{array}{ c c c }
\frac{3}{4} & 0 & -\frac{1}{12} \\
0 & \frac{1}{2} & 0 \\
0 & 0 & \frac{2}{3}
\end{array}\right]\left[\begin{array}{ c c c }
0 & 0 & 1 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]\left[\begin{array}{ c c c }
\frac{3}{4} & 0 & -\frac{1}{12} \\
0 & \frac{1}{2} & 0 \\
0 & 0 & \frac{2}{3}
\end{array}\right]=\left[\begin{array}{ c c c }
0 & 0 & \frac{4}{9} \\
0 & \frac{1}{4} & 0 \\
0 & 0 & \frac{4}{9}
\end{array}\right]\)

<tbc>with

\(\|E^{1,1}(P_\#,R_\#)\|_B=\sqrt{\frac{\sqrt{1294465}+1217}{1296}}\approx 1.34794>1.\)

Therefore, _E_<sup>1,1</sup> does not convergence. This is due to the fact that \(\|\Pi_A(P_\#,R_\#)\|_B=3>1\) and \(\Pi_A(P_\#,R_\#)\) is not _B_-orthogonal for this choice of interpolation and restriction. Increasing the (1,1)-entry of _B_ further increases the _B_-norm of \(\Pi_A(P_\#,R_\#)\).


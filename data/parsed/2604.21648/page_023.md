<tbc>and obtain<tbc>

\(\Pi_A(P_\#,R_\#)=\left[\begin{array}{ c c c }
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 0
\end{array}\right]\)

<tbc>which is _B_-orthogonal since \(\Pi_A(P_\#,R_\#)^+=\Pi_A(P_\#,R_\#)\). The eigenvalues \(\lambda\) are ordered so that \(|1-\lambda_1|\ge|1-\lambda_2|\ge|1-\lambda_3|\). Then we can apply Theorem 4.8 and obtain

\(\rho(E^{\nu_1,\nu_2}(P_\#,R_\#)=\|E^{\nu_1,\nu_2}(P_\#,R_\#)\|_B=|1-\lambda_2|^{\nu_1+\nu_2}=\frac{1}{2^{\nu_1+\nu_2}}.\)

This result cannot be obtained by \[16, Theorem 3.3\] because _D_ is not a diagonal matrix but has a block diagonal form.

The next example illustrates a case where _M_<sup>-1</sup>_A_ is not _B_-normal for any HPD matrix _B_ and therefore our convergence analysis only guarantees the convergence of \(E_+^{\nu_1,\nu_2}\) with \((\nu_1,\nu_2)\in\{(0,1),(1,0),(1,1)\}\) but not of \(E^{\nu_1,\nu_2}\). The example uses a matrix _M_<sup>-1</sup>_A_ which is not diagonalizable and thus cannot be _B_-normal.

_Example_ 4.12. We consider _n_=3 and _n<sub>c</sub>_=1 again. Let \((\nu_1,\nu_2)=(1,1)\) and<tbc>

\(A=\left[\begin{array}{ c c c }
\frac{1}{2} & 0 & 0 \\
0 & \frac{1}{2} & 1 \\
0 & 0 & \frac{1}{2}
\end{array}\right],M^{-1}=I_3\text{and}B=\left[\begin{array}{ c c c }
1 & 0 & 0 \\
0 & 1 & -2 \\
0 & -2 & 6
\end{array}\right]\)

<tbc>then _M_<sup>-1</sup>_A=A_ is not diagonalizable and _B_ is HPD. A calculation shows<tbc>

\(\widehat{M}^{-1}=M^{-1}AB^{-1}+B^{-1}A^HM^{-H}-M^{-1}AB^{-1}A^HM^{-H}=\left[\begin{array}{ c c c }
\frac{3}{4} & 0 & 0 \\
0 & \frac{11}{4} & 1 \\
0 & 1 & \frac{3}{8}
\end{array}\right]\)

<tbc>is HPD and thus the smoothing assumption is satisfied, that is \(\|I-M^{-1}A\|_B<1\). Furthermore, it holds

\(\widehat{M}^{-1}B=\left[\begin{array}{ c c c }
\frac{3}{4} & 0 & 0 \\
0 & \frac{3}{4} & \frac{1}{2} \\
0 & \frac{1}{4} & \frac{1}{4}
\end{array}\right]\)<br>
\(=\left[\begin{array}{ c c c }
1 & 0 & 0 \\
0 & -\sqrt{3}+1 & \sqrt{3}+1 \\
0 & 1 & 1
\end{array}\right]\left[\begin{array}{ c c c }
\frac{3}{4} & -\sqrt{3}+2 &  \\
 & \frac{\sqrt{3}+2}{4} &  \\
 & \frac{\sqrt{3}+2}{4}
\end{array}\right]\left[\begin{array}{ c c c }
1 & 0 & 0 \\
0 & -\sqrt{3}+1 & \sqrt{3}+1 \\
0 & 1 & 1
\end{array}\right]^{-1}\)

thus \(\widehat{M}^{-1}B\) has the sorted eigenvalues \(\mu_1=\frac{-\sqrt{3}+2}{4}\le\mu_2=\frac{3}{4}\le\mu_3=\frac{\sqrt{3}+2}{4}\) . We choose the interpolation \(P=\left[\begin{array}{ c }
0 \\
-\sqrt{3}+1
\end{array}\right]\) as eigenvector of \(\widehat{M}^{-1}B\) corresponding to \(\mu_1\) and the corresponding optimal restriction \(R_*=A^{-H}BP=\left[\begin{array}{ c }
0 \\
-2\sqrt{3}-2
\end{array}\right]\). Then by construction of _P_ and _R_<sub>∗</sub> we know that \(\Pi_A(P,R_*)\) is _B_-orthogonal. A computation also shows

\(\Pi_A(P,R_*)=\left[\begin{array}{ c c c }
0 & 0 & 0 \\
0 & \frac{-\sqrt{3}+3}{6} & -\sqrt{3} \\
0 & \frac{-\sqrt{3}}{6} & \frac{\sqrt{3}+3}{6}
\end{array}\right]\text{and}E_+^{1,1}=\left[\begin{array}{ c c c }
\frac{1}{4} & 0 & 0 \\
0 & \frac{\sqrt{3}-1}{8} & \frac{-2\sqrt{3}+3}{4} \\
0 & \frac{2\sqrt{3}-3}{24} & \frac{-3\sqrt{3}+5}{8}
\end{array}\right]\)


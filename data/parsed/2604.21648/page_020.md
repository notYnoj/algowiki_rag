<tbc>with \(D_{n_c}^{(A)}\in\mathbb{C}^{n_c\times n_c}\) and \(D_{n_f}^{(A)}\in\mathbb{C}^{n_f\times n_f}\). By the definitions of _P_<sub>#</sub> and _R_<sub>#</sub> we know that \(P_\#=V_r\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]Z\) and \(R_\#=V_l\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]S\) hold for some nonsingular matrices \(Z,S\in\mathbb{C}^{n_c\times n_c}\). It follows

\(\Pi_A(P_\#,R_\#)=V_r\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]Z\left(S^H\left[I_{n_c}0\right]V_l^HAV_r\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]Z\right)^{-1}S^H\left[I_{n_c}0\right]V_l^HA\)<br>
\(=V_r\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]\left(\left[I_{n_c}0\right]D_A\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]\right)^{-1}\left[I_{n_c}0\right]D_AV_r^{-1}\)<br>
\(=V_r\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right](D_{n_c}^{(A)})^{-1}\left[I_{n_c}0\right]D_AV_r^{-1}\)<br>
\(=V_r\left[\begin{array}{ c }
(D_{n_c}^{(A)})^{-1} \\
0
\end{array}\right]D_AV_r^{-1}=V_r\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]V_r^{-1}.\) (4.8)

By Lemma 4.7 (2) and the structure of _B_ the projection \(\Pi_A(P_\#,R_\#)\) is _B_-orthogonal. Since \(M^{-1}A=V_r\Lambda V_r^{-1}\), the matrices _M_<sup>-1</sup>_A_ and \(\Pi_A(P_\#,R_\#)\) are simultaneously diagonalizable and therefore commute. Thus, we have

\(E^{\nu_1,\nu_2}(P_\#,R_\#)=(I-M^{-1}A)^{\nu_2}(I-\Pi_A(P_\#,R_\#))(I-M^{-1}A)^{\nu_1}\)<br>
\(=(I-\Pi_A(P_\#,R_\#))(I-M^{-1}A)^{\nu_1+\nu_2}\)<br>
\(=V_r\left(I-\left[\begin{array}{ c c }
I_{n_c} & 0 \\
0 & 0
\end{array}\right]\right)V_r^{-1}V_r\left(I-\Lambda\right)^{\nu_1+\nu_2}V_r^{-1}\)<br>
\(=V_r\left[\begin{array}{ c c }
0 & 0 \\
0 & I_{n_f}-\Lambda_{n_f}
\end{array}\right]^{\nu_1+\nu_2}V_r^{-1}\)<br>
\(=V_rD^\frac{1}{2}\left[\begin{array}{ c c }
0 & 0 \\
0 & I_{n_f}-\Lambda_{n_f}
\end{array}\right]^{\nu_1+\nu_2}D^{-\frac{1}{2}}V_r^{-1}.\)

Since _D_ is HPD, \(D^\frac{1}{2}\) exists and the matrix \(V_rD^\frac{1}{2}\) is _B_-unitary. Then the error operator \(E^{\nu_1,\nu_2}(P_\#,R_\#)\) is _B_-unitarily diagonalizable and hence _B_-normal. With Proposition 2.14 and the ordering of the eigenvalues (4.5) we obtain

\(\|E^{\nu_1,\nu_2}(P_\#,R_\#)\|_B=\rho(E^{\nu_1,\nu_2}(P_\#,R_\#))=|1-\lambda_{n_c+1}|^{\nu_1+\nu_2}.\) □

_Remark_ 4.9. The result itself is independent of the smoothing assumption. However, to obtain a convergent two-grid method with \(\|E^{\nu_1,\nu_2}(P_\#,R_\#)\|_B<1\) the smoothing assumption is required.

In \[30\] we prove further characterizations of the _B_-norm of the error operator \(E^{\nu_1,\nu_2}\). The proof of Theorem 4.8 shows that \(V_rD^\frac{1}{2}\) is _B_-unitary. Since _D_ is nonsingular, it holds \(\mathcal{R}(V_r)=\mathcal{R}(V_rD^\frac{1}{2})\) and \(V_rD^\frac{1}{2}\) is a _B_-unitary eigenvector matrix of _M_<sup>-1</sup>_A_. With Theorem 3.10 we infer that \(\widehat{M}^{-1}B\) is also _B_-unitarily diagonalizable with eigenvector matrix \(V_rD^\frac{1}{2}\) and eigenvalues \(1-|1-\lambda|^2\). The block structure of _B_ shows that

\(\mathcal{R}(P_\#)=\mathcal{R}(\big[v_1\cdots v_{n_c}\big])=\mathcal{R}(\hat{P})\)

and with Lemma 3.11 we obtain

\(\mathcal{N}(R_\#^HA)=\mathcal{R}(\big[v_{n_c+1}\cdots v_n\big])=\mathcal{N}(\hat{R}^HA).\)


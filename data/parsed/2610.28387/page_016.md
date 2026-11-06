_where_

\(B_1=\left(\begin{array}{ c c }
4\mathbb{E}(aa^\mathsf{T}) & 6\mathbb{E}(ab^\mathsf{T}) \\
6\mathbb{E}(ba^\mathsf{T}) & 9\mathbb{E}(bb^\mathsf{T})
\end{array}\right),\) (4.6)

\(B_2=\left(\begin{array}{ c c }
\mathbb{E}(cc^\mathsf{T}) & 3\mathbb{E}(cd^\mathsf{T}) \\
3\mathbb{E}(dc^\mathsf{T}) & 9\mathbb{E}(dd^\mathsf{T})
\end{array}\right),\)<br>
\(B_3=\left(\begin{array}{ c c }
0_{2\times 2} & 0_{2\times 2} \\
0_{2\times 2} & \mathbb{E}(ee^\mathsf{T})
\end{array}\right).\)

_Each matrix B_<sub>1</sub>_,B_<sub>2</sub>_,B_<sub>3</sub> _is positive semidefinite._

_Proof._ We first verify (4.3). Since \(\mathbb{E}\{H_2(z,Z')\}=M_{2,1}(z)\) and \(\mathbb{E}\{a(Z')\}=0\),<tbc>

\(\mathbb{E}\{c(z,Z')\}=M_{2,1}(z)-a(z)-\lambda_2=0\)

<tbc>by (4.1). In the same way, \(\mathbb{E}\{d(z,Z')\}=M_{3,1}(z)-b(z)-\lambda_3=0\). For **_e_**, integrate out _Z_<sub>3</sub> and use E{**_H_**<sub>3</sub>(_z_<sub>1</sub>_,z_<sub>2</sub>_,Z_<sub>3</sub>)}=_M_<sub>3,2</sub>(_z_<sub>1</sub>_,z_<sub>2</sub>), E{_M_<sub>3,2</sub>(_z<sub>k</sub>,Z_<sub>3</sub>)}=_M_<sub>3,1</sub>(_z<sub>k</sub>_) for _k_=1,2, and \(\mathbb{E}\{M_{3,1}(Z_3)\}=\lambda_3\):

\(\mathbb{E}\{e(z_1,z_2,Z_3)\}=M_{3,2}(z_1,z_2)-\{M_{3,2}(z_1,z_2)+M_{3,1}(z_1)+M_{3,1}(z_2)\}\)<br>
\(+\{M_{3,1}(z_1)+M_{3,1}(z_2)+\lambda_3\}-\lambda_3=0.\)

The complete U-statistic decompositions are

\(\widehat{\lambda}_2-\lambda_2=\frac{2}{n}\sum_{i=1}^na(Z_i)+\genfrac(){pt}{2}{n}{2}^{-1}\sum_{i<j}c(Z_i,Z_j),\)<br>
\(\widehat{\lambda}_3-\lambda_3=\frac{3}{n}\sum_{i=1}^nb(Z_i)+\frac{3}{\genfrac(){pt}{2}{n}{2}}\sum_{i<j}d(Z_i,Z_j)+\genfrac(){pt}{2}{n}{3}^{-1}\sum_{i<j<k}e(Z_i,Z_j,Z_k).\)

By (4.4), a product of two terms in these decompositions has zero expectation unless both terms are evaluated at the same index set. In particular, terms of different Hoeffding orders are uncorrelated, and only matching terms remain. For the first-order terms,

\(Cov\big(\frac{2}{n}\sum_ia(Z_i),\frac{3}{n}\sum_jb(Z_j)\big)=\frac{6}{n^2}\sum_{i=1}^n\mathbb{E}\{a(Z_i)b(Z_i)^\mathsf{T}\}=\frac{6}{n}\mathbb{E}(ab^\mathsf{T}),\)

and the other first-order blocks follow in the same way with prefactors 4 and 9. For the second-order terms, the same argument gives E(**_cc_**<sup>T</sup>), 3E(**_cd_**<sup>T</sup>), and 9E(**_dd_**<sup>T</sup>), each divided by \(\genfrac(){pt}{2}{n}{2}\). The third-order term appears only in \(\widehat{\lambda}_3\) and gives E(**_ee_**<sup>T</sup>) divided by \(\genfrac(){pt}{2}{n}{3}\). These give (4.5) and (4.6). Positive semidefiniteness follows because each displayed component is an expectation of an outer product, e.g., _B_<sub>2</sub>=E((**_c_**<sup>T</sup>,3**_d_**<sup>T</sup>)<sup>T</sup>(**_c_**<sup>T</sup>,3**_d_**<sup>T</sup>)).

The leading matrix _B_<sub>1</sub> is the asymptotic covariance of \(\sqrt{n}(\widehat{\Lambda}-\Lambda)\), in agreement with Proposition 8 of Serfling and Xiao (2007). The remaining two terms are the exact finite-sample corrections, of orders _n_<sup>-2</sup> and _n_<sup>-3</sup>.


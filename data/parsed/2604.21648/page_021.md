<tbc>The _B_-orthogonality of \(\Pi_A(\hat{P},\hat{R})\) and Lemma 3.1 then yield

\(\mathcal{R}(\hat{R})=\mathcal{R}(A^{-H}B\hat{P})=\mathcal{R}(A^{-H}BP_\#)=\mathcal{R}\left(A^{-H}V_r^{-H}D^{-1}V_r^{-1}V_r\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]\right)\)<br>
\(=\mathcal{R}\left(A^{-H}V_r^{-H}\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]\right)=\mathcal{R}\left(V_lD_A\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]\right)=\mathcal{R}\left(V_l\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]\right)=\mathcal{R}(R_\#).\)

Additionally, the sorting of the eigenvalues \(\lambda\) of _M_<sup>-1</sup>_A_ as in (4.5) implies the ordering

\(\mu_1=1-|1-\lambda_1|^2\le\mu_2=1-|1-\lambda_2|^2\le\cdots\le\mu_n=1-|1-\lambda_n|^2\)

of the eigenvalues \(\mu\) of \(\widehat{M}^{-1}B\). Therefore, for \((\nu_1,\nu_2)\in\{(0,1),(1,0),(1,1)\}\) and given the assumption of Theorem 4.8, all the assumptions of Theorem 4.1 are satisfied and we obtain

\(\|E_+^{\nu_1,\nu_2}(P_\#,R_\#)\|_B^2=(1-\mu_{n_c+1})^{\nu_1+\nu_2}=|1-\lambda_{n_c+1}|^{2(\nu_1+\nu_2)}=\|E^{\nu_1,\nu_2}(P_\#,R_\#)\|_B^2.\)

In summary, for \((\nu_1,\nu_2)\in\{(0,1),(1,0),(1,1)\}\) and _M_<sup>-1</sup>_A_ is _B_-normal, Theorems 4.1 and 4.8 gives the same (up to a change of basis) restriction and interpolation operators and the same _B_-norm estimate. The theorems differ in the assumption on _M_<sup>-1</sup>_A_ and in the number of smoothing steps. While Theorem 4.1 is true for any _B_-norm and does not need assumptions on _M_<sup>-1</sup>_A_, it requires \((\nu_1,\nu_2)\in\{(0,1),(1,0),(1,1)\}\). On the other hand, Theorem 4.8 is valid for arbitrary numbers of pre- and post-smoothing steps but requires the _B_-normality of _M_<sup>-1</sup>_A_ which restricts the set of all possible _B_-norms.

The structure of the matrix _D_ and therefore also _B_ might seem complicated, but it can be explained using Theorem 2.9 (5). The interpolation and restriction _P_<sub>#</sub> and _R_<sub>#</sub> are defined independently of _B_ and by Theorem 4.8 we know that \(\Pi_A(P_\#,R_\#)\) is _B_-orthogonal for any matrix \(B=V_r^{-H}D_1^{-1}V_r^{-1}\) where _D_<sub>1</sub> is an HPD block diagonal matrix with two HPD blocks, one of size _n<sub>c</sub>_ and one of size _n<sub>f</sub>_ (cf. Lemma 4.7 (2)). This explains the HPD block _D<sub>n<sub>c</sub></sub>_ in (4.6). For the other block _D<sub>n<sub>f</sub></sub>_ we apply Theorem 2.9 (5) to _M_<sup>-1</sup>_A_ and obtain the structure \(B=V_r^{-H}D_2^{-1}V_r^{-1}\) where _D_<sub>2</sub> is now an HPD block diagonal matrix with block sizes corresponding to those of \(\Lambda\). Hence, the _B_-normality of _M_<sup>-1</sup>_A_ explains the structure of the lower right block _D<sub>n<sub>f</sub></sub>_ in (4.6). In short, for _M_<sup>-1</sup>_A_ to be _B_-normal and \(\Pi_A\) to be _B_-orthogonal, the _B_-inner product must be of the form _B=W_<sup>-_H_</sup>_DW_<sup>-1</sup> where _W_ are eigenvectors of _M_<sup>-1</sup>_A and_ \(\Pi_A\) and _D_ is an HPD block diagonal matrix with block sizes corresponding to the block sizes of the eigenvalues of _M_<sup>-1</sup>_A and_ \(\Pi_A\).

Similar to Theorem 4.4, the question remains whether (_P_<sub>#</sub>_,R_<sub>#</sub>) is the optimal combination of interpolation and restriction operator in the sense that they yield the smallest possible _B_-norm of \(E^{\nu_1,\nu_2}\). This question was already answered in \[16, Theorem 3.5\] for diagonal HPD matrices _D_ (instead of those in (4.6)). Here we state their result and extend the class of _B_-inner products by allowing block HPD matrices _D_ as in (4.6). The proof for diagonal _D_ can be found in \[16\] and we give no proof here because it is analogous to the proof in \[16\] and the proof of Theorem 4.4.

Theorem 4.10. _Let the assumptions from Theorem_ 4.8 _be fulfilled, the smoothing assumption be satisfied and I-M_<sup>-1</sup>_A be nonsingular. Then it holds_

\(\|E^{\nu_1,\nu_2}(P_\#,R_\#)\|_B=|1-\lambda_{n_c+1}|^{\nu_1+\nu_2}\le\|E^{\nu_1,\nu_2}(P,R)\|_B\)

_for all_ \(P,R\in\mathbb{C}^{n\times n_c}\) _such that R<sup>H</sup>AP is nonsingular._


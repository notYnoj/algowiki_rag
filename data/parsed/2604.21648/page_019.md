<tbc>Lemma 4.7. _Let M_<sup>-1</sup> _be diagonalizable with_ \(M^{-1}A=W\Lambda W^{-1}\) _and let_ \(\Pi_A\) _be a projection with_ \(\mathrm{dim}(\mathcal{R}(\Pi_A))=n_c\)_. Then_ \(\Pi_A\) _is diagonalizable with_ \(\Pi_A=S\left[\begin{array}{ c c }
I_{n_c} & 0 \\
0 & 0
\end{array}\right]S^{-1}\) _and the following statements holds._

_1) M_<sup>-1</sup>_A is B-normal if and only if B_=(_WDW<sup>H</sup>_)<sup>-1</sup> _for an HPD block diagonal matrix D where the block sizes correspond to those in_ \(\Lambda\).<tbc>

_2)_ \(\Pi_A\) _is B-orthogonal if and only if B_=(_SDS<sup>H</sup>_)<sup>-1</sup> _for an HPD block diagonal matrix_ \(D=\left[\begin{array}{ c c }
D_{n_c} & 0 \\
0 & D_{n_f}
\end{array}\right]\) _with two HPD blocks_ \(D_{n_c}\in\mathbb{C}^{n_c\times n_c}\) _and_ \(D_{n_f}\in\mathbb{C}^{n_f\times n_f}\).

_Proof. 1)_ follows from Theorem 2.9 (5) under the general assumption that _M_<sup>-1</sup>_A_ is diagonalizable. For _2)_ we observe that \(\Pi_A\) is always diagonalisable with \(\Pi_A=S\left[\begin{array}{ c c }
I_{n_c} & 0 \\
0 & 0
\end{array}\right]S^{-1}\) where the identity block is the size of the dimension of \(\mathcal{R}(\Pi_A)\), that is _n<sub>c</sub>_, \[10, Theorem 2.11\]. Therefore, \(\Pi_A\) has real eigenvalues and the result follows from _1)_ and Proposition 2.11. □

When we apply this result to the specific diagonalization \(M^{-1}A=V_r\Lambda V_r^{-1}\) with _V<sub>r</sub>_ as in (4.1), we can conclude that the assumption that _M_<sup>-1</sup>_A_ is diagonalizable used in \[1, 16\] leads to _B_-normal smoothers for specific HPD matrices _B_.

With this, we now present \[16, Theorem 3.3\] in the framework of _B_-normal matrices. Notice that we also extended the class of possible inner products and condensed the proof of the result.

Theorem 4.8. _Let M_<sup>-1</sup>_A be B-normal and_<tbc>

\(V_r=\left[v_1^{(r)}\cdots v_n^{(r)}\right]\text{\textit{and}}V_l=\left[v_1^{(l)}\cdots v_n^{(l)}\right]\)

<tbc>_be the right and left eigenvectors of the generalized eigenvalue problem_ (3.14)_, respectively, such that_ (4.1) _and_ (4.2) _are satisfied with the eigenvalue matrix_ \(\Lambda=\left[\begin{array}{ c c }
\Lambda_{n_c} & 0 \\
0 & \Lambda_{n_f}
\end{array}\right]\)_. Assume that the eigenvalues_ \(\lambda\) _are ordered such that_

(4.5) \(|1-\lambda_1|\ge|1-\lambda_2|\ge\cdots\ge|1-\lambda_n|\)

_and equal eigenvalues for a single diagonal block in_ \(\Lambda\)_. Let_ \(B=V_r^{-H}D^{-1}V_r^{-1}\) _where_

(4.6) \(D=\left[\begin{array}{ c c }
D_{n_c} & 0 \\
0 & D_{n_f}
\end{array}\right]\in\mathbb{C}^{n\times n}\)

_is HPD block diagonal with_ \(D_{n_c}\in\mathbb{C}^{n_c\times n_c}\) _and_ \(D_{n_f}\in\mathbb{C}^{n_f\times n_f}\)_. Both D<sub>n<sub>c</sub></sub> and D<sub>n<sub>f</sub></sub> are also HPD block diagonal with block sizes corresponding to those in_ \(\Lambda_{n_c}\) _and_ \(\Lambda_{n_f}\)_. Furthermore, let_ \(P_\#,R_\#\in\mathbb{C}^{n\times n_c}\) _be defined such that_

\(\mathcal{R}(P_\#)=\mathcal{R}\left(\left[v_1^{(r)}\cdots v_{n_c}^{(r)}\right]\right)\text{\textit{and}}\mathcal{R}(R_\#)=\mathcal{R}\left(\left[v_1^{(l)}\cdots v_{n_c}^{(l)}\right]\right).\)

_Then_ \(\Pi_A(P_\#,R_\#)\) _is B-orthogonal and it holds_

\(\rho(E^{\nu_1,\nu_2}(P_\#,R_\#))=\|E^{\nu_1,\nu_2}(P_\#,R_\#)\|_B=|1-\lambda_{n_c+1}|^{\nu_1+\nu_2}.\)

_Proof._ Let _M_<sup>-1</sup>_A_ be _B_-normal with right and left generalized eigenvectors _V<sub>r</sub>_ and _V<sub>l</sub>_ such that (4.1) and (4.2) are satisfied, respectively. Let the eigenvalues \(\lambda\) be ordered as in (4.5), let \(B=V_r^{-H}D^{-1}V_r^{-1}\) with _D_ as in (4.6) and _P_<sub>#</sub> and _R_<sub>#</sub> defined as above. We partition the diagonal matrix \(D_A\in\mathbb{C}^{n\times n}\) from (4.3) similar to \(\Lambda\), that is

(4.7) \(D_A=\left[\begin{array}{ c c }
D_{n_c}^{(A)} & 0 \\
0 & D_{n_f}^{(A)}
\end{array}\right]\)


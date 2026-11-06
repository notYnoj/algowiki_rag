<tbc>Definition 2.8. _A is called B-unitary if A<sup>H</sup>BA=I<sub>n</sub>, i.e. the columns of A are orthonormal in the B-inner product._

For a _B_-unitary matrix _A_ it holds _A_<sup>+</sup>_A=B_<sup>-1</sup> and _A_<sup>-1</sup>=_A<sup>H</sup>B_ as well as _B=A_<sup>-_H_</sup>_A_<sup>-1</sup>. The last equation already shows that the structure of the matrix _B_ also depends on the underlying matrix _A_. This behavior is described in the fifth characterization for _B_-normality in the following result which is mostly proven in \[20, Theorem 3.1\].

Theorem 2.9. _The following statements are equivalent:_

(_1)_ _A is B-normal._<tbc>

(_2)_ _A_<sup>+</sup>=_p(A_) _for some polynomial_ \(p\in\mathbb{C}[z]\).<tbc>

_(3)_ _A is B-unitarily diagonalizable, that is there exists a B-unitary matrix_ \(U\in\mathbb{C}^{n\times n}\) _and a diagonal matrix_ \(D\in\mathbb{C}^{n\times n}\) _such that A=UDU_<sup>-1</sup>.<tbc>

_(4)_ _If x is an eigenvector of A to the eigenvalue_ \(\lambda\)_, then x is an eigenvector of A_<sup>+</sup> _to the eigenvalue_ \(\overline{\lambda}\).<tbc>

_(5)_ _A is diagonalizable with eigendecomposition_ \(A=W\Lambda W^{-1}\) _(without loss of generality we consider the eigenvalues and eigenvectors of A ordered so that equal eigenvalues form a single diagonal block in_ \(\Lambda\)_). Furthermore, using the eigenvector matrix W, the matrix B_<sup>-1</sup> _has a decomposition B_<sup>-1</sup>=_WDW<sup>H</sup> where D is an HPD block diagonal matrix with block sizes corresponding to those in_ \(\Lambda\)_. There also exists a polynomial_ \(p\in\mathbb{C}[z]\) _such that_ \(p(\Lambda)=\Lambda^H\).

_Proof._ The properties follow from the fact that _AA_<sup>+</sup>=_A_<sup>+</sup>_A_ is equivalent to

\((B^\frac{1}{2}AB^{-\frac{1}{2}})(B^{-\frac{1}{2}}A^HB^\frac{1}{2})=(B^{-\frac{1}{2}}A^HB^\frac{1}{2})(B^\frac{1}{2}AB^{-\frac{1}{2}})\)

and hence \(\widetilde{A}=B^\frac{1}{2}AB^{-\frac{1}{2}}\) is normal. Therefore _B_-normality can be reduced to normality in the classic sense and any characterization from \[13\] and \[6\] can be used.

_(1)_ \(\Leftrightarrow\) _(3):_ This proof is based on the proof of \[20, Theorem 3.1\]. The matrix \(\widetilde{A}\) can be unitarily diagonalized, i.e. \(\widetilde{A}=U\Lambda U^H\) hence \(A=B^{-\frac{1}{2}}U\Lambda U^HB^\frac{1}{2}\). With \(W:=B^{-\frac{1}{2}}U\) we get \(A=W\Lambda W^{-1}\) with _W<sup>H</sup>BW=I_ (in particular _W_<sup>-1</sup>=_W<sup>H</sup>B_). Thus _A_ is _B_-unitarily diagonalizable. Conversely, if _A_ is _B_-unitary diagonalizable we have \(A=U\Lambda U^{-1}\) with _U<sup>H</sup>BU=I_. Then it holds

\(AA^+=U\Lambda U^{-1}B^{-1}U^{-H}\Lambda^HU^HB=U\Lambda\Lambda^HU^{-1}=U\Lambda^H\Lambda U^{-1}\)<br>
\(=B^{-1}U^{-H}\Lambda^HU^HU\Lambda U^{-1}=A^+A\)

and thus _A_ is _B_-normal. We used that diagonal matrices commute and _U<sup>H</sup>B=U_<sup>-1</sup>.

_(1)_ \(\Leftrightarrow\) _(2):_ Let _A_ be _B_-normal. By _(3), A_ is _B_-unitarily diagonalizable with \(A=U\Lambda U^{-1}\) where _U_ is _B_-unitary and \(\Lambda\) is a diagonal matrix containing the eigenvalues of _A_. Furthermore, there exists an interpolation polynomial with \(p(\lambda)=\overline{\lambda}\) for all eigenvalues \(\lambda\) of _A_, and thus

\(A^+=B^{-1}A^HB=B^{-1}U^{-H}\Lambda^HU^HB=B^{-1}BUp(\Lambda)U^{-1}=Up(\Lambda)U^{-1}=p(A).\)

On the other hand, if _A_<sup>+</sup>=_p(A_), then _A_<sup>+</sup> commutes with _A_.

_(1)_ \(\Leftrightarrow\) _(4):_ Let _A_ be _B_-normal and \((\lambda,x)\) be an eigenpair of _A_, that is \(Ax=\lambda x\). By (2) we have \(A^+x=p(A)x=p(\lambda)x\), hence _x_ is an eigenvector of _A_<sup>+</sup>. We even have

\(p(\lambda)\langle x,x\rangle_B=\langle p(\lambda)x,x\rangle_B=\langle A^+x,x\rangle_B=\langle x,Ax\rangle_B=\overline{\lambda}\langle x,x\rangle_B\)

and because \(x\neq 0\) it holds \(p(\lambda)=\overline{\lambda}\). Therefore, _x_ is an eigenvector of _A_<sup>+</sup> to the eigenvalue \(\overline{\lambda}\).


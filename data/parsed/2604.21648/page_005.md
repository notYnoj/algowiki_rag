<tbc>Conversely, if _(4)_ holds then \(y:=B^\frac{1}{2}x\) is an eigenvector of \(\widetilde{A}\) and of \(\widetilde{A}^H\). Therefore \(\widetilde{A}\) is normal and thus _A_ is _B_-normal (cf. \[13, Condition 10\]).

_(1)_ \(\Leftrightarrow\) _(5):_ This is an immediate consequence of \[20, Theorem 3.1\]. □

The concept of _B_-normal matrices is also used in the theory of short recurrences for computing _B_-orthogonal Krylov subspace bases \[20, 7, 21\]. There, the length of the recurrence for the computation of the Krylov subspace basis vectors depends on the degree of the polynomial _p_ in Theorem 2.9 (2). Note that we are not interested in the degree of _p_ at all but rather the set B of all possible matrices _B_ such that _A_ can be _B_-normal. This set can be characterized using equivalence Theorem 2.9 (5) and is given by

\(\mathcal{B}=\{(WDW^H)^{-1}|D\text{is an HPD block diagonal matrix}\) (2.2)

\(\text{with block sizes corresponding to those in}\Lambda\}.\)

\(\Lambda\) denotes the eigenvalue matrix of _A_. The structure of the matrices in B will be of importance later when we derive convergence bounds for AMG methods. Using these characterizations, we can conclude some useful properties of _B_-orthogonal matrices.

Proposition 2.10. _Let_ \(A\in\mathbb{C}^{n\times n}\) _be B-orthogonal. Then all eigenvalues of A are real._

_Proof._ Since _A_ is also _B_-normal, there exists a polynomial _p_ with _p(A_)=_A_<sup>+</sup>=_A_, hence _p(z_)=_z_ for all \(z\in\mathbb{C}\). The eigenvalues of _A_ then satisfy \(p(\lambda)=\overline{\lambda}=\lambda\) and thus all eigenvalues of _A_ are real. □

Proposition 2.11. _Let_ \(A\in\mathbb{C}^{n\times n}\) _be B-normal. Then A is B-orthogonal if and only if all eigenvalues of A are real._

_Proof._ Let _A_ be _B_-normal. The first part is proven in Proposition 2.10. Assume that the eigenvalues \(\lambda\) of _A_ are real. Then it holds \(\overline{\lambda}=\lambda=p(\lambda)\) for the identity polynomial _p_. Since _A_ is _B_-normal, we know by Theorem 2.9 (5) that _A_ has an eigendecomposition \(A=W\Lambda W^{-1}\) and _B_<sup>-1</sup>=_WDW<sup>H</sup>_ for an HPD block diagonal matrix _D_ where the block sizes corresponds to those in \(\Lambda\). Then it holds

\(A^+=B^{-1}A^HB=(WDW^H)(W^{-H}\Lambda^HW^H)(W^{-H}D^{-1}W^{-1})\)<br>
\(=WD\Lambda^HD^{-1}W^{-1}=W\Lambda^HW^{-1}=W\Lambda W^{-1}=A\)

and thus _A_ is _B_-orthogonal. Here, _D_ and \(\Lambda\) commute since they have the same block structure □

Using this result, we obtain another important property of the _B_-norm which for _B=I<sub>n</sub>_ again reduces to a known property of the spectral norm.

Proposition 2.12. _Let_ \(A\in\mathbb{C}^{n\times n}\)_. Then it holds_

\(\|A\|_B^2=\|AA^+\|_B=\|A^+A\|_B=\|A^+\|_B^2=\lambda_{max}(A^+A)=\lambda_{max}(AA^+),\)

_where_ \(\lambda_{max}\) _denotes the largest eigenvalue._

_Proof._ Since all the properties are known for _B=I<sub>n</sub>_, that is the spectral norm, we can use the fact that \(\|A\|_B=\|B^\frac{1}{2}AB^{-\frac{1}{2}}\|_2\) to obtain the result. □

_Remark_ 2.13. Similar to \(\lambda_{max}\) we define \(\lambda_{min}\) as the smallest eigenvalue of a matrix. Both of these quantities are well-defined if the matrix only has real eigenvalues. But since _A_<sup>+</sup>_A_ is _B_-orthogonal for any matrix \(A\in\mathbb{C}^{n\times n}\), by Proposition 2.10 its eigenvalues are always real.


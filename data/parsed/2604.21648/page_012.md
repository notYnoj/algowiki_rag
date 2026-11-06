<tbc>Recall that we consider the eigenvalue problems<tbc>

\(M^{-1}Az=\lambda z\text{and}\widehat{M}^{-1}Bv=\mu v.\)

<tbc>If the smoothing assumption is satisfied, the matrix \(\widehat{M}^{-1}\) is nonsingular and both eigenvalue problems can be equivalently rewritten as the generalized eigenvalues problems

(3.14) \(Az=\lambda Mz,\)

(3.15) \(Bv=\mu\widehat{M}v.\)

In \[1, 16\] the first generalized eigenvalue problem is considered. \[2\] studies the second (generalized) eigenvalue problem with \(\widetilde{M}^{-1}\) rather than \(\widehat{M}^{-1}\). However, we restrict ourselves to \(\widehat{M}^{-1}B\) here, because the eigenvalue problems are the same if _M_<sup>-1</sup>_A_ is _B_-normal.

Moreover, if _M_<sup>-1</sup>_A_ is _B_-normal, the proof of Corollary 3.6 suggests that there exists a relation between the eigenvalues of _M_<sup>-1</sup>_A_ and \(\widehat{M}^{-1}B\). This connection is formalized in the following result.

Theorem 3.10. _Let M_<sup>-1</sup>_A be B-normal and_ \((\lambda,z)\) _be an eigenpair of M_<sup>-1</sup>_A. Then_ \((\mu,z)\) _with_

\(\mu=\lambda+\overline{\lambda}-\overline{\lambda}\lambda=1-|\lambda-1|^2\)

_is an eigenpair of_ \(\widehat{M}^{-1}B=\widetilde{M}^{-1}B\)_. Furthermore, M_<sup>-1</sup>_A and_ \(\widehat{M}^{-1}B=\widetilde{M}^{-1}B\) _are simultaneously B-unitarily diagonalizable._

_Proof._ By Theorem 2.9 (3) the matrix _M_<sup>-1</sup>_A_ is _B_-unitarily diagonalizable, that is \(M^{-1}A=W\Lambda W^{-1}\) for a _B_-unitary matrix \(W\in\mathbb{C}^{n\times n}\) and diagonal matrix \(\Lambda\in\mathbb{C}^{n\times n}\) containing the eigenvalues. By Theorem 2.9 (4) the matrix (_M_<sup>-1</sup>_A_)<sup>+</sup> is then also diagonalizable with eigenvectors _W_ and eigenvalues \(\Lambda^H\), i.e. \((M^{-1}A)^+=W\Lambda^HW^{-1}\). Thus we have

\(\widehat{M}^{-1}B=M^{-1}A+(M^{-1}A)^+-M^{-1}A(M^{-1}A)^+=W(\Lambda+\Lambda^H-\Lambda\Lambda^H)W^{-1}.\)

By Proposition 3.3 it holds \(\widehat{M}^{-1}B=\widetilde{M}^{-1}B\). Hence, _M_<sup>-1</sup>_A_ and \(\widehat{M}^{-1}B=\widetilde{M}^{-1}B\) are simultaneously _B_-unitarily diagonalizable and each eigenpair \((\lambda,z)\) of _M_<sup>-1</sup>_A_ is an eigenpair \((\mu,z)\) of \(\widehat{M}^{-1}B\) with \(\mu=\lambda+\overline{\lambda}-\lambda\overline{\lambda}=1-|\lambda-1|^2\). □

Under the above assumptions, for \(\sigma(M^{-1}A)=\{\lambda_1,\dots,\lambda_n\}\) we obtain

\(\sigma(\widehat{M}^{-1}B)=\{1-|\lambda_1-1|^2,\dots,1-|\lambda_n-1|^2\}.\)

The function _f(z_)=1-|_z_-1|<sup>2</sup> that describes the eigenvalues of \(\widehat{M}^{-1}B\) is maximal if and only if |_z_-1|<sup>2</sup>=0 which is fulfilled for _z_=1. The zeros of _f_ are given by all \(z\in\mathbb{C}\) with |_z_-1|=1.

In the HPD case Lemma 3.10 gives the relation between the eigenpairs of _M_<sup>-1</sup>_A_ (smoother times system matrix) and \(\widetilde{M}^{-1}A\) (symmetrized smoother times system matrix) if _M_<sup>-1</sup>_A_ is _A_-normal. This condition is fulfilled if _M_ is Hermitian. Thus, if _A_ is HPD and _M_ is Hermitian we do have the relation between the eigenvalue problems, in particular the eigenvectors are the same. But in general these eigenvalue problems are different.

The next auxiliary result connects the eigenvectors of \(\widehat{M}^{-1}B\) to the _B_-orthogonality of \(\Pi_A\).


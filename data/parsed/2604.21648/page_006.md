<tbc>Another important property of _B_-normal matrices is their relation to the spectral radius \(\rho\).

Proposition 2.14. _Let_ \(A\in\mathbb{C}^{n\times n}\) _be B-normal. Then_ \(\|A\|_B=\rho(A)\).

_Proof._ With Theorem 2.9 (3) the matrix _A_ is _B_-unitarily diagonalizable, that is \(A=W\Lambda W^{-1}\) with _W<sup>H</sup>BW=I<sub>n</sub>_ and \(\Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_n)\) containing the eigenvalues of _A_. Then we have

\(\|A\|_B^2=\lambda_{max}(A^+A)=\lambda_{max}(B^{-1}W^{-H}\Lambda^HW^HBW\Lambda W^{-1})=\lambda_{max}(W\Lambda^H\Lambda W^{-1})\)<br>
\(=\lambda_{max}(\Lambda^H\Lambda)=\lambda_{max}(\mathrm{diag}(|\lambda_1|^2,\dots,|\lambda_n|^2))=\mathrm{max}_{i=1,\dots,n}|\lambda_i|^2=\rho(A)^2.\)

Taking the square root yields the result. □

**3.** _B_**-normal matrices in nonsymmetric AMG.** We consider the linear algebraic system

\(Ax=b\)

where \(A\in\mathbb{C}^{n\times n}\) is a nonsingular, nonsymmetric and indefinite matrix and \(b\in\mathbb{C}^n\). We want to solve this system using algebraic two-grid methods. Such methods typically consist of two components, the smoothing and the coarse-grid correction. Smoothing is usually a basic iterative method such as the Gauss-Seidel or Jacobi method and is done for a few iterations. The coarse-grid correction is based on a projection and requires the division of the _n_ variables in two smaller groups with _n<sub>c</sub>\<n_ and _n<sub>f</sub>\<n_ variables such that _n<sub>c</sub>+n<sub>f</sub>=n_. The number _n<sub>c</sub>_ can be interpreted as the number of variables of the coarse grid although in AMG methods there is no real underlying geometric grid. However, to pass from _n_ to _n<sub>c</sub>_ variables and vice versa, a restriction matrix \(R\in\mathbb{C}^{n\times n_c}\) and an interpolation matrix \(P\in\mathbb{C}^{n\times n_c}\) are needed. The coarse grid matrix is then given by

\(A_c=R^HAP\in\mathbb{C}^{n_c\times n_c}\)

which we always assume to be nonsingular. This implies that _R_ and _P_ must have full rank. For handling singular coarse grid system see e.g. \[33, 15\]. For HPD _A_, the typical choice is _R=P_ with full rank which always yields nonsingular _A<sub>c</sub>_.<br>
A typical approach to guarantee the convergence of a two-grid method is to assume some kind of smoothing and approximation property of the smoothing step and the coarse-grid correction, respectively. We follow this strategy in order to establish _B_- norm bounds for the algebraic two-grid error operator.

**3.1. The coarse-grid correction.** We start the analysis with the coarse-grid correction \(\Pi_A\) where

\(\Pi_A:=\Pi_A(P,R):=P(R^HAP)^{-1}R^HA=PA_c^{-1}R^HA\in\mathbb{C}^{n\times n}\)

is a projection onto R(_P_) along N(_R<sup>H</sup>A_). Here, we write \(\Pi_A(P,R)\) to denote the dependency on _P_ and _R_.<br>
A key property for the following proofs is the _B_-orthogonality of the coarse-grid correction. This property can be characterized by multiple equivalent conditions, some of which we have already introduced in section 2. The following result summarizes some of them based on the Lemmas 2.3 and 2.4 and \[35, Corollary 2\].

Lemma 3.1. _Let_ \(R,P\in\mathbb{C}^{n\times n_c}\) _such that R<sup>H</sup>AP be nonsingular. Then_ \(\Pi_A\) _is a projection and the following statements are equivalent:_


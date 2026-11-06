<tbc>Here, \(\mathcal{U}^{\perp_B}\) denotes the _B_-orthogonal complement of U.<br>
Note that we use the term _B_-orthogonal both for vectors and for projections. However, it is always clear from the context which concept is used. It follows from the definition that a projection \(\Pi\) is _B_-orthogonal if and only if

\(\mathcal{R}(\Pi)^{\perp_B}=\mathcal{N}(\Pi)\text{or equivalently}\mathcal{R}(\Pi)\perp_B\mathcal{N}(\Pi).\)

One can also prove the following lemma (see \[35, Lemma 1\]).

Lemma 2.3. _A projection_ \(\Pi\) _is B-orthogonal if and only if_

(2.1) \(\Pi=B^{-1}\Pi^HB.\)

The following result (cf. \[35, Lemma 3\] and \[36, Lemma 3.6\]) gives a useful characterization for the _B_-norm of a projection and its connection to _B_-orthogonality.

Lemma 2.4. _Let_ \(\Pi\in\mathbb{C}^{n\times n}\) _be a projection with_ \(\Pi\neq 0\) _and_ \(\Pi\neq I_n\)_. Then it holds_ \(\|\Pi\|_B=\|I-\Pi\|_B\) _and_

\(\|\Pi\|_B^2=1+sup_{x\in\mathcal{R}(\Pi)^{\perp_B}}\frac{\|\Pi x\|_B^2}{\|x\|_B^2}\)

_with_ \(\|\Pi\|_B^2=1\) _if and only if_ \(\Pi\) _is B-orthogonal._

Based on this idea of _B_-orthogonality, we introduce the general concept of the adjoint with respect to the _B_-inner product.

Definition 2.5. _Let_ \(A\in\mathbb{C}^{n\times n}\)_. The B-adjoint of A is defined as A_<sup>+</sup>=_B_<sup>-1</sup>_A<sup>H</sup>B. Then we say that A is B-normal if AA_<sup>+</sup>=_A_<sup>+</sup>_A and A is B-orthogonal if A_<sup>+</sup>=_A._

The definition of _B_-adjoint is motivated by the fact that it is the unique matrix with

\(\langle Ax,y\rangle_B=\langle x,A^+y\rangle_B\)

for all \(x,y\in\mathbb{C}^n\). For the standard inner product, that is _B=I<sub>n</sub>_, the _I<sub>n</sub>_-adjoint reduces to the Hermitian transpose and hence an _I<sub>n</sub>_-orthogonal matrix is Hermitian. If _A_ is HPD and we consider the _A_-inner product, the _A_-adjoint is given by _A_. The definition of _B_-orthogonality in Definition 2.5 is consistent with the result of Lemma 2.3 because the right hand side of (2.1) is exactly the _B_-adjoint of \(\Pi\). It is also easy to see that a _B_-orthogonal matrix _A_ is _B_-normal as well and satisfies _A<sup>H</sup>B=BA_.<br>
The close relation of the _B_-adjoint to the Hermitian transpose also shows in its other properties.

Proposition 2.6. _Let_ \(A,C\in\mathbb{C}^{n\times n}\)_, then it holds_ (_A+C_)<sup>+</sup>=_A_<sup>+</sup>+_C_<sup>+</sup>, (_AC_)<sup>+</sup>=_C_<sup>+</sup>_A_<sup>+</sup> _and_ (_A_<sup>+</sup>)<sup>+</sup>=_A._

_Remark_ 2.7. One can argue that it would be more suitable to say a matrix is _B_- Hermitian instead of _B_-orthogonal since the _B_-adjoint reduces to the Hermitian transpose for _B=I<sub>n</sub>_. But our focus is on projections where the notion of _B_-orthogonal projections is already established and therefore we use the term _B_-orthogonal.

Although _B_-orthogonality is a useful property, its assumption is very restricting. We will show that the weaker assumption of _B_-normality is often sufficient for our purposes. Similarly to classical normality there exist a lot of equivalent characterizations for _B_-normality. In \[6\] and \[13\] detailed lists with equivalent properties of _I<sub>n</sub>_-normality can be found. Most of these properties can be generalized to _B_-normal matrices. We state a few selected characterizations that are relevant for this work.


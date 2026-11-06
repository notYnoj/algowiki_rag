# A FLEXIBLE SHORT RECURRENCE KRYLOV SUBSPACE METHOD FOR MATRICES ARISING IN THE TIME INTEGRATION OF PORT HAMILTONIAN SYSTEMS AND ODES/DAES WITH A DISSIPATIVE HAMILTONIAN

**Abstract.** For several classes of mathematical models that yield linear systems, the splitting of the matrix into its Hermitian and skew Hermitian parts is naturally related to properties of the underlying model. This is particularly so for discretizations of dissipative Hamiltonian ODEs, DAEs and port Hamiltonian systems where, in addition, the Hermitian part is positive definite or semi- definite. It is then possible to develop short recurrence optimal Krylov subspace methods in which the Hermitian part is used as a preconditioner. In this paper we develop new, right preconditioned variants of this approach which as their crucial new feature allow the systems with the Hermitian part to be solved only approximately in each iteration while keeping the short recurrences. This new class of methods is particularly efficient as it allows, for example, to use few steps of a multigrid solver or a (preconditioned) CG method for the Hermitian part in each iteration. We illustrate this with several numerical experiments for large scale systems.

**Key words.** Krylov subspace, short recurrence, right preconditioning, optimal methods, flexible preconditioning, dissipative Hamiltonian, port Hamiltonian systems, implicit time integration

**AMS subject classifications.** 65F08, 65F10, 65L04, 65L80

**1. Introduction.** Consider the linear system

\(Ax=b,A\in\mathbb{C}^{n\times n},\)

and the splitting

\(A=H+S\)

with \(H=\frac{1}{2}(A+A^*)\) the Hermitian and \(S=\frac{1}{2}(A-A^*)\) the skew Hermitian part of _A_, _H_<sup>∗</sup>=_H,S_<sup>∗</sup>=-_S_. Here, <sup>∗</sup> denotes the adjoint with respect to the standard inner product, i.e., for any matrix _B_ the matrix _B_<sup>∗</sup> is obtained by transposing _B_ and taking complex conjugates for each entry.

In several important applications, and in particular in linear systems arising from discretizations of dissipative Hamiltonian ODEs and certain port Hamiltonian systems, the hermitian part _H_ is positive definite and "dominates" _S_ in the sense that _H_<sup>-1</sup>_S_ or _S_ is small. Then, _H_ is an efficient preconditioner for _A_, and as we will discuss in Section 2, there exist optimal short recurrence Krylov subspace methods using this preconditioner.

Each iterative step of these methods requires one exact solve with the matrix _H_. The purpose of this paper is to go one step further and investigate practically important short recurrence methods where the solves with _H_ are performed only approximately. For example, we might want to use an incomplete Cholesky factorization in cases where an exact factorization is too expensive, or we might want to perform just some steps of (plain or preconditioned) CG or a multigrid solver for _H_. We believe that this is an aspect of primordial importance: As long as systems are small enough such that direct factorizations with _A_ are feasible, there is no real need to consider an iterative method which, after all, requires again a direct factorization of

<sup>∗</sup>University of Wuppertal, Department of Mathematics, Gauss-Strasse 20, 42097 Wuppertal, Germany (mdiab@uni-wuppertal.de, frommer@uni-wuppertal.de, kkahl@uni-wuppertal.de ).

MALAK DIAB, ANDREAS FROMMER AND KARSTEN KAHL<sup>∗</sup>

arXiv:2212.14208v1 [math.NA] 29 Dec 2022


<tbc>by allowing arbitrary Hilbert spaces while preserving the tensor-product rule for combining separated systems.1

There is, however, a more general _commuting-operator_ model of quantum theory, where independent systems are associated to commuting operator algebras acting on a common Hilbert space (see e.g. Def. 2, 3, 5 of \[LG23\]). This model strictly contains the closure of the tensor-product model, as follows from the breakthrough result MIP<sup>∗</sup>=RE \[JNVWY21\].2

For standard bipartite Bell scenarios, the main systematic tool for proving that a distribution is impossible in the commuting-operator model is the Navascués-Pironio-Acín (NPA) hierarchy \[NPA07; NPA08\]. In contrast, the result MIP<sup>∗</sup>=RE implies that there can be no analogous complete decision procedure for the tensor-product model in full generality. Thus, a natural route for extending our lower bound beyond finite-dimensional exact strategies is to reformulate it directly in the commuting-operator model, and to use distributed analogues of the NPA hierarchy, such as the inflation-NPA hierarchy \[WPGRAN21\].

## 3. Preliminaries

### Mathematical Notation.

We use N, R, and C to denote the integers greater than zero, the reals, and the complex numbers respectively. For an integer \(n\ge 1\), we use \[_n_\]={1,2_,...,n_}. For a Hilbert space _H_, we use \(|u\rangle\) to denote vectors of _H_ and \(\langle u|\) for the corresponding co-vector. The space of complex \(d\times d\) matrices is written Mat_<sub>d</sub>_(C) and the space of endomorphisms of a vector space _E_ is denoted by End(_E_). The identity matrix is written as 1. Given an operator _P_, we write the adjoint (i.e., the conjugate-transpose), the conjugate and the transpose as _P_<sup>†</sup>, <o>_P_</o> and \(P^\top\), respectively.

### 3.1. Quantum Information Theory Basics.

We present here the essential for following our proofs and refer readers to \[NC10; Wat18\] for an extensive introduction.

For \(d\in\mathbb{N}\), a _d_-dimensional _register_ is a complex Euclidian space isomorphic to C_<sup>d</sup>_ and represents a physical device holding information. Throughout, we use sans-serif letters X,Y,Z to represents registers. A _state vector_ on X is simply a vector \(u\in\mathsf{X}\). A _(quantum) state_ on register \(\mathsf{X}\simeq\mathbb{C}^d\) is a density matrix \(\rho\): (1) \(\rho\) is a \(d\times d\) matrix with complex coefficients, (2) \(\rho\) is positive semi-definite, and (3) the trace of \(\rho\) is one. To provide some intuition, recall that from the spectral theorem, any positive semi-definite matrix (and, in particular, any density matrix) \(\rho\) can be written as

(4) \(\rho=\sum_{i=1}^r\lambda_i|u_i\rangle\langle u_i|,\)

where the \(\lambda_1,\lambda_2,\dots,\lambda_r\in\mathbb{R}_{\ge 0}\) are the eigenvalues of \(\rho\) and \(|u_1\rangle,|u_2\rangle,\dots,|u_r\rangle\in\mathbb{C}^d\) are the corresponding eigenvectors. Since the trace of \(\rho\) is one, we have that \(\sum_i\lambda_i=1\); in other words, \(\rho\) describes a probability distribution over state vectors. When \(\rho=|u\rangle\langle u|\) has rank one, we say that it is a _pure state_. A state on two registers X,Y is a state on \(\mathsf{X}\otimes\mathsf{Y}\).

Operations on a quantum state are in full generality represented by quantum channels. For the purpose of this paper, we only need two kinds of operations on quantum states: applying a unitary, and performing a measurement followed by some classical computation. If X is in a state \(\rho\) and we apply the unitary _U_ on _X_, the state becomes \(U\rho U^\dagger\). For intuition, consider applying _U_ to each \(|u_i\rangle\) in Eq (4) and observe the resulting density matrix. A _measurement_ on

1In the standard Bell scenario, the corresponding set of correlations is usually denoted C_<sub>qs</sub>_. Since this set is not closed in general \[Slo19\], one often considers its closure C_<sub>qa</sub>_. 2Unlike C_<sub>qs</sub>_, the set C_<sub>qc</sub>_ is closed.


## 4 Convergence Analysis

We now establish the rigorous theoretical convergence and oracle complexities for both variants of the 3-Circuit CRVG. Let \(f(\theta)\) be the unconstrained objective function representing the expectation value of a target Hamiltonian _H_, bounded below by _f_<sup>∗</sup>.

### 4.1 Assumptions

**Assumption 1** (Lower Boundedness)**.** The objective function \(f:\mathbb{R}^p\rightarrow\mathbb{R}\) is bounded below, i.e., there exists \(f^*>-\infty\) such that \(f(\theta)\ge f^*\) for all \(\theta\in\mathbb{R}^p\).

_Justification._ In VQAs, \(f(\theta)=\langle\psi(\theta)|H|\psi(\theta)\rangle\) is the expectation value of a Hermitian operator _H_ with finite spectrum. Since _H_ has a minimum eigenvalue \(\lambda_{min}(H)\), we have \(f(\theta)\ge\lambda_{min}(H)>-\infty\) for all \(\theta\).

**Assumption 2** (Bounded norm Hermitian _H_)**.** The norm of the Hermitian operator _H_ is bounded, i.e., there exists _G\>_0 such that \(\|H\|\le G\).

_Justification._ In the theoretical analysis of Variational Quantum Algorithms (VQAs), the parameter landscape’s Lipschitz smoothness is governed by the spectral norm of the target observable, \(\|H\|\). In classical optimization, assuming a globally bounded norm for the objective function’s generator can sometimes be considered a restrictive or artificial constraint. However, in the quantum setting, the upper bound of \(\|H\|\) is a strict mathematical guarantee arising directly from the finite-dimensional nature of the qubit system.

**1. Finite-Dimensional Spectral Bound**

Consider a quantum system composed of _n_ qubits. The corresponding Hilbert space H has a finite dimension of _d_=2_<sup>n</sup>_. The target Hamiltonian _H_ is a Hermitian operator acting on this finite-dimensional space, represented by a \(2^n\times 2^n\) matrix.

A foundational theorem in functional analysis states that every linear operator on a finite-dimensional vector space is bounded. The spectral norm of _H_, denoted as \(\|H\|_2\) (or simply \(\|H\|\)), is defined as the maximum absolute value of its eigenvalues:

\(\|H\|=max_{1\le i\le 2^n}|\lambda_i|.\) (7)

Because the matrix has exactly 2_<sup>n</sup>_ eigenvalues, the spectrum is discrete and finite. Therefore, a finite maximum must always exist, guaranteeing that \(\|H\|<\infty\).

**2. Analytical Upper Bound via Pauli Decomposition**

Beyond the existential guarantee, the upper bound of \(\|H\|\) can be strictly calculated in practice. In VQE and QAOA formulations, the Hamiltonian is typically decomposed into a linear combination of _K_ Pauli strings (tensor products of Pauli matrices _I,X,Y,Z_):

\(H=\sum_{i=1}^Kc_iP_i,\) (8)

where \(c_i\in\mathbb{R}\) are the scalar coefficients and \(P_i\in\{I,X,Y,Z\}^{\otimes n}\).

Because every Pauli string _P<sub>i</sub>_ is both unitary and Hermitian, its eigenvalues are strictly \(\pm 1\), meaning its spectral norm is exactly exactly unity (\(\|P_i\|=1\) for all _i_). By applying the triangle inequality and the scalar multiplication property of norms, we can establish a strict, analytically computable upper bound for the Hamiltonian:

\(\|H\|=\left\|\sum_{i=1}^Kc_iP_i\right\|\le\sum_{i=1}^K\|c_iP_i\|=\sum_{i=1}^K|c_i|\|P_i\|=\sum_{i=1}^K|c_i|.\) (9)

The Hamiltonian norm is strictly bounded from above by the _L_<sub>1</sub>-norm of its Pauli coefficients (\(\|H\|\le\sum|c_i|\)).

Consequently, the worst-case Lipschitz smoothness constant derived in our analysis (\(L\le p\|H\|\)) is fundamentally constrained by the physics of the parameterized circuit. The landscape is mathematically guaranteed to be globally _L_-smooth without requiring any artificial bounds or regularization, ensuring the rigorous applicability of the CRVG convergence theorems.

**Lemma 1** (Smooth)**.** For Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA) objective functions parameterized by Pauli generators, the gradient \(\nabla f(\theta)\) is Lipschitz continuous with respect to the Hamiltonian norm and parameter dimension _p_:

\(\|\nabla f(x)-\nabla f(y)\|\le p\|H\|\|x-y\|\text{for all}x,y\in\mathbb{R}^p.\) (10)


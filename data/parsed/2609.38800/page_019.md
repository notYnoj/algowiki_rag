### A.2 Standard SPSA

SPSA approximates the gradient using a single random perturbation vector \(\Delta\in\{-1,+1\}^p\). Because the objective function is projected along this _p_-dimensional random vector, SPSA injects a severe spatial variance that strictly scales linearly with the dimension of the parameter space, yielding \(\sigma_{SPSA}^2=\mathcal{O}(p)\).

• **Iteration Complexity:** Given the inflated spatial variance \(\sigma^2=\mathcal{O}(p)\), the optimizer must take significantly more steps to average out the injected noise. The required iterations scale as \(T_{SPSA}=\mathcal{O}(p/\epsilon^4)\).<tbc>

• **Inner-Loop Cost:** SPSA requires only a constant 2 circuit evaluations per step, giving an optimal inner cost of O(1).<tbc>

• **Total Sample Complexity:**<tbc>

\(\mathcal{C}_{SPSA}=T_{SPSA}\times\mathcal{O}(1)=\mathcal{O}\left(\frac{p}{\epsilon^4}\right)\times\mathcal{O}(1)=\mathcal{O}\left(\frac{p}{\epsilon^4}\right).\) \(\text{(29)}\)

This derivation formally demonstrates the dimensionality barrier in standard quantum optimization. SPSA achieves a highly efficient O(1) per-step execution cost, but its O(_p_) spatial variance penalty forces an \(\mathcal{O}(p/\epsilon^4)\) total complexity. Conversely, while PSR avoids spatial variance, its structural requirement to evaluate 2_p_ circuits per step yields an even worse \(\mathcal{O}(p^2/\epsilon^4)\) asymptotic sample complexity under finite-shot execution.

## B Technical Proofs

### B.1 Proof of Lemma 1

_Proof._ The objective function of a standard VQA is given by the expectation value of an observable (Hamiltonian) _H_:

\(f(\theta)=\langle 0|U^\dagger(\theta)HU(\theta)|0\rangle\) (30)

where the parameterized ansatz \(U(\theta)\) is composed of _p_ sequential gates:

\(U(\theta)=\prod_{j=1}^pW_je^{-i\theta_jP_j/2}\) (31)

Here, _W<sub>j</sub>_ are fixed unparameterized unitaries (such as entangling CNOT layers) and _P<sub>j</sub>_ are the Hermitian generators of the parameterized rotations. In both VQE (using hardware-efficient _R<sub>x</sub>_, _R<sub>y</sub>,R<sub>z</sub>_ gates) and QAOA, these generators are involutory Pauli strings, satisfying \(P_j^2=I\) and having a bounded spectral norm \(\|P_j\|\le 1\).

To establish _L_-smoothness, we must show that the spectral norm of the Hessian matrix \(\nabla^2f(\theta)\) is strictly bounded. We evaluate the second-order partial derivatives \(H_{jk}=\frac{\partial^2f}{\partial\theta_j\partial\theta_k}\).

By applying the derivative of the matrix exponential \(\frac{\partial}{\partial\theta_j}e^{-i\theta_jP_j/2}=-\frac{i}{2}P_je^{-i\theta_jP_j/2}\), the first derivative with respect to \(\theta_j\) can be expressed as a commutator:

\(\frac{\partial f}{\partial\theta_j}=\frac{i}{2}\langle 0|U_A^\dagger[P_j,\tilde{H}_j]U_A|0\rangle\) (32)

where \(\tilde{H}_j\) is the Hamiltonian transformed by the subsequent gates, and _U<sub>A</sub>_ represents the gates preceding \(\theta_j\).

Taking the second derivative with respect to another parameter \(\theta_k\) (assume without loss of generality that _k\>j_), we obtain nested commutators:

\(H_{jk}=\frac{\partial^2f}{\partial\theta_j\partial\theta_k}=-\frac{1}{4}\langle 0|U_A^\dagger[P_j,[P_k,\tilde{H}_{jk}]]U_A|0\rangle\) (33)

We can bound the magnitude of any element of the Hessian using the sub-multiplicative property of the operator norm and the generalized triangle inequality for commutators (\(\|[A,B]\|\le 2\|A\|B\|\)):<tbc>

\(|H_{jk}|\le\frac{1}{4}\|[P_j,[P_k,\tilde{H}_{jk}]]\|\le\frac{1}{4}\left(2\|P_j\|\cdot\|[P_k,\tilde{H}_{jk}]\|\right)\le\frac{1}{4}\left(2\|P_j\|\cdot 2\|P_k\|\cdot\|\tilde{H}_{jk}\|\right).\)

<tbc>Because unitary transformations preserve the spectral norm, \(\|\tilde{H}_{jk}\|=\|H\|\). Furthermore, because the generators are Pauli strings, \(\|P_j\|=\|P_k\|=1\). This yields a strict, global bound on every element of the Hessian matrix:

\(|H_{jk}|\le\|H\|\) (34)


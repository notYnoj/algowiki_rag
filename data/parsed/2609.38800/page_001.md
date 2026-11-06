# BREAKING THE SHOT-NOISE BARRIER: CACHED RECYCLED VARIANCE-REDUCED GRADIENTS FOR QUANTUM OPTIMIZATION

**Lam M. Nguyen**<sup>1</sup> **, Sumanta Mukherjee**<sup>1</sup> **, Dzung T. Phan**<sup>1</sup><br>
<sup>1</sup> IBM Research<br>
`amNguyen.MLTD@ibm.com, sumanm03@in.ibm.com, phandu@us.ibm.com`<tbc>

<tbc>**ABSTRACT**<tbc>

<tbc>Variational Quantum Algorithms (VQAs) rely heavily on classical optimization routines to navigate high-dimensional, noisy parameter landscapes. However, the evaluation of analytical gradients via the parameter-shift rule requires O(_p_) circuit executions, rendering this approach computationally prohibitive for deep circuits. While simultaneous perturbation methods provide an O(1) alternative, their gradient estimates suffer from severe O(_p_) spatial variance, which impedes convergence. To resolve this tension, we introduce the Cached Recycled Variance-Reduced Gradient (CRVG) by leveraging variance reduction techniques. We formulate two variants: a 3-Circuit (1-Sided) Non- Recursive CRVG and a Recursive CRVG. By introducing a center-point caching mechanism, the 3-Circuit CRVG mathematically recycles quantum measurements to reduce the inner-loop circuit complexity by 25% across both variants. We establish a theoretical separation between the two routing paths to achieve an \(\epsilon^2\)-stationary point: the non-recursive variant reaches a sample complexity of \(\mathcal{O}(max\{p/\epsilon^2,p^{2/3}/\epsilon^{10/3}\})\), while the recursive variant achieves an improved complexity of \(\mathcal{O}(max\{p/\epsilon^2,\sqrt{p}/\epsilon^3\})\). Empirically, extensive evaluations on MaxCut and Maximum Independent Set (MIS) benchmarks validate these findings. While standard simultaneous perturbation remains a robust baseline across varying depths, CRVG demonstrates targeted advantages in specific amortizable regimes, such as the non-recursive variant on EfficientSU2 circuits and both variants on depth- three QAOA, yielding superior energy minimums and tighter output variances. Ultimately, CRVG establishes a principled bias-throughput trade-off for scaling near-term quantum optimization.

### 1 Introduction

The promise of Noisy Intermediate-Scale Quantum (NISQ) devices [Preskill, 2018] hinges on the success of Variational Quantum Algorithms (VQAs), hybrid quantum-classical protocols in which a parameterized quantum circuit \(U(\theta)\) prepares a trial state \(|\psi(\theta)\rangle\), and a classical optimizer tunes the parameters \(\theta\in\mathbb{R}^p\) to minimize the expectation value of a target Hamiltonian [Peruzzo et al., 2014, Farhi et al., 2014, Cerezo et al., 2021]:

The Variational Quantum Eigensolver (VQE) [Peruzzo et al., 2014] and the Quantum Approximate Optimization Algorithm (QAOA) [Farhi et al., 2014] are canonical instances that have been demonstrated on present-day hardware for problems in quantum chemistry [Kandala et al., 2017] and combinatorial optimization [Harrigan et al., 2021].

However, the efficacy of the classical optimizer is fundamentally constrained by the quantum hardware. In classical machine learning, backpropagation computes the full gradient of a neural network in a single backward pass, with variance typically stemming only from data subsampling or mini-batching. In contrast, quantum circuits are treated as black-box oracles that suffer from two distinct, compounding sources of noise: physical shot noise (the inherent variance of projecting a quantum state into a classical bitstring) and algorithmic spatial noise (the variance injected by stochastic gradient approximation).

\(f(\theta)=\langle 0|U^\dagger(\theta)HU(\theta)|0\rangle.\) (1)


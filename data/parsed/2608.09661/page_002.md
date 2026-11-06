Shaw flow) as validation targets and performed simulation on the Frontier supercomputer.<tbc>

\(\bullet\) We implement and compare multiple linear-combination- of-unitaries (LCU) decomposition methods for VQLS initialization and quantify their runtime and memory trade-offs.<tbc>

\(\bullet\) We introduce an approximate (tolerance-controlled) parallel Pauli decomposition and characterize its accuracy- cost trade-off on large Toeplitz systems, demonstrating how truncation can drastically reduce LCU term count and VQLS circuit workload while controlling the relative Frobenius error.<tbc>

\(\bullet\) We evaluate 11 quantum ansatz families on a canonical Hele-Shaw problem and connect convergence behavior to expressibility and entanglement metrics.

The rest of the paper is organized as follows: Section II reviews related work on quantum linear systems algorithms and VQLS, and identifies the open challenges that motivate our study. Section III provides the mathematical background for VQLS and the target CFD problems and the detail of our implementation of matrix decompositions and the HPC- integrated workflow of VQLS and its variants. Section IV presents our numerical results, including the ansatz comparison and scaling studies on the Frontier supercomputer. Finally, Section V concludes with a discussion of future directions for quantum linear solvers and potential applications.

## II. RELATED WORKS

Quantum computing introduced the possibility of asymptotic speedups for certain linear algebra tasks. In particular, quantum linear systems algorithms (QLSAs) aim to prepare a quantum state proportional to the solution vector, \(|x\rangle\propto A^{-1}|b\rangle\), rather than outputting all components of **x** explicitly. The Harrow-Hassidim-Lloyd (HHL) algorithm was the first widely recognized QLSA and suggested an exponential improvement in the dependence on _N_ \[7\]. However, HHL and related approaches typically incur polynomial overhead in \(\kappa\) and _s_, and they rely on quantum phase estimation (QPE), which can increase circuit depth tremendously as tighter approximation error \(\epsilon\) and accurate encoding of the input matrix are required. These factors are critical: for matrices encountered in real-world discretized PDEs, the condition number can grow rapidly with mesh refinement, and deep circuits are challenging on current devices.

Numerous variations of the HHL algorithm have been introduced in the past decade to reduce the dependence on \(\kappa\) and QPE \[8\]-\[13\], with the best approach demonstrating a complexity of \(\mathcal{O}(\kappa log\kappa/\epsilon)\) \[14\]-\[16\]. However, the large circuits generated from these algorithms limit their scalability to practical problems on current Noisy Intermediate-Scale Quantum (NISQ) computers. Practical demonstrations of such algorithms on current hardware remain limited to small or highly structured instances. In the current era of NISQ devices, variational quantum-classical algorithms are appealing for practical workloads \[17\]. One such variational algorithm for<tbc>

<tbc>solving linear systems of equations was introduced by \[18\], namely the Variational Quantum Linear Solver (VQLS).

While fault-tolerant quantum computers remain a long-term goal, the present generation of NISQ devices has encouraged the development of hybrid quantum-classical algorithms that can operate with limited qubit counts and constrained circuit depths. Variational approaches can replace deep QPE subroutines with parameterized quantum circuits trained by a classical optimizer \[17\]. VQLS follows this philosophy by formulating the linear solve as an optimization problem and by leveraging measurements to evaluate a cost function whose minimizer corresponds to the desired solution state.

VQLS has been explored as a route to scalable quantum linear solvers on existing hardware and simulators, including demonstrations on matrices with sizes up to \(1024\times 1024\) in superconducting platforms \[18\]. Beyond proof-of-principle linear algebra, VQLS has also been proposed and applied in domain settings such as fluid dynamics \[19\]-\[22\], aligning closely with our focus on canonical flow problems on NISQ devices \[23\], \[24\]. Despite this progress, there remains a gap between algorithmic descriptions and an end-to-end workflow that is robust enough for CFD-style matrices and practical enough to be embedded in hybrid quantum-HPC environments.

In particular, deploying VQLS at scale raises several interconnected questions that are not always addressed systematically in application-focused studies. First, the matrix _A_ must be encoded in a form suitable for the quantum subroutines used to evaluate the VQLS objective, and this step can become the dominant cost driver if it produces a large number of terms. Second, the choice of ansatz family impacts trainability and expressivity, and can interact strongly with problem structure: ansatz circuits that work for small, toy matrices may not generalize to structured CFD operators. Third, the performance and stability of the classical optimizer depend on the measurement noise model, the number of shots, and the cost landscape, which can vary substantially across matrix families and decomposition strategies. Finally, even when the quantum circuits themselves are relatively small, practical experimentation often requires running large ensembles of circuits across many optimization iterations, which naturally suggests HPC-style execution; however, the mapping between VQLS workloads and HPC parallelization strategies is subtle and can be counterintuitive.

## III. METHODOLOGY AND PROBLEM SETUP

### A. Algorithm Overview

The objective of the VQLS algorithm is to find the state vector \(|x\rangle\) for \(x\in\mathbb{R}^N\), using a hybrid quantum-classical optimization approach. Given a guess for the vector, \(|\tilde{x}\rangle\), a corresponding vector \(|\tilde{b}\rangle\) can be found by

\(|\tilde{b}\rangle:=\frac{A|\tilde{x}\rangle}{\sqrt{\langle\tilde{x}|A^\dagger A|\tilde{x}\rangle}}\approx|b\rangle.\) (1)


# Riemannian tion of Sample-Based Quantum Krylov Solvers for Elliptic Problems: Energy-Norm Guarantees and Duct-Flow Applications

Doyeol (David) Ahn<sup>∗1,2</sup> and Byeongyong Park<sup>1</sup>

<sup>1</sup>Center for Quantum Information Processing, University of Seoul, 163 Seoulsiripdae-ro, Dongdaemun-gu, Seoul 02504, Republic of Korea

<sup>2</sup>Singularity Quantum Inc., 9506 Villa Isle Drive, Villa Park, California 92861, USA

**Abstract**

Sample-based quantum linear solvers measure quantum Krylov states _e_<sup>-_iAT_</sup>|_b_〉 and reconstruct the solution of _Ax=b_ classically on the observed basis states. We develop this approach for positive- definite systems that arise from elliptic partial differential equations. We formulate the sampling in any fixed basis with an efficient transform and reconstruct the solution by a Galerkin solve on the sampled set. For this reconstruction we derive expected and high-probability energy-norm error bounds, a sample complexity in terms of the smallest sampling probability on an essential set, a computable residual certificate, and a support-completeness theorem for the dephased outcome law. We formulate the method for elliptic problems on Riemannian cross sections. In two dimensions the stiffness matrix is metric-independent in conformal coordinates, and curved vessels lead to the same matrix class. Killing symmetries of the cross section give selection rules for the measurement outcomes, and the Lie derivative of the metric gives first-order bounds for geometric perturbations. As examples we treat the implicit step of pulsatile flow in elliptic, lens-shaped, and curved ducts. In simulations of up to 12 qubits, the number of Fourier modes required for 1% error grows from 14 to 60 while the number of unknowns grows from 64 to 4096. A classical residual-greedy selection is nevertheless more efficient than quantum sampling in all cases studied. On trapped-ion and superconducting processors with six and eight qubits, the outcome laws follow a replacement-noise model whose noiseless fraction decays by about 0.6% per logical two-qubit gate on both platforms, and a parity selection rule rejects shots at the predicted rate. At these sizes the samples cover nearly the whole admissible space, so the experiments test the outcome laws but not dimension reduction.

### 1 Introduction

Many problems in science and engineering lead to large linear systems _Ax=b_. Quantum algorithms for this task began with the algorithm of Harrow, Hassidim, and Lloyd [1] and were improved by later methods based on linear combinations of unitaries and quantum signal processing [2]. These algorithms prepare the solution as a quantum state. In order to read out the solution, however, one must estimate many amplitudes, and the required circuits are deep. Variational methods [3, 4] use shallow circuits, but they rely on a classical optimization without guarantees.

Sample-based methods take a different route. In sample-based quantum diagonalization (SQD), a quantum processor generates bitstrings, and a classical computer diagonalizes the Hamiltonian in the subspace spanned by these bitstrings [5]. Its performance depends on recovery procedures that repair noisy samples by using constraints visible in the measurement outcomes, such as particle-number symmetry [5]. These procedures have been extended to strongly correlated systems [6] and, through code-space<tbc>

<sup>∗</sup>Corresponding author: dahn@uos.ac.kr


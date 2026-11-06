<tbc>learning approach to construct the preconditioners solely from the input gauge configuration, directly applicable as matrix-vector products without assembling or storing explicit matrices. While this framework is general, in this work, we focus on the Schwinger model _U_(1) gauge theory in 1+1 dimensions with two flavors of mass-degenerate fermions as a proof of concept to show the viability of the proposed technique. We demonstrate the performance of the proposed method by solving the Wilson-Dirac normal equations with different lattice sizes and show the resulting preconditioners effectively reduce the number of iterations required for convergence in the CG solver. Moreover, models trained on a single lattice gauge configuration ensemble can immediately act as effective preconditioners for systems of other lattice sizes, achieving zero-shot transfer. This eliminates the need for retraining for unseen gauge configurations, at least within the parameter ranges explored in this work. We summarize the contribution of this work as follows

\(\bullet\) We propose a framework leveraging an _operator learning_ method to construct effective preconditioners for solving Wilson-Dirac normal equations.<tbc>

\(\bullet\) The framework is completely _matrix-free_ where it only operates on lattice gauge field configurations and _does not_ construct explicit matrices for either the linear operators or their preconditioners.<tbc>

\(\bullet\) We train the model in an unsupervised way and use random projections to formulate a loss function that is effective and efficient in model training, avoiding expensive condition number computation.<tbc>

\(\bullet\) The trained models produce preconditioners that can be directly integrated into CG solvers, approximately halving the required number of iterations for convergence.<tbc>

\(\bullet\) The proposed framework learns a general mapping applicable for _unseen_ lattice ensembles of different parameters and sizes, attaining zero-shot performance comparable to that of networks trained for specific action parameters.

In the remainder of this paper, we briefly discuss the related concepts in preconditioning, machine learning-based preconditioners, and operator learning frameworks in Section 2. We then describe the details of the proposed approach in Section 3 and present and analyze its performance on<tbc>

Uμ(x)
A = (D+D)[Uμ(x), K]
GO
Preconditioner Construction
PCG(A, b, T)
Uμ(x)
T = (D+D)[Uμ(x), K]
Field Configuration
Linear Operator (mat-vec product)

Fig. 1. Matrix-free neural preconditioner for the discretized Dirac operator calculated from a given gauge configuration \(U_\mu(x)\). The trained neural network \(\mathcal{G}_\theta\) outputs another set of configurations \(\tilde{U}_\mu(x)\) and uses the same discretization scheme (same \(\kappa\)) for the original system to construct the preconditioning operator \(\Gamma\). For a given linear system, we can directly pass the original and preconditioning operators, _A_ and \(\Gamma\), as well as the right hand side _b_ to a Preconditioned Conjugate Gradient (PCG) solver. All processes involved do not use explicit matrices.


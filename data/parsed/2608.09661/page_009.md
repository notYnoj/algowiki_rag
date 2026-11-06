<tbc>the best efficiency. The ‘basic’ and ‘opt-cl’ ansatz have the worst expressibility due to the lack of CX gates to create entanglement.

Figure 9 compares optimizer convergence across ansatz choices on the _n<sub>x</sub>=n<sub>y</sub>_=4 Hele-Shaw instance. We use it to identify ansatz that reliably reach low cost within the fixed iteration budget and to highlight cases that either converge rapidly (steeper initial decrease) or stagnate (plateau above the target threshold).

We simulated a canonical Hele-Shaw flow problem on a \(4\times 4\) grid using the quantum ansatz listed in  I. Optimization was performed using the torch-based NAdam optimizer integrated within PyTorch, with learning curves illustrated in Figure 9. The majority of the ansatz converged within 100 optimization steps. Notably, Opt-Mix and Global Entanglement demonstrated the fastest performance, converging in fewer than 40 steps. The Basic, Opt-2, Opt-C1, and Opt-C2 ansatz required between 50 and 60 steps. Conversely, Problem Inspired, Opt-C9, and Strong Entanglement failed to reach a cost function value below 0.01 within the 100- step limit. Interestingly, convergence performance does not align with the KL divergence values observed in  I. For instance, while the Strong Entanglement ansatz exhibits high expressibility, it showed poor convergence for the Hele-Shaw<tbc>

<tbc>problem. In contrast, the Opt-C1 and Basic ansatz converged successfully despite lacking entanglement.

We also performed Scipy-based optimizers ‘COBYLA’, ‘L- BFGS-B’, ‘Nelder-Mead’, integrated in ‘Scipy’ python package using three different quantum ansatz using three layers of ‘Strong Entanglement’, ‘Real Amplitudes’, and ‘ Opt-Mix’ solving a 4 by 4 grid points on Figure 10. From the figure, we observe a inefficiency performing optimization compared to the torch-based approach, as they generally require more function evaluations or fail to reach the same low cost values within the iteration limit.

## E. HPC timing scalability of standard VQLS and cVQLS

We performed simulations on the Frontier supercomputer. We used both `lightning.qubit` and `lightning.kokkos` to measure time per VQLS iteration and assess scalability with the available simulators. In this setting, Scipy-based optimizers such as COBYLA enable batching and parallel circuit evaluation, which benefits from CPU multi-threading to improve the performance on HPC system, whereas Torch-based optimization is effectively sequential and therefore less amenable to circuit-level parallelism.

Figure 11 demonstrates the performance of average time consumption per iteration of VQLS and coherent VQLS algorithm using the pennylene `lightning.kokkos` and `lightning.qubit` for Scipy-based VQLS algorithm to achieve the best performance with respect to time performance, extending the benchmark from 3 up to 15 qubits. We specifically implemented the pruned Pauli decomposition for the standard VQLS algorithm with the tolerance 0.01 to reduce the number of circuit execution pressure. From the Figure, the standard torch-based (NAdam) VQLS with Pauli decomposition requires the most time consumption and is the least scalable on time among all methods mentioned; its runtime grows so rapidly with system size that it becomes impractical well before reaching 15 qubits. The standard VQLS with Scipy-based optimizer (COBYLA) algorithm has<tbc>

\begin{tabular}{ccc}
**Method** & **KL Divergence** & **Entanglement Capability** \\
strong-entangle & 0.0062 & 0.8474 \\
opt-2 & 0.0167 & 0.7043 \\
global\_entanglement & 0.0168 & 0.6850 \\
hardware\_efficient & 0.0204 & 0.6047 \\
opt-c2 & 0.0225 & 0.6907 \\
opt-c1 & 0.2101 & 0.0000 \\
opt-mix & 0.2722 & 0.4717 \\
problem\_inspired & 0.4293 & 0.3656 \\
opt-c9 & 0.4318 & 1.0000 \\
opt-real-1 & 0.5602 & 0.3748 \\
basic & 0.6309 & 0.0000 \\
\end{tabular}

VQLS Learning Curve Comparison
0.5
Basic
Opt-2
Opt-C1
Opt-C2
0.4
Opt-C9
Strong Entanglement
Real Amplitudes
Hardware Efficient
0.3
Global Entanglement
Cost Value C(B)
Problem Inspired
Opt-Mix
0.2
0.1
0.0
0
20
40
60
80
100
Optimization Steps

VQLS Learning Curve Comparison
1.0
Strong Entanglement (COBYLA)
Strong Entanglement (L-BFGS-B)
Strong Entanglement (Nelder-Mead)
0.8
opt-real-1 (COBYLA)
opt-real-1 (L-BFGS-B)
opt-real-1 (Nelder-Mead)
Opt-Mix (COBYLA)
Opt-Mix (L-BFGS-B)
Opt-Mix (Nelder-Mead)
0.6
Cost Value C(B)
0.4
0.2
0.0
0
20
40
60
80
100
Optimization Steps

Fig. 9. Torch-based optimizer (NAdam) learning curve comparison of all quantum ansatz mentioned in Figure 2 using the 2D Hele-Shaw problem with _n<sub>x</sub>=n<sub>y</sub>_=4.

TABLE I

COMPARISON OF EXPRESSIBILITY (KL DIVERGENCE) AND ENTANGLEMENT CAPABILITY FOR VARIOUS QUANTUM ANSATZ (_N_=4_,L_=2).

Fig. 10. Learning curve of Scipy optimizer (COBYLA, L-BFGS-B, Nelder- Mead) performing minimization of quantum algorithms using three layers of quantum ansatz of ‘Strong Entanglement’, ‘Real Amplitudes’, and ‘ Opt-Mix’.


However, after a certain number of layers, the increasing number of layers does not benefit to the final cost and fidelity result.

For the reduced LCU terms tridiagonal Toeplitz mentioned in the Section IV-A implemented for the VQLS algorithm, it shows similar convergence speed and reaches a cost of \(1.5\times 10^{-6}\) with a fidelity of 0.99999 relative to the classical solution, demonstrating negligible loss in accuracy while reducing computing overhead through the pruning strategy.

## C. Optimizer selection

The choice of classical optimizer is crucial, particularly when navigating a complex loss landscape. Scipy-based methods such as COBYLA [34], [35] can be attractive because they typically require only one function evaluation per iteration, but they may struggle on highly nonconvex objectives. Gradient- based methods such as stochastic gradient descent and NAdam often traverse such landscapes more effectively, but typically require many more circuit evaluations per optimization step to calculate the gradient process.

The implementation results in circuits with _nb_ qubits, where _nb_ is the number of qubits required to represent the state vector, _N_=2_<sup>nb</sup>_, and the extra qubit is the ancilla. The depth of the circuit depends on the ansatz, and the number of circuit executions depends on the optimizer and how _A_ (and \(|b\rangle\)) are encoded. In our implementation of the LCU decomposition of _A_, for each function evaluation of the optimizer, there will be 2_L_<sup>2</sup>_nb_ circuit executions.

Given the validation of the implementation on simpler systems, we move on to solving the Hele-Shaw flow problem. Results of reconstructing the velocity field at distinct horizontal locations for a candidate flow setup with (_nx,ny_)=(4,4) grid points are shown in Fig. 8. The VQLS solution align with the classical solution well after the convergence with the final fidelity of 0.999438.

## D. Quantum ansatz

Selecting the right ansatz for fluid flow systems is challenging. Guidance can be deduced from the coefficients of the LCU decomposition of _A_. For both the LCU-based and tridiagonal Toeplitz systems, aside from having far fewer nonzero coefficients, the coefficients are purely real. Thus, the ansatz for these systems could benefit from gates operating predominantly on the real subspace. In contrast, the LCU decomposition of the Hele-Shaw _A_ yields both real and complex coefficients, potentially requiring higher expressibility to capture phase information.

Based on these deductions and guidance from [26], we analyze 11 quantum ansatz families in terms of expressibility by calculating KL divergence, circuit statistics, and efficiency, as shown in  I. We define the efficiency metric as the KL divergence multiplied by the number of CX gates, since two-qubit gates take significantly longer and are typically less accurate than single-qubit gates. From the table, the ‘hardware_efficient’ ansatz has the lowest KL divergence, meaning that it can generate the broadest set of states among the listed ansatz while using only six CX gates, yielding<tbc>

Convergence Analysis (15-Q Tridiagonal Toeplitz)
10-1
104
10-3
10-5
Number of LCU Terms
103
LCU Terms Relative Frobenius Norm Diff
10-7
102
10-9
101
10-11
10-1
10-3
10-5
10-7
10-9
10-11
Error Tolerance (E)

Cost and Fidelity vs. Layers (8-Qubit Sample Tridiagonal)
1.05
10-1
1.00
10-2
0.95
10-3
Cost (Log Scale)
Cost Fidelity
Fidelity
0.90
10-4
0.85
10-5
0.80
1
2
3
4
5
6
7
8
Number of Layers

Hele-Shaw Flow: Velocity Profile
1.000
0.667
Analytical Quantum Solution
y
0.333
0.000
X = 0.0
X = 0.3
X = 0.7
X = 1.0
0
0.5
1
U/Umax

Fig. 6. Number of Pauli LCU terms versus relative Frobenius-norm error.

Fig. 7. Effect of quantum ansatz layers on cost value and fidelity.

Fig. 8. Comparing velocity reconstruction for the Hele-Shaw flow with (_nx,ny_)=(4,4) grid points using VQLS algorithms.


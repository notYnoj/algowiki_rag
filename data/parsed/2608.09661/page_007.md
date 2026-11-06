truncation tolerance from 10<sup>-12</sup> to 10<sup>-2</sup>. Figure 6 reports the resulting runtime, memory usage, and approximation error measured by the relative Frobenius norm

The trade-off between fidelity and term count is controlled by discarding coefficients whose magnitude falls below the tolerance threshold. For a tolerance of 10<sup>-1</sup>, the decomposition requires only four Pauli terms and achieves a relative Frobenius error of 0.045, indicating substantial compression with limited loss in fidelity. As the tolerance decreases from 10<sup>-2</sup> to 10<sup>-4</sup>, the number of Pauli terms increases from 64 to 512 and 4096, and saturates at 10<sup>-5</sup> with 32768 terms, while the relative Frobenius error drops below 10<sup>-11</sup>. Reducing the number of LCU terms directly decreases the number of circuits executed by VQLS, thereby reducing per-iteration cost and improving overall convergence time.

Figure 6 illustrates the accuracy-cost trade-off of approximate decomposition: increasing the tolerance reduces the number of retained Pauli terms and therefore reduces runtime and memory, at the expense of a larger relative Frobenius-norm error.

## B. Validation

The validation of our LCU decomposition for a generalized _A_ matrix is computed using the tridiagonal Toeplitz matrix with a system size of \(2^8\times 2^8\). We use the NAdam optimizer. We used different layers of the quantum ansatz ‘opt-mix’ to perform the optimization to show the relationship between cost value and fidelity as shown in Fig. 7. The final cost value converges to \(9.6\times 10^{-6}\) with a minimum of 4 ansatz layers, and the fidelity exceeds 0.9999 with 4 or more layers, showing that the expressibility and convergence performance can increase by increasing the number of layers. The fidelity can reach to almost 1.00 when the cost value is below 10<sup>-3</sup>.

Complexity Comparison (LCU Terms)
Time Scaling Comparison
105
FWHT-based: Pressure
FWHT-based: Pressure
FWHT-based: Velocity
103
Naive: Pressure
Naive: Velocity
Naive: Velocity
PennyLane: Pressure
PennyLane: Pressure
PennyLane: Velocity
104
102
Number of LCU Terms
Decomposition Time (s)
103
101
102
100
101
10-1
101
102
101
102
Grid Points in the x and y Directions (nx = ny)
Grid Points in the x and y Directions (nx = ny)
Peak Memory Scaling Comparison
Average Memory Scaling Comparison
105
105
104
Average Memory (MB)
Peak Memory (MB)
103
103
FWHT-based: Pressure
FWHT-based: Pressure
FWHT-based: Velocity
Naive: Pressure
Naive: Pressure
Naive: Velocity
102
102
Nave: Velocity
PennyLane: Pressure
PennyLane: Pressure
PennyLane: Velocity
PennyLane: Velocity
101
102
101
102
Grid Points in the x and y Directions (nx = ny)
Grid Points in the x and y Directions (nx = ny)

\(\frac{\|A-B\|_F}{\|A\|_F}.\)

Fig. 5. Pauli decomposition performance for a canonical Hele-Shaw Jacobian using the naive approach, the PennyLane-integrated approach, and the FWHT approach.


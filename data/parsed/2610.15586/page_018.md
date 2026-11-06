<tbc>accurate than the selection by \(|\hat{b}|\). The residual-greedy selection remains more accurate than both.

## 6 Hardware validation on two platforms

We tested the method on two processors of different technology: the IonQ Forte-1 trapped-ion processor and the IBM superconducting processor `ibm\_cleveland`. We used the \(8\times 8\) grids (six data qubits) of the ellipse and the lens with \(\Gamma=100\) on both processors, and the \(16\times 16\) grids (eight data qubits) on the IBM processor. The six-qubit logical circuits are identical on the two platforms. At these sizes every quantity of Sec. 5 can be computed exactly. The measured outcome laws can therefore be compared with the ideal laws mode by mode. The experiment does not test asymptotic scaling, and it is not intended to show an advantage. With 1500 shots per case, which exceeds the dimension, the sampled sets cover 89 to 100% of the admissible basis. The experiments therefore test the outcome laws, the noise model, and the selection rule. They do not test the reduction of the subspace dimension, which is the purpose of sample-based methods.

### 6.1 Circuits and execution

We used three Krylov states for each duct, with \(T_k=k\Delta t\), _k_=0,1,2, and the geometric-mean step \(\Delta t=\pi/\sqrt{\lambda_{min}\lambda_{max}}\). For the ellipse the operator separates as \(A=A_\mu\otimes I+I\otimes A_\nu\), and the source _h_<sup>2</sup> has Schmidt rank two. Each circuit then consists of a short preparation of the two Schmidt coefficients and one unitary per register. The register unitary combines the Schmidt vectors of _b_, the evolution, and the transform to the cosine basis. The circuits are exact. They contain 38 or 39 logical two-qubit gates for six qubits, below the bound of 41 from generic three-qubit synthesis \[26\], and 191 for eight qubits. These register unitaries are computed from the classical diagonalization of one-dimensional operators. The ellipse circuits therefore test sampling, measurement, and reconstruction under real noise, not a scalable implementation of the time evolution.

For the lens we prepared the source exactly and used one symmetric Trotter step of the split evolution of Sec. 4.8 per circuit. A step consists of register unitaries built from the DST-I and \(e^{-i\Lambda\delta/2}\), and the diagonal phase \(e^{-i\Gamma h^2\delta}\) on all qubits. These circuits use no eigendecomposition of _A_, and all qubits are<tbc>

\begin{tabular}{ccc}
_p_ & no filter & parity filter \\
0 & \(58/8.0\times 10^{-3}\) & \(58/8.0\times 10^{-3}\) \\
0.05 & \(250/6.5\times 10^{-3}\) & \(95/6.5\times 10^{-3}\) \\
0.2 & \(650/5.2\times 10^{-3}\) & \(177/5.2\times 10^{-3}\) \\
0.5 & \(927/2.3\times 10^{-3}\) & \(236/2.3\times 10^{-3}\) \\
\end{tabular}

\begin{tabular}{ccccccc}
_N_ & _c_ & Krylov (|S| / error) & top-\(|\hat{b}|\) & top-\(|\hat{b}/\Lambda_0|\) & residual-greedy & \\
16 & 1 & \(37/1.2\times 10^{-2}\) & \(1.6\times 10^{-2}\) & \(1.0\times 10^{-2}\) & \(1.9\times 10^{-3}\) & \\
16 & 10 & \(93/1.1\times 10^{-6}\) & \(1.0\times 10^{-2}\) & \(9.7\times 10^{-3}\) & \(6.0\times 10^{-8}\) & \\
32 & 1 & \(64/1.5\times 10^{-2}\) & \(3.8\times 10^{-2}\) & \(3.8\times 10^{-2}\) & \(1.2\times 10^{-2}\) & \\
32 & 10 & \(90/1.1\times 10^{-3}\) & \(3.8\times 10^{-2}\) & \(3.5\times 10^{-3}\) & \(1.7\times 10^{-5}\) & \\
32 & 100 & \(192/9.8\times 10^{-4}\) & \(3.5\times 10^{-3}\) & \(1.6\times 10^{-3}\) & \(7.9\times 10^{-9}\) & \\
64 & 1 & \(110/3.8\times 10^{-2}\) & \(3.8\times 10^{-2}\) & \(3.8\times 10^{-2}\) & \(4.6\times 10^{-3}\) & \\
64 & 100 & \(218/1.6\times 10^{-3}\) & \(3.7\times 10^{-2}\) & \(5.3\times 10^{-4}\) & \(6.3\times 10^{-7}\) & \\
\end{tabular}

** 7:** Effect of sample contamination (lens, \(32\times 32\), \(\Gamma=100\), _M_=4800, mean of five runs). Entries are |S| / error.

** 8:** Ellipse, \(\Gamma=100\), _M_=19200: Krylov sampling with \(T_k=kc\pi/\lambda_{max}\) versus classical selections at the same |S|. Entries are relative energy-norm errors.


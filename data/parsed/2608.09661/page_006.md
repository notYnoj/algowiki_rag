<tbc>built-in function of the Pennylane package, where it encodes

\(U(A)=\left[\begin{array}{ c c }
A & \sqrt{I-AA^\dagger} \\
\sqrt{I-A^\dagger} A & -A^\dagger
\end{array}\right].\) (14)

directly by assigning the input matrix and the corresponding qubits. We also implement block encoding through LCU decomposition. This approach realizes the target operator by interleaving a Select oracle between a Prepare oracle and its adjoint. The schematic is demonstrated in Fig. 4. However, when physically implement this algorithm, the Pennylane software package does not provide gradient calculation for such encoding method, and the encoding method requires similar resource to the block encoding of the SVD decomposition, where the SVD decomposition-based block encoding requires as well. Therefore, we will not include this method in Section IV \[32\].

### F. Experimental setup

We implemented the VQLS algorithm with a single computing node on the Frontier supercomputer using PennyLane \[33\] (version 0.38.0) with a PyTorch backend (Torch version 2.5.0) for gradient-based optimization. We use the SciPy package (version 1.15.3) for Scipy-based optimization. We used the HPC-enabled quantum simulator `Lightning.kokkos` to gain acceleration on Frontier HPC system.

In the current work, we evaluate the implementation using three different problems based on their complexity: (1) a system comprised of LCU for _A_, similar to that evaluated in \[18\], (2) a tridiagonal Toeplitz system, and (3) a canonical fluid flow problem. Following the analysis in \[23\], we choose the fluid flow problem as the two-dimensional Hele-Shaw flow, which is an inviscid steady flow resulting in the simplification of the Navier-Stokes equations to a system of coupled linear partial differential equations.

## IV. RESULTS

We evaluate the LCU decomposition routine and several variants of the VQLS algorithm introduced in Section III. To enable a fair comparison, we report wall-clock time, average memory usage, and peak memory usage for each method. For cVQLS, we use two compute nodes to assess scalability with the `Lightning.kokkos` simulator.

### A. LCU decomposition

We first benchmark three LCU decomposition strategies: (1) a naive construction, (2) the PennyLane-integrated LCU decomposition, and (3) a Fast Walsh-Hadamard transform (FWHT) approach with CPU-core parallelization. Figure 5 summarizes results for tridiagonal Toeplitz matrices and a canonical Hele-Shaw Jacobian with increasing grid dimensions _n<sub>x</sub>_ and _n<sub>y</sub>_. The naive approach supports up to _n<sub>x</sub>=n<sub>y</sub>_=11 and consistently yields the fewest Pauli terms, while the other methods typically require slightly more terms. In addition, when the grid dimension is a power of two (_n<sub>x</sub>=n<sub>y</sub>_=2_<sup>k</sup>_ for _k_=2,3,4_,..._), the number of Pauli terms is minimized and scales approximately linearly with grid resolution; non-power-of-two sizes require padding to embed the matrix into a circuit, increasing the term count.

In terms of runtime, the naive and PennyLane-integrated methods are comparable for small problems (\(n_x=n_y\in\{3,4\}\)) and are faster than the multi-threaded FWHT approach. As the problem size increases, however, the naive method fails to scale beyond _n<sub>x</sub>=n<sub>y</sub>_=11, making it the least scalable option. The PennyLane-integrated method scales better, but requires more than 2000 s to generate a case with _n<sub>x</sub>=n<sub>y</sub>_=64 and does not complete _n<sub>x</sub>=n<sub>y</sub>_=128 within a 2 h time limit. The FWHT-based decomposition is the most scalable approach, requiring less than 2000 s for _n<sub>x</sub>=n<sub>y</sub>_=256. For both peak and average memory, the FWHT-based method outperforms the other approaches across all tested cases, achieving up to a \(1298\times\) reduction at _n<sub>x</sub>=n<sub>y</sub>_=11 relative to the naive method. The PennyLane- integrated approach uses approximately \(5\times\) more memory than FWHT across problem sizes. Across these metrics, the FWHT method provides the best overall scalability, while the naive and PennyLane-integrated methods can be competitive only for the smallest grid sizes.

The proposed parallelized Pauli decomposition also supports an approximate mode, enabling fewer LCU terms and faster decomposition. We apply this approximate decomposition to a tridiagonal Toeplitz matrix of size \(2^{15}\times 2^{15}\) and sweep the<tbc>

10)
10)
U(A)
10)
V(w)
10)

10)
U1
U2
Um-1
Um
1A)
10)
10)
10)
Prep
Prep
10)

Fig. 3. Schematic representation of the Variational Quantum Linear Solver (VQLS) utilizing a Block Encoding strategy. The circuit replaces the standard Linear Combination of Unitaries (LCU) decomposition with a block-encoded unitary _U<sub>A</sub>_ acting on the ancillary and system registers, coupled with the variational ansatz \(V(\theta)\).

Fig. 4. Circuit diagram for block encoding via LCU decomposition. The process consists of three stages: the state preparation unitary _Prep_ (acting on the ancilla), the selection operator _U_<sub>1</sub>_,U_<sub>2</sub>_...U_<sub>_m_-1</sub>_,U<sub>m</sub>_ (controlled by the ancilla), and the adjoint state preparation _Prep_<sup>†</sup>. The qubits that encode the selection operator contain the encoded original matrix _A_.


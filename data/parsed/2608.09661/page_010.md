better scaling performance compared with the torch-based algorithm.

After the implementation of the SVD-based decomposition, the number of circuits required per iteration is reduced dramatically compared with the Pauli decomposition, yielding better scalability and over a 10,000× time reduction on an 8-qubit tridiagonal Toeplitz matrix, with the advantage widening further at larger system sizes up to 15 qubits. For the coherent VQLS that only requires one circuit to calculate the cost value, it has better timing performance compared with the standard VQLS with Pauli decomposition. However, the slope increases as the number of qubits increases because the number of qubits required for the state preparation and encoding circuits grows dramatically during execution, leading to inefficiency for large-qubit simulation. For the coherent VQLS using SVD- based block encoding, it has the best performance among all mentioned VQLS variants with the minimum time consumption requirement. However, the slope increases dramatically as the SVD decomposed unitary matrix encoding requires large amount of memory, leading to ‘out-of-memory’ error for GPU simulation. The coherent VQLS with Pauli encoding achieved lowest slope among all approaches, and can simulate up to 15- qubits linear systems problem within the 2-hours wall time.

## V. CONCLUDING REMARKS AND FUTURE DIRECTIONS

We presented an end-to-end study of the Variational Quantum Linear Solver (VQLS) for CFD-relevant linear systems on a hybrid quantum–HPC stack. The work was organized around the three challenges identified in the introduction-- matrix encoding cost, ansatz selection, and HPC deployment-- and we summarize our findings along the same axes.

**Matrix encoding.** On the tridiagonal Toeplitz system and the two-dimensional Hele–Shaw flow, the FWHT-based parallel Pauli decomposition reduces peak memory by up to 1298× over the naive LCU on an 11×11 grid while attaining O(_n_<sup>2</sup>log_n_) scaling. The SVD-based two-term LCU minimizes the number of LCU terms (two) and qubit count required<tbc>

<tbc>for the encoded circuit, yielding more than 10,000× per- iteration speedup over standard Pauli-based VQLS at 8 qubits and the best per-iteration timing among the four strategies we tested. Each approach has a distinct failure mode: Pauli-based encodings still produce many non-zero terms in the worst case (up to the number of matrix entries), the coherent variant additionally requires deep block-encoding circuits and non- trivial state preparation, and the SVD pre-processing itself carries a non-negligible classical overhead. No single encoding dominated across problem sizes, which motivates continued exploration of compressed and structure-aware encodings.

**Ansatz and optimizer.** Across 11 ansatz families on Hele– Shaw flow and sample-tridiagonal Toeplitz matrix, we found that expressibility and entanglement metrics correlate only weakly with VQLS convergence, so off-the-shelf circuit metrics are not a reliable proxy for solver quality. Among classical optimizers, gradient-based methods incurred a higher per- iteration cost than gradient-free alternatives but converged more reliably in the HPC setting we tested. Together, these observations argue for problem-aware ansatz design rather than ansatz selection by generic expressibility scores.

**HPC deployment.** We deployed the end-to-end workflow on the OLCF Frontier supercomputer and successfully simulated a 15-qubit tridiagonal Toeplitz system on a single node, demonstrating a increasing performance with proposed optimization algorithms.

Our ongoing work extends the analysis to higher-complexity CFD problems, real quantum-hardware execution alongside the HPC simulator, problem-aware and physics-informed ansatz construction, and additional matrix-encoding strategies aimed at further reducing LCU term count and circuit depth. We see these as the immediate steps toward a deployable hybrid quantum–HPC linear-solver stack for fluid dynamics.

## VI. ACKNOWLEDGMENTS

The authors would like to thank Pooja Rao for her valuable contributions and insightful discussions that helped shape this work.

This research used resources of the Oak Ridge Leadership Computing Facility at the Oak Ridge National Laboratory, which is supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC05-00OR22725.

## VII. ACKNOWLEDGEMENT OF AI-GENERATED CONTENT

Portions of this manuscript were prepared with the assistance of large language model (LLM) tools, which were used to support drafting, editing, grammar refinement, and stylistic improvements of the text. All AI-generated content was reviewed, verified, and edited by the authors, who take full responsibility for the content in this work. No AI tools were used to generate or fabricate experimental data, numerical results, figures, or citations; all references were independently verified by the authors.

VQLS Time Consumption per Iteration vs. System Size
Pauli Gradient-Based
Pauli Gradient-Free
104
SVD Gradient-Based
Pauli Coherent Gradient-Based
SVD Coherent Gradient-Based
103
Time per Iteration (seconds)
102
101
100
10-1
3
4
5
6
7
8
9
10
11
12
13
14
15
Number of Qubits

Fig. 11. Time consumption scaling per iteration of standard and coherent VQLS with Torch-based and Scipy-free optimizers from 3 to 15 qubits, using both Pauli and SVD decomposition approaches.


<tbc>trainability and expressibility. To quantify the ability of a parameterized quantum circuit (PQC) to uniformly explore the available Hilbert space, we compute its expressibility (_E_) using the statistical framework proposed by Sim et al. \[26\]. This metric measures the deviation of the ansatz’s sampling distribution from the Haar-uniform distribution over pure quantum states in a 2_<sup>n</sup>_-dimensional Hilbert space. Specifically, we generate an empirical probability distribution \(\hat{P}_\mathrm{PQC}(F)\) of fidelities<tbc>

\(F=\left|\langle\psi(\theta)|\psi(\phi)\rangle\right|^2,\) (11)

<tbc>obtained by sampling pairs of parameterized states using independently and uniformly drawn parameters \(\theta\) and \(\phi\). This empirical distribution is compared against the analytical fidelity distribution for Haar-random pure states,<tbc>

\(P_\mathrm{Haar}(F)=(D-1)(1-F)^{D-2},\) (12)

<tbc>where _D_=2_<sup>n</sup>_ is the Hilbert space dimension. The expressibility is defined as the Kullback–Leibler (KL) divergence between the binned empirical distribution and the corresponding Haar distribution,

\(E=D_\mathrm{KL}\big(\hat{P}_\mathrm{PQC}\|P_\mathrm{Haar}\big)=\sum_i\hat{P}_\mathrm{PQC}(F_i)\mathrm{ln}\big(\frac{\hat{P}_\mathrm{PQC}(F_i)}{P_\mathrm{Haar}(F_i)}\big)\) (13)

A lower value of _E_ indicates that the circuit-generated states more closely approximate uniform sampling of the Hilbert space and therefore exhibit higher expressibility. Additionally, we define a normalized relative expressibility score by rescaling _E_ with respect to the Hilbert space dimension<tbc>

<tbc>and binning resolution, such that higher values correspond to greater expressibility. Figure 2 provides several common quantum ansatz that we analyze in this work.

Another critical metric for a quantum ansatz is its entanglement capability, which quantifies the circuit’s ability to generate entangled states. This value is determined by sampling a large set of circuit parameters from a uniform distribution and calculating the mean Meyer-Wallach measure across the resulting states \[26\]. A higher entanglement capability indicates superior performance, enabling the ansatz to access a broader range of quantum states during computation.

## E. Coherent Variational Quantum Linear Solver (cVQLS) and Block encoding

Another version of the quantum linear solver is to encode matrix _A_ into a single quantum circuit, which generates a larger circuit containing the encoded matrix _A_, the quantum ansatz, and the prepared state vector \(|b\rangle\) \[27\]. Similar to VQLS, CVQLS prepares the quantum ansatz _V(w_) such that \(V(w)\cdot|0\rangle=|x\rangle\) and minimizes \(1-U(A)|V(w)\rangle\cdot|b\rangle^\dagger\) by changing parameters _w_. The vector \(|x\rangle\) can then be reconstructed by computing _V(w_min). The circuit diagram is shown in Figure 3. To encode matrix _A_ into a single quantum circuit, it requires a block-encoding technique to initialize a larger unitary matrix \(A=\left[\begin{array}{ c }
A* \\
*
\end{array}\right]\), where the normalized matrix _A_ is a block of a larger matrix; this technique is called block encoding \[28\]-\[31\]. There exist several approaches to perform block encoding. The most straightforward approach is the<tbc>


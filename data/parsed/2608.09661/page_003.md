The goal is to optimize \(|\tilde{x}\rangle\) to maximize the overlap between \(|b\rangle\) and \(|\tilde{b}\rangle\), given by the objective function<tbc>

\(C=1-\left|\langle b|\tilde{b}\rangle\right|^2.\) (2)

<tbc>The state \(|\tilde{x}\rangle\) is represented by a variational quantum circuit _V_ using a finite number of classical real parameters _w_, given by

\(|\tilde{x}\rangle=V(w)|0\rangle.\) (3)

The parameters _w_ are optimized using a classical approach to minimize _C_. Further details of the cost function and different routes to approach the problem setup are elaborated in the original VQLS work \[18\]. The key components of the methodology that this work will focus on are: (1) the representation of the _A_ matrix, (2) the nature of the variational circuit or ansatz, and (3) the choice of the classical optimizer. The overall schematic of the VQLS algorithm is demonstrated in Figure 1.

## B. Matrix preparation using linear combination of unitaries

For the VQLS algorithm to be applicable, the _A_ matrix (and \(|b\rangle\)) should be encoded efficiently. One approach is to represent or decompose _A_ into a linear combination of unitaries (LCU), like the combination of Pauli operators

\(A=\sum_{l=1}^Lc_l\sigma_l.\) (4)

Given any _A_, in our implementation we find coefficients of all possible combinations of I and Pauli _X_, _Y_ , and _Z_ operators for the given basis dimension of the system as the trace inner<tbc>

<tbc>product of each operator combination with _A_, normalized by the number of combinations. As we will see for the fluid flow problem, this creates challenges.

The number of LCU terms increases as the dimension of the matrix increases. In the worst-case scenario, a randomized dense square matrix with dimension 2_<sup>k</sup>_ requires 4_<sup>k</sup>_ LCU terms after decomposition, leading to inefficiency and poor scalability. Moreover, finding the Pauli terms and their coefficients is computationally heavy if not optimized. In the brute-force approach, one iterates over the full Pauli-string basis to calculate all coefficients, then drops the terms whose magnitude is below a threshold. The advantage of this method is that the input only needs to be a square matrix of dimension \(2^k\times 2^k\). The detailed algorithm pseudocode is shown in Alg. 1. Despite being easy to implement and requiring no special properties of the input matrix (Hermitian or unitary), this approach enumerates all Pauli strings and thus incurs excessive memory and computation overhead.

We adopt a memory- and compute-efficient approach proposed by Georges et al. \[25\], where the LCU decomposition only needs enough memory to store the input matrix and the computation of the Pauli terms uses fixed auxiliary memory, independent of matrix size. The improved algorithm leverages the Walsh-Hadamard transform and requires the input matrix to be Hermitian (_A=A_<sup>†</sup>). The basic idea is to use the Fast Walsh-Hadamard Transform (FWHT). The Pauli terms {_I,X,Y,Z_} are indexed by two binary indices _r,s_ using _P(r<sub>j</sub>,s<sub>j</sub>_)=_i<sup>r<sub>j</sub>s<sub>j</sub>X<sup>r<sub>j</sub></sup>Z<sup>s<sub>j</sub></sup>_. With this indexing, (_r<sub>j</sub>,s<sub>j</sub>_)=(0,0),(1,0),(0,1),(1,1) correspond respectively to _I,X,Z,Y_ on qubit _j_. Then, the coefficients are calculated by:

Initialize a set of weights
H
RZ if 'imag'
H
cost
Prepare a set of weights
Controlled Pauli strings
Controlled Pauli strings
Input vector b
Input vector b
Initialize A with Linear Unitary Combinations
V(w)
Clo1
Clo1
Update weights
A =
L
L
l=1
Iterate and add up all possible combination of Clo1 and Clo1
Variational Ansatz
Perform and measure results of the quantum ansatz circuits with optimized weights
Yes
No
if stop point reached

Fig. 1. VQLS workflow combining quantum circuit components with classical optimization steps to approximate the solution to _A_|_x_〉=|_b_〉. The algorithm iterates the quantum circuits by updating the weights to minimize the overall cost. Once optimization converges, the measurement of the Variational ansatz reveals the solution state |_x_〉.


Here’s how the process unfolds:

1) Initialize each ancillary qubit to the excited state \(|1\rangle\).<tbc>

2) The diagonal checks are executed using Toffoli gates, with each diagonal check corresponding to one Toffoli gate. For every pair of rows, select the relevant ancillary qubit associated with that pair.<tbc>

3) For each pair of rows, identify the pairs of qubits situated diagonally from the chosen rows. Apply a Toffoli gate to the ancillary qubit which represents the corresponding diagonal which is being checked, controlled by these two pairs of diagonal qubits. Repeat this procedure for all pairs of diagonal qubits stemming from the selected rows.<tbc>

4) Iterate through every pair of rows, performing the same Toffoli gate operation on the corresponding ancillary qubit representing the current diagonal under check. If any diagonally placed pair of qubits is excited, it will transition the related ancillary qubit back to the ground state \(|0\rangle\).

Following these operations, if all the ancillary qubits designated for diagonal criteria remain in the excited state \(|1\rangle\), then the states that meet this condition are the ones that satisfy the diagonal criteria. In summary, if both the (_N_-1) ancillary qubits for column criteria and the \(\frac{N(N-1)}{2}\) ancillary qubits for diagonal criteria remain in the excited state \(|1\rangle\), the resulting states--excluding the ancillary qubits themselves represent the solutions to the _N_-Queens problem. These states signify the valid positions for placing _N_ queens on an \(N\times N\) chessboard, ensuring that no two queens threaten each other.

## IV. IMPROVEMENTS TO THE PREVIOUS SOLUTION

In this work we have improved upon the complexity of the existing algorithm by including efficient preparation of _W<sub>N</sub>_- states and introducing the use of dynamic circuits.

### A. Generalized _W<sub>N</sub>_ States

The concept of using _W<sub>N</sub>_ states to initialize a quantum circuit in order to satisfy the column criteria was previously introduced. This was exemplified with a \(4\times 4\) chessboard, which necessitates the creation of a 4-qubit _W_-state, a relatively straightforward task. However, the methods employed for preparing 4-qubit _W_-states are not easily adaptable for generating _W_-states for varying numbers of qubits. Subsequently, it was realized that creating _W_-states for 2_K_ qubits, where _K_ is a whole number, is comparatively simpler than devising methods for arbitrary whole numbers. As a solution, a more comprehensive approach was discovered in Cruz’s work \[22\], detailing a generalized method for preparing _N_-qubit _W_-states, where _N_ can be any whole number. To make the algorithm more practical and extensible, the aforementioned method for generating _W_-states for any number of qubits was integrated. Furthermore, there was an advancement in the process of filtering states that satisfy both row and column criteria. In the previous paper, this involved transitioning the ancillary qubits from the _Z_-axis to align with the _X_-axis, then executing controlled phase flip operations on these ancillary<tbc>

<tbc>qubits, controlled by the qubits of the corresponding column. The ancillary qubits would then be switched back to the _Z_-axis configuration. This improvement in the approach to satisfying the column criteria refined the algorithm and enhanced its practical applicability.

### B. Removing the Phase operation from the Column criteria

An alternative approach involves using a controlled bit flip gate instead of a controlled phase flip gate. This change eliminates the need to switch between the _Y_ -axis and _Z_- axis configurations. This alteration decreases the number of gates by 2 for each ancillary qubit dedicated to column criteria. Additionally, the controlled bit flip gate is simpler to implement and offers improved noise reduction in real quantum computers. In the Qiskit framework, we implemented a controlled bit flip gate using the CX-gate (CNOT gate), and a controlled phase flip gate using the CZ-gate.

### C. Introducing Dynamic Circuits

When the previous paper was proposed, dynamic circuit features were not yet introduced in any of the quantum simulation frameworks. However, today, almost every quantum computing simulation framework supports dynamic circuits. They offer a powerful way to leverage quantum computing capabilities for various applications, allowing exploration of quantum states and behaviors that might not be achievable using static circuits. However, working with dynamic circuits does present challenges, including efficient parameter optimization and managing complexity as circuits become more adaptive.  II presents a summary of the introduction years and versions for various quantum computing frameworks that support dynamic circuits:

Here, we have utilized dynamic circuits in a more clever manner. We’ve designed the circuits such that only those states which satisfy the column criteria proceed to construct<tbc>

\begin{tabular}{ccc}
**Framework** & **Year Introduced** & **Version** \\ Qiskit & 2020 & 0.23.0 \\ OpenQASM & 2021 & 3.0.0 \\ Cirq & 2021 & 1.9.0 \\ \end{tabular}

1)
10)
a 3
6
10)
a 1
3
10)
a 2
9
10)
a 2
1
2
10)
a 1
2

Fig. 3. Logarithmic Complexity Circuit for \(|W_6\rangle\). The following circuit design was referred from the article \[22\]

TABLE II

QISKIT VERSIONS FOR DYNAMIC CIRCUITS


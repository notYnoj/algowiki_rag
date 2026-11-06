chessboard, there’s a possibility of having 2<sup>_N_<sup>2</sup></sup> combinations for _N_ queen placements.

\(|00..0\rangle-\rightarrow^{H^{\otimes N^2}}\frac{1}{\sqrt{2^{N^2}}}\sum_{x=0}^{2^{N^2}-1}|x\rangle\) (1)

Let us introduce a condition: on an \(N\times N\) chessboard, we aim to place exactly _N_ queens. With this requirement in mind, the search scope narrows down to a combinatorial challenge with \(\genfrac(){pt}{2}{N\times N}{N}\) potential combinations. In a clever approach, the authors have devised a method to configure the quantum circuit, allowing the outcomes of measurements to span all the potential combinations within the search domain, satisfying the condition of rows without conflicts. For each group of _N_ qubits, representing a single row on the chessboard, the authors have introduced the concept of implementing what they refer to as an _N_-Qubit W-State, represented in Eq. (2).

\(|W_N\rangle=\frac{1}{\sqrt{N}}(|100\dots 0\rangle+|010\dots 0\rangle+\cdots+|000\dots 1\rangle)\) (2)

\(|R\rangle=|W_N\rangle=\frac{1}{\sqrt{N}}\left[|1\rangle+|2\rangle+\dots\dots|N\rangle\right]=\frac{1}{\sqrt{N}}\sum_{i=1}^N|x_i\rangle\) (3)

where \(|x\rangle\in|100\dots 0\rangle\) to |000_..._1〉. Here, each vector \(|x_i\rangle\) (\(i\in\{1,2,\dots N\}\)) represents all possible configurations of a particular row. When this process is applied to every row on the chessboard, it effectively ensures that the arrangement adheres to the row criterion without any conflicts. Taking \(|R_j\rangle\) as the state representing the _j_th row configurations, the tensor product of N of these states, represented as \(|\Psi_R\rangle\) is as follows:

\(|\Psi_R\rangle=|R_1\rangle\otimes|R_2\rangle\otimes\dots|R_N\rangle\) (4)

where \(|\Psi_R\rangle\) represents all the possible combinations of _N_<sup>2</sup> qubit vectors, each of which fulfills the **Row criterion**. This reduces the subspace, taking it from the general subspace of 2<sup>_N_<sup>2</sup></sup> to _N<sup>N</sup>_. However, it’s essential to note that the reference paper [21] doesn’t provide a precise step-by-step procedure for generating a W-State. Instead, the authors illustrate the algorithm using a \(4\times 4\) chessboard as an example. In this particular case, they employ a specialized technique to craft a W-State tailored to 4 qubits. It’s crucial to understand that this technique cannot be universally extended to accommodate any arbitrary number of qubits. Despite this limitation, the algorithm retains its appeal due to its unique ability to set up the quantum circuit directly in a way that ensures the row criteria are met without the need for complicated post- processing.

## B. Solving Column Criteria

After successfully getting all the configurations of placing _N_ queens in \(N\times N\) chessboard stored in \(\Psi_R\) that fulfills the row criteria, our exploration is now limited to _N<sup>N</sup>_ combinations. To handle and enhance the column criteria, a group of (_N_-1) ancillary qubits is introduced. These qubits act as indicators, signaling that if all these ancillary qubits are in<tbc>

<tbc>the excited state \(|1\rangle\), the specific combination adheres to the column criterion. Let’s point out the process step by step:

1) Apply a Hadamard (_H_) gate to each ancillary qubit. This transforms the ancillary qubits from their original _Z_- basis to the _X_-basis.

2) Consider qubit _q<sub>i,j</sub>_ which represents the quantum state \(|0\rangle\) or \(|1\rangle\) belonging to the _i_-th row and _j_-th column. For each _j_-th qubit present in all the rows, apply a controlled phase (_CP_) gate controlled by the _j_-th qubit and applied to _j_-th ancillary qubit. Repeat this process iteratively until _j_ reaches (_N_-1), excluding the last qubit of every row. This process is depicted in Figure 2.

3) It’s implicit that if every one of the (_N_-1) columns contains just a single qubit in the excited state \(|1\rangle\), the ultimate qubit naturally resides in the last column.

4) Implement another Hadamard (_H_) gate operation on all the ancillary qubits. The outcome of this step ensures that if a column contains multiple qubits in the excited state \(|1\rangle\) or none at all, the associated ancillary qubit remains in the ground state \(|0\rangle\).

It does not matter if there are multiple qubits in the same column because only if all the ancillary qubits are in the excited state \(|1\rangle\), the column criteria is fulfilled. In effect, only when both the row and column criteria are met, all the ancillary qubits transition to the excited state \(|1\rangle\). This signifies the fulfillment of the required conditions. In this manner, the quantum circuit proficiently examines the interplay between the row and column criteria, pinpointing valid combinations that satisfy both sets of requirements and efficiently navigating the complex constraints of the _N_-Queens problem.

## C. Solving Diagonal Criteria

After successfully fulfilling both the row and column criteria, our search space is further narrowed down to _N_! distinct states. For an \(N\times N\) chessboard, the process involves using (_N_-1) ancillary qubits to verify column criteria and \(\frac{N(N-1)}{2}\) ancillary qubits for diagonal criteria. The central concept here revolves around scrutinizing every possible pair of rows to identify the presence of excited qubits diagonally. We need to include only \(\frac{N(N-1)}{2}\) ancillary qubits, because there are fewer number of diagonal checks required as the row and column criteria are already satisfied.


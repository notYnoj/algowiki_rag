the gates needed to check the diagonal criteria. As a result, only _N_! states are used to build the circuit for verifying the diagonal criteria. All other states lead to the result \(|0\rangle\), since no measurement is performed for those trivial states. By incorporating dynamic circuits, we significantly reduce both the time required and the complexity of the gates. This reduction stems from the elimination of time and operations spent on trivial states. This addition serves as a substantial improvement by effectively harnessing the advantages of dynamic circuits.

## V. NOVEL ALGORITHMS

We have introduced two new and innovative algorithms for solving the N-Queens problem. They employ the same representation as introduced in the previous paper. We have provided comprehensive explanations for both of these algorithms in the following sections, along with relevant illustrations and examples. Sections V-A and V-B delve into the details of these novel algorithms, showcasing their unique approaches to addressing the N-Queens problem.

### A. Direct Column Algorithm

**Algorithm 1** DIRECT COLUMN ALGORITHM

1) **Initialization of First Row:**

a) Begin by creating an N-Qubit W-State for all qubits in the first row.

2) **Iterative Entanglement:**

a) For each qubit in the first row (_i_-th qubit):

i) Create a controlled W-State on the second row, excluding the _i_-th qubit in the second row.

ii) The control is based on the _i_-th qubit of the first row.

iii) Similarly, for each qubit (_j_-th qubit) entangled by the W-State in the second row:

A) Create a W-State on the third row, except for the _i_-th and _j_-th qubits.

B) The control is based on the _i_-th qubit of the first row and the _j_-th qubit of the second row.

iv) Continue this pattern iteratively, propagating through each row until the last row.

v) Final Row Operation:

A) For the last row (with only one qubit remaining):

B) Perform a Toffoli gate on that qubit, controlling it with all qubits from each row that were not included in W-States in subsequent rows.

This quantum algorithm addresses both the row criteria and column criteria concurrently. It starts by configuring the quantum circuit with combinations that satisfy both these conditions. This strategic initialization results in a substantial decrease in the search space, ultimately reaching _N_! combinations. Remarkably, this significant reduction is achieved<tbc>

<tbc>without the requirement for additional ancillary qubits to verify the column conditions, a necessity in previous algorithms. Following this accomplishment, the next step entails applying the same procedure for assessing the diagonal criteria, involving the utilization of ancillary qubits to check diagonals with the implementation of dynamic circuits to give only the possible configuration states. However, it’s important to note an important drawback associated with this approach: as the number of input queens increases, the complexity of the quantum circuit grows exponentially. This expansion in complexity is directly linked to the quantity of input queens and can pose challenges in terms of scalability and implementation. While this approach provides a remarkable reduction in the search space and simplifies the solution process by not requiring ancillary qubits for column checks, the trade-off lies in the exponential growth of circuit complexity. This algorithm shines for smaller instances of the N-Queens problem, but its feasibility diminishes as the problem size increases due to the rapidly escalating quantum circuit complexity.


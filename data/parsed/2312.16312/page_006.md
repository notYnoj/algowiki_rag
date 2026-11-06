**Algorithm 2** QUANTUM BACKTRACKING ALGORITHM

1) **Initialization of First Row:**

a) Begin by creating an N-Qubit W-State for all qubits in the first row.

2) **Iteration for Every Qubit in First Row:**

a) **Iteration over Rows:** For each qubit (i) in the first row:

i) **Disregard Certain Qubits:** Disregard qubits (i) in successive rows and those on the same diagonal as qubit (i) of the first row.

b) **Create Controlled W-State:** For remaining qubits in the next row:

i) Create an N-Qubit W-State controlled by qubit (i) from the first row.

c) **Iteration for Selected Qubits:** For qubits (j) in the second row on which W-State was applied:

i) **Disregard Certain Qubits:** Disregard qubits (i) and (j) in successive rows and those on the same diagonals.

d) **Create Controlled W-State:** For remaining qubits in the next row:

i) Create an N-Qubit W-State controlled by qubits (i) and (j) from the first and second rows, respectively.

e) **Repeat Iteration:** Continue iterating in a similar manner through each row until the last row.

f) **Final Row Operation:** For the last row (with only one qubit remaining):

i) Apply a Toffoli gate on that qubit, controlling it with qubits from previous rows that weren’t disregarded.

3) **Holding Solutions**

a) For every qubit in last row, entangle them with ancillary qubit using the Controlled-NOT gate (C- NOT) with target being the ancillary qubit

The inspiration from the well-known classical backtracking algorithm is evident in the naming of this algorithm. This quantum version closely emulates the principles of the back- tracking algorithm but within the context of a quantum circuit.

However, the results obtained here encompass not just a set of solutions but also non-solution states. Filtering these non- solution states requires only a single ancillary qubit. If this ancillary qubit is in the excited state \(|1\rangle\), the corresponding combination is included in the solution set. If progression to the subsequent row becomes impossible due to disregarding all qubits, the algorithm employs backtracking by returning to a qubit in the same row that was previously considered and involved in creating a collective W-State. The potential solution combinations are those wherein a Toffoli gate can activate a qubit from the last row. To validate this, a single<tbc>

<tbc>ancillary qubit is utilized, and _N_ controlled-NOT gates are applied. Each gate is controlled by a qubit from the last row. To manage the arrangement of gates, both a classical stack and a quantum stack are required. The use of classical computing resources becomes necessary for this computational aspect.

## VI. CONCLUSION

In conclusion we have demonstrated the mapping of an N- Queens problem into a quantum computer. Improvement is done based on previous works by defining the exact structure of the state preparation circuit of W-state and the inclusion of dynamic circuits to further reduce circuit complexity. Only valid solution states are measured, while other trivial states are cancelled out by the dynamic circuit. Two novel algorithms are presented that are inspired from the present work, one being the controlled W-state and the other one based on existing techniques like the backtracking algorithm which introduces a novel approach that holds value beyond its immediate application. Although it incorporates classical computational elements, it underscores the potential to use quantum algorithms to solve the N-Queens problem. Hence future work on showing decreased time complexity for this problem using qubit-mapping is a justified prediction. Overall, this algorithm delineates a distinctive approach influenced by classical backtracking techniques, forming a bridge between classical and quantum computing realms which will pave way for the development of more efficient ways to solve the N-Queens, hence offering valuable insights for further exploration in this dynamic field.

## REFERENCES

[1] J. G. Brookshear, _Computer science: An overview_. Benjamin-Cummings Publishing Co., Inc., 1991.

[2] C. Erbas, S. Sarkeshik, and M. M. Tanik, "Different perspectives of the n-queens problem," in _Proceedings of the 1992 ACM annual conference on communications_, pp. 99-108, 1992.

[3] J. Bell and B. Stevens, "A survey of known results and research areas for n-queens," _Discrete mathematics_, vol. 309, no. 1, pp. 1-31, 2009.

[4] E. Pauls, "Das maximalproblem der damen auf dem schachbrete," _Deutsche Schachzeitung_, vol. 29, pp. 261-263, 1874.

[5] J. R. Bitner and E. M. Reingold, "Backtrack programming techniques," _Communications of the ACM_, vol. 18, no. 11, pp. 651-656, 1975.

[6] R. Sosic and J. Gu, "Efficient local search with conflict minimization: A case study of the n-queens problem," _IEEE Transactions on Knowledge and Data Engineering_, vol. 6, no. 5, pp. 661-668, 1994.

[7] H. S. Stone and J. M. Stone, "Efficient search techniques--an empirical study of the n-queens problem," _IBM Journal of Research and Development_, vol. 31, no. 4, pp. 464-474, 1987.

|R1) W
W
W
W
W
|R2)
|R3)
+
+
+

Fig. 4. Example of Direct Column Algorithm using 3 \(\times\) 3 chessboard. This depicts the steps of 2a.(i) and (ii) in Algorithm V-A


In most QUBO solvers, including all of the ones we consider here, the solver actually minimises the loss function or Hamiltonian, so in our implementation we implement the negative of the above functions. We implement these methods on leading quantum platforms such as D-Wave and Qiskit for IBMQ in order to validate our formulations and evaluate their performance. We use the constructed solvers on small instances of real SARS-CoV-2 genomes.

A crucial factor for demonstrating quantum advantage is the ability to scale up to larger instances, beyond what classical approaches could handle. Luckily, the qubit usage scales 1-to-1 with the number of vertices in the reduced graph. For the QAOA approach, we also need to consider the depth and the gate count, which also scales approximately linearly with the size of the reduced graph:

An important aspect of the problem to keep in mind is the requirement to find **all** of the MWCs within the graph. Measuring the QAOA circuit in the computational basis yields a single bitstring that represents a subgraph. Therefore, we approach this enumeration by repeatedly measuring executions of the same circuit. This is a well-established protocol in<tbc>

400
300
Number of Qubits
200
100
0
100
200
300
400
500
600
700
800
Number of Samples
(a) Qubit Count
400
300
Depth per QAOA Layer
200
100
0
0
100
200
300
400
Number of Qubits
(b) Depth
(c) Gate Count

Figure 3: Scatter plots of the depth and gate count against number of qubits of the QAOA circuits required to solve the MWC problem on various subsets of SARS-CoV-2 genome samples.


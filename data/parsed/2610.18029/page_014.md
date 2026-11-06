## 4.2 The QUBO Lagrange Multiplier

Conventional wisdom suggests that the Lagrange multiplier used to turn a constrained problem into an unconstrained problem must be large enough such that the ground state corresponds to the case where all constraints must be satisfied. For the MWC problem, this corresponds to the Lagrange multiplier being at least as large as the largest vertex weight. For example, a common choice is twice the largest vertex weight.

However, given the above postprocessing, we can efficiently ensure our final results must satisfy our edge constraints and hence it is less essential that our quantum sampling-based solver strictly enforces these constraints. Indeed, while the ground states of the cost Hamiltonian with large Lagrange multipliers correspond to exactly the MWCs of the graph, the states with energies that are low but not optimal do not necessarily correspond to states that are very close to any of the MWCs as one could have a clique with weight that is just 1 off the maximum, but has a completely different graph structure.

We find that by taking a Lagrange multiplier that is smaller, the ground states no longer correspond to the MWCs, as adding a vertex with a few missing edges to the rest of the putative clique can still decrease the Hamiltonian energy. Taking small graph examples for which we can enumerate all possible subgraphs, and by applying the postprocessing methodology above to the low-energy subgraphs, we see that taking the ratio between the Lagrange multiplier and the highest vertex weight to be 0.1 gives the highest proportion of subgraphs that yield MWCs.

## 4.3 Hardware proof of Concept

An example of a current quantum device that the general public can have access to now is the series of devices by IBM. They have up to 156 qubits. Therefore, given the 1-to-1 variable-to-qubit mapping of our QUBO formulation of the MWC enumeration problem, on an IBM devices, we can only run instances of the problem which results in a final reduced<tbc>

0.9
Bottom 0.1%
Bottom 1%
0.8
Bottom 10%
Bottom 20%
0.7
Bottom 50%
100%
Proportion Mapping to MWCs
0.6
0.5
0.4
0.3
0.2
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
Lagrange Multiplier
Lagrange Multiplier

Bottom 0.1%
0.45
Bottom 1%
Bottom 10%
0.40
Bottom 20%
Bottom 50%
0.35
100%
Proportion Mapping to MWCs
0.30
0.25
0.20
0.15
0.10
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
Lagrange Multiplier

(a) 20 Vertices

(b) 23 Vertices

Figure 4: For different Lagrange multipliers, the low energy solutions correspond to different subgraphs. Taking different fractions of the lowest energies, we show what proportions of the corresponding subgraphs correspond to MWCs given our postprocessing algorithm.


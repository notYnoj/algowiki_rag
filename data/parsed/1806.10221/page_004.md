<tbc>polynomial with respect to memory. The first _N_<sup>2</sup> qubits denote the system qubits having state \(|\Psi\rangle\), which is a superposition of all basis states representing configurations satisfying the Row Criteria. The rest (\(\frac{N^2}{2}+\frac{N}{2}-1\)) ancillary qubits are entangled with \(|\Psi\rangle\), all of which possess \(|1\rangle\) state only for the basis states encoding the solutions to the _N_-Queens Problem, following the execution of our protocol. The other basis states will have at least one associated ancilla which is in \(|0\rangle\) state. Also, a total (_N_+2)(_N_-1) operations are required for reducing the search space to the configurations satisfying the Column Criteria, besides the Row Criteria. It has been found that O(_N_<sup>3</sup>) operations are required for the diagonal checks, a proof of which is presented in Supplementary Section. As a result, it takes quantum operations of order O(_N_<sup>3</sup>) in total to solve the problem, demonstrating that the _N_- Queens Problem can be efficiently solved on a quantum computer in both polynomial time (O(_N_<sup>3</sup>)) and polynomial memory (O(_N_<sup>2</sup>)) using our protocol.

We simulated our _N_-Queens Solver protocol using the QISKit simulator, which is the same simulator used in IBM Quantum Experience as part of its Custom Topology feature. The simulation was performed for _N_=4 case, for which we know there exist 2 solutions. Hence, a total of 25 qubits (16 system qubits plus 9 ancillas) were used. Measurements were performed on all 25 qubits. The simulation was performed 310 times. It was observed that in two out of 183 different measurement outcomes that were obtained, all the 9 ancillary measurements yielded \(|1\rangle\) state. The corresponding measurement reading of the 16-qubit system in each such case represented a chess- board configuration that satisfied the _N_-Queens Criteria. Hence, we successfully obtained both the solutions to the 4-queens problem by the implementation of our proposed algorithm. The QASM code for performing the given simulation has been presented in Supplementary Section.

## III. APPLICATION OF _N_-QUEENS PROBLEM: SATELLITE COMMUNICATION

One possible application of the _N_-Queens Problem is the transmission of information from satellites orbiting around the Earth without any data loss due to interference \[28\]. The _N_-Queens solution configurations can aid in maximizing the amount of information transmitted and the land area over which it is transmitted for a fixed number of _N_ beam reflectors on a satellite that bounds an area of \(N\times N\) sq. units in space. The information is transmitted in the form of beams.

Here, we make a few assumptions:

1. All the N beam reflectors orbit the Earth in one plane i.e. the plane of the satellite at all times, and this plane bisects the Earth.<tbc>

2. The orientation of the plane of the satellite with respect to the Earth remains constant as the satellite<tbc>

<tbc>revolves around the Earth.<tbc>

3. The N beam reflectors can transmit information vertically, horizontally and diagonally along all the planes.<tbc>

4. The N beam reflectors can only rotate about one of the three mutually orthogonal axes at a time i.e, two axes in the plane of the satellite and one axis perpendicular to the plane.<tbc>

5. The N beam reflectors have no restrictions while rotating about the axes that lie on the plane of the satellite. However, while rotating about the axis perpendicular to the satellite, all beam reflectors must rotate in the same direction, and with the same speed.

It is obvious that if two signal waves are transmitted along the same diagonal, row or column, they interfere continuously after some point with a phase difference that varies randomly with time. This leads to the superposition of the signal waves, which results in the loss of information sent by both beam reflectors.

In an _N_-Queens solution state configuration, none of the N beams transmit information along the same row, column or diagonal. Therefore, the beams produced meet<tbc>

W
A
θ
π-0
π-0
4
2
π-0
π-0
π
4
θ
θ
B
C
D

FIG. 2. **Beam configuration for satellite communication.** A, B, C and D are four beam reflectors that are placed in the satellite plane (represented by the grid) in the _N_-Queens configuration. They all reflect beams horizontally, vertically and diagonally at all times (denoted by the dotted lines). A and B rotate at speeds \(\omega\) and \(-\omega\). If A and B rotate by \(+\theta\) and \(-\theta\) degrees respectively, they interfere with a phase difference that is random with time, along the line joining the two. The same happens if they rotate by \(+(\pi/4-\theta)\) and \(-(\pi/4-\theta)\) respectively, or \(+(\pi/2-\theta)\) and \(-(\pi/2-\theta)\) respectively.

.


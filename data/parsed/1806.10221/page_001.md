# A Novel Quantum N-Queens Solver Algorithm and its Simulation and Application to Satellite Communication Using IBM Quantum Experience

Quantum computers can potentially solve problems that are computationally intractable on a classical computer in polynomial time using quantum-mechanical effects such as superposition and entanglement. The _N_-Queens Problem is a notable example that falls under the class of NP- complete problems. It involves the arrangement of _N_ chess queens on an \(N\times N\) chessboard such that no queen attacks any other queen, i.e. no two queens are placed along the same row, column or diagonal. The best time complexity that a classical computer has achieved so far in generating all solutions of the _N_-Queens Problem is of the order O(_N_!). In this paper, we propose a new algorithm to generate all solutions to the _N_-Queens Problem for a given _N_ in polynomial time of order O(_N_<sup>3</sup>) and polynomial memory of order O(_N_<sup>2</sup>) on a quantum computer. We simulate the 4-queens problem and demonstrate its application to satellite communication using IBM Quantum Experience platform.

### I. INTRODUCTION

NP complete problems encompass all decision problems in class NP that can be verified in polynomial time [1, 2]. However, the time taken to obtain a solution for an NP complete problem is not polynomial. Some common examples of NP complete problems include the traveling salesman problem [3], the subset sum problem [4], the Hamiltonian cycle problem [5], the knapsack problem [6, 7] and satisfiability problem [8, 9] to name a few.

The _N_-Queens Problem is an NP complete problem [10]. It states that _N_ queens must be placed on an \(N\times N\) chessboard such that no two queens can attack each other [11]. The queens follow the moves that a classical chess queen follows, i.e. horizontal, vertical and diagonal jumps across any number of squares as long as the queen is unobstructed by the presence of another queen. The generalized _N_-Queens Problem [11] has already been attempted over the years [12]. It has been approached using multiple classical computational methods [13]. Some of these include the brute force algorithm [14], different variants of the backtracking algorithm [15, 16] and the greedy technique [17]. The brute force algorithm has the highest growth rate (with _N_) of the order O(_N<sup>N</sup>_). The backtracking algorithm is slightly better than the former with a time complexity of the order O(_N_!). Other variants of the backtracking method such as the optimized backtracking and novice backtracking algorithms have an exponential time complexity [18]. The systematic and greedy search methods have a time complexity of the order O(_N_<sup>3</sup>) to O(_N_<sup>2</sup>). These algorithms, although solvable in polynomial time, often yield a set of

limited solutions to the _N_-Queens Problem for a given _N_.

The _N_-Queens Problem finds vast application in various fields such as parallel memory storage schemes [19], low density parity check codes [20], deadlock prevention [11], VLSI testing [21], neural networks [22, 23] and load balancing [24] etc.

### II. SOLVING THE N-QUEENS PROBLEM

The criteria for a particular configuration of an \(N\times N\) chessboard to be a solution to the _N_-Queens Problem are stated below. We shall collectively refer to them as the _N_-Queens Criteria.

\(\bullet\) **Row Criteria:** The total number of queens in each row is 1.

\(\bullet\) **Column Criteria:** The total number of queens in each column is 1.

\(\bullet\) **Diagonal Criteria:** The total number of queens in every possible diagonal is either 0 or 1.

We formulate this problem by representing the \(N\times N\) chessboard as an \(N\times N\) matrix. The positions of queens and the vacant spaces are denoted by 1s and 0s respectively. We represent each row of the resultant matrix as an _N_-qubit basis state. Hence, the _N_-qubit quantum register for all possible row configurations having one queen can be represented as,

\(|\psi\rangle=\frac{1}{\sqrt{N}}[|R_1\rangle+|R_2\rangle+\dots+|R_{N-1}\rangle+|R_N\rangle]\) (1)

where \(R_i(i\in[1,N]\cap\mathbb{N})\) represents the _i_th row of the \(N\times N\) identity matrix. The above state \((|\psi\rangle)\) is known

<sup>∗</sup> These authors contributed equally to this work.

Rounak Jha<sup>1</sup>,<sup>∗</sup> Debaiudh Das<sup>2</sup>,<sup>∗</sup> Avinash Dash<sup>3</sup>,<sup>∗</sup> Sandhya Jayaraman<sup>4</sup>, Bikash K. Behera<sup>3</sup>, and Prasanta K. Panigrahi<sup>3</sup>

<sup>1</sup>_Department of Physical Sciences, Indian Institute of Science Education and Research, Pune, 411021, India_

<sup>2</sup>_School of Physical Sciences, National Institute of Science Education and Research, HBNI, Jatni, 752050, India_

<sup>3</sup>_Department of Physical Sciences, Indian Institute of Science Education and Research Kolkata, Mohanpur, 741246, West Bengal, India and_

<sup>4</sup>_Department of Computer Science and Engineering, Nitte Meenakshi Institute of Technology, Bangalore, 560054, India_


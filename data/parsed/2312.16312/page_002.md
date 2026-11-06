and motivates computer searches to be particularly helpful. However, classical computational methods are very limited in addressing such challenges due to the need to process large datasets and explore extensive solution spaces. In recent years, quantum technology has shown rapid advancements to approach computational quantum advantage for different numerical tasks [9]-[11], particularly optimization problems (demonstrated recently even on near-term devices)

Until today, numerous algorithms have been developed to solve the N-Queens problem, each with varying time complexities. While we won’t delve into every algorithm, let’s briefly explore a few notable ones. The first algorithm is the Backtracking algorithm, which has a worst-case time complexity of _O(N_!) [13]. It is a classic approach for solving the N-Queens problem. The next algorithm, introduced by Sosic and Gu in 2010, is a linear-time algorithm. It employs a pattern-based approach to produce at least one unique solution for all values of N greater than 3. The time complexity of the Sosic and Gu algorithm is _O(N_), a significant improvement over the Backtracking algorithm’s time complexity [6]. Over the years, many efforts have been made to solve the N-Queens problem in the quantum regime. A quantum-inspired differential evolution algorithm for solving the N-Queens problem was proposed by Draa et al. [14]. Recent developments include the work of Codognet where the QUBO model was used to solve the N-Queens problem on the D-Wave quantum annealer [15].

We might wonder why there is such persistent effort to solve the challenging N-Queens problem. The reason lies in the diverse applications of the N-Queens problem and its variations across various domains. These applications encompass not only neural networks [16] algorithm benchmarking [17] and parallel memory storage schemes [18] but also extend to fields like VLSI (Very-Large-Scale Integration) design and testing [19], AI and robotics [20], and more. The versatility of the N-Queens problem makes it a valuable resource for addressing complex real-world challenges and advancing the state of the art in numerous areas of science and technology.

## III. PREVIOUS WORK

Our solution builds upon the foundations laid by the work of Jha et al [21], and we would like to acknowledge and credit this work throughout our paper. We will use notations and representations introduced in [21]. Additionally, we will<tbc>

<tbc>introduce two new solutions inspired by the ideas presented in [21]. The authors of this work leveraged quantum properties, such as superposition and entanglement, to tackle the N- Queens problem. In their approach, they proposed a novel way of representing the positions of Queens on a chessboard using an \(N\times N\) matrix. The squares are numbered from 1 in the top-left corner to N squared in the bottom-right corner, with numbering proceeding from left to right and top to bottom. This concept can be translated into a Quantum Circuit comprising \(N\times N\) qubits, where each qubit is assigned a number from 1 to \(N\times N\). If a specific position on the chessboard is occupied by a Queen, the corresponding qubit is encoded in an excited state \(|1\rangle\). All other qubits remain in the ground state \(|0\rangle\). This is shown in Figure 1.

Let’s discuss their approach to solving the N-Queens problem.

They decomposed this complex problem into three simpler criteria. A set of Queen positions satisfies all three criteria together, making it a potential solution to the N-Queens problem.

**Row Criteria:** The row criteria is satisfied when there is exactly one queen at any position in every row of the chessboard. In quantum circuit terms, this means that exactly one qubit in every row should be in the excited state \(|1\rangle\).

**Column Criteria:** The column criteria is met when there is exactly one queen at any position in every column of the chessboard. In the quantum circuit, this translates to exactly one qubit in every column being in the excited state \(|1\rangle\).

**Diagonal Criteria:** The diagonal criteria present the most challenging aspect of the problem. The chessboard contains a total of (4_N_-2) diagonals. On each of these diagonals, there should be at most one queen, and it’s acceptable for many diagonals to have no queens at all. In quantum circuit terms, this implies that on every diagonal, there should be a maximum of one qubit in the excited state \(|1\rangle\). Notably, a considerable number of diagonals might not have any qubit in the excited state \(|1\rangle\) at any of their positions. Let us now delve into how the authors of [21] have addressed these criteria in detail in the following subsections:

### A. Solving Row Criteria

We begin by exploring all the possible setups for positioning queens on a chessboard, regardless of the number of queens. Each square on the chessboard can either have a queen placed on it or remain empty, resulting in two potential options for each square. Given that there are \(N\times N\) squares on an \(N\times N\)

\begin{tabular}{cc}
_N_ & Number of Solutions \\
1 & 1 \\
2 & 0 \\
3 & 0 \\
4 & 2 \\
5 & 10 \\
6 & 4 \\
7 & 40 \\
8 & 92 \\
\end{tabular}

1
0
0
0
1
1
0
0

TABLE I NUMBER OF SOLUTIONS FOR THE N-QUEENS PROBLEM THE FOLLOWING TABLE WAS REFERRED FROM TABLE 1 OF THE ARTICLE [12]

Fig. 1. \(|1\rangle\) and \(|0\rangle\) formulated in the braket notation which is realised in the form of a chessboard


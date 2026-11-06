Next, our algorithm random selects from one of the valid position, to place the queen, Q. And the valid point algorithm 1 is used to invalidate the attacked positions, X.

The above Step 1 is then repeated by choosing another random positions that is still valid. The algorithm continues placing queens till there are at least as much valid positions as the queens to be placed. This can result in two scenios.

Here on Scenario 2 in  4, the algorithm has exhausted the valid space without solving the nqueen problem, as such it restarts the whole search from Step 1 as in  1.

## 3.3. Analysis

In this section, we present a formal analysis of the above algorithm to demonstrate its correctness. The analysis uses the concept of Loop Invariant Statement which is a condition that holds true before and after each iteration of a loop. By establishing such an condition, we show that the algorithm progresses towards its intended goal without violating essential correctness criteria

**Loop Invariant Statement**

At the start of each iteration of the loop in the las vegas function, the result matrix correctly represents the state of the board, where queens have been placed in valid positions, and all invalid positions (due to the placed queens) have been marked accordingly. Additionally, the valid space list contains only those positions that are still available for placing a new queen.

**Initialization**

The result matrix is initially filled with 1s, indicating that all positions are valid for placing a queen, and valid space list consists of index 0 to _n_<sup>2</sup>-1 Since before the loop begins, no queens<tbc>

\begin{tabular}{ccccc}
X & X & V & V & \\
Q & X & X & X & X \\
X & X & V & V & \\
X & V & X & V & \\
\end{tabular}

\begin{tabular}{ccccc}
X & X & Q & X & \\
Q & X & X & X & \\
X & X & X & Q & \\
X & Q & X & X & \\
\end{tabular}

\begin{tabular}{ccccc}
X & X & X & Q & \\
Q & X & X & X & \\
X & X & X & X & \\
X & Q & X & X & \\
\end{tabular}

2: Place Queen at position (1,0). Mark attacked squares in red (X).

3: N queens placed on a _nxn_ chessboard that follows constraint.

4: Less than N queens placed on a _nxn_ chessboard that follows constraint.


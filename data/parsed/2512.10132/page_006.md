• **Output:** The witness path _P_ is written to a write-only output tape. This tape does not contribute to the space bound.<tbc>

• **Work tape:** The machine has one or more read/write work tapes. Space is measured as the number of cells used on these work tapes over a fixed finite alphabet \(\Gamma\).<tbc>

• **Computational primitives:** We assume that operations in the semiring (comparison, \(\oplus\), \(\otimes\)) and index arithmetic on {1_,...,T_} can be performed in time and space polynomial in log_T_.

Throughout the paper, all space bounds refer to cells on the work tapes; the read-only input tape and the write-only output tape do not contribute to the space measure. When we informally say that an algorithm uses \(O(\omega)\) space (in words), we mean that it stores the values of at most \(O(\omega)\) DP states at any time, which corresponds to \(O(\omega logT)\) work-tape cells under our encoding assumptions. We restrict attention to algorithms that halt in time poly(_T_). Our primary objective is to minimize the work-tape space required to produce the output sequence _P_, as a function of the structural parameters _T_ and \(\omega\).

## 3 Warm-Up: Hirschberg as a Special Case

Before addressing the general graph-theoretic setting, we revisit Hirschberg’s classic algorithm for the Longest Common Subsequence (LCS) problem. We view it not as a special-purpose geometric trick, but as an instance of a more general pattern: a recursive decomposition of a topological order together with meet-in-the-middle reasoning about optimal paths. This perspective will directly motivate our generalization to arbitrary DAGs with bounded frontier width.

### 3.1 Classical grid DP

Let _A=a_<sub>1</sub>_...a<sub>m</sub>_ and _B=b_<sub>1</sub>_...b<sub>n</sub>_ be sequences over an alphabet \(\Sigma\). The standard dynamic programming formulation for LCS (or, with modified weights, for edit distance or global alignment) constructs a grid graph _G<sub>m,n</sub>_ with vertex set<tbc>

\(V=\{(i,j):0\le i\le m,0\le j\le n\}.\)

<tbc>Directed edges connect (_i,j_) from (_i_-1_,j_), (_i,j_-1), and (_i_-1_,j_-1), with edge weights determined by the scoring scheme (match/mismatch, insertion, deletion). The DP value _x<sub>i,j</sub>_ at (_i,j_) is defined by a max-type recurrence, e.g. for LCS:

\(x_{i,j}=\left\{\begin{array}{ c c }
0 & \text{if}i=0\text{or}j=0, \\
max\{x_{i-1,j},x_{i,j-1},x_{i-1,j-1}+\mathbf{1}[a_i=b_j]\} & \text{otherwise},
\end{array}\right.\)

with deterministic tie-breaking to select a unique predecessor in case of equality.

In the language of Section 2:

• the graph size is _T_=|_V_|=(_m_+1)(_n_+1);<tbc>

• a natural topological order \(\tau\) is lexicographical (row-major or column-major), e.g. \(\tau(i,j)=i(n+1)+j\);<tbc>

• for either of these topological orders, any cut in the order intersects \(\Theta(min\{m,n\})\) DP states, so the frontier width is \(\omega(G_{m,n},\tau)=\Theta(min\{m,n\})\);<tbc>

• the recurrence is over a max-type semiring (e.g. (Z,max,+)) with constant in-degree \(\Delta_{max}=3\), and deterministic tie-breaking yields a unique predecessor at each vertex.

A standard forward implementation maintains a rolling buffer of one row (or one column), evaluating all _T_ states in _O(T_) time and \(O(\omega)\) space (in words) and computing the optimal value _x<sub>m,n</sub>_. However, reconstructing an optimal alignment naively requires storing a back-pointer at each cell, resulting in \(\Theta(mn)\) words for traceback.


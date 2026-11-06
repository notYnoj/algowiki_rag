<tbc>We employ algorithm 1 to generate a series of subproblems by pre-placing queens in the first k rows. Specifically, starting from the first row, all feasible positions are traversed(only the first half). After k iterations, the placement of k queens is completed, subsequently generating a series of (cur, left, right) triplets. Each triplet represents a distinct subproblem corresponding to a partial solution state. Although all subproblems share the same recursion depth, the size of their solution spaces exhibits considerable variation. This, in turn, leads to significant differences in the time required to solve each individual subproblem. This was confirmed by subsequent Multi-GPU evaluation parts.

However, the recursively implemented algorithm 1 is not CUDA-friendly and must be transformed into an iterative form by explicitly simulating the recursion call using a stack structure. As previously mentioned, the solution space for each subproblem forms a subtree, where each node represents the placement of queens in the first _k_ rows, and each branch denotes a valid placement position for the _k+1_ row. For traversing such trees, there are generally two approaches: breadth-first search (BFS) and depth-first search (DFS). BFS resembles level-order traversal of a node, where all branches of a node are pushed onto the stack at once. Algorithm 1 is just a BFS-based implementation. In contrast, DFS explores only one branch at a time, proceeding along a single path until reaching its deepest point, and then backtracking to the previous node to continue exploration.

From the perspective of space complexity, DFS demonstrates significant advantages. The maximum depth of its stack space is strictly equal to N minus the number of pre- placed rows, and this deterministic upper bound ensures predictable memory requirements. Whenever the search reaches the maximum depth, the algorithm either successfully finds a valid solution or performs backtracking to return to the previous level and continue the search.

In contrast, BFS must simultaneously maintain all possible branches of the current node, resulting in a worst-case space complexity of O(N\(\times\)d). Theoretically, this imposes an N-fold increase in memory demand compared to DFS (though in practice, this gap is often somewhat reduced). Given the scarcity of GPU shared memory resources (typically limited to just tens of KB), adopting a DFS strategy minimizes memory usage, potentially allowing the complete stack structure to reside entirely within shared memory. This characteristic makes DFS the ideal choice for GPU implementations.

Therefore, our CUDA-based N-Queens algorithm employs a DFS strategy. It should be noted that the DFS implementation requires additional storage of the **valid\_pos** variable in the stack space. Nevertheless, its overall memory consumption remains significantly lower than that of the BFS approach. The code for the iterative N-Queens algorithm based on depth-first search is shown in Algorithm 2.

**Algorithm 2** DFS-based Iterative Somers Algorithm

1: **def** n\_queens\_iterative(N, cur, left, right, sum):

2: last = (1 \(\checkmark\) N) - 1

3: stack = \[0\] \* 96

4: top = 0

5: valid\_pos = last \& (∼(cur|left|right))

6: stack\[top : top + 4\] = \[cur, left, right, valid\_pos\]

7: top += 4

8: **while** top != 0:

9: \[cur, left, right, valid\_pos\] = stack\[top - 4 : top\]

10: p = valid\_pos \& (-valid\_pos)

11: valid\_pos -= p

12: stack\[top - 1\] = valid\_pos

13: top -= (valid\_pos == 0 ? 4 : 0)

14: cur = cur| p

15: **if** cur == last:

16: sum += 1

17: continue

18: left = (left|p) \(\checkmark\) 1

19: right = (right|p) \(\gg\) 1

20: valid\_pos = last \& (∼(cur|left|right))

21: **if** valid\_pos == 0:

22: continue

23: stack\[top : top + 4\] = \[cur, left, right, valid\_pos\]

24: top += 4

We have designed a stack structure with a capacity of 96 bytes <sup>4</sup> in algorithm 2. This stack is used to store four critical state variables: cur, left, right, and valid\_pos, with a maximum supported depth of 24 layers. When N \(\le\) 24, it can handle cases where no initial rows are pre-placed. If N \> 24, we can pre-place the first few rows to process subproblems with reduced depth. To fully leverage the GPU’s massive parallel computing capability, it is essential to generate a sufficient number of independent subproblems through row pre-placement strategies. Experimental results (detailed in Section 4.1) demonstrate that pre-placing 5-6 rows yields optimal parallel performance in GPU implementations. When pre-placing 5 rows, algorithm 2 can be used to solve the 28-Queens problem.

Compared to the original Somers algorithm, the above iterative depth-first search implementation of the N-Queens problem is more concise. By processing subproblems, it reduces the required stack space size, making it feasible to entirely place the stack in the GPU’s shared memory.

## 3 Bank Conflict-Free GPU Implementation

### 3.1 Bank Conflict-Free Shared Memory Access

When porting the iterative DFS-based N-Queens algorithm to GPU platforms, the code in algorithm 2 can be directly<tbc>

<sup>4</sup>A value corresponding to the maximum shared memory size per thread under static allocation strategy in NVIDIA GPUs such as the RTX 4090.


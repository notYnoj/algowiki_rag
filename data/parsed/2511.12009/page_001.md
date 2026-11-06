# High-Performance N-Queens Solver on GPU: Iterative DFS with Zero Bank Conflicts

### Abstract

The counting of solutions to the N-Queens problem is a classic NP-complete problem with extremely high computational complexity. As of now, the academic community has rigorously verified the number of solutions only up to N \(\le\) 26. In 2016, the research team led by Preußer solved the 27-Queens problem using FPGA hardware, which took approximately one year, though the result remains unverified independently. Recent studies on GPU parallel computing suggest that verifying the 27-Queens solution would still require about 17 months, indicating excessively high time and computational resource costs. To address this challenge, we propose an innovative parallel computing method on NVIDIA GPU platform, with the following core contributions: (1) An iterative depth-first search (DFS) algorithm for solving the N-Queens problem; (2) Complete mapping of the required stack structure to GPU shared memory; (3) Effective avoidance of bank conflicts through meticulously designed memory access patterns; (4) Various optimization techniques are employed to achieve optimal performance. Under the proposed optimization framework, we successfully verified the 27-Queens problem in just 28.4 days using eight RTX 5090 GPUs, thereby confirming the correctness of Preußer’s computational results. Moreover, we have reduced the projected solving time for the next open case--the 28-Queens problem--to approximately 11 months, making its resolution computationally feasible. Compared to the state-of-the-art GPU methods, our method achieves over 10\(\times\) speedup on identical hardware configurations (8 A100), while delivering over 26\(\times\) acceleration when utilizing 8 RTX 5090 GPUs, and brings fresh perspectives to this long-stagnant problem<sup>1</sup>.

### 1 Introduction

The N-Queens problem is a classical puzzle originating from the historic 8-Queens problem [1]. The objective is to place N queens on an N\(\times\)N chessboard such that no two queens threaten each other horizontally, vertically, or diagonally. While finding a single valid solution is relatively straightforward, precisely counting all valid solutions dramatically increases computational complexity. Currently, no general closed-form solution exists, leaving exhaustive search with backtracking as the only viable approach.

The most efficient classical backtracking algorithm is the Somers algorithm [12], which employs bitwise operations to rapidly eliminate invalid positions, thereby dramatically reducing the search space. Furthermore, its non-recursive implementation offers excellent portability, making it the foundation for many parallel computing implementations. However, even the Somers algorithm reaches its computational limits when dealing with large-scale N-Queens problems.

The N-Queens problem can be decomposed into a set of independent subproblems by pre-placing queens in the first few rows. These subproblems can then be solved in parallel, with their results aggregated for the final count (Figure 1). During pre-placement, only the first half of the positions in the first row need to be considered, as the solutions for the latter half are symmetric. Additionally, if N is odd, placing a queen in the central position of the first row allows symmetry-based optimizations for the second row. Due to symmetry--only N/2 - 1 positions need evaluation<sup>2</sup>. As shown in the figure, all valid solutions to the N-Queens problem form a tree, where solving the problem equates to traversing this tree. Each subproblem corresponds to an independent subtree, with no overlap between subtrees. This inherent independence provides ideal conditions for parallel acceleration, enabling subproblems to be solved entirely in parallel.

#### 1.1 Related Work

Three primary parallel optimization approaches are commonly employed: distributed multi-core computing, FPGA, and GPU. Distributed multi-core computing approach typically involves partitioning subproblems across multiple nodes and utilizing numerous CPU cores for computation. In 2004, the Kise’s team [3] successfully solved the 24-Queens problem using 68 Pentium4 Xeon processors in 22 days. Subsequently in 2007, Caromel’s team [2] employed 260 machines to solve the 25-Queens problem over 185 days. Both implementations relied on extensive CPU core clusters for parallel processing. However, as general-purpose processors, CPUs demonstrate limited advantages in parallel computation.

FPGAs later emerged as a breakthrough technology due to their high parallelism and hardware programmability. In 2009, Preußer et al. [8] solved the 26-Queens problem in

<sup>1</sup> can be found at https://github.com/ygch/n\_queens. <sup>2</sup>The subtraction accounts for the three central positions in the second row being blocked by the queen in the first row.

Guangchao Yao XiaoPeng Motors Beijing, China yaogc@xiaopeng.com

Yali Li XiaoPeng Motors Beijing, China lyl19@xiaopeng.com


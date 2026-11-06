<tbc>comparative purpose, we designate this optimization as Configuration 6.

#### 3.2.3 Approach 3.

In Algorithm 1&2, the recursion depth always reaches N levels if the solution is valid. However, when traversing to the (N-1)th row, we have already computed the valid positions (valid\_pos) for the Nth row. If valid\_pos equals 0, it indicates no feasible solution exists; otherwise, one valid solution is confirmed. This observation demonstrates that after completing the traversal of the (N- 1)th row, no additional stack push operation is required - only a check of valid\_pos is needed to determine the result. Based on this optimization, we successfully reduce the maximum recursion depth by one level, consequently increasing the maximum solvable problem size N by 1 for all configurations in  1.

### 3.3 Further Optimization Using Inline PTX Assembly

The success of Deepseek-v3 \[4\] has demonstrated that PTX \[6\] can serve as a viable alternative to CUDA for achieving superior performance in GPU computing. Its key advantages include direct hardware control for performance optimization, efficient register allocation for compute-intensive workloads, and the ability to integrate inline assembly for critical kernel optimization. PTX provides developers with fine-grained control over GPU execution while preserving compatibility across NVIDIA’s GPU generations.

To maximize code readability, we selectively converted only the while loop in Algorithm 2 into inline PTX assembly. Our approach involved: (1) generating the complete PTX implementation of the kernel function using the NVCC compiler, and (2) extracting and transforming the while loop section into inline PTX form. However, this initial modification alone did not yield performance improvements, necessitating further optimization of the inline PTX implementation.

PTX code optimization adheres to two key principles: (1) instruction count minimization in one loop and (2) branch operation reduction. Based on these two principles, we optimized three critical aspects of the inline PTX implementation: (1) employing the **lop3** instruction to compute ∼(cur | left |right), reducing the instruction count from three to one; (2) removing two address calculation instructions in the loop, and (3) redesigning the "last-row optimization" logic by using **selp** instruction to replace two branches. Furthermore, we optimized the computation by substituting the input parameter N with N-1, which removed one redundant subtraction instruction.

## 4 Experiment

The experimental evaluation primarily utilizes three GPU cards: RTX 4090, RTX 5090, and A100. The key hardware specifications \[5, 14\] of these cards are compared as follows.<tbc>

<tbc>Comparative analysis demonstrates that while the A100 exhibits superior communication bandwidth compared to the RTX 4090, it contains significantly fewer computing cores. In solving the N-Queens problem, we generate numerous mutually independent subproblems through pre-placing the first few rows. As each subproblem can be processed independently by individual threads - requiring neither inter- thread communication nor CPU interaction - the RTX 4090’s greater number of computing cores provides distinct advantages in this computational scenario. Given that the RTX 5090 offers approximately 30% more computing cores than the RTX 4090, we project a corresponding 30% improvement in computational performance.

First, we conduct experiments using a single RTX 4090 to validate the effectiveness of our proposed optimization methods. Subsequently, we scale the experiment to 8 GPUs, incorporating both A100 and RTX 5090, to compare the method’s performance across different GPU architectures. At last, we will utilize 8 RTX 5090 GPUs to solve the 26-Queens problem.

### 4.1 Impact of Pre-placed rows on Speed

Considering that Configuration 1 offers the largest problem size support capacity (see Section 3.2.1), we selected this configuration to evaluate the performance impact of pre-placing the first R rows on a single RTX 4090. The experimental results are presented in  3.

From  3, we can see RTX 4090 demonstrates significant performance sensitivity to the number of pre-placed rows. Optimal result is achieved with 5-row pre-placement, followed by 6-row pre-placement, while other configurations result in notable performance degradation. As problem<tbc>

\begin{tabular}{ccccc}
**GPU** & **CUDA** & **BandWidth** & **Max Shared** & **Compute** \\
 & **Cores** & & **Memory** & **Capability** \\
RTX 4090 & 16384 & 1008GB/s & 99KB & 8.9 \\
RTX 5090 & 21760 & 1792GB/s & 99KB & 12.0 \\
A100 & 6912 & 1935GB/s & 163KB & 8.0 \\
\end{tabular}

\begin{tabular}{cccccc}
**N** & **R=4** & **R=5** & **R=6** & **R=7** & **R=8** \\
17 & 162 & 136 & 142 & 171 & 296 \\
18 & 343 & 232 & 237 & 314 & 573 \\
19 & 1564 & 978 & 972 & 1268 & 2524 \\
20 & 8963 & 6469 & 6536 & 7495 & 10579 \\
21 & 83075 & 52583 & 52501 & 57169 & 66861 \\
22 & 630574 & 441022 & 452699 & 486972 & 537077 \\
\end{tabular}

** 2.** Hardware Comparison of RTX 4090, RTX 5090, and A100

** 3.** Performance Comparison (in milliseconds) of Different N-Queens Problem on a single RTX 4090 with Varying Pre-placed Rows


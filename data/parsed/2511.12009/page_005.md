<tbc>reused without modification. However, it should be noted that by default the stack variable resides in local memory, which is essentially part of global memory and suffers from high access latency. We can use sentence " \_shared\_int stack\[48\*256\]" to transfer the stack from local memory to shared memory with size 48KB. This allocation size corresponds to the maximum static shared memory capacity natively supported by NVIDIA GPU architectures. For scenarios requiring shared memory exceeding 48KB, a dynamic allocation strategy must be employed, mentioned in Section 3.2.

Although migrating the stack from local memory to shared memory is relatively straightforward, the primary challenge lies in effectively avoiding shared memory bank conflicts. The key principle is to ensure each thread within a warp accesses only a dedicated bank. Based on this concept, we designed a shared memory access pattern as illustrated in Figure 4. Rather than being allocated in contiguous memory space, each thread’s stack is spaced at 128-byte intervals. This arrangement guarantees that memory addresses accessed by all threads within a warp reside in distinct banks, effectively eliminating bank conflicts. Through this design, shared memory access speed is significantly enhanced, thereby dramatically improving the GPU’s computational efficiency in solving the N-Queens problem.

The above shared memory access pattern can indeed avoid bank conflict, and deliver significant acceleration. However, to access cur, left, right, and valid\_pos, the GPU still needs to trigger four separate memory transactions. In practice, we can alternatively utilize CUDA’s **int4** data type. Theoretically, using int4 would place these four variables in four consecutive memory banks, potentially causing 4-way bank conflicts<tbc>

<tbc>within a warp. However, when using int4 types, CUDA automatically reduces the scheduling granularity from warp to quarter-warp, thereby eliminating bank conflicts. Using int4 type can also complete the access through four memory transactions.

Empirical results demonstrate that compared to the bank- conflict-free implementation mentioned above, the int4 approach provides additional performance gains, particularly when implemented with inline PTX assembly. Consequently, we adopt int4 as our default implementation.

## 3.2 Optimization Techniques for Limited Shared Memory Capacity

Due to the constraints of static shared memory allocation (maximum 48 KB), when each thread requires a stack space of 96 x 4 bytes, the number of threads per block must be limited to 128 (since 48 KB = 128 x 96 x 4 bytes). This configuration reduces per-block task throughput, thereby negatively impacting overall parallel computing efficiency. To address this issue, we propose three feasible optimization approaches.

### 3.2.1 Approach 1.

To optimize parallel processing performance, we increase the number of threads per block within the 48KB shared memory constraint by reducing the stack space allocation per thread (while simultaneously decreasing the maximum recursion depth). For N-Queens problems of different scales, we designed multiple experimental configurations ( 1). Given a specific N, we select Configurations 1, 2, or 3 according to their respective maximum supported values of N. Configurations 4 and 5 are excluded from subsequent experiments due to their limited applicability to small problem sizes, but are included here for completeness.

### 3.2.2 Approach 2.

This approach replaces static shared memory allocation with dynamic allocation to overcome the 48KB limitation. For GPUs like the A100 and RTX 4090, dynamic allocation allows expanding the shared memory per block to 96KB. However, at the hardware level, shared memory and L1 cache share the same physical resources. Increasing shared memory allocation consequently reduces L1 cache space, which may offset potential speed gains. This trade-off is experimentally validated in later sections. For<tbc>

\begin{tabular}{ccccc}
**Config** & **Block

Size** & **Stack

Size** & **Recursion

Depth** & **Max N

(Pre-placing first

6 rows)** \\
1 & 128 & 96 & 24 & 30 \\
2 & 160 & 76 & 19 & 25 \\
3 & 192 & 64 & 16 & 22 \\
4 & 256 & 48 & 12 & 18 \\
5 & 512 & 24 & 6 & 12 \\
\end{tabular}

valid_pos
valid_pos
stack for thread32
96
stack for thread63
right
right
96
left
left
cur
cur
valid_pos
valid_pos
stack for thread0
right
96
stack for thread31
right
96
left
left
cur
cur
bank0
bank31

**Figure 4**. Stack space allocation in shared memory for each thread without bank conflict, each stack can hold 96 integers and support a maximum iteration depth of 24.

** 1**. Different Thread Block and Stack Size Configurations


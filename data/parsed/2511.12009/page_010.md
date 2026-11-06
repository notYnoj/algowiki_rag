also implemented various optimization techniques to achieve extreme acceleration of the code.

Experimental results demonstrate that our algorithm can solve the 27-queens problem in just 28.4 days using 8 RTX 5090 GPUs, setting a new record for this problem. Compared with latest CUDA implementation, we achieved over 10x speedup based on same configuration. These provide substantial evidence for the effectiveness of our method. It is worth emphasizing that our implementation not only provides an exemplary case for GPU shared memory optimization, but also exhibits excellent portability and scalability. The concise and efficient code can be easily deployed across various NVIDIA GPU platforms, establishing a reliable performance benchmark for related research.

Although the methodology presented in this paper is applied to the N-Queens problem, the underlying optimization principles are not limited to this specific problem. Any depth- first search problem that satisfies the following conditions can achieve consistent acceleration through our approach:

1. It must be capable of generating a sufficiently large number of subproblems;<tbc>

2. The recursive algorithm can be transformed into an iterative implementation using a stack structure;<tbc>

3. The stack memory required per iteration exceeds one int, as bank conflicts only become possible when the data size exceeds one int.

Examples of applicable problems include sudoku[11], maze searching, combinatorial permutation problems, expression evaluation, and syntactic parsing. Such problems can be effectively accelerated by converting recursion into iteration and leveraging shared memory while avoiding bank conflicts.

However, when addressing larger problem instances (e.g., the 28-queens problem), the current approach still faces challenges with prohibitively long computation times, primarily due to the inherent exponential complexity of the problem. Future research could explore three potential directions for breakthroughs: 1) developing distributed multi-node collaborative computing frameworks; 2) designing robust fault- tolerant recovery mechanisms; 3) investigating more efficient parallel algorithmic paradigms; and 4) use optimization techniques in this paper to accelerate similar problems. We anticipate that future researchers will build upon this work to explore additional efficient solution methods for the N- queens and a series of similar problems, thereby advancing the field’s continued progress.

## References


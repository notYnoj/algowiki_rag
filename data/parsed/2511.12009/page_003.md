Although shared memory features extremely low access latency, improper usage may still result in suboptimal performance gains. From a hardware perspective, shared memory is partitioned into 32 banks, each with a 32-bit width, where addresses increment sequentially across banks as illustrated in Figure 2. Special attention must be paid to avoiding bank conflicts. When threads within a warp access shared memory, high bandwidth can be achieved if each thread accesses data from different banks, enabling parallel processing of all requests. However, if multiple threads access different addresses within the same bank, bank conflicts occur, forcing serialized access. In such cases, the hardware must split these accesses into multiple sequentially executed requests, consequently increasing latency. To fully exploit the low-latency advantage of shared memory, it is crucial to carefully design data structures and access patterns to ensure threads access different banks.

Another critical consideration when using shared memory is its limited capacity, typically only tens of kilobytes \[5\]. Thus, algorithms must be carefully designed to prevent data overflow. For the N-Queens problem, as N increases, the required stack space also grows, often exceeding the limit of shared memory size. This necessitates a trade-off between time and space efficiency to optimize performance.

## 2 Iterative Depth-First Search N-Queens

This section begins with an overview of three approaches for the N-Queens problem based on Somers algorithm. Somers algorithm employs state compression techniques and bitwise operation optimization, significantly reducing memory space requirements. The algorithm utilizes three 32-bit variables (**cur, left, and right**) to encode the occupied states of columns, diagonals, and anti-diagonals respectively, as illustrated in figure 3.

When a queen is placed at a valid position p in a new row, the corresponding column becomes prohibited. This column constraint is enforced by performing a bitwise OR operation between p and cur, effectively marking the column as occupied. Similarly, to restrict the left-diagonal attacks in the next row, a bitwise OR is applied between p and left, followed by a left shift by one bit. This propagates the left-diagonal threat along the \(\unknown\) direction. Likewise, for the right-diagonal constraints, a bitwise OR between p and right is performed, followed by a right shift by one bit. This propagates the right-diagonal threat along the \(\unknown\) direction. As for finding the valid positions in the next row, we only need to compute the bitwise OR of cur, left, and right, and then take the bitwise NOT to obtain all valid positions. The original Somers algorithm adopts a non-recursive implementation, which presents considerable comprehension challenges. To facilitate understanding, we first present a simplified recursive implementation shown in algorithm 1.

**Algorithm 1** Recursive Somers Algorithm

1: **def** n\_queens(N, cur, left, right, sum):

2: last = (1 \(\checkmark\) N) - 1

3: **if** cur == last:

4: sum += 1

5: return

6: valid\_pos = last \& ( ∼(cur|left|right))

7: **while** valid\_pos != 0:

8: p = valid\_pos \& (-valid\_pos)

9: valid\_pos -= p

10: cur = cur|p

11: left = (left|p) \(\checkmark\) 1

12: right = (right|p) \(\gg\) 1

13: n\_queens(N, cur, left, right, sum)

640
644
760
764
512
516
632
636
384
388
504
508
256
260
376
380
128
132
248
252
0
4
120
124
bank0
bank1
bank30
bank31

V

**Figure 2.** Shared memory bank partitioning and address mapping

**Figure 3.** Somers algorithm uses cur(blue), left(yellow), and right(green) to efficiently filter out invalid positions in 6- queens problem


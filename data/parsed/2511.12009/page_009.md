<tbc>Notably, compared with the state-of-the-art CUDA implementation \[7\], our solution achieves over 10\(\times\) performance improvement for the 24-queens problem under same configuration(8 A100 GPUs), and achieves over 26\(\times\) performance improvement under 8 RTX 5090 GPUs. This breakthrough conclusively validates the effectiveness of our proposed optimization methodology.

Moreover, we found that for N \(\ge\) 23, the computation time for a single problem increases by approximately 10 compared to the N-1 problem, a growth rate far exceeding previous estimates \[7\]. This value is very close to the ratio of the number of solutions for two adjacent N-Queens problems. Therefore, using this ratio to estimate the computation time for larger N-Queens problems is more reasonable.

For the 26-queens problem, we successfully calculated the number of solutions under 8 RTX 5090 GPUs in **2.5** days. To date, the only known attempt to solve the 26-queens problem was made by Preußer et al., who successfully computed the solution using an FPGA in about 9 months. In contrast, our method achieves the same result over 100 times faster than their approach <sup>7</sup>.

For the 27-queens problem, we have two options: Configuration 2 pre-placing queens in first 7 rows, or Configuration 1 pre-placing queens in first 6 rows. We use 24-queens problem to verify which option is faster under 8 RTX 5090 GPUs. Option 1 finishes in 2301 seconds, and option 2 finishes in 2531 seconds. So we use option 1 to calculate the solution count. The estimated computation time on 8 RTX 5090 GPUs would be approximately 28 days = 2.5 days \* 10.52 (27-queens solution count/26-queens solution count) \* 1.04 (option 1 is<tbc>

<tbc>4% slower than configuration for solving 24-queens in figure 4). The computation was successfully completed in 28.4 days, a landmark validation that not only conquered the daunting challenge of the 27-queens problem but also demonstrated a remarkable alignment with our initial time projection. The runtime log is shown above. According to the log, there remains a notable disparity in the completion times across GPUs, confirming that the current task partitioning strategy has not yet achieved optimal load balancing for Larger N.

Regarding the unsolved 28-queens problem, the previously leading CUDA implementation was estimated to require over two decades to solve it, while even Preußer’s FPGA-based approach would have demanded more than a decade. In contrast, our method can solve 28-queens in approximately 11 months under the 8 RTX 5090 GPU configuration, if scaled to 64 RTX 5090 GPUs, the computation period can reduced to around 50 days. Notably, the 28-queens problem is likely the last instance where the solution count can be stored using the int64 data type. Larger N-queens problems will require support for the int128 data type.

## 5 Conclusion

This paper presents an efficient CUDA-based parallel algorithm for accurately counting solutions to the N-queens problem. By redesigning the implementation of Somers algorithm, we innovatively developed an iterative depth-first search (DFS) version that incorporates extreme stack space compression to fit entirely within GPU shared memory. Notably, we proposed a bank-conflict-free shared memory access pattern that effectively resolves the memory access bottleneck inherent in conventional implementations. Furthermore, we<tbc>

<sup>7</sup>Preußer’s result is verified by a supercomputer in about one month, it’s too expensive, so just ignore it.

\begin{tabular}{cc}
\multicolumn{2}{c}{**Runtime Log for 27-Queens**} \\
\[2025-08-18 10:16:52.040\] & Use 9287.60ms to generate 453688251 subproblems! \\
\[2025-08-18 10:16:53.728\] & gpu \[0\] start job, with 90737656(0.20) subproblems. \\
\[2025-08-18 10:16:53.833\] & gpu \[4\] start job, with 49905708(0.11) subproblems. \\
\[2025-08-18 10:16:53.835\] & gpu \[1\] start job, with 68053240(0.15) subproblems. \\
\[2025-08-18 10:16:53.838\] & gpu \[7\] start job, with 45368815(0.10) subproblems. \\
\[2025-08-18 10:16:53.842\] & gpu \[5\] start job, with 49905708(0.11) subproblems. \\
\[2025-08-18 10:16:53.847\] & gpu \[6\] start job, with 45368828(0.10) subproblems. \\
\[2025-08-18 10:16:53.853\] & gpu \[2\] start job, with 54442588(0.12) subproblems. \\
\[2025-08-18 10:16:53.860\] & gpu \[3\] start job, with 49905708(0.11) subproblems. \\
\[2025-09-10 15:25:18.245\] & gpu \[1\] finish job. \\
\[2025-09-10 19:45:56.094\] & gpu \[3\] finish job. \\
\[2025-09-10 22:29:02.491\] & gpu \[2\] finish job. \\
\[2025-09-12 00:05:49.185\] & gpu \[6\] finish job. \\
\[2025-09-12 08:07:13.997\] & gpu \[0\] finish job. \\
\[2025-09-13 05:31:21.437\] & gpu \[4\] finish job. \\
\[2025-09-13 08:33:48.516\] & gpu \[7\] finish job. \\
\[2025-09-15 20:15:04.518\] & gpu \[5\] finish job. \\
\[2025-09-15 20:15:07.472\] & cuda 27 queens result 234907967154122528, calc time: \[2455104768.00ms\] \\
\end{tabular}


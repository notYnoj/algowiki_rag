## 1.2 History

Approximation algorithms for balanced vertex separators have a long history. First, it should be noted that there is a standard reduction from the balanced vertex separator problem to the (weighted) balanced directed edge separator problem based on vertex-splitting, preserving approximation ratios up to constants. For papers that study balanced directed edge separators directly, we will only discuss their implications for vertex separators.

Polynomial-time _O_(log_n_)-approximations date back to Leighton and Rao in 1988 \[30, 31\], and the best-known polynomial-time approximation ratio is \(O(\sqrt{logn})\), achieved independently by two groups at S 2005 \[18, 1\]. However, all of these algorithms are quite slow. The first requires up to _O(n_) solves of linear programs with a large number of constraints, while the latter two require up to _O(n_) solves of large semidefinite programs with a large number of constraints. The number of solves is because each problem is solving the related problem of _minimum-ratio vertex cut_: Roughly speaking, this refers to finding a set of vertices _S_ whose removal disconnects a small component _C_ of the graph, while minimizing |_S|/|C_|.

Progress on fast approximation algorithms with polylogarithmic approximation ratios has been much slower, and often involves unusual tradeoffs. In 2007, Arora and Kale presented an _O_(log_n_)- approximation using \(\widetilde{O}(1)\) strongly-polynomial maximum flow computations \[3\], and hence runs in \(\widetilde{O}(m^{1.5})\) time for a graph with _m_ edges. It should be noted that their algorithm does very much require strongly-polynomial maximum-flow, and does not admit an immediate replacement: The bit-complexity of the inputs to their flow problem is polylogarithmic _only_ if they are represented with floating point arithmetic. This prevents an immediate application of almost-linear time maximum flow \[9\], which applies for integer inputs of polynomial magnitude. That said, we think it is feasible that a slightly-modified form of their algorithm could be made to appropriately handle bit-complexity. This would require more work. Arora and Kale also presented an \(O(\sqrt{logn})\)- approximation running in \(\widetilde{O}(n^2+m^{1.5})\) time using multicommodity flow.

Since then, there have been a number of alternative results. In 2010, Louis \[35\] posted a preprint claiming to attain a polylogarithmic approximation in a polylogarithmic number of maximum flow computations using a "cut-matching game". Unfortunately, the details of this proof were never published. However, if the suggested algorithm does work, it does at least appear that it would not require any extra care for handling bit-complexity.

In 2019, Brandt and Wattenhofer \[5\] presented an algorithm with an alternative approximation guarantee: For a graph admitting a balanced 2/3-separator of size OPT, their algorithm produces a separator of size \(\widetilde{O}(OPT^2)\) in time \(\widetilde{O}(OPT^3m)\). This is useful for graphs with particularly small separators.

\begin{tabular}{ccccc}
**Separator Size** & **Running Time** & **Year** & **Ref** & **Notes** \\
\(O(\mathrm{OPT}\cdot\mathrm{log}n)\) & _O(n_) large LP solves & 1988 & \[30, 31\] & \\
\(O(\mathrm{OPT}\cdot\sqrt{\mathrm{log}n})\) & _O(n_) large SDP solves & 2005 & \[18, 1\] & Best-known polynomial-time approximation ratio. \\
\(O(\mathrm{OPT}\cdot\mathrm{log}n)\) & \(\widetilde{O}(m^{1.5})\) & 2007 & \[4, 3\] & Uses \(\widetilde{O}(1)\) strongly-polynomial max-flows. \\
\(O(\mathrm{OPT}\cdot\sqrt{\mathrm{log}n})\) & \(\widetilde{O}(n^2+m^{1.5})\) & 2007 & \[4, 3\] & ... \\
\(\widetilde{O}(\mathrm{OPT})\) & \(\widetilde{O}(m^{1+o(1)})\) & 2010 & \[35\] & **Proof missing.** \\
\(\widetilde{O}(\mathrm{OPT}^2)\) & \(\widetilde{O}(\mathrm{OPT}^3m)\) & 2019 & \[5\] & ... \\
\(O(\mathrm{OPT}\sqrt{\mathrm{log}n/\varepsilon})\) & \(O(n^{1+O(\varepsilon)}m^{1+o(1)})\) & 2024 & \[28\] & Uses \(\widetilde{O}(n^{1+\widetilde{O}(\varepsilon)})\) strongly-polynomial max-flows. \\
\(O(\mathrm{OPT}\sqrt{\mathrm{log}n/\varepsilon})\) & \(O(n^{\widetilde{O}(\varepsilon)}m^{1+o(1)})\) & Ours & & Works for any \(\varepsilon\in[1/\Theta(\mathrm{log}n),\Theta(1)]\). \\
\end{tabular}

2: Previous pseudo-approximation algorithms for the balanced vertex separator problem. OPT denotes the size of the smallest \(\frac{2}{3}\)-balanced vertex separator. The notation \(\widetilde{O}\) hides polylogarithmic factors.


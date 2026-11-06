<tbc>of work and the number of global-memory accesses, we restricted the candidates to tile widths satisfying \(m=\lceil R/T\rceil\le 16\) to avoid excessive rescanning.

To reduce the influence of temporary delays and execution-time variability, we performed multiple independent measurement runs for each condition. In each run, several warm-up executions preceded the measurements; the median of the measurements was used as the representative value for that run, and the median of the representative values over all runs was used as the final representative value. Because GPU clock frequencies and system conditions may differ between runs, this aggregation reduces the effect of a temporary fluctuation in any one run.

We use host-side wall-clock time to evaluate the total cost of a single sorting operation. The measured interval begins with allocation of algorithm-specific workspace and ends after the GPU sorting operation has completed and the workspace has been deallocated. Allocation of the input and output arrays is common to all methods and is therefore excluded.

We first compared the prefix-maximum method in Algorithm 3 with the binary-search method over local CDFs used in Algorithm 7, in order to examine the performance characteristics of the output- generation method used by RT-CDF. The two methods shared the same procedure for constructing a histogram from the input. The binary-search method then constructed a local CDF for every tile and computed tile offsets, whereas the prefix-maximum method constructed a CDF for the complete range; each method subsequently performed its own output-generation procedure. Thus, this experiment compares the total sorting time, including the CDF construction required by each method, rather than only the output-generation kernels.

Because the performance of both methods varies with tile width, we measured every feasible tile-width candidate for every combination of range size, input size, and input distribution. For each method, the minimum time over the tile-width candidates was taken as the execution time for that condition. This compares the best performance obtainable by each method without fixing a tile width that might favor or disadvantage one of them. Figure 1 shows the results. We define

\(\rho=\frac{\text{minimum execution time of the prefix-maximum method}}{\text{minimum execution time of the binary-search method}}.\)

The binary-search method is faster when \(\rho>1\), whereas the prefix-maximum method is faster when \(\rho<1\). Each cell in the figure shows \(\rho\) for a particular range size _R_, input size _n_, and input distribution. The displayed values are rounded to two decimal places.


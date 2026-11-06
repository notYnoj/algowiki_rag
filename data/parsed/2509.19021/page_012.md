1. **Performance at Small Scales:** At small input sizes (_n_=1,000), Introsort (40.7 \(\mu\)s) reigns supreme, significantly outperforming all radix-based variants (\(>120\mu\)s). This validates the theoretical initial startup costs associated with non-comparison sorting (buffer allocation, frequency counting) which only amortize at larger scales. This observation establishes the lower bound of the crossover region where simpler comparison sorts are preferable. However, we also notice that despite theoretical proof suggesting a better performance derived from (_k\<n_log<sub>2</sub>_n_) condition resulting in _n\>_245 for 64 bit integer, performance gains were realised only in the input range exceeding 10,000. This delay is caused due to initialization of overhead cost while implementing non-comparison sorting algorithms.<tbc>

2. **Large-Scale Supremacy of Non-comparison Sorting:** For large datasets (_n_=1,000,000), BNRS (154.1 ms) establishes a clear lead over Introsort (173.1 ms). Notably, at _N_=100,000, the performance was comparable (13.8 ms vs 14.6 ms), but the gap widens at 10<sup>6</sup>, confirming the asymptotic advantage of the non-comparison approach _O(n_) over the comparison-based one _O(n_log_n_) as _n_ scales very large.<tbc>

3. **Analysis of Adaptive Approaches (AFS vs SP-LSD):** AFS (137.8 ms) outperformed the BNRS (154.1 ms), leveraging data skew to skip rounds. However, it (AFS) trailed SP-LSD (106.0 ms) by a wide margin. Despite being ‘adaptive’, AFS remains constrained by the predicted ‘Fat Bucket’ problem and ‘cache inefficiency’, thrashing associated with random-access partitioning. This suggests that while recursive MSD is viable, the overhead of its specific partitioning mechanism limits its potential compared to the linear scanning model of SP-LSD.<tbc>

4. **SP-LSD Dominance and Boundaries:** SP-LSD (106.0 ms) demonstrates a commanding performance advantage, establishing itself as the optimal choice. In relation to the competitors at _n_=10<sup>6</sup>:<tbc>

- It is 1.63x faster than Introsort, validating the efficiency of radix approaches for this domain.<tbc>

**-** It is 1.45x faster than BNRS, proving that the overhead of stable partitioning is fully amortized by the reduction in sorting volume (_p_).

\begin{tabular}{cccccc}
**Parameter** & **Introsort** & **AFS** & **BNRS** & **SP-LSD** & **Input Size** \\
Average Time (ns) & 40,657 & 137,911 & 200,452 & 122,265 & \multirow{3}{*}{1,000} \\
CPU Time (ns) & 40,647 & 137,908 & 200,423 & 122,253 & \\
Repetitions & 14,381 & 5,116 & 3,480 & 5,746 & \\
Average Time (ns) & 1,133,385 & 1,260,366 & 1,313,428 & 887,678 & \multirow{3}{*}{10,000} \\
CPU Time (ns) & 1,132,968 & 1,260,277 & 1,313,279 & 887,553 & \\
Repetitions & 616 & 553 & 532 & 778 & \\
Average Time (ns) & 14,636,518 & 13,725,100 & 13,829,398 & 10,452,841 & \multirow{3}{*}{100,000} \\
CPU Time (ns) & 14,628,757 & 13,722,726 & 13,826,997 & 10,450,737 & \\
Repetitions & 48 & 51 & 50 & 67 & \\
Average Time (ns) & 173,054,556 & 137,778,640 & 154,112,030 & 105,962,703 & \multirow{3}{*}{1,000,000} \\
CPU Time (ns) & 173,046,416 & 137,762,253 & 153,749,641 & 105,946,853 & \\
Repetitions & 4 & 5 & 5 & 6 & \\
\end{tabular}

6: Benchmark results for Introsort, American Flag Sort (AFS), Base-_n_ Radix Sort (BNRS), and SP-LSD on skewed datasets.


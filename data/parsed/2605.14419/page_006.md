### B. Best Case

The classical recurrence is given by,<tbc>

\(T(n)=kT(\frac{n}{k})+n\)

<tbc>where \(k=\sqrt{n}\) is fixed across recursion levels. Recursion Depth (_d_):<tbc>

\(\frac{n}{k^d}=1\Rightarrow k^d=n\Rightarrow d=\mathrm{log}_kn\Rightarrow d=\mathrm{log}_{\sqrt{n}}n=2\)

<tbc>Here, work per level is \(\Theta(n)\) Therefore, total cost

\(T(n)=(\mathrm{depth})\times(\mathrm{workperlevel})=2\cdot n=\Theta(n)\)

## IV. Results and Discussion

### A. Experimental Setup

The experiments are carried out on a system equipped with an 11_<sup>th</sup>_ Gen Intel Core _i_5-1155_G_7 processor (Tiger Lake microarchitecture) operating at a base frequency of 2.50_GHz_, coupled with 8_GB_ of Dual-Channel RAM. The system operated under the Windows environment. To ensure a fair and competitive, all algorithms are implemented in _C_++ and compiled using the _GCC_ 14.2.0 compiler. The compilation utilized the C++ 20 standard (-_std=c_++20) with aggressive optimization flags enabled (-_Ofast_, -_flto_, -_march=native_). Microarchitectural behavior is analyzed using Intel VTune Profiler 2025.7 \[25\]. The default collection settings are used to obtain the top-down pipeline breakdown, including metrics such as Retiring, Front-End Bound, Back-End Bound, and Bad Speculation \[26\]. Profiling is conducted at the application level, where each sorting algorithm is executed as a separate task.

### B. Microarchitecture Analysis

To better understand the performance of zSort beyond its theoretical complexity, a detailed analysis of the CPU pipeline is performed. This analysis shows that the performance of sorting algorithms on modern superscalar processors depends on how the instruction stream interacts with key hardware components such as the Branch Target Buffer (BTB), Translation Lookaside Buffer (TLB), and the cache hierarchy.  III presents the microarchitectural performance metrics observed for different sorting algorithms.

\(\bullet\) Instruction-Level Efficiency (IPC (Instructions Per Cycle) and Retiring): The proposed zSort shows strong instruction-level efficiency, achieving an IPC of 1.44. This value is better than traditional comparison- based algorithms such as Timsort (0.93) and _std::sort_ (0.58), and it also outperforms other non- comparison methods like Radixsort (1.25). Among all evaluated techniques, Pdqsort achieves the highest IPC, placing zSort second. However, Pdqsort does not provide stability. One of the reasons for this efficiency is the simplicity of zSort’s inner loops. The loops are straightforward and avoid complex loop-carried data dependencies. Because of this, modern compilers can effectively apply auto-vectorization using SIMD, allowing more operations to be executed per clock cycle. As a result, zSort is able to utilize CPU execution resources efficiently and maintain a high level of instruction-level parallelism. This behavior is also reflected in the retiring metric, where zSort achieves 46.70%, the highest among all stable algorithms. Although Pdqsort records a higher retiring value of 52.40%, it executes \(69\times 10^9\) instructions, while zSort executes only \(33.06\times 10^9\) instructions. In comparison, Radixsort (28.60%) and Spreadsort (32.10%) are less efficient despite being non-comparison methods. The optimized version of Radixsort (Skasort) shows a retiring percentage similar to zSort. Overall, these results indicate that zSort reduces wasted cycles and performs a larger portion of useful computation.<tbc>

\(\bullet\) Frontend and Speculation Behavior: zSort maintains a front-end bound of 18.30%, which is comparable to both comparison-based and non-comparison-based algorithms. This indicates that the instruction fetch and decode stages are not major bottlenecks, and the algorithm is able to maintain a steady flow of instructions to the execution pipeline. zSort also shows a bad speculation rate of 19.70%, which is better than Radixsort (39.90%) and Spreadsort (46.30%). Fewer branch mispredictions reduce pipeline stalls and improve overall execution efficiency. Compared to unstable comparison-based methods such as Pdqsort (52.40%), zSort provides a more predictable execution pattern while also maintaining stability. Unlike comparison-based sorting algorithms, zSort uses a deterministic mapping function _h(s<sub>i</sub>_) to directly<tbc>

\begin{tabular}{ccccccccccc}
\multirow{2}{*}{Metric} & \multicolumn{4}{c}{Comparison (Stable)} & \multicolumn{2}{c}{Comparison (Unstable)} & \multicolumn{2}{c}{Non-Comparison (Unstable)} & \multicolumn{2}{c}{Non-Comparison (Stable)} \\
 & Timsort & std::stable\_sort & flat\_stable\_sort & Spinsort & std::sort & Pdqsort & Skasort & Spreadsort & Radixsort & zSort \\
IPC & 0.93 & 0.69 & 1.03 & 0.82 & 0.58 & 2.15 & 1.36 & 1.26 & 1.25 & 1.44 \\
Frontend & 20.90% & 20.50% & 17.90% & 21.20% & 20.70% & 14.20% & 18.50% & 8.70% & 6.10% & 18.30% \\
Bad Spec & 55.00% & 55.20% & 53.60% & 55.30% & 55.90% & 25.70% & 23.10% & 46.30% & 39.90% & 19.70% \\
Retiring & 18.70% & 18.90% & 22.60% & 18.90% & 17.70% & 52.40% & 46.20% & 32.10% & 28.60% & 46.70% \\
Backend & 5.50% & 5.40% & 5.90% & 4.60% & 5.70% & 7.80% & 12.20% & 12.90% & 25.40% & 15.30% \\
Memory Bound & 8.70% & 9.00% & 9.10% & 8.00% & 10.10% & 11.20% & 19.10% & 27.60% & 35.80% & 24.50% \\
L1 Bound & 1.70% & 0.20% & 3.20% & 3.00% & 3.60% & 0.20% & 0.00% & 7.40% & 0.00% & 3.60% \\
L2 Bound & 0.20% & 0.30% & 0.60% & 0.40% & 2.10% & 5.00% & 10.50% & 3.10% & 7.40% & 8.90% \\
L3 Bound & 0.90% & 2.20% & 1.30% & 1.10% & 0.90% & 0.30% & 1.00% & 4.70% & 4.40% & 2.00% \\
DRAM Bound & 5.80% & 6.20% & 4.00% & 3.40% & 3.50% & 5.70% & 6.70% & 12.40% & 12.90% & 6.00% \\
TLB Miss % & 0.57% & 0.68% & 0.34% & 0.39% & 0.21% & 0.15% & 0.14% & 2.11% & 1.58% & 2.94% \\
\end{tabular}

TABLE III

Microarchitecture Analysis


<tbc>**Break-Even Analysis:** We require \(T_\text{SP-LSD}^\text{uniform}<T_\text{BNRS}\). Following the summation and simplification (note \(T_\text{BNRS}=R\cdot\alpha\cdot n\)):<tbc>

\((\alpha+\beta)\left[\frac{R^2-R-2}{2R}\right]<\alpha\left(\frac{R^2-R-1}{R}\right)\)

<tbc>Substituting \(\alpha=c\beta\) and solving for _c_:<tbc>

\(c>\frac{R^2-R-2}{R^2-R}=1-\frac{2}{R(R-1)}\) (1)

<tbc>Solving for _R_,<tbc>

\(R<R_\text{max}(c)=\frac{1+\sqrt{1+\frac{8}{1-c}}}{2}\) (2)

#### 5.6 Observations:

-  3 establishes the minimum hardware cost ratio required for viability as the number of rounds increases, confirming effectiveness for all standard integer widths where _R\>_2.<tbc>

**-**  4 demonstrates the algorithm’s robustness against poor hardware efficiency, defining the maximum sortable magnitude (_n<sup>R</sup>_) sustainable when partitioning is more expensive than sorting.

### 6 Experimental Evaluation and Results

To validate the efficiency of SP-LSD, we conducted both formal theoretical operational cost analysis and experimental benchmark results. We compare the performance of the SP-LSD against Base-_n_ Radix Sort (BNRS), standard Base- 10 Radix Sort (Baseline Radix Sort) and optimized comparison-based sort from the C++ standard library, `std::sort`.

\begin{tabular}{cc}
 & **Min. Cost Ratio** \\
**Rounds R** & (_c\>..._) \\
3 & 0.667 \\
4 & 0.833 \\
8 & 0.964 \\
16 & 0.992 \\
32 & 0.998 \\
\end{tabular}

\begin{tabular}{ccc}
**Cost Ratio** & **Upper Bound** & **Maximum** \\
\((c=\alpha/\beta)\) & (_R\<..._) & **Integer Value** (_k_) \\
0.95 & 6.85 & _n_<sup>6</sup>-1 \\
0.90 & 5.00 & _n_<sup>4</sup>-1 \\
0.85 & 4.19 & _n_<sup>4</sup>-1 \\
0.80 & 3.70 & _n_<sup>3</sup>-1 \\
0.75 & 3.37 & _n_<sup>3</sup>-1 \\
0.70 & 3.13 & _n_<sup>3</sup>-1 \\
0.67 & 3.01 & _n_<sup>3</sup>-1 \\
\end{tabular}

3: Minimum Cost Ratio (_c_) Required for SP-LSD Viability.

4: Maximum Feasible Rounds (_R_max) for Suboptimal Hardware (_c\<_1).


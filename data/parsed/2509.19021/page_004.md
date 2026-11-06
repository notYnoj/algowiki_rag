### 3 Analysis of Non-Comparison and Comparison Sorting Algorithms

In this section, we compare the time complexities of standard comparison-based sorting algorithms \[1\] and Base-_n_ Radix Sort (BNRS) to determine boundary of input size from which performance of non-comparison sorting algorithm would outperform comparison sorting algorithms.

1. **Complexity of Standard Comparison-Based Sorting Algorithms:** Independent of the specific implementation, the lower bound for comparison- based sorting algorithms is generally: _T_<sub>comp</sub>=_O(n_log_n_) where _n_ is the number of elements to be sorted and log_n_ is typically log<sub>2</sub>_n_. For practical purpose and benchmarking, we use _Introsort_ \[5\] which is highly efficient, hybrid and stable sorting algorithm designed for practical, real-world data. Details on Introsort is provided in Appendix.<tbc>

2. **Asymptotic Crossover:** For BNRS (and SP-LSD) to outperform comparison- based sorting algorithms, it’s complexity must be asymptotically smaller, satisfying the condition: \(O(nlog_nk)<O(nlogn)\Longrightarrow log_nk<log_2n\). Con verting to natural logarithm (ln): \(\frac{lnk}{lnn}<\frac{lnn}{ln2}\). This gives: \(lnk<\frac{(lnn)^2}{ln2}\) . Since, \(\frac{(lnn)}{ln2}=log_2n\), we get \(lnk<lnn\cdot log_2n\). Exponentiating by _e_, \(k<e^{(lnn)\cdot log_2n}\). Since _e_ln_n=n_, we get _k\<n_log<sub>2</sub>_n_. This inequality, _k\<n_log<sub>2</sub>_n_, defines the condition between _n_ and _k_ under which BNRS and SP-LSD offer a theoretically superior time complexity compared to comparison-based sorting algorithms.<tbc>

3. **Practical analysis of the relation** _k\<n_log<sub>2</sub>_n_**:** We are required to store elements of the dataset in common datatypes. Since we are utilising these datatypes for storing elements into memory, the maximum possible value that can be stored in the datatype becomes our _k<sub>max</sub>_. See  1 for the crossover input value for different datatypes. A sample mathematical calculation for obtaining the crossover value for the datatype LongLong is discussed in Appendix.

### 4 Optimised Approach - SP-LSD Radix Sort

Stable Partition - Least Significant Digit Radix Sort or SP-LSD is an optimization algorithm built on the principles of BNRS which simulates the division of

\begin{tabular}{cccc}
**Datatype** & **Bit-Width** & **Max Value (_k<sub>max</sub>_)** & **Crossover (_n\>_)** \\
Int (Signed) & 32-bit & 2<sup>31</sup>-1 & 47 \\
Long Long (Signed) & 64-bit & 2<sup>63</sup>-1 & 245 \\
BigInt / UUID & 128-bit & 2<sup>127</sup>-1 & 2,466 \\
\end{tabular}

1: Practical Crossover values (_n_) for standard datatypes.


_bsort_ as described in this paper, i.e. with no major modifications or optimizations, was implemented in C++ and was compared with the STL implementation of introsort (`std::sort`), Boost library implementation of spread sort (`boost::sort::spreadsort`), and an optimized implementation of radix sort (`ska\_sort`) in a 64-bit GNU/Linux environment with 48 GB of RAM and an Intel i5-8350U processor. The list of word size depending on the data type can be found in  II. To mitigate the impact of external factors like transient system load, and to ensure statistical significance and consistency, GoogleBenchmark v1.8.0 was used. Compilation was done using gcc 12.3.1 with optimization flag `-03`.

The analysis was performed on the data collected from various tests where each test case consisted of sorting an array of a certain size in \(\{10^5,10^6,10^7,10^8,10^9,5\cdot 10^9\}\) and a certain data type in {`char`, `short`, `int`, `long long`, `float`, `double`}, using all four algorithms previously mentioned. The source code, including implementation, testing, and the LATEXsources for this manuscript, are publicly available at https://benjaminguzman.dev. Results comparing data type and running time are found in Figures 5 and 6.

From Figures 5 and 6 it can be seen that _bsort_ demonstrates consistent linear scaling. As predicted by the analysis of its runtime in the previous section, the execution time grows linearly with the number of elements _n_. The performance gap between bsort and comparison-based introsort remains relatively stable as _n_ increases, confirming that the bitwise partitioning overhead does not degrade disproportionately for large datasets.

Results also show that when the bit-depth is shallow, _bsort_ consistently outperforms introsort, but when it is deep, its relative performance decreases. This is a direct consequence<tbc>

<tbc>of the _w_ factor, as more recursive passes are required to settle the final order.

Theoretically, bsort possesses an asymptotic advantage over comparison-based algorithms in specific regimes, as its runtime behavior is bound by _O(wn_) and that of efficient

\begin{tabular}{ccccc}
**Algorithm** & **Runtime** & **Memory**<sup>+</sup> & **In-place** & **Comp.** \\ Introsort\* & _O(n_log(_n_)) & _O_(log(_n_)) & Yes & Yes \\ Spreadsort\* & \(O(n(\frac{k}{s}+s))\) & _O(n_) & No & No \\ ska\_sort\* & _O(nw_) & \(O(d\cdot k)\) & Yes & No \\ Quicksort & _O(n_log(_n_)) & _O_(log(_n_)) & Yes & Yes \\ bsort & _O(nw_) & _O(w_) & Yes & No \\ \end{tabular}

\begin{tabular}{cc}
**Data type** & **Word size** \\ `char` & 8 \\ `short` & 16 \\ `int` & 32 \\ `long long` & 64 \\ `float` & 32 \\ `double` & 64 \\ \end{tabular}


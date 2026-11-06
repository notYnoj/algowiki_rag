8 summarizes the conditions of the main evaluation.

The uniform and normal inputs were generated in the same manner as in the preliminary evaluation. For all-equal inputs, every element was set to zero. The range supplied to the algorithms remained _R_, as for the other distributions; it was not changed to _R_=1 even though only one distinct value actually occurred. This evaluates performance when all values are concentrated at one point while the declared range remains fixed.

Because the output-generation method of Kolonias et al. assigns work by value, concentrating occurrences on one value creates a workload imbalance \[5\]. The all-equal input used here is therefore an unfavorable condition for that output-generation method.

The aggregation of measurements and the measured interval were the same as in Section 4.1. If an execution time exceeded 1000ms, measurements for larger input sizes with the same range _R_ and input distribution were terminated.

To investigate the causes of performance changes in RT-CDF, Section 4.4 uses an additional timing experiment on RT-CDF alone. This experiment fixed the input size at _n_=10<sup>8</sup> and used the same 12 range sizes, three input distributions, and tile widths from  6 as the main evaluation. The number of measurements and their aggregation also followed the main evaluation: three independent runs were performed, each containing 30 measurements after 10 warm-up executions; the median within each run was used as its representative value, and the median of the three run representatives was used as the final value. CUDA events recording positions in the GPU execution stream were placed before and after each processing stage, and elapsed times between event pairs were measured. The measured stages were histogram-array initialization, histogram construction, local-CDF construction, tile-offset construction, and output generation.<sup>∗4</sup>

<sup>∗4</sup> The implementation uses `cudaEventRecord` and `cudaEventElapsedTime` from the CUDA Runtime API.

\begin{tabular}{cc}
Item & Setting \\
Input & 32-bit integer array satisfying \(0\le A_i<R\) \\
Range size & _R_=2<sup>7</sup>,2<sup>8</sup>_,...,_2<sup>18</sup> \\
Input size & \(10^6,2\times 10^6,\dots,9\times 10^6\), \(10^7,2\times 10^7,\dots,9\times 10^7\), \(10^8,2\times 10^8,\dots,10^9\) \\
Input distribution & Uniform, normal (mean (_R_-1)/2, standard deviation 0.125_R_), and all-equal \\
Repetitions & Three independent runs per condition; 30 measurements after warm-up in each run \\
Representative value & Median of 30 measurements per run, followed by the median of the three run medians \\
Measured time & Host-side wall-clock time including allocation and deallocation of method-specific workspace \\
Termination condition & For a fixed range and distribution, omit larger input sizes after the execution time exceeds 1000ms \\
\end{tabular}

8: Measurement conditions for the main evaluation


subsection and the main evaluation in Section 4.2 were conducted in the same environment, shown in  3. One KiB is 1024 bytes.

4 summarizes the conditions of the preliminary evaluation.

We used uniform and normal input distributions. For the uniform distribution, each element was generated uniformly at random from the integer interval \[0_,R_-1\]. For the normal distribution, a real value was generated from a normal distribution with mean (_R_-1)/2 and standard deviation 0.125_R_, and was rounded to the nearest integer. A rounded value outside \[0_,R_-1\] was clipped to 0 or _R_-1.

Because every entry of a tile-local histogram and local CDF is a 32-bit integer, a thread block requires at most 4_T_ bytes of shared memory to process a tile. For the largest candidate tile width, _T_=24576, this amount is 4_T_=96 KiB, which is below the 99-KiB opt-in shared-memory limit per thread block shown in  3. For each range size _R_, we evaluated only candidates satisfying \(T\le R\) and whose shared- memory requirement did not exceed the opt-in limit per thread block. Moreover, because increasing the number of tiles _m_ causes the input array to be scanned for every tile, thereby increasing both the amount<tbc>

\begin{tabular}{cc}
Item & Setting \\
GPU & NVIDIA GeForce RTX 4090 \\
Number of SMs & 128 \\
Compute Capability & 8.9 \\
CUDA Toolkit & 13.0.1 \\
Default shared-memory limit per thread block & 48 KiB \\
Opt-in shared-memory limit per thread block & 99 KiB \\
Shared-memory limit per SM & 100 KiB \\
\end{tabular}

\begin{tabular}{cc}
Item & Setting \\
Input & 32-bit integer array satisfying \(0\le A_i<R\) \\
Range size & _R_=2<sup>7</sup>,2<sup>8</sup>_,...,_2<sup>18</sup> \\
Input size & 10<sup>6</sup>, \(2\times 10^6\), \(5\times 10^6\), 10<sup>7</sup>, \(2\times 10^7\), \(5\times 10^7\), 10<sup>8</sup>, \(2\times 10^8\), \(5\times 10^8\), 10<sup>9</sup> \\
Input distribution & Uniform distribution, Normal distribution (mean (_R_-1)/2 and standard deviation 0.125_R_) \\
Candidate tile widths & 128, 256, 512, 1024, 2048, 4096, 6144, 8192, 12288, 16384, 20480, 24576 \\
Candidate constraints & \(T\le R\), \(\lceil R/T\rceil\le 16\), and shared-memory use not exceeding the per-block limit \\
Measurements & Three independent runs per condition; 10 measurements after warm-up in each run \\
Representative value & Median of 10 measurements per run, followed by the median of the three run medians \\
Measured time & Host-side wall-clock time including allocation and deallocation of method- specific workspace \\
\end{tabular}

3: Experimental environment

4: Preliminary-evaluation conditions for selecting the implementation


<tbc>Numba: quick sort, merge sort, heap sort, Tim sort, and a custom in-place implementation of radix sort with each reported result a statistical average of 10 runs \[51\]. Analysis of the effect of tuning batch size on latency and memory usage is performed on different data set sizes. Comparison of FractalSortCPU to the state of the art involves data sets of \(n\in\{2^{10}\rightarrow 2^{31}\}\).

### A. FractalSortCPU Experiment Test Bed

The experiment setup includes a random number generator which populates batches of keys loaded to CPU and processed as shown in Figure 2.

Although the keys are uniformly distributed, the histogram tree structure provides some robustness to skew since each key independently walks its own root-to-leaf path with no input bucketing. However, the counter width tapering scheme assumes approximately balanced subtrees where counter widths decrease as \(w_{c,l}=O(\lceil log(n)-l\rceil)\). Under heavy skew (e.g., Zipfian), subtree sizes may deviate from this assumption, and empirical evaluation across non-uniform distributions is left to future work.

### B. Latency Analysis

The latency curve for FractalSortCPU has sub-linear growth compared to the baselines and is 34% faster than the next best radix sort at _n_=2<sup>29</sup> as shown in Figure 3 and  II. FractalSortCPU demonstrates lowest latency at \(n\ge 2^{21}\). This speed-up is due to the reduced number of radix passes on compressed entries, with the bandwidth savings from histogram compression becoming apparent for large _n_.

### C. Memory Usage Analysis

The memory usage analysis shows a 7x higher footprint for FractalSortCPU for small data sets which remains approximately constant for \(n\le 2^{15}\), at which point radix sort has higher utilization. This is because the histogram size is dependent on _log(n_), and due to the histogram cache between batch updates creating a trade-off between memory and latency as shown in Figure 6. At _n_=2<sup>29</sup> FractalSort consumes 4,608 MiB ranking second after the in-place comparison sorts (keys 4_n_ + entry array 4_n_ + radix temp buffers ≈_n_ bytes), and 25% less than radix sort at 6,144 MiB. At _n_=2<sup>30</sup> FractalSort uses 9,216 MiB, maintaining the 25% memory advantage over radix sort as _n_ increases.

### D. Batch Size Optimization

Streaming the dataset in input order in batches of equal size for more efficient processing with respect to the sorting resources available demonstrates varying benefits regarding latency and memory utilization depending on how the batches are processed both serially and in parallel as shown in Figure 3 and Figure 4.

#### 1) Parallel Batch Processing:

Processing batches in parallel involves dedicating a thread to each batch on the limited CPU thread pool. Increasing the number of batches has minimal impact on latency and memory usage for most data sets with latency standard deviation<tbc>

\begin{tabular}{cccccc}
Algorithm & Quick

sort & Merge

sort & Heap

sort & Radix

sort & Fractal

sort \\
Latency (s) & 59.51 & 80.36 & -- & 8.38 & 5.53 \\
Memory (MiB) & \(4.10\times 10^3\) & \(4.10\times 10^3\) & -- & \(6.14\times 10^3\) & \(4.61\times 10^3\) \\
\end{tabular}

Keys0
L2
PO
Batch 1
Keys1
Batch i
Keys
Histogram,
L2
P1
Batch nb
Histogram
Keysn,
L2
Pn,
nb
LLC Cache
DRAM
CPU

200
180
160
140
120
Latency (s)
100
80
60
40
20
0
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
log(n)
quicksort
mergesort
heapsort
fractalsort
radix

Fig. 2. FractalSortCPU Multi-batch Test Bed _p_=16

TABLE II

SORT LATENCY (SECONDS) AND MEMORY USAGE (MiB) FOR _n_=2<sup>29</sup>_,p_=32 ON CPU WITH NUMBA

Fig. 5. FractalSortCPU Latency for _n_=2<sup>30</sup>_,p_=32


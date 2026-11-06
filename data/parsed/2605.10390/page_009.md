### E. Unit Throughput

The unit throughput is calculated as \(T_{unit}=\frac{n}{t\times n_c}\) where _t_ is the latency and _n<sub>c</sub>_ is the number of CPU cores (4 cores on 8 threads). FractalSortCPU has the highest unit throughput at \(n\ge 2^{26}\) growing to \(1\times 10^7\) keys/s, a 20% speed up over the second best radix sort at _n_=2<sup>30</sup> at _p_=32 as shown in Figure 9. State-of-the-art CPU-based Paradis \[6\] sorts 4_GB_ of _p_=16 data in 4.6_s_ on a 32-core Intel Xeon (E7-8837) processor for unit throughput \(14.59\times 10^6\) keys/s, while FractalSortCPU latency is 21.22_s_ at _b_=14 for \(25.30\times 10^6\) keys/s, a 73.4% speed up.

### F. FractalSortCPU on Large Datasets

For large data sets \(n\ge 2^{30}\) FractalSortCPU exhibits low latency _t_<sub>2<sup>30</sup></sub>=13.4s in contrast to the comparison sorts which demonstrate superlinear growth as shown in Figure 5. Memory usage increases linearly with _n_ at 9_n_ bytes, 25% lower than radix sort at 12_n_ bytes as shown in Figure 6. The better performance of FractalSortCPU at large _n_ is due to its latency and memory usage being primarily determined by histogram size which grows sublinearly in _n_ as _O_(2_<sup>p</sup>_log<sub>2</sub>(_n_)), determined by the counter variable width ≈log<sub>2</sub>(_n_) stored in each node as shown in Figure 6.

#### 1) Bandwidth Efficiency:

Following the bandwidth- efficiency analysis used in prior sorting work \[17\] \[54\], we define bandwidth efficiency as the ratio of actual throughput to total memory (DRAM) bandwidth consumed:

\(b_{eff}=\frac{T_{actual}}{B_{DRAM}}\) (1)

where _T<sub>actual</sub>_ is the sum of read and write throughput in bytes per second for _n_ keys of _p_ bits sorted in time _t_, and _B<sub>DRAM</sub>_ is the total DRAM traffic in bytes per second including all intermediate reads and writes. The ratio is dimensionless with higher values indicating more efficient use of memory bandwidth. Algorithms that require multiple passes over the data or store large intermediate structures have lower _b<sub>eff</sub>_ due to increased _B<sub>DRAM</sub>_.

FractalSortCPU is compared to state-of-the-art algorithms over a variety of data set sizes to explore on-chip and off-chip memory access and sort performance. The bandwidth efficiency of FractalSortCPU is significantly higher than the state of the art due to the small size of the compressed histogram which fits entirely on CPU LLC cache at _p_=16. Compared to state-of-the-art sorting algorithms, FractalSortCPU performs very favorably with a 6x increase in bandwidth efficiency compared to CPU \[6\], 3x compared to GPU \[17\] and 2.5x compared to FPGA \[10\] for 16GB data sets as shown in Figure 10.

## V. CONCLUSION AND RECOMMENDATIONS

FractalSortCPU introduces a histogram compression scheme demonstrating low latency and sublinear memory growth as dataset size increases. It performs better for large _n_, hence suited for large dataset processing where latency and memory usage are key concerns. Though in-place radix sort shows superior performance for medium datasets and comparison-based sorters for small datasets, FractalSortCPU scales more slowly for large datasets with 25% lower memory usage compared to radix sort at _n_=2<sup>29</sup>.

The key contributions of FractalSortCPU include a space- efficient fractal sorting algorithm, involving a precision-depth bound histogram tree of sparse counters, and a parallel merge operation that eliminates the need for data pre-processing and input partitioning. Caching of the histogram allows the sharing of merge tree between batches enabling the amortization of batch-switching costs as the number of batches increases with a 20% reduction in batch memory usage at _b_=20.

FractalSortCPU provides significant improvement over state-of-the-art sorting algorithms on CPU, GPU, and FPGA by 6x, 3x, and 2.5x in bandwidth efficiency on 512MB to 32GB data sets, a key benefit of using this algorithm, and demonstrates a 73.4% improvement in unit throughput compared to the state-of-the-art CPU algorithm Paradis as shown in Figure 9. This is because no input partitioning<tbc>

1.20E+07
1.00E+07
8.00E+06
Unit Throughput (keys/s/core)
6.00E+06
4.00E+06
2.00E+06
0.00E+00
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
log(n)
quicksort
mergesort
heapsort
timsort
radix
fractalsort

1
0.8
0.6
Bandwidth Efficiency
0.4
0.2
0
FractalSortCPU
FractalSortCPUA
Bonsai 8
Bonsai 32
PARADIS
HRS
SampleSort

Fig. 9. Unit Throughput for \(2^{10}\le n\le 2^{30}\)

Fig. 10. Bandwidth Efficiency for 16GB datasets (_p_=16) compared to Bonsai \[10\], Paradis \[6\], HRS \[17\] and SampleSort \[23\]


<tbc>\(\sigma\in 0.03s\rightarrow 0.38s\approx 6\%\rightarrow 12\%\) and memory standard deviation \(\sigma\in 3\times 10^{-6}\rightarrow 14\%\).

An exception is _n_=2<sup>25</sup> and _n_=2<sup>20</sup> which show significant 20% reduction in latency at _b_=6 and 20_KB_ reduction in memory _b_=2 respectively, as shown in Figure 3.

## 2) Serial Batch Processing:

Processing batches in serial is simpler with no thread creation overhead leading to lower latency for most data sets. Increasing the number of batches has moderate impact on latency for \(b\ge 2\), with latency standard deviation \(\sigma=0.54s\) across \(b\in 1\rightarrow 20\) at _n_=2<sup>29</sup>. Latency at _b_=1 is higher due to larger per-bin radix sort temporary buffers, dropping from 7.63_s_ to 5.35_s_ at _b_=2 for all \(n\neq 2^{28}\), averaging ≈5.6_s_ for \(b\ge 2\) with periodic variation as shown in Figure 7. Memory decreases monotonically from 2,612 MiB at _b_=1 to 2,074 MiB at _b_=20, a 20% reduction, with diminishing returns beyond _b_=10 as shown in Figure 8.

Latency for n = 226 > 229
Latency for n = 220 > 225
7.21
8.56
N=2^26 (min=0.63, a=0.03)
6.93
N=2^20 (min=0.01, a=2.70)
7
N=2^27 (min=1.30, a=0.08)
8
N=2^21 (min=0.03, a=0.00)
N=2^28 (min=2.64, a=0.21)
N=2^22 (min=0.05, a=0.01)
N=2^29 (min=5.18, a=0.73)
N=2^23 (min=0.09, a=0.01)
6
5.52
5.65
5.86
N=2^24 (min=0.17, a=0.01)
5.29
5.31
5.22
5.24
5.18
N=2^25 (min=0.33, a=0.03)
5
6
Latency (s)
Latency (s)
4
3.26
3.25
4
3.16
2.86
2.82
2.85
2.77
2.87
2.82
3
2.64
2
2
1.41
1.35
1.32
1.35
1.39
1.52
1.49
1
0.69
0.74
0.72
0.72
0.71
0.67
0.68
0.63
0.67
0.68
0.38
0.40
0.40
0.34
0.34
0.36
0.40
0.39
0.34
0.33
0
2
4
6
8
10
2
4
6
8
10
Batches (b)
Batches (b)
Memory for n = 226 > 229
Memory for n = 220 > 225
160
N=2^20 (min=0.008, a=18.192)
2500
N=2^21 (min=0.023, a=3.475)
140
N=2^22 (min=12.871, a=1.235)
N=2^23 (min=31.508, a=2.201)
2000
120
N=2^24 (min=63.676, a=4.532)
N=2^25 (min=130.562, a=8.953)
Peak Memory (MiB)
100
1500
N=2^26 (min=262.047, a=17.946)
Peak Memory (MiB)
80
N=2^27 (min=524.742, a=35.338)
N=2^28 (min=1049.648, a=70.996)
N=2^29 (min=2099.270, a=141.963)
60
1000
40
500
20
0
2
4
6
8
10
2
4
6
8
10
Batches (b)
Batches (b)

14,000
12,000
10,000
Memory Usage (MiB)
8,000
6,000
4,000
2,000
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
radix
fractalsort

Fig. 3. FractalSortCPU Latency and Memory for Number of Parallel Batches \(b\in 1\rightarrow 10\)

Fig. 6. FractalSortCPU Memory Usage for \(n=2^{10}\rightarrow 2^{30}\) at _p_=32


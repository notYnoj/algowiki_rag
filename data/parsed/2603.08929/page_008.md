comparison-based algorithms usually is _O(n_log(_n_)), the relative efficiency can be characterized by the ratio \(lim_{n\rightarrow\infty}\frac{wn}{nlog(n)}=0\) and \(lim_{w\rightarrow 0}\frac{wn}{nlog(n)}=0\). These limits suggest that bsort should strictly outperform any comparison-based algorithm as the array size n grows sufficiently large or the word size w becomes sufficiently small. Indeed, our results for the 8-bit `char` data type confirm this.

However, this theoretical superiority fails to materialize due to fundamental microarchitectural constraints. To isolate the specific bottlenecks impeding bsort’s performance, the algorithm was profiled using Linux’s `perf` tool on the same machine afore benchmarks were executed.

The empirical analysis identifies three primary causes for bsort’s performance degradation: branch unpredictability, stack pollution and instructional volume. First, the algorithm relies on bitwise conditional checks inside the partitioning loop. On random data, these checks are inherently unpredictable (approaching a 50% miss rate), causing frequent pipeline flushes. This is clearly shown on Figure 7.

Second, bsort employs a rigid recursive structure that imposes a hidden penalty: register pressure and stack pollution. Unlike hybrid algorithms that switch to iterative, low- overhead methods for small datasets, bsort incurs the full cost of recursive function calls down to the final bit. This repeated context switching forces frequent register spilling and consumes valuable L1 cache lines for stack management rather than payload data. Figure 8 illustrates this inefficiency, showing bsort consistently incurs a high L1 D-cache miss rate<tbc>

<tbc>across all data types.

The same recursive structure makes bsort traverse the whole array _w_ times, whereas other algorithms like introsort typically require only _O(log(n_)) times. Consequently, the sheer number of instructions required to complete the recursion overwhelms the processor as it executes significantly more instructions than other algorithms, e.g., 64 complete array scans for 64-bit integers in bsort vs. ≈ 26 for 10<sup>8</sup> elements in introsort. This behavior is clearly shown in Figure 9.

The performance gap between bsort and other algorithms also stems from a fundamental difference in algorithmic archi

Algorithm scaling for data type: float
106
Algorithm
bsort
introsort
spreadsort
103
skasort
104
Time (ms)
103
102
102
103
103
106
107
108
109
Number of elements
108
Algorithm scaling for data type: double
106
Algorithm
bsort
introsort
spreadsort
skasort
103
104
Time (ms)
103
102
102
103
106
107
108
109
Number of elements

Branch mispredictions per data type per algorithm for sorting 100,000,000 elements
100
100
Branch misprediction count
102
102
100
Algorithm
103
bsort
introsort
spreadsort
skasort
skasort
char
short
int
Data type
float
long
double

Cache misses per data type per algorithm for sorting 100,000,000 elements
100
Cache misses count
102
Algorithm
100
bsort
introsort
spreadsort
skasort
Metric
L1 P-cache misses
char
short
int
Data type
float
long
double

Cycles and instructions per data type per algorithm for sorting 100,000,000 elements
Algorithm
bsort
introsort
spreadsort
skasort
Metric
Cycles
Instructions
Cycles/instructions count
10-10
char
short
int
Data type
float
long
double

Fig. 6: Performance comparison for floating-point types `float` and `double`.

Fig. 7: Comparison of branch misprediction count

Fig. 8: Comparison of cache misses count

Fig. 9: Comparison of CPU cycles and instructions count


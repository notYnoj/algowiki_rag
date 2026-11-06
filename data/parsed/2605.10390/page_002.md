Memory utilization in radix distribution histograms can grow exponentially with precision necessitating multiple passes to accomodate memory capacity and memory access bandwidth limits on GPUs, FPGAs and CPUs for full precision sorting [17]. Temporary buffers for histogram population, sampling and bucket balancing further increase memory demand, mitigated by techniques such as adjusting the number of keys per pass to enable near-linear precision- scaling at the cost of increased memory, cache and bandwidth usage [37] [42].

This work extends FractalSort [54], originally designed for FPGA, to a CPU-adapted implementation that introduces the concept of the fractal data structure, a sparse binary tree histogram. This enables sublinear execution time for large datasets, SIMD-enabled thread execution of histogram updates, independent key processing without input bucketing or partitioning, and amortized memory overhead for large datasets due to histogram compression and localized histogram updates. The contributions include:

1) A parallel sort and merge update for unsorted keys with amortized update contention.

2) A novel batch stream sorting algorithm for large datasets without data pre-processing or input bucketing.

3) A novel sparse histogram compression scheme for bandwidth-efficient merge operation with counter width tapering.

4) A novel bandwidth-efficient FractalSortCPUA algorithm to retrieve an array of sorted keys from the compressed histogram.

Addressing these challenges enables FractalSortCPU to offer an accessible, scalable solution for cloud servers, databases and distributed big data compute systems while lowering costs and query latency at scale [44], complementing cloud resource optimization approaches [55].

## II. RELATED WORK

Radix sorting is the state-of-the-art algorithm for large keys due to the linear complexity with implementations on both serial and parallel architectures, including least significant bit (LSB) and most significant bit (MSB) algorithms often divided into histogram, prefix sum and stable scatter phases [32] [22]. One way to determine bucket bounds is coarse- grained bucketing combined with prefix scanning that offer speed-ups on uniform distributions but suffer from distribution dependence [38] [39]. Unit processor local histograms with reduction, scanning and merge scatter phases are common on GPU, memory and cache-locality are prevalent on CPU, while streaming data paths are common on FPGA due to higher memory access speeds, with memory bandwidth, radix size and precision-scalability the primary design concerns [17] [42].

Distribution dependence mitigation strategies such as sample sort and histogram sort incur pre-processing costs including increased memory footprint, which are mitigated by dependency graphs and stochastic sampling which predict load imbalance and perform smoothing techniques while relying on costly sampling processes [35] [36] [37] [40]. Such strategies increase memory footprint and pre-processing latency depending on the distribution, with significant variance between best case and worst case performance on skewed, uniform and partially sorted data [47].

Limited parallelism due to multiple passes is mitigated by balanced buckets and increased bandwidth allocation where near-linear performance is achieved [33]. Precision-scaling latency trade-off occurs in high-precision sorting scenarios which increase the number of passes to implement in-place cache-conscious algorithms where memory is limited due to histogram prefix arrays proportional to the radix size, permutation buffers for scatter stability and dependency graph data structures for distribution tracking [17]. Increasing and reducing the per-pass radix size trades off the number of passes for memory usage, while data skew causes larger bucket size variance affecting memory and tail latency, mitigated by disaggregated radix-tree layouts which minimize I/O without fully resolving the trade-off [20].

Partitioning, sampling and merging are used together to divide data sets into buckets for efficient sorting on limited compute resources used in sample sort and histogram sort, enabling balanced partitions and parallelization [17]. _k_-way and cache-aware merging reduce passes but become the bottleneck as _k_ increases, and external memory or streaming benefit from larger sorted runs at the cost of large _k_, and extra passes trade-off bandwidth for peak memory, with sampling and partitioning enabling distribution agnosticism at the cost of memory, pre-processing and merge latency [33].

Radix sort is the state of the art for hardware-based FPGA and GPU sorting, and is affected by exponential histogram growth due to both data set size and precision, and the distribution dependence due to bucketing, making memory-bandwidth a significant limiting factor [17]. The disaggregated radix tree helps reduce bandwidth usage by eliminating redundant I/O operations [20]. FractalSort [54] addresses histogram growth on FPGA through a compressed sparse histogram achieving 2.5x bandwidth efficiency over state-of-the-art FPGA sorting algorithms. In-place radix sorts and parallel counting schemes scale poorly with 64-bit and higher precisions due to the increasing number of passes needed to increase the precision of partially sorted keys and achieve a high-precision sort [41] [42].

This work solves these limitations by using a compressed sparse histogram approach eliminating the need for costly sampling, pre-processing and input bucketing, while bounding


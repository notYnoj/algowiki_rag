# FractalSortCPU: Bandwidth-Efficient Compressed Radix Sort on CPU

Michael Dang’ana

_Electrical & Computer Engineering_

_University of Toronto_

_Eonforge Labs_

Toronto, Canada

michael.dangana@mail.utoronto.ca

_Abstract_--Cloud database systems, particularly their middleware and query execution layers, use sorting as a core operation in query processing, indexing and join execution. Distribution-dependence and limited parallelism are key issues inherent in state-of-the-art radix sort which is preferred for large datasets due to performance advantages over comparison- based algorithms. Multi-pass bucketing, stochastic sampling and dependence graph structures are common solutions to these problems that incur the cost of data pre-processing and increased memory footprint hence they are less appropriate for large-scale workloads common in cloud environments. In-place radix sort schemes increase the number of passes as precision increases, which negatively impacts latency.

Our work solves these problems by introducing a CPU-adapted histogram compression scheme for radix sorting for arbitrary- precision keys implemented on the CPU for increased accessibility, providing state-of-the-art execution time, while limiting histogram growth. Fully parallel key-based histogram updates eliminate the need for input bucketing and data pre-processing further lowering latency, mitigating distribution-dependence and reducing complexity. With a parallelized sorting architecture utilizing SIMD-accelerated operations for low latency, the algorithm demonstrates improvement over the state-of-the-art on the CPU, GPU, and FPGA by 6x, 3x and 2.5x in bandwidth efficiency on 512MB to 32GB data sets at 16-bit precision.

### I. INTRODUCTION

As workloads grow and query demand tightens, cloud database middleware and query execution systems face large-scale sorting challenges. Sorting is a key concern in big data scenarios and is impacted by growing datasets and resource scarcity, increasing the latency, throughput and consistency requirements locally and in the cloud [43] [55]. Sorting enables big data use cases for operations such as index creation, sort-merge joins, queries, and database partitioning [15]. Radix sort algorithm is ideal for larger problem sizes compared to fast approaches based on sorting networks, merge sort, and sample sort [22] [25] [26].

State-of-the-art radix sort implementations usually suffer from _distribution dependence_ where skewed distributions lead to imbalanced bucket sizes affecting efficiency due to the need to suffer degradation from larger buckets or to dynamically allocate processing resources to large buckets,<tbc>

<tbc>limited parallelism due to multiple passes required for bucketing, _linear precision-scaling latency_ where extra passes are necessary to achieve high precision sorts, and _memory usage growth_ where pre-processing techniques including stochastic sampling, distribution histograms and dependency graphs require data structures impacting memory usage [33] [34] [25] [35] [36] [37].

Distribution dependence refers to the varying performance of sorting algorithms based on the inputs regarding skew, partially sorted data, randomness, uniform and Gaussian distribution from a latency and memory usage perspective [46]. Sorting algorithms are usually evaluated in terms of best, average and worst case performance which are significantly impacted by input distribution [47]. Various techniques are used to mitigate pre-processing necessary to determine input distribution such as adaptive partitioning and sorting strategy adjustment enabling consistent performance across a range of input distributions [48].

Limited parallelism occurs where high-performance radix sort uses multiple passes to partially sort at lower precision and store the intermediate data in memory, with a significant probability of histogram bucket collisions between entries at each pass creating critical paths [37]. Platform bottlenecks such as limited cache and socket capacity on CPU, memory conflicts and warp divergence cause bottlenecks and core idling on GPU further limiting effective parallelism, mitigated by techniques including bucket balancing and increased memory bandwidth [49].

The precision-scaling latency trade-off is characterized by the increase in sorting latency with precision where reduced precision to achieve approximate sorting is significantly beneficial in terms of reducing latency by over 40% using approximate storage, and full precision can be achieved by iteratively sorting the partially sorted data, relevant in modern hardware algorithms where reductions in compute and memory access can lead to significant performance gains for large data sets [50].


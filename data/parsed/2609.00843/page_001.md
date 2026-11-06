Shared-Memory Range-Tiled CDF Sort for Small-Range Integer Keys on GPUs

**Abstract**

We study unstable integer sorting on GPUs for arrays whose elements lie in a known integer range. Focusing on counting-sort-based methods that determine the output interval of each value from its frequency and the prefix sums of the frequencies, we propose and evaluate Range-Tiled CDF sort (RT-CDF), which partitions the possible value range into small intervals, called tiles, that fit in shared memory. For each tile, RT-CDF constructs a histogram, computes its prefix sum as a local CDF, and directly generates the output array from the local CDF. We compare RT-CDF against three baselines: CUB `DeviceRadixSort`, whose processed bit range is restricted to \([0,\lceil log_2R\rceil)\) to exploit the known range size _R_; Ref-H-P sort; and an implementation based on the algorithm of Kolonias et al. Experiments on an NVIDIA GeForce RTX 4090 with range sizes from _R_=2<sup>7</sup> to 2<sup>18</sup>, input sizes from _n_=10<sup>6</sup> to 10<sup>9</sup>, and uniformly distributed, normally distributed, and all-equal inputs show that RT-CDF outperforms the baselines over a broad set of conditions for small to medium ranges, achieving a maximum speedup of 4.39 over the fastest baseline. For _R_=2<sup>18</sup>, however, at least one baseline outperforms RT-CDF for every evaluated input size and input distribution, showing that the cost of histogram construction limits the applicability of RT-CDF to larger ranges.

### 1 Introduction

Sorting is a fundamental operation used in many computational tasks, including database processing, graph processing, simulation, and image processing. GPUs can process large numbers of elements in parallel, and many parallel sorting algorithms, including radix sort, merge sort, and sample sort, have been studied and implemented [1, 2]. GPU radix sorting for integers is particularly important in practice, and recent implementations such as Onesweep reduce the amount of data read from and written to global memory [3]. CUB `DeviceRadixSort`, provided by NVIDIA, is also widely used as a highly optimized GPU sorting implementation [4].

When the range of possible input values is known in advance and is sufficiently small relative to the input size, however, this additional restriction can be exploited. In particular, counting sort can count the occurrences of each value and use prefix sums of the counts to determine the interval occupied by

<sup>1</sup>Major in Applied Informatics, Graduate School of Science and Engineering, Hosei University <sup>2</sup>THIRD, Inc. <sup>3</sup>Department of Core Informatics, Graduate School of Informatics, Osaka Metropolitan University <sup>4</sup>Information Media Education and Research Center, Hosei University

arXiv:2609.00843v1 [cs.DC] 1 Sep 2026

Kento Ando<sup>1</sup> Kaito Takase<sup>2</sup> Noriyuki Fujimoto<sup>3</sup> Koichi Wada<sup>4</sup>


_flat\_stable\_sort_ (1101.28 ms), achieving approximately a 4.5_x_ improvement. It also outperforms Spinsort (1036.71 ms), showing that its distribution-based design avoids the _O(nlogn_) limitation and reduces the branch misprediction overhead. Furthermore, zSort consistently performs better than several high-performance unstable algorithms. At _n_=10<sup>7</sup>, zSort achieves about 6-35% improvement compared to Skasort (256.88 ms) and Pdqsort (369.14 ms). This result challenges the traditional trade-off between stability and peak performance. It shows that preservation of the order of equal elements is possible without losing efficiency. When compared with radix-based approaches such as Spreadsort (512.72 ms) and Radixsort (350.27 ms), zSort achieves performance improvements of about 53% and 31%, respectively. Similar trends are also observed for smaller input sizes, demonstrating the robustness and scalability of zSort for large-scale 64-bit key sorting.

2) Normal Distribution: The performance of different sorting techniques under a normal (Gaussian) input distribution is shown in Figure 3. A Gaussian distribution has a high concentration of keys around the mean, which leads to localized clustering. Such clustering can create load-balancing issues for simple bucket-based methods and can also affect pivot selection in comparison-based algorithms. Despite these challenges, zSort achieves high performance (272.37 ms) for an input size of 10<sup>7</sup>. In comparison, standard stable sorting algorithms such as _std::stable\_sort_ (1065.18 ms) and Spinsort (986.83 ms) are almost 4_x_ slower. Among unstable comparison based algorithms, Pdqsort performs relatively well (359.94 ms) due to its improved pivot sampling strategy. However, non-comparison-based approaches, including Skasort (326.16 ms), Spreadsort (359.37 ms), and Radixsort (322.46 ms), exhibit noticeable performance degradation compared to their uniform distribution behavior. These results indicate that zSort’s recursive mapping strategy is highly resilient to localized data clustering.

3) Skewed Distribution: Figure 4 shows the performance of various sorting techniques under a skewed

input distribution. Skewed dataset modeled using power- law distributions, represent heavy-tailed workloads where a small subset of keys dominates the frequency. Such distributions can significantly stress partition balance and increase recursion depth in both comparison-based and distribution-based algorithms. Under this distribution, zSort records an execution time of 315.13 ms indicating a slight performance degradation compared to uniform and normal distributions due to the overhead associated with handling highly skewed key distributions. Despite this, zSort continues to outperform all stable sorting algorithms by a significant margin. Compared to Spinsort (942.16 ms) and _std::stable\_sort_ (1024.52 ms), zSort achieves approximately 3_x_ and 3.25_x_ speedups, respectively. Furthermore, zSort remains highly competitive with non-comparison-based methods, operating within approximately 2.6% of Radixsort (307.64 ms).

4) Nearly Sorted Data: The performance of different sorting algorithms under a nearly sorted input distribution is shown in Figure 5. Algorithms such as Timsort, Spin-

Timsort 1000 std::stable_sort 500 flat_stable_sort Spinsort std::sort 200 Pdqsort Skasort Spreadsort 100 Radixsort 50 zSort Execution Time (ms, log10 scale) 20 10 5
2 1
107 106 105 Input Data Size (n)

Timsort 1000 std::stable_sort 500 flat_stable_sort Spinsort 200 std::sort 100 Spreadsort 50 Radixsort zSort Execution Time (ms, log10 scale) 20 10 5
2 1
107 106 105 Input Data Size (n)

Timsort 1000 std::stable_sort 500 flat_stable_sort Spinsort std::sort 200 Pdqsort Skasort Spreadsort 100 Radixsort 50 zSort Execution Time (ms, log10 scale) 20 10 5
2 1
107 106 105 Input Data Size (n)

Fig. 2. Execution Time vs Input Data Size under Uniform Distribution

Fig. 3. Execution Time vs Input Data Size under Normal Distribution

Fig. 4. Execution Time vs Input Data Size under Skewed Distribution


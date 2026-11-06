sort, and Pdqsort are designed to take advantage of this type of input. However, their practical performance is still affected by microarchitectural factors. For instance, during the merge phase the frequent conditional comparisons lead to branch mispredictions. In contrast, zSort provides better execution time compared to all other techniques across different input data sizes. This is due to the fact that zSort relies on direct memory mapping, which converts the near-sorted structure into predictable memory access patterns. Among unstable algorithms, Pdqsort performs competitively (191.56 ms) due to insertion-sort optimizations for nearly sorted data. These results show that zSort can maintain high performance even in cases where adaptive algorithms are expected to perform well.

5) High Duplicate Data: The performance of different sorting algorithms under a high-duplicate input distribution is shown in Figure 6. Such datasets are challenging for both comparison-based and distribution-based algorithms because many elements have identical values, which can lead to redundant operations. Traditional algorithms like Timsort and _std::stable\_sort_ perform many repeated comparisons, resulting in slower execution times (716.05 ms and 534.99 ms, respectively). Similarly, Radixsort does not benefit from duplicate values because it processes all digit positions in the same way. In contrast, Pdqsort can handle duplicates more efficiently by using duplicate detection, achieving a time of 88.18 ms. zSort performs better across all input sizes as compared to all other techniques. It achieves run time of 74.54 ms, 7.77 ms and 0.50 ms at input size 10<sup>7</sup>,10<sup>6</sup> and 10<sup>5</sup> respectively. zSort improves performance by grouping identical keys during the distribution phase, which avoids redundant scattered writes. This also improves memory locality which leads to better execution efficiency. The results show that zSort handles duplicate-heavy datasets efficiently while maintaining higher throughput than both comparison-based and traditional distribution-based sorting algorithms.

6) Relative Performance of Sorting Algorithms Across Input Distributions: The performance of sorting algo

rithms for different input distributions highlights the specialized nature of the respective existing technique. Unstable algorithms often perform very well in particular scenarios. For example, Pdqsort achieves high instruction- level efficiency on structured data, while Skasort benefits from strong cache locality in skewed data. These observations are summarized in Figure 7. The results show that zSort not only leads among stable algorithms but also frequently sets the overall performance baseline. It achieves significant speedups of 3_x_ to 4.5_x_ over standard stable implementations such as _std::stable\_sort_, Spinsort, and Timsort, effectively eliminating the conventional stability overhead.

## V. Conclusion

In this paper the performance gap between unstable and stable sorting algorithms is addressed. While approaches

Timsort 1000 std::stable_sort 500 -
Spinsort 200 -
Spinsort 100 50 -
Execution Time (ms, log10 scale) 20 10 5
2 1
107 106 105 Input Data Size (n)

Timsort 1000 std::stable_sort 500 -
Spinsort 200 -
Spinsort 100 50 -
Execution Time (ms, log10 scale) 20 10 5
2 1
107 106 105 Input Data Size (n)

Relative Sorting Performance (n = 107) 10 Uniform 1.00 1.07 1.46 1.53 2.13 4.31 4.58 3.55 4.51 5.50 9
8 Normal 1.00 1.20 1.18 1.30 1.69 3.62 3.93 3.15 3.91 4.68 7
Skewed 1.22 1.00 1.19 1.34 1.74 3.64 4.01 3.14 3.95 4.74 5
Input Distribution 4
Nearly Sorted 1.00 1.16 1.71 1.12 1.31 1.50 1.90 1.35 1.90 1.89 3
Duplicates 1.00 2.24 5.12 1.18 2.45 6.40 7.14 4.52 7.18 9.61 2
1
ZSort Skasort Spreadsort Spinsort Std::stable_sort Std::stable_sort Timsort Algorithm

Fig. 5. Execution Time vs Input Data Size under Nearly Sorted Data

Fig. 6. Execution Time vs Input Data Size under Duplicate Data

Fig. 7. Relative Performance of Sorting Algorithms Across Input Distributions


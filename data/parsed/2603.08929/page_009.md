<tbc>tecture. As detailed in  I, state-of-the-art implementations like introsort, spreadsort, and ska_sort are _hybrid_ algorithms; they adaptively switch strategies depending on partition size or data distribution to maximize hardware efficiency [7]-[9]. By contrast, `bsort` relies exclusively on the same bitwise partitioning procedure down to the finest granularity.

Remarkably, despite the lack of hybrid optimizations and the inherent instruction overhead, `bsort` demonstrates competitive performance. In shallow bit-depth regimes (e.g., 8-bit), it statistically outperforms the hybrid, cache-optimized introsort. This suggests that while the current monolithic implementation faces microarchitectural bottlenecks for large word sizes, the core bitwise mechanism possesses significant latent potential for future architectural optimization.

## V. FUTURE ENHANCEMENTS

While this work establishes the foundational mechanics and performance characteristics of _bsort_, several avenues for optimization remain to be explored. To address the performance gaps observed in larger word-size regimes, future iterations of the algorithm could be transformed into a hybrid implementation. By adaptively switching to a non-recursive, cache-friendly subroutine once partitions reach an optimal size, the _O(nw_) recursion depth penalty could be significantly mitigated. Furthermore, performance could be enhanced through the integration of Single Instruction, Multiple Data (SIMD) instructions to parallelize bit-masking operations, branchless partitioning like conditional move instructions to prevent branch mispredictions, and exploiting Instruction- Level Parallelism (ILP) to overlap partitioning tasks.

These advanced architectural optimizations are currently outside the scope of this paper, particularly as the hardware utilized for this study does not provide native support for modern SIMD extensions. Consequently, the implementation and evaluation of these enhancements are reserved for subsequent research.

## VI. CONCLUSION

This paper presents _bsort_, an in-place, non-comparison- based sorting algorithm for signed and unsigned integers and floating-point values in _O(wn_) time and _O(w_) space. It was demonstrated through formal proof and experimental analysis that _bsort_ is particularly effective for small word-size regimes, such as 8-bit integers. However, it was also identified that for larger word sizes, the algorithm’s performance is significantly hindered by its lack of a hybrid architecture and poor cache locality compared to state-of-the-art implementations. While _bsort_ provides a memory-efficient alternative for specific data types, future work is required to bridge the gap between its theoretical potential and practical high-performance execution.

## ACKNOWLEDGMENT

I want to express my deep gratitude to Kim García for her support and belief in me, without which many personal achievements, including this paper, would not have been possible.

## REFERENCES

[1] M. L. Fredman, "How good is the information theory bound in sorting?" _Theoretical Computer Science_, vol. 1, no. 4, pp. 355-361, 1976, accessed: 2021-07-25. [Online]. Available: https: //doi.org/10.1016/0304-3975(76)90078-5

[2] J. L. Bentley and R. Sedgewick, "Fast algorithms for sorting and searching strings," in _Proceedings of the eighth annual ACM-SIAM symposium on Discrete algorithms_, 1997, pp. 360-369.

[3] A. V. K. S and A. Arya, "Fastbit-radix sort: Optimized version of radix sort," in _2016 11th International Conference on Computer Engineering & Systems (ICCES)_, 2016, pp. 305-312.

[4] P. Terdiman, "Radix sort revisited,"  Corner (Blog), 2000, accessed: 2021-09-26. [Online]. Available: https://codercorner.com/ RadixSortRevisited.htm

[5] "IEEE standard for floating-point arithmetic," _IEEE Std 754-2019 (Revision of IEEE 754-2008)_, pp. 1-84, 2019. [Online]. Available: https://doi.org/10.1109/IEEESTD.2019.8766229

[6] S. Meyers, _Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library_. Addison-Wesley Professional, 2001.

[7] D. R. Musser, "Introspective sorting and selection algorithms," _Softw. Pract. Exper._, vol. 27, no. 8, p. 983-993, Aug. 1997. [Online]. Available: https://doi.org/10.1002/(SICI)1097-024X(199708) 27:8%3C983::AID-SPE117%3E3.0.CO;2-%23

[8] M. Skarupke, "I wrote a faster sorting algorithm," Probably Dance (Blog), December 2016, accessed: 2021-12-25. [Online]. Available: https: //probablydance.com/2016/12/27/i-wrote-a-faster-sorting-algorithm/

[9] S. J. Ross, "The spreadsort high-performance general-case sorting algorithm," _C++ Report_, vol. 14, no. 5, 2002, accessed: 2021-12- 25. [Online]. Available: https://www.boost.org/doc/libs/latest/libs/sort/ doc/papers/original\_spreadsort06\_2002.pdf


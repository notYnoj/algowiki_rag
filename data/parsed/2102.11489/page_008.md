3. Call **SlowSort**_<sup>K</sup>_ to sort the extracted array and reverse route the result back to the original array.<tbc>

4. At this moment, all elements fall into the correct segment, but if a segment has multiple keys, it may not be sorted internally. Fortunately, we know that at most _K_ segments can be multi-keyed. Therefore, we use oblivious compaction to extract these _K_ segments, call **SlowSort**_<sup>K</sup>_ to sort within each extracted segment, reverse route the result back, and output the final result.

This algorithm almost works except for one subtle issue that breaks correctness: the linear- work, logarithmic-depth oblivious compaction algorithm \[AKL<sup>+</sup>20b\] is _not stable_ and in fact this is inherent \[LSX19,AFKL19\]. This means that in the Step 2 above, the extracted elements do not preserve the order in which they appear in the input array.

**The fix: granularity switching.** Note that we do not need full stability, we just need to make sure that the extracted elements are ordered based on their segment numbers -- this way, after we sort the extracted elements and route the sorted elements back into the original positions, every element will land in the correct segment.

Therefore, to fix this problem, one naïve idea is to use **SlowSort**_<sup>K</sup>_<sup>3</sup> to sort the extracted array once again based on which segment each element belongs to, but this would be too costly since it would incur \(K^3\cdot 3n/K^2=O(nK)\) work. We propose a _granularity-switching_ idea. Specifically, we switch to a more coarse-grained partitioning scheme at this point: we instead view the array as _K_<sup>2</sup> super-segments, where each super-segment is the concatenation of _K_ original segments. Therefore, we use **SlowSort**_<sup>K</sup>_<sup>2</sup> to sort the extracted array whose length is 3_n/K_<sup>2</sup>, and this incurs _O(n_) work and _O_(log_n+k_) depth. At this moment, we can follow through with Steps 3 and 4, with the following modifications:

1. The reverse-routing in Step 3 now needs to reverse the decision of the **SlowSort**_<sup>K</sup>_<sup>2</sup> instance as well as the compaction.<tbc>

2. At the end of Step 3, every element now belongs to the correct super-segment. Therefore, Step 4 now works on the super-segments rather than the segments.

We defer a detailed description of our final algorithm to the subsequent formal sections.

## 2.2 Linear-Sized, Logarithmic-Depth Compaction Circuit

So far, we can get an oblivious PRAM algorithm that sorts _k_-bit keys in \(O(n)\cdot min(k,logn)\) total work and _O_(log_n_) depth -- to achieve this, we critically make use of an oblivious PRAM algorithm for compaction that is linear in total work and logarithmic in depth. Eventually, we want to get the circuit counterpart of this result. A critical missing link is a compaction circuit optimal in both size and depth. Even though we know how to construct an optimal compaction algorithm on an Oblivious PRAM \[AKL<sup>+</sup>20b\] and this may seem tantalizingly close to a compaction circuit, unfortunately the oblivious PRAM result does not directly translate to the circuit model -- if one tries to directly convert the oblivious PRAM algorithm to the circuit model, it results in a circuit _O(nw+n_log_n_) in size \[ALS21\]. Partly, this is because word-level operations on log_n_ bits can be accomplished in unit cost on a PRAM but there is no such free lunch in the circuit model. The recent work of Asharov, Lin, and Shi \[ALS21\] showed how to obtain a compaction circuit that is _O(nw_) size (ignoring polylog<sup>∗</sup> terms), but their circuit depth (as written) is linear.

We now describe how to get a compaction circuit that is not only optimal in size upto polylog<sup>∗</sup> factors, but also optimal in depth. To accomplish this goal, we go through several steps of bootstrapping that takes us from weaker primitives to stronger primitives. Specifically, we need several<tbc>


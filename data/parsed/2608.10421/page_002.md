## 1 Introduction

Sorting is one of the most fundamental problems in computer science, carrying great practical and theoretical importance. For a comparison-based sorting algorithm to operate upon a sequence of _n_ elements, it is well known that the information theoretic lower bound is lg(_n_!)≈_n_lg_n_-1.4427_n_ comparisons. Note that all logarithms throughout this paper are base 2.

However, the classical lg(_n_!) lower bound assumes an arbitrary input permutation where all _n_! outcomes are equally likely. Conversely, real-world datasets frequently exhibit substantial pre- existing order. By exploiting this structure, adaptive sorting algorithms manage to break this generic \(\Omega(n\mathrm{log}n)\) barrier, resulting in significant speedups in practical scenarios.

A recent advancement in \[1\] has introduced two algorithms that optimally adapt to pre-existing sorted _runs_ (i.e. maximal contiguous pre-sorted subarrays). They share running times of _O(nH+n_) and use no more than _nH_+3_n_ comparisons, defined according to the run-based entropy \(H=\sum_{i=1}^{r_\#}(r_i/n)\mathrm{lg}(n/r_i)\), where _r<sub>i</sub>_ is the length of the _i_-th sorted run (non-decreasing or decreasing). However, these algorithms and earlier well-known approaches like Timsort (from \[2\]) rely heavily on run scanning and dynamically formulating run-dependent merge boundaries. This dynamic nature forces state tracking during execution, requiring _O_(lg_n_) words of stack space or sizable overhead to avoid an explicit stack (in \[3\]). Furthermore, the underlying topology of the _merging tree_ model for execution becomes highly volatile due to the reliance on runtime input rather than the static array index partitioning of classical mergesort, making proofs notoriously difficult. For example, the worst-case complexity of Timsort was finally proven in \[4\], 16 years after its initial release.

In this paper, we introduce an algorithm _directional mergesort_, which uses no more than _nH_+3_n_ comparisons, 1.5_nH_+5_n_ moves and _O_(lg_n_) words of auxiliary space excluding the buffers for merging, matching the comparison bound of Powersort and Peeksort from \[1\] whilst retaining the simplicity of static merge boundaries, but does not adapt to decreasing runs. Additionally, we propose two optimizations: an extension of adaptive capabilities to decreasing runs and a reduction to _O_(1) words of stack space. The resulting algorithm _directional mergesort_<sup>++</sup> achieves the final bounds of _nH_+3_n-r_<sub>#</sub> comparisons, 1.5_nH_+6.5_n_ moves and _O_(1) words of auxiliary space excluding the buffers for merging, where _H_ is defined for both decreasing and non-decreasing runs.

### 1.1 Technical Overview

In Section 2, we present the algorithm of directional mergesort, which is a straightforward modification of a standard top-down mergesort. Its adaptivity relies solely on:

• The well-known skip check that bypasses the merge when both halves are already in order.<tbc>

• Dynamically altering the merge direction based on the state of the halves.

In Section 3, we formally prove the claimed bounds of _nH_+3_n_ comparisons and 1.5_nH+O(n_) moves for the algorithm by analyzing the algorithm’s behavior with the merging tree model. Crucially, all adaptation occurs locally within node operations and without altering the underlying merging tree geometry, giving a clean element-charging argument over static tree levels.

In Section 4, we then introduce two optimizations applied in directional mergesort<sup>++</sup>:

• Parallel mechanisms for decreasing runs that enable the algorithm to adapt to decreasing runs as well as non-decreasing runs with zero overhead in comparisons.<tbc>

• An optimization that shrinks the top-down recursive call stack to _O_(1) words, offering a distinct improvement over predecessors such as Powersort and Peeksort. This optimization also hinges on merge steps being static so they can be computed arithmetically, demonstrating the direct algorithmic dividends of simplicity beyond theoretical clarity.<tbc>


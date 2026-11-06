When considering lower-order terms, a more careful analysis in Appendix A.2 gives the tighter bound of _nH_+3_n-r_<sub>#</sub> comparisons for directional mergesort<sup>++</sup>, exactly matching the subtractive -_r_<sub>#</sub> term from Powersort. However, the proven comparison bound of the algorithm remains slightly worse than that of Peeksort, which has a subtractive term of -2_r_<sub>#</sub>.

Practical implementations of the algorithm could consider switching to a modified insertion sort that keeps track of non-decreasing or decreasing purity for small subarrays (\(r-\ell\le\mathrm{min}\text{\_run}\)). Additionally, optimized merge procedures such as galloping during merges could accelerate unbalanced run comparisons, while ping-pong merging from [6] could reduce element moves from 1.5_nH+O(n_) to _nH+O(n_) (using half-buffered merges for the final pass to avoid a full size _n_ buffer).

Whilst directional mergesort has optimal worst-case comparison bounds, its static merge steps may cause worse performance in the average case compared to other run-adaptive algorithms, leading to inferior performance in practice for typical inputs. We leave the empirical validation of its practical performance against production implementations like Timsort to future work.

A potential practical application of directional mergesort<sup>++</sup> involves substituting the linear-time stable in-place merge algorithm from [7] for the half-buffered merge. This removes the need for a merge buffer of size \(\lceil n/2\rceil\), reducing total auxiliary space usage to _O_(1) words. However, the large constant overhead (in comparisons and moves) of the in-place merge procedure causes us to lose our exact bounds of _nH_+3_n-r_<sub>#</sub> comparisons and 1.5_nH_+6.5_n_ moves. However, the running time of merges remains linear (\(\Theta(m)\) to merge _m_ elements in total), so the overall time complexity of _O(nH+n_) is retained. Whilst this combination was achieved by a recent result in [3], their approaches incur significant overhead to avoid explicitly storing a stack of _O_(lg_n_) words, involving repeated array inspections or complex encoding techniques. This overhead is completely avoided by directional mergesort<sup>++</sup>, whose static merging tree structure inherently supports the reduction to _O_(1) words at the cost of only arithmetic operations.

Finally, we note that if the desired bound is only _nH+O(n_) comparisons and _O(nH+n_) running time (_H_ defined for exclusively non-decreasing runs), a simple mergesort with skip checks only is already sufficient. The proof mirrors Section 3.2, hence it is left to Appendix B.

## Acknowledgements

The authors would like to thank Jay Llanes for raising the question of whether a simple mergesort with skip checks could achieve _O(nH+n_) complexity, which initiated this work.

AI tools were used solely for standard copy-editing tasks, such as language refinement and formatting. The technical aspects, including all algorithms and proofs, was formulated entirely by the authors, who assume responsibility for whole content.


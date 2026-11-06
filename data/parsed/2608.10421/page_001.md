Straightforward Entropy-Sensitive Mergesort

**Abstract**

In this paper, we present a stable mergesort variant, _directional mergesort_, that to sort an array of _n_ elements makes no more than _nH_+3_n_ comparisons and 1.5_nH+O(n_) moves where _H_ is the run-based entropy of the input sequence, matching the best existing algorithms in run-adaptive sorting. However, our algorithm is surprisingly minimalistic: it leverages only skip checks, i.e., bypassing the merge step when both halves are already in order, and dynamically changing the direction of merging based on the state of the subarrays. As dynamic run scanning is avoided, all merge steps remain static and derivable from _n_, enabling a reduction to _O_(1) words of stack space (i.e. space usage excluding the merge buffer) in _directional mergesort_<sup>++</sup>, thus improving over the predecessors’ _O_(lg_n_) words. Importantly, as directional mergesort adapts only to non-decreasing runs, directional mergesort<sup>++</sup> also applies a parallel set of rules for (strictly) decreasing runs, allowing the algorithm to also adapt to decreasing runs whilst retaining the original comparison bounds.

**Keywords:** adaptive sorting, merge sort, space optimization

**Bill Jin**<br> Department of Computer Science<br> University of Toronto, Canada<br> `bill.jin@mail.utoronto.ca`

**Alex Z. Xu**<br> Independent Researcher<br> Hong Kong<br> `xuzaxstk@gmail.com`


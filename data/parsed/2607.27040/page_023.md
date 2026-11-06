## B Full Small Sort Procedure

Recall that the _small sort_ is designed to sort small subsequences \(A'\) of

\(m'=O(lg^cm)\) (B.1)

active elements given a merge buffer \(B'\) of \(m'\) buffer elements, alongside the hole and _O_(1) auxiliary words of \(w\ge lgm\) bits, where _c_ is an arbitrarily large, but constant value. This is achieved by a _k_-way merge sort, where

\(k=2^{\lceil lg(w/lglgm)\rceil}\ge lgm/lglgm\) (B.2)

Let the number of merge passes _k<sub>#</sub>_ be

\(k_\#=\lceil lgm'/lgk\rceil-1\) (B.3)

This is equivalent to the ceiling of the base-_k_ logarithm of \(m'\) minus 1. Lastly, we define the sequence _r_<sub>0</sub>_...r<sub>k<sub>#</sub></sub>_ where

\(r_i=k^{i+1}\) (B.4)

The algorithm begins with initial run sorting using table sort. We split \(A'\) into runs \(A_1\dots A_{\lceil m^\prime/r_0\rceil}\) where _A<sub>i</sub>_ is a contiguous block with size _r_<sub>0</sub>, and \(B'\) into runs \(B_1\dots B_{\lceil m^\prime/r_0\rceil}\) by the same definition. The final runs \(A_{\lceil m^\prime/r_0\rceil}\) and \(B_{\lceil m^\prime/r_0\rceil}\) may be short, containing less than _r_<sub>0</sub> elements. Processing all runs sequentially, for the _i_th run execute the following:

1. Using table sort in [9], we create an array of auxiliary pointers to each of elements in a run _A<sub>i</sub>_, and sort the pointers with merge sort. As only pointers are moved, this process makes no data moves, only arithmetic operations.

2. Since the final destinations of all elements are now stored in the pointers, transport all elements to their destination using at most 3 moves per element. If _k<sub>#</sub>_ is odd, transport all elements in sorted order into _B<sub>i</sub>_: iterating through the sorted pointer sequence, swap the element pointed to by the _i_th pointer with the _i_th element in _B<sub>i</sub>_; then logically switch the roles of \(A'\) and \(B'\), as \(B'\) now contains the active elements, and \(A'\) the buffer elements. Otherwise, the elements are permuted in-place into the sorted sequence. As active elements stay in \(A'\), there is no need to do a logical role switch in this case.

Every pointer to an element in a range of _r_<sub>0</sub> elements requires _O_(lg_r_<sub>0</sub>) bits. By merge sort’s linear space complexity, the pointer array takes up _O(r_<sub>0</sub>)_O_(lg_r_<sub>0</sub>)=_O(w_) bits by (B.1) and (B.2), which fits in _O_(1) words. Each run of size _k_ is sorted with _k_lg_k-k_+1 comparisons (by merge sort’s worst-case for power of 2 lengths), 3_k_ moves and _O(k_lg_k_) arithmetic operations. The cost of this initial run sorting phase is then \(m'lgk-m'+o(m')\) comparisons and \(3m'\) moves.

After sorting the initial runs of size _r_<sub>0</sub>, we begin the process of merging groups of _k_ runs until \(A'\) is a contiguous sorted block. Let _i_ denote the current pass of merging. Iterating through _i_=1_...k<sub>#</sub>_, we execute the following process:

In the _i_th pass of merging, \(A'\) consists of runs of size _r_<sub>_i_-1</sub>, denoted by \(A_1\dots A_{\lceil m^\prime/r_{i-1}\rceil}\), where the final run \(A_{\lceil m^\prime/r_{i-1}\rceil}\) may be short, containing less than _r_<sub>_i_-1</sub> elements. Note that \(A'\) is not necessarily the original \(A'\), but the current logical \(A'\) that may be the original \(B'\), and similarly \(B'\) is not necessarily the original \(B'\). We divide \(B'\) into runs \(B_1\dots B_{\lceil m^\prime/r_i\rceil}\) analogously, but with size _r<sub>i</sub>_. Now, we define groups of _k_ runs from \(A'\), where the _j_th group contains runs \(A_{k(j-1)+1}\dots A_{kj}\). Iterating through groups \(j=1\dots\lceil m'/r_i\rceil\) sequentially, the _j_th group is processed as follows:


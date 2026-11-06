## 1 Motivation

Comparison-based sorts dominate much of modern sorting; in-place methods such as quicksort are widely employed and well-studied. All seek to minimize the number of comparisons required. For small numbers of input (_N_), a sequence of predetermined comparisons form a decision tree of _N_! leaves; if minimal, its height is then \(\lceil Nlog_2N\rceil\) e.g. for _N_=5, 7 comparisons suffice to fully determine the input permutation. To complete the sort a sequence of cyclic exchanges then reorder the data. These are often simplified into a sequence of two-element swaps. At _N\>_5, the decision tree’s size makes it impractical in production settings. At _N_=3 all solutions require a tree having `height`=3, `leaves`=6. The tree show below is optimal in that the two comparison descents occur with \(\mathtt{mem}[1]\le\mathtt{mem}[2]\le\mathtt{mem}[3]\) or \(\mathtt{mem}[1]\ge\mathtt{mem}[2]\ge\mathtt{mem}[3]\) i.e., termination occurs early with ascendingly presorted elements:

`if mem\[1\] \<= mem\[2\] then`

`if mem\[2\] \<= mem\[3\] then return // 1 2 3`

`else if mem\[1\] \<= mem\[3\] then return // 1 3 2`

`else return // 3 1 2`

`else if mem\[2\] \>= mem\[3\] then return // 3 2 1`

`else if mem\[1\] \>= mem\[3\] then return // 2 3 1`

`else return // 2 1 3`

This network is well known. In the first two steps we either establish `mem\[1\]\<=mem\[2\]` and `mem\[2\]\<=mem\[3\]` and gain `mem\[1\]\<=mem\[3\]` by transitivity (we are sorted). Otherwise, at the first `else`, `mem\[2\]` has largest rank; we need merely disambiguate the ranks of nonadjacent `mem\[1\]` and `mem\[3\]`. The second half follows by symmetry.

(For larger _N_, we can establish that `mem\[i\]\<mem\[i+1\]` in _N_-1 steps but this set of comparisons does not lead to an optimal (balanced) decision tree.) In the code seen above, exchanges complete the sort. For the above six leaves, these are the permutations (written in cycle notation) `nil`, (23), (123), (13), (132), (12), respectively.

By contrast, compare-exchange sorting networks order an array by performing a fused compare and conditional-exchange operation. (See, e.g., [1, Section 8.6] and [4, Section 5.3.4] for further information.) They are ideally suited to sorting arrays of integers of fixed small size (_N_=1_..._25 typical) where the decision making overhead of more general methods (tree traversal using comparison and bifurcation) will diminish or even negate any reduction in total machine comparisons. An integer compare is typically a single machine instruction. While compact and efficient, a general methodology for the creation of optimal fixed compare-exchange networks remains elusive.

Worst, lack of suitable metrics may lead to sub-optimal networks. Below are two simple networks for _N_=3. In Figure 1(a), we recode based on the above algorithm. In Figure 1(b), we apply Batcher’s even-odd construction for an odd number of elements, applying central symmetry (of inversion) to the right and left halves.


<tbc>worsening the dependence on \(\pi\). In order to achieve this, we strengthen a combinatorial result of Cibulka \[Cib09\] and show that the number of \(\pi\)-avoiding \(n\times n\) binary matrices with _n_ 1-entries is at most \(c_\pi^{2n+O(1)}\).

Recall that there is a connection between pattern-avoiding permutations and permutations of bounded twin-width. In particular, any permutation of twin-width _d_ avoids a certain pattern \(\pi\), the so-called \(d\times d\)-grid with Füredi-Hajnal limit \(c_\pi\in 2^{O(d)}\). It follows that the algorithm of Theorem 1.1 can also be used to sort permutations of bounded twin-width in linear time, without having access to a decomposition of small width.

**Corollary 1.2.** _There is a comparison-based algorithm that sorts a permutation of length n and twin-with d in_ \(O(d\cdot n)\) _time even if d is a priori unknown._

Guillemot and Marx \[GM14\] devised a fixed-parameter tractable (fpt-) algorithm that computes a twin-width decomposition of width 2<sup>_O(d_)</sup> for any permutation \(\tau\) of twin-width _d_ and length _n_ in _O(n_) time. Crucially, their algorithm assumes access to \(\tau\) in sorted order by values, and otherwise its running time degrades to _O(n_log_n_) due to the extra sorting step. However, Corollary 1.2 speeds up the sorting step to linear time, and thus a 2<sup>_O(d_)</sup>-wide decomposition can be computed in \(O(d\cdot n)\) time even in the comparison-based model. As a consequence, the running time of several fpt-algorithms can be improved from _O<sub>d</sub>(n_log_n_) to _O<sub>d</sub>(n_) when the input permutation of twin-width _d_ is given as a comparison oracle without any precomputed decomposition. This improvement concerns (i) the permutation pattern matching algorithm by Guillemot and Marx \[GM14\], (ii) the algorithm for first-order model checking by Bonnet, Kim, Thomassé and Watrigant \[BKTW22\], (iii) the algorithm for factoring pattern-avoiding permutations into separable ones by Bonnet, Bourneuf, Geniet and Thomassé \[BBGT24\], and (iv) algorithms for various optimization problems on pattern-avoiding inputs by Berendsohn, Kozma and Oppler \[BKO24\].

### Structure of the paper.

In Section 2, we introduce the necessary notions and review relevant facts about the Füredi-Hajnal limits. An efficient algorithm for multi-way merging is presented in Section 3, followed by an efficient algorithm for sorting a large number of short sequences in Section 4. Finally, Theorem 1.1 is proved in Section 5 by combining the two algorithms.

## 2 Preliminaries

### Permutations and avoidance.

A _permutation_ \(\pi\) of length _n_ is a sequence \(\pi_1,\dots,\pi_n\) in which each number from the set \[_n_\]={1_,...,n_} appears exactly once. Alternatively, we can represent \(\pi\) as an \(n\times n\) binary permutation matrix \(M_\pi\) where the cell in the _i_th column and _j_th row, denoted \(M_\pi(i,j)\), contains a 1-entry if and only if \(j=\pi_i\). Note that for consistency with permutations, we number rows of matrices bottom to top. A _permutation sequence_ is any sequence _s_<sub>1</sub>_,...,s<sub>n</sub>_ of pairwise distinct values. We say that two sequences (not necessarily permutations) _s_<sub>1</sub>_,...,s<sub>n</sub>_ and _t_<sub>1</sub>_,...,t<sub>n</sub>_ are _order-isomorphic_ if for each \(i,j\in[n]\), we have _s<sub>i</sub>\<s<sub>j</sub>_ if and only if _t<sub>i</sub>\<t<sub>j</sub>_. We say that a sequence _S contains_ a permutation \(\pi\) if some subsequence of _S_ is order-isomorphic to \(\pi\). Otherwise, we say that _S avoids_ \(\pi\). See Figure 1.

Additionally, we define avoidance for binary matrices. We say that a binary matrix _M contains_ a binary matrix _P_ if _P_ can be obtained from _M_ by deleting rows or columns and changing an arbitrary subset of 1-entries to zero. Otherwise, _M avoids P_.


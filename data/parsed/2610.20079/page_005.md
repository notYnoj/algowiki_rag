Memory holds _M_ words, each disk block contains _B_ consecutive words, and \(2B\le M\le N\). A _block transfer_ reads one disk block into memory or writes one block from memory to disk. The algorithm may access any disk block, and its complexity is the total number of block transfers.

Disk data must be read into memory before they can participate in computation; computation in memory is not charged as I/O. The algorithm may perform arbitrary bit operations on integers, including combining bits from different integers into intermediate results. Data buffers and mutable workspace count toward the _M_-word memory bound.

The program is fixed from the size parameters, independently of the input values, and its code is excluded from data space. When \(w<\lceil log_2N\rceil\) and _M_ is below a fixed threshold, the construction stores its predetermined execution-step index outside the _M_ words. The threshold depends only on the construction and the constants in \(w=\Theta(logN)\). The step index specifies the position in a sequence fixed before the input values are known; it is not a buffer for input data. Appendix D gives the detailed conventions and formalization scope.

The input, output, and intermediate data on disk together occupy at most _O(N<sup>k</sup>_) words for a constant _k_ independent of _N,M,B_. We call this _polynomial disk space_. Disk addresses therefore occupy _O_(log_N_) bits, or a constant number of machine words.

**Theorem 3.1** (External-memory integer sorting)**.** Under these conventions, there is a constant \(\varepsilon>0\) such that, for every \(2B\le M\le N\), _N_ integers of \(\Theta(logN)\) bits can be sorted deterministically in

\(O\big(\frac{N}{B}\big[1+\frac{logN}{(log(M/B))^{1-\varepsilon}(logM)^\varepsilon}\big]\big)\) (2)

block transfers. The algorithm uses at most _M_ words of memory and polynomial disk space, and is correct on every input.

Here \(\varepsilon\) is independent of _N,M,B_; we take \(\varepsilon=1.5\times 10^{-5}\). The factor _N/B_ is the cost of scanning the input. The logarithmic factor in classical sorting is governed mainly by the number of blocks that fit in memory. Our bound depends on both log(_M/B_) and log_M_, reducing the cost when memory holds only a small number of blocks.

1 gives two examples with _M_=2_B_, both with saving factor \((logB)^\varepsilon\).

When the input fits in memory, reading, sorting, and writing it takes the optimal _O(N/B_) block transfers.

## 3.2 The communication model and coding counterexample

Let _G_=(_V,E_) be a finite undirected network. An edge _e_ has capacity _c(e_), shared by the two directions: their transmission rates must sum to at most _c(e_). The network has _W_ unicast sessions. Session _i_ has source _s<sub>i</sub>_, sink \(t_i\neq s_i\), and required rate _r<sub>i</sub>_. Source _s<sub>i</sub>_ holds a message _X<sub>i</sub>_<tbc>

\begin{tabular}{ccc}
Input size (_M_=2_B_) & Classical comparison sorting & This work \\
_N=B_<sup>2</sup> & \(\Theta(BlogB)\) & \(O(B(logB)^{1-\varepsilon})\) \\
_N=B_<sup>3</sup> & \(\Theta(B^2logB)\) & \(O(B^2(logB)^{1-\varepsilon})\) \\
\end{tabular}

1: Improvements for two input sizes, with \(B\rightarrow\infty\) in both cases.


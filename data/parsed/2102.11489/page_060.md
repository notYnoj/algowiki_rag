**Theorem C.3** (Tight compaction: optimal-depth, slightly non-optimal in size)**.** _There is an_ (_n,w)- tight compaction circuit with O(nw+n_loglog_n_) _generalized boolean gates, O(n_) _number of w- selector gates, and of depth O_(log_n)._

_Proof._ To construct such circuit, we need an approximate tight compaction circuit that swaps the all but 1/polylog_n_ fraction of the misplaced elements in the original array. We want that this approximate tight compaction circuit to achieve sub-logarithmic depth, but we allow the circuit size to be a loglog_n_ factor non-optimal. More specifically, we need the following:

**Lemma C.4.** _Fix an arbitrary constant_ \(\widetilde{C}>1\)_. There is an_ \((1/(logn)^\widetilde{C},n,w)\)_-approximate tight compaction circuit that has_ \(O(n\cdot logn)\) _generalized boolean gates, O(n_) _number of w-selector gates, and with depth at most O_((loglog_n_)<sup>2</sup>).

_Proof._ The construction is similar to that of Theorem 12.1, the only difference is at Step (c) of \(\widehat{\mathbf{Swap}}^n\): when performing the lossy loose compaction, we use the large-size lossy loose compaction from Theorem 8.1 instead of the small circuit from Theorem 11.1. Symmetrically at Step (e) of \(\widehat{\mathbf{Swap}}^n\), we also use the large circuit from Theorem 8.1.

With these modifications, the depth is _O_((loglog_n_)<sup>2</sup>) because each lossy loose compaction takes _O_(loglog_n_) depth and it is recursively applied for _O_(loglog_n_) times in \(\widehat{\mathbf{Swap}}^n\). The circuit size follows similarly.

**Proof of Theorem C.3:** We use the same meta-algorithm as in Section 14 (which was first proposed by Pippenger \[Pip96\] and later used in Asharov et al. \[AKL<sup>+</sup>20b\]). The algorithm proceeds as follows. First, sort all but (1/polylog_n_)-fraction using the low-depth approximate tight compaction (Lemma C.4). Second, collect the (1/polylog_n_)-fraction misplaced elements into a short list of _n/_log_n_ elements using the sparse loose compactor in Theorem 13.3. Third, sort the short list using the AKS sorting network. Finally, reversely route the sorted short list back to the original array.

Using Lemma C.4 and 13.3, the performance bound analysis is direct. Notice that the three steps are very similar to that of Theorem 14.1, and the only difference is that we perform a less efficient approximate tight compaction at the first step (Lemma C.4 instead of Theorem 12.1).

## C.2 Improving Circuit Size through Recursive Bootstrapping

Next, we show how to use the recursive bootstrapping technique of Koucký and Král \[KK21, Lemma 19\] to compress the circuit size without blowing up the asymptotical depth. The meta-algorithm is identical that of Koucký and Kràl, but we present it in a top-down recursion (compared to their bottom-up) and parameterize the algorithm using the size and depth of the given larger circuit.

Let **LargeTC**_<sub>n,w</sub>_ be the tight compaction circuit that sorts _n_ elements each with 1-bit key and _w_-bit payload, let \(O(nw+n\cdot logn)\) be the circuit size and _O_(log_n_) be the depth. We construct **TC**_<sub>n,w</sub>_ recursively as below, where _n_ is the number of elements in the input array _A_ and and _w_ is the width of each payload string. For simplicity we also suppose the division and log(_x_) always map to proper integers in the algorithm.

**TC**_<sub>n,w</sub>(A_)**:** //Assume: _A_ consists of _n_ elements of width _w_, each with a 1-bit key.

1. (Base case.) If \(loglogn\le w\), invoke **LargeTC**_<sub>n,w</sub>(A_), and then output the result. Otherwise, continue with the following.<tbc>


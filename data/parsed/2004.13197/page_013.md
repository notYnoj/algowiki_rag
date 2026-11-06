nodes corresponding to I/Os of either a preprocessed block or a block from B. The decision tree has at least _N/B_ leaves.

We first relax that the algorithm only locate _x_ to within a space of 2_B_, i.e., once \(|S|\le 2B\), we will give the algorithm the exact position for free. With this, the input of a block from B can reduce _S_ by a factor of at most 4 (actually, this factor is 2_S/(S-B_), which is very close to 2 when _S_ is large, and equals 4 when _S_=2_B_). Since the query time cannot exceed _c_log_<sub>B</sub>N_, _S_ can reduce by a factor of at most 4<sup>_c_log_<sub>B</sub>N_</sup>=_N_<sup>1-(2_c/_log_B_)</sup>. This still leaves a factor of _N_<sup>(1-(2_c/_log_B_))</sup>_/B_ to account for.

Call the set of all extra blocks preprocessed by the algorithm \(\mathcal{B}'\). Let _K_ be the set of all elements in blocks in \(\mathcal{B}'\) such that no two elements in _K_ belong to the same block in \(\mathcal{B}'\). The following holds:

1. To preprocess \(\mathcal{B}'\), the algorithm required \(\Omega(K)\mathrm{I}/\mathrm{Os}\).<tbc>

2. The maximum fan-out that using preprocessed blocks can achieve is _O(K_).

Proof of 1: Since there are _K_ elements from different blocks, each of these blocks needed to be inputted at least once at some point of preprocessing, hence requiring at least _K_ memory transfers.

Proof of 2: Regardless of the choice of K elements within _S_, there will be at least one gap that is of size at least _S/K_. Hence, the maximum factor by which the search space can be decreased is _K_.

Since the decision tree still must have enough nodes to guarantee the remaining fan-out of _N_<sup>1-(2_c/_log_B_)</sup>_/B_, the above two observations imply that \(K=\Omega(N^{1-(2c/\mathrm{log}B)}/B)\), thus finishing the proof.

**Upper Bound**: Let \(\beta=N^{1/\mathrm{log}B}\). In a linear scan, the algorithm can write out every \(\beta\)th element from _N_, and store them in contiguous blocks. There are _N_<sup>1-1/log_B_</sup> such elements, and this requires and extra space of _N_<sup>(1-1/log_B_)</sup>_/B_ blocks. The algorithm then builds a _B_-tree on this set of elements.

The search proceeds by first going through the _B_-tree, until the search space of _x_ is reduced to a set of size \(\beta\). On this set, the algorithm performs a simple binary search. The total runtime is bounded by log_<sub>B</sub>N_<sup>(1-1_/logB_)</sup>+log\(_2\beta\le 3\mathrm{log}_BN\mathrm{I}/\mathrm{Os}\).


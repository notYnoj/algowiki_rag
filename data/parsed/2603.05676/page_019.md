# Entropy-Sensitive Strictly In-Place Sorting

19

2. If \(r_k>\alpha\sum_{i=1}^{k-1}r_i\) for some constant \(\alpha\), no merge occurs.

**Corollary 2.** _The original ShiversSort and_ \(\alpha\)_-StackSort are walkable._

_Proof._ Since both ShiversSort and \(\alpha\)-StackSort \[4\] are almost-2-aware, they trivially satisfy the first property. ShiversSort’s merge condition, \(2^{\lfloor logr_2\rfloor}\le r_1\), satisfies the second property with \(\alpha=2\). \(\alpha\)-StackSort similarly does so with its own parameter \(\alpha\). Thus, both stack-based mergesorts are walkable. \(\sqcap\sqcup\)

### B TimSort is Not Walkable

It is tempting to try to extend our walk-back analyses to TimSort. Unfortunately, in this section we show that TimSort is not walkable by providing an input instance such that TimSort implemented with the walk-back algorithm performs asymptotically worse than standard, non-in-place TimSort. This motivates our jump-back algorithm, presented in Section 4, which works for virtually all stack- based mergesorts. In Section B.1, we use a similar argument to show that \(\alpha\)- MergeSort is also not walkable.

Our counterexample considers an array of length _n_ with the following preexisting runs. The first _n/_2 elements form a run, the next _n/_4 elements form a run, and the next _n/_8 elements form a run. The remaining elements form a

n/2
n/4
n/8
22222
n/2
n/4
n/8
222
n/(16logn)

Fig.11: The worst-case input sequences we construct for our TimSort walk-back implementation. The top array represents the first version we analyze. The series of _n/_16 runs of size 2 cause \(\Theta(logn)\) _stages_ to occur, blowing up walk-back cost to \(\Omega(nlogn)\). The bottom array reduces the number of runs of size 2 to _n/_(16log_n_). The walk-back cost remains \(\Omega(nlogn)\) while the Shannon entropy of the array becomes constant. Therefore, TimSort with the walk-back algorithm will perform asymptotically worse than standard TimSort on the second sequence.


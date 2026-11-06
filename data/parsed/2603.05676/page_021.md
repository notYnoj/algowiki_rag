# Entropy-Sensitive Strictly In-Place Sorting

21

Furthermore, let _k=O_(1) be the size of our shallow stack. As defined by the walk-back algorithm, we only maintain the top _k_ elements of the stack. The rest are forgotten.

**Observation 9.** _At the beginning of stage i, there are i_+3 _runs in the stack._

**Lemma 9.** _There are_ \(\Theta(logn)\) _stages that occur throughout TimSort’s main loop._

_Proof._ The first three runs have total length 7_n/_8. Then there are _n/_8 remaining elements across all remaining runs. At the end of stage _i_, the last run is of size 2_<sup>i</sup>_. This occurs for all _i_ such that \(1\le i<log(n/8)\) by definition. Then _i_ is at most log(_n/_8)-1. Thus, we have \(\Theta(logn)\) stages throughout the algorithm. \(\sqcap\sqcup\)

**Corollary 3.** _There are_ \(\Theta(logn)\) _stages such that i\>k._

_Proof._ Follows from the fact that _k_ is a constant. \(\sqcap\sqcup\)

**Lemma 10.** _At all stages i such that i\>k, applying the walk-back algorithm incurs a walk-back cost of_ \(\Omega(n)\).

_Proof._ By Observation 9, there are _i_+3 runs in the stack at the beginning of this stage. By the fact that _i\>k_, this means that the bottom three runs of size _n/_2, _n/_4, and _n/_8 have been forgotten. When the merge sequence terminates, there are four runs in the stack. This means that the run of size _n/_8 takes label _R_<sub>2</sub>. By Observation 8, we must know _r_<sub>2</sub> to determine that the merge sequence is indeed finished. The result follows from the fact that \(r_2=n/8\in\Omega(n)\). \(\sqcap\sqcup\)

By Corollary 3 and Lemma 10, the total walk-back cost of TimSort under this input instance is in \(\Omega(nlogn)\). As described, however, our counterexample input instance has entropy \(\Omega(logn)\). Thus, standard TimSort would also run in time \(\Omega(nlogn)\).

A small modification to our counterexample gives us the desired result. Instead of _n/_16 runs of size 2, reduce this to _n/_(16log_n_) runs. Have the remaining elements form a single run of size _n/_8-_n/_(8log_n_). See Figure 11. The Shannon entropy of this new array is constant, so standard TimSort would run in linear time. However, a similar analysis of this variant shows that applying the walk-back algorithm incurs a walk-back cost of \(\Omega(nlog(n/logn))\subseteq\Omega(nlogn)\). We conclude the following.

**Theorem 4.** _TimSort is not walkable._

### B.1 Additional Counterexample

We can use a similar argument to above to show that \(\alpha\)-MergeSort is not walkable.

First, let us consider the merge policy of \(\alpha\)-MergeSort.


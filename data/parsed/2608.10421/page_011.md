**Lemma 15** (Comparisons at Upper Levels: Decreasing)**.** _For a decreasing run of length r, the total number of comparisons charged to its elements at levels h\<t is bounded by rt._

_Proof._ By the accounting scheme in Lemma 5, in the worst-case scenario, each of the _r_ elements in the run is charged the worst-case of 1 comparison per level. Across all _t_ levels (_h_=0_,...,t_-1), the total charge to the run is at most _rt_.

**Lemma 16** (Comparisons at Lower Levels: Decreasing)**.** _For a decreasing run of length r, the total number of comparisons charged to its elements at levels_ \(h\ge t\) _is bounded by_ 2(_n/_2_<sup>t</sup>)._

_Proof._ As established in the proof of Lemma 6, at levels \(h\ge t\), nodes are too small to fully encapsulate the run, thus Case 3 nodes cannot exist, and nodes completely outside the run (Case 4) also cost 0 comparisons relevant to the run. Any node fully contained within the decreasing run (Case 1) will pass the decreasing skip check, bypassing the merge step, costing 0 comparisons. Therefore, the only nodes that incur costs relevant to the decreasing run are the two Boundary nodes (Case 2) at each end of the run’s contiguous interval.

## Left Boundary:

As defined in Lemma 6, let _v<sub>i</sub>_ be the Case 2 node on the left boundary at level \(i\ge t\), and _n<sub>i</sub>_=|_v<sub>i</sub>|_.

• If the boundary falls in the right child _R_, applying the worst-case charge bounds the cost by \(|R|-1\le|L|=n_i-n_{i+1}\) as in Lemma 6.<tbc>

• If the boundary falls in the left child _L_, _R_ is a pure strictly decreasing sub-run (_b_<sub>2</sub>=`true`) and thus cannot be non-decreasing (\(b_1=\mathtt{false}\)) (\(|R|\ge 2\) for all non-base cases). The algorithm utilizes MergeFw, exhausting the pure right half first and appending the remaining left-half run elements with 0 comparisons. The charged cost is exactly |_R_|=_n<sub>i</sub>-n_<sub>_i_+1</sub>.<tbc>

• If at some level _k_ boundary perfectly aligns with the partition between _L_ and _R_, the boundary path terminates. Charging the worst-case of 1 comparison to every run in _R_ gives |_R_|=_n<sub>k</sub>-n_<sub>_k_+1</sub> comparisons (where _n_<sub>_k_+1</sub>=|_L_|).

As the cost at any left boundary node _v<sub>i</sub>_ is bounded by _n<sub>i</sub>-n_<sub>_i_+1</sub> universally for all subcases, summing over all levels yields the telescoping sum \(\sum(n_i-n_{i+1})\le n/2^t\) from Lemma 6.

## Right Boundary:

By symmetry, let \(v'_i\) be the right boundary node and \(n'_i=|v'_i|\).

• If the boundary falls in _L_, the worst-case charge applies, identically yielding \(n'_i-n'_{i+1}\).<tbc>

• If the boundary falls in the right child _R_, the left child _L_ is a pure strictly decreasing sub-run (_a_<sub>2</sub>=`true`) and _R_ cannot be decreasing (_b_<sub>2</sub>=`false`). The algorithm invokes MergeBw (except when |_L_|=1; Appendix A.1 shows this does not affect the bound), exhausting the pure left half first at a cost of exactly \(|L|=n'_i-n'_{i+1}\) comparisons.<tbc>

• If the boundary aligns perfectly with the partition between _L_ and _R_ at level _k_, the boundary path terminates, and the cost is \(n'_k-n'_{k+1}\) comparisons (with \(n'_{k+1}=|L|\)).

The same telescoping sum \(\sum(n'_i-n'_{i+1})\le n/2^t\) holds for the right boundary. Adding the costs for the left and right boundaries yields the total lower-level cost bound of 2(_n/_2_<sup>t</sup>_) comparisons.

**Theorem 17** (Optimized Comparison Complexity)**.** _An array of size n containing r_<sub>#</sub> _pre-existing non-decreasing or decreasing runs of lengths r_<sub>1</sub>_,r_<sub>2</sub>_,...,r_<sub>_r_<sub>#</sub></sub> _is sorted in at most nH_+3_n comparisons, where the run-based entropy_ \(H=\sum_{i=1}^{r_\#}(r_i/n)lg(n/r_i)\).

_Proof._ Combining the bounds from Lemma 15 and Lemma 16, and setting \(t=\lceil lg(n/r_i)\rceil\), the total merge comparisons charged to any decreasing run of length _r<sub>i</sub>_ is at most _r<sub>i</sub>_lg(_n/r<sub>i</sub>_)+2_r<sub>i</sub>_ (see proof of Lemma 7). This perfectly matches the bound for non-decreasing runs in Lemma 14.


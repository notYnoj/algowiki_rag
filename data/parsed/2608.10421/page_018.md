## A.2 Tightened Bound

Here we prove the refined bound for Corollary 22 noted in Remark 23. This is done by a more precise analysis of the boundary path.

**Theorem 24** (Tighter Comparison Bound)**.** _Directional mergesort_<sup>++</sup> _sorts an array of size n containing r_<sub>#</sub> _runs in at most nH_+3_n-r_<sub>#</sub> _comparisons (where H is defined for both non-decreasing and decreasing runs)._

_Proof._ Recall that sequences of size 2 are resolved using the skip check comparison during the base case (see Algorithm 2), bypassing the merge step entirely and incurring 0 merge comparisons. Since the skip check comparisons are accounted for separately in the global _n_-1 overhead bound, we can refine our boundary node analysis when \(r\ge 2\) (_r_=1 handled separately shortly).

We redefine the termination condition of the right boundary path at a level \(k'\) to be when:

• The right boundary of the run aligns with the partition between children (Subcase C).<tbc>

• Or the size of the next right boundary node \(|v'_{k^\prime+1}|=2\). Additionally, if the first boundary node at level _t_ already has size 2, the boundary path is empty. As a boundary node of size 2 incurs no merge comparisons, and its children are leaves of size 1 which return instantly, no costs are incurred below and the early termination already accounts for all possible charges.

We examine the final size term \(n'_{k^\prime+1}\) for the right boundary:

• **Case i (Standard Termination):** The boundary perfectly aligns (Subcase C) at some level \(k'\) where \(n'_{k^\prime}\ge 3\) then \(n'_{k^\prime+1}=|R|=\lceil n'_{k^\prime}/2\rceil\ge 2\).<tbc>

• **Case ii (Base Case Termination):** The path terminates due to the redefined condition, thus \(n'_{k^\prime+1}=2\).

These two cases are fully representative of all possible boundary path terminations. This is because a node of size 2 cannot terminate the boundary path as the new condition terminates the path immediately if the next node is of size 2. Furthermore, nodes of size 1 are either purely run elements or non-run elements, so they can only be Case 1 or Case 4, and cannot be Case 2, hence they cannot be part of the boundary path. Thus, the lower bound \(n'_{k^\prime+1}\ge 2\) holds for the right boundary.

Summing the charges \(n'_i-n'_{i+1}\) from level _t_ to level \(k'\) yields a telescoping sum bounded by:<tbc>

\(\sum_{i=t}^{k^\prime}(n'_i-n'_{i+1})=n'_t-n'_{k^\prime+1}\le\lceil n/2^t\rceil-2\le n/2^t-1\)

<tbc>If the boundary path is empty, the charge is then \(0\le n/2^t-1\) (as \(t\le\lceil lg(n/2)\rceil\le lgn\) when \(r\ge 2\)). Combining with the previous left boundary cost of _n/_2_<sup>t</sup>_, the total lower level charge is 2(_n/_2_<sup>t</sup>_)-1 comparisons. Integrating this tighter deduction with the upper level costs of _rt_ (in Lemma 14 and Lemma 15) and applying the convexity bound yields:<tbc>

\(rlg(n/r)+2r-1\)

<tbc>**Case** _r_=1**:** A run of length _r_=1 consists of a single element at a leaf node in the merging tree. Since the depth of any leaf in a binary merging tree of size _n_ is at most \(\lceil lgn\rceil\), charging 1 comparison to the single run element for each ancestor of the leaf node yields:<tbc>

\(\lceil lgn\rceil\le lgn+1=1lg(n/1)+2(1)-1=rlg(n/r)+2r-1\)

<tbc>Thus, the bound of _rlg(n/r_)+2_r_-1 holds for all runs. Summing across all _r_<sub>#</sub> runs and reintroducing the global _n_-1 skip checks gives the final bounded comparisons:

\(nH+2n-r_\#+(n-1)\le nH+3n-r_\#\)


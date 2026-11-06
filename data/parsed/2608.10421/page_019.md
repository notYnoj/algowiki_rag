## B Simple Adaptive Mergesort Analysis

This Appendix is dedicated to answering the question of Jay Llanes, regarding the well-known simple adaptive mergesort with skip checks:

**Algorithm 5** Simple Adaptive Mergesort

procedure Sort\((A[],\ell,r)\triangleright\) _Processing Subarray_ \(A[\ell..r)\)<br>
   if \(r-\ell<2\) **then return**<br>
   \(m\leftarrow\lfloor(\ell+r)/2\rfloor\)<br>
   Sort\((A,\ell,m)\)<br>
   Sort(A,m,r)<br>
   if \(A[m-1]\le A[m]\) **then return**<br>
   \(\triangleright\) _Skip Check_<br>
   MergeFw\((A,\ell,m,r)\)

Unlike directional mergesort (Algorithm 1), Algorithm 5 uses only standard forward merging (MergeFw) rather than dynamic directional selection. Consequently, while Case 1 (Fully Contained) nodes bypass the merge entirely via line 6 and cost 0 comparisons, Case 2 (Boundary) nodes cannot leverage the directional savings established in Section 3.1.

To account for this, we adopt the flat amortized charging scheme introduced in Section 3.2: every element involved in an active merge loop is charged 1 comparison per level regardless of local savings, while Case 1 nodes and Case 4 nodes incur 0 cost as a whole.

### B.1 Comparison Complexity

As established in Lemma 4, the global overhead of skip checks across the _n_-1 internal nodes of the binary merging tree contributes exactly _n_-1 comparisons. We isolate this overhead first and analyze the per-run merge comparison charges over the two tree depth regimes using threshold depth \(t+1=\lceil lg(n/r)\rceil+1\) for a run of length _r_.

**Lemma 25** (Upper-Level Comparison Charge)**.** _For a non-decreasing run of length r, the total merge comparison charge incurred across upper levels (h\<t_+1_) is bounded by r(t_+1).

_Proof._ Charging each of the _r_ run elements at most 1 comparison per level across _t_+1 levels yields an upper-level cost bounded by _r(t_+1).

**Lemma 26** (Lower-Level Comparison Charge)**.** _For a non-decreasing run of length r, the total merge comparison charge incurred across lower levels (_\(h\ge t+1\)_) is bounded by_ 2(_n/_2_<sup>t</sup>)._

_Proof._ At levels \(h\ge t+1>t\), node sizes are bounded by _r_, so Case 3 nodes cannot exist. Furthermore, Case 1 and Case 4 nodes contribute 0 charge to the run. Thus, non-zero charges arise solely from at most two Case 2 boundary nodes per level.

By Fact 2, a boundary node _v_ at level _h_ has size at most \(\lceil n/2^h\rceil\). Since the run cannot fully contain a boundary node, _v_ contains at most \(\lceil n/2^h\rceil-1\le n/2^h\) run elements. Across both boundary nodes, at most 2(_n/_2_<sup>h</sup>_) run elements are charged 1 comparison at level _h_. Summing this geometric series across all lower levels \(h\ge t+1\) yields:

\(\sum_{h=t+1}^{lgn}2(n/2^h)\le 2\cdot\frac{n/2^{t+1}}{1-1/2}=4(n/2^{t+1})=2(n/2^t)\)


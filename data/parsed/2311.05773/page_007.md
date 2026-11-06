InversionSort starts by (trivially) having the backbone consist only of the artificial smallest red element _r_<sub>0</sub> and largest blue element _b_<sub>1</sub>, and _R_<sub>0</sub>=_R_ and _B_<sub>1</sub>=_B_.

For a given backbone (_u_<sub>0</sub>_,u_<sub>1</sub>_,u_<sub>2</sub>_,...,u_<sub>2_k_</sub>_,u_<sub>2_k_+1</sub>)=(_r_<sub>0</sub>_,b_<sub>1</sub>_,r_<sub>2</sub>_,...,r_<sub>2_k_</sub>_,b_<sub>2_k_+1</sub>), InversionSort first, for each pair _X<sub>i</sub>,X_<sub>_i_+1</sub> of adjacent buckets that have no proof that there is no further inversion, in a round-robin manner, does one round of comparison with amortized constant cost, as spelled out in Section 2.1. If this leads to an inversion, the inverted pair is saved and the algorithm moves to the next pair of adjacent buckets.

At the end of the round, all identified inversions are considered and used to extend the backbone. Then InversionSort splits existing buckets by pivoting with new elements on the backbone. Because there is at most one pair of inversions between each two neighboring representatives on the backbone, each element is compared to at most two new representatives in each round.

This reestablishes the backbone and creates some new pairs of neighboring buckets, for which we initialize the inversion finding procedures. Existing buckets (identified by the representative) might get smaller. Here, a new inversion finding might reuse some of the already established samples and their structure. In the analysis we present here, this is not used, so for the sake of simplicity, we assume the algorithm starts from scratch.

The algorithm stops once all neighboring pairs of buckets are no longer active, i.e., shown to not have an inversion. In this case, the current buckets form the stripes of the instance. The algorithm finishes by sorting these buckets (including the representatives) using an optimal number of additional monochromatic comparisons.

## 3 InversionSort Analysis: Proof Structure

The analysis of InversionSort constitutes the technically challenging part of the paper. Let us visualize a run of InversionSort as a ternary (refinement) tree, where nodes correspond to subproblems. For an internal node _v_, there is a corresponding subinterval on the backbone defined by two consecutive pivots, say a blue pivot followed by a red pivot, _b<sub>v</sub>\<r<sub>v</sub>_. If InversionSort finds an inversion _y\<x_ (_x_ is blue and _y_ is red) between _b<sub>v</sub>_ and _r<sub>v</sub>_, then _v_ has three children with the respective pivots (_b<sub>v</sub>,y_), (_y,x_), (_x,r<sub>v</sub>_). Note that at a snapshot somewhere during a run of InversionSort, the tree explored so far may be far from being a complete tree - InversionSort could be stuck on a large-sized problem in one region, while refining and working way down a descendant of an interval in another region. Hence InversionSort does not proceed layer-by-layer on this tree.

The random nature of the inversion searching of InversionSort, as made precise in Lemma 9 leads to the following insight:

**Theorem 5** (Height of the refinement tree)**.** _Let_ T _be the refinement tree of running InversionSort on an instance_ I _with N=n+m elements. With high probability in N, the height of_ T _is O_(log_N)._

As a second challenge in the analysis, because of the overlapping nature of the problem, InversionSort cannot easily focus on elements between neighboring representatives. For example, for the child indicated by pivots (_y,x_), instead of only getting the reds and blues that actually lie in this range as input, InversionSort instead has to also work with the red elements contained in (_b<sub>v</sub>,y_) and the blue elements inside (_x,r<sub>v</sub>_). This "spill-in" from the neighboring subintervals on the backbone needs to be analyzed. See Figure 1 for an example. Thus we distinguish between _subinstances_ and _subproblems_.

As we will argue, the cost of inversion search procedure of InversionSort is justified by the subinstance between the neighboring elements on the backbone. However, if the spill-in for this subproblem is too large, inversion search is too costly. Hence, we will identify subproblems that do<tbc>


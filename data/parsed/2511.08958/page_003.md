#### Relation to the preprint.

An earlier version of this work is available as arXiv:2511.08958v2 \[2\]. That version already contains the two-pass dense and dominance-based algorithms. The present treatment consolidates their proofs and positioning, includes the formal padding reduction, and supplies a newly implemented and measured reproducibility package. The two algorithms are not claimed as additions relative to that preprint.

## 2. Related work and the endpoint interface

Classical longest common subsequence algorithms exploit either a dense position grid or the set of equality matches. Hunt and Szymanski \[3\] established the importance of the latter parameterization. The value constraints in LCIS and LCBS require information beyond the two position orders, but do not make the sparse viewpoint new.

Yang, Huang, and Chao \[4\] give a quadratic LCIS algorithm. Chan et al. \[5\] explicitly exploit the number of matching pairs. For two length-_N_ sequences, their LCIS bound is \(O(min\{Mlog\ell,N\ell+M\}loglogN+Sort(N))\), where \(\ell\) is the LCIS length, with logarithms conventionally bounded below by a constant. Kutz et al. \[6\] give an output-dependent expected bound in terms of LCIS length and alphabet size. These results are essential comparisons: match sensitivity and sparse LCIS processing predate the present formulation. Our \(Mlg_+^2M\) bound is not an improvement over the best LCIS bounds, and we do not claim it is the best achievable LCBS bound after adapting those algorithms.

**Proposition 2.1. (Endpoint lifting)**

Suppose an LCIS procedure reports the increasing endpoint length at every match of two sequences, with a predecessor match witnessing each nontrivial value. Two calls to that procedure, one on the original inputs and one on the reversed inputs, followed by _O(M_) work, solve LCBS and reconstruct an optimal subsequence. If _T_ and _W_ bound the time and workspace of each call, including endpoint reporting, the combined computation takes _O(T+S+M_) time and _O(W+S+M_) space.

#### Proof:

Reversal maps a decreasing suffix at (_i,j_) to an increasing prefix at (_n_+1-_i,m_+1-_j_) without changing values. Retain the first call’s _O(M_) endpoint records while making the second call. Select a peak by (1), and concatenate its two witnesses after removing one copy of the peak. The validity of this concatenation is proved in Lemma 3.1 below. Reversal, alignment by counting sort on match coordinates, scanning, and reconstruction cost _O(S+M_) additional time and space. \(\sqcap\sqcup\)

Proposition 2.1 is a two-pass reuse of LCIS with an explicit output requirement. A global LCIS length or one optimal witness does not supply the required per-match scores and immutable predecessor witnesses. Importing a faster LCIS bound requires accounting for these outputs in both calls; adaptive parameters such as the LCIS length may differ after reversal. Our direct dominance implementation makes these costs explicit.

For example, if both inputs equal \(\langle 9,8,7,6,1,2,3,4\rangle\), their LCIS and longest common decreasing subsequence lengths are four and five. Adding these global lengths and subtracting one gives eight, whereas LCBS has length five. The independently optimal halves cannot be joined at a common peak. Endpoint compatibility is therefore necessary even though its implementation uses familiar tools.


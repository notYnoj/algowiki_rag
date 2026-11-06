**Lemma 3.1. (Common-peak decomposition)**<br>
Equation (1) holds, and its maximizing match together with witnesses for (3) and (4) reconstructs an LCBS.

**Proof:**<br>
Fix an embedding of a nonempty bitonic common subsequence and let _v_ be its peak match. The prefix ending at _v_ has length at most _I(v_) and the suffix starting at _v_ has length at most _D(v_), so the full length is at most _I(v_)+_D(v_)-1. Conversely, concatenate optimum witnesses for these two states. Every nonpeak prefix match lies strictly before _v_ in both inputs, and every nonpeak suffix match lies strictly after _v_. Thus the embeddings do not conflict. The values strictly increase to _a(v_) and then strictly decrease, giving a feasible subsequence of the claimed length. Singleton and monotone witnesses are included. If _V_ is empty, only the empty subsequence is feasible. \(\sqcap\sqcup\)

Pinters must identify a fixed match record, not a mutable column buffer. Following predecessor pointers strictly decreases both input positions; following successor pointers strictly increases them. Hence reconstruction terminates, visits exactly the reported number of elements, and costs time linear in the output length. Equal values may appear on opposite sides of the peak, but never as adjacent steps within a strict monotone half.

## 4. A constructive quadratic baseline

The baseline adapts the LCIS row scan to report every match state. At the start of row _i_, _d[j_] is the maximum increasing endpoint length at column _j_ using rows smaller than _i_. The buffer _e[j_] identifies a fixed match attaining that value. Within the row, a running maximum records the best eligible earlier column with value smaller than _A[i_].

**Lemma 4.1.** Algorithm 1 reports all increasing endpoint lengths and valid immutable predecessor matches in _O(S+nm_) time and _O(S+M_) auxiliary space, including storage for the inputs’ reversed copies. For positive _n,m_, its scan takes \(\Theta(nm)\) time.

**Proof:**<br>
Before processing column _j_, _b_ is the maximum of _d[k_] over _k\<j_ with _B[k]\<A[i_]. Only columns whose value equals _A[i_] can have been updated in the current row. They are ineligible for this running maximum, so every eligible _d[k_] still describes an earlier row. Thus _b_+1 is exactly (3), and _q_ is a valid predecessor. Updating _d[j_] preserves its maximum-over-rows meaning. Induction on rows and columns proves the invariant. There are _nm_ constant-time scan steps, _m_ buffer entries, and _M_ fixed endpoint records. Match records can be assigned array identifiers as they are encountered. \(\sqcap\sqcup\)

Every match gets a record, even when its candidate does not improve the column maximum. This is essential for joining at later peaks with repeated symbols. Run the scan again on reversed inputs, map each match back to the original coordinates, and apply Proposition 2.1. The resulting constructive baseline has the same asymptotic bounds. Its _O(M_) witness storage is not a linear-space reconstruction claim.


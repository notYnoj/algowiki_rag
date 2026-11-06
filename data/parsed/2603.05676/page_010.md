<tbc>_Proof._ The range of indices between the midpoints of _R_<sub>3</sub> and _R_<sub>1</sub> comprises the power intervals _I_<sub>3</sub> and _I_<sub>2</sub>. Since the merge occurred, _p_<sub>3</sub>_\>p_<sub>2</sub>. From the first part of Observation 3, the distance between the indices of these two powers is at least _n/_2<sup>_p_<sub>3</sub>+1</sup>. The proof results from the fact that the nodes containing _p_<sub>2</sub> and _p_<sub>3</sub> are in _I_<sub>2</sub> and _I_<sub>3</sub> respectively. \(\sqcap\sqcup\)

**Lemma 3.** _If_ \(r_3\ge n/2^{p_2}\)_, then_ \(p_3\le p_2\).

_Proof._ Follows directly from Observation 4. \(\sqcap\sqcup\)

**Lemma 4.** _During PowerSort’s main loop, so long as the stack has at least two entries, we always know r_<sub>2</sub>.

_Proof._ Any new _R_<sub>2</sub> was either previously labeled _R_<sub>1</sub>, whose length is known (Observation 1), or is the result of a merge. \(\sqcap\sqcup\)

From Observation 1 and Lemma 4, we always know _r_<sub>1</sub> and _r_<sub>2</sub> when testing PowerSort’s merge condition. Thus, Lemma 3 defines our stopping condition and shows that failed merges incur a walk-back cost of at most _n/_2<sup>_p_<sub>2</sub></sup>.

**Lemma 5.** _The total walk-back cost of failed merges in PowerSort is O(m+n)._

_Proof._ Consider two runs, _q_ and _s_, such that _s_ appears directly above _q_ in the stack. Their respective powers are _p<sub>q</sub>_ and _p<sub>s</sub>_. Say _q_ currently has label _R_<sub>3</sub>, _s_ has label _R_<sub>2</sub>, and we are about to test the merge condition between them. Say we find that |_q|\>n/_2<sup>_p<sub>s</sub>_</sup>; by Lemma 3, the merge condition fails, we exit the walk-back algorithm and terminate the merge sequence. What can we charge this walk-back cost of _n/_2<sup>_p<sub>s</sub>_</sup> to?

We consider two cases. In case 1, _q_ is never part of a failed merge again. Then we can charge this cost to _q_ itself since |_q|\>n/_2<sup>_p<sub>s</sub>_</sup>. Over all runs, _q_, this adds at most (_m+n_) to the walk-back cost as _q_ may be original or intermediate.

In case 2, _q_ will be part of another failed merge. This means that _q_ will have to take the label _R_<sub>3</sub> again, which implies that _s_ gets merged during the main loop. When _s_ is merged, _q_ has label _R_<sub>4</sub> and _s_ has label _R_<sub>3</sub>. By Observation 6, the distance between the midpoints of _R_<sub>3</sub> and _R_<sub>1</sub> is at least _n/_2<sup>_p<sub>s</sub>_+1</sup>. This implies that \(r_1/2+r_2+r_3/2\ge n/2^{p_s+1}\), so \(r_1+2r_2+r_3\ge n/2^{p_s}\). For simplicity, we upper bound this as 2(_r_<sub>1</sub>+_r_<sub>2</sub>+_r_<sub>3</sub>).

We can charge our cost of _n/_2<sup>_p<sub>s</sub>_</sup> to twice the sizes of the current runs with labels _R_<sub>1</sub>, _R_<sub>2</sub>, and _R_<sub>3</sub>. All three runs are charged in this way once. For _R_<sub>2</sub> and _R_<sub>3</sub>, this is because they are immediately merged and so destroyed. For _R_<sub>1</sub>, recall that we assume that _q_ fails its merge condition, so the merge sequence is subsequently terminated. When a merge sequence finishes, we push a new run onto the stack, shifting the run labeled _R_<sub>1</sub> to _R_<sub>2</sub>. There is no way for this run to ascend back to _R_<sub>1</sub>, so it is charged as _R_<sub>1</sub> once.

As a result, this case charges each run seen during the main loop twice its length at most three times (i.e., when labeled _R_<sub>1</sub>, _R_<sub>2</sub>, and _R_<sub>3</sub>). This contributes an additional _O(m+n_) to the total walk-back cost of failed merges. \(\sqcap\sqcup\)


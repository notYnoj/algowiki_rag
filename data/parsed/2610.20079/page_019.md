includes the child’s output and stack transfers. There are only a fixed number _S_ of children, so suspension and restoration cost _O_(1) per node. Only the active call holds buffers; ancestors and inactive streams stay on disk. Hence

\(Q(e,V)\le SQ(e/m,V/W)+O\big(1+\frac{V}{Bw}\big).\)

Temporary copies occupy only a fixed number of additional stream regions. They do not change the division of the original _V_ bits among the _W_ independent streams. This proves the one-level bound and its memory and space guarantees.

## 6.3 The Recursion Bound

Recursion stops when all field-value combinations can be buffered. Two fields of width _e_ have _q_<sup>2_e_</sup> combinations, so one block per combination requires _q_<sup>2_e_</sup>_B_ words. Taking \(t=\lfloor\frac{1}{8}log_q(M/B)\rfloor\) makes these buffers fit in a small fraction of memory whenever \(e\le t\); increase the fixed constant _R_<sub>0</sub> so that \(t\ge 1\).

Each recursive level divides width by _m_. To first analyze widths that reach a common stopping threshold exactly, choose the largest power of _m_ not exceeding _t_, namely \(t_0=m^{\lfloor log_mt\rfloor}\), and consider _e=t_<sub>0</sub>_m<sup>k</sup>_. Since \(t_0\le t<mt_0\) and _m,q_ are fixed, we still have \(t_0=\Theta(a)\). Write _Q(e,V_) for the cost of interchanging two base-_q_ fields of width _e_ in a _V_ -bit array.

**Lemma 6.3** (Interchange at recursive scales)**.** If _e=t_<sub>0</sub>_m<sup>k</sup>_ and the number of prefix segments is divisible by _W<sup>k</sup>_, then

\(Q(e,V)=O\big(1+\frac{V}{Bw}(e/t_0)^\tau\big).\) (18)

If \(e\le t\) or the array fits in the reserved memory, the interchange takes only _O_(1+_V/(Bw_)) block transfers.

_Proof._ If the field width \(e\le t\), set _Q=q<sup>e</sup>_ and distribute the data into _Q_<sup>2</sup> streams by field values (_H,D_), retaining (_p,g,z_) order within each stream. Reconstruct the output from these streams in (_p,D,g,H,z_) order. The number of buffer blocks satisfies \(Q^2\le(M/B)^{1/4}\) and fits in a fixed small fraction of memory.

Each stream leaves at most one partial block, giving an initial cost of _O(Q_<sup>2</sup>+_V/(Bw_)). Fix a small constant \(\mu>0\). If \(V\le\mu Mw\), process the data in memory. Otherwise, increasing _R_<sub>0</sub> ensures \(Q^2\le\mu M/B<V/(Bw)\). The base interchange therefore costs only _O_(1+_V/(Bw_)) block transfers.

By Lemma 6.2, width _e=t_<sub>0</sub>_m<sup>k</sup>_ reaches the base case after _k_ levels. The prefix divisibility condition ensures equal-length streams at every level. For a call too large for memory, \(V>\mu Mw\); choosing \(R_0\ge W/\mu\) ensures that each child handles at least \(V/W\ge Bw\) bits, so its constant startup cost is absorbed by its scan cost. Each child has 1_/W_ of its parent’s scan volume, and there are _S_ children, giving the multiplier \(\lambda=S/W\). Let _F<sub>k</sub>_ be the cost normalized by _V/(Bw_). Then

\(F_0=O(1),F_k\le\lambda F_{k-1}+O(1),F_k=O(m^{k\tau}).\)

The last bound uses (15). Calls that fit in memory stop earlier and only reduce the cost. Multiplying by the scan cost proves (18).

_Proof of Lemma 6.1._ Actual field widths and prefix counts need not satisfy these divisibility conditions. Lemma C.1 borrows a few high-order digits to form a prefix and decomposes the remaining<tbc>


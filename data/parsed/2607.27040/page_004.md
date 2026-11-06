## 4 Near-Optimal In-Place Sorting

by scanning _f_<sub>1</sub>_...f_<sub>_r_#</sub> ignoring buffer elements. This sequence is maintained as a sorted sequence by the structure in Section 2.2. The active frame elements define the _ordering invariant_ that maintains relative sorted order across segments: for any active element \(x\in S_i\), \(f'_i\le x\le f'_{i+1}\) (logical sentinels \(f'_0=-\infty\), \(f'_{s_\#+1}=\infty\)).

By the segment invariant, there are at least \(\lfloor s/2\rfloor\) active elements in each of the _s_#+1 segments, and also _s_# active elements reside in the frame. Because the total number of active elements cannot exceed _m_, we conclude that _s_# is at most

\(s_\#\le\lfloor(m-\lfloor s/2\rfloor)/(\lfloor s/2\rfloor+1)\rfloor\le\lfloor 2m/s\rfloor-1\) (2)

Consequently, the size of segment memory is bounded by:

\(|S|=(s_\#+1)s\le 2m\) (3)

Thus, the segment memory cannot surpass the reserved zone of size 2_m_.

Due to the arbitrary arrangement of the segments in the segment memory, we cannot easily locate the segment _S<sub>i</sub>_ corresponding with \(R'_i\). Thus, we introduce the **pointer memory** _P_ in _V_ , consisting of the _segment pointers P_<sub>1</sub>_...P_<sub>_r_#</sub>. Let the _active segment pointers_ be \(P'_1\dots P'_{s_\#}\), corresponding with the active representatives \(R'_1\dots R'_{s_\#}\). Each _P<sub>i</sub>_ is a block of \(\lfloor lg\lfloor 2m/s\rfloor\rfloor+1\) bits, sufficient to address any of the \(\lfloor 2m/s\rfloor\) blocks in the reserved zone by encoding an integer in binary: if \(P'_i=k\), then _S<sub>i</sub>_ occupies the block _B<sub>k</sub>_. For all segment pointers corresponding with a buffer representative, _P<sub>i</sub>_=0 representing a NIL pointer as there is no corresponding segment.

However, dereferencing a segment pointer would require \(\lfloor lg\lfloor 2m/s\rfloor\rfloor+1\) reads in _V_ using _O_(lg_m_) comparisons. To minimize overhead, we utilize one pointer dereference to operate upon a batch of _g_ elements, reducing the per-element cost of dereferencing pointers to _O_(lg_m)/g=O_(1) (see (4) below). Batch operations are facilitated by the **cache memory** _G_ using its _r_# _cache lines G_<sub>1</sub>_...G_<sub>_r_#</sub>, each a block of 2_g_ elements operating as a specialized structure used to accumulate _g_ active elements, where

\(lgm\le g\le 2lgm\) (4)

For now, assume that a cache line _G<sub>i</sub>_ is a black box that supports the operations _G<sub>i</sub>_.insert(_x_) and _G<sub>i</sub>_.flush(_x_). _G<sub>i</sub>_.insert(_x_) exchanges the active element at _x_ with a buffer element in _G<sub>i</sub>_, then returns a Boolean indicating whether _G<sub>i</sub>_ has become full. _G<sub>i</sub>_.flush(_x_) swaps the active elements in _G<sub>i</sub>_ with the contiguous block of buffer elements beginning at _x_. The cost of cache operations will be accounted for in _cache inserts_ (calls of insert) and _cache flushes_ (calls of flush). The exact implementation of cache lines is specified in Section 2.6.

Initially, all cache lines consist of only buffer elements. The _active cache line_ \(G'_i\) corresponding with \(R'_i\) temporarily stores active elements belonging in _S<sub>i</sub>_, waiting until it accumulates _g_ active elements so they are flushed into _S<sub>i</sub>_ as a batch. Thus, the ordering invariant that applies to _S<sub>i</sub>_ must also apply to \(G'_i\).

To support cache lines in their operations, the **cache data** _I_ in _V_ stores _r_# _cache integers I_<sub>1</sub>_...I_<sub>_r_#</sub>, each a block of \(\lfloor lgg\rfloor+1\) bits, used to store integers from 0 to _g_. Each cache line _G<sub>i</sub>_ may use its corresponding cache integer _I<sub>i</sub>_ to assist its operations.

To maintain a 1:1 correspondence between active representatives and segments, after a new segment is allocated, a corresponding active representative is constructed from a buffer representative _R<sub>i</sub>_ and an active element _x_ promoted to the frame. This requires _O_(lg_m_) moves: swap _x_ with _f<sub>i</sub>_ (which makes _R<sub>i</sub>_ active), then assign _P<sub>i</sub>_:=_s_# so it points to the _s_#th block in the reserved zone, i.e. the newly allocated segment.


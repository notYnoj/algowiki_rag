Testing whether a representative _R<sub>i</sub>_ is active requires a single comparison by active(_f<sub>i</sub>_). The rank of _R<sub>i</sub>_ is defined by its frame element, meaning _R<sub>i</sub>\<R<sub>j</sub>_ iff _f<sub>i</sub>\<f<sub>j</sub>_. To compare an active element _x_ and _R<sub>i</sub>_, compare _x_ and _f<sub>i</sub>_ directly. Exchanging two representatives _R<sub>i</sub>_ and _R<sub>j</sub>_ is done by exchanging each component individually: _f<sub>i</sub>_ with _f<sub>j</sub>_, _G<sub>i</sub>_ with _G<sub>j</sub>_, _P<sub>i</sub>_ with _P<sub>j</sub>_, and _I<sub>i</sub>_ with _I<sub>j</sub>_; the process requires _O_(lg_m_) comparisons and _O_(lg_m_) moves.

_S_<sub>0</sub> is unique in the sense that it has no corresponding active representative and is handled separately by the auxiliary pointers _l_<sub>0</sub> to the next buffer position in _S_<sub>0</sub> and _r_<sub>0</sub> to the end of _S_<sub>0</sub>.

## 2.2 Structure of Representatives

Let _R_ denote the collection of all _r_<sub>#</sub> representatives. We structure _R_ to support the operations _R._search(_x_) and _R._insert(_x_) efficiently. _R._search(_x_) finds the active representative \(R'_i\) such that \(f'_i\le x\le f'_{i+1}\), and returns its position in _R_, or 0 if \(x<f'_1\). _R._insert(_x_) adds a new active representative into _R_ for a newly allocated segment with _x_ as its active frame element. Full procedural descriptions and formal analysis of the operations are available in [App. A].

_R_ consists of the _library L_ at the front and the _rebuild buffer D_ at the back.

**The library** _L_ contains the sorted sequence of all active representatives interlaced with buffer representatives, which serve as slack space for efficient insertions. _L_ behaves like a dynamic array, beginning at the left of a reserved zone of \(8\lfloor 2m/s\rfloor\) buffer representatives and expands rightwards.

At any moment, the number of active representatives is _s_<sub>#</sub> as there are exactly _s_<sub>#</sub> active frame elements. Let \(s'_\#=2\lfloor lgs_\#\rfloor\le s_\#\) denote the number of active representatives at the previous resize. _L_ consists of \(s'_\#\) _gaps L_<sub>1</sub>_...L_<sub>_s_<sub>#</sub></sub>, each a block of 8 representatives \(\ell_1\dots\ell_8\). Using (2) to bound |_L_|

\(|L|\le 8s'_\#\le 8s_\#\le 8\lfloor 2m/s\rfloor\)

Each **gap** _L<sub>i</sub>_ has the form _a_<sub>1</sub>_...a<sub>k</sub>b_<sub>_k_+1</sub>_...b_<sub>8</sub>, where _a<sub>i</sub>_ are active representatives in sorted order and _b<sub>i</sub>_ are buffer representatives. The _gap invariant_ requires 0_\<k\<_8, so each gap contains at least one active and one buffer representative. The sequence \(L'_1\dots L'_{s_\#}\) where \(L'_i\) denotes the active representatives in _L<sub>i</sub>_ forms the global sorted sequence of all active representatives. At startup, _s_<sub>#</sub>=0, but we pre-allocate one gap _L_<sub>1</sub> containing only buffer representatives and set \(s'_\#=1\).


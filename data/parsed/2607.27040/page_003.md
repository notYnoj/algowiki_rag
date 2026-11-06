## 2 Sorting with Additional Memory

Before considering the full in-place algorithm, we address a simpler problem. We are given:

A contiguous block _A_ of exactly _m_ elements, called _active elements_.

A contiguous _buffer memory B_ of at least 3_m_-1 _buffer elements_. Buffer elements can be distinguished from active elements using 1 comparison. Formally, there exists a function active(_x_) that makes 1 comparison then returns a Boolean `true` if _x_ is an active element and `false` otherwise (i.e. _x_ is a buffer element).

A bit vector _V_ containing at least _m/_lg<sup>2</sup>_m_ bits, all initialized to `false`. The bit vector supports exclusively single-bit operations: _V_.read(_i_) costing 1 comparison which returns a boolean value indicating the value of the _i_th bit and _V_.write(_i_) which flips the _i_th bit costing 3 moves.

_O_(1) auxiliary words of width \(\ge\mathrm{lg}m\) bits and a single empty location, i.e. the _hole_; from the original in-place sorting setting.

The objective is to sort the _m_ active elements in _A_, making use of _B_ and _V_ as additional workspaces. When the program terminates, _B_ must be some permutation of its original elements, and _V_ must be reset to its initial blank state. Note that _B_ and _V_ serve as temporary mathematical abstractions of in-place mechanisms that will be fully detailed below in Section 3. If required, see [App. E] for a complete notation glossary.

### 2.1 Structure of the Memory

In this section we detail the high-level layout of our provided additional workspaces.

**The buffer memory** _B_ consists of three main sections arranged sequentially: the _frame memory F_, _cache memory G_ and _segment memory S_, retaining the frame-cache-segments organization established in [4]. **The bit vector** _V_ contains the _pointer memory P_ and the _cache data I_ arranged sequentially.

**The segment memory** _S_ forms the lower level of the structure, serving as the primary storage of active elements. The segment memory consists of _s_<sub>#</sub>+1 segments _S_<sub>0</sub>_...S_<sub>_s_<sub>#</sub></sub>, each a contiguous block of

\(s=2\lceil\mathrm{lg}m\rceil^3g-1\) (1)

elements, where \(g=\Theta(\mathrm{lg}m)\) is defined later in (4), giving us \(s=\Theta(\mathrm{lg}^4m)\). Physically in _S_, the segments are not necessarily stored sequentially in the order _S_<sub>0</sub>_...S_<sub>_s_<sub>#</sub></sub>; they can be arranged in any permutation with _S_<sub>0</sub> at the front. The _segment invariant_ mandates that each segment contains between \(\lfloor s/2\rfloor\) and _s_ active elements placed contiguously at the front.

Segments are dynamically allocated from a reserved zone of 2_m_ elements in _B_, divided into \(\lfloor 2m/s\rfloor\) blocks of _s_ elements \(B_0\dots B_{\lfloor 2m/s\rfloor-1}\) (any remaining elements at the end are excluded). Initially, there is only one segment _S_<sub>0</sub>. To allocate a new segment, we increment _s_<sub>#</sub> and return the next available block in the reserved zone (_B_<sub>_s_<sub>#</sub></sub>). Immediately after allocation, \(\lfloor s/2\rfloor\) active elements are moved into the new segment to fulfill the segment invariant.

Every segment _S<sub>i</sub>_ has a corresponding **active representative** \(R'_i\) in the upper level to coordinate routing into segments. These _s_<sub>#</sub> active representatives \(R'_1\dots R'_{s_\#}\) form a subset of _r_<sub>#</sub> pre-allocated _representatives_ denoted by _R_<sub>1</sub>_...R_<sub>_r_<sub>#</sub></sub>. Any remaining non-active representatives are classified as _buffer representatives_. Each representative _R<sub>i</sub>_ is a compound data type formed by _f<sub>i</sub>_, _P<sub>i</sub>_, _G<sub>i</sub>_ and _I<sub>i</sub>_ (defined shortly).

Specifically, the first component _f<sub>i</sub>_ is a _frame element_, and together _f_<sub>1</sub>_...f_<sub>_r_<sub>#</sub></sub> constitute the **frame memory** _F_. _F_ consists of _s_<sub>#</sub> active elements interleaved with buffer elements; _f<sub>i</sub>_ is active iff _R<sub>i</sub>_ is active. The _active frame elements_ form the sequence \(f'_1\dots f'_{s_\#}\) obtained


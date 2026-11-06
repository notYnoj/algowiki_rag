## A.2 Suspending and restoring recursive calls

OpenAI \[Ope26, Proposition 11, fixed-tape depth-first schedule\] explicitly parks inactive streams and restores them between child calls, charging this movement to the parent. Random disk access permits the following variant, in which inactive streams stay in place. This also specifies the transfer costs at call boundaries, which are not covered by the amortization within a single tape phase.

Each active call has a fixed number of disk regions: one for each stream assigned to a circuit register, together with temporary work tapes. Each region is packed and block-aligned, with its length and head position in the call descriptor. Regions belonging to different suspended calls are disjoint. The child reads one designated register stream of its parent as input; the child’s own register streams and work regions are allocated separately. Fresh work regions are initialized by scans within the _O(V_) local work budget. Only the active call owns the tape windows. Suspended calls have no resident buffers.

Before descending, finish the current local procedure, flush all dirty windows, and write a stack frame containing the parent dimensions, region addresses, head positions, the instruction to resume, and the child index. Adjacent irrelevant coordinates are collapsed, so this frame has a fixed number of machine words, independent of recursion depth. A frame occupies a fixed number of block-aligned disk blocks at the stack top; writing or reading it costs _O_(1) transfers even when _B_=1. The child then reuses the same window buffers and control workspace. All inactive parent streams remain on disk and are not traversed.

On return, write back the child’s windows and place its output in the designated parent register stream, using a scan of _V/W_ bits if a copy is needed. Read and remove the top stack frame, restore the parent’s descriptor, and reload its windows as needed. The child’s temporary regions can then be reused. No restoration scans an ancestor’s data or searches past another stack frame. Output copying costs _O_(1+_V/(WBw_)) per child; flushing, stack access, and window reactivation cost _O_(1) per child. The fixed number _S_ of children therefore adds _O_(1+_V/(Bw_)) transfers per parent node, with constants allowed to depend on the fixed circuit. It does not change the recursive volume multiplier _S/W_.

Together with Lemma A.1, this yields the node recurrence in Lemma 6.2. It also accounts for the constant overhead when a child reaches the stopping condition set by the available memory. The active windows, one stack-transfer buffer, and the descriptor occupy _c_<sub>1</sub>_B+c_<sub>2</sub> words for fixed constants _c_<sub>1</sub>_,c_<sub>2</sub>; the normalization below reserves this space. Ancestor regions and frames use polynomial disk space: a depth-first execution has depth _O_(log(2+_e_)), finitely many regions per level, and no level has volume larger than the padded root volume. All stored addresses therefore fit in a fixed number of machine words of width _w_.

## A.3 Constant-factor block simulation

The algorithms in the main text need a fixed number of block buffers. To cover cases such as _M_=2_B_, we reduce the simulated memory and block sizes, then perform transfers through one physical block buffer. Constant-factor adjustments preserve the complexity bounds.

**Lemma A.2** (Constant-factor block simulation)**.** For fixed constants \(R_0\ge 2\) and _C_<sub>0</sub>, there are fixed constants _K,C_<sub>∗</sub> such that, for every \(M\ge max\{2B,C_*\}\), setting

\(\widehat{M}=\lfloor M/4\rfloor,\widehat{B}=max\{1,\lfloor B/K\rfloor\},\)

gives \(\widehat{M}\ge C_0\) and \(\widehat{M}/\widehat{B}\ge R_0\). An algorithm using \(\widehat{M}\) words of memory and blocks of \(\widehat{B}\) words can<tbc>


<tbc>\(\phi(v_k\mathrm{mod}2)=\phi(b_k)\) in constant depth. A constant-depth equality test against the constants \(\phi(0)\) and \(\phi(1)\) selects the token `0/1` to be emitted, along with \(\phi(v_{k+1})\) as a soft token to be used at the next position. After _w_ steps the emitted tokens are exactly _b_<sub>0</sub>_,...,b_<sub>_w_-1</sub>, along with soft tokens for intermediate \(\phi(v_k)\) values.

**Lemma 7** (Step 5: deserialization)**.** _There exists a log-precision, finite-width continuous-CoT transformer that, on bit sequence b_<sub>0</sub>_,...,b_<sub>_w_-1</sub> _followed by w arbitrary tokens, computes_ \(\phi(v)\) _in the residual stream at the last step, where_ \(v=\sum_{k=0}^{w-1}b_k2^k\) _is the LSB evaluation of b._

Phase 6: Emit store-summary / checkpoint
(bookkeeping)
Phases 3-5 collapse into Block 3 of Fig. 4.
Soft token
Phase 5: Deserialize outputs to Φ(.)
Lem. 7
aux
one RAM step (O(((() steps)
Phase 4: Instruction oracle (TM)
Lem. 6
Phase 3: Serialize inputs to bits
Lem. 5
Φ(a)
Phase 2: Dereference operand addresses
Lem. 4
Φ(v)
Phase 1: Load pc
(bookkeeping)
aux
O(1) dim.
soft token: O(1) aux codes
Attends to full context
input
prev. step
ckpt
wts
bo
bw-1
oracle work
co
Cw-1
ckpt'
CoT transcript
work-tape suffix (used by the oracle)

Figure 5: **Phase structure and CoT transcript view** of one RAM step in the CCoT (continuous CoT) simulation; counterpart to Fig. 4. _Phases (center):_ unlike the log<sup>2</sup>-width construction in which one CoT step executes four constant-depth layer blocks, in the CCoT simulation a single RAM step expands across \(O(\kappa(w))\) decoding steps grouped into six conceptual phases (cf. the proof overview of Thm. 3). Phase 1 forms \(\phi(0)\) and reads the current \(\phi(\mathrm{PC})=\phi(\mathrm{mem}[0])\) from the rightmost matching store-summary, selecting the active instruction (under the unified memory convention, the program counter and registers all live at fixed addresses in `mem`, so reads use a single dereferencing primitive). Phase 2 dereferences each memory operand `mem`\[_a_\] by forming \(\phi(a)\) and retrieving \(\phi(v)\) from the rightmost matching store-summary (Lem. 4). Phase 3 emits the _w_ bits of each operand onto the transcript while keeping its \(\phi(\cdot)\) code in the soft token (Lem. 5). Phase 4 runs the instruction-specific TM oracle on the work-tape suffix, which streams output bits over \(O(\kappa(w))\) decoding steps (Lem. 6). Phase 5 converts each output bit stream back to \(\phi(\cdot)\) for future addressing/equality (Lem. 7). Phase 6 emits a store-summary token for each write the instruction performs to `mem` (including writes to address 0 for the new `pc` and to addresses -1,-2_,..._ for any updated registers), followed by an end-of-step checkpoint, re-establishing the transcript invariant. The dashed purple rectangle marks Phases 3-5, which together implement the bit-serial execution of the instruction; in the fixed-precision (polylog-width) construction these three phases collapse into a single constant-depth MLP block (Block 3 of Fig. 4), since values can be manipulated directly as _w_-bit residual-stream slots without the serialize/oracle/deserialize round trip needed to expose them as _w_ discrete tokens. _CoT transcript (bottom):_ the prev. checkpoint (green) carries the cached state in its soft token; serialized operand bits, the oracle’s work region, and the deserialized output bits form the work-tape suffix; the rightmost `ckpt`’ (red) is the new checkpoint emitted at the end of this step. _Soft token (right):_ the residual stream carries a constant number of _O_(1)-dimensional codes \(\phi(\cdot)\), in contrast to the _w_-dimensional bit slots of Fig. 4. Under the unified memory convention, no slot is reserved for a specific register: highlighted slots \(\phi(a),\phi(v)\) (red) hold the address being looked up and the value being loaded/written at the current step, and remaining slots are generic _O_(1) scratch (_aux_) used inside bit-serial routines.


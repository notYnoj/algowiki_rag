<tbc>_for_ \(\mathcal{O}(\kappa(w))\) _decoding steps and emits the output bit streams of I onto the transcript. Moreover, the subnetwork can be made to ignore the rest of the transcript by delimiting a_ work-tape suffix _(with a start marker) and restricting all attention inside the subroutine to positions in that suffix._

**Lemma 7** (Step 5: deserialization)**.** _There exists a log-precision, finite-width continuous-CoT transformer that, on bit sequence b_<sub>0</sub>_,...,b_<sub>_w_-1</sub> _followed by w arbitrary tokens, computes_ \(\phi(v)\) _in the residual stream at the last step, where_ \(v=\sum_{k=0}^{w-1}b_k2^k\) _is the LSB evaluation of b._

**Step 6: storing new values.** We emit a soft token encoding the target position to write to (from load step) as _k_ and the output value (from deserialize) as _v_. This completes the store step, satisfying our inductive invariant for step _s_+1, which completes the proof.

We have the following consequences of Thm. 3, depending on the complexity of the instruction set:

**Corollary 2** (Simulating Word RAMs with CCoT)**.** _Let M and T be as in Thm. 3. Depending on the complexity of the instruction set_ \(\kappa(w)\) _of M, the following hold:_

(_i)_ _T can simulate t steps of M with arbitrary poly(w)-time instructions using_ \(\tilde{\mathcal{O}}(t)\) _steps._<tbc>

(_ii)_ _T can simulate t steps of M with_ full-arithmetic _flat instructions using_ O(_t_log<sup>2</sup>_t_) _steps._<tbc>

_(iii)_ _T can simulate t steps of M with_ simple-arithmetic _flat instructions using_ O(_t_log_t_) _steps._

## 6 Simulating Word RAMs with Hybrid Models

Finally, we show that, similarly to using CCoT, leveraging hybrid models that mix transformer and linear RNN components allow simulating a Word RAM:

**Theorem 4** (Simulating Word RAMs with Hybrid Models)**.** _Let M be a c-dimensional-array Word RAM with word size w_=log(_n+t_)+O(1) _and maximum instruction cost_ \(\kappa(w)\)_. Then there exists a log-precision, fixed-width hybrid model H with a single RNN layer at the bottom such that, for any_ \(t\ge n\)_, t steps of M can be simulated by H using_ \(\mathcal{O}(t\kappa(w))\) _steps._

Let \(v=\sum_{k=0}^{w-1}b_k2^k\). The proof of this theorem is structurally identical to that of Thm. 3 for transformers with _continuous_ CoT, except for the way values _v_, represented as \(\phi(v)\) in the residual stream, are serialized as bits _b_<sub>0</sub>_,b_<sub>1</sub>_,...,b_<sub>_w_-1</sub> via CoT, and the way bits _b_<sub>0</sub>_,b_<sub>1</sub>_,...,b_<sub>_w_-1</sub> in the input layer are deserialized as \(\phi(v)\) in the residual stream. Since we no longer have access to soft tokens in the CoT output, we cannot simply emit intermediate \(\phi\) representations as part of the CoT to condition<tbc>

Phase 6: Emit store-summary / checkpoint
(bookkeeping)
Phases 3-5 collapse into Block 3 of Fig. 4.
Soft token
Phase 5: Deserialize outputs to Φ(.)
Lem. 7
one RAM step (O((w) steps)
aux
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
soft token: O(1) aux codes
aux
O(1) dim.
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
ckpt
CoT transcript
work-tape suffix (used by the oracle)

Figure 2: Six-step CCoT simulation of a RAM instruction; detailed caption in Appendix, Fig. 5.


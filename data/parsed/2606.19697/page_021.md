• _Addition and subtraction_: implementable by a constant-depth AC<sup>0</sup> circuit (Straubing, 1994, §VIII.1), and thus by an MLP.<tbc>

• _Comparison_ (\(<,\le,=,\neq,\ge,>\)): reduced to subtraction and sign extraction.<tbc>

• _Boolean and conditional_ operations: computed in _O_(1) depth from the Boolean bits in the residual stream.<tbc>

• _Move and branch targets_: the result is a hard-coded constant or a copy of an operand value already in the residual stream.<tbc>

• _Inner iteration of_ \(\times\)/\(\div\)/mod: the MLP executes one iteration of the long-multiplication or long- division algorithm using the per-iteration intermediates (partial product, remainder, quotient, phase counter) read in Block 2 from program-private memory addresses, and produces their updated values as additional destination words (Prop. 7).

Block 3 always computes, in addition, the next `pc` value \(\mathrm{bits}(\mathrm{pc}')=\mathrm{bits}(\mathrm{mem}[0])+\mathrm{bits}(1)\) (or a hard-coded branch target if _I<sub>p</sub>_ is a branch); this value is written to address 0 by Block 4. Block 3 uses no attention, and the destination values remain stable at every CoT position of the same step since the operands are fixed and Blocks 1-2 recover the same values each time.

**Proposition 6** (Store results)**.** _Suppose that at every & position_ \(s_\unknown\)_, the full snapshot for the next step--the set of destination addresses_ {_a<sub>d</sub>_} _together with_ bits(_a<sub>d</sub>_) _and the corresponding result words_ bits(_v<sub>d</sub>_)_--is in the residual stream (from Blocks 1-3 evaluated at_ \(s_\unknown\)_). Then T can, at every position_ \(t>s_\unknown\) _within the step, attend to the rightmost &, compute the offset_ \(\delta=^\mathrm{def}t-s_\unknown\)_, and emit the correct_ \(\delta^\mathrm{_th}\) _token of the step’s serialization (a `mem` marker, a # marker, an address bit, a value bit, or the closing &) in constant depth, using one attention layer and one MLP._

_Proof._ **Anchoring at the most recent &.** By construction, & tokens partition the transcript into steps: each step’s serialization is a run of _Cw+D_ tokens following an & (and ends with the next &), where _C_=2_K_ and _D_=3_K_+1 for _K_ the (program-determined) number of memory blocks committed by the active step. An attention head issues a query matching the & token type via Lem. 13, uniquely attending to the rightmost & at position \(s_\unknown<t\) (or to the input boundary token at the very first step). The retrieved value vector is the positional encoding \(\mathrm{PE}(s_\unknown)=\mathrm{bits}(s_\unknown)\). A subsequent MLP computes the within-step offset \(\delta=^\mathrm{def}t-s_\unknown\) from PE(_t_) and \(\mathrm{bits}(s_\unknown)\); this difference ranges over {1_,...,Cw+D_}. The same attention head also retrieves, from the residual stream at \(s_\unknown\), the snapshot (the destination addresses bits(_a<sub>d</sub>_) and result values bits(_v<sub>d</sub>_) for every memory block of the current step, in fixed order) that Blocks 1-3 produced at \(s_\unknown\).

**Selecting and emitting the** \(\delta^\mathrm{th}\) **token.** The serialization layout of a step is fixed once dispatched: a sequence of memory blocks of the form `mem` # \(\langle w\) address bits\(\rangle\) # \(\langle w\) value bits\(\rangle\) at known offsets, followed by a closing &. The MLP converts \(\delta\) to its one-hot encoding \(\mathbf{e}_\delta\in\{0,1\}^{Cw+D}\) and uses it to select among:

(1) the `mem` token when \(\delta\) is the offset of the start of a memory block;<tbc>

(2) a # marker when \(\delta\) is the offset of an address-field or value-field start;<tbc>

(3) an address bit \(b_j=\mathrm{bits}(a_{\mathrm{block}(\delta)})^\top\mathbf{e}_{j(\delta)}\) (Svete and Cotterell, 2024, Lem. B.1) when \(\delta\) falls inside an address field;<tbc>

(4) a value bit \(b_j=\mathrm{bits}(v_{\mathrm{block}(\delta)})^\top\mathbf{e}_{j(\delta)}\) when \(\delta\) falls inside a value field, where \(\mathrm{block}(\delta)\) and \(j(\delta)\in\{1,\dots,w\}\) are the block index and intra-field bit index determined from \(\delta\) alone;<tbc>

(5) the closing & when \(\delta=Cw+D\), which simultaneously triggers the next step’s full Block 1-3 evaluation at that position.

The selected token is emitted as the output at position _t_.

**Why the snapshot is reliable at & positions.** Blocks 1-3 are run at every position _t_ uniformly; what changes across positions is the prefix they see. At an & position \(s_\unknown\), all rightmost-address reads see the previous step’s committed memory blocks (no half-written block of the new step has yet been emitted), so the operand reads are unambiguous and Blocks 1-3 produce the correct snapshot for the next step. At any non-& position within the step’s serialization, the same machinery runs but its rightmost-match reads now collide with the partially emitted memory block of the current step: in particular, a read for any destination address _a<sub>d</sub>_ would retrieve the (possibly partial) freshly written<tbc>


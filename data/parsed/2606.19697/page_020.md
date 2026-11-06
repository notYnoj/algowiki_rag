**Proposition 3** (Load `pc`)**.** _Let T be a rightmost UHAT with_ log<sup>2</sup> _width and finite precision, and suppose the serialization format above is in use. At every CoT position t, T can recover_ bits(_mem_\[0\]) _from the transcript and place it in a dedicated residual-stream subspace using two attention layers._

_Proof._ The query address is the constant 0, hard-coded into the transformer weights and available in the residual stream as bits(0). A single application of Lem. 12 with this query retrieves bits(mem\[0\]): the first attention layer matches the rightmost `mem` block whose address field encodes 0 and extracts the position of the matching block; the second attention layer attends to the value field of that block and assembles its bits, via Lem. 11, into the dedicated bits(`pc`) subspace. If no such block exists, the override of the previous paragraph produces the program-supplied initial `pc` value bits(PC<sub>start</sub>).

**Proposition 4** (Load instruction and operands)**.** _Let T be a rightmost UHAT with_ log<sup>2</sup> _width and finite precision, and suppose_ bits(_mem_\[0\]) _is in the residual stream (from Block 1). Then T can identify the active instruction and load all its operands into designated residual-stream slots in four attention layers._

_Proof._ **Operand descriptor.** Every flat Word RAM instruction _I<sub>p</sub>_ is equipped with a static _operand descriptor_: a list of memory addresses to read. The descriptor partitions the addresses into

• _compile-time addresses_ \(A_p^\text{ct}\subseteq[2^w-1]\): integer constants known at program-compile time (the registers -_i_, the `pc` address 0, and any program-private scratch addresses used by _I<sub>p</sub>_);<tbc>

• _runtime addresses_ \(A_p^\text{rt}\): addresses of the form `mem`\[_a_\] or `inp`\[_a_\] where _a_ itself is the value at some compile-time address.

The descriptor is a _compile-time constant_: it depends only on the instruction type, not on the runtime values, so it is hard-coded into the weights of _T_.

**Sub-step 2a: Instruction identification and compile-time reads.** With bits(mem\[0\]) in the residual stream, a constant-depth MLP computes the match bit

\(\delta_p=^\text{def}\unknown[bits(mem[0])=bits(p)]\in\{0,1\}\)

for every program address \(p\in\{0,\dots,P-1\}\) simultaneously (each bits(_p_) is a hard-coded weight constant). The weights of _T_ contain _P_ attention-head groups H<sub>0</sub>_,...,_H<sub>_P_-1</sub>, one per program line. All _P_ groups run in parallel: each group H_<sub>p</sub>_ issues, for every compile-time address \(a\in A_p^\text{ct}\), one indexed read via Lem. 12 with the constant query bits(_a_), writing the retrieved bits(mem\[_a_\]) into a dedicated disjoint subspace of the residual stream. Each indexed read uses two attention layers (address matching, then value retrieval), and all _P_ groups run as parallel heads within those same two layers. A subsequent MLP gated by \(\delta_p\) copies the active group’s operands from their dedicated subspace into the shared operand slots, leaving the other subspaces unused. After Sub-step 2a, every compile-time operand of _I<sub>p</sub>_ occupies its designated slot.

**Sub-step 2b: Runtime reads.** For each runtime address in \(A_p^\text{rt}\), the address value bits(_a_) resolved in Sub-step 2a is now in the residual stream and serves as the query for a second indexed read: Lem. 12 for `mem`\[_a_\], or a direct positional attention to input position _a_ for `inp`\[_a_\]. By the _flat_ Word RAM constraint, no runtime address is itself memory-indirect, so two more attention layers suffice. After Sub-step 2b, all operands required by _I<sub>p</sub>_ reside in their designated residual-stream slots and are ready for Block 3.

The total depth of Block 2 is four attention layers plus a constant number of MLP layers.

**Proposition 5** (Execute instruction)**.** _Suppose all operands of instruction I<sub>p</sub> reside in their designated residual-stream slots (from Block 2). Then T can compute, in constant depth using a single MLP with no attention, the w-bit value_ bits(_v<sub>d</sub>_) _to be written to each address a<sub>d</sub> that I<sub>p</sub> updates, including the next `pc` value_ \(bits(\text{\textit{\textbf{pc}}}')\).

_Proof._ With all operands \(bits(a),bits(b)\in\{0,1\}^w\) in the residual stream, the active gated MLP subnetwork N_<sub>p</sub>_ computes the destination value(s) bits(_v<sub>d</sub>_) directly:

• _Bitwise operators_ (&, \(|,\oplus,\checkmark,\gg\)): each _v<sub>t</sub>_ is an _O_(1)-depth Boolean function of _a<sub>t</sub>_, _b<sub>t</sub>_ (and a hard-coded shift amount), computed in one MLP layer.<tbc>


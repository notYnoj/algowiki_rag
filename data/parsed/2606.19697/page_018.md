**What one CoT step does.** The construction decomposes each CoT step into four consecutive _layer blocks_, each handled by a constant-depth subnetwork.

**Block 1: Load pc (Prop. 3).** A single indexed read (Lem. 12) with query address 0 retrieves bits(mem[0]) from the transcript, recovering the current pc value into a dedicated residual-stream subspace. The indexed read uses two attention layers (address matching against the rightmost mem block with _a_=0, then value retrieval).

**Block 2: Load Instruction and Operands (Prop. 4).** Each instruction _I<sub>p</sub>_ in the program declares a fixed _operand descriptor_--a static list of memory addresses it reads--which the program supplies and is hard-coded into the transformer weights. The list contains two kinds of addresses: _compile-time_ addresses (the registers -_i_ and any program-private scratch cells used by _I<sub>p</sub>_) and _runtime_ addresses (memory or input cells whose index mem[_a_] or `inp[a_] is itself the value of another address that must be read first).

Residual Stream
Block 4: Store Results
Props. 6 and 7
am
Block 3: Execute Instruction
Props. 5 and 7
address/value slots for current step
one CoT step
attend to last &; copy result
Block 2: Load Instruction and Operands
Prop. 4
bit 8
Block 1: Load PC
Prop. 3
results
a1
w dim.
Attends to full context
input
prev. instr.
&
mem
#
a1
aw
#
b1
b8
CoT transcript
offset 8 from last &

Figure 4: **Layer-block structure and CoT transcript view** of one step in the log<sup>2</sup>-width simulation. _Layer blocks (center):_ each CoT step executes four constant-depth blocks. Block 1 reads bits(mem[0]) (the pc) via one indexed memory read in two attention layers (Prop. 3). Block 2 uses two more sequential attention layers: the first identifies the active instruction and reads its compile-time operand addresses; the second resolves any runtime (mem[_a_] or `inp[a_]) addresses (Prop. 4). Block 3 is a pure MLP that computes the destination value(s) and the next pc from the operands now in the residual stream (Prop. 5). Block 4 attends to the rightmost & to compute the within-step offset \(\delta\), copies the snapshot precomputed by Blocks 1-3 at that &, and emits the appropriate \(\delta^\text{th}\) token (mem, #, address bit, value bit, or closing &) into the transcript (Prop. 6). _CoT transcript (bottom):_ the input and previous steps are followed by the & that opens the current step (where Blocks 1-3 produced and cached the snapshot, depicted by the green badge), then the current step’s memory-block serialization; \(b_\delta\) (red) is the token emitted at this step; the shaded beam indicates that each block attends causally over the full prefix. _Residual stream (right):_ each memory block to be written by the current step occupies a pair of _w_-dimensional slots (address and value). Blocks 1-3 run at every position, but their rightmost-match reads only produce the correct snapshot at & positions; at the _Cw+D_-1 subsequent serialization positions their outputs are corrupted by the partially written current-step memory block and are disregarded by Block 4, which instead copies the snapshot from the most recent &.


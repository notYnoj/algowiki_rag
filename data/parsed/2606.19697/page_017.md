**Alphabet.** The output alphabet is \(\Sigma\sqcup\{0,1,\#,\&,\mathtt{mem}\}\), where & is the _end-of-step_ marker, `mem` is the _memory-write_ marker, and `0,1` are _bit tokens_. The simulator uses no other key tokens: the program counter, registers, and any instruction-private intermediate state all live in `mem` at fixed addresses (cf. §2.1), so every committed write has the same shape.

**Memory blocks.** Every write to the simulated memory appends one _memory block_ to the transcript:

\(\mathtt{mem}\underbrace{\# a_1\cdots a_w}_\mathtt{addressfield}\underbrace{\# v_1\cdots v_w}_\mathtt{valuefield},\)

occupying 2_w_+3 consecutive positions and recording \(\mathtt{mem}[a]\leftarrow v\). Lem. 12 matches an address bits(_a_) available in the residual stream against the address field of the rightmost `mem` block, then uses the known offset _w_+1 to retrieve the value field.

**Steps.** A Word RAM step is the run of (constant-many) memory blocks committed by one simulated instruction, terminated by an & token; & is therefore both an end-of-step marker and the anchor at which Blocks 1-3 produce the snapshot for the next step (see Block 4).

**Residual stream convention.** Throughout the proofs, the phrase "bits(_v_) is available in the residual stream at position _i_" means that the _w_-dimensional vector \(\text{bits}(v)=(b_1,\dots,b_w)\in\{0,1\}^w\) occupies a dedicated _w_-dimensional subspace of the \(\Theta(log^2n)\)-dimensional residual stream at that position. Each transformer layer reads from and writes to named subspaces; different subspaces hold different operands, intermediate addresses, and result slots so that they do not interfere. This can be done without loss of generality (Yang et al., 2026, §4.2).

**State recovery.** The contents of `mem`\[_a_\] at any point in the transcript is the value of the rightmost memory block whose address field encodes _a_. Lem. 12 performs this lookup in constant depth, writing the retrieved bits(_v_) into a designated residual-stream subspace.<sup>8</sup>

**Default values for unwritten cells.** At the start of simulation no memory block has been emitted, so a rightmost-match read for any address returns **0**. The Word RAM program supplies a static initialization vector that fixes the initial value at every address used by the program (zero by default; specific constants for `mem`\[0\]=PC<sub>start</sub> and any program-private scratch cells), and this initialization is baked into the transformer weights. When a read for address _a_ has no matching block in the transcript (detected by a single attention head testing whether the rightmost match exists), an MLP overrides the default **0** output of Lem. 12 with the program-specified initialization constant for that address. Because the initialization map is fixed at compile time and depends only on the program, this override is a constant-depth, finite-precision operation.

We now outline the proof of Thm. 1, which is the main result of this section; the propositions that follow will fill in the details of each component.

**Theorem 1** (Simulation of Word RAMs by log<sup>2</sup>-Width Transformers)**.** _Let M be a flat Word RAM program with word size w. Then there exists a rightmost UHAT T with finite precision,_ O(_w_) _heads each of width_ O(_w), and total model dimension_ O(_w_<sup>2</sup>)=O(log<sup>2</sup>(_n+t_))_, such that, for any_ \(t\ge n\)_, T can simulate t steps of M with_ \(t\cdot\mathcal{O}(w^2)\) _CoT steps. Further, if M does not use_ \(\times\), \(\div\)_, or_ mod_, T can simulate t steps of M with_ \(t\cdot\mathcal{O}(w)\) _CoT steps._

_Proof._ **Memory-only state.** Following the Word RAM definition (§2.1), the entire machine state-- program counter, registers, and the memory--is stored as a single random-access memory `mem` indexed by integer addresses. The transformer simulates the Word RAM by maintaining, in the CoT transcript, a log of memory writes from which the current contents of any address can be recovered. Concretely, every write to an address _a_ is appended to the transcript as a _memory block_

\(\mathtt{mem}\#\text{bits}(a)\#\text{bits}(v),\)

where \(\text{bits}(\cdot)\) is the binary encoding into {0,1}_<sup>w</sup>_. The contents of `mem`\[_a_\] at any point in the transcript is the value _v_ of the rightmost memory block whose address field encodes _a_, or the program-supplied initialization constant if no such block exists; Lem. 12 shows that a rightmost UHAT can perform this lookup in constant depth. Read-only input is handled identically: `inp`\[_i_\] is recovered by direct positional attention to input position _i_. The transcript is partitioned by & markers into _steps_, each step being the run of memory blocks committed by one simulated Word RAM instruction; see Fig. 4.

<sup>8</sup>This is analogous to the commonly studied _induction heads_ (Olsson et al., 2022): a head first matches the address pattern, then retrieves the value at the position immediately following it.


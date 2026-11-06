the most recent soft token forward (e.g. via a fixed-offset retrieval head), so the soft token acts as a small persistent register bank threaded through the transcript.

**Theorem 3** (Simulating Word RAMs with CCoT)**.** _Let M be a d-dimensional-array Word RAM with word size w_=log(_n+t_)+O(1) _and per-instruction bit-serial cost bound_ \(\kappa(w)\).<sup>5</sup> _Then there exists a log-precision, finite-width_ continuous CoT _transformer T such that, for any_ \(t\ge n\)_, t steps of M can be simulated by T using_ \(\mathcal{O}(t\kappa(w))\) _decoding steps._

_Proof overview._ We prove Thm. 3 by induction on the simulated RAM step _s_. The simulator maintains an _append-only_ transcript whose soft token stores the pair \((\phi(a),\phi(v))\) for the written address/value \(\mathtt{mem}[a]\leftarrow v\) (absorbing `pc` and registers into `mem`; see §2.1). Checkpoint and store- summary positions are marked by constant discrete tags so attention can restrict to the relevant subset. If no store-summary exists for an address _a_, the value at `mem`\[_a_\] is interpreted as 0. A useful property of continuous CoT is that we can always make the latest checkpoint available "from layer 0" at future positions: a constant-depth carry block can attend to the rightmost checkpoint tag and copy its soft-token coordinates into designated coordinates of the current residual stream.

**One simulated RAM step.** Assume the invariant holds at the end of RAM step _s_. To simulate step _s_+1, we perform the following conceptual phases (some happen within a single decoding step, others take many decoding steps), illustrated in Fig. 2:

(1) _Load `pc`._ Attend to the rightmost checkpoint and copy \(\phi(\mathrm{PC}^{(s)})\) (and the register codes) into the current residual stream. Use PC<sup>(_s_)</sup> to select which instruction subroutine/oracle to run.<tbc>

(2) _Load operand values._ For each register/constant operand, read \(\phi(\cdot)\) directly from the copied checkpoint state. For each memory operand `mem`\[_a_\], form \(\phi(a)\) and dereference the most recent matching store-summary to recover the operand in coded form \(\phi(v)\) (Lemma 4).<tbc>

(3) _Serialize inputs (write a binary tape)._ For each coded input word needed by the instruction oracle, emit its _w_ bits onto the discrete transcript using Lemma 5. This creates a delimited _work-tape suffix_ for the instruction oracle.<tbc>

(4) _Instruction execution (TM oracle)._ Activate the instruction-specific TM-oracle subroutine, which operates only on the work-tape suffix and runs for \(\mathcal{O}(\kappa(w))\) decoding steps, emitting the output words as bit streams (Lemma 6).<tbc>

(5) _Deserialize outputs._ Convert each output bit stream into its coded form \(\phi(\cdot)\) for future addressing and equality tests, using Lemma 7.<tbc>

(6) _Store updates (re-establish the invariant)._ Emit a new checkpoint token whose soft token stores the updated state \(\phi(\mathrm{PC}^{(s+1)}),\phi(r_1^{(s+1)}),\dots,\phi(r_\rho^{(s+1)})\). If the instruction writes \(\mathtt{mem}[a]\leftarrow v\), also emit a store-summary token storing \((\phi(a),\phi(v))\). By construction, this new checkpoint (and store-summary, if present) is the rightmost such entry, so it will be used at the next step.

Correctness follows from induction on _s_: step (5) appends the new rightmost checkpoint encoding the updated registers/PC, and appends the new rightmost store-summary for any updated address. The total number of decoding steps spent in phases (2)-(4) is \(\mathcal{O}(w+\kappa(w))\) per RAM instruction, yielding \(\mathcal{O}(t\kappa(w))\) steps overall. The following lemmas implement each step (proofs in §D).

**Lemma 4** (Steps 1-2: loading values)**.** _Suppose the transcript contains store-summary positions, each tagged and whose soft token stores a pair_ \((\phi(a_j),\phi(v_j))\)_. Let_ \(\tau\) _be a transcript position at which a query address a is available as_ \(\phi(a)\) _in the residual stream, and suppose_ \(a\le\tau\)_. Then a log-precision, finite-width continuous-CoT transformer can retrieve_ \(\phi(v_{j^*})\)_, where j_<sup>∗</sup> _is the largest index with a_<sub>_j_<sup>∗</sup></sub>=_a. If no such j_<sup>∗</sup> _exists, it retrieves_ \(\phi(0)\).

**Lemma 5** (Step 3: serialization)**.** _Let_ \(\tau\) _be a transcript position at which a value v is available as_ \(\phi(v)\) _in the residual stream, and suppose_ \(v\le\tau\)_. Then a log-precision, finite-width continuous-CoT transformer can emit the w bits of v over the next w decoding steps, ordered from least to most significant, while keeping_ \(\phi(v)\) _available in designated coordinates of the soft token throughout._

**Lemma 6** (Step 4: instruction execution)**.** _Fix any RAM instruction I on w-bit operands whose bit-serial implementation runs in_ \(\kappa(w)\) _decoding steps. There exists a log-precision, finite-width continuous-CoT transformer subnetwork that, once activated, simulates this bit-serial computation_<tbc>

<sup>5</sup>Here \(\kappa(w)\) counts _decoding steps_ of a fixed-alphabet bit-serial implementation of a RAM instruction on _w_-bit operands, including the unavoidable \(\Omega(w)\) serialization of any fresh _w_-bit output word over a fixed alphabet.


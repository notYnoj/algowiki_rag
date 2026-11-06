value rather than the operand-time value. Block 4 sidesteps this by anchoring on the rightmost & and copying the snapshot computed there, where only fully committed memory blocks are visible; the local outputs of Blocks 1-3 at non-& positions are disregarded.

**Proposition 7** (Multiplication, division, and modulo via per-iteration memory cells)**.** _Let I be a_ \(\times\), \(\div\)_, or_ mod _instruction with operands a and b. Then T can compute the result of I in_ O(_w_) _Word RAM steps, each costing_ O(_w_) _CoT tokens, for a total of_ O(_w_<sup>2</sup>) _CoT tokens, using only the four-block pipeline above._

_Proof._ **Why** O(_w_<sup>2</sup>) **tokens are necessary.** The standard bit-serial long-multiplication and long- division algorithms run _w_ outer iterations, each updating an _w_-bit intermediate. Compiling the instruction into _w_ flat Word RAM micro-steps that share state through memory yields a \(w\times\mathcal{O}(w)=\mathcal{O}(w^2)\) token budget; each micro-step is exactly the standard four-block pipeline, with no special control flow.

**Per-iteration state in memory.** The program reserves four private memory addresses \(\alpha_P\), \(\alpha_R\), \(\alpha_q\), \(\alpha_\pi\) (constants, fixed at compile time) for the partial product _P_, the running remainder _R_, the partial quotient _q_, and a phase counter \(\pi\), respectively, plus two more \(\alpha_a,\alpha_b\) for the operand snapshot. The compiled implementation of _I_ is a program fragment that

(1) on entry, writes the operands _a,b_ to \(\alpha_a,\alpha_b\), zero-initializes _P,R,q_, and sets \(\pi\leftarrow 1\);<tbc>

(2) executes a loop of _w_ flat micro-steps, each of which reads _a,b_, the current intermediates, and \(\pi\), performs one algorithm iteration, writes the updated intermediates and \(\pi\leftarrow\pi+1\), and branches on \(\pi\);<tbc>

(3) on exit, writes the final result to the destination address.

Each micro-step has compile-time-fixed read and write address sets (entries of \(\{\alpha_a,\alpha_b,\alpha_P,\alpha_R,\alpha_q,\alpha_\pi\}\)), so the operand descriptors and four-block pipeline of Props. 3 to 6 apply unchanged: each micro-step costs O(_w_) CoT tokens.

**Multiplication** (\(a\times b\mathrm{mod}2^w\))**.** Indexing bits LSB-first, micro-step \(\pi\) extracts \(b_\pi=\mathrm{bits}(b)^\top\mathbf{e}_\pi\) in Block 3 and computes \(P'=P+a\cdot b_\pi\cdot 2^\pi(\mathrm{mod}2^w)\). After _w_ micro-steps, \(P=a\times b(\mathrm{mod}2^w)\), and a final step copies _P_ to the destination.

**Division and modulo** (\(a\div b\), _a_mod_b_)**.** Indexing bits LSB-first, micro-step \(\pi\) processes bit \(i=w-\pi\) of _a_ (MSB to LSB). Block 3 extracts \(a_i=\mathrm{bits}(a)^\top\mathbf{e}_i\), computes \(R'=(R\checkmark 1)|a_i\), performs the trial subtraction \(R''=R'-b\), and tests the sign via the high bit of the (_w_+1)-bit result. If \(R''\ge 0\): \(q'=q|(1\checkmark i)\), \(R\leftarrow R''\); otherwise: \(q'=q\), \(R\leftarrow R'\). After _w_ micro-steps, \(q=\lfloor a/b\rfloor\) and _R=a_mod_b_, and a final step copies the appropriate value to the destination.

Both algorithms use O(_w_<sup>2</sup>) CoT tokens via the standard four-block pipeline.

**Lemma 10** (Indexed read for log<sup>2</sup>-width transformers)**.** _Let T be a finite-precision,_ log<sup>2</sup>_-width UHAT with positional encodings_ PE(_j_)=bits(_j). Let_ \(k\in[2^w-1]\) _be a query key available as_ bits(_k_) _in the residual stream at position i. Suppose the CoT transcript contains a sequence of key-value blocks: at positions_ \(s_1<s_2<\cdots<s_m\le i-1\)_, each block s<sub>i</sub>_=(_k<sub>i</sub>,v<sub>i</sub>_) _starts with a key field of w consecutive bit tokens_ \(\mathrm{bits}(k_i)\in\{0,1\}^w\) _followed by a value field of w consecutive bit tokens_ \(\mathrm{bits}(v_i)\in\{0,1\}^w\)_. Let s_<sup>∗</sup> _be the start of the rightmost block whose key field encodes k; k_<sup>∗</sup>=_k. Then we can augment T with a constant-depth subnetwork that, at position i, recovers_

\(\mathrm{bits}(v^*)=\sum_{t=0}^{w-1}b_te_t\)

_in the residual stream after the first transformer layer, where_ \(\mathrm{bits}(v^*)=(b_0\cdots b_{w-1})\)_, with the default value_ **0** _when no matching block exists._

_Proof._ **Step 1: Key matching.** Using an affine transformation of bits(_k<sub>i</sub>_) as the key vectors and bits(_k_) as the query vector, the attention scores among positions 1_,...,i_ are maximized at _s<sub>j</sub>_ for _j_=1_,...,m_ (Lem. 13). Rightmost UHAT selects the position _s_<sup>∗</sup>, extracts its positional encoding as the value vector **_v_**<sub>_s_<sup>∗</sup></sub>, and adds to it the constant offset _w_ with an MLP.

**Step 2: Value retrieval.** Position _i_ now has access to the position of the value _v_<sup>∗</sup>. The next attention layer can uniquely attend to this position and retrieve the value (Lem. 13).


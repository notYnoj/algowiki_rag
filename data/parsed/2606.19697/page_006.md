destination value(s) and the next `pc` from the operands now in the residual stream (Prop. 5); _(iv)_ **Store:** an attention layer computes the within-step offset \(\delta\) from the rightmost &, and the appropriate \(\delta^\text{th}\) token (a `mem`, a #, an address bit, a value bit, or &) is emitted as the output token (Prop. 6).

For simple instructions, Blocks _(i)-(iii)_ produce identical outputs at every token within the same step, so only \(\delta\) advances in Block _(iv)_, emitting one token at a time over O(_w_) total positions. Deserialization uses _w_ dedicated attention heads (one per bit), each of width _w_, giving the O(_w_<sup>2</sup>)=O(log<sup>2</sup>(_n+t_)) model dimension. In contrast to simple instructions, multiplication, division, and modulo _cannot_ be computed in a single transformer step and are compiled into O(_w_) flat micro-steps that share state through program-private memory cells. Each micro-step costs O(_w_) tokens, for O(_w_<sup>2</sup>) total; every micro-step uses the same four-block pipeline (Prop. 7).

**Corollary 1.** _Let M and T be as in Thm. 1. We have the following:_

(_i)_ _T can simulate t steps of M with_ full-arithmetic _flat instructions using_ O(_t_log<sup>2</sup>_t_) _steps._<tbc>

_(ii)_ _T can simulate t steps of M with_ simple-arithmetic _flat instructions using_ O(_t_log_t_) _steps._

_Remark_ 1 (Bit extraction as a dot product). Reading from and writing into the CoT transcript both require _bit extraction_: computing BIT(_v,t_), the _t_th bit of _v_. In the log<sup>2</sup>-width setting this is trivial: since \(\text{bits}(v)\in\{0,1\}^w\) is stored as a coordinate vector in the residual stream, extracting _b<sub>t</sub>_ reduces to the dot product \(\text{bits}(v)^\top\mathbf{e}_t=b_t\) with the _t_th standard basis vector **_e_**_<sub>t</sub>_. In the fixed-width constructions later, bits(_v_) is no longer directly available as a coordinate vector, so bit extraction becomes substantially more involved and is one of the primary sources of complexity in those proofs.

These results provide a general framework for how CoT can simulate Word RAM programs. However, the log<sup>2</sup>-width construction is _non-uniform_: the model grows with _n_, so new parameters--untrained on shorter inputs--must be invoked as the inputs grow longer. The construction also requires _rightmost_ UHAT; we show in Remark 3 that weaker attention models cannot implement the indexed- read step. The fixed-width constructions in the following sections avoid the non-uniformity and reliance on rightmost UHATs at the cost of more complex reading and writing mechanisms.

## 4 Towards a Uniform Fixed-Width Construction: Bottlenecks and Plan

In §3, storing bits(_v_) in the residual stream gives three things for free: _(i)_ equality checking via inner products, _(ii)_ bit extraction via \(\text{bits}(v)^\top\mathbf{e}_t=b_t\), and _(iii)_ a clean serialization/deserialization mechanism. Moving to fixed width forces us to abandon the bits representation, and each of these primitives must be rebuilt from scratch. We describe the resulting challenges below.

**Bottleneck: Reading and writing values.** The deepest challenge in moving to fixed width is that we must adopt a different representation of numbers in the residual stream. For fixed-width constructions, any such representation repr of values must satisfy two properties simultaneously:

(a) _Equality gap:_ \(\text{repr}(i)^\top\text{repr}(j)=1\) if _i=j_, and \(\text{repr}(i)^\top\text{repr}(j)<1-\epsilon\) otherwise.<tbc>

(b) _Read/write:_ We can serialize repr(_v_) to a binary CoT encoding and recover repr(_v_) from it.

The first property is needed for the indexed-read attention mechanism; the second is needed both _(a)_ to pass pointers computed at a higher layer back to lower layers in future steps, and _(b)_ to hand binary-encoded operands to the TM oracle for complex arithmetic. Past work has established the **layer-norm hash** \(\phi(i)\) as a fixed-width representation satisfying the equality-gap property (Merrill and Sabharwal, 2024), but reading and writing via \(\phi\) presents a challenge.

Writing is hard because it requires computing BIT(_v,j_) from \(\phi(v)\)--mapping a hash representation back to individual bits.<sup>3</sup> One approach is to compute \(\phi(v\mathrm{mod}2)\) and \(\phi(\lfloor v/2\rfloor)\) iteratively. When \(v\le t\), Merrill and Sabharwal (2025) give a construction for computing \(\phi(v\mathrm{mod}2)\) and \(\phi(\lfloor v/2\rfloor)\) from \(\phi(v)\); for larger values this is open (note that Prop. 2 allows easily computing \(\phi(v/2)\), but not \(\phi(\lfloor v/2\rfloor)\)). To resolve the write challenge, we adopt a normal form for Word RAMs that enforces \(v\le t\) at every step, developed in §4.1, allowing us to compute the least significant bit of _v_ as well as \(\phi(\lfloor v/2\rfloor)\). The remaining bits of _v_ can be obtained by iterating the process, which requires repeatedly _conditioning_ on \(\phi(\lfloor v/2\rfloor)\), \(\phi(\lfloor v/4\rfloor)\), etc. We show this can be achieved via either of two minimal<tbc>

<sup>3</sup>BIT(_v,j_) plays a central role in descriptive complexity theory and the analysis of transformer expressivity.


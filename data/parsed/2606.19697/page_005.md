More generally, \(\phi(a,b)=\mathrm{layernorm}(a,b,-a,-b)\). This representation has several useful properties (similar to binary encodings) that we will leverage. The first property is useful for performing an equality check using inner product, as well as tie-breaking in order to simulate rightmost attention:

**Proposition 1** (Equality Check and Mismatch Gap: Merrill and Sabharwal, 2024)**.** _Let_ \(u,v\in\{0,1,\dots,T\}\)_. Then_ \(\langle\phi(u),\phi(v)\rangle=1\) _if and only if u=v. Further, when_ \(u\neq v\), \(\phi(u),\phi(v)\rangle\le 1-\delta_T\) _where_ \(\delta_T:=\frac{1}{4(T^2+1)^2}\).

See proof in §A.2 for completeness. \(\phi\) is scale invariant (Merrill and Sabharwal, 2024): \(\phi(cu,cv)=\phi(u,v)=\phi(u/v,1)=\phi(u/v)\). We can also "swap" the dimensions of \(\phi\) to _invert_ a number: if \(\phi(v)=(s_1,s_2,-s_1,-s_2)\), then \(\phi(1/v)=(s_2,s_1,-s_2,-s_1)\). We introduce a new general _affine update_ (proof in §A.2), computable by a fixed-depth feedforward network as well as with an RNN:

**Proposition 2** (Affine Update)**.** _Fix constants_ \(a,b\in\mathbb{R}\)_. Let_ \(\phi(v)=(s_1,s_2,-s_1,-s_2)\)_. Then_ \(\phi(av+b)=\mathrm{layernorm}(as_1+bs_2,s_2,-(as_1+bs_2),-s_2)\).

## 3 Simulating Word RAMs with Polylog-Width Transformers

We begin by showing how transformers with polylogarithmic width and fixed precision can simulate Word RAMs--a stepping stone towards more _uniform_ transformer models, which do not require new parameters as the input length grows. Thus, we use the construction in this section to cleanly outline the simulation; the main ideas will re-appear in the subsequent sections.

**The transformer model.** We use a log<sup>2</sup>-width finite-precision transformer model; see Remark 2 for a discussion of why log<sup>2</sup> width is needed. The constructions build on the log-width machinery formalized by existing work (Li et al., 2024; Svete et al., 2025; Svete and Sabharwal, 2026).<sup>2</sup> This allows us to reuse existing gadgets in our constructions.

**Representation of values.** In the polylogarithmic-width setting, word-sized integers are stored in the residual stream as binary vectors denoting their binary expansions: for a value \(v\in\{0,1\}^w\), the **representation** \(\mathrm{repr}(v)=^\mathrm{def}\mathrm{bits}(v)\in\{0,1\}^w\) is placed directly as a vector in the residual stream. This gives two primitives: _(i) equality checking_ via inner products (\(\mathrm{repr}(i)^\top\mathrm{repr}(j)=w\) iff _i=j_, and strictly less otherwise), and _(ii) bit extraction_ via \(\mathrm{repr}(v)^\top\mathbf{e}_t=b_t\) for the _t_th standard basis vector **_e_**_<sub>t</sub>_. These two primitives are the key gadgets exploited throughout this section; the subsequent sections will define different representations to maintain fixed width.

Thm. 1 formalizes Word RAM simulation by log<sup>2</sup>-width transformers; see §C for the full proof.

**Theorem 1** (Simulation of Word RAMs by log<sup>2</sup>-Width Transformers)**.** _Let M be a flat Word RAM program with word size w. Then there exists a rightmost UHAT T with finite precision,_ O(_w_) _heads each of width_ O(_w), and total model dimension_ O(_w_<sup>2</sup>)=O(log<sup>2</sup>(_n+t_))_, such that, for any_ \(t\ge n\)_, T can simulate t steps of M with_ \(t\cdot\mathcal{O}(w^2)\) _CoT steps. Further, if M does not use_ \(\times\), \(\div\)_, or_ mod_, T can simulate t steps of M with_ \(t\cdot\mathcal{O}(w)\) _CoT steps._

_Proof sketch._ Following the Word RAM definition (§2.1), the Word RAM state--program counter, registers, and memory--is folded into a single random-access memory `mem`. The construction logs every memory write to the CoT transcript as a _memory block_ of the form `mem` # bits(_a_) # bits(_v_) (Fig. 1). The central operation is the _memory read_ (Lem. 12): given a query address bits(_a_) in the residual stream, recover the value of the rightmost `mem` block whose address field encodes _a_ (i.e., the most recent write to `mem`\[_a_\]). This uses two attention steps: the first selects the rightmost matching address position; the second retrieves the value field at the known offset.

Each CoT step runs four constant-depth layer blocks (cf. Fig. 4 and §C): _(i)_ **Load pc:** an indexed read with the constant query 0 recovers bits(`mem`\[0\]) in two attention layers (Prop. 3); _(ii)_ **Load Instruction and Operands:** the active line of the program is identified from bits(`mem`\[0\]) by an MLP that issues parallel reads of every compile-time address listed in the instruction’s operand descriptor (registers), and a second round of reads resolves any runtime addresses (`mem`\[_a_\] or `inp`\[_a_\]) whose index _a_ is now in the residual stream (Prop. 4); _(iii)_ **Execute:** a single MLP computes the _w_-bit<tbc>

<sup>2</sup>In particular, we use L_-uniform_ transformers (London and Kanade, 2025), (Barcelo et al., 2026, §4.4) with positional encodings that only contain the binary representation of the position. This prevents the PEs from encoding too much information and relies on the transformer abilities to simulate the Word RAM programs.


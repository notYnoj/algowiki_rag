architectural extensions: continuous CoT (§5, Lem. 5) or hybrid transformer-RNN models (§6, Lem. 8).<sup>4</sup>

Reading is hard for a complementary reason: while \(\phi(v)\) can be reconstructed from a binary CoT encoding via iterative bit-shifting within the \(\phi\) representation, this is not known to be achievable by a plain transformer. We show that this too becomes feasible with either of two minimal architectural extensions: continuous CoT (§5, Lem. 7) and hybrid transformer-RNN models (§6, Lem. 9).<sup>4</sup>

### 4.1 Writing Solution: Equivalent RAMs with Bounded Word Values

We define a _c_**-dimensional** Word RAM as a Word RAM where the tape is replaced by a _c_-dimensional array of _c_-dimensional tuples. The following lemma shows that such Word RAMs are as powerful as standard Word RAMs, up to a constant factor in runtime (see §B for a proof):

**Lemma 1.** _Let M be a 1-dimensional Word RAM with word size w=c_log(_n+t_) _for some_ \(c\in\mathbb{N}\)_. Then there exists a c-dimensional restricted Word RAM_ \(M'\) _with word size_ \(w'=\mathrm{log}(n+t)\) _and the same instruction set as M that simulates t steps of M using_ O(_t_) _steps._

This shows that we can reduce any _M_ using word size _w=c_log(_n+t_) to \(M'\) using word size _w_=log(_n+t_). Now, define a Word RAM as **restricted** if, for any step _i_, any value _v_ represented in any register satisfies \(v\le i\). Any Word RAM _M_ can be converted to be restricted by making it do nothing for the first _v_ steps, and then simulating the _i_-th step of _M_ at step _v+i_:

**Lemma 2.** _Let M be any c-dimensional Word RAM where all values are at most v(n_) _on inputs of size n. Then there exists_ \(M'\) _that simulates t steps of M using v(n_)+_t steps such that, at each step i, all values in_ \(M'\) _are at most i._

We can first invoke Lem. 1 and then apply Lem. 2 with _v(n_)=_n+t_ to obtain the following:

**Theorem 2** (Restricted Word RAM Equivalence)**.** _A standard Word RAM running in time t(n_) _on inputs of size n can be simulated by a restricted c-dimensional Word RAM in time_ O(_n+t(n_)).

This will be useful because simulating restricted Word RAMs with transformer-like models will be easier than simulating unrestricted ones. Specifically, the property \(v\le i\) will be useful for writing numbers in binary as it allows us to divide numbers using attention via the following special case of the "division lemma" of Merrill and Sabharwal (2024) where the divisor is 2 (see §B for a proof):

**Lemma 3** (Simplified Division Lemma)**.** _There exists a transformer block that, for any_ \(\phi(v)\) _present in the residual stream at position t for_ \(v\le t\)_, adds_ \(\phi(\lfloor v/2\rfloor)\) _and_ \(\phi(v\mathrm{mod}2)\) _to the residual stream._

This will be useful for writing numbers \(\phi(v)\) onto the CoT in binary because it allows computing the least significant bit via \(\phi(v\mathrm{mod}2)\), or \(\phi(v\mathrm{mod}2^i)\), which can be useful for recovering other bits.

## 5 Simulating Word RAMs with Continuous CoT

The bounded-value normal form from §4.1 ensures a crucial _bit-extraction_ precondition: during execution, every word _v_ at RAM step _s_ satisfies \(v\le s\). Since each simulated step produces at least one transcript symbol, this implies \(v\le\tau\) whenever the simulator begins emitting a bit-string segment at transcript position \(\tau\). Thus, whenever we need to stream a word as bits we may apply the simplified division primitive (Lem. 3) to compute \(\phi(\lfloor v/2\rfloor)\) and \(\phi(v\mathrm{mod}2)\) (the first bit) from \(\phi(v)\), and then repeat the process for the next bit by _conditioning_ the computation on \(\phi(\lfloor v/2\rfloor)\), and so on.

The remaining obstacle is _persistence_: after streaming _w_ discrete bits, later computation must still have access to a constant-dimensional _word code_ that supports exact-match attention (for RAM addressing) and can be carried forward across time.

We show that _continuous CoT_ can be used to achieve both conditioning and persistence.

**Continuous CoT and soft tokens.** In the continuous-CoT model, each decoding step emits both (i) a discrete token from a fixed alphabet and (ii) a constant-dimensional _soft token_ \(p_i\in\mathbb{R}^{d_s}\). The next decoding step receives the entire prefix, including the past soft tokens, so _p<sub>i</sub>_ can be attended to by future layers. In particular, a constant-depth transformer block can copy designated coordinates of<tbc>

<sup>4</sup>This iterative computation can also be performed by a logarithmic-depth transformer; we do not explore this here.


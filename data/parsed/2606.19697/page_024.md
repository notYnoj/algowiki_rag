<tbc>Abstractly, the attention score at position _j_ decomposes as

\(\mathrm{score}(i,j)=\mathbf{q}_i^\top\mathbf{k}_j=\underbrace{\mathrm{bits}(a)^\top\mathrm{bits}(a_j)}_\text{key match}+\underbrace{m(j)}_\text{rightmost bias},\)

where _a<sub>j</sub>_ is the key address at position _j_ and \(m:\mathbb{N}\rightarrow\mathbb{R}\) must be strictly increasing so that the rightmost matching position wins. The key-match term equals \(\Theta(w)\) when _a<sub>j</sub>=a_ and is strictly less otherwise, so _m_ must simultaneously satisfy: _(i)_ strict monotonicity _m(j_+1)_\>m(j_), which forces \(m(j+1)-m(j)=\Omega(1)\), thus \(m(j)=\Omega(j)=\Omega(n)\) over a transcript of length _n_ due to constant precision; and _(ii)_ a dominance bound _m(j)\<_O(log_n_) so that a mismatched position cannot outscore a matched one. These two requirements are contradictory, so rightmost UHAT is necessary.<sup>9</sup>

By contrast, attending to the _leftmost_ match is easy under AHAT: one only needs a boolean flag indicating whether the same address appeared earlier, which is computable in constant precision. Logarithmic precision also circumvents the barrier by encoding offsets _m_ with _m(j)\<_1 for all _j_ (circumventing the requirement that \(m(j+1)-m(j)=\Omega(1)\)); existing transformer Turing completeness results rely on exactly that (Pérez et al., 2021; Nowak et al., 2024).

**Lemma 12** (Reading from Memory)**.** _Let T be a rightmost UHAT with_ log<sup>2</sup> _width and finite precision. Suppose the CoT transcript contains a store log where each entry is serialized as mem_#bits(_a<sub>j</sub>_)#bits(_v<sub>j</sub>). Given an address_ \(a\in[2^w-1]\) _available as_ bits(_a_) _in the residual stream at position i, T can retrieve the most recent value v stored at address a in constant depth._

_Proof._ The retrieval is performed in two attention steps:

**Step 1: Address Matching.** _T_ generates a query bits(_a_) and attends to all positions _j\<i_ following an mem marker (these can be detected by looking back a constant number of positions). By Lem. 10, the rightmost UHAT mechanism selects the starting position _s_<sup>∗</sup> of the most recent block where the _w_ bits following mem perfectly match bits(_a_). The Transformer then extracts the positional encoding PE(_s_<sup>∗</sup>) into the residual stream.

**Step 2: Value Retrieval.** Using the retrieved PE(_s_<sup>∗</sup>), _T_ computes the position of the corresponding value field by adding to it a constant offset. A second attention layer uniquely attends to this position and uses the bit-retrieval mechanism of Lem. 11 to reconstruct \(\mathrm{bits}(v)=\sum_{t=0}^{w-1}b_t\mathbf{e}_t\) in the residual stream.

If no matching mem is found, the attention mechanism defaults to a null vector, resulting in bits(0) as per the simulation invariant.

The following is a restatement of Svete and Sabharwal (2026, Lem. D.7), used throughout this section.

**Lemma 13** (Svete and Sabharwal 2026, Lem. D.7)**.** _Let T be a finite-precision polylogarithmic-width transformer such that its residual stream contains_ bits(_v_) _at position i. Then, T’s attention heads can attend to all positions_ \(j\le i\) _that contain_ bits(_v_) _in the residual stream as well (and put zero attention to others). If T is a rightmost UHAT, the rightmost such position is uniquely attended to._

## D Proofs of Continuous CoT Results

**Lemma 5** (Step 3: serialization)**.** _Let_ \(\tau\) _be a transcript position at which a value v is available as_ \(\phi(v)\) _in the residual stream, and suppose_ \(v\le\tau\)_. Then a log-precision, finite-width continuous-CoT transformer can emit the w bits of v over the next w decoding steps, ordered from least to most significant, while keeping_ \(\phi(v)\) _available in designated coordinates of the soft token throughout._

_Proof._ Write \(v=\sum_{k=0}^{w-1}b_k2^k\) and define _v_<sub>0</sub>:=_v_, \(v_{k+1}:=\lfloor v_k/2\rfloor\), and _b<sub>k</sub>_:=_v<sub>k</sub>_mod2.

At decoding step _k_ (position \(\tau+k+1\)), we have \(v_k\le v\le\tau<\tau+k+1\), hence \(v_k\le\tau+k+1\). Therefore we may apply Lemma 3 with (_v,d_)=(_v<sub>k</sub>,_2) to compute \(\phi(\lfloor v_k/2\rfloor)=\phi(v_{k+1})\) and<tbc>

<sup>9</sup>Greater expressivity of rightmost UHAT has been established independently in the finite-precision and finite-width settings (Yang et al., 2024a; Jerad et al., 2025; Li and Cotterell, 2026); the argument above shows the same holds in the finite-precision growing-width setting.


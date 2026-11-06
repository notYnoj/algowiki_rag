<tbc>upon in the next step. However, we can use a similar ability afforded by RNNs, which naturally allow conditioning on values available in the residual stream at the immediately previous position.

The only other difference is in the _store_ step, where the continuous CoT captures operations of the form \(\mathtt{mem}[a]\leftarrow v\) by emitting a store-summary soft token storing \((\phi(a),\phi(v))\). Instead, we now serialize _a_ and _v_ using _w_ bits each via the (updated) serialization lemma below, and use the (updated) deserialization lemma on these bits to obtain \(\phi(a)\) and \(\phi(v)\) in the layer 1 residual stream after _w_ additional dummy tokens.

All other steps in the construction for Thm. 3 remain unchanged. In the remainder of this section, we thus focus on deriving counterparts of Lemmata 5 and 7 for hybrid architectures. The serialization construction is essentially the same as in the proof of Lem. 5, except that without continuous CoT, we cannot emit \(\phi(v_{k+1})\), defined as \(\phi(\lfloor v_k/2\rfloor)\), at position \(\tau+k+1\) and read it back in at the following position. Instead, we emit _b<sub>k</sub>_, computed via Lem. 3. We then compute \(\phi(\lfloor v_k/2\rfloor)\) from \(\phi(v_k)\) and _b<sub>k</sub>_ via its equivalent form \(\phi(\frac{1}{2}(v_k-b_k))\) by leveraging Prop. 2 to turn it into a linear transformation that an RNN head can perform. This gives the following result (proof in §E):

**Lemma 8** (Serialization)**.** _Let_ \(\tau\) _be a transcript position at which a value v is available as_ \(\phi(v)\) _in the residual stream, and suppose_ \(v\le\tau\)_. Then a log-precision, finite-width hybrid model can emit the w bits of v over the next w decoding steps, ordered from least to most significant._

For deserialization, we use the same recursive computation as in the corresponding lemma for continuous CoT (Lem. 7), except now the computation is within the hidden state of the linear RNN rather than via soft tokens. This gives the following result (proof in §E):

**Lemma 9** (Deserialization)**.** _There exists a log-precision, finite-width hybrid model that, on any bit sequence b_<sub>0</sub>_,...,b_<sub>_w_-1</sub> _followed by w arbitrary tokens, computes_ \(\phi(v)\)_, where_ \(v=\sum_{k=0}^{w-1}b_k2^k\) _is the LSB evaluation of b, in the residual stream at depth_ 1 _at the last token._

Analogously to Cor. 2 for the CCoT simulation, we have the following notable cases:

**Corollary 3** (Simulating Word RAM with Hybrid Models)**.** _Let M and H be as in Thm. 4. Depending on the complexity of the instruction set_ \(\kappa(w)\) _of M, the following hold:_

(_i)_ _H can simulate t steps of M with arbitrary poly(w)-time instructions using_ \(\tilde{\mathcal{O}}(t)\) _steps._<tbc>

(_ii)_ _H can simulate t steps of M with_ full-arithmetic _flat instructions using_ O(_t_log<sup>2</sup>_t_) _steps._<tbc>

_(iii)_ _H can simulate t steps of M with_ simple-arithmetic _flat instructions using_ O(_t_log_t_) _steps._

## 7 Conclusion

We show that poly-logarithmic-width transformers can simulate a Word RAM; while it is unclear whether fixed-width transformers can also do so, we show that two minimal extensions to fixed-width transformers (continuous CoT transformers and hybrid models) both can. Our results show that CoT--at least for certain architectures--allows simulating algorithms with their general textbook runtimes up to a polylogarithmic factor, removing the quadratic overhead that would be incurred by going through previously established Turing completeness results (Pérez et al., 2021; Merrill and Sabharwal, 2024). Since certain realistic extensions (continuous CoT or RNN layers) to transformers are crucial for the fixed-width constructions, it is an interesting open question to what degree these extensions are necessary for efficient Word RAM simulation. It would also be interesting to study to what degree these extensions benefit algorithmic reasoning in transformer models in practice.

## References


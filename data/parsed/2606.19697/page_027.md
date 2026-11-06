By Prop. 1, \(\langle\phi(a),\phi(\tilde{a})\rangle=1\) iff \(\tilde{a}=a\), and otherwise it is at most \(1-\delta<c\). Hence: - If a match exists, then \(\tilde{a}=a\) and the head selects the current position, outputting \(\phi(\tilde{v})=\phi(v_{j^*})\). - If no match exists, then \(\tilde{a}\neq a\) and the head selects the anchor, outputting \(\phi(0)\).

All operations use only constant-dimensional codes and inverse-polynomial margins in \(\tau\), so they are implementable with finite width and \(O(log\tau)\)-bit precision.

**Lemma 6** (Step 4: instruction execution)**.** _Fix any RAM instruction I on w-bit operands whose bit-serial implementation runs in_ \(\kappa(w)\) _decoding steps. There exists a log-precision, finite-width continuous-CoT transformer subnetwork that, once activated, simulates this bit-serial computation for_ \(\mathcal{O}(\kappa(w))\) _decoding steps and emits the output bit streams of I onto the transcript. Moreover, the subnetwork can be made to ignore the rest of the transcript by delimiting a_ work-tape suffix _(with a start marker) and restricting all attention inside the subroutine to positions in that suffix._

_Proof._ Fix any RAM instruction _I_ as a function from a fixed number of _w_-bit inputs to a fixed number of _w_-bit outputs. By assumption, there exists a Turing machine _M<sub>I</sub>_ that computes _I_ in time \(\kappa(w)\). Using existing Turing-completeness results for transformers (Merrill and Sabharwal, 2024), there exists a transformer _T<sub>I</sub>_ that simulates _M<sub>I</sub>_ (and thus computes _I_) in time \(O(\kappa(w))\).

## E Proofs of Hybrid Model Results

**Lemma 8** (Serialization)**.** _Let_ \(\tau\) _be a transcript position at which a value v is available as_ \(\phi(v)\) _in the residual stream, and suppose_ \(v\le\tau\)_. Then a log-precision, finite-width hybrid model can emit the w bits of v over the next w decoding steps, ordered from least to most significant._

_Proof._ The construction is essentially the same as in the proof of Lem. 5, except that without continuous CoT, we cannot emit \(\phi(v_{k+1})\), defined as \(\phi(\lfloor v_k/2\rfloor)\), at position \(\tau+k+1\) and read it back in at the following position. Instead, we emit _b<sub>k</sub>_, computed via Lem. 3. Write \(\phi(v)\) as (_s_<sub>1</sub>_,s_<sub>2</sub>_,-s_<sub>1</sub>,-_s_<sub>2</sub>) and observe that \(\lfloor v_k/2\rfloor=\frac{1}{2}(v_k-b_k)\). We can thus apply Prop. 2 to compute \(\phi(\lfloor v_k/2\rfloor)\), up to a normalization factor, as:

\(\big(\frac{1}{2}s_1,s_2,-\frac{1}{2}s_1,-s_2\big)\text{when}b_k=0\)<br>
\(\big(\frac{1}{2}(s_1-s_2),s_2,-\frac{1}{2}(s_1-s_2),-s_2\big)\text{when}b_k=1\)

We can use this to design a simple RNN layer that computes \(\phi(\lfloor v_k/2\rfloor)\) at position \(\tau+k+1\) as follows. The RNN state _S<sub>t</sub>_ will always be diagonal; thus we consider only its vector of diagonal entries _h<sub>t</sub>_. The hidden state \(h_{\tau+k}\) of the RNN is the (unnormalized) \(\phi(v_k)\). In particular, \(h_\tau=\phi(v_0)=\phi(v)\), which can be implemented with a 0 transition matrix and the additive term \(\phi(v)\). The RNN computes the next hidden state as \(h_{\tau+k+1}=A_kh_{\tau+k}\) where _A<sub>k</sub>_ is _B_<sub>0</sub> when _b<sub>k</sub>_=0 and _B_<sub>1</sub> when _b<sub>k</sub>_=1, where

\(B_0=\left(\begin{array}{ c c c c }
1/2 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1/2 & 0 \\
0 & 0 & 0 & 1
\end{array}\right),B_1=\left(\begin{array}{ c c c c }
1/2 & -1/2 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1/2 & -1/2 \\
0 & 0 & 0 & 1
\end{array}\right)\)

Observe that \(h_{\tau+k+1}\) is precisely the unnormalized form of \(\phi(\lfloor v_k/2\rfloor)\) derived above. The layer outputs the normalized form \(\mathrm{layernorm}(h_{\tau+k+1})\), which equals \(\phi(\lfloor v_k/2\rfloor)\), to the residual stream, which is then used in the next step to compute _b_<sub>_k_+1</sub> and continue the process.

While we do not enforce it, the matrices used in the construction have a diagonal-plus-low-rank parameterization: _B_<sub>0</sub> is directly diagonal, and each block of _B_<sub>1</sub> can be decomposed into the identity minus a rank-1 matrix. Thus, these matrices resemble the parameterizations used in architectures like DeltaNet (Schlag et al., 2021; Yang et al., 2024b) and RWKV-7 (Peng et al., 2025).

**Lemma 9** (Deserialization)**.** _There exists a log-precision, finite-width hybrid model that, on any bit sequence b_<sub>0</sub>_,...,b_<sub>_w_-1</sub> _followed by w arbitrary tokens, computes_ \(\phi(v)\)_, where_ \(v=\sum_{k=0}^{w-1}b_k2^k\) _is the LSB evaluation of b, in the residual stream at depth_ 1 _at the last token._


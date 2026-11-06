**Lemma 11** (Serializing-Deserializing values via CoT)**.** _Let T be a finite-precision,_ log<sup>2</sup>_-width UHAT. Suppose that at position i the output symbol is # and the residual stream contains_ \(\mathrm{bits}(v)=(b_1\cdots b_w)\in\{0,1\}^w\)_. Then, T can be augmented with constant-depth subnetworks such that:_

(_1)_ **_(Write)_** _With w CoT steps, T can output b<sub>t</sub> in position i+t for all_ \(t\in\{1,\dots,w\}\).<tbc>

_(2)_ **_(Read)_** _T has_ bits(_v_) _available in the residual stream at position i+w._

_Proof._ **Part (1): Write.** _T_ at position _i+t_ must emit _b<sub>t</sub>_, the _t_<sup>th</sup> bit of _v_. By hypothesis, bits(_v_) is available in the residual stream at position _i+t_ (recomputed by the same constant-depth subnetwork at each instruction-mode output step; cf. Prop. 5). To identify _t_, we use positional encodings PE(_j_)=bits(_j_). At position _i+t_, an attention layer uses rightmost-unique hard attention to attend to the last preceding # symbol, which occupies position _i_ (cf. Lem. 10). The attending position extracts bits(_i_) from the value at position _i_. A subsequent MLP subtracts bits(_i_) from the local positional encoding bits(_i+t_), yielding bits(_t_). A second MLP layer then converts bits(_t_) into the one-hot vector \(\mathbf{e}_t\in\{0,1\}^w\), which can be done as a conjunction of the bits of bits(_t_) (Svete and Cotterell, 2024, Lemma B.1). Finally, an MLP computes \(\mathrm{bits}(v)^\top\mathbf{e}_t=b_t\), which is emitted as the output token at position _i+t_.

**Part (2): Read.** At position _i+w_, we must reconstruct \(\mathrm{bits}(v)=\sum_{t=0}^{w-1}b_t\mathbf{e}_t\) in the residual stream, where **_e_**_<sub>t</sub>_ is the _t_<sup>th</sup> standard basis vector. We use _w_ dedicated hard-attention heads _H_<sub>0</sub>_,H_<sub>1</sub>_,...,H_<sub>_w_-1</sub>, one per bit. Head _H<sub>t</sub>_ must attend to position _i+t_, i.e., to the earlier position that emitted bit _b<sub>t</sub>_.

Head _H<sub>t</sub>_ at position _i+w_ computes a query from bits(_i+w_)=PE(_i+w_) and keys from bits(_j_)=PE(_j_) at each earlier position _j_. _H<sub>t</sub>_ can identify position _i+t_ exactly by forming the query PE(_i+w_)-bits(_w-t_)=PE(_i+t_), and matching it against the key PE(_j_). Hard attention then selects position _i+t_ holding the symbol _x_<sub>_i+t_</sub> as the unique position with key equal to the query.

The value map of head _H<sub>t</sub>_ returns \(x_{i+t}\cdot\mathbf{e}_t=b_t\cdot\mathbf{e}_t\). After summing over all _w_ heads, the first transformer layer at position _i+w_ produces

\(\sum_{t=0}^{w-1}x_{i+t}\cdot\mathbf{e}_t=\sum_{t=0}^{w-1}b_t\cdot\mathbf{e}_t=\mathrm{bits}(v),\)

which is repr(_v_) as required.

_Remark_ 2 (Why log<sup>2</sup> width is necessary). The Read step above uses \(w=\Theta(\mathrm{log}n)\) heads, each of width \(\Theta(\mathrm{log}n)\), for a total model dimension of \(\Theta(\mathrm{log}^2n)\). Both factors are forced.

_Logarithmically many heads._ To reconstruct bits(_v_) at a single position, one must gather _w_ bits from _w_ distinct earlier positions. Compressing information from a log-growing number of positions into fewer constantly-many heads is infeasible at constant precision: the attention weight at each position is a scalar, so with _o(w_) heads the aggregated output is a fixed-dimensional summary of _o(w_) positions, which cannot faithfully recover all _w_ bits. One could in principle design highly bespoke positional encodings (with L-uniform PEs; cf. London and Kanade (2025) and Svete and Sabharwal (2026)) that pack multiple bits into a single head’s key-query score, but this would substantially complicate the construction and break the clean one-bit-per-head structure; we therefore use \(\Theta(w)\) heads.

_Logarithmic width per head._ Each head _H<sub>t</sub>_ must attend to a specific position _i+t_, which it identifies by forming the query PE(_i+w_)-bits(_w-t_)=PE(_i+t_) and matching it against position keys. Carrying the positional offset bits(_w-t_) in the query already requires \(\theta(1)\) bits of information per head; a constant-width head cannot encode this offset. Hence each head must itself be of growing width.

Together, \(\Theta(w)\) heads of width \(\Theta(w)\) give total dimension \(\Theta(w^2)=\Theta(\mathrm{log}^2n)\). Note that the structure is highly uniform: all _w_ heads are simple affine transformations of the same log_n_-wide positional encoding PE, differing only in a constant additive offset bits(_w-t_).

_Remark_ 3 (Why rightmost UHAT is necessary). The indexed-read step requires attending to the _rightmost_ position in the transcript whose key field matches a query address \(a\in\{0,1\}^w\). We sketch why constant-precision AHAT (and equivalently leftmost UHAT (Jerad et al., 2025; Li and Cotterell, 2026)) cannot implement this.


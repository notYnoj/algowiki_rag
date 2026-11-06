## A Details on the Preliminaries

### A.1 The Transformer Model

This appendix restates the decoder-only transformer model used in Merrill and Sabharwal (2024), which itself builds on the component-level formalization of Merrill and Sabharwal (2023a). Let \(\Sigma\) be the fixed token alphabet. Let D_<sub>p</sub>_ be the datatype of _p_-bit floating-point numbers with truncated arithmetic as in Merrill and Sabharwal (2023b).

**Definition 1** (Decoder-only transformer)**.** A _p_-precision decoder-only transformer with _h_ heads, _d_ layers, model dimension _m_, and feedforward width _u_ consists of: (i) an embedding map \(e:\Sigma\times\unknown\rightarrow\mathbb{D}_p^m\); (ii) for each layer \(\ell\) and head _k_, a similarity map \(s_k^\ell:\mathbb{D}_p^m\times\mathbb{D}_p^m\rightarrow\mathbb{D}_p\) and a value map \(v_k^\ell:\mathbb{D}_p^m\rightarrow\mathbb{D}_p^{m/h}\); (iii) for each layer \(\ell\), an activation map \(f^\ell:(\mathbb{D}_p^{m/h})^h\times\mathbb{D}_p^m\rightarrow\mathbb{D}_p^m\); (iv) an output map \(\gamma:\mathbb{D}_p^m\rightarrow\Sigma'\).

**Definition 2** (One strict-causal decoding step)**.** For a prefix \(z=z_1\cdots z_n\), set \(\mathbf{h}_i^0=e(z_i,i)\). For each layer \(\ell\) and head _k_, define<tbc>

\(\mathbf{a}_{i,k}^\ell=\sum_{j<i}\frac{s_k^\ell(\mathbf{h}_i^{\ell-1},\mathbf{h}_j^{\ell-1})}{Z_{i,k}^\ell}v_k^\ell(\mathbf{h}_j^{\ell-1}),Z_{i,k}^\ell=\sum_{j<i}s_k^\ell(\mathbf{h}_i^{\ell-1},\mathbf{h}_j^{\ell-1}).\)

<tbc>Then<tbc>

\(\mathbf{h}_i^\ell=f^\ell(\mathbf{a}_{i,1}^\ell,\dots,\mathbf{a}_{i,h}^\ell,\mathbf{h}_i^{\ell-1}),g(z)=\gamma(\mathbf{h}_n^d).\)

<tbc>**Definition 3** (Projected pre-norm)**.** For a residual vector **h** and a linear map **M**, projected pre-norm applies layer norm to **Mh**:

\(\mathrm{PLN}(\mathbf{h};\mathbf{M})=\mathrm{LN}(\mathbf{Mh}).\)

We note that now-standard peri-norm (Kim et al., 2025) or reordered norm (Olmo, 2026), which did not exist at the time of Merrill and Sabharwal (2024), allows implementing projected pre-norm constructions with no extra projection. With reordered norm, we can simply always write normalized values at the layer output and then apply a projection to select those values when needed. With peri-norm, the same idea works: all writes to the residual stream are normalized, so when we read a normalized vector at the next sublayer input, the number of writes gets normalized away with no distortions.

As in Merrill and Sabharwal (2024), the lower-bound construction does not depend on any special positional encoding. We assume standard causal masking rather than strict causal masking.

### A.2 Layernorm Hash Details

**Proposition 1** (Equality Check and Mismatch Gap: Merrill and Sabharwal, 2024)**.** _Let_ \(u,v\in\{0,1,\dots,T\}\)_. Then_ \(\langle\phi(u),\phi(v)\rangle=1\) _if and only if u=v. Further, when_ \(u\neq v\), \(\phi(u),\phi(v)\rangle\le 1-\delta_T\) _where_ \(\delta_T:=\frac{1}{4(T^2+1)^2}\).

_Proof._ Since \(\phi(x)=\frac{1}{\sqrt{2(x^2+1)}}(x,1,-x,-1)\), one computes<tbc>

\(\langle\phi(x),\phi(y)\rangle=\frac{xy+1}{\sqrt{(x^2+1)(y^2+1)}}\)

<tbc>and therefore

\(1-\langle\phi(x),\phi(y)\rangle^2=\frac{(x-y)^2}{(x^2+1)(y^2+1)}.\)

If \(u\neq v\) are integers in \[0_,T_\], then \((u-v)^2\ge 1\) and \((u^2+1)(v^2+1)\le(T^2+1)^2\), hence \(1-\langle\phi(u),\phi(v)\rangle^2\ge 1/(T^2+1)^2\). Using \(\sqrt{1-\epsilon}\le 1-\epsilon/2\) gives \(\langle\phi(u),\phi(v)\rangle\le 1-\frac{1}{2(T^2+1)^2}\); the stated \(\delta_T\) is a slackened bound.

**Proposition 2** (Affine Update)**.** _Fix constants_ \(a,b\in\mathbb{R}\)_. Let_ \(\phi(v)=(s_1,s_2,-s_1,-s_2)\)_. Then_ \(\phi(av+b)=\mathrm{layernorm}(as_1+bs_2,s_2,-(as_1+bs_2),-s_2)\).


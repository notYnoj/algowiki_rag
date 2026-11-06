To first order, the two contributions to the bound are \(3\epsilon\|\mathcal{L}\|\|x\|_2\|y\|_2\) and \(3\epsilon\sigma(\Xi)\|x\|_2\|y\|_2\), respectively. With exact original inputs and no rounding of the final output, only (123) is needed. The assumptions exclude overflow and underflow and also apply to complex vectors with the stated normwise bounds.

Within this error model, the intermediate-error bound is sharp in general, but need not have the best constant for a particular factorization. To see the possible amplification, choose unit inputs with \(|a_\ell^Tx|=\|a_\ell\|_2\) and \(|b_\ell^Ty|=\|b_\ell\|_2\), and allow a relative error of magnitude \(\epsilon\) in only product \(\ell\). With the other operations exact, the resulting error is

\(\|\delta z\|_2=\epsilon\|a_\ell\|_2\|b_\ell\|_2\|c_\ell\|_2.\) (126)

For one rank-one term this product equals \(\sigma(\Xi)\); allowing all three intermediate roundings with the same sign attains the coefficient \((1+\epsilon)^3-1\). Section 7.3 establishes sharpness of the parameter-growth exponent for the centered constructions.

For the target map M of (108), \(\|\mathcal{M}\|=1\). Indeed,

\(\|\mathcal{M}(x,y)\|_2^2=\sum_{t=1}^m\|X^{(t)}Y^{(t)}\|_F^2\le\sum_{t=1}^m\|X^{(t)}\|_F^2\|Y^{(t)}\|_F^2\le\|x\|_2^2\|y\|_2^2,\) (127)

and equality is attained by inputs selecting a single scalar product. For \(\mathcal{M}_\lambda\), Lemma 8 gives \(\|\mathcal{M}_\lambda\|\le 1+\beta(\lambda)\). Thus the input-sensitivity term stays bounded as \(\lambda\rightarrow 0\), even when the intermediate-error bound grows.

**Lemma 10** (Classical spectral-norm product)**.** _For classical evaluation of the independent products in_ (108)_, the spectral-norm product is_

\(\sigma_c=n^{(max_t|U_t|+max_t|V_t|+max_t|W_t|)/2}.\) (128)

_For a balanced family_ \(\mathcal{S}\subseteq B_{N,N,N}\)_, the matrix dimension is q=n<sup>N</sup>, so_ \(\sigma_c=q^{3/2}=n^{3N/2}\)_, independently of the number of products._

_Proof._ Write \(\Xi=(A,B,C)\) for the classical algorithm. Its columns are indexed by the scalar products \(X_{\alpha\beta}^{(t)}Y_{\beta\gamma}^{(t)}\): the column of _A_ selects \(X_{\alpha\beta}^{(t)}\), that of _B_ selects \(Y_{\beta\gamma}^{(t)}\), and that of _C_ adds the product to output entry \((\alpha,\gamma)\) of block _t_. Every column is a standard basis vector. Each input entry of _X_<sup>(_t_)</sup> is used _n_<sup>|_U<sub>t</sub>_|</sup> times, each input entry of _Y_ <sup>(_t_)</sup> is used _n_<sup>|_V<sub>t</sub>_|</sup> times, and each output entry accumulates _n_<sup>|_W<sub>t</sub>_|</sup> products. Consequently,

\(AA^*=\oplus_{t=1}^mn^{|U_t|}I,BB^*=\oplus_{t=1}^mn^{|V_t|}I,CC^*=\oplus_{t=1}^mn^{|W_t|}I,\) (129)

with identity blocks of the corresponding input or output dimensions. Taking the square root of the largest coefficient in each matrix gives (128).

The ratio \(\sigma(\Xi)/\sigma_c\) compares the bounds for intermediate rounding errors under the same assumptions. Tensor products multiply \(\sigma(\Xi)\), so _k_ recursive uses of a fixed square base raise its normalized ratio to the _k_th power.

## 7.3 Factor norms of the aggregation constructions

The construction of Definition 22 has factor matrices

\(\Xi(\lambda)=(A(\lambda),B(\lambda),C(\lambda)),\mathcal{M}_\lambda(x,y)=C(\lambda)\big((A(\lambda)^Tx)\odot(B(\lambda)^Ty)\big).\) (130)

We now compute the spectral-norm product of Definition 24 from the row Gram matrices \(A(\lambda)A(\lambda)^*\), \(B(\lambda)B(\lambda)^*\), and \(C(\lambda)C(\lambda)^*\). Each is block diagonal in the original tensor blocks, and each diagonal block is a scalar multiple of the identity. For a balanced tripartition set without corrections or parameter scaling, all these scalars equal (_n_+1)_<sup>N</sup>_. Corrections and parameter exponents change the scalars while preserving this diagonal structure. Thus the spectral norms are the square roots of the largest block coefficients.

Recall the selected correction family Q from Theorem 3. The main aggregate has coefficient one, and the correction indexed by \(P\in\mathcal{Q}\) has coefficient (-1)<sup>|_P_|</sup>(_n_+1)<sup>|_P_|</sup>. We distribute (_n_+1)<sup>|_P_|/3</sup> to each of<tbc>


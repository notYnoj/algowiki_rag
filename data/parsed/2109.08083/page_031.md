(_ii)_ \(\sum iv_i=0(modn)\)_, and_<tbc>

(_iii)_ \(\sum_{i\in V^{X+Y}}i^2v_i=0(modn)\)

_is in_ \(\mathcal{L}_1^{X+Y}(\mathcal{T})\)_. Supposing that n is even, we have that any vector_ **v** _which only has non-zero support in V_ <sup>_X+Y_</sup> _and satisfies_

(_i)_ \(\sum v_i=0\),<tbc>

(_ii)_ \(\sum iv_i=0(modn)\),<tbc>

_(iii)_ \(2n|\sum_{i\in V^{X+Y}}i^2v_i\)<tbc>

_is in_ \(\mathcal{L}_1^{X+Y}(\mathcal{T})\).

To prove the converse is considerably more complicated. We defer the proof of Proposition 3.17 to after the proof of Lemma 4.14, from which it follows, in Section 4.3 where we discuss the ‘bounded integral decomposition lemma’.

As done for \(\mathcal{T}'\), we may also deduce the following two results regarding any vector in the lattice L(T). The proofs use the same strategy as for Lemma 3.12 and Corollary 3.13 respectively.

Lemma 3.18. _First suppose that n is odd. We have that_ \(\mathbf{v}\in\mathcal{L}(\mathcal{T})\) _if and only if the following all hold:_

(_i)_ \(\sum_iv_i^X=\sum_iv_i^Y=\sum_iv_i^{X+Y}=\sum_iv_i^{X-Y}\),<tbc>

(_ii)_ \(\sum_iv_i^X+\sum_iv_i^Y=\sum_iv_i^{X+Y}modn\),<tbc>

_(iii)_ \(\sum_iv_i^X-\sum_iv_i^Y=\sum_iv_i^{X-Y}modn\),<tbc>

_(iv)_ \(2\sum_i^2v_i^X+2\sum_i^2v_i^Y=\sum_i^2v_i^{X+Y}+\sum_i^2v_i^{X-Y}modn\).

_Supposing now that n is even, we have that_ \(\mathbf{v}\in\mathcal{L}(\mathcal{T})\) _if and only if the following all hold:_

(_a)_ \(\sum_iv_i^X=\sum_iv_i^Y=\sum_iv_i^{X+Y}=\sum_iv_i^{X-Y}\),<tbc>

(_b)_ \(\sum_iv_i^X+\sum_iv_i^Y=\sum_iv_i^{X+Y}modn\),<tbc>

_(c)_ \(\sum_iv_i^X-\sum_iv_i^Y=\sum_iv_i^{X-Y}modn\),<tbc>

_(d)_ \(2n|(\sum_i^2v_i^{X+Y}+\sum_i^2v_i^{X-Y}-2\sum_i^2v_i^X-2\sum_i^2v_i^Y)\).

Proof. Considering an edge \(e\in\mathcal{T}\) we have that the vector \(\mathbf{v}\in\mathcal{L}(\mathcal{T})\) associated to the edge _e_ satisfies (i)-(iv) when _n_ is odd, and (a)-(d) when _n_ is even. Thus the associated vector of any linear combination of edges will also satisfy (i)-(iv) or (a)-(d) respectively, which by definition covers all \(\mathbf{v}\in\mathcal{L}(\mathcal{T})\). Considering now a vector **v** such that (i)-(iv) or (a)-(d) hold given _n_ is odd or even respectively, we may modify **v** to **u** by adding the shadow vectors of edges in such a way as to make \(\mathbf{u}^\mathbf{X},\mathbf{u}^\mathbf{Y}\equiv\mathbf{0}\). We may then modify **u** to **w** where \(\mathbf{w}^{\mathbf{X}-\mathbf{Y}}\equiv\mathbf{0}\) and we retain \(\mathbf{w}^\mathbf{X},\mathbf{w}^\mathbf{Y}\equiv\mathbf{0}\) by adding 2-part generators. (To see this, first note that we have \(\sum_iu_i^{X-Y}=0modn\). Then considering \(\mathcal{T}'\) with parts _X,Y,X-Y_ we know that \(\mathbf{u}^\mathbf{X}\cup\mathbf{u}^\mathbf{Y}\cup\mathbf{u}^{\mathbf{X}-\mathbf{Y}}\in\mathcal{L}(\mathcal{T}')\) by Proposition 3.8 thus we can use _SQ_-gens, which we know are the vertex shadow of linear combinatorics of edges of \(\mathcal{T}'\), to reduce **u<sup>X-Y</sup>** to **0**. But lifting back from \(\mathcal{T}'\) to T , these _SQ_-gens dictate appropriate 2-part generators which have precisely the same effect on the _X-Y_ part in T .) It is clear that this forces \(\sum_iw_i^{X+Y}=0\), \(\sum_iw_i^{X+Y}=0modn\) and \(\sum_i^2w_i^{X+Y}=0modn\). Furthermore, when _n_ is even we must have \(2n|\sum_i^2w_i^{X+Y}\). Thus by Proposition 3.17 we have that \(\mathbf{w}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\), so **w** can be seen as the vertex shadow of a linear combination of edges of T . But since **v** can be obtained from **w** by removing edges, we must then also have that \(\mathbf{v}\in\mathcal{L}(\mathcal{T})\). □


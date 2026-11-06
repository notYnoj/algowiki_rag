<tbc>\(S':=\sum_{a_{i_j}^\prime\in\mathbf{A}^\prime}|a'_{ij}|\le S-2\). This holds since, in \(\mathbf{A}'\), (_b,c_) and (_a,d_) which were both negative have gained weight 1 and so are closer to zero, and (_a,c_), which was positive, has lost weight 1, thus in total reducing the total sum by 3. In the worst case \(a_{bd}\le 0\) and so \(|a'_{bd}|=|a_{bd}|+1\), but then the total sum has still been reduced by 2. □

So we see that the integer span of the collection of simple matrices describes all \(n\times n\) integer matrices with zero-sum rows and columns.

Proposition 3.7. _Let_ \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T}')\)_. Then_

(_i)_ \(\sum_iv_i=0\)_, and_<tbc>

_(ii)_ \(\sum_iv_i=0(modn)\),

_where i sums over the coordinates in_ \(V(\mathcal{T}')\)_, and v<sub>i</sub> is the entry in_ **v** _associated with coordinate i._

Proof. Recall that any \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T}')\) is a vector obtained from an integer collection of edges such that the weights in the \(X\cup Y\) parts all cancel each other, leaving only non-zero weights in _V_ <sup>_X+Y_</sup>. Thus **v** must correspond to some \(n\times n\) integer matrix as in Proposition 3.6. Thus, by Proposition 3.6, this matrix can be decomposed as the sum of simple matrices. Note that these simple matrices yield +1 weights at coordinates _a+c_ and _b+d_, and -1 weights at _a+d_ and _b+c_ in _V_ <sup>_X+Y_</sup>, (where it could be that _a+c=b+d_, or _a+d=b+c_, but not both), thus yielding weight vectors \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T}')\) such that all entries are 0 except either two +1 entries and two -1 entries, or two \(\pm 1\) entries and a \(\mp 2\) entry (with all support in _X+Y_). That is, each of these simple matrices adds a total of 1+(-1)+(-1)+1=0 to \(\sum_iv^i\), which yields the first property. To see the second, for each of the simple matrices in the decomposition, let \(a':=a+c\), \(b':=a+d\), \(c'=b+c\) and \(d':=b+d\). It follows that \(a'+d'=b'+c'(modn)\). Hence, each contributes \(a'+(-b')+(-c')+d'=(a'+d')-(b'+c')=0(modn)\) to \(\sum_iv_i\), and the result follows. □

The converse is also true:

Proposition 3.8. _Suppose_ **v** _is a vector with non-zero weights only on vertices in V_ <sup>_X+Y_</sup> _such that_

(_i)_ \(\sum_iv_i=0\)_, and_<tbc>

_(ii)_ \(\sum_iv_i=0(modn)\).

_Then_ \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T}')\).

To prove this, we first prove the following proposition (which follows from a similar argument to that in the proof of Proposition 3.6).

Proposition 3.9. _Suppose_ **v** _is a vector with non-zero weights only on vertices in V_ <sup>_X+Y_</sup> _such that_

(_i)_ \(\sum_iv_i=0\)_, and_<tbc>

_(ii)_ \(\sum_iv_i=0(modn)\).

_Then_ **v** _can be efficiently written as the sum of_ (1,-1,-1,1) _vectors with indices of the form_ (_a,b,c,b+c-a), where a, b, c, and b+c-a are all distinct._

We remark that, by _efficiently_, we mean that **v** can be decomposed into _O_(|**v**|) such vectors.


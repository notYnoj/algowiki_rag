## 2.3 Degeneration and border rank

Let \(\varepsilon\) be an indeterminate over F, let \(S\in U_1\otimes V_1\otimes W_1\) and \(T\in U_2\otimes V_2\otimes W_2\) be tensors, and choose bases of their legs. Then _T_ is a _degeneration_ of _S_, written \(T\unknown S\), if there are integers \(q,d\ge 0\), matrices _A_<sub>1</sub>, _A_<sub>2</sub> and _A_<sub>3</sub> with entries in \(\mathbb{F}[\varepsilon]\) of sizes \(dimU_2\times dimU_1\), \(dimV_2\times dimV_1\) and \(dimW_2\times dimW_1\), and tensors \(T_1,\dots,T_d\in U_2\otimes V_2\otimes W_2\), such that

\((A_1\otimes A_2\otimes A_3)S=\varepsilon^qT+\varepsilon^{q+1}T_1+\cdots+\varepsilon^{q+d}T_d.\)

This is the polynomial formulation of Strassen’s definition \[Str87, Lemmas 5.5 and 5.9\]; see also the book of Bürgisser, Clausen and Shokrollahi \[BCS97, Definition 15.19\]. The _border rank_ of a tensor _T_ is the least integer \(r\ge 0\) such that \(T\unknown\langle r\rangle\).

From now on, _z_ is an indeterminate over F. The field F(_z_) of rational functions in _z_ with coefficients in F is an infinite extension field of F, and every tensor over F is also a tensor over F(_z_).

**Lemma 2.2** (Strassen \[Str87, Lemmas 5.6 and 5.9\])**.** _Let S and T be tensors over_ F.

(i) _If_ \(T\le S\)_, then_ \(T\unknown S\).<tbc>

(ii) \(\unknown\) _is transitive._<tbc>

(iii) _For all tensors S_<sub>1</sub>_, T_<sub>1</sub>_, S_<sub>2</sub> _and T_<sub>2</sub> _over_ F _with_ \(T_1\unknown S_1\) _and_ \(T_2\unknown S_2\)_, we have_ \(T_1\oplus T_2\unknown S_1\oplus S_2\) _and_ \(T_1\otimes T_2\unknown S_1\otimes S_2\).<tbc>

(iv) _If_ \(T\le S\) _as tensors over_ F(_z), then_ \(T\unknown S\).<tbc>

(v) _For every_ \(\pi\in\mathfrak{S}_3\)_, if_ \(T\unknown S\)_, then_ \(\pi\cdot T\unknown\pi\cdot S\).

_Proof._ Part (i) holds with _q=d_=0 and the matrices of the restriction. Parts (ii) and (iii) are \[Str87, Lemma 5.6(ii) and (iii)\]. Part (v) follows from the definition of degeneration, by permuting the three matrices.

Part (iv) is the implication from (ii) to (i) in \[Str87, Lemma 5.9\], with _g_=0 and _z_ in the role of \(\varepsilon\). We give a proof for convenience of the reader. Suppose that \(T=(A_1\otimes A_2\otimes A_3)S\) for matrices _A<sub>i</sub>_ with entries in F(_z_). Choose nonzero polynomials \(p_1,p_2,p_3\in\mathbb{F}[z]\) such that the matrices _B<sub>i</sub>=p<sub>i</sub>A<sub>i</sub>_ have entries in F\[_z_\]. Then \((B_1\otimes B_2\otimes B_3)S=fT\), where _f=p_<sub>1</sub>_p_<sub>2</sub>_p_<sub>3</sub> is a nonzero polynomial. Write \(f(z)=\lambda z^q+z^{q+1}g(z)\) with \(\lambda\in\mathbb{F}\backslash\{0\}\), an integer \(q\ge 0\) and \(g\in\mathbb{F}[z]\). Then

\((\lambda^{-1}B_1\otimes B_2\otimes B_3)S=z^qT+z^{q+1}\lambda^{-1}g(z)T,\)

and replacing _z_ by \(\varepsilon\) shows that \(T\unknown S\).

## 2.4 Degeneration from block triangular tensors and weights

We will give a degeneration from a block triangular tensor to its diagonal blocks, and then a sufficient condition for degeneration in terms of weights. The first degeneration acts only on the second and third legs, in the following sense.

Let \(S\in U\otimes V_1\otimes W_1\) and \(T\in U\otimes V_2\otimes W_2\) be tensors with the same first leg _U_, and choose bases of their legs, with the same basis of _U_ for both. Then _T_ is a _degeneration of S on the second and third legs_, written \(T\unknown_1S\), if \(T\unknown S\) with the identity matrix _I_ as _A_<sub>1</sub> (Section 2.3), that is, if

\((I\otimes A_2\otimes A_3)S=\varepsilon^qT+\varepsilon^{q+1}T_1+\cdots+\varepsilon^{q+d}T_d\)

for integers \(q,d\ge 0\), matrices _A_<sub>2</sub> and _A_<sub>3</sub> with entries in \(\mathbb{F}[\varepsilon]\), and tensors \(T_1,\dots,T_d\in U\otimes V_2\otimes W_2\). Like \(\unknown\) (Lemma 2.2(ii)), the relation \(\unknown_1\) is transitive: after \(\varepsilon\) is replaced by a suitable power of \(\varepsilon\) in the degeneration that is applied first, the matrices of two such degenerations compose leg by leg, so the matrix on the first leg stays the identity.


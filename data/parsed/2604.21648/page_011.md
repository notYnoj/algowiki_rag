<tbc>and replacing \(\widetilde{M}^{-1}\) with \(\widehat{M}^{-1}\).

_(5)_ \(\Rightarrow\) _(4):_ Let \(\sigma(\widehat{M}^{-1}B)\subseteq(0,1]\). By its structure

\(B^\frac{1}{2}\widehat{M}^{-1}B^\frac{1}{2}=(I-B^\frac{1}{2}M^{-1}AB^{-\frac{1}{2}})(I-B^\frac{1}{2}M^{-1}AB^{-\frac{1}{2}})^H\)

is HPSD and with \(\sigma(B^\frac{1}{2}\widehat{M}^{-1}B^\frac{1}{2})=\sigma(\widehat{M}^{-1}B)\subseteq(0,1]\) it must be HPD. Then \(\widehat{M}^{-1}\) is also HPD.

_(4)_ \(\Rightarrow\) _(1):_ Assume that \(\widehat{M}^{-1}\) is HPD. Then \(B^\frac{1}{2}\widehat{M}^{-1}B^\frac{1}{2}\) is also HPD and thus has positive real eigenvalues. Then every eigenvalue of \(I-B^\frac{1}{2}\widehat{M}^{-1}B^\frac{1}{2}\) must be smaller than 1 and with a similar argument as (3.12) we obtain _(1)._ □

The smoothing assumption can be characterized even further if we add the assumption that _M_<sup>-1</sup>_A_ is _B_-normal.

Corollary 3.6. _Let_ \(\widetilde{M}^{-1}\) _and_ \(\widehat{M}^{-1}\) _be defined as in_ (3.7) _and_ (3.8)_, respectively. Let M_<sup>-1</sup>_A be B-normal. Then the following statements are equivalent:_

_(1)_ \(\|I-M^{-1}A\|_B<1\).

_(2)_ \(\widetilde{M}^{-1}=\widehat{M}^{-1}\) _is HPD._

_(3)_ \(\sigma(\widetilde{M}^{-1}B)=\sigma(\widehat{M}^{-1}B)\subseteq(0,1]\).

_(4)_ \(|\lambda-1|^2<1\) _for all eigenvalues_ \(\lambda\) _of M_<sup>-1</sup>_A._

_(5)_ \(\rho(I-M^{-1}A)<1\)

_Proof._ Let _M_<sup>-1</sup>_A_ be _B_-normal. Then \(\widehat{M}^{-1}\) and \(\widetilde{M}^{-1}\) coincide (see Proposition 3.3) and the first three equivalences result from Theorem 3.5 above.

_(3)_ \(\Leftrightarrow\) _(4):_ Let \((\lambda,z)\) be an eigenpair of _M_<sup>-1</sup>_A._ By Theorem 2.9 (4), the eigenvector _z_ of _M_<sup>-1</sup>_A_ to the eigenvalue \(\lambda\) is also an eigenvector of (_M_<sup>-1</sup>_A_)<sup>+</sup> to the eigenvalue \(\overline{\lambda}\). Thus, we obtain

\(\widetilde{M}^{-1}Bz=(M^{-1}A+(M^{-1}A)^+-(M^{-1}A)^+M^{-1}A)z=(\lambda+\overline{\lambda}-\overline{\lambda}\lambda)z\)

with \(0<\lambda+\overline{\lambda}-\overline{\lambda}\lambda\le 1\). By adding -1 on both sides and multiplying by -1 we get

\(0\le 1-\lambda-\overline{\lambda}+\overline{\lambda}\lambda<1\)

which is equivalent to \(0\le|\lambda-1|^2<1\). Because \(\lambda\) was arbitrary, this holds for all eigenvalues \(\lambda\) of _M_<sup>-1</sup>_A._ The converse is analogous.

_(1)_ \(\Leftrightarrow\) _(5):_ This follows from Proposition 2.14. □

Using this result we also obtain the following Corollary.

Corollary 3.7. _Assume that the smoothing assumption is satisfied. Then the matrices_ \(\widetilde{M}^{-1}B\) _and_ \(\widehat{M}^{-1}B\) _as in_ (3.9) _and_ (3.10)_, respectively, are nonsingular for any choice of nonsingular_ \(M\in\mathbb{C}^{n\times n}\) _such that M_<sup>-1</sup>_A is B-normal._

With Proposition 2.14 we obtain the following.

Corollary 3.8. _Let M_<sup>-1</sup>_A be B-normal. Then_ \(\|I-M^{-1}A\|_B=\rho(I-M^{-1}A)\).

_Remark_ 3.9. For the case _A=B_ HPD and _M_ Hermitian, this result is already known \[3, Lemma 2.11\]. Then it holds

(3.13) \(\|I-M^{-1}A\|_A=\rho(I-M^{-1}A).\)

Given this assumptions we have (_M_<sup>-1</sup>_A_)<sup>+</sup>=_M_<sup>-_H_</sup>_A=M_<sup>-1</sup>_A_ and _M_<sup>-1</sup>_A_ is _B_- orthogonal, in particular also _B_-normal and we obtain (3.13) from Corollary 3.8.


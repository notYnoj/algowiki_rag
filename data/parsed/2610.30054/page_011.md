## 2.2 Restriction and tensor rank

Let \(S\in U_1\otimes V_1\otimes W_1\) and \(T\in U_2\otimes V_2\otimes W_2\) be tensors. Then _T_ is a _restriction_ of _S_, written \(T\le S\), if there are linear maps \(A_1:U_1\rightarrow U_2\), \(A_2:V_1\rightarrow V_2\) and \(A_3:W_1\rightarrow W_2\) such that \(T=(A_1\otimes A_2\otimes A_3)S\). If these maps can be chosen invertible, then _S_ and _T_ are _isomorphic_, written \(S\cong T\).

Two tensors are equivalent if each is a restriction of the other. Let S<sub>F</sub> be the set of equivalence classes. Strassen showed that direct sum and tensor product make S<sub>F</sub> a commutative semiring: both operations are associative and commutative and have identity elements, and the tensor product distributes over the direct sum \[Str87, Section 2\]. Restriction induces a partial order on S<sub>F</sub>, and it is compatible with both operations: if \(T_1\le S_1\) and \(T_2\le S_2\), then \(T_1\oplus T_2\le S_1\oplus S_2\) and \(T_1\otimes T_2\le S_1\otimes S_2\) \[Str87, Section 3\].

The _tensor rank_ R<sub>F</sub>(_T_) of a tensor \(T\in U\otimes V\otimes W\) is the least integer \(r\ge 0\) such that \(T=\sum_{i=1}^ru_i\otimes v_i\otimes w_i\) with \(u_i\in U\), \(v_i\in V\) and \(w_i\in W\) for \(i\in[r]\). The _exponent of matrix multiplication_ over F is

\(\omega_\mathbb{F}:=inf\{\tau\in\mathbb{R}:\mathrm{R}_\mathbb{F}(\langle n,n,n\rangle)=\mathcal{O}(n^\tau)\},\)

as in \[Str87, (1.3)\].

The _flattening ranks_ R<sub>(1)</sub>(_T_), R<sub>(2)</sub>(_T_) and R<sub>(3)</sub>(_T_) of a tensor \(T\in U\otimes V\otimes W\) are the matrix ranks of the images of _T_ in \(U\otimes(V\otimes W)\), \(V\otimes(U\otimes W)\) and \(W\otimes(U\otimes V)\).

**Lemma 2.1.** _Let S and T be tensors over_ F.

(i) _If_ \(T\neq 0\)_, then_ \(\langle 1\rangle\le T\).<tbc>

(ii) _The tensor rank_ R<sub>F</sub>(_T_) _is the least integer_ \(r\ge 0\) _such that_ \(T\le\langle r\rangle\).<tbc>

(iii) _For all integers_ \(n_1,n_2,n_3,m_1,m_2,m_3\ge 1\)_, we have_<tbc>

<tbc>\(\langle n_1,n_2,n_3\rangle\otimes\langle m_1,m_2,m_3\rangle\cong\langle n_1m_1,n_2m_2,n_3m_3\rangle.\)<tbc>

(iv) _For every_ \(\pi\in\mathfrak{S}_3\)_, we have_ \(\pi\cdot(S\oplus T)\cong(\pi\cdot S)\oplus(\pi\cdot T)\), \(\pi\cdot(S\otimes T)\cong(\pi\cdot S)\otimes(\pi\cdot T)\) _and_ \(\pi\cdot\langle 1\rangle=\langle 1\rangle\)_, and if_ \(T\le S\)_, then_ \(\pi\cdot T\le\pi\cdot S\).<tbc>

(v) _For all integers_ \(n_1,n_2,n_3\ge 1\),

\(\text{(123)}\cdot\langle n_1,n_2,n_3\rangle=\langle n_3,n_1,n_2\rangle,\text{(12)}\cdot\langle n_1,n_2,n_3\rangle\cong\langle n_3,n_2,n_1\rangle,\text{(132)}\cdot\langle n_1,n_2,n_3\rangle=\langle n_2,n_3,n_1\rangle,\text{(13)}\cdot\langle n_1,n_2,n_3\rangle\cong\langle n_1,n_3,n_2\rangle,\text{(23)}\cdot\langle n_1,n_2,n_3\rangle\cong\langle n_2,n_1,n_3\rangle.\)

_Hence_ \(\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\langle n_1,n_2,n_3\rangle\cong\langle n_1n_2n_3,n_1n_2n_3,n_1n_2n_3\rangle^{\otimes 2}\).

_Proof._ Part (i) is in \[Str87, Section 3, before Proposition 3.3\], and part (ii) is \[Str87, Proposition 3.2\]. For part (iii), the maps \(E_{ij}\otimes E_{k\ell}\mapsto E_{(i,k),(j,\ell)}\) on the three legs give the isomorphism. Part (iv) holds since permuting the factors of a tensor product commutes with direct sums, tensor products and linear maps on the factors. For part (v), write \(\langle n_1,n_2,n_3\rangle=\sum_{i,j,k}E_{ij}\otimes E_{jk}\otimes E_{ki}\). The permutation (123) moves the third leg to the front, which gives \(\sum_{i,j,k}E_{ki}\otimes E_{ij}\otimes E_{jk}=\langle n_3,n_1,n_2\rangle\), and (132) moves the first leg to the back, which gives \(\sum_{i,j,k}E_{jk}\otimes E_{ki}\otimes E_{ij}=\langle n_2,n_3,n_1\rangle\). The permutation (12) gives \(\sum_{i,j,k}E_{jk}\otimes E_{ij}\otimes E_{ki}\), and transposing the matrices on all three legs turns it into \(\sum_{i,j,k}E_{kj}\otimes E_{ji}\otimes E_{ik}=\langle n_3,n_2,n_1\rangle\). In the same way, for each transposition, exchanging the two legs and transposing the matrices keeps the parameter that the two legs have in common in its place and exchanges the other two: legs 1 and 3 have _n_<sub>1</sub> in common, and legs 2 and 3 have _n_<sub>3</sub>. The six tensors \(\pi\cdot\langle n_1,n_2,n_3\rangle\) are thus isomorphic to the six tensors \(\langle n_{\sigma(1)},n_{\sigma(2)},n_{\sigma(3)}\rangle\) with \(\sigma\in\mathfrak{S}_3\), and by part (iii) their tensor product is isomorphic to \(\langle n_1n_2n_3,n_1n_2n_3,n_1n_2n_3\rangle^{\otimes 2}\).


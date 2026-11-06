First make the rational matrices act on integer addresses. Temporarily represent fields in a fixed radix (base) _q_. A short field of _f_ digits is an element of the residue ring Z_/q<sup>f</sup>_Z. Interpret a rational coefficient _a/b_ as _ab_<sup>-1</sup> in this ring, where _b_<sup>-1</sup> is the modular inverse of _b_. Fix all edge differences and the factorizations and inverses used below, then choose an odd prime _q_ avoiding every denominator and every numerator of a diagonal entry of an invertible triangular factor. There are finitely many coefficients, so such a choice exists. The identities then hold for every _f_, and the invertible factors remain invertible. Only address arithmetic changes: the streams still contain bits and the gates still use XOR.

**Lemma 6.2** (One level of the coding recursion)**.** Suppose the two fields each have _e=mf_ base-_q_ digits, the number of prefix segments is divisible by _W_, and the array contains _V_ bits. A complete interchange reduces to _S_ address-field interchanges of width _f_, each on _V/W_ bits. Apart from these recursive calls, it requires _O_(1+_V/(Bw_)) block transfers and a fixed number of block buffers.

_Proof._ Partition each long field into _m_ short fields of width _f_, and put _Q_<sub>0</sub>=_q<sup>f</sup>_. Regard _H,D_ as vectors in (Z_/q<sup>f</sup>_Z)_<sup>m</sup>_; the intervening coordinate _g_ and all outer coordinates remain fixed throughout.

## Partial swaps.

For an orthogonal projection _P_, define the address permutation<tbc>

\(D_P\left(\begin{array}{ c }
H \\
D
\end{array}\right)=\left(\begin{array}{ c c }
I-P & P \\
P & I-P
\end{array}\right)\left(\begin{array}{ c }
H \\
D
\end{array}\right).\) (16)

<tbc>It exchanges the projected components of _H,D_ and fixes their complementary components. We have \(D_P^2=I\), _D_<sub>0</sub>=_I_, and _D<sub>I</sub>(H,D_)=(_D,H_). If _Q_ is another orthogonal projection and \(P\le Q\), meaning that the image of _P_ is contained in the image of _Q_, then

\(D_QD_P=D_{Q-P}.\)

The reverse transition has the same formula because every _D<sub>P</sub>_ is an involution. Thus changing between the storage orders associated with two nested subspaces requires a partial swap defined by their projection difference. The rank of that projection difference is exactly the dimension difference counted in _S_.

## A rank-_r_ projection requires _r_ short interchanges.

Let _r_=rank_P_. Apply Gram-Schmidt without unit-length normalization to obtain a rational orthogonal basis of the image of _P_. This expresses _P_ as the sum of _r_ pairwise orthogonal rank-one projections, and the corresponding partial swaps multiply to _D<sub>P</sub>_. It suffices to implement a projection onto one rational vector \(u\neq 0\).

Put \(\xi=(u,-u)\in\mathbb{Q}^{2m}\) and \(\nu=\xi^\mathsf{T}\xi\). Then \(D_P=I-2\xi\xi^\mathsf{T}/\nu\) is the reflection in \(\xi^\perp\). Let _i,j_ be the first and last indices at which \(\xi\) is nonzero. Thus _i_ is in the first field and _j_ in the second. Set \(\alpha=-\nu/(2\xi_j)\), and let _e<sub>k</sub>_ denote the _k_th coordinate unit vector. Define the columns of a matrix _L_ by<tbc>

\(L_i=\xi+\alpha e_j,L_j=\alpha e_j,L_k=e_k-\frac{\xi_k}{\xi_j}e_j(i<k<j),\)

<tbc>and _L<sub>k</sub>=e<sub>k</sub>_ at all other indices. This matrix is lower triangular: \(\xi\) has no coordinate before _i_ or after _j_. Its diagonal entries at _i,j_ are \(\xi_i,\alpha\neq 0\) and all others are one, so it is invertible. Reflection exchanges _L<sub>i</sub>,L<sub>j</sub>_, while every other column is orthogonal to \(\xi\) and is fixed. Therefore, writing _T<sub>ij</sub>_ for the coordinate transposition,<tbc>

\(D_PL=LT_{ij},D_P=LT_{ij}L^{-1}.\) (17)


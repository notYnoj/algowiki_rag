## APPENDIX A: PROOF OF LEMMA 1

_Proof._ To prove claim 1) of the lemma, let _s_ be the _smallest_ integer for which the binary expansions of the pair `sum`(_L,i_) and `sum`(_L,j_) differ on the _s<sup>th</sup>_ bit. We first prove that _s_ and _t=t<sub>ij</sub>_ (cfr, eq. (13)) have the same value.

First of all, by definition of _s_, we know that the binary expansions of `sum`(_L,i_) and `sum`(_L,j_) are equal on the first _s_-1 bits. Moreover, since `sum`(_L,i_) and `sum`(_L,j_) are equal on the first _s_-1 bits and \(\text{\texttt{sum}}(L,i)<\cdots<\text{\texttt{sum}}(L,j)\), it follows that for each _k=i,...,j_-1, the binary expansions of `sum`(_L,k_) and `sum`(_L,k_+1) are equal on the first _s_-1 bits, too. Therefore, it holds that \(s\le t\).

Since `sum`(_L,i_) and `sum`(_L,j_) differ on the _s<sup>th</sup>_ bit and `sum`(_L,i)\<_`sum`(_L,j_), we know that the _s<sup>th</sup>_ bit of `sum`(_L,i_) is 0, while the _s<sup>th</sup>_ bit of `sum`(_L,j_) is 1. As a consequence, since \(\text{\texttt{sum}}(L,i)<\cdots<\text{\texttt{sum}}(L,j)\) and for each _k=i,...,j_-1, _both_ the binary expansions of `sum`(_L,k_) _and_ of `sum`(_L,k_+1) are equal on the first _s_-1 bits, there must exist an index \(k\in\{i,\dots,j-1\}\) such that the _s<sup>th</sup>_ bit of `sum`(_L,k_) is 0, and the _s<sup>th</sup>_ bit of `sum`(_L,k_+1) is 1. Therefore, since \(t=t_{ij}=min_{i\le k<j}t_k\) and there exists _k_ such that _t<sub>k</sub>=s_, it holds that \(s\ge t\). Thus, we finally get that _s=t_.

One can also see that \(s=\lceil-log_2(\text{\texttt{sum}}(L,i)\oplus\text{\texttt{sum}}(L,j))\rceil\), where \(\text{\texttt{sum}}(L,i)\oplus\text{\texttt{sum}}(L,j)\) is the numerical value whose binary expansion is equal to the XOR operation between the<tbc>

<tbc>binary expansions of `sum`(_L,i_) and `sum`(_L,j_). Indeed, since the binary expansions of `sum`(_L,i_) and `sum`(_L,j_) are equal on the first _s_-1 bits, it holds that the binary expansion of the value \(\text{\texttt{sum}}(L,i)\oplus\text{\texttt{sum}}(L,j)\) contains the first bit equal to 1 exactly in the _s<sup>th</sup>_ position. Therefore, one gets that _s_ is the smallest integer for which it holds that

\(2^{-s}\le\text{\texttt{sum}}(L,i)\oplus\text{\texttt{sum}}(L,j).\) (41)

From (41), we get that \(s=\lceil-log_2(\text{\texttt{sum}}(L,i)\oplus\text{\texttt{sum}}(L,j))\rceil\).

To prove claim 2) of the lemma, let \(z\in\{i,\dots,j-1\}\) denote the index for which it holds that _t<sub>z</sub>=t<sub>ij</sub>_. Then, we have that the binary expansion of `sum`(_L,z_) differs from the binary expansion of `sum`(_L,z_+1) on the \(t_{ij}^{th}\) bit. In particular, from the definition of _t<sub>z</sub>_, the binary expansions of `sum`(_L,z_) and `sum`(_L,z_+1) are equal on the first _t<sub>ij</sub>_-1 bits, and, since `sum`(_L,z)\<_`sum`(_L,z_+1), we have that `sum`(_L,z_) has a binary expansion with 0 in the \(t_{ij}^{th}\) position, while `sum`(_L,z_+1) has a binary expansion with 1 in the \(t_{ij}^{th}\) position. Finally, since \(\text{\texttt{sum}}(L,i)<\cdots<\text{\texttt{sum}}(L,j)\) and since the binary expansions of the values in the subset {`sum`(_L,i),...,_`sum`(_L,j_)} are equal on the first _t<sub>ij</sub>_-1 bits (this comes from the definition of _t<sub>ij</sub>_), we get that for the index _z_ it holds that

\(\text{\texttt{sum}}(L,z)<\text{\texttt{trunc}}(t_{ij},\text{\texttt{sum}}(L,i))+2^{-t_{ij}}\)

and

\(\text{\texttt{sum}}(L,z+1)\ge\text{\texttt{trunc}}(t_{ij},\text{\texttt{sum}}(L,i))+2^{-t_{ij}}.\)

This concludes the proof.

## APPENDIX B

**Lemma 4.** _For any non-increasing dyadic distribution_ \(\phi=(\phi_1,\dots,\phi_m)\)_, let_ \(\nu'=(0,\phi_1,0,\dots,0,\phi_m,0)\) _be its fully extended distribution, then there does not exist any alphabetic code with lengths_ \(L=\langle\ell_1,\dots,\ell_{2m+1}\rangle\) _defined as follows_

\(\ell_i=\left\{\begin{array}{ c c }
x_i & \text{\textit{if}}\nu'_i=0, \\
\lceil-log_2\nu'_i\rceil+1 & \text{\textit{if}}\nu'_i>0,
\end{array}\right.\)

_where_ \(x_i\in\mathbb{N}_+\) _are arbitrarily chosen values._

_Proof._ Without loss of generality let us assume that \(\phi_m>0\). Otherwise, we can simply show that the lemma holds for \((\phi_1,\dots,\phi_{m-1})\) and hence for \(\phi\).

Let \(L=\langle\ell_1,\dots,\ell_{2m+1}\rangle\) be the list of lengths as defined in the statement of the Lemma. We will consider two cases. The first corresponds to the case in which, for each \(i\in\{1,3,\dots,2m-1\}\), we have \(x_i=\ell_i\ge\ell_{i+1}\) and \(x_{2m+1}=\ell_{2m+1}\ge\ell_{2m}\); the second case is for all other possible choices of the _x<sub>i</sub>_.

**Case 1**: Recall that, for \(i\in\{2,\dots,m\}\), we have that \(\alpha_i=min(\ell_{i-1},\ell_i)\). Since \(\phi\) is non-increasing, for each \(i\in\{2,4,\dots,2m-2\}\), we have that \(\ell_i\le\ell_{i+2}\). Thereby, for each \(i\in\{2,\dots,2m\}\), it holds that \(\alpha_i\le\alpha_{i+1}\). In particular, for each \(i\in\{2,4,\dots,2m\}\), we have that

\(\alpha_i=\alpha_{i+1}=\lceil-log_2\phi_\frac{i}{2}\rceil+1=-log_2\phi_\frac{i}{2}+1.\)


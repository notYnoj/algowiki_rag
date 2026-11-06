For convenience, this expression involves a slight abuse of notation, as the row and column indices start from 0 rather than 1. It is straightforward to verify that _F<sub>n</sub>_ is both symmetric and unitary. Extending this definition, the multi-level Fourier matrix for \(n\in\mathbb{N}^d\) is given by<tbc>

\(F_n:=F_{n_1}\otimes\cdots\otimes F_{n_d},\)

<tbc>and its _r_-block counterpart is defined as

\(F_{n,r}:=F_n\otimes I_r.\)

The matrix _F<sub>n</sub>_ preserves the symmetry and unitarity of its constituent matrices _F<sub>n<sub>i</sub></sub>_, _i_=1_,...,d_, as a direct consequence of the structural properties of the Kronecker product; the same holds for _F<sub>n,r</sub>_, which is unitary as well.<br>
_F<sub>n</sub>_ inherits its symmetry and unitarity from its components _F<sub>n<sub>i</sub></sub>_, _i_=1_,...,d_, by virtue of the properties of the Kronecker product.<br>
For any multi-level block circulant matrix, we have the following block-diagonalization.

**Theorem 3.4** _For all_ \(n\in\mathbb{N}^d\) _and_ \(r\in\mathbb{N}\),<tbc>

\(C_{n,r}=\left[A_{(i-j)modn}\right]_{i,j=1}^n=F_{n,r}\Lambda_{n,r}F_{n,r}^*,\) (3.4)

<tbc>_where_ \(\Lambda_{n,r}\) _is the block diagonal matrix_<tbc>

\(\Lambda_{n,r}:=\mathrm{diag}_{j=0,\dots,n-1}\left(p\left(\frac{2\pi j}{n}\right)\right),\)

<tbc>_whose_ \(r\times r\) _diagonal blocks are the values of_

\(p(\theta):=\sum_{k=0}^{n-1}A_ke^{ik\cdot\theta}\in\mathbb{C}^{r\times r},k\cdot\theta=k_1\theta_1+\cdots+k_d\theta_d.\)

The proof of this theorem relies on finding a diagonalization of the uni-level generator _Z<sub>n</sub>_, which can be obtained explicitly by computing its eigenvalues and eigenvectors. The block-diagonalization for _C<sub>n,r</sub>_ then follows directly from equation (3.2), and the extension to the multi-level case is achieved by exploiting the properties of the Kronecker product.<br>
Theorem 3.4 offers numerous significant discoveries. Every multi-level _r_-block circulant matrix is unitarily similar to the block diagonal matrix \(\Lambda_{n,r}\); in particular, it is normal if and only if each \(r\times r\) block \(p(2\pi j/n)\) is normal, which for _r_=1 is always the case. Secondly, the spectrum of _C<sub>n,r</sub>_ is the union of the spectra of these blocks,

\(\Lambda\big(C_{n,r}\big)=\bigcup_{j=0}^{n-1}\Lambda\big(p(\theta_j)\big),p(\theta_j)=\sum_{k=0}^{n-1}A_ke^{ik\cdot\theta_j},\theta_j:=\frac{2\pi j}{n},j=0,\dots,n-1,\)

which means that the blocks \(p(\theta_j)\) can be computed by performing the DFT of the first block column of _C<sub>n,r</sub>_. The corresponding invariant subspaces are spanned by the columns of _F<sub>n,r</sub>_. Moreover, for _r_=1 circulant matrices form an algebra that is closed under inversion, and every matrix in this algebra is uniformly diagonalized by _F<sub>n</sub>_; for _r\>_1 the block circulant matrices are simultaneously block-diagonalized by _F<sub>n,r</sub>_, and the algebraic operations are inherited from those of the blocks.


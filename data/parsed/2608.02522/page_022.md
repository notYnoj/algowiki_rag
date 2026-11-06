Before we can give the proof of Lemma 4.5, we first deduce the following handy consequence of Theorem 4.6. In the following, given a finite set _S_, a matrix \(A\in\mathbb{R}^{S\times S}\) and a subset \(T\subseteq S\), we denote by _A<sub>T</sub>_ the matrix obtained from _A_ by replacing all entries _A<sub>i,j</sub>_ where at least one of _i,j_ does not lie in _T_ by a 0. In other words, the \(T\times T\)-submatrix is inherited from _A_, while all other entries are 0-s.

**Lemma 4.7.** _Let S be a finite set, and let_ \(M\in\mathrm{Sym}_S\) _be a positive semidefinite matrix such that M<sub>s,s</sub>_=1 _for all_ \(s\in S\)_. Let_ \(q\in\mathbb{N}\)_. Then there exists a partition_ \(S=T_1\sqcup\cdots\sqcup T_q\) _of S (empty parts allowed) such that_

\(\|M_{T_i}\|\le\left(\sqrt{\frac{\|M\|}{q}}+1\right)^2\)

_for every_ \(i\in[q]\).

In the proof of this auxiliary result, we will use the following four well-known linear algebra facts:

1. Every positive semi-definite \(n\times n\)-matrix is the Gram matrix of a collection of _n_ vectors (this can, for instance, be proved via Cholesky-factorization).<tbc>

2. Every positive semidefinite \(n\times n\)-matrix can be written as a sum of matrices of the form \(\mathbf{u}\mathbf{u}^\top\) where **u** is an _n_-dimensional vector (this, in fact, is an easy consequence of the first fact stated above).<tbc>

3. For any matrix _B_, the two matrices \(B^\top B\) and \(BB^\top\) have the same non-zero eigenvalues (the proof is elementary).<tbc>

4. For any two positive semidefinite matrices _U_ and _V_ , we have \(\|U\|\le\|U+V\|\). This follows immediately from the representation of these spectral norms as maximal Rayleigh-quotients.

_Proof of Lemma 4.7._ Since \(M\in\mathbb{R}^{S\times S}\) is positive semidefinite by assumption of the lemma, the first linear algebra fact recorded above implies that _M_ is a Gram matrix of a collection of vectors \((\mathbf{b}_s)_{s\in S}\) in R_<sup>S</sup>_. In other words, we have that \(M_{s,s^\prime}=\mathbf{b}_s^\top\mathbf{b}_{s^\prime}\) for all \(s,s'\in S\). Denoting by \(B\in\mathbb{R}^{S\times S}\) the matrix whose column with index _s_ equals **b**_<sub>s</sub>_, for every \(s\in S\), we then have \(M=B^\top B\). Note that the matrix \(BB^\top\) is also positive semi-definite, and, by the third aforementioned linear algebra fact, has the same non-zero eigenvalues (which must all be positive). This in particular implies that \(\|BB^\top\|=\lambda_\mathrm{max}(BB^\top)=\lambda_\mathrm{max}(B^\top B)=\|B^\top B\|=\|M\|\). Now, consider the matrix \(C:=I_S-\frac{1}{\|M\|}BB^\top\) (this is well-defined: since all diagonal entries of _M_ are 1-s, we have \(\|M\|\ge 1\)). _C_ is clearly symmetric, and for every \(\mathbf{x}\in\mathbb{R}^S\) we have

\(\mathbf{x}^\top C\mathbf{x}=\mathbf{x}^\top\mathbf{x}-\frac{\mathbf{x}^\top(BB^\top)\mathbf{x}}{\|M\|}\ge\mathbf{x}^\top\mathbf{x}-\frac{\lambda_\mathrm{max}(BB^\top)(\mathbf{x}^\top\mathbf{x})}{\|M\|}\ge 0,\)

where we used that \(\lambda_\mathrm{max}(BB^\top)\le\|M\|\) in the last step. Hence, \(C\in\mathrm{Sym}_S\) is positive semidefinite. By the second linear algebra fact mentioned above, there are vectors **u**<sub>1</sub>_,...,_**u**_<sub>k</sub>_ for some \(k\in\mathbb{N}\) such that \(C=\sum_{i=1}^k\mathbf{u}_i\mathbf{u}_i^\top\). Note that since \(\mathbf{u}\mathbf{u}^\top=(\frac{1}{2}\mathbf{u})(\frac{1}{2}\mathbf{u})^\top+(\frac{1}{2}\mathbf{u})(\frac{1}{2}\mathbf{u})^\top+(\frac{1}{2}\mathbf{u})(\frac{1}{2}\mathbf{u})^\top+(\frac{1}{2}\mathbf{u})(\frac{1}{2}\mathbf{u})^\top\) and \((\frac{1}{2}\mathbf{u})^\top(\frac{1}{2}\mathbf{u})=\frac{1}{4}(\mathbf{u}^\top\mathbf{u})\) for every \(\mathbf{u}\in\mathbb{R}^S\), possibly by suitably increasing _k_ we may assume that we choose **u**<sub>1</sub>_,...,_**u**_<sub>k</sub>_ in this representation of _C_ such that \(\mathbf{u}_i^\top\mathbf{u}_i\le\frac{1}{\|M\|}\) for every \(i\in[k]\). Next, for every \(s\in S\), let us set \(\mathbf{u}_s:=\frac{1}{\sqrt{\|M\|}}\mathbf{b}_s\). Since _M_ is the Gram-matrix of the \((\mathbf{b}_s)_{s\in S}\) and by assumption<tbc>


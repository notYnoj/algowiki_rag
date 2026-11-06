## 4 A fixed matrix multiplication identity

We now compose the packing in both length parameters. Each round shrinks the coefficient matrices and increases the polynomial lengths; the terminal bound in Lemma 3.3 accounts for the cost of those longer polynomials.

### 4.1 Construction of the identity

The next theorem produces a single finite rational identity. Once its parameters have been fixed, ordinary block recursion will apply it to matrices of arbitrary size.

**Theorem 4.1** (A fixed identity)**.** _For every_ \(\tau>9/4\)_, there are computable integers_ \(v,r\ge 2\) _with_ \(r<v^\tau\)_, rational linear forms_ \(\ell_\nu,m_\nu\) _on_ \(v\times v\) _matrices, and rational matrices_ \(W_\nu\in\mathbb{Q}^{v\times v}\) _such that_<tbc>

\(AB=\sum_{\nu=1}^r\ell_\nu(A)m_\nu(B)W_\nu(A,B\in\mathbb{Q}^{v\times v}).\) (6)

<tbc>_Proof._ Fix \(c\ge 2\), to be chosen sufficiently large, and take _d=c_<sup>3</sup>, _u,w_ from (4), and \(\alpha=2w-1\). Set

\(R=\lfloor w/u\rfloor^2,\rho=1+\frac{3}{c-1}.\)

We have _w\>_2_u_, \(R\ge 4\), and log_R_=8_c_<sup>2</sup>+_O(c_) by (5).

### One round.

Given _w_<sup>3</sup> products of _G<sub>L,L</sub>_ with square coefficient matrices of side _w_<sup>2</sup>_Rn_, put

\(t=\left\lceil\frac{3L-1}{c-1}\right\rceil,L'=L+t\le\rho L+1.\)

The condition \(ct\ge a+2b-1\) holds both at (_a,b_)=(_L,L_) and at \((L',L)\), since \((c-1)t\ge 3L-1\). Theorem 2.9 and Lemma 3.1 first reduce the _w_<sup>3</sup> given products to \(\alpha^3\) products of \(G_{L,L^\prime}\) at matrix side _wuRn_. Use Lemma 3.2 to replace each by \(G_{L^\prime,L}\), permuting its coefficient lists and undoing the output permutation when decoding.

Since \(\alpha<2w\), put these products into eight batches of _w_<sup>3</sup>, padding with zero inputs. Apply the same packing to each batch. This gives at most \(8\alpha^3<64w^3\) products of \(G_{L^\prime,L^\prime}\) at matrix side \(u^2Rn\le w^2n\). Pad to side _w_<sup>2</sup>_n_ and to 64_w_<sup>3</sup> products. Lemma 2.2 composes the two steps modulo one parameter. Thus a round divides the matrix side by _R_, multiplies the product count by at most 64, and changes _L_ to at most \(\rho L+1\).

### Iteration.

Start one matrix product of side _v<sub>k</sub>=w_<sup>2</sup>_R<sup>k</sup>_ in a list of _w_<sup>3</sup> products of _G_<sub>1,1</sub>, with zero inputs in the other positions. After _k_ rounds there are at most _w_<sup>3</sup>64_<sup>k</sup>_ products of _G<sub>L<sub>k</sub>,L<sub>k</sub></sub>_ at matrix side _w_<sup>2</sup>, where<tbc>

\(L_0=1,L_k\le\rho^k+\frac{\rho^k-1}{\rho-1}=O_c(\rho^k).\)

<tbc>Finish each using Lemma 3.3, and compute the remaining fixed-size matrix products by the elementary algorithm. Repeated use of Lemma 2.2 gives a packing modulo \(\varepsilon\) for the original matrix product with at most<tbc>

\(r_k=O_c\big((64\rho^{6d})^k\big)\)


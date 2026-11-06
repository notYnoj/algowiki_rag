\(\blacktriangleright\) **Observation 3.3.** _Any submatrix_ \(A'\) _(not necessarily contiguous) of a Monge matrix A is Monge._

**Proof.** By Observation 2.2, if _A_ is Monge, the Monge property holds for every (not necessarily contiguous) \(2\times 2\) submatrix of _A_. In particular, it holds for contiguous \(2\times 2\) submatrices of \(A'\), and thus \(A'\) satisfies Definition 2.1. \(\blacktriangleleft\)

We next show a crucial property of the witness matrix.

\(\blacktriangleright\) **Lemma 3.4** (\[52, Theorem 1\])**.** _For any two Monge matrices, A of size_ \(p\times q\) _and B of size_ \(q\times r\)_, the witness matrix_ W_<sup>A,B</sup> is non-decreasing by rows and columns._

**Proof.** We prove that W_<sup>A,B</sup>_ is non-decreasing by columns. The claim for rows is analogous. Fix some \(i\in[0..p-1)\) and \(k\in[0..r)\). Let \(j^*:=\mathcal{W}_{i,k}^{A,B}\) and \(j\in[0..j^*)\). As _j_<sup>∗</sup> is the smallest witness for (_i,k_), we have _A<sub>i,j</sub>+B<sub>j,k</sub>\>A<sub>i,j<sup>∗</sup></sub>+B<sub>j<sup>∗</sup>,k</sub>_. Using this fact and the Monge property for _A_, we derive

\(A_{i+1,j}+B_{j,k}\ge(A_{i,j}+A_{i+1,j^*}-A_{i,j^*})+B_{j,k}\)<br>
\(=(A_{i,j}+B_{j,k})+(A_{i+1,j^*}-A_{i,j^*})\)<br>
\(>(A_{i,j^*}+B_{j^*,k})+(A_{i+1,j^*}-A_{i,j^*})\)<br>
\(=A_{i+1,j^*}+B_{j^*,k}.\)

Since _A_<sub>_i_+1_,j_</sub>+_B<sub>j,k</sub>\>A_<sub>_i_+1_,j_<sup>∗</sup></sub>+_B<sub>j<sup>∗</sup>,k</sub>_ for all \(j\in[0..j^*)\), we conclude that \(\mathcal{W}_{i+1,k}^{A,B}\ge j^*=\mathcal{W}_{i,k}^{A,B}\) holds as required. \(\blacktriangleleft\)

We now show how to bound \(\delta^\Sigma(A\otimes B)\) in terms of \(\delta^\Sigma(A)\) and \(\delta^\Sigma(B)\).

\(\blacktriangleright\) **Lemma 3.5.** _Let A be a_ \(p\times q\) _Monge matrix, and let B be a_ \(q\times r\) _Monge matrix. Then,_ \(\delta^\Sigma(A\otimes B)\le min\{\delta^\Sigma(A),\delta^\Sigma(B)\}\).

**Proof.** Let \(C:=A\otimes B\). Denote \(j:=\mathcal{W}_{0,0}^{A,B}\) and \(j':=\mathcal{W}_{p-1,r-1}^{A,B}\), where \(j\le j'\) due to Lemma 3.4. We have _C_<sub>0,0</sub>=_A_<sub>0_,j_</sub>+_B_<sub>_j,_0</sub> and \(C_{p-1,r-1}=A_{p-1,j^\prime}+B_{j^\prime,r-1}\). Furthermore, \(C_{p-1,0}\le A_{p-1,j}+B_{j,0}\) and \(C_{0,r-1}\le A_{0,j^\prime}+B_{j^\prime,r-1}\) due to the definition of _C_. Hence, due to Observation 3.1, we obtain

\(\delta^\Sigma(C)=C_{p-1,0}+C_{0,r-1}-C_{0,0}-C_{p-1,r-1}\)<br>
\(\le(A_{p-1,j}+B_{j,0})+(A_{0,j^\prime}+B_{j^\prime,r-1})-(A_{0,j}+B_{j,0})-(A_{p-1,j^\prime}+B_{j^\prime,r-1})\)<br>
\(=A_{p-1,j}+A_{0,j^\prime}-A_{0,j}-A_{p-1,j^\prime}\)<br>
\(=\delta^\Sigma(A[0..p)[j..j'])\)<br>
\(\le\delta^\Sigma(A).\)

The inequality \(\delta^\Sigma(C)\le\delta^\Sigma(B)\) can be obtained using a symmetric argument. \(\blacktriangleleft\)

The following corollary says that every core element of \(A\otimes B\) can be attributed to at least one core element of _A_ and at least one core element of _B_.

\(\blacktriangleright\) **Corollary 3.6.** _Let A be a_ \(p\times q\) _Monge matrix, let B be a_ \(q\times r\) _Monge matrix, and let_ \(C:=A\otimes B\)_. Consider integers_ \(i\in[0..p-1)\) _and_ \(k\in[0..r-1)\) _such that_ \(C_{i,k}^\square\neq 0\)_. There exist integers_ \(j_A,j_B\in[\mathcal{W}_{i,k}^{A,B}..\mathcal{W}_{i+1,k+1}^{A,B})\) _such that_ \(A_{i,j_A}^\square\neq 0\) _and_ \(B_{j_B,k}^\square\neq 0\).


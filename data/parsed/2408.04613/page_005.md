\(\blacktriangleright\) **Definition 2.3.** _The_ min-plus product _of a matrix A of size_ \(p\times q\) _and a matrix B of size_ \(q\times r\) _is a matrix_ \(A\otimes B=C\) _of size_ \(p\times r\) _satisfying_ \(C_{i,k}=min_{j\in[0..q)}A_{i,j}+B_{j,k}\) _for all_ \(i\in[0..p)\) _and_ \(k\in[0..r)\).

_For_ \(i\in[0..p)\) _and_ \(k\in[0..r)\)_, we call_ \(j\in[0..q)\) _a witness of C<sub>i,k</sub> if and only if C<sub>i,k</sub>=A<sub>i,j</sub>+B<sub>j,k</sub>. We define the_ \(p\times r\) _witness matrix W<sup>A,B</sup> such that_ \(\mathcal{W}_{i,k}^{A,B}\) _is the smallest witness of C<sub>i,k</sub> for each_ \(i\in[0..p)\) _and_ \(k\in[0..r)\).

The min-plus product of two Monge matrices is also Monge; we include a simple proof in Appendix A for completeness.

\(\blacktriangleright\) **Fact 2.4** (\[52, Corollary A\])**.** _Let A,B, and C be matrices such that_ \(A\otimes B=C\)_. If A and B are Monge, then C is also Monge._

In the context of Monge matrices, it is useful to define the core and the density matrix.

\(\blacktriangleright\) **Definition 2.5.** _The_ density matrix _of a matrix A of size_ \(p\times q\) _is a matrix_ \(A^\square\) _of size_ \((p-1)\times(q-1)\) _satisfying_ \(A_{i,j}^\square=A_{i,j+1}+A_{i+1,j}-A_{i,j}-A_{i+1,j+1}\) _for_ \(i\in[0..p-1),j\in[0..q-1)\).

_We define the_ core _of the matrix A as_

\(core(A):=\{(i,j,A_{i,j}^\square)|i\in[0..p-1),j\in[0..q-1),A_{i,j}^\square\neq 0\}\)

_and denote the_ core size _of the matrix A by_ \(\delta(A):=|core(A)|\)_. Furthermore, we define the_ core sum _of the matrix A as the sum of the values of all core elements of A, that is,_

\(\delta^\Sigma(A):=\sum_{i\in[0..p-1)}\sum_{j\in[0..q-1)}A_{i,j}^\square.\)

Note that, for a Monge matrix _A_, all entries of its density matrix are non-negative, and thus core(_A_) consists of triples (_i,j,v_) with some positive values _v_.

For any matrix _A_ of size \(p\times q\) and integers \(0\le a<b\le p\) and \(0\le c<d\le q\), we write _A[a..b_][_c..d_) to denote the contiguous submatrix of _A_ consisting of all entries on the intersection of rows [_a..b_) and columns [_c..d_) of _A_. Matrices _A[a..b_][_c..d_], _A(a..b_][_c..d_), etc., are defined analogously.

## 3 Properties of \(\delta\) and \(\delta^\Sigma\)

In this section, we provide some useful properties of \(\delta\) and \(\delta^\Sigma\). Most importantly, we show how to bound \(\delta(A\otimes B)\) in terms of \(\delta(A)\) and \(\delta(B)\).

The following observation is a straightforward consequence of the definitions of \(\delta^\Sigma\) and \(A^\square\).

\(\blacktriangleright\) **Observation 3.1.** _For a matrix A of size_ \(p\times q\)_, and integers_ \(0\le a\le b<p\) _and_ \(0\le c\le d<q\),

\(A_{a,c}+A_{b,d}+\delta^\Sigma(A[a..b][c..d])=A_{a,d}+A_{b,c}.\)

**Proof.** By the definition of \(A^\square\), we have \(A_{i,j}+A_{i+1,j+1}+A_{i,j}^\square=A_{i,j+1}+A_{i+1,j}\) for all \(i\in[a..b)\) and \(j\in[c..d)\). The desired equality follows by summing up all these equalities.

An application of Observation 3.1 for _a=c_=0 implies that every value of _A_ can be uniquely reconstructed from _A_’s core and the values in the topmost row and the leftmost column of _A_.

\(\blacktriangleright\) **Definition 3.2.** _The_ condensed representation _of a matrix A consists of the core of A as well as the values in the topmost row and the leftmost column of A._


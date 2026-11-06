**Lemma 2.6** (Generalized Laplace expansion)**.** _Let A be an_ \(n\times n\) _matrix and let its rows be partitioned into k contiguous blocks R_<sub>1</sub>_,...,R<sub>k</sub> of sizes r_<sub>1</sub>_,...,r<sub>k</sub> with_ \(\sum_ir_i=n\)_. Then_

\(det(A)=\sum_{S_1\unknown\cdots\unknown S_k=[n]|S_i|=r_i}(-1)^{\sigma(S_1,\dots,S_k)}\prod_{i=1}^kdet(A_{R_i,S_i}),\)

_where the sum is taken over all ordered partitions of the columns_ \[_n_\] _into blocks_ \(S_1\unknown\cdots\unknown S_k\) _with_ |_S<sub>i</sub>_|=_r<sub>i</sub>, and_ \((-1)^{\sigma(S_1,\dots,S_k)}\) _is the sign of the permutation that reorders_ \[_n_\] _into_ (_S_<sub>1</sub>_,...,S<sub>k</sub>)._

We finally state the Schwartz-Zippel lemma which will be useful in providing high probability success bounds for our algorithms.

**Lemma 2.7** (Schwartz-Zippel lemma)**.** _Let P(x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>N</sub>_) _be a non-zero polynomial of degree d over a finite field_ F_. If a point is selected uniformly at random from_ F_<sup>N</sup>, then the probability that P evaluates to a non-zero value is at least_ 1-_d/_|F|.

In this paper, we shall work with finite fields. Thus |F| will be _p<sup>r</sup>_, for some prime _p_ and integer \(r\ge 1\). We will be working with fields representable in _O_(log_n_) bits. This would support addition and multiplication over F in constant time in the Word-RAM model.

## Matroid Terminology

We next briefly review standard matroid terminology.

**Definition 2.8** (Matroid)**.** _A_ matroid _M_=(_E,_I) _consists of a finite ground set E and a collection_ I _of subsets of E, called_ independent sets, _satisfying three properties:_

1. \(\emptyset\in\mathcal{I}\) ;<tbc>

2. _if_ \(I\in\mathcal{I}\) _and_ \(I'\subseteq I\)_, then_ \(I'\in\mathcal{I}\) _; and_<tbc>

_3._ _if_ \(I_1,I_2\in\mathcal{I}\) _with_ |_I_<sub>1</sub>|_\<|I_<sub>2</sub>|_, there exists an element_ \(e\in I_2\backslash I_1\) _such that_ \(I_1\cup\{e\}\in\mathcal{I}\) .

**Definition 2.9** (Basis)**.** _A_ basis _of M is a maximal independent set. It is well known that all bases of M have the same cardinality, known as the_ rank _of the matroid, denoted r(M_) _(or simply r if M is clear from the context). We denote the set of all bases of M by_ B(_M)._

**Definition 2.10** (Linear Matroid)**.** _A matroid M_=(_E,_I) _on a ground set E of size m is said to be_ linear _if there exists a_ \(d\times m\) _matrix A over_ F _such that_ \(S\subseteq E\) _is independent iff the sub-matrix A<sub>S</sub> (columns of A indexed by S) has full column rank in_ F_. If the rank of M is r, we can assume without loss of generality that d=r._

Note that for any linear matroid _M_ of size _m_ and rank _r_ it is possible to produce a linear representation matrix _A_ of size \(r\times m\). Clearly, for such a representation _A_, any basis \(S\in\mathcal{B}(M)\) satisfies \(det(A_S)\neq 0\).

**Definition 2.11** (Sparse Linear Matroid)**.** _A linear matroid M is said to be c_-sparse _(or c_-column- sparse) _if there exists a representation matrix A for M over a field_ F _such that every column of A contains at most c non-zero entries. For convenience, we refer to the matrix as just_ sparse _if c=O_(1).

Matroids arising from graphs (such as graphic or partition matroids) naturally admit sparse representations, as their elements map to edges with constant-sized incidence bounds. We next define the notion of strongly base-orderable matroids.

